# Gitraze CLI

Gitraze provides a command-line interface for accessing GitHub data directly from the terminal.

The general command structure is:

```bash
gitraze <command> [arguments] [options]
```

Use `--help` to view the available commands and options:

```bash
gitraze --help
```

---

## `gitraze --version`

Displays the installed Gitraze version.

### Syntax

```bash
gitraze --version
```

### Example

```bash
gitraze --version
```

Example output:

```text
gitraze 0.3.0
```

The displayed version depends on the installed Gitraze release.

---

## `gitraze user`

Retrieves information about a GitHub user.

### How it works

The command accepts a GitHub username and retrieves the corresponding user data.

### Syntax

```bash
gitraze user <username> [options]
```

* `<username>` : GitHub username to retrieve.
* `--data-format` : Data format to use.

### Example

```bash
gitraze user octocat
```

Example output:

```text
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

---

## `gitraze repo`

Retrieves information about a GitHub repository.

### How it works

The command accepts a repository in `owner/repository` form and retrieves the corresponding repository data.

### Syntax

```bash
gitraze repo <owner>/<repo> [options]
```

* `<owner>` : GitHub username or organization that owns the repository.
* `<repo>` : Repository name.
* `--data-format` : Data format to use.

### Example

```bash
gitraze repo torvalds/linux --data-format=full
```

The repository query uses the `owner/repository` format.

---

## `gitraze search`

Searches GitHub using a supported search category.

### How it works

The command accepts a search category and query, then retrieves matching results from GitHub.

### Syntax

```bash
gitraze search <category> <query> [options]
```

* `<category>` : Search category.
* `<query>` : Search query.
* `-n` : Number of results to return.
* `--data-format` : Data format to use.

### Example

```bash
gitraze search repos "machine learning" -n 5 --data-format=compact
```

This searches repositories for the query `machine learning` and requests five results.

---

## Search Categories

Gitraze supports the following search categories:

* users
* repos
* prs
* issues
* topics


For example:

```bash
gitraze search users "octocat"
```

or:

```bash
gitraze search repos "machine learning" -n 5
```

---

## Data Formats

Gitraze supports multiple data formats for commands that return GitHub data.

### `compact`

Returns a concise, human-readable representation of the result.

For example:
```bash
gitraze user octocat --data-format=compact
```

### `full`

Returns all processed fields exposed by Gitraze.

For example:
```bash
gitraze repo torvalds/linux --data-format=full
```

### `raw`

Returns the raw GitHub API response.

For example:
```bash
gitraze user octocat --data-format=raw
```

The available fields and output may change as Gitraze develops.

---

## Help

Use `--help` to inspect available commands and options.

For general help:

```bash
gitraze --help
```

For command-specific help:

```bash
gitraze <command> --help
```

The help output reflects the commands and options available in the installed version.
