# Chương trình Generator
#
# Yêu cầu:
# - Viết generator sinh dãy số chẵn.
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
# - Dùng yield để sinh từng giá trị.
# - Không tạo toàn bộ list ngay từ đầu.
# - Duyệt generator bằng list().

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def sinh_so_chan(n):
    for i in range(0, n + 1, 2):
        yield i


n = int(input("Nhập n: "))
print("Các số chẵn:", list(sinh_so_chan(n)))
