import sys


def average_three(a: float, b: float, c: float) -> float:
    """Return the arithmetic mean of three numbers."""
    return (a + b + c) / 3


def main() -> None:
    a, b, c = map(float, sys.stdin.read().split())
    print(f"{average_three(a, b, c):.2f}")


if __name__ == "__main__":
    main()
