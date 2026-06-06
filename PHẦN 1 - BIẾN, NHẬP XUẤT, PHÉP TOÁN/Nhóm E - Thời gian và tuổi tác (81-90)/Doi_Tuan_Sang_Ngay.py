# Chương trình đổi tuần sang ngày
#
# 1 tuần = 7 ngày
#
# Công thức:
# ngay = tuan * 7
#
# Ví dụ:
# Nếu tuần = 4 thì:
# ngày = 4 * 7 = 28
#
# Ý tưởng:
# - Nhập số tuần.
# - Nhân số tuần với 7.
# - In kết quả ra màn hình.

tuan = float(input("Nhập số tuần: "))

ngay = tuan * 7

print(tuan, "tuần =", ngay, "ngày")
