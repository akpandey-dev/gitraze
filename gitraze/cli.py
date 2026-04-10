import argparse
from gitraze.utils.helpers import pretty_print
from gitraze.modules.user import get_user


def main():
    parser = argparse.ArgumentParser(
        prog="gitraze",
        description="GitRaze CLI Tool"
    )

    # Global flag
    parser.add_argument(
        "--version",
        action="version",
        version="gitraze 0.0.1"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- USER ---
    user_parser = subparsers.add_parser("user", help="Fetch user info (GitHub username)")
    user_parser.add_argument("username")

    # --- REPO ---
    repo_parser = subparsers.add_parser("repo", help="Fetch repo info (Repository in owner/repo format)")
    repo_parser.add_argument("repo")

    # --- SEARCH ---
    search_parser = subparsers.add_parser("search", help="Search GitHub")
    search_parser.add_argument("query", nargs="+")

    # --- ANALYZE ---
    analyze_parser = subparsers.add_parser("analyze", help="Analyze target")
    analyze_parser.add_argument("target", nargs="+")

    args = parser.parse_args()

    # --- ROUTING ---
    if args.command == "user":
        handle_user(args)
    elif args.command == "repo":
        handle_repo(args)
    elif args.command == "search":
        handle_search(args)
    elif args.command == "analyze":
        handle_analysis(args)
    else:
        parser.print_help()


# --- HANDLERS  ---

def handle_user(args):
    data = get_user(args.username)

    if "error" in data:
        print(data["error"])
        return

    pretty_print(data, title=f"User: {args.username}")


def handle_repo(args):
    print(f"[REPO] Fetching data for {args.repo}")
    print("Not implemented yet")


def handle_search(args):
    query = " ".join(args.query)
    print(f"[SEARCH] Searching for '{query}'")
    print("Not implemented yet")


def handle_analysis(args):
    target = " ".join(args.target)
    print(f"[ANALYZE] Analyzing '{target}'")
    print("Not implemented yet")