# Chương trình in tam giác cân sao

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập chiều cao: "))

if n <= 0:
    print("Chiều cao phải lớn hơn 0")
else:
    for i in range(1, n + 1):
        khoang_trang = " " * (n - i)
        sao = "* " * i
        print(khoang_trang + sao)
