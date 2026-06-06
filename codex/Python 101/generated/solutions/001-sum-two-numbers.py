import sys


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def main() -> None:
    # Read both numbers from one line.
    a, b = map(int, sys.stdin.read().split())
    print(add_numbers(a, b))


if __name__ == "__main__":
    main()
