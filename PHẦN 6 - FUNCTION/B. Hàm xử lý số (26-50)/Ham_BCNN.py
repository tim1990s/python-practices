# Chương trình hàm BCNN
#
# Yêu cầu:
# - Viết hàm tìm bội chung nhỏ nhất của hai số.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện viết hàm xử lý số nguyên, số thực, chữ số, ước số, bội số, dãy Fibonacci và các bài toán số học cơ bản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Tính UCLN bằng thuật toán Euclid.
# - Áp dụng công thức BCNN = |a*b| / UCLN.
# - Xử lý trường hợp một trong hai số bằng 0.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def ucln(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def bcnn(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // ucln(a, b)


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("BCNN:", bcnn(a, b))
