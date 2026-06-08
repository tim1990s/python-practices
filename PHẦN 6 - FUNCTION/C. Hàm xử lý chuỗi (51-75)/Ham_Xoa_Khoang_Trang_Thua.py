# Chương trình hàm xóa khoảng trắng thừa
#
# Yêu cầu:
# - Viết hàm xóa khoảng trắng thừa trong chuỗi.
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
# - Tách chuỗi bằng split().
# - Ghép lại bằng một khoảng trắng.
# - Trả về chuỗi đã chuẩn hóa.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def xoa_khoang_trang_thua(chuoi):
    return " ".join(chuoi.split())


chuoi = input("Nhập chuỗi: ")
print("Chuỗi sau xử lý:", xoa_khoang_trang_thua(chuoi))
