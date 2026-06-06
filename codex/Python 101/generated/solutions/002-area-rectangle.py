import sys


def rectangle_area(length: int, width: int) -> int:
    """Return the area of a rectangle."""
    return length * width


def main() -> None:
    # Input contains length and width.
    length, width = map(int, sys.stdin.read().split())
    print(rectangle_area(length, width))


if __name__ == "__main__":
    main()
