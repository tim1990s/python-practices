import sys


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words."""
    return len(text.split())


def main() -> None:
    text = sys.stdin.read()
    print(count_words(text))


if __name__ == "__main__":
    main()
