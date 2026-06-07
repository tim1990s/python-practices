# Chương trình tính lũy thừa bằng vòng lặp

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

co_so = float(input("Nhập cơ số: "))
so_mu = int(input("Nhập số mũ nguyên không âm: "))

ket_qua = 1

if so_mu < 0:
    print("Số mũ phải không âm")
else:
    for _ in range(so_mu):
        ket_qua *= co_so

    print("Kết quả là:", ket_qua)
