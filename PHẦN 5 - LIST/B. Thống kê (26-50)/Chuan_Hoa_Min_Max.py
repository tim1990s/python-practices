# Chương trình chuẩn hóa min-max
#
# Yêu cầu:
# - Viết chương trình chuẩn hóa list số về khoảng 0 đến 1 bằng min-max scaling.
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
# - Tìm min và max.
# - Áp dụng công thức (x - min) / (max - min).

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
    print("List rỗng")
else:
    gia_tri_min = min(danh_sach)
    gia_tri_max = max(danh_sach)
    if gia_tri_min == gia_tri_max:
        ket_qua = [0 for _ in danh_sach]
    else:
        ket_qua = [(gia_tri - gia_tri_min) / (gia_tri_max - gia_tri_min) for gia_tri in danh_sach]
    print("List sau khi chuẩn hóa:", dinh_dang_list(ket_qua))
