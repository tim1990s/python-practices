# Chương trình giải bất phương trình bậc nhất dạng a*x + b > 0

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a == 0:
    if b > 0:
        print("Bất phương trình đúng với mọi x")
    else:
        print("Bất phương trình vô nghiệm")
elif a > 0:
    print("Nghiệm của bất phương trình là x >", -b / a)
else:
    print("Nghiệm của bất phương trình là x <", -b / a)
