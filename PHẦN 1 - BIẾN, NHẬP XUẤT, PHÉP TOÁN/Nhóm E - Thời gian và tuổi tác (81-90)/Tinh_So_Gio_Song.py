# Chương trình tính số giờ sống
#
# Bài này tính gần đúng số giờ sống dựa trên số tuổi.
#
# Quy ước:
# 1 năm = 365 ngày
# 1 ngày = 24 giờ
#
# Công thức:
# so_gio_song = tuoi * 365 * 24
#
# Ý tưởng:
# - Nhập số tuổi.
# - Kiểm tra tuổi không được âm.
# - Nhân tuổi với 365 rồi nhân với 24.

tuoi = float(input("Nhập số tuổi: "))

if tuoi < 0:
    print("Tuổi không được âm")
else:
    so_gio_song = tuoi * 365 * 24
    print("Số giờ sống gần đúng là:", so_gio_song)
