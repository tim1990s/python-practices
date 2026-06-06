# Chương trình tính diện tích mặt cầu
#
# Diện tích mặt cầu là diện tích bề mặt bên ngoài của hình cầu.
#
# Công thức:
# dien_tich = 4 * pi * ban_kinh * ban_kinh
#
# Ví dụ:
# Nếu bán kính = 3 thì:
# Diện tích mặt cầu = 4 * pi * 3 * 3
#
# Ý tưởng:
# - Nhập bán kính hình cầu.
# - Kiểm tra bán kính phải lớn hơn 0.
# - Dùng math.pi để lấy giá trị pi.
# - Áp dụng công thức tính diện tích mặt cầu.
# - In kết quả ra màn hình.

import math

ban_kinh = float(input("Nhập bán kính hình cầu: "))

if ban_kinh <= 0:
    print("Bán kính phải lớn hơn 0")
else:
    dien_tich = 4 * math.pi * ban_kinh * ban_kinh
    print("Diện tích mặt cầu là:", dien_tich)
