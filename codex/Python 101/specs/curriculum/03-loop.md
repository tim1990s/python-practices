# Module 03: Loop

## Mục tiêu học tập

- Hiểu khi nào cần dùng vòng lặp thay vì viết lặp lại nhiều dòng code.
- Sử dụng `for` với `range()` và `while` cho các bài toán lặp chưa biết trước số bước.
- Biết tích lũy kết quả bằng biến đếm, biến tổng và biến trạng thái.
- Biết dừng vòng lặp đúng điều kiện và tránh vòng lặp vô hạn.

## Kiến thức Python cần học

- `for`, `while`.
- `range(start, stop, step)`.
- Biến đếm và biến tích lũy.
- `break`, `continue` ở mức cơ bản.
- Mẫu thuật toán kiểm tra số nguyên.

## Các dạng bài

- Tính tổng dãy số.
- Tính giai thừa.
- Đếm chữ số.
- Kiểm tra số nguyên tố.
- Tìm ước chung lớn nhất.

## Độ khó

Easy-Medium đến Medium.

## Kiến thức tiên quyết

- Thành thạo input/output.
- Biết câu lệnh điều kiện.
- Biết phép chia lấy dư và khái niệm ước số.

## Danh sách bài tập

```json
[
  {
    "id": "011",
    "slug": "sum-1-to-n",
    "title": "Tính tổng từ 1 đến n",
    "module": "Loop",
    "difficulty": "Easy",
    "exercise_type": "Tích lũy tổng",
    "prerequisites": ["Số nguyên dương", "Vòng lặp for", "Biến tổng"],
    "python_topics": ["for", "range()", "biến tích lũy"],
    "math_topics": ["Tổng cấp số cộng đơn giản"],
    "problem": "Nhập số nguyên dương n, tính tổng các số từ 1 đến n.",
    "input": "Một số nguyên dương n.",
    "output": "Một số nguyên là tổng 1 + 2 + ... + n.",
    "sample_input": "5",
    "sample_output": "15",
    "sample_explanation": "1 + 2 + 3 + 4 + 5 = 15."
  },
  {
    "id": "012",
    "slug": "factorial",
    "title": "Tính giai thừa",
    "module": "Loop",
    "difficulty": "Easy-Medium",
    "exercise_type": "Tích lũy tích",
    "prerequisites": ["Số nguyên không âm", "Vòng lặp for", "Phép nhân"],
    "python_topics": ["for", "range()", "biến product"],
    "math_topics": ["Giai thừa"],
    "problem": "Nhập số nguyên không âm n, tính n!.",
    "input": "Một số nguyên không âm n.",
    "output": "Một số nguyên là n!.",
    "sample_input": "5",
    "sample_output": "120",
    "sample_explanation": "5! = 1 * 2 * 3 * 4 * 5 = 120."
  },
  {
    "id": "013",
    "slug": "count-digits",
    "title": "Đếm số chữ số",
    "module": "Loop",
    "difficulty": "Easy-Medium",
    "exercise_type": "Vòng lặp while",
    "prerequisites": ["Số nguyên", "Phép chia nguyên", "while"],
    "python_topics": ["while", "abs()", "toán tử //"],
    "math_topics": ["Biểu diễn thập phân của số nguyên"],
    "problem": "Nhập một số nguyên n, đếm số chữ số trong biểu diễn thập phân của n.",
    "input": "Một số nguyên n.",
    "output": "Một số nguyên là số chữ số của n.",
    "sample_input": "-2030",
    "sample_output": "4",
    "sample_explanation": "Bỏ dấu âm, số 2030 có 4 chữ số."
  },
  {
    "id": "014",
    "slug": "prime-number",
    "title": "Kiểm tra số nguyên tố",
    "module": "Loop",
    "difficulty": "Medium",
    "exercise_type": "Kiểm tra ước số",
    "prerequisites": ["Số nguyên", "Ước số", "Vòng lặp", "if"],
    "python_topics": ["for", "range()", "math.isqrt()", "break"],
    "math_topics": ["Số nguyên tố", "Ước số không tầm thường"],
    "problem": "Nhập số nguyên n, kiểm tra n có phải là số nguyên tố hay không.",
    "input": "Một số nguyên n.",
    "output": "In YES nếu n là số nguyên tố, ngược lại in NO.",
    "sample_input": "29",
    "sample_output": "YES",
    "sample_explanation": "29 chỉ có hai ước dương là 1 và 29."
  },
  {
    "id": "015",
    "slug": "gcd-euclid",
    "title": "Ước chung lớn nhất bằng thuật toán Euclid",
    "module": "Loop",
    "difficulty": "Medium",
    "exercise_type": "Thuật toán số học cổ điển",
    "prerequisites": ["Số nguyên", "Phép chia lấy dư", "while"],
    "python_topics": ["while", "toán tử %", "tuple assignment"],
    "math_topics": ["Ước chung lớn nhất", "Thuật toán Euclid"],
    "problem": "Nhập hai số nguyên a và b, tính ước chung lớn nhất của hai số.",
    "input": "Một dòng gồm hai số nguyên a và b.",
    "output": "Một số nguyên không âm là ước chung lớn nhất của a và b.",
    "sample_input": "48 18",
    "sample_output": "6",
    "sample_explanation": "Ước chung lớn nhất của 48 và 18 là 6."
  }
]
```
