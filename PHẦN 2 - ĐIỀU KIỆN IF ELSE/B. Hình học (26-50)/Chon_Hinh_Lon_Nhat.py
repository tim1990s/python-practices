# Chương trình chọn hình lớn nhất theo diện tích

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

dien_tich_1 = float(input("Nhập diện tích hình thứ nhất: "))
dien_tich_2 = float(input("Nhập diện tích hình thứ hai: "))
dien_tich_3 = float(input("Nhập diện tích hình thứ ba: "))

if dien_tich_1 < 0 or dien_tich_2 < 0 or dien_tich_3 < 0:
    print("Diện tích không được âm")
elif dien_tich_1 >= dien_tich_2 and dien_tich_1 >= dien_tich_3:
    print("Hình thứ nhất lớn nhất")
elif dien_tich_2 >= dien_tich_1 and dien_tich_2 >= dien_tich_3:
    print("Hình thứ hai lớn nhất")
else:
    print("Hình thứ ba lớn nhất")
