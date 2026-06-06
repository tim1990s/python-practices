import sys


def fibonacci(index: int) -> int:
    """Return the Fibonacci number at zero-based index."""
    if index == 0:
        return 0
    previous, current = 0, 1
    for _ in range(2, index + 1):
        previous, current = current, previous + current
    return current


def main() -> None:
    index = int(sys.stdin.read().strip())
    print(fibonacci(index))


if __name__ == "__main__":
    main()
