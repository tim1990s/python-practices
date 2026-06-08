# Chương trình Callback
#
# Yêu cầu:
# - Viết hàm dùng callback để xử lý kết quả.
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
# - Tạo hàm chính nhận callback.
# - Tính kết quả trong hàm chính.
# - Gọi callback với kết quả đó.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def xu_ly(a, b, callback):
    ket_qua = a + b
    callback(ket_qua)


def in_ket_qua(ket_qua):
    print("Kết quả callback:", ket_qua)


a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
xu_ly(a, b, in_ket_qua)
