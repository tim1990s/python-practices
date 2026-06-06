import math
import sys


def is_prime(number: int) -> bool:
    """Return True when number is prime."""
    if number < 2:
        return False
    limit = math.isqrt(number)
    for divisor in range(2, limit + 1):
        if number % divisor == 0:
            return False
    return True


def main() -> None:
    number = int(sys.stdin.read().strip())
    print("YES" if is_prime(number) else "NO")


if __name__ == "__main__":
    main()
