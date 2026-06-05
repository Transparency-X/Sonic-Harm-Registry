# Contributing to Sonic Harm Registry

We welcome contributions from legal researchers, developers, designers, translators, and advocates.

## How to contribute
1. **Fork** the repository.
2. **Create a branch** for your change (`git checkout -b feature/amazing-feature`).
3. **Make your changes** following the existing style.
4. **Run tests** (`pytest tests/`).
5. **Commit** with a clear message.
6. **Push** and open a Pull Request.

## Adding or updating a term
- Edit `data/registry.json` (must pass JSON Schema validation).
- Update `docs/research_report.md` if the definition changes substantially.
- Provide at least one primary source citation in `data/sources.json`.

## Code style
- Python: PEP 8, run `black .` before commit.
- JavaScript: ES6, 2 spaces.
- HTML/CSS: semantic elements, responsive design.

## Reporting issues
Use GitHub Issues. Label accordingly: `bug`, `legal-update`, `feature-request`, `documentation`.
