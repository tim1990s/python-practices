# Chương trình tính trung bình cộng của dãy số
#
# Người dùng sẽ nhập vào:
# - Số lượng phần tử.
# - Các phần tử của dãy số, nhập lần lượt theo thứ tự.
#
# Ví dụ:
# Nếu nhập:
# số lượng phần tử = 5
# các phần tử = 1, 2, 3, 4, 5
# Kết quả là: chương trình tính trung bình cộng của dãy số rồi in kết quả.
#
# Lưu ý:
# - Số lượng phần tử phải lớn hơn 0.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: tính trung bình cộng của dãy số.
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
    tong = 0

    for i in range(1, n + 1):
        so = float(input("Nhập số thứ " + str(i) + ": "))
        tong += so

    print("Trung bình cộng là:", tong / n)
