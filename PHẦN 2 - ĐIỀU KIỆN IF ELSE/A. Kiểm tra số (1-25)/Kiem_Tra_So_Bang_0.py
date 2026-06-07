# Chương trình kiểm tra số bằng 0

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = float(input("Nhập số cần kiểm tra: "))

if n == 0:
    print("Số vừa nhập bằng 0")
else:
    print("Số vừa nhập không bằng 0")
