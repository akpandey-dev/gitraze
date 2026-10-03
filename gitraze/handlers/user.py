import json
from gitraze.utils.helpers import pretty_print
from gitraze.modules.user import get_user_rest

def handle_user(args):
    """Handle the user CLI command."""

    print("[+] Fetching user data...")
    data = get_user_rest(args.username, data_format=args.data_format)

    if "error" in data:
        print(data["error"])
        return

    print("[✓] Done")
    
    if args.data_format == "raw":
        print(json.dumps(data, indent=2))
        return

    pretty_print(data, title=f"User: {args.username}")