# Chương trình đổi EUR sang VND
#
# Bài này dùng tỷ giá cố định để luyện tập phép nhân.
# Có thể thay đổi biến ty_gia_eur nếu muốn dùng tỷ giá khác.
#
# Quy ước:
# 1 EUR = 27000 VND
#
# Công thức:
# vnd = eur * ty_gia_eur
#
# Ví dụ:
# Nếu EUR = 10 thì:
# VND = 10 * 27000 = 270000
#
# Ý tưởng:
# - Nhập số tiền EUR.
# - Nhân số EUR với tỷ giá.
# - In kết quả ra màn hình.

ty_gia_eur = 27000

eur = float(input("Nhập số tiền EUR: "))

vnd = eur * ty_gia_eur

print(eur, "EUR =", vnd, "VND")
