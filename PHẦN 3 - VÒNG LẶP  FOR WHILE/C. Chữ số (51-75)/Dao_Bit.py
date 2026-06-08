# Chương trình đảo bit của chuỗi nhị phân
#
# Người dùng sẽ nhập vào:
# - Chuỗi nhị phân.
#
# Ví dụ:
# Nếu nhập:
# chuỗi nhị phân = 10110
# Kết quả là: chương trình thực hiện yêu cầu đảo bit của chuỗi nhị phân.
#
# Lưu ý:
# - Chuỗi nhị phân không hợp lệ.
# - Chuỗi nhị phân hợp lệ chỉ gồm các ký tự 0 và 1.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp for để lặp qua các giá trị cần xử lý.
# - Thực hiện yêu cầu: đảo bit của chuỗi nhị phân.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

chuoi = input("Nhập chuỗi nhị phân: ")
hop_le = True
ket_qua = ""

for bit in chuoi:
    if bit == "0":
        ket_qua += "1"
    elif bit == "1":
        ket_qua += "0"
    else:
        hop_le = False
        break

if not hop_le or chuoi == "":
    print("Chuỗi nhị phân không hợp lệ")
else:
    print("Chuỗi sau khi đảo bit là:", ket_qua)
