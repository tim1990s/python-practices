# Chương trình Markdown parser đơn giản
#
# Yêu cầu:
# - Viết chương trình markdown parser đơn giản.
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
markdown = input("Nhập một dòng Markdown: ")
html = markdown
if re.fullmatch(r"#{1,6}\s+.+", markdown):
    cap = len(markdown) - len(markdown.lstrip("#"))
    noi_dung = markdown[cap:].strip()
    html = f"<h{cap}>" + noi_dung + f"</h{cap}>"
else:
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html)
    html = re.sub(r"\[(.+?)\]\((.+?)\)", r"<a href='\2'>\1</a>", html)
print("HTML:", html)
