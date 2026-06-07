# Chương trình kiểm tra số nguyên tố

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên cần kiểm tra: "))

if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    la_nguyen_to = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break

    if la_nguyen_to:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")
