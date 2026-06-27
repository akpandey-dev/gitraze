import json
from gitraze.utils.helpers import pretty_print
from gitraze.modules.user import get_user_rest

def handle_user(args):
    print("[+] Fetching user data...")
    data = get_user_rest(args.username, output_format=args.format)

    if "error" in data:
        print(data["error"])
        return

    print("[✓] Done")
    
    if args.format == "raw":
        print(json.dumps(data, indent=2))
        return

    pretty_print(data, title=f"User: {args.username}")