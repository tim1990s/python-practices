# Chương trình tính trung bình cộng 3 số
#
# Trung bình cộng của 3 số bằng tổng của 3 số chia cho 3.
#
# Công thức:
# trung_binh_cong = (a + b + c) / 3
#
# Ví dụ:
# Nếu a = 6, b = 7, c = 8 thì:
# Trung bình cộng = (6 + 7 + 8) / 3 = 7
#
# Ý tưởng:
# - Nhập ba số a, b và c.
# - Tính tổng của ba số.
# - Chia tổng cho 3.
# - In kết quả ra màn hình.

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

trung_binh_cong = (a + b + c) / 3

print("Trung bình cộng của 3 số là:", trung_binh_cong)
