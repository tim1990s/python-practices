# Chương trình hàm đổi giây sang giờ phút giây
#
# Yêu cầu:
# - Viết hàm đổi tổng số giây thành giờ, phút và giây.
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
# - Định nghĩa hàm nhận tổng số giây.
# - Dùng chia nguyên và chia dư.
# - Trả về bộ ba giờ, phút, giây.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def doi_giay(tong_giay):
    gio = tong_giay // 3600
    phan_du = tong_giay % 3600
    phut = phan_du // 60
    giay = phan_du % 60
    return gio, phut, giay


tong_giay = int(input("Nhập tổng số giây: "))
gio, phut, giay = doi_giay(tong_giay)
print(f"{gio} giờ {phut} phút {giay} giây")
