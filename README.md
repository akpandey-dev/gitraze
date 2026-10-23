# Gitraze

> A CLI and Python library for GitHub exploration, search, and analysis

Gitraze is a CLI and Python library for exploring, analyzing, and extracting insights from GitHub through the REST API, with GraphQL planned.

**Status:** Early development — expect bugs, missing features, and rapid changes. APIs and CLI may change without notice.

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

Gitraze is built around a simpler approach:

* Fast, minimal, no nonsense
* Built for developers who think in terminals
* Deep GitHub data access through the REST API
* Modular and extensible architecture

---

## Features

* Modular system
* GitHub REST API integration
* CLI-first workflow
* SDK support
* Repository insights
* User analysis
* Search users, repositories, issues, pull requests, and topics
* Automatic filtering of pull requests and issues
* Human-readable timestamps
* Cleaned descriptions
* Three data formats
* Save or display output
* Analytics modules in progress
* GraphQL planned

---

## Installation

### From PyPI

```bash
pip install gitraze
```

### From source

```bash
git clone https://github.com/akpandey-dev/gitraze.git
cd gitraze
pip install -e .
```

> There may be some gaps between releases on GitHub and PyPI, as multiple commits are sometimes clustered into a single release on PyPI.


---

## Usage

Gitraze can be used from the command line or as a Python library.

### CLI

```bash
gitraze --help
```

Example:

```bash
gitraze --version
gitraze --help
gitraze user octocat --data-format=raw --output-action=save
gitraze repo torvalds/linux --data-format=full # Query format must match
gitraze search repos "machine learning" -n 5 --data-format=compact
gitraze analyze <target> # Coming soon!
```

### Python

```python
import gitraze as gz
```

For example:
```python
import gitraze as gz
user = gz.user("octocat", data_format="compact")
print(user["name"])
print(user["followers"])
```

For command usage, API reference, output formats, and examples, see the **[documentation](docs/)**.

---

## Philosophy

Gitraze is built for speed, clarity, and control.

No clutter, no distractions — just raw access to GitHub data, the way it should be.

If you live in the terminal, Gitraze lives with you.

---

## Project Status

Gitraze is in active development:

* Expect breaking changes
* Some commands may not work
* Features are being added rapidly
* GraphQL is not implemented yet; Gitraze is REST-focused for now

If you're here early — you're basically a beta tester.

---

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

---

## License

MIT License — do whatever you want, just don't blame me if you break stuff.
