# Chương trình kiểm tra hình thoi

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập cạnh thứ nhất: "))
b = float(input("Nhập cạnh thứ hai: "))
c = float(input("Nhập cạnh thứ ba: "))
d = float(input("Nhập cạnh thứ tư: "))

if a <= 0 or b <= 0 or c <= 0 or d <= 0:
    print("Bốn cạnh phải lớn hơn 0")
elif a == b == c == d:
    print("Đây là hình thoi")
else:
    print("Đây không phải là hình thoi")
