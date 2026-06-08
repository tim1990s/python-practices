# Chương trình hàm giải phương trình bậc hai
#
# Yêu cầu:
# - Viết hàm giải phương trình ax^2 + bx + c = 0.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện cách khai báo hàm, truyền tham số, trả về kết quả bằng return và tách chương trình thành các khối xử lý nhỏ.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc hệ số a, b, c.
# - Tách logic giải phương trình vào hàm.
# - Xử lý phương trình bậc nhất, vô nghiệm, nghiệm kép và hai nghiệm.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math


def giai_pt_bac_hai(a, b, c):
    if a == 0:
        if b == 0:
            return "Vô số nghiệm" if c == 0 else "Vô nghiệm"
        return "Nghiệm: x = " + str(-c / b)

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "Vô nghiệm"
    if delta == 0:
        return "Nghiệm kép: x = " + str(-b / (2 * a))
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return "Hai nghiệm: x1 = " + str(x1) + ", x2 = " + str(x2)


a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
print(giai_pt_bac_hai(a, b, c))
