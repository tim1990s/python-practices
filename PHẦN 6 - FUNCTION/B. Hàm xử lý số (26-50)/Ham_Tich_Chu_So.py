# Chương trình hàm tính tích chữ số
#
# Yêu cầu:
# - Viết hàm tính tích các chữ số của một số nguyên.
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
# - Lấy trị tuyệt đối của số.
# - Tách từng chữ số bằng chia lấy dư.
# - Nhân các chữ số lại với nhau.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def tich_chu_so(n):
    n = abs(n)
    if n == 0:
        return 0
    tich = 1
    while n > 0:
        tich *= n % 10
        n //= 10
    return tich


n = int(input("Nhập n: "))
print("Tích chữ số:", tich_chu_so(n))
