# Python Practices

Kho bài luyện tập Python được tổ chức theo từng chủ đề, đi từ nền tảng nhập xuất, phép toán, điều kiện, vòng lặp, xử lý chuỗi đến lập trình hướng đối tượng. Mục tiêu của repo là giúp người học có một bộ bài thực hành rõ ràng, dễ chạy, dễ tra cứu và có thể học theo lộ trình tăng dần độ khó.

Repo này không phải là một thư viện Python để cài bằng `pip`. Đây là bộ sưu tập bài tập thực hành, mỗi bài thường nằm trong một file `.py` riêng để người học có thể mở, đọc yêu cầu, chạy thử và chỉnh sửa độc lập.

## Repo Này Cung Cấp Gì?

- Bộ bài Python nền tảng theo từng phần học, phù hợp cho người mới bắt đầu hoặc người muốn ôn lại cú pháp.
- Hệ thống bài tập nhỏ, độc lập, dễ chạy trực tiếp bằng terminal hoặc PyCharm.
- Các nhóm bài có mục tiêu rõ ràng: tính toán, hình học, chuyển đổi đơn vị, tài chính, điều kiện, vòng lặp, chữ số, mẫu hình, chuỗi, regex và OOP.
- File `CheckList.md` để theo dõi toàn bộ kế hoạch bài tập và trạng thái hoàn thành.
- Thư mục OOP có tài liệu, ví dụ chạy được và 10 bài starter để tự thiết kế class.
- Một số bài luyện thêm trong `Other/`, bao gồm bài HackerRank và các file bổ sung.

## Đối Tượng Phù Hợp

- Người mới học Python và cần nhiều bài nhỏ để luyện cú pháp.
- Người đang học nhập xuất, biến, toán tử, `if/else`, `for`, `while`, `string`, `regex` và OOP.
- Người muốn có một repo mẫu để luyện tư duy chia bài theo chủ đề.
- Người cần tài liệu tham khảo nhanh về cách tổ chức bài tập Python cơ bản.

## Yêu Cầu Môi Trường

- Python 3.x.
- Không cần cài thư viện ngoài cho các bài hiện có. Các import đang dùng đều thuộc Python standard library như `math`, `random`, `re`, `json`, `csv`, `html`, `collections`, `dataclasses`, `abc`, `urllib`, `email`, `xml`.
- Có thể chạy bằng terminal, PowerShell, Command Prompt, PyCharm hoặc IDE Python bất kỳ.

Kiểm tra Python:

```bash
python --version
```

## Cấu Trúc Tổng Quan

```text
Python Practices/
|-- README.md
|-- CheckList.md
|-- .gitignore
|
|-- PHẦN 1 - BIẾN, NHẬP XUẤT, PHÉP TOÁN/
|   |-- Nhóm A - Phép toán cơ bản (1-20)/
|   |-- Nhóm B - Hình học cơ bản (21-40)/
|   |-- Nhóm C - Chuyển đổi đơn vị (41-60)/
|   |-- Nhóm D - Tài chính (61-80)/
|   |-- Nhóm E - Thời gian và tuổi tác (81-90)/
|   |-- Nhóm F - Công thức ứng dụng (91-100)/
|
|-- PHẦN 2 - ĐIỀU KIỆN IF ELSE/
|   |-- A. Kiểm tra số (1-25)/
|   |-- B. Hình học (26-50)/
|   |-- C. Phương trình (51-70)/
|   |-- D. Thực tế (71-100)/
|   |-- Other/
|
|-- PHẦN 3 - VÒNG LẶP  FOR WHILE/
|   |-- A. Vòng lặp cơ bản (1-25)/
|   |-- B. Tính toán (26-50)/
|   |-- C. Chữ số (51-75)/
|   |-- D. Mẫu hình (76-100)/
|
|-- PHẦN 4 - CHUỖI STRING/
|   |-- A. Cơ bản (1-25)/
|   |-- B. Phân tích văn bản (26-50)/
|   |-- C. Regex (51-75)/
|   |-- D. Nâng cao (76-100)/
|
|-- PHẦN 5 - HƯỚNG ĐỐI TƯỢNG/
|   |-- README.md
|   |-- docs/
|   |-- examples/
|   |-- exercises/
|
|-- Other/
|   |-- HackerRank/
|   |-- Practices/
```

Các thư mục `.venv/`, `.idea/`, `__pycache__/` và `Other/Practices/` không được xem là nội dung học chính và đã được cấu hình trong `.gitignore`.

## Tiến Độ Hiện Tại

