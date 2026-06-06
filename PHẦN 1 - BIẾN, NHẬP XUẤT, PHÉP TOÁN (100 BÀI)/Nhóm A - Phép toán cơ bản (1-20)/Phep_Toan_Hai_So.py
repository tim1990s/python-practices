# Chương trình tính kết quả của hai số a và b theo phép toán nhập vào
#
# Người dùng sẽ nhập vào:
# - Số thứ nhất là a.
# - Số thứ hai là b.
# - Phép toán muốn thực hiện.
#
# Các phép toán được hỗ trợ:
# + : cộng hai số
# - : trừ hai số
# * : nhân hai số
# / : chia hai số
#
# Ví dụ:
# Nếu nhập:
# a = 10
# b = 5
# phép toán = +
# Kết quả là: 10 + 5 = 15
#
# Nếu nhập:
# a = 10
# b = 5
# phép toán = /
# Kết quả là: 10 / 5 = 2
#
# Lưu ý:
# - Với phép chia a / b, số b là số chia.
# - Số chia không được bằng 0.
# - Nếu b = 0 mà người dùng chọn phép chia thì chương trình sẽ báo lỗi.
#
# Ý tưởng:
# - Nhập hai số a và b từ bàn phím.
# - Nhập phép toán cần thực hiện.
# - Kiểm tra phép toán là cộng, trừ, nhân hay chia.
# - Nếu là phép chia thì kiểm tra b có bằng 0 hay không.
# - Tính kết quả phù hợp với phép toán.
# - In kết quả ra màn hình.

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

phep_toan = input("Nhập phép toán (+, -, *, /): ")

if phep_toan == "+":
    ket_qua = a + b
    print("Kết quả:", a, "+", b, "=", ket_qua)

elif phep_toan == "-":
    ket_qua = a - b
    print("Kết quả:", a, "-", b, "=", ket_qua)

elif phep_toan == "*":
    ket_qua = a * b
    print("Kết quả:", a, "*", b, "=", ket_qua)

elif phep_toan == "/":
    if b == 0:
        print("Không thể thực hiện phép chia vì số chia b không được bằng 0")
    else:
        ket_qua = a / b
        print("Kết quả:", a, "/", b, "=", ket_qua)

else:
    print("Phép toán không hợp lệ. Vui lòng nhập một trong các phép toán: +, -, *, /")
