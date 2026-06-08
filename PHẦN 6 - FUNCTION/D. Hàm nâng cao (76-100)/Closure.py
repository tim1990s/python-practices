# Chương trình Closure
#
# Yêu cầu:
# - Viết hàm closure tạo bộ nhân.
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
# - Hàm ngoài nhận hệ số.
# - Hàm trong sử dụng hệ số đó.
# - Trả về hàm trong để dùng về sau.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def tao_bo_nhan(he_so):
    def nhan(x):
        return x * he_so
    return nhan


he_so = float(input("Nhập hệ số: "))
x = float(input("Nhập x: "))
bo_nhan = tao_bo_nhan(he_so)
print("Kết quả:", bo_nhan(x))
