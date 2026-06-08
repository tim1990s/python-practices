# Chương trình hàm so sánh không phân biệt hoa thường
#
# Yêu cầu:
# - Viết hàm so sánh hai chuỗi không phân biệt chữ hoa chữ thường.
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
# - Nhận hai chuỗi.
# - Dùng casefold() để chuẩn hóa.
# - So sánh kết quả chuẩn hóa.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def so_sanh_khong_phan_biet_hoa_thuong(a, b):
    return a.casefold() == b.casefold()


a = input("Nhập chuỗi thứ nhất: ")
b = input("Nhập chuỗi thứ hai: ")
print("Hai chuỗi bằng nhau:", so_sanh_khong_phan_biet_hoa_thuong(a, b))
