# Chương trình đổi ngày sang giờ
#
# 1 ngày = 24 giờ
#
# Công thức:
# gio = ngay * 24
#
# Ví dụ:
# Nếu ngày = 3 thì:
# giờ = 3 * 24 = 72
#
# Ý tưởng:
# - Nhập số ngày.
# - Nhân số ngày với 24.
# - In kết quả ra màn hình.

ngay = float(input("Nhập số ngày: "))

gio = ngay * 24

print(ngay, "ngày =", gio, "giờ")
