# Documentation Router (docs/INDEX.md)

Tài liệu này là Router đơn (Single Router) phân tầng điều hướng toàn bộ tài liệu dự án. Mọi Agent bắt đầu tra cứu từ file này.

---

## 1. Core Context Files (Cốt lõi - Cấp File)

- [`README.md`](../README.md) — Điểm vào cho người đọc: đề tài một câu, cấu trúc thư mục, lấy dữ liệu ở đâu và checksum, quy ước nhánh.
- [`RULES.md`](../RULES.md) — Quy tắc vận hành, ngân sách dòng ($\le 200$ dòng), kỷ luật Git, Single Source of Truth, và **luật nhật ký** (nhật ký bất biến — đính chính bằng cách chèn dòng, không sửa nội dung cũ).
- [`AGENTS.md`](../AGENTS.md) — Định vị đề tài, phạm vi In-scope / Out-of-scope và thứ tự đọc tài liệu.
- [`STATUS.md`](../STATUS.md) — Ảnh chụp trạng thái **cấp dự án** ($\le 40$ dòng). Chỉ sửa khi có `RDR` mới, đổi pha, hoặc chốt RQ.
- [`docs/BACKLOG.md`](BACKLOG.md) — Việc **đang mở** ở cấp dự án. Xong thì đổi trạng thái, không xoá dòng.
- [`refs/INDEX.md`](../refs/INDEX.md) — Danh mục tài liệu tham khảo và thư viện bài báo khoa học.

---

## 2. Architecture & Decision Records (Cấp File)

Thư mục lưu trữ các quyết định kỹ thuật và kiến trúc theo quy tắc Append-only (`RDR-NNNN`). Quyết định có số hiệu lớn nhất là nguồn sự thật tối cao.

- [`docs/decisions/RDR-0001_endpoint_literature_survey.md`](decisions/RDR-0001_endpoint_literature_survey.md) — Mục tiêu và tiêu chí dừng khảo sát văn hiến (Literature Survey Endpoint).
- [`docs/decisions/RDR-0002_latest_first_literature_scanning.md`](decisions/RDR-0002_latest_first_literature_scanning.md) — Chỉ quét chủ động tài liệu trong cửa sổ 36 tháng mới nhất; nguồn cũ chỉ được truy xuất theo ngoại lệ xác minh provenance.
- [`docs/decisions/RDR-0005_close_survey_and_lock_framework.md`](decisions/RDR-0005_close_survey_and_lock_framework.md) — Đóng khảo sát có điều kiện: miễn tiêu chí bão hòa, định nghĩa lại ba cụm, đóng băng core set, khóa khung lý thuyết, chốt boundary conditions và phạm vi dữ liệu 9.990 review.
- [`docs/decisions/RDR-0003_review_and_reset_survey.md`](decisions/RDR-0003_review_and_reset_survey.md) — Mở lại khảo sát để tái định hình RQ3; ưu tiên journal và nguồn đóng khi quét.
- [`docs/decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md`](decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md) — Chốt RQ3 theo cơ chế asymmetric aspect compensation; chốt bốn kiểm định phụ và danh sách boundary conditions dùng/loại.
- [`docs/decisions/RDR-0006_freeze_negative_span_definition.md`](decisions/RDR-0006_freeze_negative_span_definition.md) — Đóng băng định nghĩa "ca bất nhất" cấp review: loại span gắn `Branding`, giữ `Loyalty` → **394 ca**; khai tử con số 402 không tái lập được, kèm số dẫn xuất tính lại.

---

## 3. Logs & Working Notes (Cấp Thư mục)

Khu vực ghi lại tiến trình tư duy, khảo sát văn hiến và nhật ký thử nghiệm (không áp dụng giới hạn 200 dòng):
- [`notes/project_overview.md`](../notes/project_overview.md) — Bản đồ một trang về đề tài: hướng nghiên cứu, research gap, RQ nháp, sản phẩm đầu ra và lộ trình.
- [`notes/survey_overview.md`](../notes/survey_overview.md) — tổng quan **bốn vòng** khảo sát văn hiến: quy tắc quét, mỗi vòng thu được gì, nhóm có gì sau bốn vòng, khảo sát dừng ở đâu và còn thiếu gì.
- [`notes/reference_map.md`](../notes/reference_map.md) — bản đồ đọc nhanh từng ref: tóm tắt, tác dụng trong đề tài và trạng thái full text/local file.
- [`notes/glossary.md`](../notes/glossary.md) — Từ điển thuật ngữ nghiên cứu: định nghĩa song ngữ toàn bộ khái niệm cốt lõi, lý thuyết hành vi, mô hình ABSA/NLP và công thức đo lường.
- [`notes/pillar_strength.md`](../notes/pillar_strength.md) — Độ mạnh **6 trụ cột bằng chứng** (coverage 45% + evidence 35% + recency 20%), chi tiết từng trụ cột và khoảng trống thước đo discrepancy có dấu ở cấp khía cạnh.
- [`notes/theory/INDEX.md`](../notes/theory/INDEX.md) — **Bốn lớp lý thuyết nền tảng** đã khóa ở `RDR-0005` (S-O-R · Kano/three-factor + IAA/PRCA/AIPA · Prospect Theory · hai giai đoạn non-compensatory → compensatory): vai trò từng lớp, bằng chứng trong `refs/`, câu hỏi bảo vệ và bốn câu không được viết.

