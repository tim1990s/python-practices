# Chương trình Function Composition
#
# Yêu cầu:
# - Viết hàm kết hợp nhiều function.
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
# - Tạo hàm compose nhận nhiều hàm.
# - Áp dụng các hàm theo thứ tự phải sang trái.
# - Trả về kết quả cuối cùng.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def compose(*functions):
    def inner(value):
        for func in reversed(functions):
            value = func(value)
        return value
    return inner


def gap_doi(x):
    return x * 2


def cong_mot(x):
    return x + 1


x = float(input("Nhập x: "))
ham = compose(gap_doi, cong_mot)
print("Kết quả compose:", ham(x))
