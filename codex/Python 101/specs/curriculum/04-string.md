# Module 04: String

## Mục tiêu học tập

- Hiểu chuỗi là một dãy ký tự có thể duyệt từng phần tử.
- Biết dùng các phương thức chuỗi phổ biến để làm sạch và biến đổi dữ liệu.
- Viết được thuật toán xử lý văn bản đơn giản.
- Phân biệt chữ hoa, chữ thường, khoảng trắng và ký tự đặc biệt.

## Kiến thức Python cần học

- Duyệt chuỗi bằng `for`.
- `lower()`, `upper()`, `strip()`, `split()`, `join()`.
- Kiểm tra ký tự bằng `isalpha()`, `isdigit()`, `isalnum()`.
- Cắt chuỗi và đảo chuỗi.
- Xây dựng chuỗi kết quả.

## Các dạng bài

- Đếm ký tự theo điều kiện.
- Kiểm tra palindrome.
- Chuẩn hóa họ tên.
- Đếm số từ.
- Mã hóa ký tự đơn giản.

## Độ khó

Easy-Medium đến Medium.

## Kiến thức tiên quyết

- Biết vòng lặp và điều kiện.
- Biết danh sách ở mức cơ bản là lợi thế nhưng chưa bắt buộc.
- Biết khái niệm ký tự và chuỗi.

## Danh sách bài tập

```json
[
  {
    "id": "016",
    "slug": "count-vowels",
    "title": "Đếm nguyên âm trong chuỗi",
    "module": "String",
    "difficulty": "Easy",
    "exercise_type": "Đếm ký tự",
    "prerequisites": ["Chuỗi", "Vòng lặp for", "if"],
    "python_topics": ["for", "lower()", "in"],
    "math_topics": ["Đếm phần tử thỏa điều kiện"],
    "problem": "Nhập một chuỗi, đếm số ký tự nguyên âm tiếng Anh a, e, i, o, u trong chuỗi, không phân biệt hoa thường.",
    "input": "Một dòng văn bản.",
    "output": "Một số nguyên là số nguyên âm.",
    "sample_input": "Python is fun",
    "sample_output": "3",
    "sample_explanation": "Các nguyên âm là o, i, u nên có 3 ký tự."
  },
  {
    "id": "017",
    "slug": "palindrome-string",
    "title": "Kiểm tra chuỗi palindrome",
    "module": "String",
    "difficulty": "Easy-Medium",
    "exercise_type": "So sánh chuỗi",
    "prerequisites": ["Chuỗi", "Cắt chuỗi", "So sánh"],
    "python_topics": ["lower()", "isalnum()", "join()", "slicing"],
    "math_topics": ["Tính đối xứng"],
    "problem": "Nhập một chuỗi, bỏ qua khoảng trắng, dấu câu và hoa thường, kiểm tra chuỗi có phải palindrome hay không.",
    "input": "Một dòng văn bản.",
    "output": "In YES nếu là palindrome, ngược lại in NO.",
    "sample_input": "A man, a plan, a canal: Panama",
    "sample_output": "YES",
    "sample_explanation": "Sau khi chuẩn hóa còn amanaplanacanalpanama, chuỗi này đọc xuôi và ngược giống nhau."
  },
  {
    "id": "018",
    "slug": "normalize-full-name",
    "title": "Chuẩn hóa họ tên",
    "module": "String",
    "difficulty": "Easy-Medium",
    "exercise_type": "Làm sạch dữ liệu văn bản",
    "prerequisites": ["Chuỗi", "split()", "join()"],
    "python_topics": ["strip()", "split()", "capitalize()", "join()"],
    "math_topics": ["Chuẩn hóa dữ liệu theo quy tắc"],
    "problem": "Nhập một họ tên có thể thừa khoảng trắng và sai hoa thường, chuẩn hóa để mỗi từ viết hoa chữ cái đầu và các chữ còn lại viết thường.",
    "input": "Một dòng chứa họ tên.",
    "output": "Họ tên đã chuẩn hóa.",
    "sample_input": "   nGUYEN   vAN   aN  ",
    "sample_output": "Nguyen Van An",
    "sample_explanation": "Các khoảng trắng thừa được bỏ, mỗi từ được chuyển về dạng chữ cái đầu viết hoa."
  },
  {
    "id": "019",
    "slug": "word-count",
    "title": "Đếm số từ trong câu",
    "module": "String",
    "difficulty": "Easy",
    "exercise_type": "Tách chuỗi",
    "prerequisites": ["Chuỗi", "split()"],
    "python_topics": ["strip()", "split()", "len()"],
    "math_topics": ["Đếm phần tử sau khi tách"],
    "problem": "Nhập một câu, đếm số từ trong câu. Các từ được phân tách bởi một hoặc nhiều khoảng trắng.",
    "input": "Một dòng văn bản.",
    "output": "Một số nguyên là số từ.",
    "sample_input": "Python   makes   practice clear",
    "sample_output": "4",
    "sample_explanation": "Câu có bốn từ: Python, makes, practice, clear."
  },
  {
    "id": "020",
    "slug": "caesar-cipher",
    "title": "Mã hóa Caesar",
    "module": "String",
    "difficulty": "Medium",
    "exercise_type": "Biến đổi ký tự",
    "prerequisites": ["Chuỗi", "Vòng lặp", "Mã ASCII", "Phép chia lấy dư"],
    "python_topics": ["ord()", "chr()", "isalpha()", "modulo"],
    "math_topics": ["Dịch vòng trong bảng chữ cái"],
    "problem": "Nhập một chuỗi và số nguyên shift, mã hóa chuỗi bằng Caesar cipher. Chữ cái được dịch vòng trong bảng chữ cái, giữ nguyên hoa thường; ký tự không phải chữ cái giữ nguyên.",
    "input": "Dòng thứ nhất là chuỗi cần mã hóa. Dòng thứ hai là số nguyên shift.",
    "output": "Chuỗi sau khi mã hóa.",
    "sample_input": "Abc Zz!\n2",
    "sample_output": "Cde Bb!",
    "sample_explanation": "A dịch thành C, b thành d, c thành e, Z dịch vòng thành B, z dịch vòng thành b."
  }
]
```
