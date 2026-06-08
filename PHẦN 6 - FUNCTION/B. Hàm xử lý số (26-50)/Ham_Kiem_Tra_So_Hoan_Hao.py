# Chương trình hàm kiểm tra số hoàn hảo
#
# Yêu cầu:
# - Viết hàm kiểm tra một số có phải số hoàn hảo không.
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
# - Số hoàn hảo bằng tổng các ước dương nhỏ hơn chính nó.
# - Tính tổng ước thực sự.
# - So sánh tổng với số ban đầu.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def la_so_hoan_hao(n):
    if n <= 1:
        return False
    tong = 1
    for i in range(2, n):
        if n % i == 0:
            tong += i
    return tong == n


n = int(input("Nhập n: "))
print("Là số hoàn hảo:", la_so_hoan_hao(n))
