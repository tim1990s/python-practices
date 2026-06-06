# Chương trình tính tiền lãi kép
#
# Lãi kép là tiền lãi được cộng vào tiền gốc sau mỗi kỳ.
#
# Công thức:
# tong_tien = tien_goc * (1 + lai_suat / 100) ** so_nam
# tien_lai = tong_tien - tien_goc
#
# Ý tưởng:
# - Nhập tiền gốc, lãi suất phần trăm mỗi năm và số năm gửi.
# - Tính tổng tiền theo công thức lãi kép.
# - Tính tiền lãi bằng tổng tiền trừ tiền gốc.

tien_goc = float(input("Nhập số tiền gốc: "))
lai_suat = float(input("Nhập lãi suất mỗi năm (%): "))
so_nam = float(input("Nhập số năm gửi: "))

tong_tien = tien_goc * (1 + lai_suat / 100) ** so_nam
tien_lai = tong_tien - tien_goc

print("Tiền lãi kép là:", tien_lai)
print("Tổng tiền nhận được là:", tong_tien)
