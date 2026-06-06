import sys


def factorial(number: int) -> int:
    """Return number factorial."""
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def main() -> None:
    number = int(sys.stdin.read().strip())
    print(factorial(number))


if __name__ == "__main__":
    main()
