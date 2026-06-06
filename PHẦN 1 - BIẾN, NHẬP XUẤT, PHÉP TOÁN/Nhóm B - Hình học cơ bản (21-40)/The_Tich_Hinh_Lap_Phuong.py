# Chương trình tính thể tích hình lập phương
#
# Hình lập phương là hình khối có tất cả các cạnh bằng nhau.
#
# Công thức:
# the_tich = canh * canh * canh
#
# Ví dụ:
# Nếu cạnh = 4 thì:
# Thể tích = 4 * 4 * 4 = 64
#
# Ý tưởng:
# - Nhập độ dài cạnh hình lập phương.
# - Kiểm tra cạnh phải lớn hơn 0.
# - Áp dụng công thức tính thể tích.
# - In kết quả ra màn hình.

canh = float(input("Nhập cạnh hình lập phương: "))

if canh <= 0:
    print("Cạnh hình lập phương phải lớn hơn 0")
else:
    the_tich = canh * canh * canh
    print("Thể tích hình lập phương là:", the_tich)
