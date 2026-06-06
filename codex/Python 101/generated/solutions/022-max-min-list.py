import sys


def min_max(numbers: list[int]) -> tuple[int, int]:
    """Return the smallest and largest numbers."""
    return min(numbers), max(numbers)


def main() -> None:
    data = sys.stdin.read().split()
    count = int(data[0])
    numbers = list(map(int, data[1:1 + count]))
    smallest, largest = min_max(numbers)
    print(f"{smallest} {largest}")


if __name__ == "__main__":
    main()
