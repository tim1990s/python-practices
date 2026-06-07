# Chương trình giải phương trình log đơn giản dạng log_a(x) = b

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập cơ số a: "))
b = float(input("Nhập vế phải b: "))

if a <= 0 or a == 1:
    print("Cơ số a phải lớn hơn 0 và khác 1")
else:
    x = a ** b
    print("Nghiệm của phương trình là x =", x)
