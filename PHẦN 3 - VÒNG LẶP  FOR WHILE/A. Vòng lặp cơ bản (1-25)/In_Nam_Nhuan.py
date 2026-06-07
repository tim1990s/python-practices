# Chương trình in các năm nhuận trong khoảng

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

bat_dau = int(input("Nhập năm bắt đầu: "))
ket_thuc = int(input("Nhập năm kết thúc: "))

if bat_dau <= 0 or ket_thuc <= 0 or bat_dau > ket_thuc:
    print("Khoảng năm không hợp lệ")
else:
    for nam in range(bat_dau, ket_thuc + 1):
        if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
            print(nam)
