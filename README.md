# Gitraze

> A fast, hacker-style CLI for slicing through GitHub data like a blade.

Gitraze is a powerful command-line tool designed to explore, analyze, and extract insights from GitHub using REST, with GraphQL support coming soon; all from your terminal.

⚠️ **Status:** Early development — expect bugs, missing features, and rapid changes. APIs and CLI may change without notice.

> Built for developers who prefer terminals over tabs.

[![PyPI](https://img.shields.io/pypi/v/gitraze)](https://pypi.org/project/gitraze/)
[![Python Versions](https://img.shields.io/pypi/pyversions/gitraze)](https://pypi.org/project/gitraze/)
[![Downloads](https://img.shields.io/pypi/dm/gitraze)](https://pypi.org/project/gitraze/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/akpandey-dev/gitraze/ci.yml?branch=main)](https://github.com/akpandey-dev/gitraze/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/akpandey-dev/gitraze)](https://github.com/akpandey-dev/gitraze/issues)
[![Stars](https://img.shields.io/github/stars/akpandey-dev/gitraze?style=social)](https://github.com/akpandey-dev/gitraze)
[![Last Commit](https://img.shields.io/github/last-commit/akpandey-dev/gitraze)](https://github.com/akpandey-dev/gitraze/commits/main)
[![Contributors](https://img.shields.io/github/contributors/akpandey-dev/gitraze)](https://github.com/akpandey-dev/gitraze/graphs/contributors)


---

## Why Gitraze?

Most GitHub tools are either slow, bloated, or UI-heavy.

**Gitraze is different:**
-  Fast, minimal, no nonsense
-  Built for developers who think in terminals
-  Deep GitHub data access (REST + GraphQL)
-  Modular and extensible architecture

---

## Features

-  Modular system (easy to extend and hack on)
-  CLI-first workflow
-  GitHub API integration (REST + GraphQL)
-  Repository insights
-  User analysis
-  Filter PRs vs issues automatically
-  Human-readable timestamps
-  Cleaned descriptions (HTML stripped)
-  Analytics modules (in progress)
-  Search users, repos, issues, PRs, and topics


---

## Installation

### From PyPI using `pip`

```bash
pip install gitraze
```

### Using source code from Repository

> Read the `Development setup` section.

---
> There may be some gap between releases on GitHub and PyPI, as more than one commits are sometimes clustered as a single release on PyPI.


## Usage

### Run directly from your terminal:

Example: 
```bash
gitraze --version
gitraze --help
gitraze user octocat --format=raw 
gitraze repo torvalds/linux --format=full # Query format must match
gitraze search repos "machine learning" -n 5 --format=compact 
gitraze analyze <target> # Coming soon!
```

Example output:

```bash
$ gitraze user octocat

[+] Fetching user data...
[✓] Done

User: octocat
-------------
Name             : The Octocat
Login            : octocat
Id               : 583231
Node_id          : MDQ6VXNlcjU4MzIzMQ==
Type             : User
User_view_type   : public
Bio              : None
Followers        : 22312
Following        : 9
Public_repos     : 8
Public_gists     : 8
Location         : San Francisco
Profile_url      : https://github.com/octocat
Created_at       : 25 Jan 2011
Email            : None
Twitter_username : None

```

> Commands prefixed with `$` should be run in your terminal.

### Gitraze can also be used as a lightweight Python SDK.

#### User:
```python
import gitraze as gz

user = gz.user("octocat", output_format="compact")

print(user["name"])
print(user["followers"])
```

#### Repository:
```python
import gitraze as gz

repo = gz.repo("torvalds", "linux", output_format="full")

print(repo["name"])
print(repo["owner"])
```

> Note: Unlike the CLI, the SDK accepts owner and repository name as separate arguments.

#### Search: 

```python
import gitraze as gz

results = gz.search(gz.REPOS, "machine learning", 3, output_format="compact")

for repo in results:
    print(repo["full_name"])
```

### Custom Output Format:

All three SDK functions support output customization:

```python
import gitraze as gz

user = gz.user("octocat", output_format="full")
repo = gz.repo("torvalds", "linux", output_format="raw")
results = gz.search(gz.REPOS, "machine learning", 3, output_format="full")
```

#### Available options are:

* `output_format="compact"`: Returns a concise, human-friendly subset of the most useful fields.
* `output_format="full"`: Returns all available processed fields exposed by Gitraze.
* `output_format="raw"`: Returns the raw GitHub API response without filtering or formatting.


### Pretty-print results in terminal style:

```python
from gitraze import *

display(user("octocat"))
```

Example output:

```bash
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

> Note: **`import gitraze as gz`** is the recommended import.

> Note: Exact fields and values may differ from the examples shown, depending on the GitHub API response.

## Available exports:

### Functions: 

- `user(username, output_format="compact")`
- `repo(owner, repo, output_format="compact")`
- `search(category, query, limit=1, output_format="compact")`
- `display(data)`

### Constants:

- `USERS`
- `REPOS`
- `PRS`
- `ISSUES`
- `TOPICS`

> Constants depend on the module internals and may change without prior notice.

> CLI commands and SDK APIs are still evolving and may change between releases.


## Philosophy

Gitraze is built for speed, clarity, and control.

No GUI. No clutter. No distractions.  
Just raw access to GitHub data — the way it should be.

If you live in the terminal, Gitraze lives with you.

## Development Setup

Clone the repo and install locally:

```bash
git clone https://github.com/akpandey-dev/gitraze.git
cd gitraze
pip install -e .
```

## Project Status

Gitraze is in active development:

- Expect breaking changes
- Some commands may not work
- Features are being added rapidly
- GraphQL feature is basically absent now, but integration is planned; currently REST-focused.

If you're here early — you're basically a beta tester.

## Contributing

PRs, ideas, bug reports, and feature suggestions are welcome.
If you want to improve or modify Gitraze, go ahead.
* Fork the repository
* Create a feature branch
* Submit a PR with clean commit messages

```bash
git checkout -b feature/cool-thing
```

Just keep the code clean and the terminal fast.


## License

MIT License — do whatever you want, just don’t blame me if you break stuff.

