# Chương trình giải phương trình chứa căn dạng sqrt(a*x + b) = c

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập vế phải c: "))

if c < 0:
    print("Phương trình vô nghiệm vì căn bậc hai không âm")
elif a == 0:
    if b >= 0 and math.sqrt(b) == c:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = (c ** 2 - b) / a

    if a * x + b >= 0:
        print("Nghiệm của phương trình là x =", x)
    else:
        print("Phương trình vô nghiệm")
