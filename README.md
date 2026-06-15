# ShadowForge — Advanced Wordlist & Password Generator

ShadowForge is a modular, interactive wordlist generator intended for security
researchers, red-teamers, and developers who want to quickly craft large, targeted
password lists from small input seeds. It combines pattern permutations, numeric
mangling, symbol insertion, and optional leetspeak expansion to produce diverse
wordlists suitable for offline use.

**Current status:** Fully scaffolded and interactive; core generators ready for
extension.

**Key features**

- Interactive wizard for building generation profiles (`ui/wizard.py`).
- Pattern & permutation engine that combines base words, keywords, numbers and
  symbols (`core/generator.py`).
- Leetspeak expansion with configurable maps (`core/leet.py`).
- Numeric generators supporting random or sequential modes (`core/numbers.py`).
- Output filtering by minimum/maximum length and result limiting.
- Colorized terminal UI and ASCII banner for polished UX.

## Quickstart

Clone the project and set up a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Run the interactive wizard to build and save a wordlist:

```powershell
python shadowforge.py
```

Non-interactive mode is available by passing CLI options directly:

```powershell
python shadowforge.py -p "acme corp" -k admin support --min 6 --max 12 --leet --use-symbols --symbols "!@" --digits 2 4 --numbers-mode random --limit 50000
```

The tool will prompt for base names, keywords, length constraints, whether to
include leetspeak and symbols, digits range and mode, and a generation limit. The
final wordlist is saved under `wordlists/` as `<profile>_wordlist.txt`.

## Quick Example

- Base names: `acme corp`
- Keywords: `admin support`
- Min/Max length: `6` / `12`
- Enable leet: `y`
- Use symbols: `y` (custom: `!@`)
- Digits range: `2 4` (random)

This configuration will generate permutations such as `AcmeAdmin1!`, `support@acme`
and thousands of leetified variants where applicable.

## Project Layout

- `shadowforge.py` — CLI entry point; runs the banner and wizard, coordinates
  generation and outputs.
- `core/` — generation primitives
  - `generator.py` — apply patterns, concatenate permutations, symbol insertion
  - `leet.py` — leetspeak expansion map and combinator
  - `numbers.py` — numeric sequences and random number generation
  - `filter.py` — post-generation filtering utilities
- `ui/` — user-facing terminal helpers
  - `banner.py` — ASCII banner and system info
  - `colors.py` — color constants (uses `colorama`)
  - `wizard.py` — interactive prompts for configuration
- `wordlists/outputs/` — place for generated lists (ignored by git)
- `requirements.txt`, `LICENSE`, `.gitignore`

## Development & Extension Guide

- Improving patterns: Extend `core/generator.py` to add more pattern templates
  (e.g., separators, camelCase, leet-aware capitalization).
- Performance: Generation can produce large intermediate sets. Consider streaming
  output, using generators, or deduplicating early to reduce memory pressure.
- Testing: Add unit tests for `leet.leet()`, `numbers.generate_numbers()` and
  `generator.apply_patterns()` to ensure deterministic behavior.
- CLI: Add flags for non-interactive runs (e.g., `--profile`, `--limit`,
  `--symbols`) to integrate into automation pipelines.

## Security and Ethics

This tool can be used for legitimate security testing and also misused. Only
use ShadowForge on systems and accounts for which you have explicit permission.

## Contributing

1. Fork the repository and create a feature branch.
2. Add tests and update `requirements.txt` if you add dependencies.
3. Open a pull request describing the change and use cases.

## License

This project is licensed under the MIT License — see `LICENSE`.

## Roadmap (Ideas)

- Add a headless mode for CI integration and batch generation.
- Add a JSON/YAML config format for reproducible wordlist profiles.
- Provide a streaming writer that writes results as they are generated.
- Add a plugin system for custom pattern modules.
