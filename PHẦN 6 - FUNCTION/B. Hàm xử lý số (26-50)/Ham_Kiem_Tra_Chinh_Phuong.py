# Chương trình hàm kiểm tra số chính phương
#
# Yêu cầu:
# - Viết hàm kiểm tra một số có phải số chính phương không.
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
# - Số chính phương là bình phương của một số nguyên.
# - Lấy căn bậc hai nguyên.
# - Kiểm tra bình phương lại có bằng số ban đầu không.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math


def la_chinh_phuong(n):
    if n < 0:
        return False
    can = int(math.sqrt(n))
    return can * can == n


n = int(input("Nhập n: "))
print("Là số chính phương:", la_chinh_phuong(n))
