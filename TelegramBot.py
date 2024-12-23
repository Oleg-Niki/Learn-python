import os
import json
import logging
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

import requests # type: ignore
from datetime import datetime

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


# 3. Build the application globally
#    This ensures we only build once (better performance, fewer cold starts).
application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

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

# async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     response = requests.get("https://official-joke-api.appspot.com/random_joke")
#     if response.status_code == 200:
#         joke_data = response.json()
#         setup = joke_data["setup"]
#         punchline = joke_data["punchline"]
#         await update.message.reply_text(f"{setup}\n\n{punchline} 😂")
#     else:
#         await update.message.reply_text("Oops! Couldn't fetch a joke right now.")

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

# async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     if not context.args:
#         await update.message.reply_text("Please provide a math expression to evaluate. Example: /calc 2 + 2")
#         return

#     try:
#         expression = ' '.join(context.args)
#         result = eval(expression)
#         await update.message.reply_text(f"The result of {expression} is: {result}")
#     except Exception as e:
#         await update.message.reply_text(f"Error in calculation: {e}")

# async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     await update.message.reply_text(f"The current time is: {current_time}")

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user_text = ' '.join(context.args)
#     await update.message.reply_text(user_text)

# async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     for member in update.message.new_chat_members:
#         await update.message.reply_text(f"Welcome to the group, {member.full_name}! 🎉")

# Register all handlers ONCE (globally)
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
#application.add_handler(CommandHandler("joke", joke))
application.add_handler(CommandHandler("weather", weather))
# application.add_handler(CommandHandler("calc", calculate))
# application.add_handler(CommandHandler("time", time_command))
# application.add_handler(CommandHandler("echo", echo))
# application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

async def inline_init_and_process(update):
    # Initialize the application (sets up internal state).
    await application.initialize()
    # Start the application (connect signals, etc.).
    await application.start()
    try:
        # Process the actual update (/start, /help, etc.).
        await application.process_update(update)
    finally:
        # Stop the application gracefully.
        # This cleans up any sessions, open connections, etc.
        await application.stop()
        
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

                        
            # Immediately process the update in a synchronous manner
            # so Lambda doesn't exit before handlers run
            asyncio.run(inline_init_and_process(update))
                   

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
            "statusCode": 200,
            "body": "OK"
        }
