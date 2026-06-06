import sys


def remove_duplicates(numbers: list[int]) -> list[int]:
    """Remove duplicates while keeping first appearance order."""
    seen: set[int] = set()
    result: list[int] = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result


def main() -> None:
    data = sys.stdin.read().split()
    count = int(data[0])
    numbers = list(map(int, data[1:1 + count]))
    result = remove_duplicates(numbers)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
