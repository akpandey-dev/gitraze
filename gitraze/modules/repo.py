# repo.py
from gitraze.utils.helpers import format_date 
from gitraze.utils.helpers import normalize_api_data
from gitraze.core.api_rest import get_repo as rest_get_repo

def get_repo_rest(owner, repo, data_format="compact"):
    """Fetch GitHub repository data in the requested data format.

    Args:
        owner: GitHub repository owner's username or organization name.
        repo: GitHub repository name.
        data_format: Data format: "compact", "full", or "raw".

    Returns:
        Repository data in the requested format, or an error dictionary.
    """
    
    data = rest_get_repo(owner, repo)

    if "error" in data:
        return data

    if data_format == "raw":
        return data
    if data_format == "full":
        return normalize_api_data(data)
        
    return {
        "name": data.get("name"),
        "full_name": data.get("full_name"),
        "owner": data.get("owner", {}).get("login"),
        "description": data.get("description"),
        "private": data.get("private"),
        "fork": data.get("fork"),
        "language": data.get("language"),
        "topics": data.get("topics"),
        "stars": data.get("stargazers_count"),
        "forks": data.get("forks_count"),
        "watchers": data.get("watchers_count"),
        "open_issues": data.get("open_issues_count"),
        "size": data.get("size"),
        "default_branch": data.get("default_branch"),
        "repo_url": data.get("html_url"),
        "clone_url": data.get("clone_url"),
        "created_at": format_date(data.get("created_at")),
        "updated_at": format_date(data.get("updated_at")),
        "pushed_at": format_date(data.get("pushed_at")),
        "license": data.get("license", {}).get("name") if data.get("license") else None,
    }