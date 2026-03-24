# CLAUDE.md

## Project Overview
A minimal Python stdin-to-stdout echo utility. Reads lines from stdin and writes them back to stdout in real time.

## Commands

### Run the application
```bash
python3 app.py
```
Type lines of input; each line is echoed back. Press Ctrl+D (EOF) or Ctrl+C to exit.

### Run tests
```bash
python3 test_app.py
```
Runs a subprocess-based integration test. Prints `SUCCESS` or `FAILURE`.

## Architecture
- `app.py` — main loop: reads stdin line-by-line, writes to stdout with flush
- `test_app.py` — spawns `app.py` via subprocess, sends test input, validates output

## Code Conventions
- Pure Python 3 standard library — no external dependencies, no requirements.txt
- No build system — run files directly with `python3`
