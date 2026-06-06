import sys


def sum_to_n(number: int) -> int:
    """Return 1 + 2 + ... + number."""
    total = 0
    for value in range(1, number + 1):
        total += value
    return total


def main() -> None:
    number = int(sys.stdin.read().strip())
    print(sum_to_n(number))


if __name__ == "__main__":
    main()
