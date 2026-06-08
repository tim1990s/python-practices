# Chương trình tìm sản phẩm bán chạy bằng list
#
# Yêu cầu:
# - Viết chương trình tìm sản phẩm có số lượng bán cao nhất.
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
# - Đọc sản phẩm dạng tên, số lượng bán.
# - Lưu sản phẩm vào list.
# - Tìm sản phẩm bán nhiều nhất.

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

records = doc_ban_ghi("Nhập sản phẩm dạng tên,số_lượng_bán; ...: ")
items = []
for dong in records:
    ten, so_luong = tach_truong(dong)
    items.append({"ten": ten, "so_luong_ban": int(so_luong)})
print("Sản phẩm bán chạy nhất:", max(items, key=lambda x: x["so_luong_ban"]) if items else "Chưa có dữ liệu")
