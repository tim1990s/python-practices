# Chương trình tính hoa hồng bán hàng
#
# Hoa hồng bán hàng là tiền thưởng dựa trên doanh số bán hàng.
#
# Công thức:
# hoa_hong = doanh_so * ti_le_hoa_hong / 100
#
# Ý tưởng:
# - Nhập doanh số bán hàng.
# - Nhập tỷ lệ hoa hồng.
# - Tính tiền hoa hồng.

doanh_so = float(input("Nhập doanh số bán hàng: "))
ti_le_hoa_hong = float(input("Nhập tỷ lệ hoa hồng (%): "))

hoa_hong = doanh_so * ti_le_hoa_hong / 100

print("Tiền hoa hồng là:", hoa_hong)
