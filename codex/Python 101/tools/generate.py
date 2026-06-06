"""Generate curriculum artifacts from markdown specification files."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
CURRICULUM_DIR = ROOT / "specs" / "curriculum"
GENERATED_DIR = ROOT / "generated"

REQUIRED_FIELDS = [
    "id",
    "slug",
    "title",
    "module",
    "difficulty",
    "exercise_type",
    "prerequisites",
    "python_topics",
    "math_topics",
    "problem",
    "input",
    "output",
    "sample_input",
    "sample_output",
    "sample_explanation",
]

MODULE_THEORY = {
    "Basic Math": (
        "Trong nhóm bài Basic Math, trọng tâm không phải là công thức khó mà là "
        "cách biến một yêu cầu toán học thành chương trình Python tuyến tính. "
        "Người học cần nhìn thấy luồng dữ liệu đi từ input, qua biến trung gian, "
        "đến output. Đây là nền tảng cho mọi bài sau này, vì nếu chưa hiểu dữ "
        "liệu được đọc, chuyển kiểu và tính toán như thế nào thì các cấu trúc "
        "phức tạp hơn cũng sẽ trở nên mơ hồ."
    ),
    "Condition If Else": (
        "Ở module điều kiện, chương trình không còn chạy một đường thẳng duy "
        "nhất. Python phải chọn nhánh dựa trên kết quả của biểu thức boolean. "
        "Điều quan trọng là viết điều kiện sao cho phản ánh đúng quy tắc của "
        "bài toán, đồng thời sắp xếp các nhánh từ trường hợp đặc biệt đến "
        "trường hợp tổng quát để tránh kết quả sai."
    ),
    "Loop": (
        "Vòng lặp giúp chương trình xử lý các thao tác lặp đi lặp lại mà không "
        "cần sao chép code. Với người mới học, điểm khó nhất là xác định biến "
        "nào cần được cập nhật sau mỗi vòng, điều kiện nào khiến vòng lặp dừng, "
        "và giá trị ban đầu của biến tích lũy nên là gì."
    ),
    "String": (
        "Chuỗi trong Python là một dãy ký tự có thứ tự. Xử lý chuỗi thường bao "
        "gồm các bước làm sạch dữ liệu, duyệt từng ký tự hoặc từng từ, kiểm tra "
        "điều kiện và ghép kết quả. Đây là kỹ năng rất thực tế vì dữ liệu người "
        "dùng nhập vào hiếm khi sạch hoàn toàn."
    ),
    "List": (
        "List cho phép lưu nhiều giá trị trong cùng một biến và xử lý chúng như "
        "một dãy. Khi làm việc với list, người học cần tập trung vào thứ tự phần "
        "tử, cách duyệt, cách tích lũy kết quả và cách chọn cấu trúc phụ như "
        "set hoặc dictionary khi bài toán cần kiểm tra trùng lặp hay đếm tần "
        "suất."
    ),
    "Function": (
        "Hàm là công cụ để chia chương trình thành các khối nhỏ có tên gọi rõ "
        "ràng. Một hàm tốt nhận dữ liệu qua tham số, xử lý một nhiệm vụ cụ thể "
        "và trả về kết quả. Cách viết này giúp chương trình dễ đọc, dễ kiểm thử "
        "và dễ mở rộng khi bài toán lớn hơn."
    ),
}


def parse_curriculum() -> list[dict[str, object]]:
    """Read all curriculum markdown files and extract exercise catalogs."""
    exercises: list[dict[str, object]] = []
    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()

    for spec_file in sorted(CURRICULUM_DIR.glob("*.md")):
        text = spec_file.read_text(encoding="utf-8")
        match = re.search(r"```json\s*(\[.*?\])\s*```", text, re.DOTALL)
        if not match:
            raise ValueError(f"No JSON exercise catalog found in {spec_file}")

        module_exercises = json.loads(match.group(1))
        for exercise in module_exercises:
            missing = [field for field in REQUIRED_FIELDS if field not in exercise]
            if missing:
                raise ValueError(
                    f"{spec_file} exercise {exercise.get('id')} "
                    f"missing fields: {missing}"
                )

            exercise_id = str(exercise["id"])
            slug = str(exercise["slug"])
            if exercise_id in seen_ids:
                raise ValueError(f"Duplicate exercise id: {exercise_id}")
            if slug in seen_slugs:
                raise ValueError(f"Duplicate exercise slug: {slug}")
            seen_ids.add(exercise_id)
            seen_slugs.add(slug)
            exercises.append(exercise)

    return sorted(exercises, key=lambda item: str(item["id"]))


def file_stem(exercise: dict[str, object]) -> str:
    return f"{exercise['id']}-{exercise['slug']}"


def as_list_text(values: object) -> str:
    return ", ".join(str(value) for value in values)


def bullet_lines(values: object) -> str:
    return "\n".join(f"- {value}" for value in values)


def algorithm_steps(exercise: dict[str, object]) -> list[str]:
    slug = str(exercise["slug"])
    steps_by_slug = {
        "sum-two-numbers": [
            "Đọc hai số nguyên a và b từ input.",
            "Tính tổng bằng phép cộng.",
            "In tổng ra màn hình.",
        ],
        "area-rectangle": [
            "Đọc chiều dài và chiều rộng.",
            "Nhân hai giá trị để lấy diện tích.",
            "In diện tích.",
        ],
        "circle-circumference-area": [
            "Đọc bán kính r dưới dạng số thực.",
            "Tính chu vi bằng công thức 2 * pi * r.",
            "Tính diện tích bằng công thức pi * r * r.",
            "In hai kết quả với 2 chữ số thập phân.",
        ],
        "average-three-numbers": [
            "Đọc ba số thực.",
            "Cộng ba số lại.",
            "Chia tổng cho 3.",
            "In trung bình với 2 chữ số thập phân.",
        ],
        "perfect-square": [
            "Đọc số nguyên n.",
            "Tính căn bậc hai nguyên của n.",
            "Bình phương căn nguyên vừa tìm được.",
            "So sánh với n để quyết định YES hoặc NO.",
        ],
        "even-odd": [
            "Đọc số nguyên n.",
            "Tính n chia lấy dư cho 2.",
            "Nếu phần dư bằng 0 thì in EVEN.",
            "Ngược lại in ODD.",
        ],
        "min-max-three": [
            "Đọc ba số nguyên.",
            "Tìm giá trị nhỏ nhất.",
            "Tìm giá trị lớn nhất.",
            "In hai giá trị theo thứ tự nhỏ nhất rồi lớn nhất.",
        ],
        "leap-year": [
            "Đọc năm cần kiểm tra.",
            "Kiểm tra năm chia hết cho 400.",
            "Nếu không, kiểm tra năm chia hết cho 4 và không chia hết cho 100.",
            "In LEAP nếu một trong hai điều kiện đúng, ngược lại in COMMON.",
        ],
        "grade-classification": [
            "Đọc điểm dưới dạng số thực.",
            "Kiểm tra điểm có nằm ngoài khoảng 0 đến 10 hay không.",
            "So sánh điểm với từng ngưỡng từ cao xuống thấp.",
            "In nhãn phân loại tương ứng.",
        ],
        "triangle-type": [
            "Đọc ba cạnh và sắp xếp theo thứ tự tăng dần.",
            "Kiểm tra cạnh nhỏ nhất có dương và hai cạnh nhỏ có lớn hơn cạnh lớn không.",
            "Nếu không hợp lệ thì in NOT TRIANGLE.",
            "Nếu hợp lệ, so sánh các cạnh để phân loại đều, cân hoặc thường.",
        ],
        "sum-1-to-n": [
            "Đọc số nguyên dương n.",
            "Khởi tạo biến tổng bằng 0.",
            "Duyệt các số từ 1 đến n và cộng vào tổng.",
            "In tổng cuối cùng.",
        ],
        "factorial": [
            "Đọc số nguyên không âm n.",
            "Khởi tạo kết quả bằng 1.",
            "Nhân kết quả lần lượt với các số từ 2 đến n.",
            "In kết quả.",
        ],
        "count-digits": [
            "Đọc số nguyên n và lấy trị tuyệt đối.",
            "Nếu n bằng 0 thì số chữ số là 1.",
            "Nếu không, lặp khi n còn lớn hơn 0.",
            "Mỗi vòng chia nguyên n cho 10 và tăng biến đếm.",
        ],
        "prime-number": [
            "Đọc số nguyên n.",
            "Nếu n nhỏ hơn 2 thì không phải số nguyên tố.",
            "Kiểm tra các ước từ 2 đến căn bậc hai của n.",
            "Nếu tìm thấy ước thì in NO, nếu không thì in YES.",
        ],
        "gcd-euclid": [
            "Đọc hai số nguyên a và b rồi lấy trị tuyệt đối.",
            "Lặp khi b khác 0.",
            "Thay a bằng b và b bằng a chia lấy dư cho b.",
            "Khi vòng lặp dừng, a là ước chung lớn nhất.",
        ],
        "count-vowels": [
            "Đọc chuỗi đầu vào.",
            "Chuyển từng ký tự về chữ thường khi kiểm tra.",
            "Nếu ký tự thuộc tập nguyên âm thì tăng biến đếm.",
            "In số lượng nguyên âm.",
        ],
        "palindrome-string": [
            "Đọc chuỗi đầu vào.",
            "Giữ lại các ký tự chữ hoặc số và chuyển về chữ thường.",
            "So sánh chuỗi đã chuẩn hóa với phiên bản đảo ngược.",
            "In YES nếu giống nhau, ngược lại in NO.",
        ],
        "normalize-full-name": [
            "Đọc họ tên.",
            "Tách chuỗi thành các từ, tự động bỏ khoảng trắng thừa.",
            "Chuẩn hóa từng từ về dạng chữ cái đầu viết hoa.",
            "Ghép các từ bằng một dấu cách.",
        ],
        "word-count": [
            "Đọc câu đầu vào.",
            "Dùng split để tách theo khoảng trắng.",
            "Đếm số phần tử sau khi tách.",
            "In kết quả.",
        ],
        "caesar-cipher": [
            "Đọc chuỗi cần mã hóa và độ dịch shift.",
            "Duyệt từng ký tự trong chuỗi.",
            "Nếu là chữ cái, dịch vòng trong bảng chữ cái phù hợp với hoa hoặc thường.",
            "Nếu không phải chữ cái, giữ nguyên.",
            "Ghép các ký tự đã xử lý và in kết quả.",
        ],
        "sum-list": [
            "Đọc n và list gồm n số nguyên.",
            "Khởi tạo tổng bằng 0 hoặc dùng hàm sum.",
            "Cộng toàn bộ phần tử trong list.",
            "In tổng.",
        ],
        "max-min-list": [
            "Đọc n và list gồm n số nguyên.",
            "Tìm giá trị nhỏ nhất.",
            "Tìm giá trị lớn nhất.",
            "In hai giá trị.",
        ],
        "count-frequency": [
            "Đọc n và list gồm n số nguyên.",
            "Duyệt list và cập nhật số lần xuất hiện trong dictionary.",
            "Duyệt các khóa đã sắp xếp tăng dần.",
            "In mỗi giá trị cùng tần suất của nó.",
        ],
        "remove-duplicates": [
            "Đọc n và list gồm n số nguyên.",
            "Tạo set để ghi nhớ giá trị đã gặp.",
            "Duyệt list theo thứ tự ban đầu.",
            "Nếu giá trị chưa gặp, thêm vào kết quả và đánh dấu đã gặp.",
            "In list kết quả.",
        ],
        "second-largest": [
            "Đọc n và list gồm n số nguyên.",
            "Loại trùng các giá trị.",
            "Sắp xếp các giá trị khác nhau theo thứ tự giảm dần.",
            "Nếu có ít nhất hai giá trị, in giá trị thứ hai; ngược lại in thông báo.",
        ],
        "temperature-converter": [
            "Đọc nhiệt độ Celsius.",
            "Gọi hàm chuyển đổi sang Fahrenheit.",
            "Trong hàm, áp dụng công thức C * 9 / 5 + 32.",
            "In kết quả với 2 chữ số thập phân.",
        ],
        "fibonacci-function": [
            "Đọc chỉ số n.",
            "Gọi hàm fibonacci(n).",
            "Trong hàm, xử lý trực tiếp n bằng 0 hoặc 1.",
            "Dùng hai biến để cập nhật hai số Fibonacci liên tiếp.",
            "Trả về F_n và in kết quả.",
        ],
        "valid-password": [
            "Đọc mật khẩu.",
            "Gọi hàm kiểm tra mật khẩu.",
            "Kiểm tra độ dài và từng nhóm ký tự bắt buộc.",
            "Trả về True nếu mọi điều kiện đều đúng.",
            "In VALID hoặc INVALID.",
        ],
        "linear-search-function": [
            "Đọc n, list số nguyên và target.",
            "Gọi hàm linear_search.",
            "Duyệt list bằng enumerate để có cả chỉ số và giá trị.",
            "Trả về chỉ số đầu tiên khi tìm thấy target.",
            "Nếu duyệt hết mà không thấy, trả về -1.",
        ],
        "quadratic-equation": [
            "Đọc ba hệ số a, b, c.",
            "Nếu a bằng 0, xử lý như phương trình bậc nhất hoặc hằng.",
            "Nếu a khác 0, tính delta = b^2 - 4ac.",
            "Dựa trên delta để xác định vô nghiệm thực, nghiệm kép hoặc hai nghiệm.",
            "Tính nghiệm và in theo định dạng yêu cầu.",
        ],
    }
    return steps_by_slug[slug]


def pseudocode(exercise: dict[str, object]) -> str:
    steps = algorithm_steps(exercise)
    lines = ["BEGIN"]
    for step in steps:
        lines.append(f"  {step}")
    lines.append("END")
    return "\n".join(lines)


def solution_code(slug: str) -> str:
    solutions = {
        "sum-two-numbers": r'''
            import sys


            def add_numbers(a: int, b: int) -> int:
                """Return the sum of two integers."""
                return a + b


            def main() -> None:
                # Read both numbers from one line.
                a, b = map(int, sys.stdin.read().split())
                print(add_numbers(a, b))


            if __name__ == "__main__":
                main()
        ''',
        "area-rectangle": r'''
            import sys


            def rectangle_area(length: int, width: int) -> int:
                """Return the area of a rectangle."""
                return length * width


            def main() -> None:
                # Input contains length and width.
                length, width = map(int, sys.stdin.read().split())
                print(rectangle_area(length, width))


            if __name__ == "__main__":
                main()
        ''',
        "circle-circumference-area": r'''
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
        ''',
        "average-three-numbers": r'''
            import sys


            def average_three(a: float, b: float, c: float) -> float:
                """Return the arithmetic mean of three numbers."""
                return (a + b + c) / 3


            def main() -> None:
                a, b, c = map(float, sys.stdin.read().split())
                print(f"{average_three(a, b, c):.2f}")


            if __name__ == "__main__":
                main()
        ''',
        "perfect-square": r'''
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
        ''',
        "even-odd": r'''
            import sys


            def is_even(number: int) -> bool:
                """Return True when number is even."""
                return number % 2 == 0


            def main() -> None:
                number = int(sys.stdin.read().strip())
                print("EVEN" if is_even(number) else "ODD")


            if __name__ == "__main__":
                main()
        ''',
        "min-max-three": r'''
            import sys


            def min_max_three(values: list[int]) -> tuple[int, int]:
                """Return the smallest and largest values."""
                return min(values), max(values)


            def main() -> None:
                values = list(map(int, sys.stdin.read().split()))
                smallest, largest = min_max_three(values)
                print(f"{smallest} {largest}")


            if __name__ == "__main__":
                main()
        ''',
        "leap-year": r'''
            import sys


            def is_leap_year(year: int) -> bool:
                """Return True for a Gregorian leap year."""
                return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


            def main() -> None:
                year = int(sys.stdin.read().strip())
                print("LEAP" if is_leap_year(year) else "COMMON")


            if __name__ == "__main__":
                main()
        ''',
        "grade-classification": r'''
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
        ''',
        "triangle-type": r'''
            import sys


            def classify_triangle(a: int, b: int, c: int) -> str:
                """Return the triangle type for three side lengths."""
                sides = sorted([a, b, c])
                x, y, z = sides
                if x <= 0 or x + y <= z:
                    return "NOT TRIANGLE"
                if x == z:
                    return "EQUILATERAL"
                if x == y or y == z:
                    return "ISOSCELES"
                return "SCALENE"


            def main() -> None:
                a, b, c = map(int, sys.stdin.read().split())
                print(classify_triangle(a, b, c))


            if __name__ == "__main__":
                main()
        ''',
        "sum-1-to-n": r'''
            import sys


            def sum_to_n(number: int) -> int:
                """Return 1 + 2 + ... + number."""
                total = 0
                for value in range(1, number + 1):
                    total += value
                return total


            def main() -> None:
                number = int(sys.stdin.read().strip())
                print(sum_to_n(number))


            if __name__ == "__main__":
                main()
        ''',
        "factorial": r'''
            import sys


            def factorial(number: int) -> int:
                """Return number factorial."""
                result = 1
                for value in range(2, number + 1):
                    result *= value
                return result


            def main() -> None:
                number = int(sys.stdin.read().strip())
                print(factorial(number))


            if __name__ == "__main__":
                main()
        ''',
        "count-digits": r'''
            import sys


            def count_digits(number: int) -> int:
                """Return the number of decimal digits."""
                number = abs(number)
                if number == 0:
                    return 1

                count = 0
                while number > 0:
                    count += 1
                    number //= 10
                return count


            def main() -> None:
                number = int(sys.stdin.read().strip())
                print(count_digits(number))


            if __name__ == "__main__":
                main()
        ''',
        "prime-number": r'''
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
        ''',
        "gcd-euclid": r'''
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
        ''',
        "count-vowels": r'''
            import sys


            def count_vowels(text: str) -> int:
                """Count English vowels in text."""
                vowels = set("aeiou")
                count = 0
                for character in text.lower():
                    if character in vowels:
                        count += 1
                return count


            def main() -> None:
                text = sys.stdin.read().rstrip("\n")
                print(count_vowels(text))


            if __name__ == "__main__":
                main()
        ''',
        "palindrome-string": r'''
            import sys


            def normalize(text: str) -> str:
                """Keep only alphanumeric characters and lowercase them."""
                return "".join(
                    character.lower()
                    for character in text
                    if character.isalnum()
                )


            def is_palindrome(text: str) -> bool:
                """Return True when normalized text is a palindrome."""
                cleaned = normalize(text)
                return cleaned == cleaned[::-1]


            def main() -> None:
                text = sys.stdin.read().rstrip("\n")
                print("YES" if is_palindrome(text) else "NO")


            if __name__ == "__main__":
                main()
        ''',
        "normalize-full-name": r'''
            import sys


            def normalize_name(name: str) -> str:
                """Normalize spaces and capitalization in a full name."""
                words = name.split()
                normalized_words = [word.lower().capitalize() for word in words]
                return " ".join(normalized_words)


            def main() -> None:
                name = sys.stdin.read()
                print(normalize_name(name))


            if __name__ == "__main__":
                main()
        ''',
        "word-count": r'''
            import sys


            def count_words(text: str) -> int:
                """Return the number of whitespace-separated words."""
                return len(text.split())


            def main() -> None:
                text = sys.stdin.read()
                print(count_words(text))


            if __name__ == "__main__":
                main()
        ''',
        "caesar-cipher": r'''
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
        ''',
        "sum-list": r'''
            import sys


            def sum_list(numbers: list[int]) -> int:
                """Return the sum of all numbers."""
                total = 0
                for number in numbers:
                    total += number
                return total


            def main() -> None:
                data = sys.stdin.read().split()
                count = int(data[0])
                numbers = list(map(int, data[1:1 + count]))
                print(sum_list(numbers))


            if __name__ == "__main__":
                main()
        ''',
        "max-min-list": r'''
            import sys


            def min_max(numbers: list[int]) -> tuple[int, int]:
                """Return the smallest and largest numbers."""
                return min(numbers), max(numbers)


            def main() -> None:
                data = sys.stdin.read().split()
                count = int(data[0])
                numbers = list(map(int, data[1:1 + count]))
                smallest, largest = min_max(numbers)
                print(f"{smallest} {largest}")


            if __name__ == "__main__":
                main()
        ''',
        "count-frequency": r'''
            import sys


            def count_frequency(numbers: list[int]) -> dict[int, int]:
                """Return a frequency table for numbers."""
                frequency: dict[int, int] = {}
                for number in numbers:
                    frequency[number] = frequency.get(number, 0) + 1
                return frequency


            def main() -> None:
                data = sys.stdin.read().split()
                count = int(data[0])
                numbers = list(map(int, data[1:1 + count]))
                frequency = count_frequency(numbers)
                lines = [
                    f"{number} {frequency[number]}"
                    for number in sorted(frequency)
                ]
                sys.stdout.write("\n".join(lines))


            if __name__ == "__main__":
                main()
        ''',
        "remove-duplicates": r'''
            import sys


            def remove_duplicates(numbers: list[int]) -> list[int]:
                """Remove duplicates while keeping first appearance order."""
                seen: set[int] = set()
                result: list[int] = []
                for number in numbers:
                    if number not in seen:
                        seen.add(number)
                        result.append(number)
                return result


            def main() -> None:
                data = sys.stdin.read().split()
                count = int(data[0])
                numbers = list(map(int, data[1:1 + count]))
                result = remove_duplicates(numbers)
                print(" ".join(map(str, result)))


            if __name__ == "__main__":
                main()
        ''',
        "second-largest": r'''
            import sys


            def second_largest(numbers: list[int]) -> int | None:
                """Return the second distinct largest value if it exists."""
                unique_values = sorted(set(numbers), reverse=True)
                if len(unique_values) < 2:
                    return None
                return unique_values[1]


            def main() -> None:
                data = sys.stdin.read().split()
                count = int(data[0])
                numbers = list(map(int, data[1:1 + count]))
                result = second_largest(numbers)
                if result is None:
                    print("NO SECOND LARGEST")
                else:
                    print(result)


            if __name__ == "__main__":
                main()
        ''',
        "temperature-converter": r'''
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
        ''',
        "fibonacci-function": r'''
            import sys


            def fibonacci(index: int) -> int:
                """Return the Fibonacci number at zero-based index."""
                if index == 0:
                    return 0
                previous, current = 0, 1
                for _ in range(2, index + 1):
                    previous, current = current, previous + current
                return current


            def main() -> None:
                index = int(sys.stdin.read().strip())
                print(fibonacci(index))


            if __name__ == "__main__":
                main()
        ''',
        "valid-password": r'''
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
        ''',
        "linear-search-function": r'''
            import sys


            def linear_search(numbers: list[int], target: int) -> int:
                """Return the first index of target, or -1."""
                for index, number in enumerate(numbers):
                    if number == target:
                        return index
                return -1


            def main() -> None:
                data = sys.stdin.read().split()
                count = int(data[0])
                numbers = list(map(int, data[1:1 + count]))
                target = int(data[1 + count])
                print(linear_search(numbers, target))


            if __name__ == "__main__":
                main()
        ''',
        "quadratic-equation": r'''
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
        ''',
    }
    return dedent(solutions[slug]).strip() + "\n"


def render_exercise(exercise: dict[str, object]) -> str:
    return dedent(
        f"""
        # {exercise['id']}. {exercise['title']}

        ## Module

        {exercise['module']}

        ## Difficulty

        {exercise['difficulty']}

        ## Exercise Type

        {exercise['exercise_type']}

        ## Prerequisites

        {bullet_lines(exercise['prerequisites'])}

        ## Python Topics

        {bullet_lines(exercise['python_topics'])}

        ## Math Or Reasoning Topics

        {bullet_lines(exercise['math_topics'])}

        ## Problem Statement

        {exercise['problem']}

        ## Input

        {exercise['input']}

        ## Output

        {exercise['output']}

        ## Example

        ### Sample Input

        ```text
        {exercise['sample_input']}
        ```

        ### Sample Output

        ```text
        {exercise['sample_output']}
        ```

        ### Explanation

        {exercise['sample_explanation']}

        > This exercise file intentionally contains no solution. Solutions are
        > generated separately in `generated/solutions/`.
        """
    ).strip() + "\n"


def render_example(exercise: dict[str, object]) -> str:
    return dedent(
        f"""
        # {exercise['id']}. {exercise['title']} - Examples

        ## Sample Input

        ```text
        {exercise['sample_input']}
        ```

        ## Sample Output

        ```text
        {exercise['sample_output']}
        ```

        ## Explanation

        {exercise['sample_explanation']}

        This example follows the exact input and output contract from the
        exercise specification. When testing locally, provide the sample input
        through standard input and compare the printed result with the sample
        output shown above.
        """
    ).strip() + "\n"


def render_lesson(exercise: dict[str, object]) -> str:
    slug = str(exercise["slug"])
    module = str(exercise["module"])
    python_topics = as_list_text(exercise["python_topics"])
    math_topics = as_list_text(exercise["math_topics"])
    prerequisites = as_list_text(exercise["prerequisites"])
    steps = algorithm_steps(exercise)
    algorithm = "\n".join(f"{index}. {step}" for index, step in enumerate(steps, 1))
    code = solution_code(slug)

    lesson = dedent(
        f"""
        # {exercise['id']}. {exercise['title']}

        # Learning Objectives

        Sau bài học này, bạn cần đạt được bốn mục tiêu. Thứ nhất, bạn hiểu đề bài
        `{exercise['title']}` không chỉ như một yêu cầu tính kết quả, mà như một
        đặc tả nhỏ gồm dữ liệu vào, dữ liệu ra và quy tắc xử lý. Thứ hai, bạn biết
        sử dụng các kiến thức Python liên quan: {python_topics}. Thứ ba, bạn kết
        nối được phần lập trình với nền tảng toán học hoặc tư duy logic: {math_topics}.
        Thứ tư, bạn có thể tự viết lại lời giải theo từng bước, kiểm tra bằng ví dụ
        mẫu, rồi điều chỉnh nếu gặp dữ liệu khác.

        Bài học cũng rèn thói quen đọc kỹ input và output trước khi viết code. Với
        người mới học, lỗi thường không nằm ở cú pháp phức tạp mà nằm ở việc hiểu
        sai đề: đọc thiếu một dòng, in thừa chữ, làm tròn sai định dạng, hoặc dùng
        nhầm kiểu dữ liệu. Vì vậy, mục tiêu quan trọng là xây dựng quy trình làm bài:
        xác định dữ liệu, chọn biến, viết thuật toán, chuyển thuật toán thành Python,
        chạy thử với ví dụ, sau đó nghĩ thêm về các trường hợp biên.

        # Theory

        {MODULE_THEORY[module]}

        Trong bài này, các chủ đề Python chính là {python_topics}. Bạn không nên
        học chúng như những lệnh rời rạc. Hãy xem mỗi chủ đề là một công cụ trong
        một chuỗi xử lý. `input()` hoặc `sys.stdin.read()` đưa dữ liệu thô vào chương
        trình dưới dạng chuỗi. Các hàm chuyển kiểu như `int()` và `float()` biến dữ
        liệu đó thành dạng có thể tính toán. Các toán tử, điều kiện, vòng lặp, list
        hoặc hàm sẽ thực hiện logic chính. Cuối cùng, `print()` hoặc `sys.stdout.write()`
        biến kết quả thành văn bản để người chấm hoặc người dùng đọc được.

        Một thói quen tốt là đặt tên biến theo ý nghĩa của dữ liệu, không đặt theo
        cảm hứng nhất thời. Nếu đề nói đến bán kính, hãy dùng `radius`; nếu đề nói
        đến danh sách số, hãy dùng `numbers`; nếu đề nói đến mục tiêu tìm kiếm, hãy
        dùng `target`. Tên biến rõ giúp bạn giảm gánh nặng ghi nhớ. Khi quay lại bài
        sau vài ngày, bạn vẫn hiểu code đang làm gì mà không cần đọc từng toán tử.

        Cũng cần phân biệt giữa code chạy được và code dễ học. Một dòng Python quá
        ngắn đôi khi tạo cảm giác giỏi, nhưng với người mới, việc tách thành hàm nhỏ
        hoặc biến trung gian thường hữu ích hơn. Biến trung gian cho phép bạn đặt
        tên cho từng ý tưởng: dữ liệu đã chuẩn hóa, tổng hiện tại, căn bậc hai,
        kết quả phân loại. Khi thuật toán rõ ràng, Python chỉ còn là cách diễn đạt.

        Hãy tưởng tượng chương trình như một quầy xử lý hồ sơ. Input là hồ sơ được
        đưa vào quầy. Phần xử lý kiểm tra giấy tờ, tính toán hoặc phân loại. Output
        là kết quả trả lại. Nếu hồ sơ đầu vào chưa được chuyển đúng dạng, bước xử lý
        phía sau sẽ sai. Nếu quy tắc xử lý không rõ, kết quả trả ra có thể hợp cú
        pháp nhưng sai nghiệp vụ. Lập trình tốt bắt đầu từ việc kiểm soát luồng này.

        # Mathematical Background

        Phần toán học hoặc tư duy nền tảng của bài là: {math_topics}. Với các bài
        cơ bản, toán học thường là công thức quen thuộc. Với các bài điều kiện, toán
        học nằm trong quy tắc phân loại. Với vòng lặp, toán học xuất hiện ở mẫu lặp,
        biến tích lũy và điều kiện dừng. Với chuỗi và list, tư duy quan trọng là xem
        dữ liệu như một dãy phần tử rồi xử lý từng phần tử theo cùng một tiêu chí.

        Khi gặp một bài toán như `{exercise['title']}`, bạn nên tự hỏi: đại lượng nào
        đã biết, đại lượng nào cần tìm, và quan hệ giữa chúng là gì. Nếu có công thức,
        hãy viết công thức bằng lời trước. Nếu có quy tắc, hãy liệt kê từng trường hợp.
        Nếu phải duyệt dữ liệu, hãy xác định mỗi vòng lặp cần cập nhật thông tin nào.
        Cách suy nghĩ này giúp bạn không bị cuốn vào việc gõ code quá sớm.

        Một điểm quan trọng khác là trường hợp biên. Trường hợp biên là dữ liệu vẫn
        hợp lệ nhưng dễ làm chương trình sai, ví dụ số 0, list chỉ có một phần tử,
        chuỗi rỗng, số âm, điểm đúng bằng ngưỡng, hoặc phương trình có delta bằng 0.
        Không phải bài nào cũng có tất cả các trường hợp này, nhưng thói quen nghĩ
        về chúng sẽ giúp bạn viết chương trình ổn định hơn.

        # Problem Statement

        {exercise['problem']}

        Hãy đọc câu trên như một hợp đồng. Chương trình của bạn nhận đúng dữ liệu
        được mô tả, xử lý đúng quy tắc, và chỉ in đúng kết quả được yêu cầu. Trong
        môi trường học thuật hoặc chấm tự động, việc in thêm lời chào, chú thích,
        hoặc đơn vị không được yêu cầu đều có thể khiến bài bị sai dù thuật toán đúng.

        # Input

        {exercise['input']}

        Trước khi parse input, hãy xác định dữ liệu gồm bao nhiêu dòng và mỗi dòng
        có bao nhiêu phần. Nếu dữ liệu nằm trên một dòng, `split()` thường đủ. Nếu
        dữ liệu có thể chứa cả khoảng trắng như một câu hoặc họ tên, bạn cần đọc cả
        dòng hoặc toàn bộ nội dung thay vì tách quá sớm.

        # Output

        {exercise['output']}

        Output là phần dễ bị xem nhẹ. Bạn cần chú ý chữ hoa chữ thường, số chữ số
        thập phân, thứ tự in kết quả và việc có hay không có dấu cách cuối dòng. Với
        số thực, định dạng như `{{value:.2f}}` giúp kết quả thống nhất và dễ so sánh.

        # Example

        Sample Input:

        ```text
        {exercise['sample_input']}
        ```

        Sample Output:

        ```text
        {exercise['sample_output']}
        ```

        Explanation:

        {exercise['sample_explanation']}

        Ví dụ mẫu không chỉ để minh họa. Nó là bài kiểm tra đầu tiên cho chương trình.
        Nếu chương trình không tạo ra đúng output mẫu, hãy kiểm tra lại từng bước:
        đọc input có đúng không, kiểu dữ liệu có đúng không, công thức hoặc điều kiện
        có đúng không, và định dạng in ra có khớp yêu cầu không.

        # Algorithm

        {algorithm}

        Thuật toán trên được viết bằng ngôn ngữ tự nhiên để bạn nhìn thấy ý tưởng
        trước khi nhìn thấy Python. Khi tự luyện tập, hãy cố gắng viết phần này ra
        giấy hoặc ghi chú trước. Nếu bạn không thể mô tả thuật toán bằng lời, việc
        viết code thường sẽ biến thành thử sai. Ngược lại, khi các bước đã rõ, mỗi
        dòng code chỉ cần bám theo một bước cụ thể.

        # Pseudocode

        ```text
        {pseudocode(exercise)}
        ```

        Pseudocode là cầu nối giữa ý tưởng và Python. Nó bỏ qua chi tiết cú pháp,
        nhưng vẫn giữ thứ tự xử lý. Với người mới, pseudocode giúp giảm áp lực phải
        nhớ chính xác dấu ngoặc, dấu hai chấm hoặc tên hàm ngay từ đầu.

        # Python Solution

        ```python
        {code}
        ```

        # Code Explanation

        Lời giải Python được viết theo cấu trúc có hàm xử lý và hàm `main()`. Hàm xử
        lý chứa logic chính của bài, còn `main()` chịu trách nhiệm đọc input và in
        output. Cách tách này giúp bạn kiểm tra logic dễ hơn. Nếu muốn thử nhiều bộ
        dữ liệu, bạn có thể gọi trực tiếp hàm xử lý trong Python shell hoặc trong
        một file test nhỏ mà không cần nhập lại từ bàn phím.

        Các dòng đọc dữ liệu dùng đúng định dạng input của bài. Khi đề yêu cầu số
        nguyên, chương trình chuyển sang `int`; khi đề yêu cầu số thực, chương trình
        chuyển sang `float`; khi đề xử lý văn bản, chương trình giữ dữ liệu ở dạng
        chuỗi. Đây là bước rất quan trọng vì Python không tự đoán rằng chuỗi `"5"`
        nên được cộng như số 5. Nếu quên chuyển kiểu, phép cộng có thể trở thành nối
        chuỗi hoặc gây lỗi.

        Phần xử lý chính bám sát thuật toán đã nêu. Với bài tính toán, code thường
        dùng công thức trực tiếp. Với bài điều kiện, code dùng các nhánh rõ ràng để
        tránh nhập nhằng. Với bài vòng lặp, code khởi tạo biến trước vòng lặp, cập
        nhật biến trong vòng lặp, rồi trả về kết quả sau khi vòng lặp kết thúc. Với
        bài list hoặc chuỗi, code duyệt từng phần tử và chỉ lưu thêm dữ liệu khi cần.

        Các comment trong solution chỉ xuất hiện ở nơi giúp người học định hướng.
        Không phải dòng nào cũng cần comment. Ví dụ, `return a + b` đã đủ rõ, nhưng
        một bước như chuẩn hóa chuỗi, cập nhật dictionary tần suất, hoặc xử lý phương
        trình suy biến nên có tên hàm hoặc comment rõ hơn. Comment tốt giải thích
        lý do hoặc ý tưởng, không lặp lại máy móc điều code đã nói.

        # Complexity Analysis

        Độ phức tạp thời gian phụ thuộc vào số lượng phần tử mà chương trình phải
        xử lý. Nếu bài chỉ đọc vài số cố định và áp dụng công thức, thời gian là
        O(1). Nếu bài duyệt từ 1 đến n, thời gian thường là O(n). Nếu bài duyệt một
        chuỗi hoặc list có n phần tử, thời gian cũng thường là O(n). Nếu có sắp xếp,
        thời gian có thể là O(n log n). Với bài này, hãy nhìn vào vòng lặp hoặc thao
        tác sắp xếp trong code để xác định chi phí chính.

        Độ phức tạp bộ nhớ cho biết chương trình cần thêm bao nhiêu bộ nhớ ngoài dữ
        liệu đầu vào. Nếu chỉ dùng vài biến, bộ nhớ phụ là O(1). Nếu tạo list kết quả,
        set các giá trị đã gặp, hoặc dictionary tần suất, bộ nhớ phụ có thể là O(n).
        Việc hiểu complexity không chỉ để thi thuật toán; nó giúp bạn dự đoán chương
        trình có còn chạy tốt khi dữ liệu lớn hơn ví dụ mẫu hay không.

        # Common Mistakes

        Một lỗi phổ biến là đọc input sai dạng. Nếu đề có nhiều số trên một dòng mà
        bạn chỉ gọi `input()` một lần nhưng không `split()`, chương trình sẽ không có
        đủ dữ liệu. Ngược lại, nếu đề là một câu văn có khoảng trắng mà bạn dùng
        `split()` ngay, bạn có thể làm mất cấu trúc ban đầu của chuỗi.

        Lỗi thứ hai là dùng sai kiểu dữ liệu. Số thực cần `float`, số nguyên cần
        `int`, còn chuỗi cần được giữ nguyên khi bài yêu cầu xử lý ký tự. Lỗi thứ ba
        là in sai định dạng: thiếu chữ hoa, thừa dấu cách, hoặc không làm tròn số
        thực đúng yêu cầu. Lỗi thứ tư là bỏ qua trường hợp biên như 0, dữ liệu chỉ
        có một phần tử, hoặc giá trị nằm đúng trên ngưỡng so sánh.

        Khi debug, đừng sửa ngẫu nhiên nhiều chỗ cùng lúc. Hãy in thử dữ liệu sau khi
        đọc, kiểm tra biến trung gian, rồi đối chiếu từng bước với thuật toán. Sau
        khi hiểu lỗi, hãy bỏ các dòng in thử để output cuối cùng sạch và đúng đặc tả.

        # Additional Exercises

        1. Thay đổi dữ liệu mẫu và tự dự đoán output trước khi chạy chương trình.
        2. Viết thêm ít nhất ba test case, trong đó có một trường hợp biên.
        3. Tách phần xử lý thành hàm riêng nếu solution hiện tại chưa có hàm.
        4. Viết lại thuật toán bằng lời của bạn mà không nhìn vào bài học.
        5. Mở rộng bài toán bằng cách xử lý nhiều bộ test liên tiếp.

        # Further Reading

        Để học sâu hơn, hãy đọc lại tài liệu Python về các chủ đề: {python_topics}.
        Sau đó xem lại phần toán hoặc tư duy nền tảng: {math_topics}. Bạn cũng nên
        luyện lại các kiến thức tiên quyết: {prerequisites}. Khi gặp bài tương tự,
        hãy bắt đầu từ đặc tả input/output, viết thuật toán ngắn, sau đó mới chuyển
        sang Python. Đây là quy trình quan trọng hơn việc ghi nhớ một lời giải cụ
        thể, vì nó giúp bạn tự giải được bài mới.
        """
    ).strip() + "\n"

    word_count = len(re.findall(r"\b[\wÀ-ỹ]+\b", lesson, flags=re.UNICODE))
    if word_count < 1000:
        raise ValueError(
            f"Lesson {exercise['id']} has only {word_count} words; "
            "minimum is 1000."
        )
    return lesson


def reset_generated_dirs() -> dict[str, Path]:
    dirs = {
        "lessons": GENERATED_DIR / "lessons",
        "exercises": GENERATED_DIR / "exercises",
        "solutions": GENERATED_DIR / "solutions",
        "examples": GENERATED_DIR / "examples",
    }
    for directory in dirs.values():
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True, exist_ok=True)
    return dirs


def write_outputs(exercises: list[dict[str, object]]) -> None:
    dirs = reset_generated_dirs()
    for exercise in exercises:
        stem = file_stem(exercise)
        slug = str(exercise["slug"])

        (dirs["lessons"] / f"{stem}.md").write_text(
            render_lesson(exercise), encoding="utf-8"
        )
        (dirs["exercises"] / f"{stem}.md").write_text(
            render_exercise(exercise), encoding="utf-8"
        )
        solution_path = dirs["solutions"] / f"{stem}.py"
        source_code = solution_code(slug)
        solution_path.write_text(source_code, encoding="utf-8")
        (dirs["examples"] / f"{stem}-examples.md").write_text(
            render_example(exercise), encoding="utf-8"
        )

        compile(source_code, str(solution_path), "exec")


def main() -> None:
    exercises = parse_curriculum()
    write_outputs(exercises)
    print(f"Generated {len(exercises)} exercises into {GENERATED_DIR}")


if __name__ == "__main__":
    main()
