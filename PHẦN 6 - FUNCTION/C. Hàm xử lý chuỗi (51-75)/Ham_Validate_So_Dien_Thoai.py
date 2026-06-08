# Chương trình hàm validate số điện thoại
#
# Yêu cầu:
# - Viết hàm kiểm tra số điện thoại Việt Nam cơ bản.
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
# - Xóa khoảng trắng.
# - Dùng regex kiểm tra số bắt đầu bằng 0.
# - Yêu cầu tổng cộng 10 chữ số.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re


def validate_so_dien_thoai(sdt):
    sdt = sdt.replace(" ", "")
    return re.fullmatch(r"0\d{9}", sdt) is not None


sdt = input("Nhập số điện thoại: ")
print("Số điện thoại hợp lệ:", validate_so_dien_thoai(sdt))
