# Chương trình tính tỷ lệ đậu/rớt
#
# Tỷ lệ đậu cho biết số học sinh đậu chiếm bao nhiêu phần trăm tổng số học sinh.
# Tỷ lệ rớt cho biết số học sinh rớt chiếm bao nhiêu phần trăm tổng số học sinh.
#
# Công thức:
# ty_le_dau = so_luong_dau / tong_so * 100
# ty_le_rot = so_luong_rot / tong_so * 100
#
# Ý tưởng:
# - Nhập tổng số học sinh.
# - Nhập số học sinh đậu.
# - Tính số học sinh rớt.
# - Tính tỷ lệ đậu và tỷ lệ rớt.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

tong_so = int(input("Nhập tổng số học sinh: "))
so_luong_dau = int(input("Nhập số học sinh đậu: "))

if tong_so <= 0:
    print("Tổng số học sinh phải lớn hơn 0")
elif so_luong_dau < 0 or so_luong_dau > tong_so:
    print("Số học sinh đậu phải từ 0 đến tổng số học sinh")
else:
    so_luong_rot = tong_so - so_luong_dau
    ty_le_dau = so_luong_dau / tong_so * 100
    ty_le_rot = so_luong_rot / tong_so * 100

    print("Số học sinh rớt là:", so_luong_rot)
    print("Tỷ lệ đậu là:", ty_le_dau, "%")
    print("Tỷ lệ rớt là:", ty_le_rot, "%")
