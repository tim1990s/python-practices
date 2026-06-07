# Chương trình kiểm tra hình vuông

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập cạnh thứ nhất: "))
b = float(input("Nhập cạnh thứ hai: "))
c = float(input("Nhập cạnh thứ ba: "))
d = float(input("Nhập cạnh thứ tư: "))
goc1 = float(input("Nhập góc thứ nhất: "))
goc2 = float(input("Nhập góc thứ hai: "))
goc3 = float(input("Nhập góc thứ ba: "))
goc4 = float(input("Nhập góc thứ tư: "))

if a <= 0 or b <= 0 or c <= 0 or d <= 0:
    print("Bốn cạnh phải lớn hơn 0")
elif a == b == c == d and goc1 == goc2 == goc3 == goc4 == 90:
    print("Đây là hình vuông")
else:
    print("Đây không phải là hình vuông")
