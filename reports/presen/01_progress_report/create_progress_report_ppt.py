from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor

OUT = Path(__file__).with_name("progress_report.pptx")

# Palette: restrained academic navy with teal/amber signals.
NAVY = "071A2D"
NAVY_2 = "0D2942"
TEAL = "00A6A6"
TEAL_DARK = "007B7B"
BLUE = "2D6CDF"
AMBER = "F4B942"
RED = "D55454"
GREEN = "2E9B70"
INK = "102A43"
MUTED = "52677D"
LIGHT = "F5F8FB"
WHITE = "FFFFFF"
LINE = "D9E3EC"
PALE_TEAL = "E6F7F6"
PALE_BLUE = "EBF2FF"
PALE_AMBER = "FFF4D6"
PALE_RED = "FCEBEB"
PALE_SLATE = "EEF3F7"
FONT = "Arial"
MONO = "Consolas"


def rgb(value):
    value = value.lstrip("#")
    return RGBColor(int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16))


def rect(slide, x, y, w, h, fill, line=None, radius=False):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(y), Inches(w), Inches(h),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(fill)
    shape.line.color.rgb = rgb(line if line else fill)
    return shape


def line(slide, x1, y1, x2, y2, color=LINE, width=1.0):
    shape = slide.shapes.add_connector(1, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    shape.line.color.rgb = rgb(color)
    shape.line.width = Pt(width)
    return shape


def txt(slide, x, y, w, h, text, size=16, color=INK, bold=False,
        align=PP_ALIGN.LEFT, font=FONT, italic=False, valign=MSO_ANCHOR.TOP,
        margin=0.03):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(margin)
    tf.margin_right = Inches(margin)
    tf.margin_top = Inches(margin)
    tf.margin_bottom = Inches(margin)
    tf.vertical_anchor = valign
    for i, paragraph_text in enumerate(str(text).split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = paragraph_text
        p.alignment = align
        p.space_after = Pt(0)
        p.space_before = Pt(0)
        p.font.name = font
        p.font.size = Pt(size)
        p.font.bold = bold
        p.font.italic = italic
        p.font.color.rgb = rgb(color)
    return shape


def bullets(slide, x, y, w, h, items, size=15, color=INK, bullet_color=TEAL,
            gap=7, bullet_indent=0.18):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(0.02)
    tf.margin_right = Inches(0.02)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)
    for i, item in enumerate(items):
        if isinstance(item, tuple):
            label, text_value = item
            text_value = f"{label}  {text_value}"
        else:
            text_value = item
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = text_value
        p.level = 0
        p.font.name = FONT
        p.font.size = Pt(size)
        p.font.color.rgb = rgb(color)
        p.space_after = Pt(gap)
        p.bullet = True
        # python-pptx uses XML bullet defaults; prefix improves portability.
        p.text = "• " + p.text
    return shape


def card(slide, x, y, w, h, title, body, accent=TEAL, fill=WHITE,
         title_size=17, body_size=13.5, body_color=INK):
    rect(slide, x, y, w, h, fill, LINE, True)
    rect(slide, x, y, 0.07, h, accent, accent, True)
    txt(slide, x + 0.22, y + 0.16, w - 0.36, 0.34, title, title_size, INK, True)
    txt(slide, x + 0.22, y + 0.57, w - 0.38, h - 0.68, body, body_size, body_color)


def pill(slide, x, y, w, label, fill=PALE_TEAL, text_color=TEAL_DARK, size=11.5):
    rect(slide, x, y, w, 0.34, fill, fill, True)
    txt(slide, x, y + 0.04, w, 0.22, label, size, text_color, True, PP_ALIGN.CENTER)


def metric(slide, x, y, w, number, label, accent=TEAL, suffix=""):
    rect(slide, x, y, w, 1.22, WHITE, LINE, True)
    txt(slide, x + 0.15, y + 0.13, w - 0.3, 0.53, number + suffix, 27, accent, True, PP_ALIGN.CENTER)
    txt(slide, x + 0.15, y + 0.75, w - 0.3, 0.30, label, 11.5, INK, False, PP_ALIGN.CENTER)


def header(slide, title, kicker=None, n=None):
    rect(slide, 0, 0, 13.333, 7.5, LIGHT)
    rect(slide, 0, 0, 13.333, 0.16, TEAL)
    if kicker:
        txt(slide, 0.6, 0.37, 4.4, 0.2, kicker.upper(), 10.5, TEAL_DARK, True)
    txt(slide, 0.6, 0.63, 11.8, 0.55, title, 25, NAVY, True)
    line(slide, 0.6, 1.28, 12.73, 1.28, LINE, 0.8)
    txt(slide, 0.6, 7.15, 6.8, 0.16, "DAP391m · Báo cáo tiến độ dự án", 8.5, MUTED)
    if n is not None:
        txt(slide, 12.15, 7.12, 0.55, 0.18, f"{n:02d}", 8.5, MUTED, True, PP_ALIGN.RIGHT)


def add_arrow(slide, x, y, w, h, fill=TEAL):
    shape = slide.shapes.add_shape(MSO_SHAPE.CHEVRON, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(fill)
    shape.line.color.rgb = rgb(fill)
    return shape


def add_badge(slide, x, y, label, fill=TEAL):
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(0.38), Inches(0.38))
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(fill)
    shape.line.color.rgb = rgb(fill)
    txt(slide, x, y + 0.075, 0.38, 0.18, str(label), 10, WHITE, True, PP_ALIGN.CENTER)


def add_quote(slide, x, y, w, h, quote, rating, direction, accent):
    rect(slide, x, y, w, h, WHITE, LINE, True)
    rect(slide, x, y, w, 0.12, accent, accent, True)
    txt(slide, x + 0.28, y + 0.28, 0.42, 0.3, "“", 30, accent, True)
    txt(slide, x + 0.7, y + 0.36, w - 1.0, h - 1.12, quote, 14, INK, False, italic=True)
    pill(slide, x + 0.28, y + h - 0.55, 0.83, rating, PALE_AMBER if accent == AMBER else PALE_RED,
         NAVY, 11)
    txt(slide, x + 1.2, y + h - 0.49, w - 1.5, 0.2, direction, 11.5, accent, True)


prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

# 01 — title
s = prs.slides.add_slide(blank)
rect(s, 0, 0, 13.333, 7.5, NAVY)
rect(s, 0, 0, 0.18, 7.5, TEAL)
rect(s, 8.78, 0.0, 4.55, 7.5, NAVY_2)
for i, (x, y, r, col) in enumerate([(9.3, 1.0, 0.52, TEAL), (11.2, 1.8, 0.25, AMBER), (10.2, 4.5, 0.36, BLUE), (12.0, 5.2, 0.47, TEAL)]):
    shp = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y), Inches(r), Inches(r))
    shp.fill.solid(); shp.fill.fore_color.rgb = rgb(col); shp.line.color.rgb = rgb(col)
