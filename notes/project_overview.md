# Tổng quan Dự án (Project Overview)

- **Ngày tạo:** 2026-09-21
- **Cập nhật gần nhất:** 2026-09-23, sau Survey Round 4 (verification round).
- **Mục đích:** Bản đồ một trang về đề tài — hướng nghiên cứu, research gap, câu hỏi nghiên cứu và sản phẩm đầu ra. Dùng để định hướng lại khi bị lạc trong thuật ngữ.

> **Cảnh báo về thẩm quyền:** Đây là bản tóm tắt định hướng, **không phải nguồn sự thật**. Nguồn sự thật là các quyết định trong `docs/decisions/` (`RDR-NNNN`, số lớn nhất thắng). **Khung lý thuyết và phạm vi dữ liệu đã khóa theo `RDR-0005`;** RQ1–RQ2 vẫn ở dạng nháp.

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
- Chưa có phép đo nào đồng thời giữ **magnitude** và **direction** ở **cấp khía cạnh dịch vụ** trên dữ liệu khách sạn. Round 4 đã kiểm tra tính mới độc lập (log `0006` mục 4.3) và không tìm thấy tiền lệ trực tiếp.
- Hệ quả kéo theo: dùng rating làm nhãn cảm xúc (ground truth) là thực hành phổ biến nhưng chưa được kiểm định.

### 2.2. Về mặt hành vi (kinh tế lượng / lý thuyết)

- Các nghiên cứu về forgiveness/anger thường dùng bảng hỏi và các outcome như repatronage hoặc dissatisfaction; chúng không đủ để suy diễn trực tiếp trạng thái tâm lý từ rating quan sát được.
- **Khoảng trống sau Round 3:** văn hiến mới chủ yếu giải thích overall satisfaction; chưa kiểm định trực tiếp cách nhiều aspect kết hợp bất đối xứng để tạo **direction và magnitude của sentiment–rating discrepancy** trên điểm sao quan sát được.
- **Khoảng trống sau Round 4 — chốt lại kèm hai ranh giới:**
  - Chưa tìm thấy tiền lệ trực tiếp cho **thước đo discrepancy có dấu ở cấp khía cạnh**; kết luận chỉ ở mức "chưa tìm thấy" vì tìm kiếm title/abstract không chứng minh được sự vắng mặt. Ranh giới tính mới mỏng: Regitz et al. (2026) làm gần đúng việc này, chỉ khác đơn vị phân tích (hệ số hồi quy theo topic thay vì review có nhãn người gán).
  - **Hạn chế nhận dạng (identification):** review công khai không phân biệt được bù trừ thật với thiên lệch trình bày và méo cấu trúc nền tảng; mọi tuyên bố prevalence phải ghi phạm vi **TripAdvisor 2015–2023**.

---

## 3. Câu hỏi nghiên cứu (RQ3 đã chốt theo `RDR-0004`; RQ1–RQ2 còn nháp)

- **RQ1 (khám phá):** Hiện tượng bất nhất giữa nội dung review và số sao xuất hiện với tần suất bao nhiêu, và gồm những dạng có hướng nào khi số sao cao hơn hoặc thấp hơn so với mức mà nội dung văn bản gợi ý?
- **RQ2 (phương pháp):** Làm thế nào để lượng hóa độ bất nhất này theo từng khía cạnh dịch vụ mà giữ được cả magnitude lẫn direction?
- **RQ3 (đã chốt theo `RDR-0004`):** Cảm xúc tích cực và tiêu cực trên nhiều khía cạnh kết hợp bất đối xứng như thế nào để quyết định chiều hướng và độ lớn của sentiment–rating discrepancy?
  - Hai điều chỉnh **không thương lượng** sau Round 4: (a) bỏ mọi ngôn ngữ khẳng định nhân quả kiểu "khách tha thứ" khi chỉ có dữ liệu công khai; (b) kiểm định phụ #1 (aspect nào penalty-dominant) chỉ được trình bày như **phân tích khám phá**. Bốn thay đổi đầy đủ nằm ở log `0006` mục 5.2.

---

## 4. Sản phẩm đầu ra dự kiến

