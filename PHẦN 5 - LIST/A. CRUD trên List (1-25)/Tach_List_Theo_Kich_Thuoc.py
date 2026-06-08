# Chương trình tách list theo kích thước nhóm
#
# Yêu cầu:
# - Viết chương trình chia list thành các nhóm nhỏ có kích thước được nhập.
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
# - Đọc kích thước mỗi nhóm.
# - Dùng vòng lặp và slicing để tách list.

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
kich_thuoc = int(input("Nhập kích thước mỗi nhóm: "))

if kich_thuoc <= 0:
    print("Kích thước nhóm phải lớn hơn 0")
else:
    ket_qua = [danh_sach[i:i + kich_thuoc] for i in range(0, len(danh_sach), kich_thuoc)]
    print("Các nhóm sau khi tách:", ket_qua)
