# Chương trình hàm kiểm tra số Armstrong
#
# Yêu cầu:
# - Viết hàm kiểm tra một số có phải số Armstrong không.
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
# - Đếm số chữ số.
# - Lấy từng chữ số lũy thừa theo số chữ số.
# - Cộng lại và so sánh với số ban đầu.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def la_armstrong(n):
    if n < 0:
        return False
    chuoi = str(n)
    so_mu = len(chuoi)
    tong = sum(int(chu_so) ** so_mu for chu_so in chuoi)
    return tong == n


n = int(input("Nhập n: "))
print("Là số Armstrong:", la_armstrong(n))
