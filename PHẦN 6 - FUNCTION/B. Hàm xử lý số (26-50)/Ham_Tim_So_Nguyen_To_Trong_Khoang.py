# Chương trình hàm tìm số nguyên tố trong khoảng
#
# Yêu cầu:
# - Viết hàm liệt kê các số nguyên tố trong đoạn [a, b].
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
# - Viết hàm kiểm tra nguyên tố.
# - Duyệt từ a đến b.
# - Giữ lại các số nguyên tố.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math


def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def nguyen_to_trong_khoang(a, b):
    if a > b:
        a, b = b, a
    return [n for n in range(a, b + 1) if la_nguyen_to(n)]


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Các số nguyên tố:", nguyen_to_trong_khoang(a, b))
