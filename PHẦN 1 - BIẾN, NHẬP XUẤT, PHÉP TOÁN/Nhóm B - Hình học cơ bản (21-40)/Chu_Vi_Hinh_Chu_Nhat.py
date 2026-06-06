# Chương trình tính chu vi hình chữ nhật
#
# Hình chữ nhật là hình có hai cặp cạnh đối diện bằng nhau.
#
# Công thức:
# chu_vi = (chieu_dai + chieu_rong) * 2
#
# Ví dụ:
# Nếu chiều dài = 8 và chiều rộng = 5 thì:
# Chu vi = (8 + 5) * 2 = 26
#
# Ý tưởng:
# - Nhập chiều dài và chiều rộng.
# - Kiểm tra cả hai giá trị phải lớn hơn 0.
# - Áp dụng công thức tính chu vi.
# - In kết quả ra màn hình.

chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))

if chieu_dai <= 0 or chieu_rong <= 0:
    print("Chiều dài và chiều rộng phải lớn hơn 0")
else:
    chu_vi = (chieu_dai + chieu_rong) * 2
    print("Chu vi hình chữ nhật là:", chu_vi)
