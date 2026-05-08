from gitraze.utils.helpers import pretty_print
from gitraze.modules.user import get_user_rest

def handle_user(args):
    print("[+] Fetching user data...")
    data = get_user_rest(args.username)

    if "error" in data:
        print(data["error"])
        return

    print("[✓] Done")
    pretty_print(data, title=f"User: {args.username}")