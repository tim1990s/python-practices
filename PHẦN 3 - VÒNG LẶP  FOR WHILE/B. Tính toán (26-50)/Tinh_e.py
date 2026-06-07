# Chương trình tính e xấp xỉ bằng chuỗi 1/n!

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng số hạng: "))

if n <= 0:
    print("Số lượng số hạng phải lớn hơn 0")
else:
    e = 0
    giai_thua = 1

    for i in range(n):
        if i > 0:
            giai_thua *= i

        e += 1 / giai_thua

    print("e xấp xỉ là:", e)
