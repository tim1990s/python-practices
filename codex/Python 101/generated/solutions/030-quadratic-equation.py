import math
import sys


EPSILON = 1e-12


def solve_quadratic(a: float, b: float, c: float) -> str:
    """Classify and solve ax^2 + bx + c = 0 over real numbers."""
    if abs(a) < EPSILON:
        if abs(b) < EPSILON:
            if abs(c) < EPSILON:
                return "Infinite solutions"
            return "No solution"
        root = -c / b
        return f"One root: x = {root:.2f}"

    delta = b * b - 4 * a * c
    if delta < -EPSILON:
        return "No real roots"
    if abs(delta) <= EPSILON:
        root = -b / (2 * a)
        return f"One root: x = {root:.2f}"

    sqrt_delta = math.sqrt(delta)
    root_one = (-b - sqrt_delta) / (2 * a)
    root_two = (-b + sqrt_delta) / (2 * a)
    x1, x2 = sorted([root_one, root_two])
    return f"Two roots: x1 = {x1:.2f}, x2 = {x2:.2f}"


def main() -> None:
    a, b, c = map(float, sys.stdin.read().split())
    print(solve_quadratic(a, b, c))


if __name__ == "__main__":
    main()
