# Chương trình tính chu vi tam giác
#
# Chu vi tam giác là tổng độ dài ba cạnh của tam giác.
#
# Công thức:
# chu_vi = canh_a + canh_b + canh_c
#
# Ví dụ:
# Nếu ba cạnh là 3, 4, 5 thì:
# Chu vi = 3 + 4 + 5 = 12
#
# Ý tưởng:
# - Nhập ba cạnh của tam giác.
# - Kiểm tra ba cạnh phải lớn hơn 0.
# - Kiểm tra ba cạnh có tạo thành tam giác hợp lệ hay không.
# - Nếu hợp lệ thì cộng ba cạnh để tính chu vi.
# - In kết quả ra màn hình.

canh_a = float(input("Nhập cạnh a: "))
canh_b = float(input("Nhập cạnh b: "))
canh_c = float(input("Nhập cạnh c: "))

if canh_a <= 0 or canh_b <= 0 or canh_c <= 0:
    print("Ba cạnh tam giác phải lớn hơn 0")
elif canh_a + canh_b <= canh_c or canh_a + canh_c <= canh_b or canh_b + canh_c <= canh_a:
    print("Ba cạnh không tạo thành tam giác hợp lệ")
else:
    chu_vi = canh_a + canh_b + canh_c
    print("Chu vi tam giác là:", chu_vi)
