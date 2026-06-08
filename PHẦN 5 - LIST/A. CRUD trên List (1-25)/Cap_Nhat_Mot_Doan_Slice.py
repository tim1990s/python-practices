# Chương trình cập nhật một đoạn list bằng slice
#
# Yêu cầu:
# - Viết chương trình thay thế một đoạn trong list bằng các phần tử mới.
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
# - Đọc khoảng cần thay thế và list mới.
# - Gán list mới vào slice tương ứng.

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

danh_sach = doc_list_chuoi("Nhập list ban đầu: ")
bat_dau = int(input("Nhập vị trí bắt đầu cần thay: "))
ket_thuc = int(input("Nhập vị trí kết thúc cần thay: "))
phan_tu_moi = doc_list_chuoi("Nhập list phần tử mới: ")
danh_sach[bat_dau:ket_thuc] = phan_tu_moi
print("List sau khi cập nhật đoạn:", danh_sach)
