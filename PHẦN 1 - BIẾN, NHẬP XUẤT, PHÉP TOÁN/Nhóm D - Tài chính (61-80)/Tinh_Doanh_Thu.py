# Chương trình tính doanh thu
#
# Doanh thu là tổng số tiền thu được từ việc bán hàng.
#
# Công thức:
# doanh_thu = so_luong * don_gia
#
# Ý tưởng:
# - Nhập số lượng sản phẩm bán được.
# - Nhập đơn giá mỗi sản phẩm.
# - Nhân số lượng với đơn giá.

so_luong = int(input("Nhập số lượng sản phẩm bán được: "))
don_gia = float(input("Nhập đơn giá: "))

doanh_thu = so_luong * don_gia

print("Doanh thu là:", doanh_thu)
