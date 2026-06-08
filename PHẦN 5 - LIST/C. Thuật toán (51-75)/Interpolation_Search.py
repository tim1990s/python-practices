# Chương trình Interpolation Search
#
# Yêu cầu:
# - Viết chương trình tìm kiếm nội suy trong list đã sắp xếp.
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
# - Đọc list đã sắp xếp.
# - Ước lượng vị trí dựa trên giá trị cần tìm.
# - Thu hẹp khoảng tìm kiếm.

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

danh_sach = doc_list_so_nguyen("Nhập list đã sắp xếp tăng dần: ")
x = int(input("Nhập giá trị cần tìm: "))
thap, cao = 0, len(danh_sach) - 1
vi_tri = -1
while thap <= cao and danh_sach and danh_sach[thap] <= x <= danh_sach[cao]:
    if danh_sach[cao] == danh_sach[thap]:
        if danh_sach[thap] == x:
            vi_tri = thap
        break
    pos = thap + ((x - danh_sach[thap]) * (cao - thap)) // (danh_sach[cao] - danh_sach[thap])
    if danh_sach[pos] == x:
        vi_tri = pos
        break
    if danh_sach[pos] < x:
        thap = pos + 1
    else:
        cao = pos - 1
print("Không tìm thấy" if vi_tri == -1 else "Tìm thấy tại vị trí: " + str(vi_tri))
