# Chương trình hàm chia
#
# Yêu cầu:
# - Viết hàm chia hai số và xử lý trường hợp chia cho 0.
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
# - Định nghĩa hàm nhận số bị chia và số chia.
# - Nếu số chia bằng 0 thì trả về thông báo lỗi.
# - Ngược lại trả về thương.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    return a / b


a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print("Thương:", chia(a, b))
