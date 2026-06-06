# Chương trình tính số tiền tiết kiệm hằng tháng
#
# Số tiền tiết kiệm hằng tháng bằng thu nhập hằng tháng trừ chi tiêu hằng tháng.
#
# Công thức:
# tiet_kiem = thu_nhap_hang_thang - chi_tieu_hang_thang
#
# Ý tưởng:
# - Nhập thu nhập hằng tháng.
# - Nhập chi tiêu hằng tháng.
# - Lấy thu nhập trừ chi tiêu.

thu_nhap_hang_thang = float(input("Nhập thu nhập hằng tháng: "))
chi_tieu_hang_thang = float(input("Nhập chi tiêu hằng tháng: "))

tiet_kiem = thu_nhap_hang_thang - chi_tieu_hang_thang

print("Số tiền tiết kiệm hằng tháng là:", tiet_kiem)
