# Chương trình tính trung bình cộng n số
#
# Trung bình cộng của n số bằng tổng của các số chia cho số lượng số.
#
# Công thức:
# trung_binh_cong = tong / n
#
# Ví dụ:
# Nếu nhập 3 số: 4, 5, 6 thì:
# Tổng = 4 + 5 + 6 = 15
# Trung bình cộng = 15 / 3 = 5
#
# Ý tưởng:
# - Nhập số lượng số cần tính là n.
# - Kiểm tra n phải lớn hơn 0.
# - Dùng vòng lặp để nhập từng số và cộng vào biến tổng.
# - Lấy tổng chia cho n.
# - In kết quả ra màn hình.

n = int(input("Nhập số lượng số cần tính: "))

if n <= 0:
    print("Số lượng số phải lớn hơn 0")
else:
    tong = 0

    for i in range(1, n + 1):
        so = float(input("Nhập số thứ " + str(i) + ": "))
        tong = tong + so

    trung_binh_cong = tong / n

    print("Tổng của", n, "số là:", tong)
    print("Trung bình cộng của", n, "số là:", trung_binh_cong)
