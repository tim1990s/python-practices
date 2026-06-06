# Chương trình đổi phút sang giờ
#
# 60 phút = 1 giờ
#
# Công thức:
# gio = phut / 60
#
# Ví dụ:
# Nếu phút = 90 thì:
# giờ = 90 / 60 = 1.5
#
# Ý tưởng:
# - Nhập số phút.
# - Chia số phút cho 60.
# - In kết quả ra màn hình.

phut = float(input("Nhập số phút: "))

gio = phut / 60

print(phut, "phút =", gio, "giờ")
