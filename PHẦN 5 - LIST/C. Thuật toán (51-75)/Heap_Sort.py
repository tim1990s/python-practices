# Chương trình Heap Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list bằng heap.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Luyện các thuật toán phổ biến trên list như sắp xếp, tìm kiếm, chia tách, tổng tiền tố và xử lý dãy con.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc list số nguyên.
# - Đưa list vào min heap.
# - Lấy từng phần tử nhỏ nhất ra khỏi heap.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_list_so_nguyen(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [int(x.strip()) for x in du_lieu.split(",") if x.strip()]

import heapq

danh_sach = doc_list_so_nguyen("Nhập list số nguyên: ")
heapq.heapify(danh_sach)
ket_qua = []
while danh_sach:
    ket_qua.append(heapq.heappop(danh_sach))
print("List sau khi Heap Sort:", ket_qua)
