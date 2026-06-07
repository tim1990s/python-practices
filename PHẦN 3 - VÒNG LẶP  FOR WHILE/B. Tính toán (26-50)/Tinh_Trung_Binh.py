# Chương trình tính trung bình cộng của dãy số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng phần tử: "))

if n <= 0:
    print("Số lượng phần tử phải lớn hơn 0")
else:
    tong = 0

    for i in range(1, n + 1):
        so = float(input("Nhập số thứ " + str(i) + ": "))
        tong += so

    print("Trung bình cộng là:", tong / n)
