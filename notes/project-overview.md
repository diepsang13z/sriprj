# Tổng quan Dự án (Project Overview)

- **Ngày tạo:** 2026-09-21
- **Cập nhật gần nhất:** 2026-09-22, sau Survey Round 3 và đợt audit thư viện `refs/`.
- **Mục đích:** Bản đồ một trang về đề tài — hướng nghiên cứu, research gap, câu hỏi nghiên cứu và sản phẩm đầu ra. Dùng để định hướng lại khi bị lạc trong thuật ngữ.

> **Cảnh báo về thẩm quyền:** Đây là bản tóm tắt định hướng, **không phải nguồn sự thật**. Nguồn sự thật là các quyết định trong `docs/decisions/` (`RDR-NNNN`, số lớn nhất thắng). Các RQ dưới đây mới ở dạng **nháp, chưa được ban hành chính thức**.

---

## 1. Hướng nghiên cứu (The Big Idea)

**Bài toán gốc:** phân tích cảm xúc review khách sạn trên TripAdvisor / Booking.com.

**Vấn đề của cách làm phổ biến hiện nay:** các nghiên cứu trước mặc định _"khen thì 5 sao, chê thì 1 sao"_. Khi gặp review chê mà vẫn chấm 5 sao, họ coi đó là lỗi hoặc nhiễu (label noise) và loại bỏ.

**Hướng đi của đề tài:** **lấy chính những trường hợp "nói một đằng, chấm một nẻo" làm đối tượng nghiên cứu**, không xóa chúng đi.

- Rating cao dù có negative aspects có thể phản ánh **cross-aspect compensation**, lỗi nhẹ hoặc lỗi đã được recovery.
- Rating thấp dù phần lớn nội dung tích cực có thể phản ánh một lỗi **penalty-dominant/non-compensatory** đủ nghiêm trọng hoặc đủ diagnostic. Không suy diễn trực tiếp `forgiveness` hay `anger` chỉ từ rating.

---

## 2. Research Gap

### 2.1. Về mặt kỹ thuật (NLP / đo lường)

- Phần lớn phép đo dùng trị tuyệt đối $|Rating - Text|$ nên **mất chiều** — không phân biệt rating cao hơn với rating thấp hơn mức mà nội dung văn bản gợi ý.
- Chưa có phép đo nào đồng thời giữ **magnitude** và **direction** ở **cấp khía cạnh dịch vụ** trên dữ liệu khách sạn.
- Hệ quả kéo theo: dùng rating làm nhãn cảm xúc (ground truth) là thực hành phổ biến nhưng chưa được kiểm định.

### 2.2. Về mặt hành vi (kinh tế lượng / lý thuyết)

- Các nghiên cứu về forgiveness/anger thường dùng bảng hỏi và các outcome như repatronage hoặc dissatisfaction; chúng không đủ để suy diễn trực tiếp trạng thái tâm lý từ rating quan sát được.
- **Khoảng trống sau Round 3:** văn hiến mới chủ yếu giải thích overall satisfaction; chưa kiểm định trực tiếp cách nhiều aspect kết hợp bất đối xứng để tạo **direction và magnitude của sentiment–rating discrepancy** trên điểm sao quan sát được.

---

## 3. Câu hỏi nghiên cứu (RQ — bản nháp, chưa chốt chính thức)

- **RQ1 (khám phá):** Hiện tượng bất nhất giữa nội dung review và số sao xuất hiện với tần suất bao nhiêu, và gồm những dạng có hướng nào khi số sao cao hơn hoặc thấp hơn so với mức mà nội dung văn bản gợi ý?
- **RQ2 (phương pháp):** Làm thế nào để lượng hóa độ bất nhất này theo từng khía cạnh dịch vụ mà giữ được cả magnitude lẫn direction?
- **RQ3 (candidate sau Round 3, chưa chốt):** Cảm xúc tích cực và tiêu cực trên nhiều khía cạnh kết hợp bất đối xứng như thế nào để quyết định chiều hướng và độ lớn của sentiment–rating discrepancy?

---

## 4. Sản phẩm đầu ra dự kiến

1. **Bộ dữ liệu chuẩn (evaluation benchmark dataset):** khoảng 600 review đã được 2 người gán nhãn thủ công độc lập, kèm nhóm aligned controls để đo false-positive rate.
2. **Pipeline xử lý dữ liệu và đo lường (source code / notebook):** module trích xuất cảm xúc theo khía cạnh (ABSA) + module tính điểm bất nhất có dấu ở cấp aspect.
3. **Mô hình kinh tế lượng:** bảng kết quả kiểm định compensatory/non-compensatory aspect effects; `Service × Facility` là một planned contrast.
4. **Báo cáo học thuật:** Research Proposal và báo cáo kết quả hoàn chỉnh theo format học phần DAP391m (IMRAD).

---

## 5. Lộ trình và trạng thái hiện tại

```
[Survey Round 1–2] ──────► XONG (15 nguồn hạt nhân)
        │
        ▼
[Survey Round 3] ────────► XONG targeted scan theo RDR-0003
                            → 9 journal candidates; 2/9 đã có toàn văn
                            → candidate: asymmetric compensatory/non-compensatory RQ3
        │
        ▼
[Bước hiện tại] ──────────► Nghiên cứu viên chọn/chỉnh candidate RQ3
                            → audit 3 nguồn trực tiếp còn thiếu: Kwon, Wang, Albayrak
                            → hàng đợi rộng còn 7 bài; không tiếp tục cào ngoài hàng đợi
        │
        ▼
[Sau khi chốt RQ3] ───────► Cập nhật Research Proposal
                            → khóa validation/econometric model
                            → dựng evaluation set và chạy kiểm định
                            → viết báo cáo kết quả
```

---

## 6. Đọc thêm

- [`refs/root/factsheet.md`](../refs/root/factsheet.md) — bài báo gốc: tham số, phương trình hồi quy, các lỗ hổng bị phản biện.
- [`docs/logs/brainstorm/0001_root_idea.md`](../docs/logs/brainstorm/0001_root_idea.md) — phân tích bài gốc, lỗi lập luận vòng của biến `Loyalty`.
- [`docs/logs/literature-survey/0004_synthesis_and_next_step.md`](../docs/logs/literature-survey/0004_synthesis_and_next_step.md) — tổng kết bằng chứng, các điểm đã chốt và còn mở.
- [`docs/logs/literature-survey/0005_survey_matrix_round_3_rq3_rescoping.md`](../docs/logs/literature-survey/0005_survey_matrix_round_3_rq3_rescoping.md) — targeted scan tái định hình RQ3 và đánh giá các phương án theo fit dữ liệu.
- [`notes/survey-round-3-overview.md`](survey-round-3-overview.md) — bản giải thích ngắn về mục đích, phạm vi, số liệu và kết quả chính của Survey Round 3.
- [`notes/reference-map.md`](reference-map.md) — mỗi ref nói gì, được dùng vào đâu và trạng thái đã/chưa kéo toàn văn.
- [`docs/logs/validation/0001_manual_annotation_protocol.md`](../docs/logs/validation/0001_manual_annotation_protocol.md) — thiết kế evaluation set và quy chuẩn gán nhãn.
- [`reports/md/research_proposal_draft.md`](../reports/md/research_proposal_draft.md) — bản nháp Research Proposal, Phụ lục A liệt kê 16 điểm chưa chốt.
- [`notes/glossary.md`](glossary.md) — từ điển thuật ngữ song ngữ.
