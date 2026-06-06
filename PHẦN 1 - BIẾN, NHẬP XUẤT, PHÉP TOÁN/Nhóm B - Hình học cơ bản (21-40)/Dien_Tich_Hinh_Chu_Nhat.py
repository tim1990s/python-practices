# Chương trình tính diện tích hình chữ nhật
#
# Diện tích hình chữ nhật cho biết phần mặt phẳng nằm bên trong hình.
#
# Công thức:
# dien_tich = chieu_dai * chieu_rong
#
# Ví dụ:
# Nếu chiều dài = 8 và chiều rộng = 5 thì:
# Diện tích = 8 * 5 = 40
#
# Ý tưởng:
# - Nhập chiều dài và chiều rộng.
# - Kiểm tra cả hai giá trị phải lớn hơn 0.
# - Áp dụng công thức tính diện tích.
# - In kết quả ra màn hình.

chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))

if chieu_dai <= 0 or chieu_rong <= 0:
    print("Chiều dài và chiều rộng phải lớn hơn 0")
else:
    dien_tich = chieu_dai * chieu_rong
    print("Diện tích hình chữ nhật là:", dien_tich)
