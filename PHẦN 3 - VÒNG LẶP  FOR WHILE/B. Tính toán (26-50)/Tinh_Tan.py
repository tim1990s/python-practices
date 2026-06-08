# Chương trình tính tan(x) xấp xỉ từ sin(x) và cos(x)
#
# Người dùng sẽ nhập vào:
# - X theo radian.
# - Số lượng số hạng.
#
# Ví dụ:
# Nếu nhập:
# x theo radian = 1
# số lượng số hạng = 5
# Kết quả là: chương trình tính tan(x) xấp xỉ từ sin(x) và cos(x) rồi in kết quả.
#
# Lưu ý:
# - Số lượng số hạng phải lớn hơn 0.
# - Không tính được tan(x) vì cos(x) bằng 0.
# - Số lượng số hạng càng lớn thì kết quả xấp xỉ thường càng gần giá trị thật.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Cộng dồn từng số hạng của công thức xấp xỉ bằng vòng lặp.
# - Thực hiện yêu cầu: tính tan(x) xấp xỉ từ sin(x) và cos(x).
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
    sin_x = 0
    cos_x = 0

    for i in range(n):
        mu_sin = 2 * i + 1
        giai_thua_sin = 1

        for j in range(1, mu_sin + 1):
            giai_thua_sin *= j

        sin_x += ((-1) ** i) * (x ** mu_sin) / giai_thua_sin

        mu_cos = 2 * i
        giai_thua_cos = 1

        for j in range(1, mu_cos + 1):
            giai_thua_cos *= j

        cos_x += ((-1) ** i) * (x ** mu_cos) / giai_thua_cos

    if cos_x == 0:
        print("Không tính được tan(x) vì cos(x) bằng 0")
    else:
        print("tan(x) xấp xỉ là:", sin_x / cos_x)
