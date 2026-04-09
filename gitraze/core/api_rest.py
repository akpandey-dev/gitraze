# api_rest.py
import requests
from gitraze.config import REST_BASE_URL, DEFAULT_HEADERS, DEFAULT_TIMEOUT


def get_user(username):
    url = f"{REST_BASE_URL}/users/{username}"
    response = requests.get(url, headers=DEFAULT_HEADERS, timeout=DEFAULT_TIMEOUT)

    if response.status_code != 200:
        return {"error": f"Failed to fetch user: {response.status_code}"}

    return response.json()


def get_repo(owner, repo):
    url = f"{REST_BASE_URL}/repos/{owner}/{repo}"
    response = requests.get(url, headers=DEFAULT_HEADERS, timeout=DEFAULT_TIMEOUT)

    if response.status_code != 200:
        return {"error": f"Failed to fetch repo: {response.status_code}"}

    return response.json()