# Chương trình quản lý công việc dự án bằng list
#
# Yêu cầu:
# - Viết chương trình lưu task và tính tỷ lệ hoàn thành.
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
# - Đọc task dạng tên, trạng thái.
# - Lưu task vào list.
# - Tính phần trăm task đã xong.

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

records = doc_ban_ghi("Nhập task dạng tên,trạng_thái; ...: ")
items = []
for dong in records:
    ten, trang_thai = tach_truong(dong)
    items.append({"ten": ten, "trang_thai": trang_thai.lower()})
da_xong = sum(1 for x in items if x["trang_thai"] in ("done", "xong", "hoàn thành"))
ty_le = da_xong / len(items) * 100 if items else 0
print("Tỷ lệ hoàn thành:", dinh_dang_so(ty_le), "%")
