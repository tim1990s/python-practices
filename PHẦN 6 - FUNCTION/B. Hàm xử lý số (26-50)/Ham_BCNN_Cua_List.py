# Chương trình hàm tính BCNN của list
#
# Yêu cầu:
# - Viết hàm tính bội chung nhỏ nhất của một list số nguyên.
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
# - Viết hàm UCLN.
# - Viết hàm BCNN của hai số.
# - Duyệt list và gộp dần kết quả.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def ucln(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def bcnn_hai_so(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // ucln(a, b)


def bcnn_list(danh_sach):
    if not danh_sach:
        return None
    ket_qua = abs(danh_sach[0])
    for so in danh_sach[1:]:
        ket_qua = bcnn_hai_so(ket_qua, so)
    return ket_qua


du_lieu = input("Nhập các số nguyên, cách nhau bởi dấu phẩy: ")
danh_sach = [int(x.strip()) for x in du_lieu.split(",") if x.strip()]
print("BCNN của list:", bcnn_list(danh_sach))
