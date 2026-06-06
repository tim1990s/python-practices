# Module 05: List

## Mục tiêu học tập

- Hiểu list là cấu trúc dữ liệu lưu nhiều giá trị theo thứ tự.
- Biết đọc một dãy số từ input và xử lý bằng vòng lặp.
- Biết dùng list để lưu, duyệt, lọc và thống kê dữ liệu.
- Viết được các thuật toán cơ bản trên dãy số.

## Kiến thức Python cần học

- Tạo list và truy cập phần tử.
- Duyệt list bằng `for`.
- `append()`, `in`, `len()`, `set()` ở mức cơ bản.
- Dictionary để đếm tần suất.
- Sắp xếp và loại trùng khi cần.

## Các dạng bài

- Tính tổng phần tử.
- Tìm giá trị lớn nhất, nhỏ nhất.
- Đếm tần suất.
- Loại bỏ phần tử trùng.
- Tìm giá trị lớn thứ hai.

## Độ khó

Easy đến Medium.

## Kiến thức tiên quyết

- Vòng lặp và điều kiện.
- Biến tích lũy.
- Kiểu số nguyên và cách tách input.

## Danh sách bài tập

```json
[
  {
    "id": "021",
    "slug": "sum-list",
    "title": "Tính tổng các phần tử trong list",
    "module": "List",
    "difficulty": "Easy",
    "exercise_type": "Duyệt list và tích lũy",
    "prerequisites": ["List", "Vòng lặp for", "Biến tổng"],
    "python_topics": ["list", "map()", "sum()"],
    "math_topics": ["Tổng của dãy số"],
    "problem": "Nhập n và n số nguyên, tính tổng các phần tử trong list.",
    "input": "Dòng thứ nhất là số nguyên n. Dòng thứ hai gồm n số nguyên.",
    "output": "Một số nguyên là tổng các phần tử.",
    "sample_input": "5\n1 2 3 4 5",
    "sample_output": "15",
    "sample_explanation": "Tổng của 1, 2, 3, 4, 5 là 15."
  },
  {
    "id": "022",
    "slug": "max-min-list",
    "title": "Tìm giá trị nhỏ nhất và lớn nhất trong list",
    "module": "List",
    "difficulty": "Easy",
    "exercise_type": "Duyệt list và so sánh",
    "prerequisites": ["List", "So sánh", "for"],
    "python_topics": ["list", "min()", "max()"],
    "math_topics": ["Giá trị cực trị trong dãy"],
    "problem": "Nhập n và n số nguyên, in ra giá trị nhỏ nhất và lớn nhất.",
    "input": "Dòng thứ nhất là số nguyên dương n. Dòng thứ hai gồm n số nguyên.",
    "output": "Hai số nguyên: nhỏ nhất và lớn nhất.",
    "sample_input": "6\n4 -1 9 9 2 0",
    "sample_output": "-1 9",
    "sample_explanation": "Số nhỏ nhất là -1 và số lớn nhất là 9."
  },
  {
    "id": "023",
    "slug": "count-frequency",
    "title": "Đếm tần suất xuất hiện",
    "module": "List",
    "difficulty": "Medium",
    "exercise_type": "Thống kê bằng dictionary",
    "prerequisites": ["List", "Dictionary", "Vòng lặp"],
    "python_topics": ["dict", "get()", "sorted()"],
    "math_topics": ["Tần suất xuất hiện"],
    "problem": "Nhập n và n số nguyên, đếm số lần xuất hiện của từng giá trị. In các giá trị theo thứ tự tăng dần, mỗi dòng gồm giá trị và số lần xuất hiện.",
    "input": "Dòng thứ nhất là số nguyên n. Dòng thứ hai gồm n số nguyên.",
    "output": "Nhiều dòng, mỗi dòng gồm value count theo thứ tự value tăng dần.",
    "sample_input": "7\n2 3 2 1 3 2 1",
    "sample_output": "1 2\n2 3\n3 2",
    "sample_explanation": "Số 1 xuất hiện 2 lần, số 2 xuất hiện 3 lần, số 3 xuất hiện 2 lần."
  },
  {
    "id": "024",
    "slug": "remove-duplicates",
    "title": "Loại bỏ phần tử trùng lặp",
    "module": "List",
    "difficulty": "Medium",
    "exercise_type": "Lọc dữ liệu giữ thứ tự",
    "prerequisites": ["List", "Set", "Vòng lặp"],
    "python_topics": ["set", "append()", "in"],
    "math_topics": ["Tập hợp và thứ tự xuất hiện"],
    "problem": "Nhập n và n số nguyên, loại bỏ các phần tử trùng lặp nhưng giữ lại thứ tự xuất hiện đầu tiên.",
    "input": "Dòng thứ nhất là số nguyên n. Dòng thứ hai gồm n số nguyên.",
    "output": "Một dòng gồm các phần tử sau khi loại trùng, cách nhau bởi dấu cách.",
    "sample_input": "8\n5 1 5 2 1 3 2 4",
    "sample_output": "5 1 2 3 4",
    "sample_explanation": "Mỗi giá trị chỉ được giữ ở lần xuất hiện đầu tiên."
  },
  {
    "id": "025",
    "slug": "second-largest",
    "title": "Tìm số lớn thứ hai",
    "module": "List",
    "difficulty": "Medium",
    "exercise_type": "Tìm cực trị có điều kiện",
    "prerequisites": ["List", "Set", "Sắp xếp", "Điều kiện"],
    "python_topics": ["set()", "sorted()", "reverse=True"],
    "math_topics": ["Thứ hạng trong dãy số"],
    "problem": "Nhập n và n số nguyên, tìm giá trị lớn thứ hai khác với giá trị lớn nhất.",
    "input": "Dòng thứ nhất là số nguyên n. Dòng thứ hai gồm n số nguyên.",
    "output": "In số lớn thứ hai nếu tồn tại, ngược lại in NO SECOND LARGEST.",
    "sample_input": "6\n10 5 10 8 7 8",
    "sample_output": "8",
    "sample_explanation": "Các giá trị khác nhau là 10, 8, 7, 5; số lớn thứ hai là 8."
  }
]
```
