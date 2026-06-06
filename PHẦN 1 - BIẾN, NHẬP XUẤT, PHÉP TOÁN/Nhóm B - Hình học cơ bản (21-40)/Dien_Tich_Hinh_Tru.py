# Chương trình tính diện tích hình trụ
#
# Diện tích hình trụ trong bài này là diện tích toàn phần.
# Diện tích toàn phần gồm diện tích xung quanh và diện tích hai đáy.
#
# Công thức:
# dien_tich = 2 * pi * ban_kinh * (ban_kinh + chieu_cao)
#
# Ví dụ:
# Nếu bán kính = 3 và chiều cao = 5 thì:
# Diện tích = 2 * pi * 3 * (3 + 5)
#
# Ý tưởng:
# - Nhập bán kính đáy và chiều cao hình trụ.
# - Kiểm tra cả hai giá trị phải lớn hơn 0.
# - Dùng math.pi để lấy giá trị pi.
# - Áp dụng công thức tính diện tích toàn phần.
# - In kết quả ra màn hình.

import math

ban_kinh = float(input("Nhập bán kính đáy hình trụ: "))
chieu_cao = float(input("Nhập chiều cao hình trụ: "))

if ban_kinh <= 0 or chieu_cao <= 0:
    print("Bán kính và chiều cao phải lớn hơn 0")
else:
    dien_tich = 2 * math.pi * ban_kinh * (ban_kinh + chieu_cao)
    print("Diện tích toàn phần hình trụ là:", dien_tich)
