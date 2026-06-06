# Chương trình tính thể tích hình trụ
#
# Hình trụ có hai đáy là hai hình tròn bằng nhau và có chiều cao.
#
# Công thức:
# the_tich = pi * ban_kinh * ban_kinh * chieu_cao
#
# Ví dụ:
# Nếu bán kính = 3 và chiều cao = 5 thì:
# Thể tích = pi * 3 * 3 * 5
#
# Ý tưởng:
# - Nhập bán kính đáy và chiều cao hình trụ.
# - Kiểm tra cả hai giá trị phải lớn hơn 0.
# - Dùng math.pi để lấy giá trị pi.
# - Áp dụng công thức tính thể tích.
# - In kết quả ra màn hình.

import math

ban_kinh = float(input("Nhập bán kính đáy hình trụ: "))
chieu_cao = float(input("Nhập chiều cao hình trụ: "))

if ban_kinh <= 0 or chieu_cao <= 0:
    print("Bán kính và chiều cao phải lớn hơn 0")
else:
    the_tich = math.pi * ban_kinh * ban_kinh * chieu_cao
    print("Thể tích hình trụ là:", the_tich)
