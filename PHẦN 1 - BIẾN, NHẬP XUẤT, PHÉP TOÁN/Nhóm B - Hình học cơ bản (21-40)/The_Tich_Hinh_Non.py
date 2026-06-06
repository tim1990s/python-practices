# Chương trình tính thể tích hình nón
#
# Hình nón có đáy là hình tròn và có chiều cao.
#
# Công thức:
# the_tich = 1 / 3 * pi * ban_kinh * ban_kinh * chieu_cao
#
# Ví dụ:
# Nếu bán kính = 3 và chiều cao = 6 thì:
# Thể tích = 1 / 3 * pi * 3 * 3 * 6
#
# Ý tưởng:
# - Nhập bán kính đáy và chiều cao hình nón.
# - Kiểm tra cả hai giá trị phải lớn hơn 0.
# - Dùng math.pi để lấy giá trị pi.
# - Áp dụng công thức tính thể tích.
# - In kết quả ra màn hình.

import math

ban_kinh = float(input("Nhập bán kính đáy hình nón: "))
chieu_cao = float(input("Nhập chiều cao hình nón: "))

if ban_kinh <= 0 or chieu_cao <= 0:
    print("Bán kính và chiều cao phải lớn hơn 0")
else:
    the_tich = 1 / 3 * math.pi * ban_kinh * ban_kinh * chieu_cao
    print("Thể tích hình nón là:", the_tich)
