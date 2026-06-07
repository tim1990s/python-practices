# Chương trình chọn loại khách hàng theo tổng chi tiêu

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

tong_chi_tieu = float(input("Nhập tổng chi tiêu: "))

if tong_chi_tieu < 0:
    print("Tổng chi tiêu không được âm")
elif tong_chi_tieu >= 100000000:
    print("Khách hàng VIP")
elif tong_chi_tieu >= 30000000:
    print("Khách hàng thân thiết")
elif tong_chi_tieu >= 5000000:
    print("Khách hàng tiềm năng")
else:
    print("Khách hàng mới")
