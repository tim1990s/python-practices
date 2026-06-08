# Chương trình hàm kiểm tra số nguyên tố
#
# Yêu cầu:
# - Viết hàm kiểm tra một số có phải số nguyên tố không.
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
# - Số nguyên tố là số nguyên lớn hơn 1.
# - Kiểm tra các ước từ 2 đến căn bậc hai của n.
# - Trả về True nếu không tìm thấy ước.

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


n = int(input("Nhập n: "))
print("Là số nguyên tố:", la_nguyen_to(n))
