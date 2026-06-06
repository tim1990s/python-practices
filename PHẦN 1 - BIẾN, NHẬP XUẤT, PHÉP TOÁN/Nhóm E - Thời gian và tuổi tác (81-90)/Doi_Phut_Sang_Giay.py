# Chương trình đổi phút sang giây
#
# 1 phút = 60 giây
#
# Công thức:
# giay = phut * 60
#
# Ví dụ:
# Nếu phút = 5 thì:
# giây = 5 * 60 = 300
#
# Ý tưởng:
# - Nhập số phút.
# - Nhân số phút với 60.
# - In kết quả ra màn hình.

phut = float(input("Nhập số phút: "))

giay = phut * 60

print(phut, "phút =", giay, "giây")
