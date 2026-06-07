# Chương trình tính median của dãy số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng phần tử: "))

if n <= 0:
    print("Số lượng phần tử phải lớn hơn 0")
else:
    ds = []

    for i in range(1, n + 1):
        so = float(input("Nhập số thứ " + str(i) + ": "))
        ds.append(so)

    ds.sort()
    giua = n // 2

    if n % 2 == 1:
        median = ds[giua]
    else:
        median = (ds[giua - 1] + ds[giua]) / 2

    print("Median là:", median)
