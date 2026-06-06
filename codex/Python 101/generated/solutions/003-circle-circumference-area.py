import math
import sys


def circle_values(radius: float) -> tuple[float, float]:
    """Return circumference and area of a circle."""
    circumference = 2 * math.pi * radius
    area = math.pi * radius * radius
    return circumference, area


def main() -> None:
    radius = float(sys.stdin.read().strip())
    circumference, area = circle_values(radius)
    print(f"{circumference:.2f} {area:.2f}")


if __name__ == "__main__":
    main()
