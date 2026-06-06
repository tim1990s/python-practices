# Chương trình nhập 2 số và tính hiệu
#
# Hiệu của hai số là kết quả nhận được khi lấy số thứ nhất trừ số thứ hai.
#
# Công thức:
# hieu = a - b
#
# Ví dụ:
# Nếu a = 10 và b = 4 thì:
# Hiệu = 10 - 4 = 6
#
# Ý tưởng:
# - Nhập số thứ nhất là a.
# - Nhập số thứ hai là b.
# - Lấy a trừ b để tính hiệu.
# - In kết quả ra màn hình.

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

hieu = a - b

print("Hiệu của", a, "và", b, "là:", hieu)
