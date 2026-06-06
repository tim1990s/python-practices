# Chương trình tính diện tích toàn phần hình hộp chữ nhật
#
# Diện tích toàn phần hình hộp chữ nhật là tổng diện tích của 6 mặt.
#
# Công thức:
# dien_tich_toan_phan = 2 * (dai * rong + dai * cao + rong * cao)
#
# Ví dụ:
# Nếu dài = 6, rộng = 4, cao = 3 thì:
# Diện tích toàn phần = 2 * (6 * 4 + 6 * 3 + 4 * 3) = 108
#
# Ý tưởng:
# - Nhập chiều dài, chiều rộng và chiều cao.
# - Kiểm tra cả ba giá trị phải lớn hơn 0.
# - Áp dụng công thức tính diện tích toàn phần.
# - In kết quả ra màn hình.

chieu_dai = float(input("Nhập chiều dài hình hộp chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng hình hộp chữ nhật: "))
chieu_cao = float(input("Nhập chiều cao hình hộp chữ nhật: "))

if chieu_dai <= 0 or chieu_rong <= 0 or chieu_cao <= 0:
    print("Chiều dài, chiều rộng và chiều cao phải lớn hơn 0")
else:
    dien_tich_toan_phan = 2 * (
        chieu_dai * chieu_rong + chieu_dai * chieu_cao + chieu_rong * chieu_cao
    )
    print("Diện tích toàn phần hình hộp chữ nhật là:", dien_tich_toan_phan)
