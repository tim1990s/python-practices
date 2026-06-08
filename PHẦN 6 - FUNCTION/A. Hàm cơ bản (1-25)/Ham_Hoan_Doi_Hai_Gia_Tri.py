# Chương trình hàm hoán đổi hai giá trị
#
# Yêu cầu:
# - Viết hàm hoán đổi hai giá trị.
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
# - Định nghĩa hàm nhận hai giá trị.
# - Trả về hai giá trị theo thứ tự ngược lại.
# - Gọi hàm và in kết quả.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def hoan_doi(a, b):
    return b, a


a = input("Nhập a: ")
b = input("Nhập b: ")
a, b = hoan_doi(a, b)
print("Sau khi hoán đổi:")
print("a =", a)
print("b =", b)
