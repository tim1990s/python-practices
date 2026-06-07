# Chương trình tính giai thừa

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

giai_thua = 1

if n < 0:
    print("N không được âm")
else:
    for i in range(1, n + 1):
        giai_thua *= i

    print(n, "! =", giai_thua)
