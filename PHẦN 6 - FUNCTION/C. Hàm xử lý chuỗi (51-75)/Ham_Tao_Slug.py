# Chương trình hàm tạo slug
#
# Yêu cầu:
# - Viết hàm tạo slug URL-friendly từ chuỗi.
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
# - Chuẩn hóa Unicode để bỏ dấu.
# - Đưa về chữ thường.
# - Thay nhóm ký tự không phải chữ số/chữ cái bằng dấu gạch ngang.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re
import unicodedata


def tao_slug(chuoi):
    chuoi = unicodedata.normalize("NFD", chuoi)
    chuoi = "".join(ky_tu for ky_tu in chuoi if unicodedata.category(ky_tu) != "Mn")
    chuoi = chuoi.lower()
    chuoi = re.sub(r"[^a-z0-9]+", "-", chuoi)
    return chuoi.strip("-")


chuoi = input("Nhập chuỗi: ")
print("Slug:", tao_slug(chuoi))
