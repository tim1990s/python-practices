# Chương trình quản lý điểm danh bằng list
#
# Yêu cầu:
# - Viết chương trình lưu điểm danh và liệt kê người vắng.
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
# - Đọc điểm danh dạng tên, trạng thái.
# - Lưu bản ghi vào list.
# - Lọc người vắng.

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

records = doc_ban_ghi("Nhập điểm danh dạng tên,trạng_thái; ...: ")
items = []
for dong in records:
    ten, trang_thai = tach_truong(dong)
    items.append({"ten": ten, "trang_thai": trang_thai.lower()})
print("Người vắng:", [x for x in items if x["trang_thai"] in ("vắng", "vang", "absent")])
