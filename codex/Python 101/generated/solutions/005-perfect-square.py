import math
import sys


def is_perfect_square(number: int) -> bool:
    """Return True when number is a perfect square."""
    if number < 0:
        return False
    root = math.isqrt(number)
    return root * root == number


def main() -> None:
    number = int(sys.stdin.read().strip())
    print("YES" if is_perfect_square(number) else "NO")


if __name__ == "__main__":
    main()
