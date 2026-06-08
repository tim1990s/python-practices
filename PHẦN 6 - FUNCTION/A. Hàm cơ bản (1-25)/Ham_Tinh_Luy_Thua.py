# Chương trình hàm tính lũy thừa
#
# Yêu cầu:
# - Viết hàm tính a mũ b.
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
# - Định nghĩa hàm nhận cơ số và số mũ.
# - Dùng toán tử ** để tính lũy thừa.
# - Trả về kết quả.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def luy_thua(a, b):
    return a ** b


a = float(input("Nhập cơ số a: "))
b = float(input("Nhập số mũ b: "))
print("Kết quả:", luy_thua(a, b))
