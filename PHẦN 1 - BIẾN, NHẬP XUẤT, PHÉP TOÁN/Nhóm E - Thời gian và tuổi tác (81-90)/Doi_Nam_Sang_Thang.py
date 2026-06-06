# Chương trình đổi năm sang tháng
#
# 1 năm = 12 tháng
#
# Công thức:
# thang = nam * 12
#
# Ví dụ:
# Nếu năm = 2 thì:
# tháng = 2 * 12 = 24
#
# Ý tưởng:
# - Nhập số năm.
# - Nhân số năm với 12.
# - In kết quả ra màn hình.

nam = float(input("Nhập số năm: "))

thang = nam * 12

print(nam, "năm =", thang, "tháng")
