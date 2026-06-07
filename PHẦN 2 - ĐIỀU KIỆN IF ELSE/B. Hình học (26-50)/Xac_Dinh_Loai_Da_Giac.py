# Chương trình xác định loại đa giác theo số cạnh

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

so_canh = int(input("Nhập số cạnh của đa giác: "))

if so_canh < 3:
    print("Không phải là đa giác")
elif so_canh == 3:
    print("Đây là tam giác")
elif so_canh == 4:
    print("Đây là tứ giác")
elif so_canh == 5:
    print("Đây là ngũ giác")
elif so_canh == 6:
    print("Đây là lục giác")
else:
    print("Đây là đa giác có", so_canh, "cạnh")
