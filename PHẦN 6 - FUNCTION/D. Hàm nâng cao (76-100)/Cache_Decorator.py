# Chương trình Cache Decorator
#
# Yêu cầu:
# - Viết decorator cache kết quả hàm.
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
# - Dùng dict để lưu kết quả theo tham số.
# - Nếu tham số đã có trong cache thì trả về ngay.
# - Nếu chưa có thì gọi hàm gốc và lưu kết quả.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def cache(func):
    bo_nho = {}

    def wrapper(n):
        if n not in bo_nho:
            bo_nho[n] = func(n)
        return bo_nho[n]
    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Nhập n: "))
print("Fibonacci:", fibonacci(n))
