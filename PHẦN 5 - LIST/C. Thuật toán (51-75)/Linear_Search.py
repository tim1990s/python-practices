# Chương trình Linear Search
#
# Yêu cầu:
# - Viết chương trình tìm kiếm tuyến tính trong list.
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
# - Duyệt từng phần tử.
# - So sánh từng phần tử với giá trị cần tìm.

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

danh_sach = doc_list_so_nguyen("Nhập list số nguyên: ")
x = int(input("Nhập giá trị cần tìm: "))
vi_tri = -1
for i, gia_tri in enumerate(danh_sach):
    if gia_tri == x:
        vi_tri = i
        break
print("Không tìm thấy" if vi_tri == -1 else "Tìm thấy tại vị trí: " + str(vi_tri))
