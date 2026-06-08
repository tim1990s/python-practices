# Chương trình parse log bằng regex
#
# Yêu cầu:
# - Viết chương trình parse log bằng regex.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Sử dụng regular expression hoặc parser chuẩn để kiểm tra, tìm kiếm, trích xuất hoặc phân tích chuỗi có cấu trúc.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc chuỗi hoặc văn bản đầu vào.
# - Xây dựng mẫu regex hoặc dùng parser phù hợp với định dạng dữ liệu.
# - In kết quả hợp lệ, không hợp lệ hoặc dữ liệu đã parse.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re
log = input("Nhập log dạng [YYYY-MM-DD HH:MM:SS] LEVEL message: ")
mau = r"^\[(?P<thoi_gian>[^\]]+)\]\s+(?P<muc_do>[A-Z]+)\s+(?P<noi_dung>.+)$"
match = re.fullmatch(mau, log)
if not match:
    print("Log không đúng định dạng")
else:
    print("Thời gian:", match.group("thoi_gian"))
    print("Mức độ:", match.group("muc_do"))
    print("Nội dung:", match.group("noi_dung"))
