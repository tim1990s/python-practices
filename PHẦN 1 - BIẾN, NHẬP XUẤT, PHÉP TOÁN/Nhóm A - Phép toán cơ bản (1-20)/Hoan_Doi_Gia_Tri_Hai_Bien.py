# Chương trình hoán đổi giá trị hai biến
#
# Hoán đổi giá trị hai biến nghĩa là đổi giá trị của biến a cho biến b
# và đổi giá trị của biến b cho biến a.
#
# Ví dụ:
# Trước khi hoán đổi:
# a = 5
# b = 9
#
# Sau khi hoán đổi:
# a = 9
# b = 5
#
# Ý tưởng:
# - Nhập giá trị ban đầu của a và b.
# - Dùng cú pháp a, b = b, a để hoán đổi.
# - In giá trị trước và sau khi hoán đổi.

a = input("Nhập giá trị a: ")
b = input("Nhập giá trị b: ")

print("Trước khi hoán đổi:")
print("a =", a)
print("b =", b)

a, b = b, a

print("Sau khi hoán đổi:")
print("a =", a)
print("b =", b)
