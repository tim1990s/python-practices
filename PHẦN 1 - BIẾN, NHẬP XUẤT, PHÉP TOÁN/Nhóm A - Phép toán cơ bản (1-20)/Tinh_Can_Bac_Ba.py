# Chương trình tính căn bậc ba
#
# Căn bậc ba của n là số mà khi nhân với chính nó 3 lần sẽ bằng n.
#
# Công thức:
# can_bac_ba = n ** (1 / 3)
#
# Ví dụ:
# Nếu n = 27 thì:
# Căn bậc ba của 27 là 3
#
# Ý tưởng:
# - Nhập số n.
# - Nếu n không âm thì tính n ** (1 / 3).
# - Nếu n âm thì lấy căn bậc ba của giá trị dương rồi đổi dấu.
# - In kết quả ra màn hình.

n = float(input("Nhập số n: "))

if n >= 0:
    can_bac_ba = n ** (1 / 3)
else:
    can_bac_ba = -((-n) ** (1 / 3))

print("Căn bậc ba của", n, "là:", can_bac_ba)
