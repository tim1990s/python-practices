# Chương trình tính tỷ suất lợi nhuận
#
# Tỷ suất lợi nhuận cho biết lợi nhuận chiếm bao nhiêu phần trăm doanh thu.
#
# Công thức:
# ty_suat = loi_nhuan / doanh_thu * 100
#
# Ý tưởng:
# - Nhập doanh thu và lợi nhuận.
# - Kiểm tra doanh thu phải lớn hơn 0.
# - Tính tỷ suất lợi nhuận.

doanh_thu = float(input("Nhập doanh thu: "))
loi_nhuan = float(input("Nhập lợi nhuận: "))

if doanh_thu <= 0:
    print("Doanh thu phải lớn hơn 0")
else:
    ty_suat = loi_nhuan / doanh_thu * 100
    print("Tỷ suất lợi nhuận là:", ty_suat, "%")
