import sys


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor."""
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def main() -> None:
    a, b = map(int, sys.stdin.read().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
