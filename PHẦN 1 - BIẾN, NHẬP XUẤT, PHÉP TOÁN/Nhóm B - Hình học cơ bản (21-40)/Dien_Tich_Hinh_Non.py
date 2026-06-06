# Chương trình tính diện tích hình nón
#
# Diện tích hình nón trong bài này là diện tích toàn phần.
# Diện tích toàn phần gồm diện tích xung quanh và diện tích đáy.
#
# Công thức:
# duong_sinh = sqrt(ban_kinh * ban_kinh + chieu_cao * chieu_cao)
# dien_tich = pi * ban_kinh * (ban_kinh + duong_sinh)
#
# Ví dụ:
# Nếu bán kính = 3 và chiều cao = 4 thì:
# Đường sinh = sqrt(3 * 3 + 4 * 4) = 5
# Diện tích = pi * 3 * (3 + 5)
#
# Ý tưởng:
# - Nhập bán kính đáy và chiều cao hình nón.
# - Kiểm tra cả hai giá trị phải lớn hơn 0.
# - Tính đường sinh bằng định lý Pythagoras.
# - Áp dụng công thức tính diện tích toàn phần.
# - In kết quả ra màn hình.

import math

ban_kinh = float(input("Nhập bán kính đáy hình nón: "))
chieu_cao = float(input("Nhập chiều cao hình nón: "))

if ban_kinh <= 0 or chieu_cao <= 0:
    print("Bán kính và chiều cao phải lớn hơn 0")
else:
    duong_sinh = math.sqrt(ban_kinh * ban_kinh + chieu_cao * chieu_cao)
    dien_tich = math.pi * ban_kinh * (ban_kinh + duong_sinh)

    print("Đường sinh hình nón là:", duong_sinh)
    print("Diện tích toàn phần hình nón là:", dien_tich)
