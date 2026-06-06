# Chương trình tính lập phương của một số
#
# Lập phương của một số là kết quả khi nhân số đó với chính nó 3 lần.
#
# Công thức:
# lap_phuong = n * n * n
#
# Ví dụ:
# Nếu n = 3 thì:
# Lập phương = 3 * 3 * 3 = 27
#
# Ý tưởng:
# - Nhập số n.
# - Nhân n với n rồi nhân tiếp với n.
# - In kết quả ra màn hình.

n = float(input("Nhập số n: "))

lap_phuong = n * n * n

print("Lập phương của", n, "là:", lap_phuong)
