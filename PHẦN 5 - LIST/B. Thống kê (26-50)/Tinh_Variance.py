# Chương trình tính phương sai
#
# Yêu cầu:
# - Viết chương trình tính phương sai của list số.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Luyện thống kê dữ liệu số trong list như max, min, trung bình, trung vị, mode, phương sai, độ lệch chuẩn, phân vị và tần suất.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc list số.
# - Tính trung bình.
# - Tính trung bình bình phương độ lệch so với trung bình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_list_so(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [float(phan_tu.strip()) for phan_tu in du_lieu.split(",") if phan_tu.strip()]


def dinh_dang_so(gia_tri):
    if isinstance(gia_tri, float) and gia_tri.is_integer():
        return int(gia_tri)
    return round(gia_tri, 4)


def dinh_dang_list(danh_sach):
    return [dinh_dang_so(gia_tri) for gia_tri in danh_sach]

danh_sach = doc_list_so("Nhập list số, các số cách nhau bởi dấu phẩy: ")
if not danh_sach:
    print("Không thể tính phương sai của list rỗng")
else:
    trung_binh = sum(danh_sach) / len(danh_sach)
    phuong_sai = sum((gia_tri - trung_binh) ** 2 for gia_tri in danh_sach) / len(danh_sach)
    print("Phương sai:", dinh_dang_so(phuong_sai))
