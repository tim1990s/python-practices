# Chương trình kiểm tra điều kiện nghiệm không làm mẫu bằng 0

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập nghiệm cần kiểm tra: "))
a = float(input("Nhập hệ số a của mẫu: "))
b = float(input("Nhập hệ số b của mẫu: "))

if a * x + b != 0:
    print("Nghiệm thỏa điều kiện")
else:
    print("Nghiệm không thỏa điều kiện vì làm mẫu bằng 0")
