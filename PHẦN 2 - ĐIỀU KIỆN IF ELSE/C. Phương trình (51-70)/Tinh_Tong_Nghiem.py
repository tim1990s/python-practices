# Chương trình tính tổng nghiệm của phương trình bậc hai

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Đây không phải là phương trình bậc hai")
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Phương trình vô nghiệm trong tập số thực")
    else:
        tong = -b / a
        print("Tổng nghiệm là:", tong)
