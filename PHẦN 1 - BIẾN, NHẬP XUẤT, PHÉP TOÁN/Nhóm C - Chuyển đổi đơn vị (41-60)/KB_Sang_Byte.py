# Chương trình đổi KB sang Byte
#
# Trong bài này dùng quy ước:
# 1 KB = 1024 Byte
#
# Công thức:
# byte = kb * 1024
#
# Ví dụ:
# Nếu KB = 2 thì:
# Byte = 2 * 1024 = 2048
#
# Ý tưởng:
# - Nhập số KB.
# - Nhân số KB với 1024.
# - In kết quả ra màn hình.

kb = float(input("Nhập số KB: "))

byte = kb * 1024

print(kb, "KB =", byte, "Byte")