txt(s, 0.75, 0.9, 7.2, 0.3, "BÁO CÁO TIẾN ĐỘ DỰ ÁN", 14, "7EE5DC", True)
txt(s, 0.75, 1.52, 7.42, 1.45, "Bất nhất cảm xúc – điểm số\nở cấp khía cạnh", 31, WHITE, True)
txt(s, 0.75, 3.25, 7.15, 0.55, "Aspect-Level Sentiment–Rating Discrepancy in Online Hotel Reviews", 16, "C7D5E0", False, italic=True)
line(s, 0.75, 4.28, 6.8, 4.28, "4F6B80", 0.8)
txt(s, 0.75, 4.58, 6.6, 0.28, "Nhóm: [điền]  ·  Môn DAP391m  ·  [ngày báo cáo]", 13, "C7D5E0")
txt(s, 9.35, 2.65, 3.0, 0.36, "KHÁCH VIẾT", 15, "B8D9D9", True, PP_ALIGN.CENTER)
txt(s, 9.35, 3.14, 3.0, 0.6, "một đằng", 27, WHITE, True, PP_ALIGN.CENTER)
line(s, 9.82, 4.03, 11.9, 4.03, "4F6B80", 0.8)
txt(s, 9.35, 4.22, 3.0, 0.36, "NHƯNG CHẤM SAO", 15, "B8D9D9", True, PP_ALIGN.CENTER)
txt(s, 9.35, 4.69, 3.0, 0.6, "một nẻo", 27, "7EE5DC", True, PP_ALIGN.CENTER)

