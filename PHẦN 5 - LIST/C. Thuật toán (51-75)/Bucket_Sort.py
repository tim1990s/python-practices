# Chương trình Bucket Sort
#
# Yêu cầu:
# - Viết chương trình sắp xếp list số thực bằng Bucket Sort.
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
# - Chia dữ liệu vào nhiều bucket.
# - Sắp xếp từng bucket.
# - Ghép các bucket lại.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_list_so(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [float(x.strip()) for x in du_lieu.split(",") if x.strip()]


def dinh_dang_so(x):
    if isinstance(x, float) and x.is_integer():
        return int(x)
    return round(x, 4)


def dinh_dang_list(danh_sach):
    return [dinh_dang_so(x) for x in danh_sach]

danh_sach = doc_list_so("Nhập list số thực: ")
if not danh_sach:
    print("List sau khi Bucket Sort: []")
else:
    so_bucket = len(danh_sach)
    nho_nhat, lon_nhat = min(danh_sach), max(danh_sach)
    if nho_nhat == lon_nhat:
        ket_qua = danh_sach
    else:
        buckets = [[] for _ in range(so_bucket)]
        for x in danh_sach:
            vi_tri = int((x - nho_nhat) / (lon_nhat - nho_nhat) * (so_bucket - 1))
            buckets[vi_tri].append(x)
        ket_qua = []
        for bucket in buckets:
            ket_qua.extend(sorted(bucket))
    print("List sau khi Bucket Sort:", dinh_dang_list(ket_qua))
