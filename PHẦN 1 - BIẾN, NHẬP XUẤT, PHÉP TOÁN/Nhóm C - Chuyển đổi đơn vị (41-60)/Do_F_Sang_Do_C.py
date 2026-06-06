# Chương trình đổi độ F sang độ C
#
# Độ F và độ C là hai đơn vị đo nhiệt độ.
#
# Công thức:
# do_c = (do_f - 32) * 5 / 9
#
# Ví dụ:
# Nếu độ F = 32 thì:
# độ C = (32 - 32) * 5 / 9 = 0
#
# Ý tưởng:
# - Nhập nhiệt độ theo độ F.
# - Áp dụng công thức đổi sang độ C.
# - In kết quả ra màn hình.

do_f = float(input("Nhập nhiệt độ F: "))

do_c = (do_f - 32) * 5 / 9

print(do_f, "độ F =", do_c, "độ C")
