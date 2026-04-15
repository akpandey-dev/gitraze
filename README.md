# Gitraze

> A fast, hacker-style CLI for slicing through GitHub data like a blade.

Gitraze is a powerful command-line tool designed to explore, analyze, and extract insights from GitHub using both REST and GraphQL APIs — all from your terminal.

⚠️ **Status:** Early development — expect bugs, missing features, and rapid changes.

---

## Why Gitraze?

Most GitHub tools are either slow, bloated, or UI-heavy.

**Gitraze is different:**
- ⚡ Fast, minimal, no nonsense
- 🧠 Built for developers who think in terminals
- 🔍 Deep GitHub data access (REST + GraphQL)
- 🧩 Modular and extensible architecture

---

## Features

- 🔌 Modular system (easy to extend and hack on)
- 💻 CLI-first workflow
- 🌐 GitHub API integration (REST + GraphQL)
- 📦 Repository insights
- 👤 User analysis
- 🔎 Search capabilities
- 📊 Analytics modules (in progress)

---

## Installation

```bash
pip install gitraze
```


## Usage

Run directly from your terminal:

Example: 
```bash
gitraze --help
gitraze user octocat
gitraze repo torvalds/linux       
gitraze search "machine learning" 
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
> 💡 Commands prefixed with `$` should be run in your terminal.

You can also use it inside Python:

```python
import gitraze
```

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

## License

MIT License — do whatever you want, just don’t blame me if you break stuff.