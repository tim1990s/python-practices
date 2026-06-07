# Chương trình kiểm tra số nhị phân

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chuoi = input("Nhập chuỗi cần kiểm tra: ")
hop_le = chuoi != ""

for ky_tu in chuoi:
    if ky_tu not in "01":
        hop_le = False
        break

if hop_le:
    print("Đây là số nhị phân")
else:
    print("Đây không phải là số nhị phân")
