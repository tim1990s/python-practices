# Chương trình tính tiền lương theo giờ
#
# Lương theo giờ bằng số giờ làm nhân với tiền công mỗi giờ.
#
# Công thức:
# tien_luong = so_gio_lam * tien_cong_moi_gio
#
# Ý tưởng:
# - Nhập số giờ làm.
# - Nhập tiền công mỗi giờ.
# - Nhân hai giá trị để tính lương.

so_gio_lam = float(input("Nhập số giờ làm: "))
tien_cong_moi_gio = float(input("Nhập tiền công mỗi giờ: "))

tien_luong = so_gio_lam * tien_cong_moi_gio

print("Tiền lương là:", tien_luong)
