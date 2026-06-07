# Chương trình so sánh diện tích

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

dien_tich_1 = float(input("Nhập diện tích thứ nhất: "))
dien_tich_2 = float(input("Nhập diện tích thứ hai: "))

if dien_tich_1 < 0 or dien_tich_2 < 0:
    print("Diện tích không được âm")
elif dien_tich_1 > dien_tich_2:
    print("Diện tích thứ nhất lớn hơn")
elif dien_tich_1 < dien_tich_2:
    print("Diện tích thứ hai lớn hơn")
else:
    print("Hai diện tích bằng nhau")
