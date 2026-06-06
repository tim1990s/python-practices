# Chương trình đổi VND sang USD
#
# Bài này dùng tỷ giá cố định để luyện tập phép chia.
# Có thể thay đổi biến ty_gia_usd nếu muốn dùng tỷ giá khác.
#
# Quy ước:
# 1 USD = 25000 VND
#
# Công thức:
# usd = vnd / ty_gia_usd
#
# Ví dụ:
# Nếu VND = 250000 thì:
# USD = 250000 / 25000 = 10
#
# Ý tưởng:
# - Nhập số tiền VND.
# - Chia số VND cho tỷ giá USD.
# - In kết quả ra màn hình.

ty_gia_usd = 25000

vnd = float(input("Nhập số tiền VND: "))

usd = vnd / ty_gia_usd

print(vnd, "VND =", usd, "USD")
