# Module 01: Basic Math

## Mục tiêu học tập

- Làm quen với cách đọc dữ liệu bằng `input()` và in kết quả bằng `print()`.
- Hiểu biến, kiểu số nguyên, kiểu số thực và cách chuyển kiểu dữ liệu.
- Sử dụng các toán tử số học cơ bản trong Python.
- Biết cách diễn đạt một bài toán số học thành các bước xử lý rõ ràng.

## Kiến thức Python cần học

- Biến và phép gán.
- `int()`, `float()`, `str()`.
- Toán tử `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- Làm tròn và định dạng số bằng f-string.
- Cấu trúc chương trình tuyến tính.

## Các dạng bài

- Tính tổng, hiệu, tích, thương.
- Tính diện tích và chu vi.
- Tính trung bình cộng.
- Kiểm tra tính chất số học đơn giản.
- Áp dụng công thức toán học cơ bản.

## Độ khó

Easy đến Easy-Medium.

## Kiến thức tiên quyết

- Biết mở file Python và chạy chương trình.
- Biết khái niệm số nguyên và số thực.
- Biết đọc đề bài, xác định dữ liệu vào và dữ liệu ra.

## Danh sách bài tập

```json
[
  {
    "id": "001",
    "slug": "sum-two-numbers",
    "title": "Tổng hai số",
    "module": "Basic Math",
    "difficulty": "Easy",
    "exercise_type": "Tính toán cơ bản",
    "prerequisites": ["Biến", "Số nguyên", "input()", "print()"],
    "python_topics": ["int()", "split()", "toán tử +"],
    "math_topics": ["Phép cộng số nguyên"],
    "problem": "Nhập hai số nguyên a và b, sau đó in ra tổng của chúng.",
    "input": "Một dòng gồm hai số nguyên a và b, cách nhau bởi dấu cách.",
    "output": "Một số nguyên duy nhất là a + b.",
    "sample_input": "3 5",
    "sample_output": "8",
    "sample_explanation": "Tổng của 3 và 5 là 8."
  },
  {
    "id": "002",
    "slug": "area-rectangle",
    "title": "Diện tích hình chữ nhật",
    "module": "Basic Math",
    "difficulty": "Easy",
    "exercise_type": "Áp dụng công thức hình học",
    "prerequisites": ["Biến", "Số nguyên", "Phép nhân"],
    "python_topics": ["int()", "split()", "toán tử *"],
    "math_topics": ["Diện tích hình chữ nhật"],
    "problem": "Nhập chiều dài và chiều rộng của một hình chữ nhật, sau đó in ra diện tích.",
    "input": "Một dòng gồm hai số nguyên dương length và width.",
    "output": "Một số nguyên là diện tích hình chữ nhật.",
    "sample_input": "7 4",
    "sample_output": "28",
    "sample_explanation": "Diện tích bằng chiều dài nhân chiều rộng: 7 * 4 = 28."
  },
  {
    "id": "003",
    "slug": "circle-circumference-area",
    "title": "Chu vi và diện tích hình tròn",
    "module": "Basic Math",
    "difficulty": "Easy-Medium",
    "exercise_type": "Tính toán với số thực",
    "prerequisites": ["Số thực", "Hằng số pi", "Định dạng số"],
    "python_topics": ["float()", "math.pi", "f-string", "định dạng .2f"],
    "math_topics": ["Chu vi hình tròn", "Diện tích hình tròn"],
    "problem": "Nhập bán kính r của hình tròn, in ra chu vi và diện tích, mỗi giá trị làm tròn 2 chữ số thập phân.",
    "input": "Một số thực dương r.",
    "output": "Hai số thực: chu vi và diện tích, cách nhau bởi dấu cách, làm tròn 2 chữ số thập phân.",
    "sample_input": "2",
    "sample_output": "12.57 12.57",
    "sample_explanation": "Với r = 2, chu vi = 2 * pi * r và diện tích = pi * r * r, cả hai xấp xỉ 12.57."
  },
  {
    "id": "004",
    "slug": "average-three-numbers",
    "title": "Trung bình cộng của ba số",
    "module": "Basic Math",
    "difficulty": "Easy",
    "exercise_type": "Tính trung bình",
    "prerequisites": ["Số thực", "Phép cộng", "Phép chia"],
    "python_topics": ["float()", "split()", "toán tử /", "định dạng .2f"],
    "math_topics": ["Trung bình cộng"],
    "problem": "Nhập ba số thực, sau đó in ra trung bình cộng của ba số đó với 2 chữ số thập phân.",
    "input": "Một dòng gồm ba số thực a, b và c.",
    "output": "Một số thực là trung bình cộng, làm tròn 2 chữ số thập phân.",
    "sample_input": "8 9 10",
    "sample_output": "9.00",
    "sample_explanation": "Trung bình cộng là (8 + 9 + 10) / 3 = 9."
  },
  {
    "id": "005",
    "slug": "perfect-square",
    "title": "Kiểm tra số chính phương",
    "module": "Basic Math",
    "difficulty": "Easy-Medium",
    "exercise_type": "Kiểm tra tính chất số học",
    "prerequisites": ["Số nguyên", "Căn bậc hai", "So sánh"],
    "python_topics": ["int()", "math.isqrt()", "if đơn giản"],
    "math_topics": ["Số chính phương", "Căn bậc hai nguyên"],
    "problem": "Nhập một số nguyên không âm n, kiểm tra n có phải là số chính phương hay không.",
    "input": "Một số nguyên không âm n.",
    "output": "In YES nếu n là số chính phương, ngược lại in NO.",
    "sample_input": "49",
    "sample_output": "YES",
    "sample_explanation": "49 = 7 * 7 nên 49 là số chính phương."
  }
]
```
