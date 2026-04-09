# user.py

from gitraze.core.api_rest import get_user as rest_get_user

def get_user(username):
    data = rest_get_user(username)

    if "error" in data:
        return data

    return {
        "name": data.get("name"),
        "login": data.get("login"),
        "bio": data.get("bio"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "public_repos": data.get("public_repos"),
        "location": data.get("location"),
        "profile_url": data.get("html_url")
    }