# Chương trình tính lũy thừa bằng vòng lặp
#
# Người dùng sẽ nhập vào:
# - Cơ số.
# - Số mũ nguyên không âm.
#
# Ví dụ:
# Nếu nhập:
# cơ số = 2
# số mũ nguyên không âm = 3
# Kết quả là: chương trình tính lũy thừa bằng vòng lặp rồi in kết quả.
#
# Lưu ý:
# - Số mũ phải không âm.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: tính lũy thừa bằng vòng lặp.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

co_so = float(input("Nhập cơ số: "))
so_mu = int(input("Nhập số mũ nguyên không âm: "))

ket_qua = 1

if so_mu < 0:
    print("Số mũ phải không âm")
else:
    for _ in range(so_mu):
        ket_qua *= co_so

    print("Kết quả là:", ket_qua)
