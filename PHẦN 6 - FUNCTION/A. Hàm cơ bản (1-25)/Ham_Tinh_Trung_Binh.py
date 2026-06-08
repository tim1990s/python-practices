# Chương trình hàm tính trung bình
#
# Yêu cầu:
# - Viết hàm tính trung bình cộng của một list số.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện cách khai báo hàm, truyền tham số, trả về kết quả bằng return và tách chương trình thành các khối xử lý nhỏ.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc list số từ bàn phím.
# - Tách logic tính trung bình vào hàm.
# - Kiểm tra list rỗng trước khi chia.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def tinh_trung_binh(danh_sach):
    if not danh_sach:
        return None
    return sum(danh_sach) / len(danh_sach)


du_lieu = input("Nhập các số, cách nhau bởi dấu phẩy: ")
danh_sach = [float(x.strip()) for x in du_lieu.split(",") if x.strip()]
ket_qua = tinh_trung_binh(danh_sach)
print("Không thể tính trung bình của list rỗng" if ket_qua is None else "Trung bình: " + str(ket_qua))
