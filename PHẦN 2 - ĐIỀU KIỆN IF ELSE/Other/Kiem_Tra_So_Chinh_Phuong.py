# Chương trình kiểm tra số chính phương
#
# Số chính phương là số có thể viết dưới dạng bình phương
# của một số nguyên.
#
# Ví dụ:
# 0 = 0 * 0
# 1 = 1 * 1
# 4 = 2 * 2
# 9 = 3 * 3
# 16 = 4 * 4
#
# Ý tưởng:
# - Tính căn bậc hai của số n.
# - Nếu căn bậc hai là một số nguyên thì n là số chính phương.
# - Ngược lại thì không phải.

import math
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

du_lieu = input("Nhập số cần kiểm tra: ").strip().replace(chr(65279), "")
n = int(du_lieu)

if n < 0:
    print("Số âm không phải là số chính phương")
else:
    can_bac_hai = int(math.sqrt(n))

    if can_bac_hai * can_bac_hai == n:
        print(n, "là số chính phương")
    else:
        print(n, "không phải là số chính phương")
