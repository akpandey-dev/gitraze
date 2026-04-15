# config.py

'''=============REST=============='''

# --- BASE CONFIGS ---
REST_BASE_URL = "https://api.github.com"
GRAPHQL_URL = "https://api.github.com/graphql"
DEFAULT_TIMEOUT = 10
DEFAULT_HEADERS = {
    "Accept": "application/vnd.github+json"
}

# --- USER CONFIG ---


# --- REPO CONFIG ---


# --- SEARCH CONFIG ---
SEARCH_MAP = {
    "repos": "repositories",
    "users": "users",
    "issues": "issues",
    "topics": "topics",
    "prs": "issues"
}


