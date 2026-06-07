# Chương trình tính hoa hồng theo doanh số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

doanh_so = float(input("Nhập doanh số: "))

if doanh_so < 0:
    print("Doanh số không được âm")
elif doanh_so >= 100000000:
    hoa_hong = doanh_so * 0.10
    print("Hoa hồng là:", hoa_hong)
elif doanh_so >= 50000000:
    hoa_hong = doanh_so * 0.07
    print("Hoa hồng là:", hoa_hong)
elif doanh_so >= 10000000:
    hoa_hong = doanh_so * 0.05
    print("Hoa hồng là:", hoa_hong)
else:
    hoa_hong = doanh_so * 0.02
    print("Hoa hồng là:", hoa_hong)
