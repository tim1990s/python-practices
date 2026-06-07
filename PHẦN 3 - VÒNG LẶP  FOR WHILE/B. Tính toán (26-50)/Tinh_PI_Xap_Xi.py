# Chương trình tính PI xấp xỉ bằng chuỗi Leibniz

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng số hạng: "))

if n <= 0:
    print("Số lượng số hạng phải lớn hơn 0")
else:
    tong = 0

    for i in range(n):
        tong += ((-1) ** i) / (2 * i + 1)

    pi = 4 * tong
    print("PI xấp xỉ là:", pi)
