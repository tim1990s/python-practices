# Chương trình tính điểm trung bình học tập
#
# Điểm trung bình học tập có thể tính bằng tổng điểm chia cho số môn học.
#
# Công thức:
# diem_trung_binh = tong_diem / so_mon
#
# Ý tưởng:
# - Nhập tổng điểm.
# - Nhập số môn học.
# - Kiểm tra số môn học phải lớn hơn 0.
# - Tính điểm trung bình và in kết quả ra màn hình.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

tong_diem = float(input("Nhập tổng điểm: "))
so_mon = int(input("Nhập số môn học: "))

if so_mon <= 0:
    print("Số môn học phải lớn hơn 0")
else:
    diem_trung_binh = tong_diem / so_mon
    print("Điểm trung bình học tập là:", diem_trung_binh)
