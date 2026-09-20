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

---

## 3. Logs & Working Notes (Cấp Thư mục)

Khu vực ghi lại tiến trình tư duy, khảo sát văn hiến và nhật ký thử nghiệm (không áp dụng giới hạn 200 dòng):

- [`docs/logs/brainstorm/`](logs/brainstorm/) — Nhật ký phát triển ý tưởng, bóc tách bài báo gốc và định hình đề tài:
  - [`0001_root_idea.md`](logs/brainstorm/0001_root_idea.md) — Phân tích bài báo gốc (IJHM 2026) và định hướng Sentiment–Rating Inconsistency.
- [`docs/logs/literature-survey/`](logs/literature-survey/) — Nhật ký khảo sát các bài báo liên quan, phân tích đối chứng và tổng quan lý thuyết.

---

## 4. Reports & Deliverables (Cấp Thư mục)

- `reports/templates/` — Các biểu mẫu học phần DAP391m (Research Proposal, Project Planning, Weekly Report, Slide Sample).
- `reports/md/` — Các bản thảo báo cáo, đề cương nghiên cứu dạng Markdown phục vụ nghiệm thu.
