# Ý tưởng Ứng dụng & Ràng buộc Môn học DAP391m

- **Ngày ghi:** 2026-09-21
- **Loại tài liệu:** Nhật ký khám phá (exploratory log) — **KHÔNG phải quyết định kiến trúc**
- **Trạng thái:** **Chưa quyết định thay đổi gì.** Không ban hành RDR, không đổi phạm vi đề tài, không đổi pipeline hiện tại, không cam kết nhóm sẽ xây ứng dụng nào.

> **Cảnh báo thẩm quyền:** Ghi chú này **không** phải nguồn sự thật. Nguồn sự thật vẫn là các quyết định trong `docs/decisions/` (`RDR-NNNN`, số lớn nhất thắng). Mọi nội dung dưới đây chỉ là phương án để bàn.

---

## 1. Vì sao ghi lại

Đọc `reports/templates/DAP391m_Guide_FA26.pdf` cho thấy **môn học bắt buộc có artifact ứng dụng AI**, nên đây không phải hạng mục mở rộng tự nguyện. Câu hỏi chưa chốt chỉ là **xây ứng dụng nào**, không phải **có xây hay không**.

Đồng thời phát hiện một **khoảng trống cấu trúc** giữa đề tài hiện tại và yêu cầu Bước 5 của môn — ghi lại ở Mục 3.

---

## 2. Ràng buộc rút từ guide (dùng làm checklist nội bộ)

### 2.1. Ba thành phần điểm

| Thành phần | Trọng số | Nội dung |
| --- | --- | --- |
| PBL | 40% | Pipeline dữ liệu, ≥5 mô hình so baseline, dịch vụ đám mây, ứng dụng |
| RBL | 30% | RQ, đọc ≥3 bài báo, Research Proposal (tuần 3), Final Report mẫu Springer |
| AI Reflection | 30% | 15–20 core prompt, ≥3 hallucination, Human Delta 4 chiều — **nộp theo từng cá nhân** |

### 2.2. Rubric 8 tiêu chí (thang 100)

Report 20 · Business/Data 5 · Python 10 · Advanced Viz 10 · Model 15 · Services 10 · App 10 · Q&A 20.

**Hai tiêu chí Services + App = 20 điểm** và là phần khác biệt so với ADY201m.

### 2.3. Sáu bước bắt buộc

| Bước | Yêu cầu tối thiểu |
| --- | --- |
| B1 Business + Data | Problem Statement, 6 RQ, Data Dictionary, nguồn có bài báo mô tả |
| B2 Prep + SQL nâng cao | Notebook ghi số dòng trước/sau mỗi thao tác; SQL có window function hoặc CTE gắn RQ |
| B3 Viz nâng cao | ≥3 biểu đồ nâng cao, mỗi hình một insight, **dashboard tương tác** |
| B4 Services API | Endpoint trả JSON, **một cảnh báo thật đã nhận**, sơ đồ kiến trúc |
| B5 Model | **≥5 mô hình, có một mô hình học sâu**, so baseline, tuning, cross-validation |
| B6 App | Ứng dụng demo được, bảng RQ → quyết định, nêu hạn chế |

### 2.4. Checklist thiết kế ứng dụng (Bảng 37)

1. Mọi tính năng dựa trên kết quả mô hình, không rời rạc
2. Hiển thị dự báo **kèm giải thích** (SHAP, Grad-CAM) **và khuyến nghị**
3. Có tương tác: lọc, drill-down hoặc hỏi đáp
4. **Cảnh báo khi vượt ngưỡng hoạt động thật**
5. Bảo mật credential bằng IAM role hoặc biến môi trường
6. Demo được khi vấn đáp, không chỉ mock

### 2.5. Dịch vụ tối thiểu phải chạy thật

Ba việc: **phục vụ mô hình qua endpoint** · **một cảnh báo** · **một kênh hỏi đáp**.

