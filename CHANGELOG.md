# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Added docstrings across `core`, `handlers`, `modules`, `utilities`, and `CLI functions`.
* Corrected the project version number in `gitraze/__init__.py`.
* Cleaned up `gitraze/config.py`.

## [0.3.0] - 2026-06-29

### Added

* Added `compact`, `full`, and `raw` output formats for user, repository, and search operations.
* Added `--format` support to the `user`, `repo`, and `search` CLI commands.
* Added normalized API data handling for full output.

### Changed

* Updated CLI and SDK examples to document the available output formats.
* Expanded README documentation, SDK examples, and contributing instructions.
* Clarified that Gitraze is currently REST-focused, with GraphQL integration planned.
* Updated project metadata to version `0.3.0`.

### Removed

* Removed the unused `api_graphql.py` placeholder module.

## [0.2.6] - 2026-05-09

### Added

* Added list rendering support to terminal output.

### Fixed

* Preserved existing dictionary rendering while adding list support.

## [0.2.5] - 2026-05-09

### Added

* Added and refined the Python SDK interface.
* Expanded SDK documentation and examples.

### Changed

* Improved Python SDK imports.
* Updated the README with expanded usage documentation.

## [0.2.4] - 2026-05-08

### Changed

* Separated CLI command handlers from `cli.py`.
* Introduced dedicated handlers for user, repository, search, and analyze commands.
* Simplified CLI routing and configuration handling.

## [0.2.3] - 2026-05-05

### Changed

* Updated search query handling to use category-aware queries.
* Removed invalid global search filters.
* Updated CLI and documentation to reflect the revised search behavior.

### Fixed

* Resolved search behavior caused by invalid global filters.

## [0.2.2] - 2026-04-16

### Fixed

* Fixed issues and pull-request search failures.
* Improved search-related API handling and CLI behavior.

## [0.2.1] - 2026-04-15

### Fixed

* Removed an invalid standard-library dependency that caused package installation failures.

### Changed

* Updated package metadata and documentation following the packaging fix.

## [0.2.0] - 2026-04-15

### Added

* Added multi-result GitHub search.
* Added `-n` / `--limit` support for controlling the number of search results.
* Added pull-request search support and filtering.
* Added search support across repositories, users, issues, pull requests, and topics.

### Changed

* Improved search output formatting.
* Improved API error handling.
* Expanded CLI search functionality and documentation.

## [0.1.0] - 2026-04-13

### Added

* Added repository information commands.
* Added repository API handling.
* Added the MIT license.

### Changed

* Improved CLI routing.
* Refactored API handling.
* Updated project metadata for the `0.1.0` release.

## [0.0.2] - 2026-04-11

### Added

* Added reusable helper utilities.
* Expanded CLI functionality and output handling.
* Added additional README documentation and usage examples.

### Changed

* Improved CLI structure and user experience.
* Improved API error handling.
* Expanded output coverage.
* Updated project metadata for the `0.0.2` release.

## [0.0.1] - 2026-04-09

### Added

* Initial Gitraze release.
* Added the `user` command.
* Added GitHub REST API integration for retrieving user information.
* Established the initial CLI and Python package structure.

[Unreleased]: https://github.com/akpandey-dev/gitraze/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/akpandey-dev/gitraze/compare/v0.2.6...v0.3.0
[0.2.6]: https://github.com/akpandey-dev/gitraze/compare/v0.2.5...v0.2.6
[0.2.5]: https://github.com/akpandey-dev/gitraze/compare/v0.2.4...v0.2.5
[0.2.4]: https://github.com/akpandey-dev/gitraze/compare/v0.2.3...v0.2.4
[0.2.3]: https://github.com/akpandey-dev/gitraze/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/akpandey-dev/gitraze/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/akpandey-dev/gitraze/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/akpandey-dev/gitraze/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/akpandey-dev/gitraze/compare/v0.0.2...v0.1.0
[0.0.2]: https://github.com/akpandey-dev/gitraze/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/akpandey-dev/gitraze/releases/tag/v0.0.1
