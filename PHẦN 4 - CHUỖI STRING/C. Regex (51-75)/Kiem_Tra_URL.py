# Chương trình kiểm tra URL bằng regex
#
# Yêu cầu:
# - Viết chương trình kiểm tra URL bằng regex.
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
url = input("Nhập URL: ")
mau = r"^(https?://)?([A-Za-z0-9-]+\.)+[A-Za-z]{2,}(:\d+)?(/[\w\-.~:/?#\[\]@!$&'()*+,;=%]*)?$"
print("URL hợp lệ" if re.fullmatch(mau, url) else "URL không hợp lệ")
