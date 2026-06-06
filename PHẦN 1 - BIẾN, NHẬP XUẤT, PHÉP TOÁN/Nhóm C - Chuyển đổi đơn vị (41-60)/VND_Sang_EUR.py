# Chương trình đổi VND sang EUR
#
# Bài này dùng tỷ giá cố định để luyện tập phép chia.
# Có thể thay đổi biến ty_gia_eur nếu muốn dùng tỷ giá khác.
#
# Quy ước:
# 1 EUR = 27000 VND
#
# Công thức:
# eur = vnd / ty_gia_eur
#
# Ví dụ:
# Nếu VND = 270000 thì:
# EUR = 270000 / 27000 = 10
#
# Ý tưởng:
# - Nhập số tiền VND.
# - Chia số VND cho tỷ giá EUR.
# - In kết quả ra màn hình.

ty_gia_eur = 27000

vnd = float(input("Nhập số tiền VND: "))

eur = vnd / ty_gia_eur

print(vnd, "VND =", eur, "EUR")
