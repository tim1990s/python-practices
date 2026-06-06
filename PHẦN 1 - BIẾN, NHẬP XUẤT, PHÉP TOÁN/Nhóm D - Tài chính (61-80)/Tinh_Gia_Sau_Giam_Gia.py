# Chương trình tính giá sau giảm giá
#
# Giá sau giảm giá là giá gốc trừ đi số tiền được giảm.
#
# Công thức:
# tien_giam = gia_goc * phan_tram_giam / 100
# gia_sau_giam = gia_goc - tien_giam
#
# Ý tưởng:
# - Nhập giá gốc và phần trăm giảm giá.
# - Tính số tiền được giảm.
# - Lấy giá gốc trừ tiền giảm.

gia_goc = float(input("Nhập giá gốc: "))
phan_tram_giam = float(input("Nhập phần trăm giảm giá: "))

tien_giam = gia_goc * phan_tram_giam / 100
gia_sau_giam = gia_goc - tien_giam

print("Số tiền được giảm là:", tien_giam)
print("Giá sau giảm giá là:", gia_sau_giam)
