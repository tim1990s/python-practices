# Chương trình BBCode parser đơn giản
#
# Yêu cầu:
# - Viết chương trình bBCode parser đơn giản.
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
bbcode = input("Nhập BBCode: ")
html = bbcode
html = re.sub(r"\[b\](.+?)\[/b\]", r"<strong>\1</strong>", html, flags=re.IGNORECASE)
html = re.sub(r"\[i\](.+?)\[/i\]", r"<em>\1</em>", html, flags=re.IGNORECASE)
html = re.sub(r"\[url=(.+?)\](.+?)\[/url\]", r"<a href='\1'>\2</a>", html, flags=re.IGNORECASE)
print("HTML:", html)
