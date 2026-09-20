# Documentation Router (docs/INDEX.md)

Tài liệu này là Router đơn (Single Router) phân tầng điều hướng toàn bộ tài liệu dự án. Mọi Agent bắt đầu tra cứu từ file này.

---

## 1. Core Context Files (Cốt lõi - Cấp File)

- [`RULES.md`](../RULES.md) — Quy tắc vận hành, ngân sách dòng ($\le 200$ dòng), kỷ luật Git và Single Source of Truth.
- [`AGENTS.md`](../AGENTS.md) — Định vị đề tài, phạm vi In-scope / Out-of-scope và thứ tự đọc tài liệu.
- [`STATUS.md`](../STATUS.md) — Ảnh chụp trạng thái hiện tại của dự án ($\le 40$ dòng, cập nhật ghi đè).
- [`refs/INDEX.md`](../refs/INDEX.md) — Danh mục tài liệu tham khảo và thư viện bài báo khoa học.

---

## 2. Architecture & Decision Records (Cấp File)

Thư mục lưu trữ các quyết định kỹ thuật và kiến trúc theo quy tắc Append-only (`RDR-NNNN`). Quyết định có số hiệu lớn nhất là nguồn sự thật tối cao.

- [`docs/decisions/RDR-0001-endpoint-literature-survey.md`](decisions/RDR-0001-endpoint-literature-survey.md) — Mục tiêu và tiêu chí dừng khảo sát văn hiến (Literature Survey Endpoint).
- [`docs/decisions/RDR-0002-latest-first-literature-scanning.md`](decisions/RDR-0002-latest-first-literature-scanning.md) — Chỉ quét chủ động tài liệu trong cửa sổ 36 tháng mới nhất; nguồn cũ chỉ được truy xuất theo ngoại lệ xác minh provenance.

---

## 3. Logs & Working Notes (Cấp Thư mục)

Khu vực ghi lại tiến trình tư duy, khảo sát văn hiến và nhật ký thử nghiệm (không áp dụng giới hạn 200 dòng):
- [`notes/project-overview.md`](../notes/project-overview.md) — Bản đồ một trang về đề tài: hướng nghiên cứu, research gap, RQ nháp, sản phẩm đầu ra và lộ trình.
- [`notes/glossary.md`](../notes/glossary.md) — Từ điển thuật ngữ nghiên cứu: định nghĩa song ngữ toàn bộ khái niệm cốt lõi, lý thuyết hành vi, mô hình ABSA/NLP và công thức đo lường.

- [`docs/logs/brainstorm/`](logs/brainstorm/) — Nhật ký phát triển ý tưởng, bóc tách bài báo gốc và định hình đề tài:
  - [`0001_root_idea.md`](logs/brainstorm/0001_root_idea.md) — Phân tích bài báo gốc (IJHM 2026) và định hướng Sentiment–Rating Inconsistency.
  - [`0002_direction_of_work_after_survey_2.md`](logs/brainstorm/0002_direction_of_work_after_survey_2.md) — Nhật ký hướng triển khai B1–B3 sau Survey Round 2 (EDA dataset → evaluation set → gán nhãn thủ công).
  - [`0003_app_concept_and_course_requirements.md`](logs/brainstorm/0003_app_concept_and_course_requirements.md) — Nhật ký khám phá: ràng buộc môn DAP391m, khoảng trống nhánh dự báo, ý tưởng ứng dụng Fair-Value Rating Radar và các bẫy rò rỉ dữ liệu đã xác minh. **Chưa quyết định gì.**
- [`docs/logs/literature-survey/`](logs/literature-survey/) — Nhật ký khảo sát các bài báo liên quan, phân tích đối chứng và tổng quan lý thuyết:
  - [`0001_discrepancy_formulations.md`](logs/literature-survey/0001_discrepancy_formulations.md) — Phân loại các họ phương pháp lượng hóa mâu thuẫn điểm số - bài viết và câu hỏi định hướng khảo sát.
  - [`0002_survey_matrix_round_1.md`](logs/literature-survey/0002_survey_matrix_round_1.md) — Vòng khảo sát đầu tiên: search protocol, ma trận 11 nguồn, theory/measurement/baseline synthesis và endpoint check.
  - [`0003_survey_matrix_round_2.md`](logs/literature-survey/0003_survey_matrix_round_2.md) — Vòng quét latest-first: 6 core candidates mới, operationalization magnitude/direction/aspect conflict, core-set curation và endpoint check.
  - [`0004_synthesis_and_next_step.md`](logs/literature-survey/0004_synthesis_and_next_step.md) — Tổng kết toàn bộ evidence, các quyết định đã/chưa chốt và phase gate cho validation trên dữ liệu dự án.

- [`docs/logs/validation/`](logs/validation/) — Nhật ký và quy chuẩn thử nghiệm, kiểm định trên tập dữ liệu thực tế:
  - [`0001_manual_annotation_protocol.md`](logs/validation/0001_manual_annotation_protocol.md) — Hướng dẫn thiết kế tập đánh giá (Evaluation Set) và quy chuẩn gán nhãn thủ công (Ground Truth).

---
## 4. Reports & Deliverables (Cấp Thư mục)

- `reports/templates/` — Các biểu mẫu học phần DAP391m (Research Proposal, Project Planning, Weekly Report, Slide Sample).
- `reports/md/` — Các bản thảo báo cáo, đề cương nghiên cứu dạng Markdown phục vụ nghiệm thu.
  - [`research_proposal_draft.md`](../reports/md/research_proposal_draft.md) — Bản nháp Research Proposal: abstract, literature review, gap, objectives, scope, feasibility, approach & method, expected results; các điểm chưa chốt gom ở Phụ lục A.
