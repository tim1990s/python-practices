# Chương trình Iterator
#
# Yêu cầu:
# - Viết iterator tự tạo đếm ngược.
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
# - Tạo class có __iter__.
# - Tạo __next__ để trả từng giá trị.
# - Raise StopIteration khi kết thúc.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

class DemNguoc:
    def __init__(self, bat_dau):
        self.hien_tai = bat_dau

    def __iter__(self):
        return self

    def __next__(self):
        if self.hien_tai < 0:
            raise StopIteration
        gia_tri = self.hien_tai
        self.hien_tai -= 1
        return gia_tri


n = int(input("Nhập n: "))
print("Đếm ngược:", list(DemNguoc(n)))
