# Chương trình Coroutine
#
# Yêu cầu:
# - Viết coroutine nhận dữ liệu bằng send().
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
# - Tạo generator coroutine.
# - Dùng yield để chờ dữ liệu gửi vào.
# - Dùng send() để truyền dữ liệu cho coroutine.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def bo_dem_tu():
    tong = 0
    while True:
        chuoi = yield tong
        tong += len(chuoi.split())


co = bo_dem_tu()
next(co)
chuoi_1 = input("Nhập câu thứ nhất: ")
print("Tổng từ:", co.send(chuoi_1))
chuoi_2 = input("Nhập câu thứ hai: ")
print("Tổng từ:", co.send(chuoi_2))
