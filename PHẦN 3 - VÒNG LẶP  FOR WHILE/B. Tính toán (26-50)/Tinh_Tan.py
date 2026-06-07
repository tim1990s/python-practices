# Chương trình tính tan(x) xấp xỉ từ sin(x) và cos(x)

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
    sin_x = 0
    cos_x = 0

    for i in range(n):
        mu_sin = 2 * i + 1
        giai_thua_sin = 1

        for j in range(1, mu_sin + 1):
            giai_thua_sin *= j

        sin_x += ((-1) ** i) * (x ** mu_sin) / giai_thua_sin

        mu_cos = 2 * i
        giai_thua_cos = 1

        for j in range(1, mu_cos + 1):
            giai_thua_cos *= j

        cos_x += ((-1) ** i) * (x ** mu_cos) / giai_thua_cos

    if cos_x == 0:
        print("Không tính được tan(x) vì cos(x) bằng 0")
    else:
        print("tan(x) xấp xỉ là:", sin_x / cos_x)
