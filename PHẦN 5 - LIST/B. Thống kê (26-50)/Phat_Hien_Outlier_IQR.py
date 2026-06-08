# Chương trình phát hiện outlier bằng IQR
#
# Yêu cầu:
# - Viết chương trình tìm các giá trị ngoại lệ trong list số bằng quy tắc IQR.
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
# - Tính Q1, Q3 và IQR.
# - Outlier là giá trị nhỏ hơn Q1 - 1.5*IQR hoặc lớn hơn Q3 + 1.5*IQR.

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

import math


def tinh_percentile(danh_sach_da_sap_xep, p):
    vi_tri = (len(danh_sach_da_sap_xep) - 1) * p / 100
    duoi = math.floor(vi_tri)
    tren = math.ceil(vi_tri)
    if duoi == tren:
        return danh_sach_da_sap_xep[int(vi_tri)]
    ty_le = vi_tri - duoi
    return danh_sach_da_sap_xep[duoi] * (1 - ty_le) + danh_sach_da_sap_xep[tren] * ty_le


danh_sach = doc_list_so("Nhập list số, các số cách nhau bởi dấu phẩy: ")
if not danh_sach:
    print("List rỗng")
else:
    danh_sach_sap_xep = sorted(danh_sach)
    q1 = tinh_percentile(danh_sach_sap_xep, 25)
    q3 = tinh_percentile(danh_sach_sap_xep, 75)
    iqr = q3 - q1
    can_duoi = q1 - 1.5 * iqr
    can_tren = q3 + 1.5 * iqr
    outlier = [gia_tri for gia_tri in danh_sach if gia_tri < can_duoi or gia_tri > can_tren]
    print("Cận dưới:", dinh_dang_so(can_duoi))
    print("Cận trên:", dinh_dang_so(can_tren))
    print("Outlier:", dinh_dang_list(outlier))