| Khu vực | Nội dung chính | Trạng thái |
| --- | --- | --- |
| Phần 1 | Biến, nhập xuất, phép toán | Đã có 100 bài Python |
| Phần 2 | Điều kiện `if/else` | Đã có bộ bài chính và bài bổ sung |
| Phần 3 | Vòng lặp `for/while` | Đã có 100 bài Python |
| Phần 4 | Chuỗi, phân tích văn bản, regex, thuật toán chuỗi | Đã có 100 bài Python |
| Phần 5 | Hướng đối tượng | Đã có tài liệu, ví dụ và 10 bài starter |
| Other | HackerRank và bài luyện bổ sung | Có một số bài rời |
| CheckList.md | Kế hoạch tổng thể và trạng thái bài | Đang là nguồn theo dõi chính |

Lưu ý: `CheckList.md` còn chứa kế hoạch dài hạn cho các phần List và Function. Cây thư mục hiện tại đang có `PHẦN 5 - HƯỚNG ĐỐI TƯỢNG`, nên README này mô tả theo trạng thái thực tế của repo tại thời điểm cập nhật.

## Cách Chạy Bài Tập

Mở terminal tại thư mục gốc của repo:

```bash
cd "C:\Users\mrphu\OneDrive\Desktop\Python Practices"
```

Chạy một file bất kỳ:

```bash
python "PHẦN 1 - BIẾN, NHẬP XUẤT, PHÉP TOÁN/Nhóm A - Phép toán cơ bản (1-20)/Tinh_Tong.py"
```

Ví dụ chạy bài điều kiện:

```bash
python "PHẦN 2 - ĐIỀU KIỆN IF ELSE/A. Kiểm tra số (1-25)/Kiem_Tra_So_Chan.py"
```

Ví dụ chạy bài vòng lặp:

```bash
python "PHẦN 3 - VÒNG LẶP  FOR WHILE/B. Tính toán (26-50)/Giai_Thua.py"
```

Ví dụ chạy bài chuỗi:

```bash
python "PHẦN 4 - CHUỖI STRING/C. Regex (51-75)/Kiem_Tra_Email.py"
```

Ví dụ chạy demo OOP:

```bash
python "PHẦN 5 - HƯỚNG ĐỐI TƯỢNG/examples/oop_examples.py"
```

Do tên thư mục có khoảng trắng và tiếng Việt, nên luôn đặt đường dẫn trong dấu nháy kép khi chạy bằng PowerShell hoặc terminal.

## Cách Học Đề Xuất

1. Bắt đầu từ Phần 1 nếu bạn chưa chắc về biến, nhập dữ liệu, ép kiểu và phép toán.
2. Chuyển sang Phần 2 để luyện cách đặt điều kiện, chia nhánh và xử lý nhiều trường hợp.
3. Học Phần 3 để thành thạo lặp, tích lũy kết quả, duyệt chữ số, sinh dãy và in mẫu hình.
4. Học Phần 4 để luyện xử lý chuỗi, phân tích văn bản, regex và thuật toán tìm kiếm chuỗi.
5. Học Phần 5 khi đã biết function, list và muốn chuyển sang tư duy thiết kế object.
6. Dùng `CheckList.md` để biết bài nào đã có, bài nào thuộc kế hoạch tiếp theo.

## Chi Tiết Từng Phần

### Phần 1 - Biến, Nhập Xuất, Phép Toán

Mục tiêu chính của phần này là xây nền móng Python cơ bản. Người học luyện cách nhập dữ liệu bằng `input()`, chuyển kiểu dữ liệu, lưu giá trị vào biến, dùng toán tử số học và in kết quả bằng `print()`.

Phần này phù hợp với người mới bắt đầu vì mỗi bài thường chỉ tập trung vào một công thức hoặc một thao tác tính toán cụ thể.

| Nhóm | Mục tiêu | Người học luyện được gì |
| --- | --- | --- |
| Nhóm A - Phép toán cơ bản | Làm quen với cộng, trừ, nhân, chia, chia dư, lũy thừa, căn, trung bình, hoán đổi biến | Cú pháp biến, toán tử, ép kiểu, công thức đơn giản |
| Nhóm B - Hình học cơ bản | Áp dụng công thức chu vi, diện tích, thể tích cho các hình phổ biến | Biến đổi công thức toán học thành code Python |
| Nhóm C - Chuyển đổi đơn vị | Chuyển đổi độ dài, khối lượng, thời gian, dữ liệu, tiền tệ | Tư duy tỷ lệ, nhân chia hệ số, đặt tên biến rõ nghĩa |
| Nhóm D - Tài chính | Tính lãi đơn, lãi kép, VAT, giảm giá, lợi nhuận, tiền điện, tiền lương | Phần trăm, công thức thực tế, xử lý số tiền |
| Nhóm E - Thời gian và tuổi tác | Tính tuổi, số ngày/tháng/giờ đã sống, đổi đơn vị thời gian | Làm việc với công thức thời gian đơn giản |
| Nhóm F - Công thức ứng dụng | Tính vận tốc, quãng đường, BMI, BMR, điểm trung bình, mật độ dân số | Áp dụng Python vào bài toán đời sống |

