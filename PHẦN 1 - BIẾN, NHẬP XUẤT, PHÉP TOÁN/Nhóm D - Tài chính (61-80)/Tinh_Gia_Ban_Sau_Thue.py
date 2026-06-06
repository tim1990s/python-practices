# Chương trình tính giá bán sau thuế
#
# Giá bán sau thuế bằng giá bán ban đầu cộng với tiền thuế.
#
# Công thức:
# tien_thue = gia_ban * thue_suat / 100
# gia_sau_thue = gia_ban + tien_thue
#
# Ý tưởng:
# - Nhập giá bán ban đầu.
# - Nhập thuế suất phần trăm.
# - Tính tiền thuế và giá sau thuế.

gia_ban = float(input("Nhập giá bán ban đầu: "))
thue_suat = float(input("Nhập thuế suất (%): "))

tien_thue = gia_ban * thue_suat / 100
gia_sau_thue = gia_ban + tien_thue

print("Tiền thuế là:", tien_thue)
print("Giá bán sau thuế là:", gia_sau_thue)
