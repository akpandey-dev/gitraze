# user.py
from gitraze.utils.helpers import format_date 
from gitraze.utils.helpers import normalize_api_data
from gitraze.core.api_rest import get_user as rest_get_user

def get_user_rest(username, output_format="compact"):
    data = rest_get_user(username)

    if "error" in data:
        return data


    if output_format == "raw":
        return data
    if output_format == "full":
        return normalize_api_data(data)

    return {
        "name": data.get("name"),
        "login": data.get("login"),
        "id": data.get("id"),
        "node_id": data.get("node_id"),
        "type": data.get("type"),
        "user_view_type": data.get("user_view_type"),
        "bio": data.get("bio"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "public_repos": data.get("public_repos"),
        "public_gists": data.get("public_gists"),
        "location": data.get("location"),
        "profile_url": data.get("html_url"),
        "created_at": format_date(data.get("created_at")),
        "email": data.get("email"),
        "twitter_username": data.get("twitter_username")
    }