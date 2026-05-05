import argparse
from gitraze.utils.helpers import pretty_print
from gitraze.modules.user import get_user_rest
from gitraze.modules.repo import get_repo_rest
from gitraze.modules.search import get_search_rest


def main():
    parser = argparse.ArgumentParser(
        prog="gitraze",
        description="GitRaze CLI Tool"
    )

    # Global flag
    parser.add_argument(
        "--version",
        action="version",
        version="gitraze 0.2.3"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- USER ---
    user_parser = subparsers.add_parser("user", help="Fetch user info (GitHub username)")
    user_parser.add_argument("username", help="Format: username")

    # --- REPO ---
    repo_parser = subparsers.add_parser("repo", help="Fetch repo info (Repository in owner/repo format)")
    repo_parser.add_argument("repo", help="Format: owner/repo")

    # --- SEARCH ---
    search_parser = subparsers.add_parser("search", help="Search GitHub")
    search_parser.add_argument("category",choices=["repos", "users", "issues", "prs", "topics"],help="repos | users | issues | prs | topics")
    search_parser.add_argument("query", nargs="+", help="Search category (repos, users, issues, topics)")
    search_parser.add_argument("-n", "--limit", type=int, default=1, help="Number of results to show")

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
    print("[+] Fetching user data...")
    data = get_user_rest(args.username)

    if "error" in data:
        print(data["error"])
        return

    print("[✓] Done")
    pretty_print(data, title=f"User: {args.username}")


def handle_repo(args):
    print("[+] Fetching repository data...")
    parts = args.repo.split("/")
    
    if len(parts) != 2:
        print("Invalid format. Use: owner/repo")
        return
    owner, repo = parts
    data = get_repo_rest(owner, repo)

    if "error" in data:
        print(data["error"])
        return

    print("[✓] Done")
    pretty_print(data, title=f"User: {owner}, Repository: {repo}")


def handle_search(args):
    category = args.category

    raw_query = " ".join(args.query)
    clean_query = raw_query.replace('"', '')
    query = f'"{clean_query}"'

    print(f"[+] Searching {category} for {query}...")


    data = get_search_rest(category, query, args.limit)

    if "error" in data:
        print(data["error"])
        return

    print("[✓] Done")

    if isinstance(data, list):
        for i, item in enumerate(data, 1):
            pretty_print(item, title=f"{category} [{i}] -> {query}")
    else:
        pretty_print(data, title=f"Search: {category} -> {query}")


def handle_analysis(args):
    target = " ".join(args.target)
    print(f"[ANALYZE] Analyzing '{target}'")
    print("Not implemented yet")