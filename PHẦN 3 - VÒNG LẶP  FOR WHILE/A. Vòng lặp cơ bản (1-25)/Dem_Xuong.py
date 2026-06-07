# Chương trình đếm xuống

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

bat_dau = int(input("Nhập số bắt đầu: "))
ket_thuc = int(input("Nhập số kết thúc: "))

if bat_dau < ket_thuc:
    print("Số bắt đầu phải lớn hơn hoặc bằng số kết thúc")
else:
    while bat_dau >= ket_thuc:
        print(bat_dau)
        bat_dau -= 1