Kiến trúc tham chiếu (Hình 22): Ứng dụng → API Gateway → Lambda (tiền xử lý, logic, cảnh báo) → Endpoint mô hình; kết quả lưu bảng dữ liệu → SNS cảnh báo + Lex/Transcribe hỏi đáp. Không gọi endpoint trực tiếp bằng khoá cứng.

### 2.6. Mốc thời gian

10 tuần · Review 1/2/3 ở tuần 5/7/9 do giảng viên khác chấm chéo · chấm hội đồng tuần 11 · **không đổi đề sau tuần 2**.
Sản phẩm cuối: Final Report 10–12 trang tiếng Anh mẫu Springer Nature + slide 22 trang tiếng Anh.
6 RQ: 3 do giảng viên gợi ý (tuần 1–4) + 3 do nhóm tự đặt (tuần 6–9).

---

## 3. Khoảng trống phát hiện được

**Bước 5 yêu cầu ≥5 mô hình dự báo, trong đó có một mô hình học sâu.** Thiết kế nghiên cứu hiện tại của nhóm dừng ở **WMLR / Ordered Logit** — đây là mô hình kinh tế lượng giải thích, không phải mô hình dự báo, và chỉ có một mô hình.

Hệ quả nếu giữ nguyên:
- Mất gần trọn 15 điểm tiêu chí Model.
- Bước 4 không có mô hình nào để gọi endpoint → ảnh hưởng tiếp 10 điểm Services.
- Bước 6 không có gì để gắn vào ứng dụng → ảnh hưởng tiếp 10 điểm App.

**Kết luận tạm:** cần bổ sung một **nhánh dự báo** bên cạnh nhánh đo lường. Nhánh này không phá đề tài — nó tạo ra chính đại lượng cần nghiên cứu (phần dư giữa điểm thực tế và điểm dự báo từ văn bản).

---

## 4. Ý tưởng ứng dụng đề xuất: Fair-Value Rating Radar

> Tách hai thứ mà các OTA đang gộp làm một: **điểm khách bấm** (observed rating) và **điểm mà nội dung review biện minh được** (text-implied rating).

**Người dùng:** quản lý vận hành / revenue manager khách sạn.

**Ba quyết định ứng dụng phải hỗ trợ:**

| Quyết định | Dữ liệu app đưa ra |
| --- | --- |
| Khách sạn tôi đang được điểm cao hơn thực lực bao nhiêu? | Chênh lệch giữa điểm thực tế và điểm dự báo từ văn bản |
| Khoản chênh đó đến từ khía cạnh nào? | Signed aspect discrepancy $D_{i,a}$ theo từng khía cạnh |
| Sắp tới nên đầu tư vào đâu — CapEx hay đào tạo? | Xếp hạng khía cạnh **được tha thứ** so với **bị trừng phạt** |

### 4.1. Hai họ mô hình — phải tách, đây là chỗ dễ sai nhất

| | Họ A — Rating predictor | Họ B — Tín hiệu aspect |
| --- | --- | --- |
| Nhiệm vụ | Dự đoán `score` từ văn bản | Cảm xúc cấp khía cạnh |
| Huấn luyện trên | **Nhãn sao** | **Nhãn span cảm xúc do người gán** (108.598 span, `origin: manual`) |
| Dùng cho | Bước 5, tính "fair value", sensitivity analysis | Phép đo bất nhất — RQ2, RQ3 |
| Lý do tách | — | Nếu lấy họ A làm thước đo cảm xúc thì vi phạm yêu cầu cốt lõi của đề tài (không dùng rating để huấn luyện sentiment estimator); hệ số hồi quy sẽ tái tạo lại chính biến phụ thuộc |

### 4.2. Ánh xạ 6 bước → sản phẩm cụ thể

