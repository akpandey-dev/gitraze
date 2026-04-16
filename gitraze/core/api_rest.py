# api_rest.py
import requests
from gitraze.config import REST_BASE_URL, DEFAULT_HEADERS, DEFAULT_TIMEOUT
from gitraze.config import SEARCH_MAP

def get_user(username):
    url = f"{REST_BASE_URL}/users/{username}"

    try:
        response = requests.get(
            url,
            headers=DEFAULT_HEADERS,
            timeout=DEFAULT_TIMEOUT
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Check your connection."}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


def get_repo(owner, repo):
    url = f"{REST_BASE_URL}/repos/{owner}/{repo}"
    try:
        response = requests.get(
            url,
            headers=DEFAULT_HEADERS,
            timeout=DEFAULT_TIMEOUT
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Check your connection."}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    
def get_search(category, query):
    url = f"{REST_BASE_URL}/search/{SEARCH_MAP.get(category)}"
    filters = []
    if category == "prs":
        filters.append("type:pr")
    elif category == "issues":
        filters.append("type:issue")

    filters.extend([
        "in:title",
        "comments:1..50",
        "-author:app",
    ])

    final_query = f"{query} {' '.join(filters)}"
    params = {
        "q": final_query,
        "per_page": 100,
        "sort": "comments",
        "order": "desc"
    }

    try:
        response = requests.get(
            url,
            headers=DEFAULT_HEADERS,
            params=params,
            timeout=DEFAULT_TIMEOUT
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Check your connection."}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}