# Chương trình hàm trừ
#
# Yêu cầu:
# - Viết hàm trừ hai số.
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
# - Định nghĩa hàm nhận hai tham số.
# - Trả về hiệu a - b.
# - In kết quả sau khi gọi hàm.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def tru(a, b):
    return a - b


a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print("Hiệu:", tru(a, b))
