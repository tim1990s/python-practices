# Chương trình kiểm tra nghiệm thuộc tập xác định của biểu thức sqrt(a*x + b) / (c*x + d)

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập giá trị x: "))
a = float(input("Nhập hệ số a trong căn: "))
b = float(input("Nhập hệ số b trong căn: "))
c = float(input("Nhập hệ số c ở mẫu: "))
d = float(input("Nhập hệ số d ở mẫu: "))

if a * x + b < 0:
    print("x không thuộc tập xác định vì biểu thức trong căn âm")
elif c * x + d == 0:
    print("x không thuộc tập xác định vì mẫu bằng 0")
else:
    print("x thuộc tập xác định")
