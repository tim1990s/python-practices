# Chương trình kiểm tra số đối xứng

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên cần kiểm tra: "))

if n < 0:
    print(n, "không phải là số đối xứng")
else:
    chuoi = str(n)

    if chuoi == chuoi[::-1]:
        print(n, "là số đối xứng")
    else:
        print(n, "không phải là số đối xứng")
