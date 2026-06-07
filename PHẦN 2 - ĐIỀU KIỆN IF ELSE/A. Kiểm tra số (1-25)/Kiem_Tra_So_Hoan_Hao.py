# Chương trình kiểm tra số hoàn hảo

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên cần kiểm tra: "))

if n <= 0:
    print(n, "không phải là số hoàn hảo")
else:
    tong_uoc = 0

    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i

    if tong_uoc == n:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải là số hoàn hảo")
