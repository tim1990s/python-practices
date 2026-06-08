# Chương trình tính ln(x) xấp xỉ bằng chuỗi Taylor biến đổi
#
# Người dùng sẽ nhập vào:
# - X dương.
# - Số lượng số hạng.
#
# Ví dụ:
# Nếu nhập:
# x dương = 5
# số lượng số hạng = 5
# Kết quả là: chương trình tính ln(x) xấp xỉ bằng chuỗi Taylor biến đổi rồi in kết quả.
#
# Lưu ý:
# - x và số lượng số hạng phải lớn hơn 0.
# - Số lượng số hạng càng lớn thì kết quả xấp xỉ thường càng gần giá trị thật.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Cộng dồn từng số hạng của công thức xấp xỉ bằng vòng lặp.
# - Thực hiện yêu cầu: tính ln(x) xấp xỉ bằng chuỗi Taylor biến đổi.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập x dương: "))
n = int(input("Nhập số lượng số hạng: "))

if x <= 0 or n <= 0:
    print("x và số lượng số hạng phải lớn hơn 0")
else:
    y = (x - 1) / (x + 1)
    tong = 0

    for i in range(n):
        mu = 2 * i + 1
        tong += (y ** mu) / mu

    log_x = 2 * tong
    print("ln(x) xấp xỉ là:", log_x)
