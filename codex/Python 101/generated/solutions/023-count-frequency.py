import sys


def count_frequency(numbers: list[int]) -> dict[int, int]:
    """Return a frequency table for numbers."""
    frequency: dict[int, int] = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    return frequency


def main() -> None:
    data = sys.stdin.read().split()
    count = int(data[0])
    numbers = list(map(int, data[1:1 + count]))
    frequency = count_frequency(numbers)
    lines = [
        f"{number} {frequency[number]}"
        for number in sorted(frequency)
    ]
    sys.stdout.write("\n".join(lines))


if __name__ == "__main__":
    main()
