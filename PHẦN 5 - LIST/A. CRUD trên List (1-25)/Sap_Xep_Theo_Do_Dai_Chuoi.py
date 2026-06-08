# Chương trình sắp xếp list chuỗi theo độ dài
#
# Yêu cầu:
# - Viết chương trình sắp xếp các chuỗi trong list theo độ dài tăng dần.
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
# - Đọc list chuỗi.
# - Dùng sorted() với key=len.
# - In list sau khi sắp xếp.

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

danh_sach = doc_list_chuoi("Nhập list chuỗi, các phần tử cách nhau bởi dấu phẩy: ")
ket_qua = sorted(danh_sach, key=len)
print("List sắp xếp theo độ dài:", ket_qua)
