# Chương trình tính thể tích hình hộp chữ nhật
#
# Hình hộp chữ nhật có ba kích thước: chiều dài, chiều rộng và chiều cao.
#
# Công thức:
# the_tich = chieu_dai * chieu_rong * chieu_cao
#
# Ví dụ:
# Nếu chiều dài = 6, chiều rộng = 4, chiều cao = 3 thì:
# Thể tích = 6 * 4 * 3 = 72
#
# Ý tưởng:
# - Nhập chiều dài, chiều rộng và chiều cao.
# - Kiểm tra cả ba giá trị phải lớn hơn 0.
# - Áp dụng công thức tính thể tích.
# - In kết quả ra màn hình.

chieu_dai = float(input("Nhập chiều dài hình hộp chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng hình hộp chữ nhật: "))
chieu_cao = float(input("Nhập chiều cao hình hộp chữ nhật: "))

if chieu_dai <= 0 or chieu_rong <= 0 or chieu_cao <= 0:
    print("Chiều dài, chiều rộng và chiều cao phải lớn hơn 0")
else:
    the_tich = chieu_dai * chieu_rong * chieu_cao
    print("Thể tích hình hộp chữ nhật là:", the_tich)
