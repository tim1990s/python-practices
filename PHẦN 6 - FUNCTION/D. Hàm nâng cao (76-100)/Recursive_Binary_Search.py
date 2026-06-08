# Chương trình Recursive Binary Search
#
# Yêu cầu:
# - Viết hàm tìm kiếm nhị phân bằng đệ quy.
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
# - Nhận list đã sắp xếp và giá trị cần tìm.
# - So sánh với phần tử giữa.
# - Gọi đệ quy trên nửa trái hoặc nửa phải.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def binary_search(a, x, trai=0, phai=None):
    if phai is None:
        phai = len(a) - 1
    if trai > phai:
        return -1
    giua = (trai + phai) // 2
    if a[giua] == x:
        return giua
    if a[giua] < x:
        return binary_search(a, x, giua + 1, phai)
    return binary_search(a, x, trai, giua - 1)


a = [int(x.strip()) for x in input("Nhập list tăng dần: ").split(",") if x.strip()]
x = int(input("Nhập giá trị cần tìm: "))
print("Vị trí:", binary_search(a, x))
