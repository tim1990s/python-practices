# Chương trình Plugin Function
#
# Yêu cầu:
# - Viết hệ thống plugin function đơn giản.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện các kỹ thuật hàm nâng cao: đệ quy, decorator, closure, higher-order function, generator, iterator, callback, async và các pattern đơn giản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Lưu plugin trong dict.
# - Đăng ký function theo tên.
# - Gọi plugin dựa trên tên người dùng nhập.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

plugins = {}


def dang_ky_plugin(ten, ham):
    plugins[ten] = ham


def chay_plugin(ten, gia_tri):
    if ten not in plugins:
        return "Không tìm thấy plugin"
    return plugins[ten](gia_tri)


dang_ky_plugin("upper", lambda s: s.upper())
dang_ky_plugin("lower", lambda s: s.lower())
ten_plugin = input("Nhập plugin (upper/lower): ")
chuoi = input("Nhập chuỗi: ")
print("Kết quả:", chay_plugin(ten_plugin, chuoi))
