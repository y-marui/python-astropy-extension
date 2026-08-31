# AI_CONTEXT.md

## Project Overview

astropy を拡張する Python ライブラリ。天文データ解析向けのカスタム単位・単位フォーマット・可視化・データ入出力ユーティリティを提供する。

**技術スタック:**
- 言語: Python >= 3.9（pyenv で 3.14 を使用）
- 主要依存: astropy >= 5.1, numpy >= 1.23.3, matplotlib >= 3.6.1, pylightxl >= 1.61
- パッケージ管理: uv（`uv sync --extra dev`）
- linter / formatter: ruff
- 型チェック: mypy
- テスト: pytest

**主要ディレクトリ:**

```
astropy_extension/   # ライブラリ本体
  io/                # データ入出力
  units.py           # カスタム単位定義 (sccm, uohm_cm, A__m2 等)
  units_format.py    # 単位フォーマット
  visualization.py   # 可視化ユーティリティ
  utils_misc.py      # 汎用ユーティリティ
tests/               # pytest テスト
docs/dev-charter/    # 開発憲章（git subtree）
```

## Applied Charter Principles

憲章参照: `docs/dev-charter/CHARTER_INDEX.md` でトピックを特定してから該当ファイルのみ読む

- **コード設計**: YAGNI 原則・最小限の依存・既存パターンへの準拠（[PRINCIPLES.md](docs/dev-charter/PRINCIPLES.md)）
- **ドキュメント構成**: DEVELOPING.md（開発者向け）・CONTRIBUTING.md（外部向け）・docs/ の責務分離（[DOCS_STRUCTURE.md](docs/dev-charter/DOCS_STRUCTURE.md)）
- **ドキュメント同期**: 仕様・ルール・構成の変更時、同じ作業内で関連ドキュメント（docs/・AI_CONTEXT.md・README.md 等）を更新する（[AI_TOOL_SETUP.md](docs/dev-charter/AI_TOOL_SETUP.md)）
- **コミットメッセージ**: Conventional Commits（feat/fix/chore/docs/refactor）
- **セキュリティ**: pre-commit フック（gitleaks・detect-dotenv・detect-private-key・no-hardcoded-local-paths）必須
- **CI**: GitHub Actions で security / lint（ruff + mypy） / test → build → gate（`Required Checks`）の順で実行。docs-only の変更では lint/test/build は自動スキップされる。`gate` job が Branch Protection 必須チェック
- **コメント**: 「なぜそうするか」のみ書く。自明な処理には書かない
- **pre-commit**: `pre-commit run --all-files` で全フック通過が必須
- **憲章参照手順**: 不明点は `CHARTER_INDEX.md` → 該当ファイル（1〜2 件）の順で参照（[AI_COLLABORATION_RULES.md](docs/dev-charter/AI_COLLABORATION_RULES.md)）

## Project-Specific Rules

- パッケージ管理は **uv** を使用する（`uv sync --extra dev`）
- lint: `uv run ruff check .` / format: `uv run ruff format .`
- 型チェック: `uv run mypy astropy_extension`
- テスト実行: `uv run pytest`
- Python バージョン制約: >= 3.11（EOL まで 6 ヶ月以上あるバージョンをサポート対象とする）

## AI Tool Assignments

- **使用ツール**：Claude Code、Codex、GitHub Copilot、Gemini CLI、ローカル LLM（Ollama）
- **標準担当の正本**：`docs/dev-charter/AI_COLLABORATION_RULES.md` の「AI Tool Responsibilities」と「Rules for Multi-AI Usage」
- **プロジェクト固有の上書き**：なし

## Prohibited Actions

- シークレット・認証情報のコードへの埋め込み
- `.env` ファイルのコミット（`.env.example` は可）
- ローカル絶対パス（`/Users/xxx/`）のコードへのハードコード
- `docs/dev-charter/` 配下の直接編集（subtree 経由で管理）
