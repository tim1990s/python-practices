# Chương trình tính số ngày sống
#
# Bài này tính gần đúng số ngày sống dựa trên số tuổi.
#
# Quy ước:
# 1 năm = 365 ngày
#
# Công thức:
# so_ngay_song = tuoi * 365
#
# Ý tưởng:
# - Nhập số tuổi.
# - Kiểm tra tuổi không được âm.
# - Nhân tuổi với 365 để tính số ngày sống gần đúng.

tuoi = float(input("Nhập số tuổi: "))

if tuoi < 0:
    print("Tuổi không được âm")
else:
    so_ngay_song = tuoi * 365
    print("Số ngày sống gần đúng là:", so_ngay_song)
