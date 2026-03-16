import sys

def main():
    """
    A simple script that reads input from stdin and echoes it back to stdout.
    Used for testing text input/output.
    """
    try:
        for line in sys.stdin:
            # Echo the line back to stdout
            sys.stdout.write(line)
            sys.stdout.flush()
    except EOFError:
        pass
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
