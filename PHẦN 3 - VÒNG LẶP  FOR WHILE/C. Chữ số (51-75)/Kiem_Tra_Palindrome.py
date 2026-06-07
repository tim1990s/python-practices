# Chương trình kiểm tra số palindrome

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số nguyên: "))
chuoi = str(abs(n))
la_palindrome = True

for i in range(len(chuoi) // 2):
    if chuoi[i] != chuoi[len(chuoi) - 1 - i]:
        la_palindrome = False
        break

if la_palindrome:
    print(n, "là số palindrome")
else:
    print(n, "không phải là số palindrome")
