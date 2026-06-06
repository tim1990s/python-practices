# Chương trình tính đường chéo hình chữ nhật
#
# Đường chéo hình chữ nhật là đoạn thẳng nối hai đỉnh đối diện.
#
# Công thức:
# duong_cheo = sqrt(chieu_dai * chieu_dai + chieu_rong * chieu_rong)
#
# Ví dụ:
# Nếu chiều dài = 4 và chiều rộng = 3 thì:
# Đường chéo = sqrt(4 * 4 + 3 * 3) = 5
#
# Ý tưởng:
# - Nhập chiều dài và chiều rộng.
# - Kiểm tra cả hai giá trị phải lớn hơn 0.
# - Dùng định lý Pythagoras để tính đường chéo.
# - In kết quả ra màn hình.

import math

chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))

if chieu_dai <= 0 or chieu_rong <= 0:
    print("Chiều dài và chiều rộng phải lớn hơn 0")
else:
    duong_cheo = math.sqrt(chieu_dai * chieu_dai + chieu_rong * chieu_rong)
    print("Đường chéo hình chữ nhật là:", duong_cheo)
