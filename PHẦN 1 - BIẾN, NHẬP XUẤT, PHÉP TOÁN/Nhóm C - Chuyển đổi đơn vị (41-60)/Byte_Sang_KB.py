# Chương trình đổi Byte sang KB
#
# Trong bài này dùng quy ước:
# 1024 Byte = 1 KB
#
# Công thức:
# kb = byte / 1024
#
# Ví dụ:
# Nếu Byte = 2048 thì:
# KB = 2048 / 1024 = 2
#
# Ý tưởng:
# - Nhập số Byte.
# - Chia số Byte cho 1024.
# - In kết quả ra màn hình.

byte = float(input("Nhập số Byte: "))

kb = byte / 1024

print(byte, "Byte =", kb, "KB")
