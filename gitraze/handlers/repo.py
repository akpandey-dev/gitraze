from gitraze.utils.helpers import pretty_print
from gitraze.modules.repo import get_repo_rest

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