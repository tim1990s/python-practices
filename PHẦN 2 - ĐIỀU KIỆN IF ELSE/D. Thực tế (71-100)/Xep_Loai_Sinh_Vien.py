# Chương trình xếp loại sinh viên theo GPA hệ 4

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

gpa = float(input("Nhập GPA hệ 4: "))

if gpa < 0 or gpa > 4:
    print("GPA phải từ 0 đến 4")
elif gpa >= 3.6:
    print("Sinh viên xuất sắc")
elif gpa >= 3.2:
    print("Sinh viên giỏi")
elif gpa >= 2.5:
    print("Sinh viên khá")
elif gpa >= 2.0:
    print("Sinh viên trung bình")
else:
    print("Sinh viên yếu")
