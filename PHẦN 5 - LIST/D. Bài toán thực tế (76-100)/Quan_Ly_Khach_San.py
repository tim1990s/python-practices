# Chương trình quản lý phòng khách sạn bằng list
#
# Yêu cầu:
# - Viết chương trình lưu phòng và lọc phòng trống.
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
# - Đọc phòng dạng số phòng, loại, trạng thái.
# - Lưu phòng vào list.
# - Lọc phòng trống.

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

records = doc_ban_ghi("Nhập phòng dạng số_phòng,loại,trạng_thái; ...: ")
items = []
for dong in records:
    so_phong, loai, trang_thai = tach_truong(dong)
    items.append({"so_phong": so_phong, "loai": loai, "trang_thai": trang_thai.lower()})
print("Phòng trống:", [x for x in items if x["trang_thai"] in ("trống", "trong", "available")])
