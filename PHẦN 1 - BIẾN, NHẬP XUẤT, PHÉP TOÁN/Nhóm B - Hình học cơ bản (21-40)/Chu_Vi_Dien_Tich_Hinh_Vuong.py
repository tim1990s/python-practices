# Chương trình tính chu vi và diện tích hình vuông
#
# Hình vuông là hình có 4 cạnh bằng nhau.
#
# Nếu biết độ dài một cạnh của hình vuông, ta có thể tính:
# - Chu vi hình vuông.
# - Diện tích hình vuông.
#
# Công thức:
# chu_vi = canh * 4
# dien_tich = canh * canh
#
# Ví dụ:
# Nếu cạnh hình vuông là 5 thì:
# Chu vi = 5 * 4 = 20
# Diện tích = 5 * 5 = 25
#
# Nếu cạnh hình vuông là 3.5 thì:
# Chu vi = 3.5 * 4 = 14
# Diện tích = 3.5 * 3.5 = 12.25
#
# Ý tưởng:
# - Nhập độ dài cạnh hình vuông.
# - Kiểm tra cạnh có lớn hơn 0 hay không.
# - Nếu cạnh không lớn hơn 0 thì báo lỗi.
# - Nếu cạnh hợp lệ thì tính chu vi bằng cạnh nhân 4.
# - Tính diện tích bằng cạnh nhân cạnh.
# - In kết quả ra màn hình.

canh = float(input("Nhập độ dài cạnh hình vuông: "))

if canh <= 0:
    print("Độ dài cạnh hình vuông phải lớn hơn 0")
else:
    chu_vi = canh * 4
    dien_tich = canh * canh

    print("Chu vi hình vuông là:", chu_vi)
    print("Diện tích hình vuông là:", dien_tich)
