from .modules.user import get_user_rest as user
from .modules.repo import get_repo_rest as repo
from .modules.search import get_search_rest as search

from .utils.helpers import display
from .utils.helpers import save
from .utils.helpers import output_action

__version__ = "0.5.0"

USERS = "users"
REPOS = "repos"
PRS = "prs"
ISSUES = "issues"
TOPICS = "topics"

__all__ = [
    "output_action",
    "display",
    "save",
    "user",
    "repo",
    "search",
    "USERS",
    "REPOS",
    "PRS",
    "ISSUES",
    "TOPICS",
]