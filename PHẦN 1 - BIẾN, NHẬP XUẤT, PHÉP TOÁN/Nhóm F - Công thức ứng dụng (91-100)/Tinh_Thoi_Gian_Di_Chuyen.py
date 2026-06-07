# Chương trình tính thời gian di chuyển
#
# Thời gian di chuyển có thể tính bằng quãng đường chia cho vận tốc.
#
# Công thức:
# thoi_gian = quang_duong / van_toc
#
# Ý tưởng:
# - Nhập quãng đường.
# - Nhập vận tốc.
# - Kiểm tra vận tốc phải lớn hơn 0.
# - Tính thời gian và in kết quả ra màn hình.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

quang_duong = float(input("Nhập quãng đường: "))
van_toc = float(input("Nhập vận tốc: "))

if van_toc <= 0:
    print("Vận tốc phải lớn hơn 0")
else:
    thoi_gian = quang_duong / van_toc
    print("Thời gian di chuyển là:", thoi_gian)