# 02 — agenda
s = prs.slides.add_slide(blank); header(s, "Lộ trình báo cáo", "Tổng quan", 2)
steps = [
    ("01", "Đề tài", "Hiện tượng cần giải thích"),
    ("02", "Khoảng trống", "Vì sao không thể coi là nhiễu"),
    ("03", "Câu hỏi", "Ba RQ và nhánh kỹ thuật"),
    ("04", "Phương pháp", "Ba tầng · năm bước"),
    ("05", "Khảo sát", "Kết quả và điểm dừng"),
    ("06", "Tiếp theo", "Việc mở và góp ý"),
    ("07", "Ứng dụng", "Bảng soát điểm sao"),
]
for i, (no, title, desc) in enumerate(steps):
    x = 0.65 + (i % 4) * 3.07
    y = 1.72 + (i // 4) * 2.1
    rect(s, x, y, 2.7, 1.55, WHITE, LINE, True)
    txt(s, x + 0.2, y + 0.17, 0.45, 0.24, no, 11, TEAL_DARK, True)
    txt(s, x + 0.2, y + 0.53, 2.15, 0.3, title, 17, NAVY, True)
    txt(s, x + 0.2, y + 0.94, 2.2, 0.35, desc, 11.5, MUTED)
    rect(s, x + 2.37, y + 0.2, 0.1, 1.1, TEAL, TEAL, True)
rect(s, 9.85, 3.95, 2.75, 1.1, PALE_TEAL, PALE_TEAL, True)
txt(s, 10.05, 4.16, 2.35, 0.23, "Thông điệp xuyên suốt", 10.5, TEAL_DARK, True, PP_ALIGN.CENTER)
txt(s, 10.05, 4.52, 2.35, 0.25, "Lệch pha là tín hiệu, không phải lỗi.", 13.5, NAVY, True, PP_ALIGN.CENTER)

# 03 — topic
s = prs.slides.add_slide(blank); header(s, "Đề tài: không khớp là một tín hiệu hành vi", "01 · Đề tài", 3)
txt(s, 0.78, 1.62, 7.4, 0.52, "Khách hàng để lại hai tín hiệu cùng lúc khi đánh giá khách sạn.", 20, NAVY, True)
card(s, 0.78, 2.42, 3.18, 1.7, "Văn bản tự do", "Kể lại trải nghiệm bằng ngôn ngữ tự nhiên: phòng, dịch vụ, tiện ích…", TEAL, WHITE, 18, 13.3)
card(s, 4.3, 2.42, 3.18, 1.7, "Điểm sao", "Chấm một đánh giá tổng thể từ 1 đến 5 sao.", AMBER, WHITE, 18, 13.3)
add_arrow(s, 7.85, 2.88, 0.64, 0.62, TEAL)
rect(s, 8.78, 1.74, 3.72, 3.1, NAVY, NAVY, True)
txt(s, 9.08, 2.1, 3.1, 0.24, "ĐIỂM XUẤT PHÁT", 10.5, "7EE5DC", True, PP_ALIGN.CENTER)
txt(s, 9.05, 2.56, 3.18, 1.15, "Viết một đằng\nnhưng chấm sao một nẻo", 23, WHITE, True, PP_ALIGN.CENTER)
txt(s, 9.2, 4.1, 2.9, 0.32, "Nhóm nghiên cứu chính những ca này,\nthay vì coi chúng là lỗi dữ liệu.", 11.5, "C7D5E0", False, PP_ALIGN.CENTER)
pill(s, 0.78, 5.18, 5.2, "Không phải mọi tín hiệu văn bản và điểm sao đều ăn khớp", PALE_BLUE, BLUE, 12)

# 04 — examples
s = prs.slides.add_slide(blank); header(s, "Hai hướng của sự không khớp", "01 · Ví dụ cụ thể", 4)
add_quote(s, 0.72, 1.67, 5.78, 3.75,
          "Phòng sạch, nhân viên thân thiện, nhưng điều hoà kêu rất to và wifi yếu. Nhìn chung vẫn là chỗ ổn.",
          "5 SAO", "Chê một số điểm · vẫn chấm cao", AMBER)
add_quote(s, 6.82, 1.67, 5.78, 3.75,
          "Vị trí tuyệt vời, phòng đẹp, ăn sáng ngon. Nhưng tiếng ồn buổi tối khiến tôi không ngủ được.",
          "2 SAO", "Khen nhiều điểm · vẫn chấm thấp", RED)
rect(s, 2.18, 5.74, 8.98, 0.67, PALE_TEAL, PALE_TEAL, True)
txt(s, 2.37, 5.93, 8.6, 0.22, "Cùng một kiểu “không khớp”, nhưng có hai chiều hành vi đối nghịch.", 15.5, NAVY, True, PP_ALIGN.CENTER)

# 05 — importance
s = prs.slides.add_slide(blank); header(s, "Vì sao hiện tượng này quan trọng?", "02 · Khoảng trống", 5)
card(s, 0.75, 1.64, 5.83, 3.98, "Đối với nghiên cứu",
     "• Nhiều mô hình cảm xúc dùng điểm sao làm nhãn huấn luyện.\n\n• Khi sao không phản ánh đúng văn bản, mô hình học từ nhãn yếu — và sai một cách âm thầm.\n\n• Các ca lệch thường bị coi là nhiễu để loại bỏ, thay vì đối tượng cần phân tích.",
     TEAL, WHITE, 20, 15)
card(s, 6.75, 1.64, 5.83, 3.98, "Đối với quản trị khách sạn",
     "• Nhìn được khía cạnh nào khách sẵn sàng bỏ qua.\n\n• Nhìn được khía cạnh nào có thể dìm toàn bộ điểm số.\n\n• Từ đó phân bổ nguồn lực đúng chỗ: sửa cơ sở vật chất hay đào tạo nhân viên.",
     AMBER, WHITE, 20, 15)
pill(s, 2.13, 5.94, 9.1, "Mục tiêu không phải “làm sạch” dữ liệu — mà là giải thích mẫu hành vi quan sát được.", PALE_BLUE, BLUE, 13)

# 06 — data
s = prs.slides.add_slide(blank); header(s, "Dữ liệu của nhóm cho thấy hiện tượng có thật", "02 · Bằng chứng ban đầu", 6)
txt(s, 0.78, 1.55, 11.8, 0.3, "TripAdvisor tiếng Anh · 2015–2023 · 9.990 review · 2.622 khách sạn", 17, NAVY, True)
metric(s, 0.78, 2.15, 2.75, "394", "Review 5 sao vẫn chứa phàn nàn tiêu cực", AMBER)
metric(s, 3.73, 2.15, 2.75, "199", "Review 1–2 sao vẫn chứa lời khen", RED)
metric(s, 6.68, 2.15, 2.75, "593", "Tổng số review đáng ngờ", TEAL)
metric(s, 9.63, 2.15, 2.75, "461", "Khách sạn có ca đáng ngờ", BLUE)
rect(s, 0.78, 3.85, 11.6, 1.25, PALE_TEAL, PALE_TEAL, True)
txt(s, 1.03, 4.08, 11.05, 0.28, "394 + 199 không phải chỉ là một vài dòng dữ liệu “lạ”; chúng tạo thành một mẫu hành vi có cấu trúc.", 18, NAVY, True, PP_ALIGN.CENTER)
txt(s, 0.8, 5.62, 11.5, 0.24, "Nguồn: tính trực tiếp trên data/TripAdvisor_EN.json, 22/09/2026. 199 ca được tính trên tổng 465 review 1–2 sao.", 11.5, MUTED, False, PP_ALIGN.CENTER)

# 07 — conventional approach
s = prs.slides.add_slide(blank); header(s, "Cách làm phổ biến hiện nay làm mất chiều hành vi", "02 · Vấn đề phương pháp", 7)
flow = [
    ("1", "Giả định", "Khen → 5 sao\nChê → 1 sao", PALE_BLUE, BLUE),
    ("2", "Xử lý lệch", "Coi là lỗi\nXoá khỏi tập huấn luyện", PALE_AMBER, AMBER),
    ("3", "Đo độ lệch", "|Điểm − Cảm xúc|\nTrị tuyệt đối", PALE_RED, RED),
]
for i, (num, title, body, fill, accent) in enumerate(flow):
    x = 0.8 + i * 4.05
    rect(s, x, 2.03, 3.25, 2.28, fill, fill, True)
    add_badge(s, x + 0.22, 2.25, num, accent)
    txt(s, x + 0.75, 2.27, 2.1, 0.28, title, 17, NAVY, True)
    txt(s, x + 0.28, 2.93, 2.63, 0.7, body, 15, INK, False, PP_ALIGN.CENTER)
    if i < 2:
        add_arrow(s, x + 3.42, 2.77, 0.42, 0.52, TEAL)
rect(s, 1.72, 5.05, 9.86, 0.82, NAVY, NAVY, True)
txt(s, 1.95, 5.29, 9.4, 0.3, "Trị tuyệt đối cho biết độ lớn — nhưng không cho biết khách cho thêm điểm hay dìm điểm.", 17, WHITE, True, PP_ALIGN.CENTER)

# 08 — root paper
s = prs.slides.add_slide(blank); header(s, "Kế thừa bài gốc — và phản biện ba điểm", "02 · Bài báo đối chuẩn", 8)
txt(s, 0.77, 1.55, 11.85, 0.28, "Le et al. (2026) · International Journal of Hospitality Management", 18, NAVY, True)
pill(s, 0.78, 2.02, 6.47, "Kế thừa: S-O-R · bối cảnh review khách sạn · tách khía cạnh · dữ liệu đối chuẩn", PALE_TEAL, TEAL_DARK, 11.5)
crit = [
    ("01", "Giả định đơn điệu", "Cảm xúc tích cực → điểm tăng; tiêu cực → điểm giảm. Nhưng không giải thích được 394 review 5 sao vẫn có phàn nàn.", RED),
    ("02", "Lập luận vòng ở Loyalty", "Câu “sẽ quay lại / khuyến khích” được dùng để giải thích chính điểm số — dùng vế lời giải thích vế số.", AMBER),
    ("03", "Trộn hai trục", "“Khách nói về cái gì” (khía cạnh) khác với “khách cảm thấy như thế nào” (cảm xúc).", BLUE),
]
for i, (no, title, body, accent) in enumerate(crit):
    x = 0.78 + i * 4.03
    card(s, x, 2.66, 3.68, 2.64, title, body, accent, WHITE, 16.5, 12.6)
    pill(s, x + 0.22, 4.74, 0.5, no, PALE_SLATE, MUTED, 10)

# 09 — research gap & boundaries
s = prs.slides.add_slide(blank); header(s, "Khoảng trống nghiên cứu — và ranh giới nhóm tự đặt", "02 · Research gap", 9)
card(s, 0.75, 1.63, 5.8, 2.0, "Khoảng trống đo lường",
     "Chưa có phép đo giữ đồng thời độ lớn + chiều ở cấp khía cạnh, trên dữ liệu review khách sạn.", TEAL, WHITE, 19, 15)
card(s, 6.78, 1.63, 5.8, 2.0, "Khoảng trống hành vi",
     "Chưa kiểm định trực tiếp việc nhiều khía cạnh kết hợp bất đối xứng để tạo độ lệch trên điểm sao quan sát được.", BLUE, WHITE, 19, 15)
rect(s, 0.75, 4.03, 11.83, 1.55, PALE_AMBER, PALE_AMBER, True)
txt(s, 1.0, 4.25, 11.3, 0.26, "Ba giới hạn phải tuyên bố rõ", 16, NAVY, True)
bullets(s, 1.0, 4.72, 11.1, 0.6, [
    "Đóng góp thu hẹp: độ lệch có dấu ở cấp khía cạnh; labeling data thay vì topic modeling gộp.",
    "Không suy ra nhân quả hay trạng thái tâm lý nội tại của khách hàng từ dữ liệu công khai.",
], 12.5, INK, AMBER, 3)

# 10 — RQs
s = prs.slides.add_slide(blank); header(s, "Ba câu hỏi nghiên cứu và ba câu hỏi kỹ thuật", "03 · Câu hỏi nghiên cứu", 10)
rqs = [
    ("RQ1", "Khám phá", "Tần suất bao nhiêu?\nCó những dạng có hướng nào?", TEAL),
    ("RQ2", "Phương pháp", "Lượng hóa theo từng khía cạnh thế nào để giữ độ lớn lẫn chiều?", BLUE),
    ("RQ3", "Cơ chế", "Cảm xúc tích cực / tiêu cực trên nhiều khía cạnh kết hợp bất đối xứng thế nào?", AMBER),
]
for i, (rq, tag, question, accent) in enumerate(rqs):
    x = 0.78 + i * 4.0
    rect(s, x, 1.72, 3.65, 2.14, WHITE, LINE, True)
    pill(s, x + 0.22, 1.94, 0.68, rq, PALE_TEAL if accent == TEAL else (PALE_BLUE if accent == BLUE else PALE_AMBER), accent if accent != AMBER else NAVY, 11)
    txt(s, x + 1.02, 1.99, 2.2, 0.2, tag, 11.5, MUTED, True)
    txt(s, x + 0.24, 2.52, 3.05, 0.82, question, 14, INK, True, PP_ALIGN.CENTER)
rect(s, 0.78, 4.35, 11.65, 1.48, NAVY, NAVY, True)
txt(s, 1.06, 4.56, 3.2, 0.23, "Nhánh dự báo của môn học", 12, "7EE5DC", True)
txt(s, 1.06, 4.98, 10.75, 0.45, "Sub-RQ1: 5 mô hình dự đoán điểm  ·  Sub-RQ2: phân bố phần dư  ·  Sub-RQ3: dự đoán review bị dìm điểm", 14.5, WHITE, True, PP_ALIGN.CENTER)

# 11 — three layers
s = prs.slides.add_slide(blank); header(s, "Phương pháp: ba tầng liên kết", "04 · Phương pháp", 11)
layers = [
    ("TẦNG 1", "Xử lý ngôn ngữ", "Trích tín hiệu cảm xúc theo từng khía cạnh\n(từ span do team gán nhãn độc lập).", TEAL),
    ("TẦNG 2", "Đo lường", "So rating với sentiment text để có D theo khía cạnh — giữ cả độ lớn và chiều.", BLUE),
    ("TẦNG 3", "Kinh tế lượng", "Xác định khía cạnh chi phối, khía cạnh bù trừ và điều kiện biên.", AMBER),
]
txt(s, 0.85, 1.65, 3.55, 0.35, "Văn bản review", 15, NAVY, True)
for i, (tag, title, body, accent) in enumerate(layers):
    x = 0.8 + i * 4.1
    rect(s, x, 2.25, 3.55, 3.35, WHITE, LINE, True)
    shp = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x + 0.25), Inches(2.53), Inches(0.52), Inches(0.52))
    shp.fill.solid(); shp.fill.fore_color.rgb = rgb(accent); shp.line.color.rgb = rgb(accent)
    txt(s, x + 0.25, 2.65, 0.52, 0.24, str(i + 1), 11, WHITE, True, PP_ALIGN.CENTER)
    pill(s, x + 2.18, 2.62, 1.08, tag, PALE_SLATE, MUTED, 10)
    txt(s, x + 0.25, 3.31, 3.05, 0.42, title, 20, NAVY, True)
    txt(s, x + 0.25, 4.02, 3.05, 1.26, body, 15, INK)
    if i < 2:
        add_arrow(s, x + 3.7, 3.7, 0.25, 0.38, TEAL)
