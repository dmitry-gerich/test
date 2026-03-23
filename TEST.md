# Test Plan for Echo Utility

## Overview
`app.py` is a stdin-to-stdout echo utility. It reads lines from stdin and writes them back to stdout immediately. This document describes what should be tested to verify correct behavior.

---

## 1. Core Echo Behavior

**1.1 Single line**
- Input: one line of text ending with a newline
- Expected: the exact same line (including the newline) is written to stdout

**1.2 Multiple lines**
- Input: several lines of text
- Expected: each line is echoed in order, preserving all content and newlines

**1.3 Whitespace preservation**
- Input: lines with leading/trailing spaces or tabs
- Expected: whitespace is preserved exactly — no trimming or modification

**1.4 Output is byte-for-byte identical to input**
- The entire stdout should equal the entire stdin with no additions, deletions, or transformations

---

## 2. Edge Cases

**2.1 Empty input (no lines)**
- Input: immediate EOF with no data
- Expected: no output, exit with code 0

**2.2 Blank lines**
- Input: lines that contain only a newline character
- Expected: blank lines are echoed as-is

**2.3 Very long lines**
- Input: a single line with thousands of characters
- Expected: the full line is echoed without truncation

**2.4 Special characters**
- Input: lines containing characters such as `!@#$%^&*()`, quotes, backslashes, null bytes, etc.
- Expected: all characters are preserved and echoed unchanged

**2.5 Unicode / multibyte characters**
- Input: lines containing non-ASCII text (e.g., accented letters, CJK characters, emoji)
- Expected: characters are echoed correctly without corruption

---

## 3. Real-Time Flushing

**3.1 Output appears immediately after each line**
- After writing each line, `sys.stdout.flush()` is called
- Expected: a reader on the other end of the pipe receives each line without waiting for the process to exit
- This is distinct from buffered I/O and is critical for interactive use

---

## 4. Exit Conditions

**4.1 EOF (Ctrl+D / end of pipe)**
- When stdin is closed or exhausted, the application should exit cleanly
- Expected: exit code 0, no error message, no exception traceback

**4.2 KeyboardInterrupt (Ctrl+C)**
- When the process receives SIGINT, the application should exit cleanly
- Expected: exit code 0, no error message, no exception traceback

---

## 5. Stderr

**5.1 No output to stderr under normal operation**
- For any valid input, stderr should remain empty
- Unexpected stderr output indicates an unhandled exception or misconfiguration

---

## 6. Existing Test Coverage (`test_app.py`)

The current integration test in `test_app.py` covers:
- Two-line input with standard ASCII text
- Exact match of stdout to input string
- Basic subprocess launch and clean exit

Gaps not yet covered by `test_app.py`:
- Empty input
- Blank lines
- Long lines
- Special/unicode characters
- Real-time flushing behavior
- Ctrl+C / SIGINT handling
- Stderr being empty
