# Chương trình kiểm tra mật khẩu mạnh

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

mat_khau = input("Nhập mật khẩu: ")

co_chu_thuong = any(ky_tu.islower() for ky_tu in mat_khau)
co_chu_hoa = any(ky_tu.isupper() for ky_tu in mat_khau)
co_chu_so = any(ky_tu.isdigit() for ky_tu in mat_khau)
co_ky_tu_dac_biet = any(not ky_tu.isalnum() for ky_tu in mat_khau)

if len(mat_khau) >= 8 and co_chu_thuong and co_chu_hoa and co_chu_so and co_ky_tu_dac_biet:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu chưa đủ mạnh")
