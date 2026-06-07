# Chương trình đếm số chữ số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên cần kiểm tra: "))
so_chu_so = len(str(abs(n)))

print(n, "có", so_chu_so, "chữ số")
