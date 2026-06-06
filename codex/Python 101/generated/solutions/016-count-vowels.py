import sys


def count_vowels(text: str) -> int:
    """Count English vowels in text."""
    vowels = set("aeiou")
    count = 0
    for character in text.lower():
        if character in vowels:
            count += 1
    return count


def main() -> None:
    text = sys.stdin.read().rstrip("\n")
    print(count_vowels(text))


if __name__ == "__main__":
    main()
