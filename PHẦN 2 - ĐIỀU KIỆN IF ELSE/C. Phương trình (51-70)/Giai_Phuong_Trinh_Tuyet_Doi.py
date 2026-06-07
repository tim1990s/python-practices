# Chương trình giải phương trình tuyệt đối dạng |a*x + b| = c

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập vế phải c: "))

if c < 0:
    print("Phương trình vô nghiệm")
elif a == 0:
    if abs(b) == c:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
elif c == 0:
    x = -b / a
    print("Phương trình có nghiệm x =", x)
else:
    x1 = (c - b) / a
    x2 = (-c - b) / a
    print("Phương trình có hai nghiệm:")
    print("x1 =", x1)
    print("x2 =", x2)
