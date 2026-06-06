# Chương trình tính phần trăm chiết khấu
#
# Phần trăm chiết khấu cho biết tiền giảm chiếm bao nhiêu phần trăm giá gốc.
#
# Công thức:
# phan_tram_chiet_khau = tien_chiet_khau / gia_goc * 100
#
# Ý tưởng:
# - Nhập giá gốc và tiền chiết khấu.
# - Kiểm tra giá gốc phải lớn hơn 0.
# - Tính phần trăm chiết khấu.

gia_goc = float(input("Nhập giá gốc: "))
tien_chiet_khau = float(input("Nhập số tiền chiết khấu: "))

if gia_goc <= 0:
    print("Giá gốc phải lớn hơn 0")
else:
    phan_tram_chiet_khau = tien_chiet_khau / gia_goc * 100
    print("Phần trăm chiết khấu là:", phan_tram_chiet_khau, "%")
