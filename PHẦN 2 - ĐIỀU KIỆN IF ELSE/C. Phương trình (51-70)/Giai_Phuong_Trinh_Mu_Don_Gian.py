# Chương trình giải phương trình mũ đơn giản dạng a^x = b

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math

a = float(input("Nhập cơ số a: "))
b = float(input("Nhập vế phải b: "))

if a <= 0 or a == 1:
    print("Cơ số a phải lớn hơn 0 và khác 1")
elif b <= 0:
    print("Phương trình vô nghiệm")
else:
    x = math.log(b, a)
    print("Nghiệm của phương trình là x =", x)
