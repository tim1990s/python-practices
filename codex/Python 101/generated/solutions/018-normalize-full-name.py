import sys


def normalize_name(name: str) -> str:
    """Normalize spaces and capitalization in a full name."""
    words = name.split()
    normalized_words = [word.lower().capitalize() for word in words]
    return " ".join(normalized_words)


def main() -> None:
    name = sys.stdin.read()
    print(normalize_name(name))


if __name__ == "__main__":
    main()
