# Chương trình tính đường chéo hình vuông
#
# Đường chéo hình vuông là đoạn thẳng nối hai đỉnh đối diện.
#
# Công thức:
# duong_cheo = canh * sqrt(2)
#
# Ví dụ:
# Nếu cạnh = 5 thì:
# Đường chéo = 5 * sqrt(2)
#
# Ý tưởng:
# - Nhập độ dài cạnh hình vuông.
# - Kiểm tra cạnh phải lớn hơn 0.
# - Dùng math.sqrt(2) để tính căn bậc hai của 2.
# - Áp dụng công thức tính đường chéo.
# - In kết quả ra màn hình.

import math

canh = float(input("Nhập cạnh hình vuông: "))

if canh <= 0:
    print("Cạnh hình vuông phải lớn hơn 0")
else:
    duong_cheo = canh * math.sqrt(2)
    print("Đường chéo hình vuông là:", duong_cheo)
