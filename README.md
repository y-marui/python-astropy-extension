# Astropy Extension

> **This is the reference (English) version.**
> The canonical (Japanese) version is [README-jp.md](README-jp.md).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/y-marui/python-astropy-extension/actions/workflows/ci.yml/badge.svg)](https://github.com/y-marui/python-astropy-extension/actions/workflows/ci.yml)
[![Charter Check](https://github.com/y-marui/python-astropy-extension/actions/workflows/dev-charter-check.yml/badge.svg)](https://github.com/y-marui/python-astropy-extension/actions/workflows/dev-charter-check.yml)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/y-marui?style=social)](https://github.com/sponsors/y-marui)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-donate-yellow.svg)](https://www.buymeacoffee.com/y.marui)

A utility library that extends astropy, providing custom units, visualization, and data I/O utilities for astronomy and condensed-matter data analysis.

## Requirements

- Python >= 3.11
- astropy >= 5.1
- numpy >= 1.23.3
- matplotlib >= 3.6.1
- pylightxl >= 1.61

## Setup

```sh
uv sync
```

## Usage

```python
from astropy_extension import units
from astropy_extension.units import sccm, uohm_cm, A__m2, get_exponential_as_unit
import astropy.units as u

# Use custom units
flow = 1.5 * sccm
resistivity = 2.0 * uohm_cm
current_density = 3.0 * A__m2

# Create an exponent unit
e12 = get_exponential_as_unit(12)
```

| Command | Description |
|---|---|
| `uv run pytest` | Run tests |
| `uv run ruff check .` | Lint |
| `uv run ruff format .` | Format |
| `uv run mypy astropy_extension` | Type check |

## License

[MIT](LICENSE)

---
*This document has a Japanese canonical version [README-jp.md](README-jp.md). Update both in the same commit when editing.*
