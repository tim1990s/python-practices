# Chương trình kiểm tra 3 cạnh tạo tam giác

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
elif a + b > c and a + c > b and b + c > a:
    print("Ba cạnh có thể tạo thành tam giác")
else:
    print("Ba cạnh không thể tạo thành tam giác")
