import sys


def min_max_three(values: list[int]) -> tuple[int, int]:
    """Return the smallest and largest values."""
    return min(values), max(values)


def main() -> None:
    values = list(map(int, sys.stdin.read().split()))
    smallest, largest = min_max_three(values)
    print(f"{smallest} {largest}")


if __name__ == "__main__":
    main()
