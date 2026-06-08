# Chương trình Exponential Search
#
# Yêu cầu:
# - Viết chương trình tìm kiếm lũy tiến trong list đã sắp xếp.
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
# - Tăng phạm vi tìm kiếm theo lũy thừa 2.
# - Xác định đoạn có thể chứa giá trị.
# - Binary search trong đoạn đó.

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

def binary_search(a, trai, phai, x):
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            return giua
        if a[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return -1


danh_sach = doc_list_so_nguyen("Nhập list đã sắp xếp tăng dần: ")
x = int(input("Nhập giá trị cần tìm: "))
if not danh_sach:
    vi_tri = -1
elif danh_sach[0] == x:
    vi_tri = 0
else:
    i = 1
    while i < len(danh_sach) and danh_sach[i] <= x:
        i *= 2
    vi_tri = binary_search(danh_sach, i // 2, min(i, len(danh_sach) - 1), x)
print("Không tìm thấy" if vi_tri == -1 else "Tìm thấy tại vị trí: " + str(vi_tri))
