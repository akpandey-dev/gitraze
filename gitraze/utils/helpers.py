# helpers.py
from datetime import datetime
import json
from colorama import Fore, Style, init
import re

init(autoreset=True)


def pretty_print(data, title=None):
    """Print dictionary data as formatted key-value pairs."""

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
    """Display dictionary or list data in a formatted terminal layout."""
    
    if isinstance(data, list):

        if not data:
            print(Fore.RED + "No results found")
            return

        for i, item in enumerate(data, 1):
            item_title = f"{title} [{i}]" if title else f"Result [{i}]"
            pretty_print(item, title=item_title)

        return

    pretty_print(data, title=f"Result: ")

def file_save(data, title=None):
    """Save dictionary data as JSON file."""

    filename = title if title else "file.txt"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def save(data, title=None):
    """Save dictionary or list data as JSON files."""
    
    if isinstance(data, list):
        for i, item in enumerate(data, 1):
            filename = f"{title}-{i}.json" if title else f"gitraze-data-{i}.json"
            file_save(item, filename)
    else:
        filename = f"{title}.json" if title else "gitraze-data.json"
        file_save(data, filename)

def output_action(action, data, title=None):
    """Perform the specified output action (display or save) on the data."""
    
    if action == "display":
        display(data, title)
    elif action == "save":
        save(data, title)
    else:
        raise ValueError("Invalid action. Use 'display' or 'save'.")

def format_date(date_str):
    """Format a GitHub API date string for display."""

    if not date_str:
        return None

    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b %Y")
    except ValueError:
        return date_str  # fallback (don’t crash)

def clean_html(text):
    """Remove HTML tags from text."""

    return re.sub(r"<.*?>", "", text) if text else text

def normalize_api_data(data):
    """Normalize API data for human-readable output."""

    cleaned = {}
    for key, value in data.items():

        if key.endswith("_at") and isinstance(value, str):
            value = format_date(value)

        if isinstance(value, str):
            value = clean_html(value)

        cleaned[key] = value

    return cleaned