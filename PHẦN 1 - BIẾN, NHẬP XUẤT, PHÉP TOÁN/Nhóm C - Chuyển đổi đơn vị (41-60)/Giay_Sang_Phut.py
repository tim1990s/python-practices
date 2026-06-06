# Chương trình đổi giây sang phút
#
# 60 giây = 1 phút
#
# Công thức:
# phut = giay / 60
#
# Ví dụ:
# Nếu giây = 120 thì:
# phút = 120 / 60 = 2
#
# Ý tưởng:
# - Nhập số giây.
# - Chia số giây cho 60.
# - In kết quả ra màn hình.

giay = float(input("Nhập số giây: "))

phut = giay / 60

print(giay, "giây =", phut, "phút")
