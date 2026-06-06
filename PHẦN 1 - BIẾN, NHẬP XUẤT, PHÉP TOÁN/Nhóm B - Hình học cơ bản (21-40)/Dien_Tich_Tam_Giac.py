# Chương trình tính diện tích tam giác
#
# Diện tích tam giác có thể tính khi biết độ dài đáy và chiều cao.
#
# Công thức:
# dien_tich = day * chieu_cao / 2
#
# Ví dụ:
# Nếu đáy = 10 và chiều cao = 6 thì:
# Diện tích = 10 * 6 / 2 = 30
#
# Ý tưởng:
# - Nhập độ dài đáy và chiều cao.
# - Kiểm tra cả hai giá trị phải lớn hơn 0.
# - Áp dụng công thức tính diện tích.
# - In kết quả ra màn hình.

day = float(input("Nhập độ dài đáy tam giác: "))
chieu_cao = float(input("Nhập chiều cao tam giác: "))

if day <= 0 or chieu_cao <= 0:
    print("Đáy và chiều cao phải lớn hơn 0")
else:
    dien_tich = day * chieu_cao / 2
    print("Diện tích tam giác là:", dien_tich)