rect(s, 0.8, 6.12, 11.75, 0.58, PALE_TEAL, PALE_TEAL, True)
txt(s, 1.0, 6.25, 11.35, 0.32, "Đầu ra: một phép đo được kiểm chứng + mô hình giải thích mẫu chấm điểm", 14, TEAL_DARK, True, PP_ALIGN.CENTER)

# 12 — validation & separation
s = prs.slides.add_slide(blank); header(s, "Validation trước khi chốt phép đo", "04 · Quy trình 5 bước", 12)
steps = [
    ("1", "EDA & toàn vẹn", "Đặc tả dữ liệu"),
    ("2", "Tập đối chứng 600–800", "Có ca lệch + ca bình thường"),
    ("3", "Hai người gán nhãn", "Cohen’s Kappa ≥ 0,70"),
    ("4", "So 3 công thức", "Chọn phép đo chính thức"),
    ("5", "Mô hình hành vi", "Kết quả kiểm định"),
]
for i, (num, title, body) in enumerate(steps):
    x = 0.68 + i * 2.52
    rect(s, x, 1.72, 2.18, 2.22, WHITE, LINE, True)
    add_badge(s, x + 0.18, 1.93, num, TEAL if i < 3 else (BLUE if i == 3 else AMBER))
    txt(s, x + 0.2, 2.56, 1.76, 0.42, title, 14.5, NAVY, True, PP_ALIGN.CENTER)
    txt(s, x + 0.2, 3.22, 1.76, 0.36, body, 11, MUTED, False, PP_ALIGN.CENTER)
    if i < 4:
        add_arrow(s, x + 2.23, 2.55, 0.22, 0.34, TEAL)
