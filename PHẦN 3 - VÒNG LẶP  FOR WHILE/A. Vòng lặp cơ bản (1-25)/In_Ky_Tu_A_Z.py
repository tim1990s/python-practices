# Chương trình in ký tự A-Z
#
# Người dùng sẽ nhập vào:
# - Không cần nhập dữ liệu từ bàn phím.
#
# Ví dụ:
# Chạy chương trình trực tiếp, không cần nhập dữ liệu.
# Kết quả là: chương trình in ký tự A-Z ra màn hình.
#
# Lưu ý:
# - Dữ liệu nhập cần đúng kiểu theo yêu cầu của từng dòng input.
#
# Ý tưởng:
# - Xác định sẵn khoảng giá trị cần duyệt trong chương trình.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: in ký tự A-Z.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

for ma in range(ord("A"), ord("Z") + 1):
    print(chr(ma))
