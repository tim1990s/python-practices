# Chương trình in bảng ASCII trong một khoảng mã

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

bat_dau = int(input("Nhập mã ASCII bắt đầu: "))
ket_thuc = int(input("Nhập mã ASCII kết thúc: "))

if bat_dau < 0 or ket_thuc < 0 or bat_dau > ket_thuc:
    print("Khoảng mã ASCII không hợp lệ")
else:
    for ma in range(bat_dau, ket_thuc + 1):
        print(ma, "=", chr(ma))
