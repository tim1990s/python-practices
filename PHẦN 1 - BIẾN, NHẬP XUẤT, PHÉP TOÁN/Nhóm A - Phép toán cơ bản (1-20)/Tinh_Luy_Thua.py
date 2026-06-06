# Chương trình tính lũy thừa a^b
#
# Lũy thừa a^b là kết quả của việc nhân a với chính nó b lần.
#
# Công thức:
# luy_thua = a ** b
#
# Ví dụ:
# Nếu a = 2 và b = 3 thì:
# Lũy thừa = 2 ** 3 = 8
#
# Ý tưởng:
# - Nhập cơ số a.
# - Nhập số mũ b.
# - Dùng toán tử ** để tính a mũ b.
# - In kết quả ra màn hình.

a = float(input("Nhập cơ số a: "))
b = float(input("Nhập số mũ b: "))

luy_thua = a ** b

print(a, "mũ", b, "là:", luy_thua)
