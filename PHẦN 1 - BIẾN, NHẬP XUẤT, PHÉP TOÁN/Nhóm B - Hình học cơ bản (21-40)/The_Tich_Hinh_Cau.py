# Chương trình tính thể tích hình cầu
#
# Hình cầu là hình khối tròn đều trong không gian.
#
# Công thức:
# the_tich = 4 / 3 * pi * ban_kinh * ban_kinh * ban_kinh
#
# Ví dụ:
# Nếu bán kính = 3 thì:
# Thể tích = 4 / 3 * pi * 3 * 3 * 3
#
# Ý tưởng:
# - Nhập bán kính hình cầu.
# - Kiểm tra bán kính phải lớn hơn 0.
# - Dùng math.pi để lấy giá trị pi.
# - Áp dụng công thức tính thể tích.
# - In kết quả ra màn hình.

import math

ban_kinh = float(input("Nhập bán kính hình cầu: "))

if ban_kinh <= 0:
    print("Bán kính phải lớn hơn 0")
else:
    the_tich = 4 / 3 * math.pi * ban_kinh * ban_kinh * ban_kinh
    print("Thể tích hình cầu là:", the_tich)
