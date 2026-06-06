# Chương trình tính tiền điện đơn giản
#
# Bài này tính tiền điện theo một đơn giá cố định.
#
# Công thức:
# tien_dien = so_kwh * don_gia
#
# Ý tưởng:
# - Nhập số kWh đã dùng.
# - Nhập đơn giá cho mỗi kWh.
# - Nhân số kWh với đơn giá.

so_kwh = float(input("Nhập số kWh điện đã dùng: "))
don_gia = float(input("Nhập đơn giá mỗi kWh: "))

tien_dien = so_kwh * don_gia

print("Tiền điện phải trả là:", tien_dien)
