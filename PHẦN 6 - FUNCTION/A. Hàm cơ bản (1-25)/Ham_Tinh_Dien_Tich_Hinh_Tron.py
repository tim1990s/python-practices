# Chương trình hàm tính diện tích hình tròn
#
# Yêu cầu:
# - Viết hàm tính diện tích hình tròn từ bán kính.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện cách khai báo hàm, truyền tham số, trả về kết quả bằng return và tách chương trình thành các khối xử lý nhỏ.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Định nghĩa hàm nhận bán kính.
# - Kiểm tra bán kính không âm.
# - Áp dụng công thức pi * r^2.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math


def dien_tich_hinh_tron(r):
    if r < 0:
        return None
    return math.pi * r ** 2


r = float(input("Nhập bán kính: "))
ket_qua = dien_tich_hinh_tron(r)
print("Bán kính không hợp lệ" if ket_qua is None else "Diện tích:", ket_qua)
