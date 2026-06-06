# Chương trình tính phần dư
#
# Phần dư là số còn lại sau khi chia một số cho một số khác.
#
# Công thức:
# phan_du = a % b
#
# Ví dụ:
# Nếu a = 10 và b = 3 thì:
# 10 chia 3 được 3 dư 1
# Phần dư = 10 % 3 = 1
#
# Ý tưởng:
# - Nhập số bị chia là a.
# - Nhập số chia là b.
# - Kiểm tra b có bằng 0 hay không.
# - Nếu b khác 0 thì dùng toán tử % để tính phần dư.
# - In kết quả ra màn hình.

a = int(input("Nhập số bị chia a: "))
b = int(input("Nhập số chia b: "))

if b == 0:
    print("Không thể chia vì số chia b không được bằng 0")
else:
    phan_du = a % b
    print("Phần dư của", a, "chia", b, "là:", phan_du)
