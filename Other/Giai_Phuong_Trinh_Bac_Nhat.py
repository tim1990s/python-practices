# Chương trình giải phương trình bậc nhất
#
# Phương trình bậc nhất có dạng:
#     ax + b = 0
#
# Trong đó:
# - a và b là các số thực
# - x là ẩn số cần tìm
#
# Cách giải:
# 1. Nếu a khác 0:
#       x = -b / a
#    => Phương trình có một nghiệm duy nhất.
#
# 2. Nếu a = 0 và b = 0:
#    => Phương trình có vô số nghiệm.
#
# 3. Nếu a = 0 và b khác 0:
#    => Phương trình vô nghiệm.
#
# Ví dụ:
# 2x + 4 = 0
# => x = -4 / 2 = -2
#
# -3x + 9 = 0
# => x = -9 / (-3) = 3

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Nghiệm của phương trình là x =", x)