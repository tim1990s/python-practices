# Chương trình đổi g sang kg
#
# 1000 g = 1 kg
#
# Công thức:
# kg = g / 1000
#
# Ví dụ:
# Nếu g = 2500 thì:
# kg = 2500 / 1000 = 2.5
#
# Ý tưởng:
# - Nhập số gram.
# - Chia số gram cho 1000.
# - In kết quả ra màn hình.

g = float(input("Nhập số gram: "))

kg = g / 1000

print(g, "g =", kg, "kg")
