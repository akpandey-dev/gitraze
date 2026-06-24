# helpers.py
from datetime import datetime
from colorama import Fore, Style, init
import re

init(autoreset=True)


def pretty_print(data, title=None):
    if not isinstance(data, dict):
        print(Fore.RED + "Invalid data format")
        return

    # Title
    if title:
        print(Fore.CYAN + Style.BRIGHT + f"\n{title}")
        print(Fore.CYAN + "-" * len(title))

    # Calculate max key length for alignment
    max_key_len = max(len(str(key)) for key in data.keys())

    # Print key-value pairs
    for key, value in data.items():
        key_str = f"{key.capitalize():<{max_key_len}}"
        print(
            Fore.YELLOW + key_str +
            Fore.WHITE + " : " +
            Fore.GREEN + str(value)
        )

    print()  # spacing

def display(data, title=None):

    if isinstance(data, list):

        if not data:
            print(Fore.RED + "No results found")
            return

        for i, item in enumerate(data, 1):

            item_title = f"{title} [{i}]" if title else f"Result [{i}]"

            pretty_print(item, title=item_title)

        return

    pretty_print(data, title=f"Result: ")

def format_date(date_str):
    if not date_str:
        return None

    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b %Y")
    except ValueError:
        return date_str  # fallback (don’t crash)

def clean_html(text):
    return re.sub(r"<.*?>", "", text) if text else text

def normalize_api_data(data):
    cleaned = {}

    for key, value in data.items():

        if key.endswith("_at") and isinstance(value, str):
            value = format_date(value)

        if isinstance(value, str):
            value = clean_html(value)

        cleaned[key] = value

    return cleaned