import sys


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def main() -> None:
    celsius = float(sys.stdin.read().strip())
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{fahrenheit:.2f}")


if __name__ == "__main__":
    main()
