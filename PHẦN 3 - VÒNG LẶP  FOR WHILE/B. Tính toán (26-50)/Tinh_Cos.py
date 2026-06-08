# Chương trình tính cos(x) xấp xỉ bằng chuỗi Taylor
#
# Người dùng sẽ nhập vào:
# - X theo radian.
# - Số lượng số hạng.
#
# Ví dụ:
# Nếu nhập:
# x theo radian = 1
# số lượng số hạng = 5
# Kết quả là: chương trình tính cos(x) xấp xỉ bằng chuỗi Taylor rồi in kết quả.
#
# Lưu ý:
# - Số lượng số hạng phải lớn hơn 0.
# - Số lượng số hạng càng lớn thì kết quả xấp xỉ thường càng gần giá trị thật.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Cộng dồn từng số hạng của công thức xấp xỉ bằng vòng lặp.
# - Thực hiện yêu cầu: tính cos(x) xấp xỉ bằng chuỗi Taylor.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

x = float(input("Nhập x theo radian: "))
n = int(input("Nhập số lượng số hạng: "))

if n <= 0:
    print("Số lượng số hạng phải lớn hơn 0")
else:
    cos_x = 0

    for i in range(n):
        mu = 2 * i
        giai_thua = 1

        for j in range(1, mu + 1):
            giai_thua *= j

        cos_x += ((-1) ** i) * (x ** mu) / giai_thua

    print("cos(x) xấp xỉ là:", cos_x)
