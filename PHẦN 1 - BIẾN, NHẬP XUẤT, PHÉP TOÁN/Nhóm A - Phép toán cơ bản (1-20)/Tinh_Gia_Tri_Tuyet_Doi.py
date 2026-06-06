# Chương trình tính giá trị tuyệt đối
#
# Giá trị tuyệt đối của một số là khoảng cách từ số đó đến số 0 trên trục số.
#
# Công thức:
# gia_tri_tuyet_doi = abs(n)
#
# Ví dụ:
# abs(-5) = 5
# abs(7) = 7
#
# Ý tưởng:
# - Nhập số n.
# - Dùng hàm abs(n) để tính giá trị tuyệt đối.
# - In kết quả ra màn hình.

n = float(input("Nhập số n: "))

gia_tri_tuyet_doi = abs(n)

print("Giá trị tuyệt đối của", n, "là:", gia_tri_tuyet_doi)
