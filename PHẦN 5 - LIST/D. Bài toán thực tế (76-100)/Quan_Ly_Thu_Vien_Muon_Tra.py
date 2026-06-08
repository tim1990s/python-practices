# Chương trình quản lý mượn trả thư viện bằng list
#
# Yêu cầu:
# - Viết chương trình lưu giao dịch mượn trả và lọc sách chưa trả.
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
# - Đọc giao dịch dạng sách, người mượn, trạng thái.
# - Lưu giao dịch vào list.
# - Lọc giao dịch chưa trả.

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

records = doc_ban_ghi("Nhập giao dịch dạng sách,người_mượn,trạng_thái; ...: ")
items = []
for dong in records:
    sach, nguoi_muon, trang_thai = tach_truong(dong)
    items.append({"sach": sach, "nguoi_muon": nguoi_muon, "trang_thai": trang_thai.lower()})
print("Sách chưa trả:", [x for x in items if x["trang_thai"] not in ("đã trả", "da tra", "returned")])
