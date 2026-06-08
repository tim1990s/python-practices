# Chương trình hàm tìm ước chung của hai số
#
# Yêu cầu:
# - Viết hàm liệt kê các ước chung của hai số nguyên.
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
# - Tìm giá trị nhỏ hơn giữa hai số.
# - Duyệt từ 1 đến giá trị đó.
# - Thêm i vào kết quả nếu cả hai số cùng chia hết cho i.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def uoc_chung(a, b):
    a, b = abs(a), abs(b)
    gioi_han = min(a, b)
    return [i for i in range(1, gioi_han + 1) if a % i == 0 and b % i == 0]


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Ước chung:", uoc_chung(a, b))
