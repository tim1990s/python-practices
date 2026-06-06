import sys


def linear_search(numbers: list[int], target: int) -> int:
    """Return the first index of target, or -1."""
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1


def main() -> None:
    data = sys.stdin.read().split()
    count = int(data[0])
    numbers = list(map(int, data[1:1 + count]))
    target = int(data[1 + count])
    print(linear_search(numbers, target))


if __name__ == "__main__":
    main()
