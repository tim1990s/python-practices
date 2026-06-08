# Chương trình parse email header
#
# Yêu cầu:
# - Viết chương trình parse email header.
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

from email.parser import Parser
print("Nhập email header, nhập dòng rỗng để kết thúc:")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
headers = Parser().parsestr("\n".join(lines))
if not headers.items():
    print("Không có header")
else:
    print("Các email header:")
    for key, value in headers.items():
        print(key + ":", value)