| Bước | Sản phẩm cho đề tài này |
| --- | --- |
| B1 | Problem Statement: điểm sao mất tính đại diện vì khách vị tha hoặc trừng phạt. Data Dictionary cho JSON của Label Studio, giải thích `meta_info` và phân biệt `annotations` với `drafts`. 3 bài baseline đã có sẵn trong `refs/INDEX.md` |
| B2 | SQL dùng window function + CTE: tỷ lệ review bất nhất theo khách sạn, `LAG` so quý trước, `RANK` xếp khách sạn theo punitive rate |
| B3 | **Sankey** (khía cạnh → hướng cảm xúc → nhóm chênh lệch) · **Radar** (hồ sơ 6 khía cạnh của một khách sạn) · **Choropleth/Folium** (rủi ro trừng phạt theo 50 địa điểm) · **Heatmap** (khía cạnh × mức sao) · **Word Cloud** (span tiêu cực theo khía cạnh) |
| B4 | SageMaker endpoint phục vụ họ A · Lambda tiền xử lý span và tính $D$ · API Gateway · DynamoDB lưu điểm · **SNS cảnh báo** khi punitive count vượt ngưỡng · Lex + Transcribe cho hỏi đáp |
| B5 | Họ A dự đoán `score`: TF-IDF + Logistic Regression · TF-IDF + SVM · LightGBM · BiLSTM · **DeBERTa** (học sâu). Metric macro-F1 và PR-AUC, **không dùng accuracy** |
| B6 | Streamlit hoặc Dash: radar khách sạn, hàng đợi review rủi ro, highlight span gây lệch, chatbot, hàng chờ cảnh báo |

