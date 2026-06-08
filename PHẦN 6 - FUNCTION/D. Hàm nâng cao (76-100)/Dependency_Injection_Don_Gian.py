# Chương trình Dependency Injection đơn giản
#
# Yêu cầu:
# - Viết ví dụ truyền dependency vào hàm.
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
# - Tạo hàm nhận một service.
# - Service là hàm xử lý được truyền từ ngoài vào.
# - Giúp hàm chính không phụ thuộc cứng vào implementation.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def gui_thong_bao(noi_dung, sender):
    return sender(noi_dung)


def console_sender(noi_dung):
    return "Đã gửi ra console: " + noi_dung


noi_dung = input("Nhập thông báo: ")
print(gui_thong_bao(noi_dung, console_sender))