- [`docs/logs/progress/`](logs/progress/) — Nhật ký tiến độ theo người: mỗi người một tệp theo ngày, append-only, không sửa tệp của người khác.
- [`docs/logs/brainstorm/`](logs/brainstorm/) — Nhật ký phát triển ý tưởng, bóc tách bài báo gốc và định hình đề tài:
  - [`0001_root_idea.md`](logs/brainstorm/0001_root_idea.md) — Phân tích bài báo gốc (IJHM 2026) và định hướng Sentiment–Rating Inconsistency.
  - [`0002_direction_of_work_after_survey_2.md`](logs/brainstorm/0002_direction_of_work_after_survey_2.md) — Nhật ký hướng triển khai B1–B3 sau Survey Round 2 (EDA dataset → evaluation set → gán nhãn thủ công).
  - [`0003_app_concept_and_course_requirements.md`](logs/brainstorm/0003_app_concept_and_course_requirements.md) — Ràng buộc môn DAP391m, khoảng trống nhánh dự báo, các phương án ứng dụng đã cân nhắc, bằng chứng số loại radar, bẫy rò rỉ dữ liệu đã xác minh và **quyết định chốt hướng app 1 — Bảng soát điểm sao**.
- [`docs/logs/literature_survey/`](logs/literature_survey/) — Nhật ký khảo sát các bài báo liên quan, phân tích đối chứng và tổng quan lý thuyết:
  - [`0001_discrepancy_formulations.md`](logs/literature_survey/0001_discrepancy_formulations.md) — Phân loại các họ phương pháp lượng hóa mâu thuẫn điểm số - bài viết và câu hỏi định hướng khảo sát.
  - [`0002_survey_matrix_round_1.md`](logs/literature_survey/0002_survey_matrix_round_1.md) — Vòng khảo sát đầu tiên: search protocol, ma trận 11 nguồn, theory/measurement/baseline synthesis và endpoint check.
  - [`0003_survey_matrix_round_2.md`](logs/literature_survey/0003_survey_matrix_round_2.md) — Vòng quét latest-first: 6 core candidates mới, operationalization magnitude/direction/aspect conflict, core-set curation và endpoint check.
  - [`0004_synthesis_and_next_step.md`](logs/literature_survey/0004_synthesis_and_next_step.md) — Tổng kết toàn bộ evidence, các quyết định đã/chưa chốt và phase gate cho validation trên dữ liệu dự án.
  - [`0005_survey_matrix_round_3_rq3_rescoping.md`](logs/literature_survey/0005_survey_matrix_round_3_rq3_rescoping.md) — Vòng quét targeted theo RDR-0003: asymmetry, compensatory/non-compensatory decision và các phương án tái định hình RQ3.
  - [`0006_survey_matrix_round_4.md`](logs/literature_survey/0006_survey_matrix_round_4.md) — Round 4 kiểm chứng: 5 cluster targeted, 26 nguồn mới đã xác minh, checkpoint phản biện bắt buộc, kiểm tra tính mới độc lập và đề xuất phân loại cụm.

- [`docs/logs/validation/`](logs/validation/) — Nhật ký và quy chuẩn thử nghiệm, kiểm định trên tập dữ liệu thực tế:
  - [`0001_manual_annotation_protocol.md`](logs/validation/0001_manual_annotation_protocol.md) — Hướng dẫn thiết kế tập đánh giá (Evaluation Set) và quy chuẩn gán nhãn thủ công (Ground Truth).

---
## 4. Reports & Deliverables (Cấp Thư mục)

- `reports/templates/` — Các biểu mẫu học phần DAP391m (Research Proposal, Project Planning, Weekly Report, Slide Sample).
- `reports/md/` — Các bản thảo báo cáo, đề cương nghiên cứu dạng Markdown phục vụ nghiệm thu.
  - [`project_planning.md`](../reports/md/project_planning.md) — Project Planning theo template DAP391m: thông tin nhóm, đề tài và dataset, ba câu hỏi nghiên cứu, ba paper baseline, kế hoạch 10 tuần, phân công, kế hoạch dùng AI và audit log, rủi ro.
  - [`research_proposal.md`](../reports/md/research_proposal.md) — Research Proposal theo template học phần: abstract, literature review, limitations, necessity, objectives, scope, feasibility, approach & method, research plan, expected results.
- `reports/presen/` — Bài trình bày theo từng mốc báo cáo, đặt số thứ tự theo mốc.
  - [`01_progress_report/progress_slide.md`](../reports/presen/01_progress_report/progress_slide.md) — Slide báo cáo tiến độ dạng markdown: đề tài, khoảng trống nghiên cứu, RQ, phương pháp, kết quả khảo sát văn hiến, việc tiếp theo và ứng dụng Bảng soát điểm sao.