rect(s, 0.72, 4.48, 5.78, 1.3, PALE_RED, PALE_RED, True)
txt(s, 0.95, 4.7, 5.3, 0.23, "Ca bình thường là bắt buộc", 16, RED, True)
txt(s, 0.95, 5.08, 5.23, 0.35, "Nếu chỉ kiểm thử ca nghi ngờ, phép đo quá nhạy vẫn có thể “đúng” nhưng báo động giả liên tục.", 12, INK)
rect(s, 6.77, 4.48, 5.78, 1.3, PALE_TEAL, PALE_TEAL, True)
txt(s, 7.0, 4.7, 5.25, 0.23, "Tách hai họ mô hình", 16, TEAL_DARK, True)
txt(s, 7.0, 5.08, 5.22, 0.35, "Mô hình dự đoán điểm học từ sao; bộ ước lượng cảm xúc học từ nhãn người gán. Không thay thế nhau.", 12, INK)

# 13 — measure candidates
s = prs.slides.add_slide(blank); header(s, "Chốt phép đo bằng ground truth — không theo trực giác", "04 · Đo lường", 13)
opts = [
    ("Baseline", "Ma trận phân cực\ncó hướng 3×3", "Nhãn lớp dễ diễn giải", TEAL),
    ("Ứng viên", "Khoảng cách\nchuẩn hóa có dấu", "Một số kèm dấu cho cả bài", BLUE),
    ("Ứng viên", "Khoảng cách cấp\nkhía cạnh có dấu", "Vector theo từng khía cạnh", AMBER),
]
for i, (tag, title, desc, accent) in enumerate(opts):
    x = 0.78 + i * 4.02
    rect(s, x, 1.72, 3.67, 2.15, WHITE, LINE, True)
    pill(s, x + 0.22, 1.95, 1.0, tag, PALE_TEAL if accent == TEAL else (PALE_BLUE if accent == BLUE else PALE_AMBER), accent if accent != AMBER else NAVY, 10)
    txt(s, x + 0.22, 2.49, 3.05, 0.55, title, 17, NAVY, True, PP_ALIGN.CENTER)
    txt(s, x + 0.22, 3.3, 3.05, 0.22, desc, 11.5, MUTED, False, PP_ALIGN.CENTER)
rect(s, 1.24, 4.48, 10.86, 1.12, NAVY, NAVY, True)
txt(s, 1.52, 4.68, 10.28, 0.18, "Tiêu chí chọn", 11.5, "7EE5DC", True, PP_ALIGN.CENTER)
txt(s, 1.47, 5.0, 10.38, 0.28, "Khớp nhãn người · giữ dấu · ổn định hai phía điểm · giải thích theo khía cạnh · không dùng điểm sao để huấn luyện", 13, WHITE, True, PP_ALIGN.CENTER)
txt(s, 1.25, 6.02, 10.8, 0.25, "Nếu không đạt: giữ ma trận phân cực làm baseline và ghi rõ lý do.", 12.5, MUTED, False, PP_ALIGN.CENTER)

