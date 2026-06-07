# Chương trình kiểm tra điểm nằm trong hình tròn

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập hoành độ điểm: "))
y = float(input("Nhập tung độ điểm: "))
x_tam = float(input("Nhập hoành độ tâm: "))
y_tam = float(input("Nhập tung độ tâm: "))
r = float(input("Nhập bán kính: "))

if r <= 0:
    print("Bán kính phải lớn hơn 0")
elif (x - x_tam) ** 2 + (y - y_tam) ** 2 <= r ** 2:
    print("Điểm nằm trong hoặc trên đường tròn")
else:
    print("Điểm nằm ngoài hình tròn")
