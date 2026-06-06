# Chương trình đổi độ C sang độ F
#
# Độ C và độ F là hai đơn vị đo nhiệt độ.
#
# Công thức:
# do_f = do_c * 9 / 5 + 32
#
# Ví dụ:
# Nếu độ C = 0 thì:
# độ F = 0 * 9 / 5 + 32 = 32
#
# Ý tưởng:
# - Nhập nhiệt độ theo độ C.
# - Áp dụng công thức đổi sang độ F.
# - In kết quả ra màn hình.

do_c = float(input("Nhập nhiệt độ C: "))

do_f = do_c * 9 / 5 + 32

print(do_c, "độ C =", do_f, "độ F")
