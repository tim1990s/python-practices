import sys


def sum_list(numbers: list[int]) -> int:
    """Return the sum of all numbers."""
    total = 0
    for number in numbers:
        total += number
    return total


def main() -> None:
    data = sys.stdin.read().split()
    count = int(data[0])
    numbers = list(map(int, data[1:1 + count]))
    print(sum_list(numbers))


if __name__ == "__main__":
    main()
