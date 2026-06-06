# Chương trình tính diện tích hình tròn
#
# Diện tích hình tròn cho biết phần mặt phẳng nằm bên trong đường tròn.
#
# Công thức:
# dien_tich = pi * ban_kinh * ban_kinh
#
# Ví dụ:
# Nếu bán kính = 3 thì:
# Diện tích = pi * 3 * 3
#
# Ý tưởng:
# - Nhập bán kính hình tròn.
# - Kiểm tra bán kính phải lớn hơn 0.
# - Dùng math.pi để lấy giá trị pi.
# - Áp dụng công thức tính diện tích.
# - In kết quả ra màn hình.

import math

ban_kinh = float(input("Nhập bán kính hình tròn: "))

if ban_kinh <= 0:
    print("Bán kính phải lớn hơn 0")
else:
    dien_tich = math.pi * ban_kinh * ban_kinh
    print("Diện tích hình tròn là:", dien_tich)
