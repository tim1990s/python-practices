# Chương trình tính tiền bảo hiểm bắt buộc đơn giản

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

luong = float(input("Nhập mức lương: "))

if luong < 0:
    print("Mức lương không được âm")
else:
    bhxh = luong * 0.08
    bhyt = luong * 0.015
    bhtn = luong * 0.01
    tong = bhxh + bhyt + bhtn

    print("Bảo hiểm xã hội:", bhxh)
    print("Bảo hiểm y tế:", bhyt)
    print("Bảo hiểm thất nghiệp:", bhtn)
    print("Tổng tiền bảo hiểm:", tong)
