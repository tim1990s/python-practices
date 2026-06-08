# Chương trình hàm cắt chuỗi
#
# Yêu cầu:
# - Viết hàm cắt chuỗi theo vị trí bắt đầu và kết thúc.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện viết hàm xử lý chuỗi: đảo chuỗi, chuẩn hóa, validate, parse, tìm kiếm, thống kê và biến đổi văn bản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Nhận chuỗi đầu vào.
# - Nhận vị trí bắt đầu và kết thúc.
# - Dùng slicing để cắt chuỗi.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def cat_chuoi(chuoi, bat_dau, ket_thuc):
    return chuoi[bat_dau:ket_thuc]


chuoi = input("Nhập chuỗi: ")
bat_dau = int(input("Nhập vị trí bắt đầu: "))
ket_thuc = int(input("Nhập vị trí kết thúc: "))
print("Chuỗi sau khi cắt:", cat_chuoi(chuoi, bat_dau, ket_thuc))
