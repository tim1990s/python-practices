# Chương trình hàm tần suất từ
#
# Yêu cầu:
# - Viết hàm thống kê tần suất từ trong chuỗi.
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
# - Tách văn bản thành các từ.
# - Chuyển về chữ thường.
# - Dùng Counter để đếm tần suất.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re
from collections import Counter


def tan_suat_tu(chuoi):
    tu = re.findall(r"[^\W\d_]+", chuoi.lower(), flags=re.UNICODE)
    return dict(Counter(tu))


chuoi = input("Nhập chuỗi: ")
print("Tần suất từ:", tan_suat_tu(chuoi))
