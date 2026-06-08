# Chương trình hàm đếm chữ số
#
# Yêu cầu:
# - Viết hàm đếm số chữ số của một số nguyên.
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
# - Số 0 có 1 chữ số.
# - Chia nguyên cho 10 đến khi hết số.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def dem_chu_so(n):
    n = abs(n)
    if n == 0:
        return 1
    dem = 0
    while n > 0:
        dem += 1
        n //= 10
    return dem


n = int(input("Nhập n: "))
print("Số chữ số:", dem_chu_so(n))
