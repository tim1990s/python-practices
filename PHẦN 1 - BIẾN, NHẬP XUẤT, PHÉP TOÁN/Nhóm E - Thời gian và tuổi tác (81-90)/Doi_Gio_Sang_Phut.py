# Chương trình đổi giờ sang phút
#
# 1 giờ = 60 phút
#
# Công thức:
# phut = gio * 60
#
# Ví dụ:
# Nếu giờ = 2 thì:
# phút = 2 * 60 = 120
#
# Ý tưởng:
# - Nhập số giờ.
# - Nhân số giờ với 60.
# - In kết quả ra màn hình.

gio = float(input("Nhập số giờ: "))

phut = gio * 60

print(gio, "giờ =", phut, "phút")
