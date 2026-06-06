# Chương trình tính thuế thu nhập đơn giản
#
# Bài này tính thuế thu nhập theo một tỷ lệ phần trăm cố định.
#
# Công thức:
# tien_thue = thu_nhap * thue_suat / 100
# thu_nhap_sau_thue = thu_nhap - tien_thue
#
# Ý tưởng:
# - Nhập thu nhập.
# - Nhập thuế suất phần trăm.
# - Tính tiền thuế và thu nhập sau thuế.

thu_nhap = float(input("Nhập thu nhập: "))
thue_suat = float(input("Nhập thuế suất (%): "))

tien_thue = thu_nhap * thue_suat / 100
thu_nhap_sau_thue = thu_nhap - tien_thue

print("Tiền thuế thu nhập là:", tien_thue)
print("Thu nhập sau thuế là:", thu_nhap_sau_thue)
