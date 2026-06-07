# Chương trình tính chỉ số BMR
#
# BMR là lượng calo cơ thể cần để duy trì các hoạt động sống cơ bản.
#
# Công thức Mifflin-St Jeor:
# Nam: bmr = 10 * can_nang + 6.25 * chieu_cao - 5 * tuoi + 5
# Nữ:  bmr = 10 * can_nang + 6.25 * chieu_cao - 5 * tuoi - 161
#
# Trong đó:
# - can_nang tính bằng kg.
# - chieu_cao tính bằng cm.
# - tuoi tính bằng năm.
#
# Ý tưởng:
# - Nhập cân nặng, chiều cao, tuổi và giới tính.
# - Kiểm tra dữ liệu số phải lớn hơn 0.
# - Tính BMR theo giới tính.

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (cm): "))
tuoi = int(input("Nhập tuổi: "))
gioi_tinh = input("Nhập giới tính (nam/nu): ").lower()

if can_nang <= 0 or chieu_cao <= 0 or tuoi <= 0:
    print("Cân nặng, chiều cao và tuổi phải lớn hơn 0")
elif gioi_tinh == "nam":
    bmr = 10 * can_nang + 6.25 * chieu_cao - 5 * tuoi + 5
    print("Chỉ số BMR là:", bmr)
elif gioi_tinh == "nu":
    bmr = 10 * can_nang + 6.25 * chieu_cao - 5 * tuoi - 161
    print("Chỉ số BMR là:", bmr)
else:
    print("Giới tính chỉ được nhập là nam hoặc nu")
