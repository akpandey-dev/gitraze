import json
from gitraze.utils.helpers import file_save, pretty_print
from gitraze.modules.repo import get_repo_rest

def handle_repo(args):
    """Handle the repo CLI command."""

    print("[+] Fetching repository data...")
    parts = args.repo.split("/")
    
    if len(parts) != 2:
        print("Invalid format. Use: owner/repo")
        return
    owner, repo = parts
    data = get_repo_rest(owner, repo, data_format=args.data_format)

    if "error" in data:
        print(data["error"])
        return

    print("[✓] Done")

    if args.output_action == "save":
        file_save(data, f"{owner}-{repo}-data.json")
        return
    elif args.output_action == "display":
        if args.data_format == "raw":
            print(json.dumps(data, indent=2))
            return
        else:
            pretty_print(data, title=f"User: {owner}, Repository: {repo}")
