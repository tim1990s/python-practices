# Chương trình template engine đơn giản
#
# Yêu cầu:
# - Viết chương trình template engine đơn giản.
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
template = input("Nhập template, ví dụ: Xin chào {{ name }}: ")
raw_data = input("Nhập dữ liệu dạng key=value, cách nhau bởi dấu phẩy: ")
data = {}
for item in raw_data.split(","):
    if "=" in item:
        key, value = item.split("=", 1)
        data[key.strip()] = value.strip()
def thay_the(match):
    key = match.group(1).strip()
    return data.get(key, match.group(0))
ket_qua = re.sub(r"\{\{\s*(.*?)\s*\}\}", thay_the, template)
print("Kết quả:", ket_qua)