1. **Bộ dữ liệu chuẩn (evaluation benchmark dataset):** khoảng 600 review đã được 2 người gán nhãn thủ công độc lập, kèm nhóm aligned controls để đo false-positive rate.
2. **Pipeline xử lý dữ liệu và đo lường (source code / notebook):** module trích xuất cảm xúc theo khía cạnh (ABSA) + module tính điểm bất nhất có dấu ở cấp aspect.
3. **Mô hình kinh tế lượng:** bảng kết quả kiểm định compensatory/non-compensatory aspect effects; `Service × Facility` là một planned contrast.
4. **Báo cáo học thuật:** Research Proposal và báo cáo kết quả hoàn chỉnh theo format học phần DAP391m (IMRAD).
5. **Ứng dụng học phần DAP391m — Bảng soát điểm sao:** tách *điểm khách bấm* khỏi *điểm văn bản biện minh*, kèm nhánh dự báo (RQ4–RQ6) cho Bước 5 của môn. Chi tiết: [`docs/logs/brainstorm/0003_app_concept_and_course_requirements.md`](../docs/logs/brainstorm/0003_app_concept_and_course_requirements.md).

---

## 5. Lộ trình và trạng thái hiện tại

```
[Survey Round 1–2] ──────► XONG (15 nguồn hạt nhân)
        │
        ▼
[Survey Round 3] ────────► XONG targeted scan theo RDR-0003
                            → 9 journal candidates; 3/9 đã có toàn văn
        │
        ▼
[Survey Round 4] ────────► XONG verification round (2026-09-23)
                            → 26 nguồn mới xác minh qua 5 cluster A–E
                            → 9 toàn văn, đã xếp vào cụm chức năng trong refs/
                            → novelty check độc lập; devil's advocate PASS có điều kiện
        │
        ▼
[Bước hiện tại] ──────────► Khảo sát ĐÓNG có điều kiện (RDR-0005, 2026-09-23)
                            → khung lý thuyết khóa: S-O-R + Kano + Prospect Theory
                            → phạm vi dữ liệu khóa: 9.990 review gán nhãn, TripAdvisor 2015–2023
                            → còn 2 bài mở tải tay (Liu, Slevitch) + 14 bài đóng cần thư viện (refs/INDEX.md mục 9)
                            → cập nhật Research Proposal theo RQ3 + bốn điều chỉnh của Round 4
        │
        ▼
[Sau khi khóa] ───────────► dựng evaluation set → chốt công thức đo discrepancy
                            → khóa econometric model → viết báo cáo kết quả
```

---

## 6. Đọc thêm

- [`refs/01_root/factsheet.md`](../refs/01_root/factsheet.md) — bài báo gốc: tham số, phương trình hồi quy, các lỗ hổng bị phản biện.
- [`docs/logs/brainstorm/0001_root_idea.md`](../docs/logs/brainstorm/0001_root_idea.md) — phân tích bài gốc, lỗi lập luận vòng của biến `Loyalty`.
- [`docs/logs/literature_survey/0004_synthesis_and_next_step.md`](../docs/logs/literature_survey/0004_synthesis_and_next_step.md) — tổng kết bằng chứng, các điểm đã chốt và còn mở.
- [`docs/logs/literature_survey/0005_survey_matrix_round_3_rq3_rescoping.md`](../docs/logs/literature_survey/0005_survey_matrix_round_3_rq3_rescoping.md) — targeted scan tái định hình RQ3 và đánh giá các phương án theo fit dữ liệu.
- [`docs/logs/literature_survey/0006_survey_matrix_round_4.md`](../docs/logs/literature_survey/0006_survey_matrix_round_4.md) — Round 4 verification: 5 cluster, 26 nguồn mới, checkpoint phản biện, kiểm tra tính mới và đề xuất phân loại cụm.
- [`notes/survey_round_3_overview.md`](survey_round_3_overview.md) — bản giải thích ngắn về mục đích, phạm vi, số liệu và kết quả chính của Survey Round 3.
- [`notes/reference_map.md`](reference_map.md) — mỗi ref nói gì, được dùng vào đâu và trạng thái đã/chưa kéo toàn văn.
- [`docs/logs/validation/0001_manual_annotation_protocol.md`](../docs/logs/validation/0001_manual_annotation_protocol.md) — thiết kế evaluation set và quy chuẩn gán nhãn.
- [`reports/md/research_proposal_draft.md`](../reports/md/research_proposal_draft.md) — bản nháp Research Proposal, Phụ lục A liệt kê 16 điểm chưa chốt.
- [`notes/reference_map.md`](reference_map.md) — trạng thái từng ref, đọc kèm mục 6 (Round 4) và mục 10 (giới hạn sử dụng).
- [`reports/pillar_strength.html`](../reports/pillar_strength.html) — **xem độ mạnh 6 trụ cột bằng chứng** (thanh điểm: coverage 45% + evidence 35% + recency 20%) và khoảng trống thước đo có dấu cấp khía cạnh.
- [`notes/glossary.md`](glossary.md) — từ điển thuật ngữ song ngữ.
