# Chương trình tính Q1, Q3 và IQR
#
# Yêu cầu:
# - Viết chương trình tính tứ phân vị Q1, Q3 và khoảng tứ phân vị IQR.
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
# - Sắp xếp list.
# - Tính percentile 25 và 75 rồi lấy IQR = Q3 - Q1.

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


danh_sach = sorted(doc_list_so("Nhập list số, các số cách nhau bởi dấu phẩy: "))
if not danh_sach:
    print("List rỗng")
else:
    q1 = tinh_percentile(danh_sach, 25)
    q3 = tinh_percentile(danh_sach, 75)
    iqr = q3 - q1
    print("Q1:", dinh_dang_so(q1))
    print("Q3:", dinh_dang_so(q3))
    print("IQR:", dinh_dang_so(iqr))
