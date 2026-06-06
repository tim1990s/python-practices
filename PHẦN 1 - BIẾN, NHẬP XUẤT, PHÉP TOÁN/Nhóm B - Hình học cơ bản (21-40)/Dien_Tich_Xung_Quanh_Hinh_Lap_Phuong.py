# Chương trình tính diện tích xung quanh hình lập phương
#
# Diện tích xung quanh hình lập phương là tổng diện tích 4 mặt bên.
#
# Công thức:
# dien_tich_xung_quanh = 4 * canh * canh
#
# Ví dụ:
# Nếu cạnh = 5 thì:
# Diện tích xung quanh = 4 * 5 * 5 = 100
#
# Ý tưởng:
# - Nhập độ dài cạnh hình lập phương.
# - Kiểm tra cạnh phải lớn hơn 0.
# - Áp dụng công thức tính diện tích xung quanh.
# - In kết quả ra màn hình.

canh = float(input("Nhập cạnh hình lập phương: "))

if canh <= 0:
    print("Cạnh hình lập phương phải lớn hơn 0")
else:
    dien_tich_xung_quanh = 4 * canh * canh
    print("Diện tích xung quanh hình lập phương là:", dien_tich_xung_quanh)
