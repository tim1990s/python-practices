a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))

phep_toan = input("Nhap phep toan (+, -, *, /): ")

if phep_toan == "+":
    ket_qua = a + b
    print(f"Ket qua: {a} {phep_toan} {b} = {ket_qua}")
if phep_toan == "-":
    ket_qua = a - b
    print(f"Ket qua: {a} {phep_toan} {b} = {ket_qua}")

if phep_toan == "*":
    ket_qua = a * b
    print(f"Ket qua: {a} {phep_toan} {b}= {ket_qua}")

if phep_toan == "/":
    if b == 0:
        print("Khong the chia voi so 0")
    else:
        ket_qua = a / b
        print(f"Ket qua: {a} {phep_toan} {b}= {ket_qua}")
else:
    print("Phep toan khong hop le")