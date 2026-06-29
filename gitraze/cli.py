import argparse
from gitraze.handlers.user import handle_user
from gitraze.handlers.repo import handle_repo
from gitraze.handlers.search import handle_search
from gitraze.handlers.analyze import handle_analysis


def main():
    parser = argparse.ArgumentParser(
        prog="gitraze",
        description="GitRaze CLI Tool"
    )

    # Global flag
    parser.add_argument(
        "--version",
        action="version",
        version="gitraze 0.3.0"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # USER 
    user_parser = subparsers.add_parser("user", help="Fetch user info (GitHub username)")
    user_parser.add_argument("username", help="Format: username")
    user_parser.add_argument("--format", choices=["compact", "full", "raw"], default="compact", help="Output format (default: compact)")
    user_parser.set_defaults(func=handle_user)


    # REPO 
    repo_parser = subparsers.add_parser("repo", help="Fetch repo info (Repository in owner/repo format)")
    repo_parser.add_argument("repo", help="Format: owner/repo")
    repo_parser.add_argument("--format", choices=["compact", "full", "raw"], default="compact", help="Output format (default: compact)")
    repo_parser.set_defaults(func=handle_repo)


    # SEARCH 
    search_parser = subparsers.add_parser("search", help="Search GitHub")
    search_parser.add_argument("category",choices=["repos", "users", "issues", "prs", "topics"],help="repos | users | issues | prs | topics")
    search_parser.add_argument("query", nargs="+", help="Search category (repos, users, issues, topics)")
    search_parser.add_argument("-n", "--limit", type=int, default=1, help="Number of results to show")
    search_parser.add_argument("--format", choices=["compact", "full", "raw"], default="compact", help="Output format (default: compact)")
    search_parser.set_defaults(func=handle_search)


    # ANALYZE 
    analyze_parser = subparsers.add_parser("analyze", help="Analyze target")
    analyze_parser.add_argument("target", nargs="+")
    analyze_parser.set_defaults(func=handle_analysis)

    args = parser.parse_args()
    args.func(args)




if __name__ == "__main__":
    main()






