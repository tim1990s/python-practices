# Chương trình tính căn bậc hai
#
# Căn bậc hai của n là số mà khi nhân với chính nó sẽ bằng n.
#
# Công thức:
# can_bac_hai = sqrt(n)
#
# Ví dụ:
# Nếu n = 16 thì:
# Căn bậc hai của 16 là 4
#
# Ý tưởng:
# - Nhập số n.
# - Kiểm tra n có âm hay không.
# - Nếu n âm thì không tính căn bậc hai trong phạm vi số thực.
# - Nếu n không âm thì dùng math.sqrt(n).
# - In kết quả ra màn hình.

import math

n = float(input("Nhập số n: "))

if n < 0:
    print("Không thể tính căn bậc hai của số âm trong phạm vi số thực")
else:
    can_bac_hai = math.sqrt(n)
    print("Căn bậc hai của", n, "là:", can_bac_hai)
