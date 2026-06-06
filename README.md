# Python Practices

Repository này dùng để lưu các bài luyện tập Python theo từng chủ đề, từ cơ bản đến nâng cao.

Mục tiêu chính của dự án là xây dựng một bộ bài tập nhỏ, dễ đọc, dễ chạy và có giải thích rõ ràng. Mỗi file Python là một bài riêng, tập trung vào một kiến thức cụ thể để luyện tập từng bước.

## Mục Tiêu Dự Án

- Luyện tập cú pháp Python cơ bản.
- Làm quen với biến, nhập xuất, phép toán, điều kiện, vòng lặp, chuỗi, list và function.
- Viết code đơn giản, rõ ràng, phù hợp cho người mới học.
- Mỗi bài có phần mô tả, ví dụ, ý tưởng và phần code.
- Tổ chức bài tập theo từng phần và từng nhóm kiến thức.

## Cấu Trúc Dự Án

```text
Python Practices/
|-- PHẦN 1 - BIẾN, NHẬP XUẤT, PHÉP TOÁN (100 BÀI)/
|   |-- Nhóm A - Phép toán cơ bản (1-20)/
|   |   |-- Tinh_Tong.py
|   |   |-- Phep_Toan_Hai_So.py
|   |   |-- Tinh_Trung_Binh_Cong_2_So.py
|
|-- Other/
|   |-- Giai_Phuong_Trinh_Bac_Nhat.py
|   |-- Giai_Phuong_Trinh_Bac_hai.py
|   |-- Kiem_Tra_So_Chinh_Phuong.py
|
|-- .gitignore
|-- README.md
```

## Cách Chạy Chương Trình

Mở terminal tại thư mục gốc của dự án:

```bash
cd "C:\Users\mrphu\OneDrive\Desktop\Python Practices"
```

Sau đó chạy file Python cần học.

Ví dụ:

```bash
python "PHẦN 1 - BIẾN, NHẬP XUẤT, PHÉP TOÁN (100 BÀI)/Nhóm A - Phép toán cơ bản (1-20)/Tinh_Trung_Binh_Cong_2_So.py"
```

Hoặc chạy file trong thư mục `Other`:

```bash
python "Other/Kiem_Tra_So_Chinh_Phuong.py"
```

## Quy Ước Viết Bài

Mỗi bài tập nên có cấu trúc như sau:

```python
# Tên chương trình
#
# Mô tả ngắn gọn bài toán.
#
# Ví dụ:
# ...
#
# Ý tưởng:
# - Bước 1.
# - Bước 2.
# - Bước 3.

# Code Python
```

Ví dụ tên file nên viết rõ ràng, không dấu và dùng dấu gạch dưới:

```text
Tinh_Tong.py
Tinh_Hieu.py
Tinh_Tich.py
Tinh_Trung_Binh_Cong_2_So.py
```

## Nội Dung Luyện Tập

Dự án có thể được phát triển theo các phần sau:

- Phần 1: Biến, nhập xuất, phép toán.
- Phần 2: Điều kiện `if/else`.
- Phần 3: Vòng lặp `for/while`.
- Phần 4: Chuỗi `string`.
- Phần 5: Danh sách `list`.
- Phần 6: Hàm `function`.

## Các Bài Đã Có

- Tính tổng.
- Tính kết quả của hai số theo phép toán cộng, trừ, nhân, chia.
- Tính trung bình cộng 2 số.
- Kiểm tra số chính phương.
- Giải phương trình bậc nhất.
- Giải phương trình bậc hai.

## Ghi Chú Git

File `.gitignore` đang bỏ qua các thư mục và file không cần đưa lên repository:

```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
.idea/
Other/Practices/
```

Thư mục `Other/Practices/` là thư mục phụ và không dùng làm nội dung chính của repository.
