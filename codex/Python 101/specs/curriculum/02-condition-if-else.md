# Module 02: Condition If Else

## Mục tiêu học tập

- Hiểu biểu thức điều kiện và giá trị boolean.
- Sử dụng `if`, `elif`, `else` để rẽ nhánh chương trình.
- Kết hợp nhiều điều kiện bằng `and`, `or`, `not`.
- Biết kiểm tra dữ liệu và phân loại kết quả theo quy tắc.

## Kiến thức Python cần học

- Toán tử so sánh: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Câu lệnh `if`, `elif`, `else`.
- Toán tử logic.
- Điều kiện lồng nhau.
- Cách viết điều kiện rõ ràng, tránh trùng lặp.

## Các dạng bài

- Kiểm tra chẵn lẻ.
- Tìm giá trị lớn nhất hoặc nhỏ nhất.
- Kiểm tra năm nhuận.
- Phân loại điểm số.
- Kiểm tra điều kiện hình học.

## Độ khó

Easy đến Medium.

## Kiến thức tiên quyết

- Nắm biến, input, output.
- Biết các phép toán số học cơ bản.
- Biết cách so sánh hai giá trị.

## Danh sách bài tập

```json
[
  {
    "id": "006",
    "slug": "even-odd",
    "title": "Kiểm tra chẵn lẻ",
    "module": "Condition If Else",
    "difficulty": "Easy",
    "exercise_type": "Rẽ nhánh đơn",
    "prerequisites": ["Số nguyên", "Phép chia lấy dư", "if else"],
    "python_topics": ["toán tử %", "if", "else"],
    "math_topics": ["Tính chẵn lẻ"],
    "problem": "Nhập một số nguyên n, kiểm tra n là số chẵn hay số lẻ.",
    "input": "Một số nguyên n.",
    "output": "In EVEN nếu n chẵn, ngược lại in ODD.",
    "sample_input": "12",
    "sample_output": "EVEN",
    "sample_explanation": "12 chia hết cho 2 nên là số chẵn."
  },
  {
    "id": "007",
    "slug": "min-max-three",
    "title": "Tìm số nhỏ nhất và lớn nhất trong ba số",
    "module": "Condition If Else",
    "difficulty": "Easy",
    "exercise_type": "So sánh nhiều giá trị",
    "prerequisites": ["Số nguyên", "So sánh", "if elif else"],
    "python_topics": ["min()", "max()", "split()"],
    "math_topics": ["Thứ tự trên tập số nguyên"],
    "problem": "Nhập ba số nguyên a, b, c, sau đó in ra số nhỏ nhất và số lớn nhất.",
    "input": "Một dòng gồm ba số nguyên a, b và c.",
    "output": "Hai số nguyên: giá trị nhỏ nhất và giá trị lớn nhất.",
    "sample_input": "4 -2 9",
    "sample_output": "-2 9",
    "sample_explanation": "Trong ba số 4, -2 và 9, nhỏ nhất là -2 và lớn nhất là 9."
  },
  {
    "id": "008",
    "slug": "leap-year",
    "title": "Kiểm tra năm nhuận",
    "module": "Condition If Else",
    "difficulty": "Medium",
    "exercise_type": "Điều kiện kết hợp",
    "prerequisites": ["Số nguyên", "Phép chia hết", "and", "or"],
    "python_topics": ["if", "and", "or", "toán tử %"],
    "math_topics": ["Quy tắc năm nhuận Gregorian"],
    "problem": "Nhập một năm, kiểm tra năm đó có phải là năm nhuận theo lịch Gregorian hay không.",
    "input": "Một số nguyên year.",
    "output": "In LEAP nếu là năm nhuận, ngược lại in COMMON.",
    "sample_input": "2024",
    "sample_output": "LEAP",
    "sample_explanation": "2024 chia hết cho 4 và không chia hết cho 100 nên là năm nhuận."
  },
  {
    "id": "009",
    "slug": "grade-classification",
    "title": "Phân loại điểm số",
    "module": "Condition If Else",
    "difficulty": "Easy-Medium",
    "exercise_type": "Phân loại theo khoảng",
    "prerequisites": ["Số thực", "So sánh", "elif"],
    "python_topics": ["float()", "if", "elif", "else"],
    "math_topics": ["Khoảng giá trị"],
    "problem": "Nhập điểm số từ 0 đến 10 và phân loại kết quả học tập.",
    "input": "Một số thực score.",
    "output": "In INVALID nếu điểm ngoài khoảng 0 đến 10; EXCELLENT nếu điểm từ 8.5; GOOD nếu từ 7.0; AVERAGE nếu từ 5.0; ngược lại BELOW AVERAGE.",
    "sample_input": "8.7",
    "sample_output": "EXCELLENT",
    "sample_explanation": "8.7 nằm trong khoảng từ 8.5 đến 10 nên được phân loại EXCELLENT."
  },
  {
    "id": "010",
    "slug": "triangle-type",
    "title": "Phân loại tam giác",
    "module": "Condition If Else",
    "difficulty": "Medium",
    "exercise_type": "Kiểm tra điều kiện hình học",
    "prerequisites": ["Bất đẳng thức tam giác", "if elif else", "and"],
    "python_topics": ["int()", "sorted()", "if", "elif"],
    "math_topics": ["Bất đẳng thức tam giác", "Tam giác đều", "Tam giác cân", "Tam giác thường"],
    "problem": "Nhập ba cạnh của một tam giác, kiểm tra chúng có tạo thành tam giác không và phân loại tam giác.",
    "input": "Một dòng gồm ba số nguyên dương a, b và c.",
    "output": "In NOT TRIANGLE nếu không tạo thành tam giác; EQUILATERAL nếu tam giác đều; ISOSCELES nếu tam giác cân; SCALENE nếu tam giác thường.",
    "sample_input": "5 5 8",
    "sample_output": "ISOSCELES",
    "sample_explanation": "Ba cạnh 5, 5, 8 tạo thành tam giác và có hai cạnh bằng nhau."
  }
]
```
