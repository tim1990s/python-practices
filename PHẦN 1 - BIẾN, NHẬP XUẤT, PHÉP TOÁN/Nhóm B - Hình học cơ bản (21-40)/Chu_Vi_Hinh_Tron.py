# Chương trình tính chu vi hình tròn
#
# Chu vi hình tròn là độ dài đường bao quanh hình tròn.
#
# Công thức:
# chu_vi = 2 * pi * ban_kinh
#
# Ví dụ:
# Nếu bán kính = 3 thì:
# Chu vi = 2 * pi * 3
#
# Ý tưởng:
# - Nhập bán kính hình tròn.
# - Kiểm tra bán kính phải lớn hơn 0.
# - Dùng math.pi để lấy giá trị pi.
# - Áp dụng công thức tính chu vi.
# - In kết quả ra màn hình.

import math

ban_kinh = float(input("Nhập bán kính hình tròn: "))

if ban_kinh <= 0:
    print("Bán kính phải lớn hơn 0")
else:
    chu_vi = 2 * math.pi * ban_kinh
    print("Chu vi hình tròn là:", chu_vi)
