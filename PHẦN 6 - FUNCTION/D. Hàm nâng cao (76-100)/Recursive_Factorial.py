# Chương trình Recursive Factorial
#
# Yêu cầu:
# - Viết hàm đệ quy tính giai thừa.
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
# - Xác định điều kiện dừng n bằng 0 hoặc 1.
# - Gọi lại hàm với n - 1.
# - Nhân n với kết quả đệ quy.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def giai_thua(n):
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * giai_thua(n - 1)


n = int(input("Nhập n: "))
print("Giai thừa:", giai_thua(n))
