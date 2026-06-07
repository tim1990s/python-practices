# Chương trình tính tiền internet theo gói dịch vụ

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

goi = input("Nhập gói internet (co ban/nang cao/cao cap): ").lower()
so_thang = int(input("Nhập số tháng sử dụng: "))

if so_thang <= 0:
    print("Số tháng sử dụng phải lớn hơn 0")
elif goi == "co ban":
    tien = 150000 * so_thang
    print("Tiền internet phải trả là:", tien, "đồng")
elif goi == "nang cao":
    tien = 250000 * so_thang
    print("Tiền internet phải trả là:", tien, "đồng")
elif goi == "cao cap":
    tien = 400000 * so_thang
    print("Tiền internet phải trả là:", tien, "đồng")
else:
    print("Gói internet không hợp lệ")
