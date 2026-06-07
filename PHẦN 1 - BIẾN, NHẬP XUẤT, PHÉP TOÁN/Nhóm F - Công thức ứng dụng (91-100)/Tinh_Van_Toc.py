# Chương trình tính vận tốc
#
# Vận tốc cho biết quãng đường đi được trong một đơn vị thời gian.
#
# Công thức:
# van_toc = quang_duong / thoi_gian
#
# Ý tưởng:
# - Nhập quãng đường.
# - Nhập thời gian di chuyển.
# - Kiểm tra thời gian phải lớn hơn 0.
# - Tính vận tốc và in kết quả ra màn hình.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

quang_duong = float(input("Nhập quãng đường đã đi: "))
thoi_gian = float(input("Nhập thời gian di chuyển: "))

if thoi_gian <= 0:
    print("Thời gian phải lớn hơn 0")
else:
    van_toc = quang_duong / thoi_gian
    print("Vận tốc là:", van_toc)