# 14 — literature protocol
s = prs.slides.add_slide(blank); header(s, "Khảo sát văn hiến: có tiêu chí dừng và nhánh phản biện", "05 · Cách khảo sát", 14)
card(s, 0.75, 1.62, 5.78, 1.28, "Quy tắc 1 — Mục tiêu dừng rõ ràng", "Dừng khi đủ nguyên liệu cho đề cương, có baseline, và không còn phát hiện làm đổi thiết kế.", TEAL, WHITE, 16.5, 12.2)
card(s, 0.75, 3.13, 5.78, 1.28, "Quy tắc 2 — Cửa sổ 36 tháng", "Tài liệu cũ chỉ lấy khi là nguồn gốc của khái niệm đang dùng; phải ghi lý do.", BLUE, WHITE, 16.5, 12.2)
rect(s, 6.83, 1.62, 5.78, 3.83, NAVY, NAVY, True)
txt(s, 7.12, 1.9, 5.2, 0.24, "Bốn nguyên tắc khi đọc", 16.5, "7EE5DC", True)
for i, item in enumerate([
    "Ưu tiên journal trước hội nghị / preprint",
    "Mỗi DOI kiểm chứng qua Crossref + OpenAlex",
    "Gán mức bằng chứng I–VII cho từng nguồn",
    "Bắt buộc tìm bằng chứng chống giả thuyết",
]):
    y = 2.43 + i * 0.68
    add_badge(s, 7.15, y, i + 1, TEAL)
    txt(s, 7.68, y + 0.05, 4.25, 0.28, item, 13.5, WHITE)
pill(s, 1.25, 5.92, 10.83, "Mục tiêu là khảo sát đủ để ra thiết kế vững — không phải quét thật nhiều.", PALE_AMBER, NAVY, 13)

# 15 — literature results
s = prs.slides.add_slide(blank); header(s, "Kết quả khảo sát: cơ chế bất đối xứng đã được mở rộng", "05 · Kết quả", 15)
rect(s, 0.76, 1.63, 5.78, 2.24, PALE_RED, PALE_RED, True)
txt(s, 1.0, 1.89, 5.25, 0.24, "NHÁNH CHI PHỐI", 12, RED, True)
txt(s, 1.0, 2.32, 5.12, 0.43, "Một lỗi cơ bản và nghiêm trọng có thể chi phối cả đánh giá.", 18, NAVY, True)
txt(s, 1.0, 3.1, 5.08, 0.28, "Severity và Service Recovery là biến điều kiện thực.", 12.3, MUTED)
rect(s, 6.8, 1.63, 5.78, 2.24, PALE_TEAL, PALE_TEAL, True)
txt(s, 7.04, 1.89, 5.25, 0.24, "NHÁNH BÙ TRỪ", 12, TEAL_DARK, True)
txt(s, 7.04, 2.32, 5.12, 0.43, "Lỗi nhẹ hoặc đã được khắc phục mới cho phép các điểm tích cực cộng gộp.", 18, NAVY, True)
txt(s, 7.04, 3.1, 5.08, 0.28, "Không giả định bù trừ tuyến tính giữa mọi khía cạnh.", 12.3, MUTED)
for i, (head, body, color) in enumerate([
    ("88.309 + 540.000", "Bất đối xứng đã có bằng chứng ở các quy mô lớn", BLUE),
    ("17,3%", "Mốc tham chiếu từ một nghiên cứu độc lập", AMBER),
    ("Giới hạn nhận dạng", "Không tuyên bố nhân quả hay “tha thứ”", RED),
]):
    x = 0.78 + i * 4.0
    card(s, x, 4.55, 3.66, 1.15, head, body, color, WHITE, 15, 10.5)

