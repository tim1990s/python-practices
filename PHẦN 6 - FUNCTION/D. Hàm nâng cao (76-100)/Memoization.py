# Chương trình Memoization
#
# Yêu cầu:
# - Viết hàm Fibonacci dùng memoization.
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
# - Dùng dict làm cache.
# - Nếu n đã có trong cache thì trả về ngay.
# - Nếu chưa có thì tính và lưu lại.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def fibonacci(n, cache={0: 0, 1: 1}):
    if n < 0:
        return None
    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]


n = int(input("Nhập n: "))
print("Fibonacci:", fibonacci(n))
