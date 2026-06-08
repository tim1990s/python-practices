# Chương trình parse Markdown đơn giản
#
# Yêu cầu:
# - Viết chương trình parse Markdown đơn giản.
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
line = input("Nhập một dòng Markdown: ")
if re.fullmatch(r"#{1,6}\s+.+", line):
    cap = len(line) - len(line.lstrip("#"))
    print("Heading cấp", cap)
    print("Nội dung:", line[cap:].strip())
elif re.fullmatch(r"[-*+]\s+.+", line):
    print("List item")
    print("Nội dung:", line[2:].strip())
elif re.search(r"\*\*.+?\*\*", line):
    print("Có đoạn bold")
elif re.search(r"\[.+?\]\(.+?\)", line):
    print("Có link Markdown")
else:
    print("Markdown thường hoặc không nhận dạng được")
