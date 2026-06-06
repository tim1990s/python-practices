# Chương trình nhập 2 số và tính thương
#
# Thương của hai số là kết quả nhận được khi lấy số thứ nhất chia cho số thứ hai.
#
# Công thức:
# thuong = a / b
#
# Ví dụ:
# Nếu a = 10 và b = 2 thì:
# Thương = 10 / 2 = 5
#
# Lưu ý:
# - Với phép chia a / b, b là số chia.
# - Số chia không được bằng 0.
#
# Ý tưởng:
# - Nhập số thứ nhất là a.
# - Nhập số thứ hai là b.
# - Nếu b bằng 0 thì báo lỗi.
# - Nếu b khác 0 thì tính thương.
# - In kết quả ra màn hình.

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

if b == 0:
    print("Không thể chia vì số chia b không được bằng 0")
else:
    thuong = a / b
    print("Thương của", a, "và", b, "là:", thuong)
