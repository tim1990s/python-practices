# Chương trình tính thương nguyên
#
# Thương nguyên là phần nguyên của kết quả phép chia.
#
# Công thức:
# thuong_nguyen = a // b
#
# Ví dụ:
# Nếu a = 10 và b = 3 thì:
# 10 chia 3 được thương nguyên là 3
#
# Ý tưởng:
# - Nhập số bị chia là a.
# - Nhập số chia là b.
# - Kiểm tra b có bằng 0 hay không.
# - Nếu b khác 0 thì dùng toán tử // để tính thương nguyên.
# - In kết quả ra màn hình.

a = int(input("Nhập số bị chia a: "))
b = int(input("Nhập số chia b: "))

if b == 0:
    print("Không thể chia vì số chia b không được bằng 0")
else:
    thuong_nguyen = a // b
    print("Thương nguyên của", a, "chia", b, "là:", thuong_nguyen)
