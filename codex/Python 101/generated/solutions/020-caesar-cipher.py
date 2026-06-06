import sys


def shift_letter(character: str, shift: int) -> str:
    """Shift one alphabetic character by shift positions."""
    if character.islower():
        base = ord("a")
    else:
        base = ord("A")
    offset = (ord(character) - base + shift) % 26
    return chr(base + offset)


def caesar_cipher(text: str, shift: int) -> str:
    """Encode text with the Caesar cipher."""
    result: list[str] = []
    for character in text:
        if character.isalpha():
            result.append(shift_letter(character, shift))
        else:
            result.append(character)
    return "".join(result)


def main() -> None:
    lines = sys.stdin.read().splitlines()
    text = lines[0] if lines else ""
    shift = int(lines[1]) if len(lines) > 1 else 0
    print(caesar_cipher(text, shift))


if __name__ == "__main__":
    main()
