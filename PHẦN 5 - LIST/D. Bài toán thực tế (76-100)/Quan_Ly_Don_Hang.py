# Chương trình quản lý đơn hàng bằng list
#
# Yêu cầu:
# - Viết chương trình lưu đơn hàng và tính doanh thu đã thanh toán.
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
# - Đọc đơn hàng dạng mã, khách, số tiền, trạng thái.
# - Lưu đơn hàng vào list.
# - Cộng tiền đơn đã thanh toán.

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

records = doc_ban_ghi("Nhập đơn hàng dạng mã,khách,số_tiền,trạng_thái; ...: ")
items = []
for dong in records:
    ma, khach, so_tien, trang_thai = tach_truong(dong)
    items.append({"ma": ma, "khach": khach, "so_tien": float(so_tien), "trang_thai": trang_thai.lower()})
doanh_thu = sum(x["so_tien"] for x in items if x["trang_thai"] in ("paid", "đã thanh toán", "da thanh toan"))
print("Doanh thu đã thanh toán:", dinh_dang_so(doanh_thu))
