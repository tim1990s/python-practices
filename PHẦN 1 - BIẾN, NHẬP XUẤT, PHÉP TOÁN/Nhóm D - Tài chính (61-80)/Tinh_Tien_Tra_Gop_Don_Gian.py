# Chương trình tính tiền trả góp đơn giản
#
# Bài này chia đều tổng số tiền phải trả cho số tháng trả góp.
#
# Công thức:
# tien_lai = tien_vay * lai_suat * so_thang / 100
# tong_phai_tra = tien_vay + tien_lai
# tien_moi_thang = tong_phai_tra / so_thang
#
# Ý tưởng:
# - Nhập số tiền vay, lãi suất mỗi tháng và số tháng.
# - Tính tổng tiền lãi.
# - Chia tổng tiền phải trả cho số tháng.

tien_vay = float(input("Nhập số tiền vay: "))
lai_suat_thang = float(input("Nhập lãi suất mỗi tháng (%): "))
so_thang = int(input("Nhập số tháng trả góp: "))

if so_thang <= 0:
    print("Số tháng trả góp phải lớn hơn 0")
else:
    tien_lai = tien_vay * lai_suat_thang * so_thang / 100
    tong_phai_tra = tien_vay + tien_lai
    tien_moi_thang = tong_phai_tra / so_thang

    print("Tổng tiền phải trả là:", tong_phai_tra)
    print("Tiền phải trả mỗi tháng là:", tien_moi_thang)
