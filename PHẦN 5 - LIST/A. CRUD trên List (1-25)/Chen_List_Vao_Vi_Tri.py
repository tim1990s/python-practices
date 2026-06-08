# Chương trình chèn một list vào vị trí bất kỳ
#
# Yêu cầu:
# - Viết chương trình chèn toàn bộ một list vào vị trí bất kỳ của list khác.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Luyện các thao tác CRUD và biến đổi cơ bản trên list như thêm, xóa, sửa, tìm kiếm, sắp xếp, cắt, ghép và tách list.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc list gốc.
# - Đọc list cần chèn và vị trí chèn.
# - Dùng slice rỗng để chèn nhiều phần tử.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_list_chuoi(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [phan_tu.strip() for phan_tu in du_lieu.split(",")]

danh_sach = doc_list_chuoi("Nhập list gốc: ")
vi_tri = int(input("Nhập vị trí cần chèn list mới: "))
list_can_chen = doc_list_chuoi("Nhập list cần chèn: ")

if vi_tri < 0:
    vi_tri = 0
elif vi_tri > len(danh_sach):
    vi_tri = len(danh_sach)

danh_sach[vi_tri:vi_tri] = list_can_chen
print("List sau khi chèn:", danh_sach)