Sau phần này, người học nên nắm được cách viết một chương trình Python nhỏ theo luồng: nhập dữ liệu, xử lý, xuất kết quả.

### Phần 2 - Điều Kiện If Else

Mục tiêu chính của phần này là luyện tư duy rẽ nhánh. Thay vì chỉ tính theo một công thức cố định, người học phải xác định điều kiện nào đúng, điều kiện nào sai và chương trình cần xử lý ra sao trong từng trường hợp.

| Nhóm | Mục tiêu | Người học luyện được gì |
| --- | --- | --- |
| A. Kiểm tra số | Kiểm tra chẵn/lẻ, âm/dương, chia hết, chính phương, nguyên tố, hoàn hảo, Armstrong, đối xứng, tăng giảm chữ số | Biểu thức điều kiện, toán tử so sánh, toán tử logic, kiểm tra trường hợp biên |
| B. Hình học | Kiểm tra tam giác, phân loại hình, điểm nằm trong vùng, góc, song song, vuông góc, so sánh diện tích/chu vi | Điều kiện hình học, kết hợp nhiều điều kiện, validate dữ liệu |
| C. Phương trình | Giải phương trình bậc nhất, bậc hai, hệ phương trình, bất phương trình, xét delta, điều kiện nghiệm | Chia trường hợp toán học, xử lý nghiệm đặc biệt, kiểm tra tập xác định |
| D. Thực tế | Xếp loại học lực, tính tiền điện/nước/internet, thuế, bảo hiểm, tuổi lao động, validate email/mật khẩu/số điện thoại/CCCD | Áp dụng `if/elif/else` vào nghiệp vụ gần thực tế |
| Other | Các bài bổ sung như giải phương trình, kiểm tra số chính phương, tính tổng | Bài luyện thêm ngoài nhóm chính |

Sau phần này, người học nên biết cách viết chương trình có nhiều nhánh xử lý và biết kiểm tra dữ liệu đầu vào trước khi tính toán.

### Phần 3 - Vòng Lặp For While

Mục tiêu chính của phần này là luyện xử lý lặp lại. Người học sẽ dùng `for`, `while`, biến đếm, biến tích lũy, điều kiện dừng và vòng lặp lồng nhau.

| Nhóm | Mục tiêu | Người học luyện được gì |
| --- | --- | --- |
| A. Vòng lặp cơ bản | In dãy số, số chẵn/lẻ, bảng cửu chương, Fibonacci, số nguyên tố, ký tự, ASCII, mẫu sao đơn giản | `range()`, biến đếm, duyệt dãy, điều kiện trong vòng lặp |
| B. Tính toán | Tổng dãy, giai thừa, lũy thừa, Fibonacci thứ n, xấp xỉ PI/e/sin/cos/tan/log, trung bình, max/min, variance, median, mode | Biến tích lũy, thuật toán tính dần, xử lý thống kê cơ bản |
| C. Chữ số | Đếm chữ số, tổng/tích chữ số, đảo số, palindrome, tìm chữ số đầu/cuối, chuyển hệ cơ số, đếm bit | Vòng lặp `while`, chia lấy dư, xử lý từng chữ số |
| D. Mẫu hình | In hình vuông, tam giác, kim tự tháp, kim cương, chữ cái, bàn cờ, Pascal, Floyd, zigzag, xoắn ốc | Vòng lặp lồng nhau, căn chỉnh output, tư duy hàng/cột |

Sau phần này, người học nên hiểu cách thiết kế thuật toán lặp và biết khi nào dùng `for`, khi nào dùng `while`.

### Phần 4 - Chuỗi String

Mục tiêu chính của phần này là luyện xử lý dữ liệu văn bản. Đây là phần quan trọng vì chuỗi xuất hiện trong hầu hết chương trình thực tế: nhập liệu người dùng, log, email, URL, file cấu hình, dữ liệu web và dữ liệu text.

