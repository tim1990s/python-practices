# Chương trình tính tổng các số từ 1 đến n
#
# Tính tổng là cộng các số lại với nhau để được một kết quả.
#
# Ví dụ:
# Nếu n = 5 thì:
# 1 + 2 + 3 + 4 + 5 = 15
#
# Nếu n = 10 thì:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
#
# Ý tưởng:
# - Nhập vào số nguyên dương n.
# - Tạo biến tong ban đầu bằng 0.
# - Dùng vòng lặp để cộng lần lượt các số từ 1 đến n vào tong.
# - In ra kết quả tổng.

n = int(input("Nhập số n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương")
else:
    tong = 0

    for i in range(1, n + 1):
        tong = tong + i

    print("Tổng các số từ 1 đến", n, "là:", tong)
