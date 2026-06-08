# Chương trình quản lý bệnh nhân bằng list
#
# Yêu cầu:
# - Viết chương trình lưu bệnh nhân và sắp xếp theo mức ưu tiên.
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
# - Đọc bệnh nhân dạng tên, tuổi, ưu tiên.
# - Lưu bệnh nhân vào list.
# - Sắp xếp giảm dần theo ưu tiên.

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

records = doc_ban_ghi("Nhập bệnh nhân dạng tên,tuổi,ưu_tiên; ...: ")
items = []
for dong in records:
    ten, tuoi, uu_tien = tach_truong(dong)
    items.append({"ten": ten, "tuoi": int(tuoi), "uu_tien": int(uu_tien)})
print("Danh sách theo ưu tiên:", sorted(items, key=lambda x: x["uu_tien"], reverse=True))
