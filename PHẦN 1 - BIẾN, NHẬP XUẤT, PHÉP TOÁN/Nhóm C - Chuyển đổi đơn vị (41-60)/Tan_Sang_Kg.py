# Chương trình đổi tấn sang kg
#
# 1 tấn = 1000 kg
#
# Công thức:
# kg = tan * 1000
#
# Ví dụ:
# Nếu tấn = 3 thì:
# kg = 3 * 1000 = 3000
#
# Ý tưởng:
# - Nhập số tấn.
# - Nhân số tấn với 1000.
# - In kết quả ra màn hình.

tan = float(input("Nhập số tấn: "))

kg = tan * 1000

print(tan, "tấn =", kg, "kg")
