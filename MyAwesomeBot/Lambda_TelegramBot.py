import os
import json
import logging
import asyncio
import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)


# 1. Logger setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 2. Environment variables (best practice: store secrets, keys in Lambda env vars)
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    logger.error("TELEGRAM_TOKEN is not set! Please configure the environment variable.")

OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")

if not OPENWEATHER_API_KEY:
    logger.warning("OPENWEATHER_API_KEY is not set. The /weather command may fail.")


# ====== Your Handler Functions (converted to async) ====== #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Handling /start command from user=%s", update.effective_user.id)
    await update.message.reply_text(
        "Hello! I am your multi-functional bot. Type /help to see what I can do!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Here are some commands you can try:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/joke - Get a random joke\n"
        "/weather [city] - Get the current weather in a city\n"
        "/calc [expression] - Simple calculator\n"
        "/time - Get the current time\n"
        "/echo [text] - I'll repeat your message"
    )

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke_data = response.json()
        setup = joke_data["setup"]
        punchline = joke_data["punchline"]
        await update.message.reply_text(f"{setup}\n\n{punchline} 😂")
    else:
        await update.message.reply_text("Oops! Couldn't fetch a joke right now.")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Please provide a city name. Example: /weather London")
        return

    city = ' '.join(context.args)
    # Use environment variable for your OpenWeatherMap API key
    api_key = OPENWEATHER_API_KEY
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        await update.message.reply_text(f"Weather in {city}: {description}, Temperature: {temp}°C")
    else:
        error_message = response.json().get("message", "")
        if "city not found" in error_message.lower():
            await update.message.reply_text(f"City '{city}' not found. Please check the city name.")
        elif response.status_code == 401:
            await update.message.reply_text("Invalid API Key. Please check your OpenWeatherMap API key.")
        else:
            await update.message.reply_text(f"An error occurred: {error_message}")


application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("joke", joke))
application.add_handler(CommandHandler("weather", weather))

async def inline_init_and_process(update):
    await application.process_update(update)

        
# ====== Lambda entry point ======
def lambda_handler(event, context):
    """
    The main Lambda function that AWS calls whenever your API Gateway endpoint is invoked.
    It receives a JSON 'event' dict, which for HTTP API v2 includes 'requestContext.http.method'
    and a 'body' with Telegram's update data, plus 'context' for Lambda runtime info.
    """

    logger.info("***** LAMBDA HANDLER START, event = %s", event)

    # For HTTP API v2, the HTTP method is in event["requestContext"]["http"]["method"]
    # We'll retrieve it safely to avoid KeyErrors if the keys don't exist.
    method = event.get("requestContext", {}).get("http", {}).get("method", "")

    # We also check if 'body' is present (which holds Telegram's JSON update).
    if method == "POST" and "body" in event:
        try:
            # 'body' is the raw JSON string from Telegram's webhook
            body = event["body"]
            # Convert JSON string to a Python dict
            update_dict = json.loads(body)
            # Turn that dict into a python-telegram-bot Update object
            update = Update.de_json(update_dict, application.bot)
                        
            loop = asyncio.get_event_loop()
            
            # NOTE(oleg): start if not started, do nothing otherwise
            if not application.running:
                logger.info("Starting application")
                loop.run_until_complete(application.initialize())
                loop.run_until_complete(application.start())
            else:
                logger.info("Application already running")

            # process update and wait for completion
            loop.run_until_complete(application.process_update(update))

            # Return a 200 to tell Telegram "we processed this successfully"
            return {
                "statusCode": 200,
                "body": ""
            }

        except Exception as e:
            # If anything goes wrong (JSON parse, telegram send error), log it.
            logger.error("Error processing Telegram update", exc_info=True)

            # Return a 500 so Telegram knows we failed to process the update
            return {
                "statusCode": 500,
                "body": "Internal Server Error"
            }

    else:
        # If it's not a POST request or doesn't have 'body',
        # we likely received a GET or some other request (health checks, etc.).
        logger.info("Not a POST or no body in event")
        return {
            # FIXME(oleg): probably should be a bad request, 400
            "statusCode": 200,
            "body": "Not a POST or no body in event"
        }
