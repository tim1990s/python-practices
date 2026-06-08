# Chương trình Decorator
#
# Yêu cầu:
# - Viết decorator đo thời gian chạy hàm.
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
# - Viết hàm decorator nhận một hàm khác.
# - Tạo wrapper để chạy hàm gốc.
# - In thời gian thực thi.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import time


def do_thoi_gian(func):
    def wrapper(*args, **kwargs):
        bat_dau = time.time()
        ket_qua = func(*args, **kwargs)
        print("Thời gian chạy:", round(time.time() - bat_dau, 6), "giây")
        return ket_qua
    return wrapper


@do_thoi_gian
def tinh_tong(n):
    return sum(range(n + 1))


n = int(input("Nhập n: "))
print("Tổng:", tinh_tong(n))
