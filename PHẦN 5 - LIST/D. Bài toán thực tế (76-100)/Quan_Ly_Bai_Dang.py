# Chương trình quản lý bài đăng bằng list
#
# Yêu cầu:
# - Viết chương trình lưu bài đăng và tìm bài nhiều lượt thích nhất.
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
# - Đọc bài đăng dạng tiêu đề, lượt thích.
# - Lưu bài đăng vào list.
# - Tìm bài có lượt thích cao nhất.

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

records = doc_ban_ghi("Nhập bài đăng dạng tiêu_đề,lượt_thích; ...: ")
items = []
for dong in records:
    tieu_de, luot_thich = tach_truong(dong)
    items.append({"tieu_de": tieu_de, "luot_thich": int(luot_thich)})
print("Bài nhiều lượt thích nhất:", max(items, key=lambda x: x["luot_thich"]) if items else "Chưa có dữ liệu")
