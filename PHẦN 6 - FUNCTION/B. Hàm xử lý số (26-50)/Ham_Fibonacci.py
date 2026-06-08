# Chương trình hàm Fibonacci
#
# Yêu cầu:
# - Viết hàm tính số Fibonacci thứ n.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện viết hàm xử lý số nguyên, số thực, chữ số, ước số, bội số, dãy Fibonacci và các bài toán số học cơ bản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - F(0) = 0 và F(1) = 1.
# - Dùng vòng lặp để tính dần.
# - Trả về số Fibonacci thứ n.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def fibonacci(n):
    if n < 0:
        return None
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


n = int(input("Nhập n: "))
ket_qua = fibonacci(n)
print("n không hợp lệ" if ket_qua is None else "Fibonacci:", ket_qua)
