# search.py
from gitraze.utils.helpers import format_date 
from gitraze.utils.helpers import clean_html
from gitraze.core.api_rest import get_search


def get_search_rest(category, query,  limit=1):
    if category not in ["repos", "users", "issues", "prs", "topics"]:
        return {"error": "Invalid category"}
    data = get_search(category, query)
    if "error" in data:
        return data
    items = data.get("items", [])
    
    if category == "issues":
        items = [i for i in items if "pull_request" not in i]
    elif category == "prs":
        items = [i for i in items if "pull_request" in i]
        
    if not items:
        return {"error": "No results found"}
    items = items[:limit]
    results = []

    for item in items:
        match(category):
            case "repos":
                results.append({
                "full_name": item.get("full_name"),
                "html_url": item.get("html_url"),
                "description": clean_html(item.get("description")),
                "stargazers_count": item.get("stargazers_count"),
                "watchers_count": item.get("watchers_count"),
                "forks_count": item.get("forks_count"),
                "open_issues_count": item.get("open_issues_count"),
                "archived": item.get("archived"),
                "disabled": item.get("disabled"),
                "updated_at": format_date(item.get("updated_at")),
                "pushed_at": format_date(item.get("pushed_at")),
                "language": item.get("language"),
                "visibility": item.get("visibility"),
                "default_branch": item.get("default_branch"),
                "owner": item.get("owner", {}).get("login"),
                "For More, use": "$ gitraze repo <owner/repo>"
            })

            case "users":
                results.append({
                "login": item.get("login"),
                "html_url": item.get("html_url"),
                "type": item.get("type"),
                "score": item.get("score"),
                "site_admin": item.get("site_admin"),
                "repos_url": item.get("repos_url"),
                "followers_url": item.get("followers_url"),
                "following_url": item.get("following_url"),
                "organizations_url": item.get("organizations_url"),
                "For More, use": "$ gitraze user <username>"
            })

            case "issues":
                results.append({
                "title": item.get("title"),
                "html_url": item.get("html_url"),
                "state": item.get("state"),
                "number": item.get("number"),
                "comments": item.get("comments"),
                "created_at": format_date(item.get("created_at")),
                "updated_at": format_date(item.get("updated_at")),
                "closed_at": format_date(item.get("closed_at")),
                "user": item.get("user", {}).get("login"),
                "repository_url": item.get("repository_url"),
                "labels": [label.get("name") for label in item.get("labels", [])]
            })
            case "prs":
                 results.append({
                "title": item.get("title"),
                "html_url": item.get("html_url"),
                "state": item.get("state"),
                "number": item.get("number"),
                "comments": item.get("comments"),
                "created_at": format_date(item.get("created_at")),
                "updated_at": format_date(item.get("updated_at")),
                "closed_at": format_date(item.get("closed_at")),
                "merged_at": format_date(item.get("pull_request", {}).get("merged_at")),
                "user": item.get("user", {}).get("login"),
                "repository_url": item.get("repository_url"),
                "labels": [label.get("name") for label in item.get("labels", [])],
                "draft": item.get("draft"),
                "pr_url": item.get("pull_request", {}).get("html_url")
            })
        
            case "topics":
                 results.append({
                "name": item.get("name"),
                "display_name": item.get("display_name"),
                "short_description": clean_html(item.get("short_description")),
                "description": clean_html(item.get("description")),
                "score": item.get("score"),
                "created_by": item.get("created_by"),
                "released": item.get("released"),
                "created_at": format_date(item.get("created_at")),
                "featured": item.get("featured")
            })

    return results

