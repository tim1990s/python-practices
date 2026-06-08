# Chương trình hàm tính giá sau giảm
#
# Yêu cầu:
# - Viết hàm tính giá sau khi áp dụng phần trăm giảm giá.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện cách khai báo hàm, truyền tham số, trả về kết quả bằng return và tách chương trình thành các khối xử lý nhỏ.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Định nghĩa hàm nhận giá gốc và phần trăm giảm.
# - Tính số tiền được giảm.
# - Trả về giá sau giảm.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def gia_sau_giam(gia_goc, phan_tram_giam):
    return gia_goc * (1 - phan_tram_giam / 100)


gia_goc = float(input("Nhập giá gốc: "))
phan_tram_giam = float(input("Nhập phần trăm giảm: "))
print("Giá sau giảm:", gia_sau_giam(gia_goc, phan_tram_giam))
