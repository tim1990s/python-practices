# Chương trình hàm chuẩn hóa tên
#
# Yêu cầu:
# - Viết hàm chuẩn hóa họ tên.
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
# - Xóa khoảng trắng thừa.
# - Chuyển toàn bộ về chữ thường.
# - Viết hoa chữ cái đầu mỗi từ.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def chuan_hoa_ten(ten):
    return " ".join(tu.capitalize() for tu in ten.strip().lower().split())


ten = input("Nhập họ tên: ")
print("Tên sau khi chuẩn hóa:", chuan_hoa_ten(ten))
