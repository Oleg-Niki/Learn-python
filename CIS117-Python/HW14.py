# Homework 14 Assignment
# Oleg Nikitashin
# April 29, 2025 due  23:59
# This program scrapes the College of San Mateo website for email addresses

import re
from html.parser import HTMLParser
from urllib.request import urlopen
import tkinter as tk
from tkinter import scrolledtext

# URL to scrape for emails
URL = 'https://collegeofsanmateo.edu/wellnesscenter'

class EmailHTMLParser(HTMLParser):
    """
    Subclass of HTMLParser to parse HTML and extract email addresses
    using regular expressions.
    """
    def __init__(self):
        super().__init__()
        self.emails = set()

    def handle_data(self, data):
        """Extract emails from text data using re."""
        email_pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}'
        if re.search(email_pattern, data):
            found_emails = re.findall(email_pattern, data)
            self.emails.update(found_emails)

    def collect_emails(self):
        """Returns collected emails."""
        return '\n'.join(sorted(self.emails))

def fetch_emails(url):
    """Fetch HTML content and parse emails from it."""
    response = urlopen(url)
    html_page = response.read().decode()
    parser = EmailHTMLParser()
    parser.feed(html_page)
    return parser.collect_emails()

# GUI Part using Tkinter
def create_gui():
    """Create GUI to display email addresses."""
    window = tk.Tk()
    window.title("CSM Email Scraper")
    window.geometry('600x400')

    # Personalized GUI appearance
    window.configure(bg='#e6f2ff')

    tk.Label(window, text="Enter URL:", font=("Helvetica", 14), bg='#e6f2ff').grid(row=0, column=0, pady=10, padx=5, sticky='w')

    url_entry = tk.Entry(window, width=50, font=("Arial", 12))
    url_entry.grid(row=1, column=0, pady=5, padx=5, sticky='w')
    url_entry.insert(0, URL)  # Default URL provided

    submit_btn = tk.Button(window, text="SUBMIT", font=("Arial", 12), bg='blue', fg='white',
                           command=lambda: click())
    submit_btn.grid(row=2, column=0, pady=10, padx=5, sticky='w')

    output = scrolledtext.ScrolledText(window, width=75, height=15, wrap=tk.WORD, font=("Consolas", 10))
    output.grid(row=3, column=0, pady=10, padx=5, sticky='w')

    def click():
        """Fetch and display emails based on user-input URL."""
        url = url_entry.get()
        emails = fetch_emails(url)
        output.delete('1.0', tk.END)
        if emails:
            output.insert(tk.END, emails)
        else:
            output.insert(tk.END, "No emails found.")

    window.mainloop()

if __name__ == '__main__':
    create_gui()
