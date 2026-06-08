# Chương trình tìm max trong dãy số
#
# Người dùng sẽ nhập vào:
# - Số lượng phần tử.
# - Số thứ 1.
# - Các phần tử của dãy số, nhập lần lượt theo thứ tự.
#
# Ví dụ:
# Nếu nhập:
# số lượng phần tử = 5
# số thứ 1 = 5
# các phần tử = 1, 2, 3, 4, 5
# Kết quả là: chương trình tìm max trong dãy số rồi in giá trị tìm được.
#
# Lưu ý:
# - Số lượng phần tử phải lớn hơn 0.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: tìm max trong dãy số.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng phần tử: "))

if n <= 0:
    print("Số lượng phần tử phải lớn hơn 0")
else:
    max_so = float(input("Nhập số thứ 1: "))

    for i in range(2, n + 1):
        so = float(input("Nhập số thứ " + str(i) + ": "))

        if so > max_so:
            max_so = so

    print("Giá trị lớn nhất là:", max_so)
