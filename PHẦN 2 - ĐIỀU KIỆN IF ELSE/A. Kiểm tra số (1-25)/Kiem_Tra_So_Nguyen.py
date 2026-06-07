# Chương trình kiểm tra số nguyên

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

du_lieu = input("Nhập giá trị cần kiểm tra: ")

try:
    so = float(du_lieu)

    if so.is_integer():
        print(du_lieu, "là số nguyên")
    else:
        print(du_lieu, "không phải là số nguyên")
except ValueError:
    print(du_lieu, "không phải là số")
