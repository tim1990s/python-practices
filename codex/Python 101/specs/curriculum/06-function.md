# Module 06: Function

## Mục tiêu học tập

- Biết chia chương trình thành các hàm nhỏ, mỗi hàm có một nhiệm vụ rõ ràng.
- Hiểu tham số, giá trị trả về và phạm vi biến ở mức cơ bản.
- Viết hàm để tái sử dụng logic và kiểm thử dễ hơn.
- Kết hợp hàm với điều kiện, vòng lặp, chuỗi và list.

## Kiến thức Python cần học

- `def`, tham số, `return`.
- Type hints cho hàm đơn giản.
- Hàm thuần không phụ thuộc input/output trực tiếp.
- Tách `main()` để đọc dữ liệu và gọi hàm xử lý.
- Tư duy thiết kế hàm theo đặc tả.

## Các dạng bài

- Hàm chuyển đổi đơn vị.
- Hàm tính dãy số.
- Hàm kiểm tra điều kiện.
- Hàm tìm kiếm.
- Hàm giải bài toán toán học trung cấp.

## Độ khó

Easy-Medium đến Medium.

## Kiến thức tiên quyết

- Nắm biến, điều kiện, vòng lặp, chuỗi và list.
- Biết đọc input nhiều dòng.
- Biết công thức toán học cơ bản.

## Danh sách bài tập

```json
[
  {
    "id": "026",
    "slug": "temperature-converter",
    "title": "Hàm chuyển đổi nhiệt độ",
    "module": "Function",
    "difficulty": "Easy-Medium",
    "exercise_type": "Thiết kế hàm chuyển đổi",
    "prerequisites": ["Hàm", "Số thực", "Công thức tuyến tính"],
    "python_topics": ["def", "return", "float()", "f-string"],
    "math_topics": ["Chuyển đổi Celsius và Fahrenheit"],
    "problem": "Nhập nhiệt độ Celsius, viết hàm chuyển sang Fahrenheit và in kết quả với 2 chữ số thập phân.",
    "input": "Một số thực celsius.",
    "output": "Một số thực là nhiệt độ Fahrenheit, làm tròn 2 chữ số thập phân.",
    "sample_input": "25",
    "sample_output": "77.00",
    "sample_explanation": "F = C * 9 / 5 + 32, nên 25 độ C bằng 77 độ F."
  },
  {
    "id": "027",
    "slug": "fibonacci-function",
    "title": "Hàm tính số Fibonacci",
    "module": "Function",
    "difficulty": "Medium",
    "exercise_type": "Hàm và vòng lặp",
    "prerequisites": ["Hàm", "Vòng lặp", "Biến trạng thái"],
    "python_topics": ["def", "return", "for", "tuple assignment"],
    "math_topics": ["Dãy Fibonacci"],
    "problem": "Nhập số nguyên không âm n, viết hàm trả về số Fibonacci thứ n với F0 = 0 và F1 = 1.",
    "input": "Một số nguyên không âm n.",
    "output": "Một số nguyên là F_n.",
    "sample_input": "10",
    "sample_output": "55",
    "sample_explanation": "Dãy bắt đầu 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 nên F10 = 55."
  },
  {
    "id": "028",
    "slug": "valid-password",
    "title": "Hàm kiểm tra mật khẩu hợp lệ",
    "module": "Function",
    "difficulty": "Medium",
    "exercise_type": "Hàm kiểm tra điều kiện chuỗi",
    "prerequisites": ["Hàm", "Chuỗi", "Điều kiện", "any()"],
    "python_topics": ["def", "any()", "islower()", "isupper()", "isdigit()"],
    "math_topics": ["Logic nhiều điều kiện"],
    "problem": "Nhập một mật khẩu, viết hàm kiểm tra mật khẩu hợp lệ nếu có ít nhất 8 ký tự, có chữ thường, chữ hoa, chữ số và ký tự đặc biệt.",
    "input": "Một dòng chứa mật khẩu.",
    "output": "In VALID nếu mật khẩu hợp lệ, ngược lại in INVALID.",
    "sample_input": "Python@123",
    "sample_output": "VALID",
    "sample_explanation": "Mật khẩu đủ dài và có chữ hoa, chữ thường, chữ số, ký tự đặc biệt."
  },
  {
    "id": "029",
    "slug": "linear-search-function",
    "title": "Hàm tìm kiếm tuyến tính",
    "module": "Function",
    "difficulty": "Easy-Medium",
    "exercise_type": "Hàm xử lý list",
    "prerequisites": ["Hàm", "List", "Vòng lặp"],
    "python_topics": ["def", "list[int]", "enumerate()", "return"],
    "math_topics": ["Tìm kiếm trong dãy hữu hạn"],
    "problem": "Nhập n, list gồm n số nguyên và giá trị target, viết hàm tìm vị trí xuất hiện đầu tiên của target. Nếu không có thì trả về -1.",
    "input": "Dòng thứ nhất là n. Dòng thứ hai gồm n số nguyên. Dòng thứ ba là target.",
    "output": "Một số nguyên là chỉ số đầu tiên theo 0-based index, hoặc -1 nếu không tìm thấy.",
    "sample_input": "5\n4 8 15 16 23\n15",
    "sample_output": "2",
    "sample_explanation": "Giá trị 15 xuất hiện đầu tiên tại chỉ số 2."
  },
  {
    "id": "030",
    "slug": "quadratic-equation",
    "title": "Hàm giải phương trình bậc hai",
    "module": "Function",
    "difficulty": "Medium",
    "exercise_type": "Hàm giải toán theo trường hợp",
    "prerequisites": ["Hàm", "Điều kiện", "Căn bậc hai", "Số thực"],
    "python_topics": ["def", "tuple", "math.sqrt()", "if elif else"],
    "math_topics": ["Phương trình bậc hai", "Biệt thức delta"],
    "problem": "Nhập ba hệ số a, b, c của phương trình ax^2 + bx + c = 0, viết hàm phân loại và tính nghiệm thực nếu có.",
    "input": "Một dòng gồm ba số thực a, b và c.",
    "output": "Nếu vô số nghiệm in Infinite solutions. Nếu vô nghiệm in No solution hoặc No real roots tùy trường hợp. Nếu có một nghiệm in One root: x = value. Nếu có hai nghiệm in Two roots: x1 = value, x2 = value. Các nghiệm làm tròn 2 chữ số thập phân.",
    "sample_input": "1 -3 2",
    "sample_output": "Two roots: x1 = 1.00, x2 = 2.00",
    "sample_explanation": "Delta = 1, hai nghiệm thực là 1 và 2."
  }
]
```
