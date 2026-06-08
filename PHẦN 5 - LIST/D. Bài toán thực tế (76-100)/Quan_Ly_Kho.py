# Chương trình quản lý kho bằng list
#
# Yêu cầu:
# - Viết chương trình lưu hàng tồn kho và tính tổng giá trị kho.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Luyện cách dùng list để lưu nhiều bản ghi, duyệt dữ liệu, lọc, tìm kiếm, thống kê và cập nhật thông tin trong bài toán thực tế.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc hàng dạng mã, tên, số lượng, đơn giá.
# - Lưu mỗi mặt hàng vào list.
# - Tính số lượng nhân đơn giá.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def doc_ban_ghi(thong_bao):
    du_lieu = input(thong_bao).strip()
    if not du_lieu:
        return []
    return [dong.strip() for dong in du_lieu.split(";") if dong.strip()]


def tach_truong(dong):
    return [x.strip() for x in dong.split(",")]


def dinh_dang_so(x):
    if isinstance(x, float) and x.is_integer():
        return int(x)
    return round(x, 2)

records = doc_ban_ghi("Nhập hàng dạng mã,tên,số_lượng,đơn_giá; ...: ")
items = []
for dong in records:
    ma, ten, so_luong, don_gia = tach_truong(dong)
    items.append({"ma": ma, "ten": ten, "so_luong": int(so_luong), "don_gia": float(don_gia)})
print("Danh sách hàng:", items)
print("Tổng giá trị kho:", dinh_dang_so(sum(x["so_luong"] * x["don_gia"] for x in items)))