# 16 — current checkpoint
s = prs.slides.add_slide(blank); header(s, "Khảo sát đóng có điều kiện — nhưng chưa được chốt công thức đo", "05 · Điểm dừng", 16)
rect(s, 0.75, 1.66, 4.35, 3.92, NAVY, NAVY, True)
txt(s, 1.0, 1.96, 3.85, 0.24, "ĐÃ CÓ", 11.5, "7EE5DC", True)
txt(s, 1.0, 2.43, 3.7, 1.65, "35\ntệp toàn văn", 31, WHITE, True, PP_ALIGN.CENTER)
txt(s, 1.0, 4.5, 3.73, 0.5, "8 cụm chức năng · 5 quyết định nội bộ\nKhung lý thuyết và phạm vi dữ liệu đã khóa", 12.5, "C7D5E0", False, PP_ALIGN.CENTER)
rect(s, 5.38, 1.66, 7.2, 1.1, PALE_TEAL, PALE_TEAL, True)
txt(s, 5.68, 1.91, 6.6, 0.22, "Đã đủ để viết đề cương; “bão hòa” được thay bằng tiêu chí: không còn phát hiện đổi thiết kế.", 14.2, NAVY, True, PP_ALIGN.CENTER)
missing = [
    ("16 bài đóng", "Cần thư viện trường; ưu tiên Kwon W. 2026, Han & Anderson, Slevitch", AMBER),
    ("Công thức đo D", "Chưa chốt — chờ validation trên dữ liệu của nhóm", RED),
    ("Bộ ước lượng cảm xúc", "Cùng được chốt qua validation", BLUE),
    ("Nguồn gốc / giấy phép", "Chưa khai báo", TEAL),
]
for i, (title, body, accent) in enumerate(missing):
    y = 3.03 + (i // 2) * 1.25
    x = 5.38 + (i % 2) * 3.67
    card(s, x, y, 3.42, 1.1, title, body, accent, WHITE, 13.3, 10.7)

# 17 — next steps
s = prs.slides.add_slide(blank); header(s, "Việc tiếp theo: khóa validation trước, mở rộng sau", "06 · Kế hoạch", 17)
roadmap = [
    ("1", "Validation", "Tập đánh giá · 2 người gán · so 3 công thức", "Công thức đo được chốt", TEAL),
    ("2", "Bài đóng", "Nhờ thư viện lấy theo thứ tự ưu tiên", "Toàn văn phương pháp", BLUE),
    ("3", "Research Proposal", "Cập nhật theo khung và RQ3 đã khóa", "Bản đề cương", AMBER),
    ("4", "Kinh tế lượng", "Khóa sau khi đã có phép đo", "Bảng kiểm định", RED),
    ("5", "Ứng dụng", "Dựng nhánh app và endpoint sớm", "Demo được", TEAL),
]
for i, (no, title, detail, output, accent) in enumerate(roadmap):
    y = 1.6 + i * 0.95
    rect(s, 0.78, y, 11.8, 0.72, WHITE, LINE, True)
    add_badge(s, 1.0, y + 0.17, no, accent)
    txt(s, 1.55, y + 0.18, 1.85, 0.21, title, 13.5, NAVY, True)
    txt(s, 3.47, y + 0.18, 4.74, 0.23, detail, 12.3, INK)
    txt(s, 8.5, y + 0.18, 3.5, 0.23, output, 12, accent, True, PP_ALIGN.RIGHT)
txt(s, 0.8, 6.64, 11.7, 0.26, "Thứ tự là có chủ đích: không xây màn hình hiển thị D khi phép đo D chưa qua validation.", 13, MUTED, False, PP_ALIGN.CENTER)

# 18 — feedback
s = prs.slides.add_slide(blank); header(s, "Năm điểm nhóm cần thầy góp ý", "06 · Cần định hướng", 18)
feedback = [
    ("Tên đề tài", "Giữ tên tạm; chốt sau khi đã có công thức đo."),
    ("RQ1 & RQ2", "Có nên chốt sớm khi chưa hoàn tất validation?"),
    ("Phạm vi dữ liệu", "9.990 review đã có span label thay vì corpus 782.584 review."),
    ("Ba baseline", "Le et al. (2026), Kwon et al. (2025), You et al. (2024)."),
    ("Trọng tâm đo lường", "Ưu tiên phép đo D và ground truth hơn tối ưu mô hình dự báo?"),
]
for i, (title, detail) in enumerate(feedback):
    y = 1.62 + i * 0.95
    rect(s, 0.9, y, 11.55, 0.67, WHITE, LINE, True)
    rect(s, 0.9, y, 0.72, 0.67, TEAL if i < 2 else (BLUE if i < 4 else AMBER), TEAL, True)
    txt(s, 0.9, y + 0.2, 0.72, 0.18, str(i + 1), 13, WHITE, True, PP_ALIGN.CENTER)
    txt(s, 1.9, y + 0.15, 2.35, 0.24, title, 13.5, NAVY, True)
    txt(s, 4.15, y + 0.13, 7.9, 0.30, detail, 13.5, INK)

# 19 — application logic
s = prs.slides.add_slide(blank); header(s, "Ứng dụng: Bảng soát điểm sao", "07 · Hướng ứng dụng", 19)
txt(s, 0.78, 1.56, 11.6, 0.31, "Nền tảng chỉ hiển thị một con số; ứng dụng tách nó thành hai.", 19, NAVY, True)
rect(s, 0.78, 2.04, 5.28, 1.45, NAVY, NAVY, True)
txt(s, 1.03, 2.31, 4.75, 0.24, "ĐIỂM KHÁCH BẤM", 11.5, "7EE5DC", True, PP_ALIGN.CENTER)
txt(s, 1.03, 2.74, 4.75, 0.37, "vs. điểm nội dung review biện minh được", 17.3, WHITE, True, PP_ALIGN.CENTER)
add_arrow(s, 6.34, 2.46, 0.7, 0.62, TEAL)
rect(s, 7.34, 2.04, 5.24, 1.45, PALE_TEAL, PALE_TEAL, True)
txt(s, 7.59, 2.31, 4.74, 0.24, "KHOẢNG CÁCH CẦN NHÌN", 11.5, TEAL_DARK, True, PP_ALIGN.CENTER)
txt(s, 7.59, 2.74, 4.74, 0.37, "Chênh lệch theo khách sạn và theo khía cạnh", 17.1, NAVY, True, PP_ALIGN.CENTER)
questions = [
    ("Khách sạn được điểm cao hơn thực lực bao nhiêu?", "Chênh giữa điểm thực tế và điểm dự báo từ văn bản"),
    ("Khoản chênh đến từ khía cạnh nào?", "D có dấu theo từng khía cạnh"),
    ("Nên đầu tư vào đâu?", "Xếp hạng khía cạnh bị dìm điểm / được bỏ qua"),
]
for i, (q, a) in enumerate(questions):
    x = 0.78 + i * 4.0
    card(s, x, 4.02, 3.66, 1.47, f"{i + 1}. {q}", a, TEAL if i != 2 else AMBER, WHITE, 13.1, 11.3)
pill(s, 2.1, 5.95, 9.08, "Người dùng mục tiêu: quản lý vận hành / revenue manager — không phải khách du lịch.", PALE_BLUE, BLUE, 12.5)

# 20 — app dashboard
s = prs.slides.add_slide(blank); header(s, "Màn hình chính: một ca demo có thật", "07 · Bảng soát điểm sao", 20)
rect(s, 0.95, 1.55, 7.38, 4.95, WHITE, "B9C9D7", True)
rect(s, 0.95, 1.55, 7.38, 0.58, NAVY, NAVY, True)
txt(s, 1.2, 1.74, 2.4, 0.2, "SOÁT ĐIỂM SAO", 12.5, WHITE, True)
txt(s, 4.75, 1.72, 3.2, 0.24, "Sofitel Legend Metropole  ▾", 12.5, "C7D5E0", False, PP_ALIGN.RIGHT)
metric(s, 1.28, 2.45, 1.75, "4.0", "★ thực tế", AMBER, "★")
metric(s, 3.42, 2.45, 1.75, "3.2", "★ văn bản", TEAL, "★")
metric(s, 5.56, 2.45, 1.75, "+0.8", "★ chênh lệch", BLUE, "★")
rect(s, 1.28, 4.13, 6.04, 1.45, PALE_SLATE, PALE_SLATE, True)
txt(s, 1.52, 4.30, 1.45, 0.22, "Review #131571", 11.5, MUTED, True)
txt(s, 1.52, 4.66, 4.0, 0.24, "“…beds were so comfortable…”", 14, GREEN, True)
txt(s, 1.52, 5.04, 4.0, 0.24, "“…wait staff were very slow…”", 14, RED, True)
txt(s, 5.34, 4.66, 1.76, 0.55, "chấm cao hơn\nnội dung 0.8★", 12.5, BLUE, True, PP_ALIGN.CENTER)
card(s, 8.72, 1.7, 3.75, 1.18, "Ca demo trong dữ liệu", "Sofitel Legend Metropole: 8 / 85 review", TEAL, WHITE, 15.5, 11.5)
card(s, 8.72, 3.1, 3.75, 2.15, "Bốn ràng buộc khi xây", "• Chưa hiển thị D trước validation.\n• Không suy diễn “khách tha thứ”.\n• Không tổng hợp nếu <20 review.\n• Không dùng biểu đồ radar.", AMBER, WHITE, 15.5, 11.5)
txt(s, 0.98, 6.74, 11.6, 0.24, "Các ca khác: Anantara Hội An (6/39) · Salinda Phú Quốc (4/31) · Lavender Central (4/60) · Indochine Palace (4/30).", 11, MUTED, False, PP_ALIGN.CENTER)

# 21 — appendix I
s = prs.slides.add_slide(blank); header(s, "Phụ lục: câu hỏi dự kiến (1/2)", "Gợi ý trả lời", 21)
qa1 = [
    ("Vì sao không dùng điểm sao làm nhãn cảm xúc?", "Vì 394 review 5 sao vẫn có phàn nàn tiêu cực. Dùng sao làm nhãn sẽ khiến mô hình học luôn phần không khớp đó."),
    ("Vì sao cần hai người gán nhãn?", "Vì “bất nhất thật” là phán đoán chủ quan. Cohen’s Kappa cho biết quy chuẩn có dùng được không; bất đồng phải được giải quyết."),
    ("Sao không dùng LLM cho nhanh?", "Có thể dùng, nhưng vẫn phải đánh giá trên tập do người gán. Bộ đo cảm xúc không được huấn luyện từ điểm sao."),
]
for i, (q, a) in enumerate(qa1):
    y = 1.55 + i * 1.62
    rect(s, 0.82, y, 11.75, 1.31, WHITE, LINE, True)
    pill(s, 1.06, y + 0.22, 0.52, f"{i + 1}", PALE_TEAL, TEAL_DARK, 10.5)
    txt(s, 1.79, y + 0.17, 10.1, 0.30, q, 15.5, NAVY, True)
    txt(s, 1.79, y + 0.64, 10.0, 0.42, a, 13.5, INK)

# 22 — appendix II / close
s = prs.slides.add_slide(blank); header(s, "Phụ lục: câu hỏi dự kiến (2/2)", "Gợi ý trả lời", 22)
card(s, 0.82, 1.58, 5.65, 1.95, "Sao chỉ có 9.990 review?", "Đây là phần có nhãn khía cạnh và cảm xúc ở cấp span — điều kiện bắt buộc để đo lệch theo khía cạnh. Corpus lớn hơn không có span label không trả lời được RQ2–RQ3.", BLUE, WHITE, 17, 13)
card(s, 6.85, 1.58, 5.65, 1.95, "Có chắc là khách tha thứ không?", "Không. Dữ liệu công khai không đủ để suy ra trạng thái tâm lý. Nhóm chỉ phát biểu về mẫu hành vi chấm điểm quan sát được.", RED, WHITE, 17, 13)
rect(s, 0.82, 4.06, 11.68, 1.4, NAVY, NAVY, True)
txt(s, 1.15, 4.32, 11.0, 0.28, "Điểm cần thầy định hướng", 13, "7EE5DC", True, PP_ALIGN.CENTER)
txt(s, 1.15, 4.79, 11.0, 0.29, "Tên đề tài · RQ1/RQ2 · phạm vi 9.990 review · ba baseline · trọng tâm validation", 16.5, WHITE, True, PP_ALIGN.CENTER)
txt(s, 0.82, 6.05, 11.68, 0.35, "Cảm ơn thầy — nhóm mong nhận góp ý để khóa thiết kế validation.", 18, NAVY, True, PP_ALIGN.CENTER)

# Document metadata for traceability.
props = prs.core_properties
props.title = "Báo cáo tiến độ dự án — Bất nhất cảm xúc–điểm số ở cấp khía cạnh"
props.subject = "DAP391m progress report"
props.author = "Nhóm dự án"
props.keywords = "hotel review, sentiment-rating discrepancy, DAP391m"
prs.save(OUT)
print(f"Created {OUT.resolve()} with {len(prs.slides)} slides")
