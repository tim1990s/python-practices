# Chương trình đổi USD sang VND
#
# Bài này dùng tỷ giá cố định để luyện tập phép nhân.
# Có thể thay đổi biến ty_gia_usd nếu muốn dùng tỷ giá khác.
#
# Quy ước:
# 1 USD = 25000 VND
#
# Công thức:
# vnd = usd * ty_gia_usd
#
# Ví dụ:
# Nếu USD = 10 thì:
# VND = 10 * 25000 = 250000
#
# Ý tưởng:
# - Nhập số tiền USD.
# - Nhân số USD với tỷ giá.
# - In kết quả ra màn hình.

ty_gia_usd = 25000

usd = float(input("Nhập số tiền USD: "))

vnd = usd * ty_gia_usd

print(usd, "USD =", vnd, "VND")
