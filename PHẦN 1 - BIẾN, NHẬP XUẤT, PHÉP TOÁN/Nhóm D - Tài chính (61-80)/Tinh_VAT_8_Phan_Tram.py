# Chương trình tính VAT 8%
#
# VAT là thuế giá trị gia tăng.
#
# Công thức:
# tien_vat = gia_goc * 8 / 100
# gia_sau_vat = gia_goc + tien_vat
#
# Ý tưởng:
# - Nhập giá gốc.
# - Tính tiền VAT 8%.
# - Cộng giá gốc với tiền VAT.

gia_goc = float(input("Nhập giá gốc: "))

tien_vat = gia_goc * 8 / 100
gia_sau_vat = gia_goc + tien_vat

print("Tiền VAT 8% là:", tien_vat)
print("Giá sau VAT là:", gia_sau_vat)
