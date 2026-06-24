# Gitraze

> A fast, hacker-style CLI for slicing through GitHub data like a blade.

Gitraze is a powerful command-line tool designed to explore, analyze, and extract insights from GitHub using both REST and GraphQL APIs — all from your terminal.

⚠️ **Status:** Early development — expect bugs, missing features, and rapid changes. APIs and CLI may change without notice.

> Built for developers who prefer terminals over tabs.


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

```bash
pip install gitraze
```


## Usage

### Run directly from your terminal:

Example: 
```bash
gitraze --help
gitraze user octocat --format=compact # Flag is entirely optional and available options are: 'compact', 'full', and 'raw'
gitraze repo torvalds/linux  
gitraze search repos "machine learning" -n 5 # Will show top 5 results, but it is optional flag
gitraze analyze github # Coming soon!
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

user = gz.user("octocat")

print(user["name"])
print(user["followers"])
```

#### Repository:
```python
import gitraze as gz

repo = gz.repo("torvalds", "linux")

print(repo["name"])
print(repo["owner"])
```

> Note: Unlike the CLI, the SDK accepts owner and repository name as separate arguments.

#### Search: 

```python
results = gz.search(gz.REPOS, "machine learning", 3)

for repo in results:
    print(repo["full_name"])
```

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

## Available exports:

### Functions: 

- `user()`
- `repo()`
- `search()`
- `display()`

### Constants:

- `USERS`
- `REPOS`
- `PRS`
- `ISSUES`
- `TOPICS`



⚠️ CLI commands are still evolving and may change.

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
- GraphQL feature is basically absent now, but is coming soon

If you're here early — you're basically a beta tester 😈

## Contributing

PRs, ideas, bug reports, and feature suggestions are welcome.
If you want to improve or modify Gitraze, go ahead.

```bash
git checkout -b feature/cool-thing
```

Just keep the code clean and the terminal fast.


## License

MIT License — do whatever you want, just don’t blame me if you break stuff.

