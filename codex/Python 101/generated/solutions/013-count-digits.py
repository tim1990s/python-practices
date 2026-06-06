import sys


def count_digits(number: int) -> int:
    """Return the number of decimal digits."""
    number = abs(number)
    if number == 0:
        return 1

    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


def main() -> None:
    number = int(sys.stdin.read().strip())
    print(count_digits(number))


if __name__ == "__main__":
    main()
