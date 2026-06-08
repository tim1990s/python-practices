# Chương trình Retry Decorator
#
# Yêu cầu:
# - Viết decorator retry khi hàm bị lỗi.
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
# - Decorator nhận số lần thử.
# - Wrapper bắt exception.
# - Thử lại cho đến khi thành công hoặc hết lượt.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def retry(so_lan):
    def decorator(func):
        def wrapper(*args, **kwargs):
            loi_cuoi = None
            for _ in range(so_lan):
                try:
                    return func(*args, **kwargs)
                except Exception as loi:
                    loi_cuoi = loi
            raise loi_cuoi
        return wrapper
    return decorator


@retry(3)
def chia(a, b):
    return a / b


a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
try:
    print("Kết quả:", chia(a, b))
except Exception as loi:
    print("Thất bại sau khi retry:", loi)
