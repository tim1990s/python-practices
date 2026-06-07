# Chương trình giải phương trình phân thức dạng (a*x + b) / (c*x + d) = 0

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
d = float(input("Nhập hệ số d: "))

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm, trừ các giá trị làm mẫu bằng 0")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a

    if c * x + d == 0:
        print("Phương trình vô nghiệm vì nghiệm làm mẫu bằng 0")
    else:
        print("Nghiệm của phương trình là x =", x)
