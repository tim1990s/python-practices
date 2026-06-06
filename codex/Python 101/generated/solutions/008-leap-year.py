import sys


def is_leap_year(year: int) -> bool:
    """Return True for a Gregorian leap year."""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main() -> None:
    year = int(sys.stdin.read().strip())
    print("LEAP" if is_leap_year(year) else "COMMON")


if __name__ == "__main__":
    main()
