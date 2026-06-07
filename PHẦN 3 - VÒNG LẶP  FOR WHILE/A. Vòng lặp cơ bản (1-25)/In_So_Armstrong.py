# Chương trình in các số Armstrong từ 1 đến N

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

if n < 1:
    print("N phải lớn hơn hoặc bằng 1")
else:
    for so in range(1, n + 1):
        chuoi = str(so)
        so_chu_so = len(chuoi)
        tong = 0

        for chu_so in chuoi:
            tong += int(chu_so) ** so_chu_so

        if tong == so:
            print(so)
