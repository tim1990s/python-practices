# Chương trình tính mật độ dân số
#
# Mật độ dân số cho biết trung bình có bao nhiêu người trên một đơn vị diện tích.
#
# Công thức:
# mat_do = dan_so / dien_tich
#
# Ý tưởng:
# - Nhập dân số.
# - Nhập diện tích.
# - Kiểm tra dân số không âm và diện tích phải lớn hơn 0.
# - Tính mật độ dân số và in kết quả ra màn hình.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

dan_so = int(input("Nhập dân số: "))
dien_tich = float(input("Nhập diện tích: "))

if dan_so < 0:
    print("Dân số không được âm")
elif dien_tich <= 0:
    print("Diện tích phải lớn hơn 0")
else:
    mat_do = dan_so / dien_tich
    print("Mật độ dân số là:", mat_do)
