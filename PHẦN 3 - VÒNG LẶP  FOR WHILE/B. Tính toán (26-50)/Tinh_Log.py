# Chương trình tính ln(x) xấp xỉ bằng chuỗi Taylor biến đổi

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập x dương: "))
n = int(input("Nhập số lượng số hạng: "))

if x <= 0 or n <= 0:
    print("x và số lượng số hạng phải lớn hơn 0")
else:
    y = (x - 1) / (x + 1)
    tong = 0

    for i in range(n):
        mu = 2 * i + 1
        tong += (y ** mu) / mu

    log_x = 2 * tong
    print("ln(x) xấp xỉ là:", log_x)
