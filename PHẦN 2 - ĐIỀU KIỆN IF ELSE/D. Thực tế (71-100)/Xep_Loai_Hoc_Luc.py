# Chương trình xếp loại học lực

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

diem = float(input("Nhập điểm trung bình: "))

if diem < 0 or diem > 10:
    print("Điểm trung bình phải từ 0 đến 10")
elif diem >= 8.5:
    print("Học lực giỏi")
elif diem >= 7:
    print("Học lực khá")
elif diem >= 5:
    print("Học lực trung bình")
else:
    print("Học lực yếu")
