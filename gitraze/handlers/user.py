import json
from gitraze.utils.helpers import file_save, pretty_print
from gitraze.modules.user import get_user_rest

def handle_user(args):
    """Handle the user CLI command."""

    print("[+] Fetching user data...")
    data = get_user_rest(args.username, data_format=args.data_format)

    if "error" in data:
        print(data["error"])
        return

    print("[✓] Done")
    
    if args.output_action == "save":
        file_save(data, f"{args.username}-data.json")
        return
    elif args.output_action == "display":
        if args.data_format == "raw":
            print(json.dumps(data, indent=2))
            return
        else:
            pretty_print(data, title=f"User: {args.username}")