# Chương trình tính PI xấp xỉ bằng chuỗi Leibniz
#
# Người dùng sẽ nhập vào:
# - Số lượng số hạng.
#
# Ví dụ:
# Nếu nhập:
# số lượng số hạng = 5
# Kết quả là: chương trình tính PI xấp xỉ bằng chuỗi Leibniz rồi in kết quả.
#
# Lưu ý:
# - Số lượng số hạng phải lớn hơn 0.
# - Số lượng số hạng càng lớn thì kết quả xấp xỉ thường càng gần giá trị thật.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Cộng dồn từng số hạng của công thức xấp xỉ bằng vòng lặp.
# - Thực hiện yêu cầu: tính PI xấp xỉ bằng chuỗi Leibniz.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng số hạng: "))

if n <= 0:
    print("Số lượng số hạng phải lớn hơn 0")
else:
    tong = 0

    for i in range(n):
        tong += ((-1) ** i) / (2 * i + 1)

    pi = 4 * tong
    print("PI xấp xỉ là:", pi)
