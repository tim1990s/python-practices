# Chương trình lấy một đoạn list bằng slice
#
# Yêu cầu:
# - Viết chương trình lấy một đoạn con của list theo vị trí bắt đầu và kết thúc.
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
# - Đọc list ban đầu.
# - Đọc vị trí bắt đầu và kết thúc.
# - Dùng slicing để lấy đoạn con.

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

danh_sach = doc_list_chuoi("Nhập list, các phần tử cách nhau bởi dấu phẩy: ")
bat_dau = int(input("Nhập vị trí bắt đầu: "))
ket_thuc = int(input("Nhập vị trí kết thúc: "))
ket_qua = danh_sach[bat_dau:ket_thuc]
print("Đoạn list được lấy:", ket_qua)
