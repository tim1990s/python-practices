# Chương trình hàm tính tổng ước số
#
# Yêu cầu:
# - Viết hàm tính tổng các ước số dương của một số nguyên.
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
# - Tái sử dụng ý tưởng liệt kê ước số.
# - Cộng các ước tìm được.
# - Trả về tổng.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def tong_uoc_so(n):
    n = abs(n)
    if n == 0:
        return 0
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong


n = int(input("Nhập n: "))
print("Tổng ước số:", tong_uoc_so(n))
