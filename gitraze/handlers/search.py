from gitraze.utils.helpers import pretty_print
from gitraze.modules.search import get_search_rest

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