# Chương trình Strategy Pattern
#
# Yêu cầu:
# - Viết ví dụ Strategy Pattern đơn giản.
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
# - Tạo nhiều hàm chiến lược.
# - Chọn chiến lược theo input.
# - Gọi chiến lược đã chọn để tính kết quả.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def cong(a, b):
    return a + b


def nhan(a, b):
    return a * b


strategies = {"cong": cong, "nhan": nhan}
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
ten = input("Nhập strategy (cong/nhan): ")
ham = strategies.get(ten)
print("Kết quả:", ham(a, b) if ham else "Strategy không hợp lệ")
