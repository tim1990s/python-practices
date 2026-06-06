import sys


def is_valid_password(password: str) -> bool:
    """Check length and required character groups."""
    has_lower = any(character.islower() for character in password)
    has_upper = any(character.isupper() for character in password)
    has_digit = any(character.isdigit() for character in password)
    has_special = any(
        not character.isalnum() for character in password
    )
    return (
        len(password) >= 8
        and has_lower
        and has_upper
        and has_digit
        and has_special
    )


def main() -> None:
    password = sys.stdin.read().rstrip("\n")
    print("VALID" if is_valid_password(password) else "INVALID")


if __name__ == "__main__":
    main()
