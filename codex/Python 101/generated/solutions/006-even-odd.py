import sys


def is_even(number: int) -> bool:
    """Return True when number is even."""
    return number % 2 == 0


def main() -> None:
    number = int(sys.stdin.read().strip())
    print("EVEN" if is_even(number) else "ODD")


if __name__ == "__main__":
    main()
