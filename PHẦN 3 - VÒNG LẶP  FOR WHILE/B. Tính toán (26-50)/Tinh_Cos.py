# Chương trình tính cos(x) xấp xỉ bằng chuỗi Taylor

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập x theo radian: "))
n = int(input("Nhập số lượng số hạng: "))

if n <= 0:
    print("Số lượng số hạng phải lớn hơn 0")
else:
    cos_x = 0

    for i in range(n):
        mu = 2 * i
        giai_thua = 1

        for j in range(1, mu + 1):
            giai_thua *= j

        cos_x += ((-1) ** i) * (x ** mu) / giai_thua

    print("cos(x) xấp xỉ là:", cos_x)
