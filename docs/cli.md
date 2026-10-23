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
* `[options]` :
    * `--data-format` : Data format to use.
    * `--output-action` : Display or save data.

### Example

```bash
gitraze user octocat --data-format=compact --output-action=display
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

Exact fields and values may differ depending on the GitHub API response.

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
* `[options]` :
    * `--data-format` : Data format to use.
    * `--output-action` : Display or save data.

### Example

```bash
gitraze repo torvalds/linux --data-format=full --output-action=display
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
* `[options]` :
    * `-n` or `--limit` : Number of results to return.
    * `--data-format` : Data format to use.
    * `--output-action` : Display or save data.

### Example

```bash
gitraze search repos "machine learning" -n 5 --data-format=compact --output-action=display
```

This searches repositories for the query `machine learning` and requests five results.

---

## Search Categories

Gitraze supports the following search categories:

* `users`
* `repos`
* `prs`
* `issues`
* `topics`


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

## Output Actions

Gitraze supports multiple output actions for commands that return GitHub data.

The output action is selected using the `--output-action` option.

### `display`

Displays the result in a human-readable terminal format.

For example:

```bash
gitraze user octocat --output-action=display
```

The title is automatically constructed by the Gitraze CLI handlers.

### `save`

Saves the result to a `.json` file in the current directory.

For example:

```bash
gitraze user octocat --output-action=save
```

The filename is automatically constructed by the Gitraze CLI handlers.

> The available output actions may change as Gitraze develops.

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
