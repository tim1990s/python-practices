# Chương trình parse SQL SELECT đơn giản
#
# Yêu cầu:
# - Viết chương trình parse SQL SELECT đơn giản.
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
sql = input("Nhập câu SELECT đơn giản: ")
mau = r"^\s*SELECT\s+(?P<cot>.+?)\s+FROM\s+(?P<bang>[A-Za-z_][A-Za-z0-9_]*)(?:\s+WHERE\s+(?P<where>.+))?\s*;?\s*$"
match = re.fullmatch(mau, sql, flags=re.IGNORECASE)
if not match:
    print("Không parse được SQL")
else:
    print("Cột:", match.group("cot"))
    print("Bảng:", match.group("bang"))
    if match.group("where"):
        print("Điều kiện:", match.group("where"))
