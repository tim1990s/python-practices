# Chương trình tính trung bình cộng của 2 số
#
# Trung bình cộng của 2 số là giá trị được tính bằng cách:
# - Cộng hai số lại với nhau.
# - Sau đó chia tổng đó cho 2.
#
# Công thức:
# trung_binh_cong = (a + b) / 2
#
# Ví dụ:
# Nếu a = 6 và b = 8 thì:
# Tổng của hai số là: 6 + 8 = 14
# Trung bình cộng là: 14 / 2 = 7
#
# Nếu a = 2.5 và b = 7.5 thì:
# Tổng của hai số là: 2.5 + 7.5 = 10
# Trung bình cộng là: 10 / 2 = 5
#
# Ý tưởng:
# - Nhập số thứ nhất là a.
# - Nhập số thứ hai là b.
# - Tính tổng của a và b.
# - Lấy tổng đó chia cho 2 để được trung bình cộng.
# - In kết quả ra màn hình.

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

tong = a + b
trung_binh_cong = tong / 2

print("Tổng của", a, "và", b, "là:", tong)
print("Trung bình cộng của", a, "và", b, "là:", trung_binh_cong)
