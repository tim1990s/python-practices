# Chương trình đổi giây sang giờ
#
# 3600 giây = 1 giờ
#
# Công thức:
# gio = giay / 3600
#
# Ví dụ:
# Nếu giây = 7200 thì:
# giờ = 7200 / 3600 = 2
#
# Ý tưởng:
# - Nhập số giây.
# - Chia số giây cho 3600.
# - In kết quả ra màn hình.

giay = float(input("Nhập số giây: "))

gio = giay / 3600

print(giay, "giây =", gio, "giờ")
