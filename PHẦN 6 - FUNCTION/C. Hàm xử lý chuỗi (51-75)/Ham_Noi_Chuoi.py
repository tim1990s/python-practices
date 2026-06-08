# Chương trình hàm nối chuỗi
#
# Yêu cầu:
# - Viết hàm nối list chuỗi bằng ký tự phân cách.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện viết hàm xử lý chuỗi: đảo chuỗi, chuẩn hóa, validate, parse, tìm kiếm, thống kê và biến đổi văn bản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc các phần tử cách nhau bởi dấu phẩy.
# - Đọc ký tự phân cách.
# - Dùng join() để nối chuỗi.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def noi_chuoi(danh_sach, phan_cach):
    return phan_cach.join(danh_sach)


danh_sach = [x.strip() for x in input("Nhập các chuỗi, cách nhau bởi dấu phẩy: ").split(",")]
phan_cach = input("Nhập ký tự phân cách: ")
print("Chuỗi sau khi nối:", noi_chuoi(danh_sach, phan_cach))
