import sys


def classify_grade(score: float) -> str:
    """Classify a score from 0 to 10."""
    if score < 0 or score > 10:
        return "INVALID"
    if score >= 8.5:
        return "EXCELLENT"
    if score >= 7.0:
        return "GOOD"
    if score >= 5.0:
        return "AVERAGE"
    return "BELOW AVERAGE"


def main() -> None:
    score = float(sys.stdin.read().strip())
    print(classify_grade(score))


if __name__ == "__main__":
    main()
