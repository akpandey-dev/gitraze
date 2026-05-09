from .modules.user import get_user_rest as user
from .modules.repo import get_repo_rest as repo
from .modules.search import get_search_rest as search

from .utils.helpers import pretty_print as display

__version__ = "0.2.5"

USERS = "users"
REPOS = "repos"
PRS = "prs"
ISSUES = "issues"
TOPICS = "topics"

__all__ = [
    "display",
    "user",
    "repo",
    "search",
    "USERS",
    "REPOS",
    "PRS",
    "ISSUES",
    "TOPICS",
]