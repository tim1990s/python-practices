# Chương trình tính BMI
#
# BMI là chỉ số khối cơ thể, thường dùng để đánh giá cân nặng so với chiều cao.
#
# Công thức:
# bmi = can_nang / (chieu_cao * chieu_cao)
#
# Trong đó:
# - can_nang tính bằng kg.
# - chieu_cao tính bằng mét.
#
# Ý tưởng:
# - Nhập cân nặng.
# - Nhập chiều cao.
# - Kiểm tra cân nặng và chiều cao phải lớn hơn 0.
# - Tính BMI và in kết quả ra màn hình.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

if can_nang <= 0 or chieu_cao <= 0:
    print("Cân nặng và chiều cao phải lớn hơn 0")
else:
    bmi = can_nang / (chieu_cao * chieu_cao)
    print("Chỉ số BMI là:", bmi)
