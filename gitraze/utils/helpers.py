# helpers.py
from colorama import Fore, Style, init

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