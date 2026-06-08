# Chương trình tạo slug
#
# Yêu cầu:
# - Viết chương trình tạo slug.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Cài đặt thuật toán hoặc kỹ thuật xử lý chuỗi nâng cao để giải quyết bài toán.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc dữ liệu đầu vào theo yêu cầu.
# - Cài đặt thuật toán, cấu trúc dữ liệu hoặc hàm xử lý chuỗi cần thiết.
# - Trả về hoặc in kết quả cuối cùng rõ ràng.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re
import unicodedata
text = input("Nhập chuỗi: ")
khong_dau = unicodedata.normalize("NFD", text)
khong_dau = "".join(ky_tu for ky_tu in khong_dau if unicodedata.category(ky_tu) != "Mn")
khong_dau = khong_dau.lower().replace("đ", "d")
slug = re.sub(r"[^a-z0-9]+", "-", khong_dau).strip("-")
print("Slug:", slug)
