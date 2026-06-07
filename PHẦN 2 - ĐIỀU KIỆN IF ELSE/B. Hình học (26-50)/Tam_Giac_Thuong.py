# Chương trình kiểm tra tam giác thường

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập cạnh thứ nhất: "))
b = float(input("Nhập cạnh thứ hai: "))
c = float(input("Nhập cạnh thứ ba: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Ba cạnh phải lớn hơn 0")
elif not (a + b > c and a + c > b and b + c > a):
    print("Ba cạnh không tạo thành tam giác")
else:
    x, y, z = sorted([a, b, c])
    la_vuong = abs(x * x + y * y - z * z) < 1e-9
    la_can = a == b or a == c or b == c

    if not la_can and not la_vuong:
        print("Đây là tam giác thường")
    else:
        print("Đây không phải là tam giác thường")
