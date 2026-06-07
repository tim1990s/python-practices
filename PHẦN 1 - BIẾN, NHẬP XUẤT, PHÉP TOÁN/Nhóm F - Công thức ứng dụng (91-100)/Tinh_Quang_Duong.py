# Chương trình tính quãng đường
#
# Quãng đường có thể tính bằng vận tốc nhân với thời gian di chuyển.
#
# Công thức:
# quang_duong = van_toc * thoi_gian
#
# Ý tưởng:
# - Nhập vận tốc.
# - Nhập thời gian di chuyển.
# - Kiểm tra vận tốc và thời gian không được âm.
# - Tính quãng đường và in kết quả ra màn hình.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

van_toc = float(input("Nhập vận tốc: "))
thoi_gian = float(input("Nhập thời gian di chuyển: "))

if van_toc < 0 or thoi_gian < 0:
    print("Vận tốc và thời gian không được âm")
else:
    quang_duong = van_toc * thoi_gian
    print("Quãng đường là:", quang_duong)
