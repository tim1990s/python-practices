# Chương trình đổi MB sang GB
#
# Trong bài này dùng quy ước:
# 1024 MB = 1 GB
#
# Công thức:
# gb = mb / 1024
#
# Ví dụ:
# Nếu MB = 2048 thì:
# GB = 2048 / 1024 = 2
#
# Ý tưởng:
# - Nhập số MB.
# - Chia số MB cho 1024.
# - In kết quả ra màn hình.

mb = float(input("Nhập số MB: "))

gb = mb / 1024

print(mb, "MB =", gb, "GB")
