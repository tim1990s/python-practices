# Chương trình tính tuổi từ năm sinh
#
# Tuổi có thể tính bằng cách lấy năm hiện tại trừ đi năm sinh.
#
# Công thức:
# tuoi = nam_hien_tai - nam_sinh
#
# Ví dụ:
# Nếu năm hiện tại = 2026 và năm sinh = 2000 thì:
# Tuổi = 2026 - 2000 = 26
#
# Ý tưởng:
# - Nhập năm sinh.
# - Nhập năm hiện tại.
# - Kiểm tra năm hiện tại không được nhỏ hơn năm sinh.
# - Tính tuổi và in kết quả ra màn hình.

nam_sinh = int(input("Nhập năm sinh: "))
nam_hien_tai = int(input("Nhập năm hiện tại: "))

if nam_hien_tai < nam_sinh:
    print("Năm hiện tại không được nhỏ hơn năm sinh")
else:
    tuoi = nam_hien_tai - nam_sinh
    print("Tuổi của bạn là:", tuoi)
