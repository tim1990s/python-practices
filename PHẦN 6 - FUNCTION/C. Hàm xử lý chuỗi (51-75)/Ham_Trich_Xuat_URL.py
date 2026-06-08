# Chương trình hàm trích xuất URL
#
# Yêu cầu:
# - Viết hàm trích xuất URL trong văn bản.
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
# - Đọc văn bản.
# - Dùng regex tìm chuỗi bắt đầu bằng http hoặc https.
# - Trả về list URL.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re


def trich_xuat_url(van_ban):
    return re.findall(r"https?://\S+", van_ban)


van_ban = input("Nhập văn bản: ")
print("URL tìm được:", trich_xuat_url(van_ban))
