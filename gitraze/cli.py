import sys
from gitraze.utils.helpers import pretty_print
from gitraze.modules.user import get_user


def main():
    args = sys.argv[1:]

    if not args:
        print("Gitraze CLI")
        print("Usage: gitraze <command> [options]")
        return

    command = args[0]

    if command == "user":
        handle_user(args[1:])
    elif command == "repo":
        handle_repo(args[1:])
    elif command == "search":
        handle_search(args[1:])
    else:
        print(f"Unknown command: {command}")


# --- COMMAND HANDLERS ---

from gitraze.modules.user import get_user

def handle_user(args):
    username = args[0]
    data = get_user(username)

    if "error" in data:
        print(data["error"])
        return

    pretty_print(data, title=f"User: {username}")


def handle_repo(args):
    if not args:
        print("Usage: gitraze repo <owner/repo>")
        return

    repo = args[0]
    print(f"[REPO] Fetching data for {repo}")
    print("Not implemented yet")


def handle_search(args):
    if not args:
        print("Usage: gitraze search <query>")
        return

    query = " ".join(args)
    print(f"[SEARCH] Searching for '{query}'")
    print("Not implemented yet")