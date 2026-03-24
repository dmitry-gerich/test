import sys

RIDDLE = (
    "I have cities, but no houses live there.\n"
    "I have mountains, but no trees grow there.\n"
    "I have water, but no fish swim there.\n"
    "I have roads, but no cars drive there.\n"
    "What am I?"
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 app.py <answer>")
        sys.exit(1)

    expected = sys.argv[1].strip().lower()
    print(f"Riddle: {RIDDLE}")

    try:
        for line in sys.stdin:
            guess = line.strip().lower()
            if guess == expected:
                print("Correct!")
                sys.exit(0)
            else:
                print("Wrong answer, try again.")
                sys.stdout.flush()
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

if __name__ == "__main__":
    main()
