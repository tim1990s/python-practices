# Chương trình hàm tìm chữ số lớn nhất
#
# Yêu cầu:
# - Viết hàm tìm chữ số lớn nhất trong một số nguyên.
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
# - Tách từng chữ số.
# - Cập nhật chữ số lớn nhất.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def chu_so_lon_nhat(n):
    n = abs(n)
    lon_nhat = 0
    while n > 0:
        lon_nhat = max(lon_nhat, n % 10)
        n //= 10
    return lon_nhat


n = int(input("Nhập n: "))
print("Chữ số lớn nhất:", chu_so_lon_nhat(n))
