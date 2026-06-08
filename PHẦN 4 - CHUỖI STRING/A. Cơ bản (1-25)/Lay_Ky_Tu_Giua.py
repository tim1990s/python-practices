# Chương trình lấy ký tự giữa
#
# Yêu cầu:
# - Viết chương trình lấy ký tự giữa.
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
do_dai = len(chuoi)
if do_dai == 0:
    print("Chuỗi rỗng")
elif do_dai % 2 == 1:
    print("Ký tự giữa:", chuoi[do_dai // 2])
else:
    print("Hai ký tự giữa:", chuoi[do_dai // 2 - 1:do_dai // 2 + 1])
