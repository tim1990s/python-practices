# Chương trình kiểm tra hai đường thẳng song song

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))

if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
    print("Hệ số đường thẳng không hợp lệ")
elif a1 * b2 == a2 * b1 and (a1 * c2 != a2 * c1 or b1 * c2 != b2 * c1):
    print("Hai đường thẳng song song")
else:
    print("Hai đường thẳng không song song")
