# Chương trình kiểm tra số nghiệm của phương trình bậc hai

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có một nghiệm")
else:
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        print("Phương trình có hai nghiệm phân biệt")
    elif delta == 0:
        print("Phương trình có một nghiệm kép")
    else:
        print("Phương trình vô nghiệm trong tập số thực")
