# Chương trình Event Handler
#
# Yêu cầu:
# - Viết hệ thống xử lý event đơn giản.
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
# - Lưu danh sách handler theo tên event.
# - Cho phép đăng ký handler.
# - Kích hoạt event để gọi các handler.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

handlers = {}


def dang_ky(event, handler):
    handlers.setdefault(event, []).append(handler)


def kich_hoat(event, data):
    for handler in handlers.get(event, []):
        handler(data)


def chao_mung(data):
    print("Xin chào", data)


dang_ky("user_login", chao_mung)
ten = input("Nhập tên user: ")
kich_hoat("user_login", ten)
