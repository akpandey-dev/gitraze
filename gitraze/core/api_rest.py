# api_rest.py
import requests
from gitraze.config import REST_BASE_URL, DEFAULT_HEADERS, DEFAULT_TIMEOUT


import requests

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
    response = requests.get(url, headers=DEFAULT_HEADERS, timeout=DEFAULT_TIMEOUT)

    if response.status_code != 200:
        return {"error": f"Failed to fetch repo: {response.status_code}"}

    return response.json()