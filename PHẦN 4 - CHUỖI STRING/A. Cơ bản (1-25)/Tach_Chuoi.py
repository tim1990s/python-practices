# Chương trình tách chuỗi
#
# Yêu cầu:
# - Viết chương trình tách chuỗi.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Dùng các thao tác chuỗi cơ bản như độ dài, cắt chuỗi, đổi hoa thường, tìm kiếm hoặc thay thế.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc chuỗi đầu vào từ bàn phím.
# - Áp dụng phương thức chuỗi hoặc phép cắt chuỗi phù hợp.
# - In kết quả sau khi xử lý.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chuoi = input("Nhập chuỗi: ")
phan_cach = input("Nhập ký tự phân cách, bỏ trống để tách theo khoảng trắng: ")
if phan_cach == "":
    ket_qua = chuoi.split()
else:
    ket_qua = chuoi.split(phan_cach)
print("Các phần sau khi tách:")
for phan in ket_qua:
    print(phan)
