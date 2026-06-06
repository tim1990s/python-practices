# Chương trình tính số tiền gửi sau n tháng
#
# Bài này tính theo lãi đơn hằng tháng.
#
# Công thức:
# tien_lai = tien_goc * lai_suat_thang * so_thang / 100
# tong_tien = tien_goc + tien_lai
#
# Ý tưởng:
# - Nhập tiền gốc, lãi suất mỗi tháng và số tháng gửi.
# - Tính tiền lãi theo số tháng.
# - In tổng tiền sau n tháng.

tien_goc = float(input("Nhập số tiền gửi ban đầu: "))
lai_suat_thang = float(input("Nhập lãi suất mỗi tháng (%): "))
so_thang = int(input("Nhập số tháng gửi: "))

tien_lai = tien_goc * lai_suat_thang * so_thang / 100
tong_tien = tien_goc + tien_lai

print("Tiền lãi sau", so_thang, "tháng là:", tien_lai)
print("Tổng tiền sau", so_thang, "tháng là:", tong_tien)
