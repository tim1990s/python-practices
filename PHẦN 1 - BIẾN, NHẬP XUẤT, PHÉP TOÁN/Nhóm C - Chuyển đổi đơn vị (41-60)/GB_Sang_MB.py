# Chương trình đổi GB sang MB
#
# Trong bài này dùng quy ước:
# 1 GB = 1024 MB
#
# Công thức:
# mb = gb * 1024
#
# Ví dụ:
# Nếu GB = 2 thì:
# MB = 2 * 1024 = 2048
#
# Ý tưởng:
# - Nhập số GB.
# - Nhân số GB với 1024.
# - In kết quả ra màn hình.

gb = float(input("Nhập số GB: "))

mb = gb * 1024

print(gb, "GB =", mb, "MB")