| Nhóm | Mục tiêu | Người học luyện được gì |
| --- | --- | --- |
| A. Cơ bản | Đếm ký tự, đếm từ, in hoa/thường, capitalize, đảo chuỗi, palindrome, ghép/tách/cắt/thay thế chuỗi, trim, tìm kiếm, mã hóa Caesar/ROT13 | Index, slicing, method của string, thao tác text cơ bản |
| B. Phân tích văn bản | Đếm nguyên âm/phụ âm/số/ký tự đặc biệt, tìm từ dài/ngắn, tần suất từ/ký tự, token, n-gram, hashtag, mention, URL, email, số điện thoại, ngày tháng, tiền tệ, IP, Unicode | Tách và phân tích văn bản, thống kê text, chuẩn hóa dữ liệu |
| C. Regex | Kiểm tra email, URL, IPv4/IPv6, CCCD, số điện thoại, biển số, mã số thuế, password, tìm số/ngày/tiền/hashtag/mention, parse log/CSV/JSON/XML/Markdown/SQL/query/User-Agent/email header | Dùng `re`, thiết kế pattern, validate và extract dữ liệu |
| D. Nâng cao | Levenshtein, Similarity, Fuzzy Search, Anagram, KMP, Rabin-Karp, Boyer-Moore, Trie, Autocomplete, Spell Check, Search Engine mini, parser, template, slug, HTML escape/unescape | Thuật toán chuỗi, cấu trúc dữ liệu text, xử lý văn bản nâng cao |

Sau phần này, người học nên biết cách xử lý text từ đơn giản đến nâng cao và có nền tảng tốt để học xử lý dữ liệu, web scraping hoặc backend validation.

### Phần 5 - Hướng Đối Tượng

Mục tiêu chính của phần này là chuyển từ tư duy viết script tuần tự sang tư duy thiết kế object. Người học sẽ học cách nhóm dữ liệu và hành vi vào class, tạo object, quản lý trạng thái và thiết kế quan hệ giữa các đối tượng.

Cấu trúc phần này:

| Thư mục/file | Vai trò |
| --- | --- |
| `PHẦN 5 - HƯỚNG ĐỐI TƯỢNG/README.md` | Giới thiệu riêng cho phần OOP và lộ trình học 7 ngày |
| `docs/oop_python_guide.md` | Tài liệu lý thuyết OOP Python |
| `examples/oop_examples.py` | Ví dụ có thể chạy trực tiếp để quan sát class/object hoạt động |
| `exercises/README.md` | Mô tả 10 bài tập OOP, mục tiêu kiến thức và gợi ý thiết kế |
| `exercises/*.py` | Starter code để người học tự hoàn thiện, không phải lời giải sẵn |

10 bài OOP hiện có:

| Bài | Chủ đề | Kiến thức chính |
| --- | --- | --- |
| `01_student.py` | Quản lý học sinh | Class, object, instance attribute, method |
| `02_bank_account.py` | Tài khoản ngân hàng | Encapsulation, private attribute, `@property`, validation |
| `03_shapes.py` | Rectangle và Circle | Method, abstraction cơ bản, `__str__` |
| `04_library.py` | Quản lý thư viện | Composition, list object, quản lý trạng thái |
| `05_employee_management.py` | Nhân viên, quản lý, lập trình viên | Inheritance, overriding, `super()`, polymorphism |
| `06_shopping_cart.py` | Giỏ hàng | Composition, aggregation, `__len__` |
| `07_login_system.py` | User và AdminUser | Encapsulation, inheritance, class method, quyền quản trị |
| `08_game_characters.py` | Nhân vật game | Inheritance, polymorphism, overriding |
| `09_order_management.py` | Quản lý đơn hàng | Dataclass, composition, magic method |
| `10_school_management.py` | Mini project trường học | Tổng hợp OOP, nhiều class liên kết với nhau |

Sau phần này, người học nên biết cách nhận diện thực thể, thuộc tính, hành vi và quan hệ giữa class trong một bài toán thực tế.

### Other

Thư mục `Other/` chứa nội dung ngoài lộ trình chính:

| Thư mục | Mục đích |
| --- | --- |
| `Other/HackerRank/` | Bài luyện từ HackerRank hoặc bài theo format thử thách lập trình |
| `Other/Practices/` | Khu vực luyện nháp hoặc nội dung không đưa vào repo chính, đang được ignore |

Ngoài ra, `PHẦN 2 - ĐIỀU KIỆN IF ELSE/Other/` chứa một số bài bổ sung liên quan đến điều kiện và phương trình.

## CheckList.md Dùng Để Làm Gì?

