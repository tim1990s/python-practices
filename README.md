# Python Practices

Kho bài luyện tập Python được tổ chức theo từng chủ đề, phục vụ việc học và ôn lại lập trình Python từ nền tảng đến nâng cao.

Mỗi bài tập được viết thành một file `.py` riêng, có phần mô tả bài toán, công thức hoặc ý tưởng giải, ví dụ minh họa và phần code chạy trực tiếp trên terminal.

## Mục Tiêu

- Xây dựng repository chứa các bài luyện tập Python có hệ thống.
- Luyện cú pháp Python cơ bản qua các bài nhỏ, dễ chạy, dễ kiểm tra.
- Tổ chức bài tập theo từng phần: phép toán, điều kiện, vòng lặp, chuỗi, list và function.
- Giữ code rõ ràng, phù hợp cho người mới học.
- Theo dõi tiến độ bài đã làm bằng checklist trong `Other/Plan.txt`.

## Cấu Trúc Dự Án

```text
Python Practices/
|-- PHẦN 1 - BIẾN, NHẬP XUẤT, PHÉP TOÁN/
|   |-- Nhóm A - Phép toán cơ bản (1-20)/
|   |-- Nhóm B - Hình học cơ bản (21-40)/
|   |-- Nhóm C - Chuyển đổi đơn vị (41-60)/
|   |-- Nhóm D - Tài chính (61-80)/
|   |-- Nhóm E - Thời gian và tuổi tác (81-90)/
|   |-- Nhóm F - Công thức ứng dụng (91-100)/
|
|-- PHẦN 2 - ĐIỀU KIỆN IF ELSE/
|-- PHẦN 3 - VÒNG LẶP  FOR WHILE/
|-- Other/
|   |-- Plan.txt
|   |-- Giai_Phuong_Trinh_Bac_Nhat.py
|   |-- Giai_Phuong_Trinh_Bac_hai.py
|   |-- Kiem_Tra_So_Chinh_Phuong.py
|
|-- codex/
|-- .gitignore
|-- README.md
```

## Tiến Độ Hiện Tại

| Phần | Nhóm | Trạng thái |
| --- | --- | --- |
| Phần 1 | Nhóm A - Phép toán cơ bản | Hoàn thành |
| Phần 1 | Nhóm B - Hình học cơ bản | Hoàn thành |
| Phần 1 | Nhóm C - Chuyển đổi đơn vị | Hoàn thành |
| Phần 1 | Nhóm D - Tài chính | Hoàn thành |
| Phần 1 | Nhóm E - Thời gian và tuổi tác | Hoàn thành |
| Phần 1 | Nhóm F - Công thức ứng dụng | Chưa hoàn thành |

Chi tiết đầy đủ nằm trong [Plan.txt](Other/Plan.txt).

## Cách Chạy Bài Tập

Mở terminal tại thư mục gốc của dự án:

```bash
cd "C:\Users\mrphu\OneDrive\Desktop\Python Practices"
```

Chạy một file Python bất kỳ:

```bash
python "PHẦN 1 - BIẾN, NHẬP XUẤT, PHÉP TOÁN/Nhóm A - Phép toán cơ bản (1-20)/Tinh_Thuong.py"
```

Ví dụ khác:

```bash
python "PHẦN 1 - BIẾN, NHẬP XUẤT, PHÉP TOÁN/Nhóm E - Thời gian và tuổi tác (81-90)/Tinh_Tuoi_Tu_Nam_Sinh.py"
```

## Chuẩn Viết Mỗi Bài

Mỗi file bài tập nên giữ cấu trúc sau:

```python
# Tên chương trình
#
# Mô tả bài toán.
#
# Công thức hoặc ví dụ:
# ...
#
# Ý tưởng:
# - Bước 1.
# - Bước 2.
# - Bước 3.

# Code Python
```

Quy ước đặt tên file:

- Dùng tiếng Việt không dấu.
- Dùng dấu gạch dưới `_` để ngăn cách từ.
- Tên file mô tả đúng nội dung bài.

Ví dụ:

```text
Tinh_Tong.py
Tinh_Thuong.py
Tinh_Tien_Lai_Don.py
Doi_Gio_Sang_Phut.py
```

## Nội Dung Luyện Tập

- Phần 1: Biến, nhập xuất, phép toán.
- Phần 2: Điều kiện `if/else`.
- Phần 3: Vòng lặp `for/while`.
- Phần 4: Chuỗi `string`.
- Phần 5: Danh sách `list`.
- Phần 6: Hàm `function`.

## Ghi Chú

- `Other/Plan.txt` là file theo dõi toàn bộ danh sách bài tập và trạng thái hoàn thành.
- `.gitignore` bỏ qua môi trường ảo, cache Python, cấu hình IDE và thư mục phụ không dùng làm nội dung chính.
- Một số file trong `Other` là bài luyện tập riêng hoặc bài tham khảo ngoài cấu trúc chính.
