# Chương trình tính tiền nước đơn giản
#
# Bài này tính tiền nước theo một đơn giá cố định.
#
# Công thức:
# tien_nuoc = so_m3 * don_gia
#
# Ý tưởng:
# - Nhập số mét khối nước đã dùng.
# - Nhập đơn giá cho mỗi mét khối.
# - Nhân số mét khối với đơn giá.

so_m3 = float(input("Nhập số m3 nước đã dùng: "))
don_gia = float(input("Nhập đơn giá mỗi m3: "))

tien_nuoc = so_m3 * don_gia

print("Tiền nước phải trả là:", tien_nuoc)
