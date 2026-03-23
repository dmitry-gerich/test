# Repository Guidelines

## Project Overview
- This repository contains a minimal Python CLI program in `app.py`.
- The program reads from `stdin`, writes each line back to `stdout`, and flushes after each write.
- The main executable behavior lives in `main()`.

## Files That Matter
- `app.py`: echo implementation and process exit behavior.
- `test_app.py`: subprocess-based integration check for the echo behavior.
- `README.md`: user-facing project description.
- `TEST.md`: notes about current coverage and known test gaps.

## Working Conventions
- Keep changes small and focused on the requested task.
- Preserve the current simple structure unless a change clearly requires refactoring.
- Follow existing Python style in the repo: straightforward functions, minimal abstraction, and readable names.
- Avoid adding dependencies unless explicitly requested.

## Running And Testing
- Run the app with `python3 app.py`.
- Run the current test with `python3 test_app.py`.
- If you add behavior, prefer updating the existing subprocess-based test before introducing a new test framework.

## Implementation Notes
- `stdout` flushing is part of the intended behavior and should be preserved.
- `KeyboardInterrupt` currently exits cleanly with status `0`; do not change that without a reason.
- Treat this as a command-line utility, not a web or GUI project.

## Documentation
- Update `README.md` when behavior or usage changes.
- Update `TEST.md` when test coverage meaningfully changes.