**Ghi chú về yêu cầu "giải thích dự báo" (checklist #2):** dữ liệu đã có `start` / `end` / `text` cho từng span, nên chỉ cần tô sáng span trong câu gốc. Cách này thuyết phục hơn SHAP và gần như không tốn công triển khai.

---

## 5. Bẫy rò rỉ dữ liệu — đã xác minh trực tiếp trên `data/TripAdvisor_EN.json`

| # | Bẫy | Số liệu xác minh | Cách chặn |
| --- | --- | --- | --- |
| 1 | **Rò rỉ theo khách sạn** | **2.622 khách sạn**; cao nhất **85 review/khách sạn** | `GroupShuffleSplit` theo `hotel name` hoặc `id_url`. Chia ngẫu nhiên để cùng khách sạn nằm cả train lẫn test |
| 2 | **Rò rỉ nhãn qua span `Branding`** | **1.339 span** khách tự viết số sao (*"give 5 star"*, *"would personally rate 2 stars"*) | Xóa trước khi đưa vào mô hình |
| 3 | **Lệch lớp cực nặng** | 5 sao = **7.148/9.990 = 71,6%** | Không báo accuracy; dùng macro-F1, PR-AUC, class weight hoặc SMOTE **chỉ trên train** |
| 4 | **Trường `drafts`** | **37 bản ghi** có draft; `predictions` = 0; toàn bộ **108.598 span đều `origin: manual`** | Chỉ dùng `annotations`, bỏ `drafts` |
| 5 | **Nhầm `meta_info.star` với nhãn** | `star` = hạng sao khách sạn (`3-star`, `5-star`), **khác** `score` = điểm review | `star` là thuộc tính khách sạn → phải xử lý cùng bẫy #1 |
| 6 | **Chuỗi thời gian** | Dữ liệu trải **2015–2023** | Nếu làm RQ theo thời gian: chia theo mốc thời gian, không shuffle; `lag`/`rolling` chỉ tính từ quá khứ |

Số liệu tham chiếu thêm: 50 địa điểm phân biệt · 54.326 span khía cạnh (Service 19.289 · Facility 12.641 · Experience 9.113 · Amenity 7.651 · Loyalty 4.293 · Branding 1.339) · 54.272 span cảm xúc (Positive 46.772 · Negative 4.508 · Neutral 2.992) · 404 review 5 sao chứa span `Negative` · 199 review 1–2 sao chứa span `Positive` trên tổng 465 review 1–2 sao.

---

## 6. Sáu RQ đề xuất

**Ba RQ kỹ thuật (khớp Bước 5):**

- **RQ4** — Năm mô hình dự đoán điểm sao từ văn bản đạt macro-F1 bao nhiêu, và mô hình học sâu vượt baseline cổ điển bao nhiêu điểm khi chia tập **theo khách sạn** thay vì chia ngẫu nhiên?
- **RQ5** — Phần dư `score − score_dự_báo` phân bố thế nào giữa hai phía điểm, và có ổn định giữa các mức sao không?
- **RQ6** — Có dự đoán được review nào rơi vào nhóm trừng phạt ($D < 0$) từ đặc trưng khía cạnh và severity không?

**Ba RQ nghiên cứu** đã có trong [`notes/project-overview.md`](../../../notes/project-overview.md) mục 3: khám phá hình thái bất nhất · lượng hóa có dấu · kiểm định vai trò điều tiết.

---

## 7. Phạm vi cắt bỏ và thứ tự thực hiện

**Không làm:** booking flow · tài khoản người dùng · multi-tenant SaaS · scraping thời gian thực · app mobile · LLM sinh lời khuyên ở bản đầu.

**Ba ràng buộc:**

1. **Nhánh dự báo (Bước 2–5) không phụ thuộc các quyết định đo lường còn mở** (#8–#12 trong Phụ lục A của proposal). Nhóm bắt đầu Bước 2–5 được ngay, chạy song song với validation study. Chỉ phần hiển thị $D_{i,a}^{signed}$ trong app mới phải chờ `RDR-0003`.
2. **Ưu tiên review:** `RDR-0001` mục 2.2 đặt Review 1 ở tuần 5 với sản phẩm "năm mô hình sơ bộ". Nếu Bước 5 chưa có gì ở tuần 5, điểm On-going Assessment (30 điểm) bị ảnh hưởng trước cả điểm Model.
3. **Chưa ship app trước `RDR-0003`:** xây giao diện trên một công thức đang thay đổi sẽ phải viết lại tầng tính toán.

---

## 8. Ranh giới phạm vi cần quyết định

`AGENTS.md` ghi out-of-scope: *"Xây dựng ứng dụng đặt phòng thương mại đầy đủ (Booking engine full-stack) hoặc hệ thống frontend/backend cho người dùng cuối."*

Ứng dụng đề xuất ở Mục 4 là **công cụ hỗ trợ ra quyết định phục vụ học thuật**, không phải sản phẩm thương mại cho end-user. Hai loại artifact khác nhau về bản chất, nhưng ranh giới này **chưa được ghi nhận trong bất kỳ quyết định nào** và cần chốt tường minh nếu nhóm quyết định đi tiếp.

---

## 9. Việc cần làm để biến ghi chú này thành quyết định

1. Chốt **nhánh dự báo có được thêm vào đề tài hay không** — đây là thay đổi phạm vi, phải do người dùng quyết.
2. Nếu có: cập nhật `AGENTS.md` (bổ sung artifact ứng dụng vào in-scope) và `STATUS.md`.
3. Cập nhật Mục 5 của `reports/md/research_proposal_draft.md` để có nhánh dự báo, và Phụ lục A để thêm các điểm mở #17–#18 (5 mô hình nào · dịch vụ AWS nào).
4. Ban hành RDR riêng cho quyết định này nếu nó ràng buộc công việc về sau.
5. Ghi nhánh dự báo vào `docs/logs/validation/` khi bắt đầu Bước 2.

---

## 10. Đọc thêm

- [`reports/templates/DAP391m_Guide_FA26.pdf`](../../../reports/templates/DAP391m_Guide_FA26.pdf) — nguồn của toàn bộ ràng buộc ở Mục 2 (Bảng 3, 14, 37; Hình 22; chương 4, 6, 7).
- [`notes/project-overview.md`](../../../notes/project-overview.md) — định hướng đề tài và ba RQ nghiên cứu.
- [`reports/md/research_proposal_draft.md`](../../../reports/md/research_proposal_draft.md) — proposal hiện tại và 16 điểm chưa chốt.
- [`docs/logs/validation/0001_manual_annotation_protocol.md`](../validation/0001_manual_annotation_protocol.md) — thiết kế evaluation set và quy chuẩn gán nhãn.
