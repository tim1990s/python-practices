# Chương trình tính tiền tăng ca
#
# Tiền tăng ca thường được tính theo hệ số cao hơn tiền công bình thường.
#
# Công thức:
# tien_tang_ca = so_gio_tang_ca * tien_cong_moi_gio * he_so
#
# Ý tưởng:
# - Nhập số giờ tăng ca.
# - Nhập tiền công mỗi giờ.
# - Nhập hệ số tăng ca.
# - Tính tiền tăng ca.

so_gio_tang_ca = float(input("Nhập số giờ tăng ca: "))
tien_cong_moi_gio = float(input("Nhập tiền công mỗi giờ: "))
he_so = float(input("Nhập hệ số tăng ca: "))

tien_tang_ca = so_gio_tang_ca * tien_cong_moi_gio * he_so

print("Tiền tăng ca là:", tien_tang_ca)
