# Chương trình kiểm tra IPv6 bằng regex
#
# Yêu cầu:
# - Viết chương trình kiểm tra IPv6 bằng regex.
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
ip = input("Nhập địa chỉ IPv6: ")
mau_day_du = r"^(?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$"
mau_rut_gon = r"^((?:[0-9A-Fa-f]{1,4}:){0,7}:)(?:[0-9A-Fa-f]{1,4}:?){0,7}$"
print("IPv6 hợp lệ" if re.fullmatch(mau_day_du, ip) or re.fullmatch(mau_rut_gon, ip) else "IPv6 không hợp lệ")
