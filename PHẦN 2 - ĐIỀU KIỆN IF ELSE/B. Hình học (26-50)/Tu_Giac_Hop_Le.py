# Chương trình kiểm tra tứ giác hợp lệ theo 4 cạnh

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

a = float(input("Nhập cạnh thứ nhất: "))
b = float(input("Nhập cạnh thứ hai: "))
c = float(input("Nhập cạnh thứ ba: "))
d = float(input("Nhập cạnh thứ tư: "))

canh = [a, b, c, d]

if a <= 0 or b <= 0 or c <= 0 or d <= 0:
    print("Bốn cạnh phải lớn hơn 0")
elif max(canh) < sum(canh) - max(canh):
    print("Bốn cạnh có thể tạo thành tứ giác hợp lệ")
else:
    print("Bốn cạnh không tạo thành tứ giác hợp lệ")
