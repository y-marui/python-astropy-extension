# Astropy Extension

> **このファイルは正本（日本語版）です。**
> 英語版（参照）は [README.md](README.md) を参照してください。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/y-marui/python-astropy-extension/actions/workflows/ci.yml/badge.svg)](https://github.com/y-marui/python-astropy-extension/actions/workflows/ci.yml)
[![Charter Check](https://github.com/y-marui/python-astropy-extension/actions/workflows/dev-charter-check.yml/badge.svg)](https://github.com/y-marui/python-astropy-extension/actions/workflows/dev-charter-check.yml)

astropy を拡張するユーティリティライブラリ。天文・物性データ解析向けのカスタム単位・可視化・データ入出力ユーティリティを提供します。

## Requirements

- Python >= 3.8
- astropy >= 5.1
- numpy >= 1.23.3
- matplotlib >= 3.6.1
- pylightxl >= 1.61

## Setup

```sh
pip install poetry
poetry install
```

## Usage

```python
from astropy_extension import units
from astropy_extension.units import sccm, uohm_cm, A__m2, get_exponential_as_unit
import astropy.units as u

# カスタム単位を使う
flow = 1.5 * sccm
resistivity = 2.0 * uohm_cm
current_density = 3.0 * A__m2

# 指数単位を生成する
e12 = get_exponential_as_unit(12)
```

| コマンド | 説明 |
|---|---|
| `poetry run pytest` | テスト実行 |

## License

[MIT](LICENSE)

---
*この文書には英語版 [README.md](README.md) があります。編集時は同一コミットで更新してください。*
