# Chương trình Context Manager
#
# Yêu cầu:
# - Viết context manager đơn giản.
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
# - Tạo class có __enter__ và __exit__.
# - In thông báo khi bắt đầu và kết thúc.
# - Dùng with để chạy khối lệnh.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

class QuanLyTacVu:
    def __enter__(self):
        print("Bắt đầu tác vụ")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Kết thúc tác vụ")
        return False


with QuanLyTacVu():
    noi_dung = input("Nhập nội dung tác vụ: ")
    print("Đang xử lý:", noi_dung)
