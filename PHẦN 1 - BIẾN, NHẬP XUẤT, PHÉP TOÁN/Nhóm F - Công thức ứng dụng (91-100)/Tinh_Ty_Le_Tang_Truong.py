# Chương trình tính tỷ lệ tăng trưởng
#
# Tỷ lệ tăng trưởng cho biết giá trị sau tăng hoặc giảm bao nhiêu phần trăm
# so với giá trị ban đầu.
#
# Công thức:
# ty_le_tang_truong = (gia_tri_sau - gia_tri_truoc) / gia_tri_truoc * 100
#
# Ý tưởng:
# - Nhập giá trị ban đầu.
# - Nhập giá trị sau.
# - Kiểm tra giá trị ban đầu phải khác 0.
# - Tính tỷ lệ tăng trưởng và in kết quả ra màn hình.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

gia_tri_truoc = float(input("Nhập giá trị ban đầu: "))
gia_tri_sau = float(input("Nhập giá trị sau: "))

if gia_tri_truoc == 0:
    print("Giá trị ban đầu phải khác 0")
else:
    ty_le_tang_truong = (gia_tri_sau - gia_tri_truoc) / gia_tri_truoc * 100
    print("Tỷ lệ tăng trưởng là:", ty_le_tang_truong, "%")
