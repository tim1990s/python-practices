# Chương trình parse User-Agent đơn giản
#
# Yêu cầu:
# - Viết chương trình parse User-Agent đơn giản.
# - Nhập dữ liệu cần xử lý từ bàn phím.
# - In kết quả rõ ràng ra màn hình.
#
# Mô tả:
# Sử dụng regular expression hoặc parser chuẩn để kiểm tra, tìm kiếm, trích xuất hoặc phân tích chuỗi có cấu trúc.
#
# Ví dụ:
# - Input: dữ liệu mẫu phù hợp với yêu cầu của bài.
# - Output: kết quả xử lý tương ứng.
#
# Ý tưởng:
# - Đọc chuỗi hoặc văn bản đầu vào.
# - Xây dựng mẫu regex hoặc dùng parser phù hợp với định dạng dữ liệu.
# - In kết quả hợp lệ, không hợp lệ hoặc dữ liệu đã parse.

import sys

if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8-sig")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import re
ua = input("Nhập User-Agent: ")
if "Chrome/" in ua and "Edg/" not in ua:
    trinh_duyet = "Chrome"
elif "Firefox/" in ua:
    trinh_duyet = "Firefox"
elif "Edg/" in ua:
    trinh_duyet = "Edge"
elif "Safari/" in ua and "Chrome/" not in ua:
    trinh_duyet = "Safari"
else:
    trinh_duyet = "Không rõ"
he_dieu_hanh = "Không rõ"
if "Windows" in ua:
    he_dieu_hanh = "Windows"
elif "Mac OS X" in ua:
    he_dieu_hanh = "macOS"
elif "Android" in ua:
    he_dieu_hanh = "Android"
elif "Linux" in ua:
    he_dieu_hanh = "Linux"
tim_phien_ban = re.search(r"(?:Chrome|Firefox|Edg|Version)/(\d+(?:\.\d+)*)", ua)
print("Trình duyệt:", trinh_duyet)
print("Hệ điều hành:", he_dieu_hanh)
if tim_phien_ban:
    print("Phiên bản:", tim_phien_ban.group(1))
