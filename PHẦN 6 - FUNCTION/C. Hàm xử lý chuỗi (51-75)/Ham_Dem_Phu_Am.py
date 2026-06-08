# Chương trình hàm đếm phụ âm
#
# Yêu cầu:
# - Viết hàm đếm số phụ âm trong chuỗi.
# - Viết logic chính trong một hoặc nhiều hàm.
# - Nhập dữ liệu từ bàn phím và in kết quả rõ ràng.
#
# Mô tả:
# Luyện viết hàm xử lý chuỗi: đảo chuỗi, chuẩn hóa, validate, parse, tìm kiếm, thống kê và biến đổi văn bản.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Duyệt từng ký tự.
# - Chỉ xét ký tự chữ cái.
# - Loại các nguyên âm để đếm phụ âm.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def dem_phu_am(chuoi):
    nguyen_am = "aeiouAEIOUáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ"
    return sum(1 for ky_tu in chuoi if ky_tu.isalpha() and ky_tu not in nguyen_am)


chuoi = input("Nhập chuỗi: ")
print("Số phụ âm:", dem_phu_am(chuoi))
