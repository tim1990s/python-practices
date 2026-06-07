# Chương trình in các số nguyên tố từ 1 đến N

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập N: "))

if n < 2:
    print("Không có số nguyên tố nào")
else:
    for so in range(2, n + 1):
        la_nguyen_to = True

        for i in range(2, int(so ** 0.5) + 1):
            if so % i == 0:
                la_nguyen_to = False
                break

        if la_nguyen_to:
            print(so)
