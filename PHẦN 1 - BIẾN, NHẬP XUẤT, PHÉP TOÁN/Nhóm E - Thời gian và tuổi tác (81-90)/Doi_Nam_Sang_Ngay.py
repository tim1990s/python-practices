# Chương trình đổi năm sang ngày
#
# Bài này đổi năm sang ngày theo cách tính gần đúng.
#
# Quy ước:
# 1 năm = 365 ngày
#
# Công thức:
# ngay = nam * 365
#
# Ý tưởng:
# - Nhập số năm.
# - Nhân số năm với 365.
# - In kết quả ra màn hình.

nam = float(input("Nhập số năm: "))

ngay = nam * 365

print(nam, "năm =", ngay, "ngày")
