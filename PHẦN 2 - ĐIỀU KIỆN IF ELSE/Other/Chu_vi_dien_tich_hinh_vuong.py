canh = float(input("Nhap do dai canh hinh vuong: "))
if canh <= 0:
    print("Do dai phai lon hon 0")
else:
    chu_vi = canh *4;
    dien_tich = canh * canh;

    print(f"Chu vi hinh vuong: {chu_vi}")
    print(f"Dien tich hinh vuong: {dien_tich}")
