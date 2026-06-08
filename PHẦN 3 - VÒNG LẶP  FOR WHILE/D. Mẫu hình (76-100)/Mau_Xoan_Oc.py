# Chương trình in mẫu xoắn ốc số
#
# Người dùng sẽ nhập vào:
# - Kích thước.
#
# Ví dụ:
# Nếu nhập:
# kích thước = 5
# Kết quả là: chương trình in mẫu xoắn ốc số theo dữ liệu đã nhập.
#
# Lưu ý:
# - Kích thước phải lớn hơn 0.
# - Kích thước, chiều cao hoặc số dòng cần là số nguyên dương để in được mẫu hình.
#
# Ý tưởng:
# - Nhập dữ liệu cần thiết từ bàn phím.
# - Kiểm tra dữ liệu đầu vào trước khi xử lý chính.
# - Dùng vòng lặp để xây từng dòng của mẫu hình.
# - Thực hiện yêu cầu: in mẫu xoắn ốc số.
# - In kết quả ra màn hình.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập kích thước: "))

if n <= 0:
    print("Kích thước phải lớn hơn 0")
else:
    ma_tran = [[0 for _ in range(n)] for _ in range(n)]
    tren = 0
    duoi = n - 1
    trai = 0
    phai = n - 1
    so = 1

    while tren <= duoi and trai <= phai:
        for cot in range(trai, phai + 1):
            ma_tran[tren][cot] = so
            so += 1
        tren += 1

        for hang in range(tren, duoi + 1):
            ma_tran[hang][phai] = so
            so += 1
        phai -= 1

        if tren <= duoi:
            for cot in range(phai, trai - 1, -1):
                ma_tran[duoi][cot] = so
                so += 1
            duoi -= 1

        if trai <= phai:
            for hang in range(duoi, tren - 1, -1):
                ma_tran[hang][trai] = so
                so += 1
            trai += 1

    for hang in ma_tran:
        dong = ""

        for gia_tri in hang:
            dong += str(gia_tri).rjust(3) + " "

        print(dong)
