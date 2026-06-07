# Chương trình kiểm tra số Armstrong

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên cần kiểm tra: "))

if n < 0:
    print(n, "không phải là số Armstrong")
else:
    chuoi = str(n)
    so_chu_so = len(chuoi)
    tong = 0

    for chu_so in chuoi:
        tong += int(chu_so) ** so_chu_so

    if tong == n:
        print(n, "là số Armstrong")
    else:
        print(n, "không phải là số Armstrong")
