# Gitraze Development

This guide covers the basic setup and structure used when developing Gitraze.

## Development Setup

Clone the repository:

```bash
git clone https://github.com/akpandey-dev/gitraze.git
cd gitraze
```

Install Gitraze in editable mode:

```bash
pip install -e .
```

Editable installation allows changes made to the source code to be reflected immediately without reinstalling the package.

---

## Project Structure

The main package is located under `gitraze/`.

### `cli.py`

Contains the command-line interface and command handling.

### `config.py`

Contains project configuration and shared configuration values.

### `core/`

Contains the core functionality used by the rest of the package.

### `handlers/`

Contains higher-level handlers for specific operations.

### `modules/`

Contains the main functional modules used by Gitraze.

### `utils/`

Contains reusable utility functionality shared across the project.

---

## Working on Gitraze

After installing the project in editable mode, changes can be made directly to the source code and used immediately.

For example, test CLI changes with:

```bash
gitraze --help
```

Python API changes can be tested by importing the local package:

```python
import gitraze as gz
```

Keep changes focused on the relevant part of the project and follow the existing structure.

When changing public functionality, update the corresponding documentation as well.