`CheckList.md` là file quản lý kế hoạch bài tập. File này cho biết:

- Mỗi phần dự kiến có những nhóm bài nào.
- Bài nào đã có trong repo bằng dấu `[x]`.
- Bài nào còn nằm trong kế hoạch bằng dấu `[ ]`.
- Quy tắc kiểm tra tiến độ, ví dụ không tính `.venv`, `sample.py`, `__pycache__` và `Other/Practices`.

Khi thêm bài mới, nên cập nhật `CheckList.md` để trạng thái repo luôn rõ ràng.

## Cách Đọc Một Bài `.py`

Một bài trong repo thường nên được đọc theo thứ tự:

1. Tên file để biết bài giải quyết vấn đề gì.
2. Phần comment đầu file nếu có, thường mô tả bài toán, công thức hoặc ý tưởng.
3. Phần nhập dữ liệu để biết chương trình yêu cầu người dùng nhập gì.
4. Phần xử lý chính để hiểu thuật toán hoặc công thức.
5. Phần in kết quả để biết output mong đợi.

Ví dụ tên file:

```text
Tinh_Tong.py
Tinh_Lai_Kep.py
Kiem_Tra_So_Nguyen_To.py
Giai_Phuong_Trinh_Bac_hai.py
Dem_Ky_Tu.py
Kiem_Tra_Email.py
```

Tên file được viết bằng tiếng Việt không dấu, dùng dấu gạch dưới `_` để dễ đọc và tránh lỗi đường dẫn.

## Chuẩn Viết Một Bài Mới

Khi thêm bài mới, nên giữ cấu trúc đơn giản và thống nhất:

```python
# Tên chương trình
#
# Mô tả bài toán:
# - Chương trình cần làm gì?
# - Input gồm những gì?
# - Output cần in ra là gì?
#
# Công thức hoặc ý tưởng:
# - Bước 1: Nhập dữ liệu.
# - Bước 2: Xử lý dữ liệu.
# - Bước 3: In kết quả.

# Code Python bắt đầu từ đây
```

Quy ước nên giữ:

- Mỗi bài là một file `.py` độc lập.
- Không trộn nhiều bài không liên quan vào cùng một file.
- Tên file dùng tiếng Việt không dấu và dấu gạch dưới `_`.
- Nếu bài có công thức, ghi công thức trong comment.
- Nếu bài có nhiều nhánh xử lý, ghi rõ từng trường hợp.
- Nếu dùng thuật toán khó, thêm comment ngắn giải thích ý tưởng.
- Không cần dùng thư viện ngoài nếu bài có thể giải bằng Python standard library.

## Quy Ước Tổ Chức Thư Mục

- Tên phần lớn viết theo dạng `PHẦN X - TÊN CHỦ ĐỀ`.
- Bên trong mỗi phần có nhóm nhỏ theo khoảng bài, ví dụ `(1-25)`, `(26-50)`.
- Mỗi nhóm gom các bài có cùng mục tiêu kiến thức.
- File `sample.py` nếu có chỉ nên xem là file thử nghiệm hoặc mẫu, không phải bài chính trong checklist.
- `__pycache__/` là cache do Python tạo ra khi chạy code, không phải nội dung học.
- `.venv/` là môi trường ảo local, không phải nội dung bài tập.
- `.idea/` là cấu hình IDE local, không phải nội dung học.

## Lộ Trình Nâng Cấp Repo

Các hướng phát triển tự nhiên của repo:

1. Hoàn thiện thêm phần List theo kế hoạch trong `CheckList.md`.
2. Hoàn thiện thêm phần Function theo kế hoạch trong `CheckList.md`.
3. Bổ sung test case hoặc input/output mẫu cho từng bài.
4. Chuẩn hóa comment đầu file cho toàn bộ bài.
5. Thêm hướng dẫn chạy hàng loạt bài hoặc kiểm tra syntax tự động.
6. Tách bài starter và bài lời giải nếu repo muốn hỗ trợ cả tự luyện và tham khảo đáp án.

## Ghi Chú Quan Trọng

- Nguồn theo dõi tiến độ chính là `CheckList.md`.
- README này mô tả mục tiêu học, cấu trúc repo và cách sử dụng tổng thể.
- Các bài trong repo ưu tiên tính dễ hiểu, dễ chạy, phù hợp cho luyện tập hơn là tối ưu hóa phức tạp.
- Khi dùng trên Windows, nên đặt đường dẫn trong dấu nháy kép vì tên thư mục có khoảng trắng và ký tự tiếng Việt.
