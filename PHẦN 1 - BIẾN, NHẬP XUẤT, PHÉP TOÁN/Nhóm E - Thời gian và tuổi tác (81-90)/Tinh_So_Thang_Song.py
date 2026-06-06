# Chương trình tính số tháng sống
#
# Số tháng sống có thể tính gần đúng từ số tuổi.
#
# Quy ước:
# 1 năm = 12 tháng
#
# Công thức:
# so_thang_song = tuoi * 12
#
# Ý tưởng:
# - Nhập số tuổi.
# - Kiểm tra tuổi không được âm.
# - Nhân tuổi với 12 để tính số tháng sống.

tuoi = float(input("Nhập số tuổi: "))

if tuoi < 0:
    print("Tuổi không được âm")
else:
    so_thang_song = tuoi * 12
    print("Số tháng sống gần đúng là:", so_thang_song)
