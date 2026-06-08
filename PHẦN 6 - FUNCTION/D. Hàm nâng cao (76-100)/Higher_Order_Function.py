# Chương trình Higher Order Function
#
# Yêu cầu:
# - Viết hàm nhận hàm khác làm tham số.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện các kỹ thuật hàm nâng cao: đệ quy, decorator, closure, higher-order function, generator, iterator, callback, async và các pattern đơn giản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Tạo hàm áp dụng phép biến đổi.
# - Truyền một hàm vào làm tham số.
# - Trả về list đã được biến đổi.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def ap_dung(danh_sach, ham):
    return [ham(x) for x in danh_sach]


def gap_doi(x):
    return x * 2


danh_sach = [float(x.strip()) for x in input("Nhập list số: ").split(",") if x.strip()]
print("List sau khi gấp đôi:", ap_dung(danh_sach, gap_doi))
