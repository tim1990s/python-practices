# Chương trình so sánh n số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng số cần so sánh: "))

if n <= 0:
    print("Số lượng số phải lớn hơn 0")
else:
    so_dau_tien = float(input("Nhập số thứ 1: "))
    lon_nhat = so_dau_tien
    nho_nhat = so_dau_tien

    for i in range(2, n + 1):
        so = float(input("Nhập số thứ " + str(i) + ": "))

        if so > lon_nhat:
            lon_nhat = so

        if so < nho_nhat:
            nho_nhat = so

    print("Số lớn nhất là:", lon_nhat)
    print("Số nhỏ nhất là:", nho_nhat)
