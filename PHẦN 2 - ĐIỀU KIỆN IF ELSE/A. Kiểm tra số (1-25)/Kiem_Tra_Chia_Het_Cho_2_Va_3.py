# Chương trình kiểm tra chia hết cho 2 và 3

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên cần kiểm tra: "))

if n % 2 == 0 and n % 3 == 0:
    print(n, "chia hết cho cả 2 và 3")
else:
    print(n, "không chia hết cho cả 2 và 3")
