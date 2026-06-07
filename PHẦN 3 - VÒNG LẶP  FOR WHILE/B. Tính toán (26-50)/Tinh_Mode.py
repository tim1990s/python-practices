# Chương trình tính mode của dãy số

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

n = int(input("Nhập số lượng phần tử: "))

if n <= 0:
    print("Số lượng phần tử phải lớn hơn 0")
else:
    ds = []

    for i in range(1, n + 1):
        so = float(input("Nhập số thứ " + str(i) + ": "))
        ds.append(so)

    mode = ds[0]
    tan_suat_lon_nhat = 0

    for so in ds:
        tan_suat = 0

        for gia_tri in ds:
            if gia_tri == so:
                tan_suat += 1

        if tan_suat > tan_suat_lon_nhat:
            tan_suat_lon_nhat = tan_suat
            mode = so

    print("Mode là:", mode)
    print("Tần suất:", tan_suat_lon_nhat)
