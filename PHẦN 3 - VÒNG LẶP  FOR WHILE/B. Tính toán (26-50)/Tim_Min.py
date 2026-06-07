# Chương trình tìm min trong dãy số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng phần tử: "))

if n <= 0:
    print("Số lượng phần tử phải lớn hơn 0")
else:
    min_so = float(input("Nhập số thứ 1: "))

    for i in range(2, n + 1):
        so = float(input("Nhập số thứ " + str(i) + ": "))

        if so < min_so:
            min_so = so

    print("Giá trị nhỏ nhất là:", min_so)
