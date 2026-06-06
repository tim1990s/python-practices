# Python 101 Curriculum As Code

Repository này là một dự án mẫu để xây dựng giáo trình Python từ cơ bản đến
trung cấp theo hướng:

- Curriculum as Code
- Specification Driven Development
- Documentation Generation

Mục tiêu chính là tách rõ đặc tả và nội dung sinh ra. Người biên soạn chỉnh sửa
curriculum trong `specs/`, sau đó chạy generator để tái tạo lesson, exercise,
solution và example trong `generated/`.

## Cấu trúc thư mục

```text
project-root/
├── README.md
├── specs/
│   ├── curriculum/
│   │   ├── 01-basic-math.md
│   │   ├── 02-condition-if-else.md
│   │   ├── 03-loop.md
│   │   ├── 04-string.md
│   │   ├── 05-list.md
│   │   └── 06-function.md
│   ├── generation-rules.md
│   └── lesson-template.md
├── generated/
│   ├── lessons/
│   ├── exercises/
│   ├── solutions/
│   └── examples/
└── tools/
    └── generate.py
```

## Mục tiêu dự án

Dự án cung cấp một pipeline đơn giản nhưng đầy đủ để biến curriculum specs thành
tài liệu học tập. Mỗi bài học được sinh theo cùng một template, có lý thuyết,
nền tảng toán học, đề bài, ví dụ, thuật toán, pseudocode, lời giải Python, giải
thích code, phân tích complexity, lỗi thường gặp và bài tập mở rộng.

Repository hiện có 6 module:

- Basic Math
- Condition If Else
- Loop
- String
- List
- Function

Mỗi module có 5 bài tập, tổng cộng 30 bài. File specs không chứa lời giải; lời
giải được sinh riêng vào `generated/solutions/`.

## Quy trình sinh nội dung

Chạy lệnh:

```bash
python tools/generate.py
```

Generator sẽ:

- đọc tất cả file Markdown trong `specs/curriculum/`;
- parse exercise catalog dạng JSON trong từng spec;
- kiểm tra field bắt buộc, id trùng và slug trùng;
- tái tạo các thư mục trong `generated/`;
- sinh lesson Markdown trong `generated/lessons/`;
- sinh exercise statement trong `generated/exercises/`;
- sinh Python solution trong `generated/solutions/`;
- sinh sample example trong `generated/examples/`;
- kiểm tra mỗi lesson có tối thiểu 1000 từ;
- compile từng solution để bắt lỗi cú pháp.

## Cách mở rộng curriculum

Để thêm module mới:

1. Tạo file mới trong `specs/curriculum/`, ví dụ
   `07-dictionary.md`.
2. Viết các phần mô tả bắt buộc: mục tiêu học tập, kiến thức Python, dạng bài,
   độ khó, kiến thức tiên quyết.
3. Thêm exercise catalog dạng JSON trong code fence `json`.
4. Đảm bảo mỗi bài có `id` và `slug` chưa dùng.
5. Cập nhật `tools/generate.py` nếu module mới cần phần theory riêng hoặc dạng
   solution mới.
6. Chạy lại `python tools/generate.py`.

## Cách thêm bài tập mới

Trong file module tương ứng, thêm một object mới vào JSON catalog với các field:

- `id`
- `slug`
- `title`
- `module`
- `difficulty`
- `exercise_type`
- `prerequisites`
- `python_topics`
- `math_topics`
- `problem`
- `input`
- `output`
- `sample_input`
- `sample_output`
- `sample_explanation`

Specs chỉ mô tả bài toán, không viết lời giải trực tiếp. Nếu bài mới thuộc một
dạng solution chưa có, thêm strategy tương ứng trong `tools/generate.py`, gồm
algorithm steps, pseudocode và Python solution template.

## Cách tái sinh lesson

Sau khi sửa specs hoặc generator, chạy:

```bash
python tools/generate.py
```

Không chỉnh sửa thủ công các file trong `generated/` nếu muốn giữ workflow
Specification Driven Development. Khi cần thay đổi nội dung học, hãy sửa nguồn
đúng nơi:

- sửa cấu trúc lesson trong `specs/lesson-template.md`;
- sửa luật chất lượng trong `specs/generation-rules.md`;
- sửa danh sách bài trong `specs/curriculum/`;
- sửa logic sinh file trong `tools/generate.py`.

## Kiểm tra nhanh solution

Mỗi file solution là một chương trình Python độc lập. Ví dụ:

```bash
python generated/solutions/001-sum-two-numbers.py
```

Sau đó nhập:

```text
3 5
```

Kết quả mong đợi:

```text
8
```

## Ghi chú thiết kế

Thiết kế hiện tại cố tình đơn giản để phù hợp với lớp Python nhập môn. Specs là
nguồn sự thật cho curriculum, còn generator giữ các quy tắc biến đặc tả thành
nội dung học tập có cấu trúc. Khi giáo trình lớn hơn, có thể thay JSON catalog
bằng YAML hoặc một schema riêng, thêm test runner, thêm CI, hoặc xuất ra HTML và
PDF từ Markdown.
