# Chương trình hàm UCLN
#
# Yêu cầu:
# - Viết hàm tìm ước chung lớn nhất của hai số.
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
# - Dùng thuật toán Euclid.
# - Lặp đến khi số dư bằng 0.
# - Trả về giá trị tuyệt đối của UCLN.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def ucln(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN:", ucln(a, b))
