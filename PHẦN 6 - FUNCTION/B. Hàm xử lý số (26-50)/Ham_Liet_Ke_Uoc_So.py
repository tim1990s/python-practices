# Chương trình hàm liệt kê ước số
#
# Yêu cầu:
# - Viết hàm liệt kê tất cả ước số dương của một số nguyên.
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
# - Duyệt từ 1 đến căn bậc hai của n.
# - Nếu chia hết thì thêm cả cặp ước.
# - Sắp xếp danh sách ước trước khi trả về.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math


def liet_ke_uoc_so(n):
    n = abs(n)
    if n == 0:
        return []
    uoc_so = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            uoc_so.append(i)
            if i != n // i:
                uoc_so.append(n // i)
    return sorted(uoc_so)


n = int(input("Nhập n: "))
print("Các ước số:", liet_ke_uoc_so(n))
