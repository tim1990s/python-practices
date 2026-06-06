import sys


def classify_triangle(a: int, b: int, c: int) -> str:
    """Return the triangle type for three side lengths."""
    sides = sorted([a, b, c])
    x, y, z = sides
    if x <= 0 or x + y <= z:
        return "NOT TRIANGLE"
    if x == z:
        return "EQUILATERAL"
    if x == y or y == z:
        return "ISOSCELES"
    return "SCALENE"


def main() -> None:
    a, b, c = map(int, sys.stdin.read().split())
    print(classify_triangle(a, b, c))


if __name__ == "__main__":
    main()
