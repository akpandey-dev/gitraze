# Gitraze SDK

Gitraze can be used as a Python SDK for accessing GitHub data programmatically.

The recommended import style is:

```python
import gitraze as gz
```

The SDK currently provides functions for retrieving users and repositories, searching GitHub, and displaying results.

---

## `gz.user()`

Retrieves information about a GitHub user.

### How it works

The function accepts a GitHub username, requests the user's data through the GitHub API, and returns the result in the selected data format.

### Syntax

```python
gz.user(username, data_format="compact")
```

* `username` : GitHub username to retrieve.
* `data_format` : Format in which the result should be returned.

### Example

```python
import gitraze as gz

user = gz.user("octocat")

print(user["name"])
print(user["followers"])
```

---

## `gz.repo()`

Retrieves information about a GitHub repository.

### How it works

The function accepts the repository owner and repository name separately, requests the repository data through the GitHub API, and returns the result in the selected data format.

### Syntax

```python
gz.repo(owner, repo, data_format="compact")
```

* `owner` : GitHub username or organization that owns the repository.
* `repo` : Repository name.
* `data_format` : Format in which the result should be returned.

### Example

```python
import gitraze as gz

repo = gz.repo("torvalds", "linux", data_format="full")

print(repo["name"])
print(repo["owner"])
```

Unlike the CLI, the SDK accepts the repository owner and repository name as separate arguments.

---

## `gz.search()`

Searches GitHub using one of the supported search categories.

### How it works

The function accepts a search category, query, and optional result limit. It sends the search request to GitHub and returns the matching results in the selected data format.

### Syntax

```python
gz.search(category, query, limit=1, data_format="compact")
```

* `category` : Search category.
* `query` : Search query.
* `limit` : Maximum number of results to return.
* `data_format` : Format in which the results should be returned.

### Example

```python
import gitraze as gz

results = gz.search(
    gz.REPOS,
    "machine learning",
    3,
    data_format="compact"
)

for repo in results:
    print(repo["full_name"])
```

---

## Search Categories

The SDK exposes constants for supported search categories:

```python
gz.USERS
gz.REPOS
gz.PRS
gz.ISSUES
gz.TOPICS
```

These constants can be passed to `gz.search()`.

For example:

```python
results = gz.search(
    gz.USERS,
    "octocat",
    3
)
```

---

## Data Formats

The SDK functions support three data formats:

```python
"compact"
"full"
"raw"
```

### `compact`

Returns a concise, human-readable subset of the most useful fields.

This is the default format.

```python
user = gz.user("octocat", data_format="compact")
```

### `full`

Returns all available processed fields exposed by Gitraze.

```python
repo = gz.repo(
    "torvalds",
    "linux",
    data_format="full"
)
```

### `raw`

Returns the raw GitHub API response without Gitraze's filtering or formatting.

```python
results = gz.search(
    gz.REPOS,
    "machine learning",
    3,
    data_format="raw"
)
```

The available processed fields may change as the SDK develops.

---

## `gz.display()`

Displays Gitraze data in a human-readable terminal format.

### How it works

`display()` accepts Gitraze data and formats it for terminal output rather than returning the data in the same way as the SDK query functions.

### Syntax

```python
gz.display(data)
```

* `data` : Data returned by a Gitraze SDK function.

### Example

```python
import gitraze as gz

user = gz.user("octocat")

gz.display(user)
```

Example output:

```text
Name             : The Octocat
Login            : octocat
Id               : 583231
Node_id          : MDQ6VXNlcjU4MzIzMQ==
Type             : User
User_view_type   : public
Bio              : None
Followers        : 22578
Following        : 9
Public_repos     : 8
Public_gists     : 8
Location         : San Francisco
Profile_url      : https://github.com/octocat
Created_at       : 25 Jan 2011
Email            : None
Twitter_username : None
```

Exact fields and values may differ depending on the GitHub API response.

---


> The SDK is designed to provide programmatic access to the same GitHub data used by Gitraze's CLI.
