# Chương trình kiểm tra điểm nằm trong hình chữ nhật

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập hoành độ điểm: "))
y = float(input("Nhập tung độ điểm: "))
x_min = float(input("Nhập x nhỏ nhất của hình chữ nhật: "))
y_min = float(input("Nhập y nhỏ nhất của hình chữ nhật: "))
x_max = float(input("Nhập x lớn nhất của hình chữ nhật: "))
y_max = float(input("Nhập y lớn nhất của hình chữ nhật: "))

if x_min > x_max or y_min > y_max:
    print("Tọa độ hình chữ nhật không hợp lệ")
elif x_min <= x <= x_max and y_min <= y <= y_max:
    print("Điểm nằm trong hoặc trên cạnh hình chữ nhật")
else:
    print("Điểm nằm ngoài hình chữ nhật")
