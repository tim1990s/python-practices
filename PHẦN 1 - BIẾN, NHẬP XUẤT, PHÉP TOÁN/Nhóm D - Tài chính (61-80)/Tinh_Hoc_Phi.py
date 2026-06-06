# Chương trình tính học phí
#
# Học phí có thể tính bằng số tín chỉ nhân với tiền mỗi tín chỉ.
#
# Công thức:
# hoc_phi = so_tin_chi * tien_moi_tin_chi
#
# Ý tưởng:
# - Nhập số tín chỉ.
# - Nhập tiền mỗi tín chỉ.
# - Nhân hai giá trị để tính học phí.

so_tin_chi = int(input("Nhập số tín chỉ: "))
tien_moi_tin_chi = float(input("Nhập tiền mỗi tín chỉ: "))

hoc_phi = so_tin_chi * tien_moi_tin_chi

print("Học phí là:", hoc_phi)
