# Chương trình tính năng suất lao động
#
# Năng suất lao động cho biết số sản phẩm làm được trong một đơn vị thời gian.
#
# Công thức:
# nang_suat = so_san_pham / thoi_gian
#
# Ý tưởng:
# - Nhập số sản phẩm.
# - Nhập thời gian làm việc.
# - Kiểm tra số sản phẩm không âm và thời gian phải lớn hơn 0.
# - Tính năng suất lao động và in kết quả ra màn hình.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

so_san_pham = int(input("Nhập số sản phẩm: "))
thoi_gian = float(input("Nhập thời gian làm việc: "))

if so_san_pham < 0:
    print("Số sản phẩm không được âm")
elif thoi_gian <= 0:
    print("Thời gian làm việc phải lớn hơn 0")
else:
    nang_suat = so_san_pham / thoi_gian
    print("Năng suất lao động là:", nang_suat)
