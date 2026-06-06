# Chương trình tính tiền lãi đơn
#
# Lãi đơn là tiền lãi được tính trên số tiền gốc ban đầu.
#
# Công thức:
# tien_lai = tien_goc * lai_suat * thoi_gian / 100
# tong_tien = tien_goc + tien_lai
#
# Ý tưởng:
# - Nhập tiền gốc, lãi suất phần trăm mỗi năm và thời gian gửi theo năm.
# - Tính tiền lãi đơn.
# - Cộng tiền gốc với tiền lãi để ra tổng tiền.

tien_goc = float(input("Nhập số tiền gốc: "))
lai_suat = float(input("Nhập lãi suất mỗi năm (%): "))
thoi_gian = float(input("Nhập thời gian gửi (năm): "))

tien_lai = tien_goc * lai_suat * thoi_gian / 100
tong_tien = tien_goc + tien_lai

print("Tiền lãi đơn là:", tien_lai)
print("Tổng tiền nhận được là:", tong_tien)
