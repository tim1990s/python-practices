import sys


def normalize(text: str) -> str:
    """Keep only alphanumeric characters and lowercase them."""
    return "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )


def is_palindrome(text: str) -> bool:
    """Return True when normalized text is a palindrome."""
    cleaned = normalize(text)
    return cleaned == cleaned[::-1]


def main() -> None:
    text = sys.stdin.read().rstrip("\n")
    print("YES" if is_palindrome(text) else "NO")


if __name__ == "__main__":
    main()
