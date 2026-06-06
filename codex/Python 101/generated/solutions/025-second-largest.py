import sys


def second_largest(numbers: list[int]) -> int | None:
    """Return the second distinct largest value if it exists."""
    unique_values = sorted(set(numbers), reverse=True)
    if len(unique_values) < 2:
        return None
    return unique_values[1]


def main() -> None:
    data = sys.stdin.read().split()
    count = int(data[0])
    numbers = list(map(int, data[1:1 + count]))
    result = second_largest(numbers)
    if result is None:
        print("NO SECOND LARGEST")
    else:
        print(result)


if __name__ == "__main__":
    main()
