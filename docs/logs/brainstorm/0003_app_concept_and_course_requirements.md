# Nhật ký Hướng ứng dụng & Ràng buộc Môn học DAP391m

- **Ngày ghi:** 2026-09-21 · **Cập nhật và chốt:** 2026-09-22
- **Loại tài liệu:** Nhật ký khám phá + ghi nhận quyết định **hướng ứng dụng** (không phải `RDR`)
- **Trạng thái:** **ĐÃ CHỐT — Hướng app 1: Bảng soát điểm sao.** Không đổi câu hỏi nghiên cứu; một **nhánh dự báo** được thêm vào để đáp ứng Bước 5 của môn.
- **Phạm vi ảnh hưởng:** thêm artifact ứng dụng vào sản phẩm đầu ra; thêm họ mô hình dự báo. Không đổi dữ liệu, không đổi RQ, không thay công thức đo lường. RQ3 đã được chốt riêng theo [`RDR-0004`](../../decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md) ngày 2026-09-23.

> **Cảnh báo thẩm quyền:** nguồn sự thật vẫn là các quyết định trong `docs/decisions/` (`RDR-NNNN`, số lớn nhất thắng). Tài liệu này ghi **lý do và bằng chứng** cho lựa chọn ứng dụng, không thay thế `RDR`.

---

## 1. Vì sao ghi lại

Đọc `reports/templates/DAP391m_Guide_FA26.pdf` cho thấy **môn học bắt buộc có artifact ứng dụng AI** — đây không phải hạng mục mở rộng tự nguyện. Câu hỏi cần chốt không phải *có xây hay không*, mà là **xây cái gì**, và **chốt cái gì trước tuần 4** vì guide ghi không đổi đề sau tuần 2.

Đồng thời phát hiện khoảng trống giữa đề tài hiện tại và Bước 5 (Mục 3), và một ranh giới phạm vi chưa được ghi nhận tường minh (Mục 9.1).

---

## 2. Ràng buộc rút từ guide

### 2.1. Ba thành phần điểm

| Thành phần | Trọng số | Nội dung |
| --- | --- | --- |
| PBL | 40% | Pipeline dữ liệu, ≥5 mô hình so baseline, dịch vụ đám mây, ứng dụng |
| RBL | 30% | RQ, đọc ≥3 bài báo, Research Proposal (tuần 3), Final Report mẫu Springer |
| AI Reflection | 30% | 15–20 core prompt, ≥3 hallucination, Human Delta 4 chiều — **nộp theo từng cá nhân** |

### 2.2. Rubric 8 tiêu chí (thang 100)

Report 20 · Business/Data 5 · Python 10 · Advanced Viz 10 · Model 15 · Services 10 · App 10 · Q&A 20.

**Services + App = 20 điểm**, và cùng với Model (15) tạo thành **35 điểm** phụ thuộc trực tiếp vào artifact ứng dụng.

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

### 2.5. Ba dịch vụ tối thiểu phải chạy thật

**Phục vụ mô hình qua endpoint · một cảnh báo · một kênh hỏi đáp.**

Kiến trúc tham chiếu (Hình 22): Ứng dụng → API Gateway → Lambda (tiền xử lý, logic, cảnh báo) → Endpoint mô hình; kết quả lưu bảng dữ liệu → SNS cảnh báo + Lex/Transcribe hỏi đáp. Không gọi endpoint trực tiếp bằng khoá cứng.

### 2.6. Mốc thời gian

10 tuần · Review 1/2/3 ở tuần 5/7/9 do giảng viên khác chấm chéo · chấm hội đồng tuần 11 · **không đổi đề sau tuần 2**.
Sản phẩm cuối: Final Report 10–12 trang tiếng Anh mẫu Springer Nature + slide 22 trang tiếng Anh.
6 RQ: 3 do giảng viên gợi ý (tuần 1–4) + 3 do nhóm tự đặt (tuần 6–9).

### 2.7. Khi hết tín dụng

Được chạy mock cục bộ bằng FastAPI **cùng giao diện JSON** với endpoint thật, nhưng phải khai rõ trong Audit Log và báo cáo, và **phải chứng minh đã từng gọi endpoint thật** bằng log hoặc ảnh chụp có thời gian.

---

## 3. Khoảng trống: Bước 5 không khớp thiết kế nghiên cứu hiện tại

Bước 5 yêu cầu **≥5 mô hình dự báo, có một mô hình học sâu**. Thiết kế nghiên cứu hiện tại dừng ở **WMLR / Ordered Logit** — mô hình kinh tế lượng giải thích, không phải mô hình dự báo, và chỉ có một mô hình.

Hệ quả nếu giữ nguyên: mất gần trọn 15 điểm Model · Bước 4 không có mô hình để gọi endpoint (ảnh hưởng 10 điểm Services) · Bước 6 không có gì gắn vào ứng dụng (ảnh hưởng 10 điểm App).

**Cách giải quyết đã chốt:** bổ sung một **nhánh dự báo** bên cạnh nhánh đo lường. Nhánh này không phá đề tài — nó tạo ra chính đại lượng cần nghiên cứu (phần dư giữa điểm thực tế và điểm dự báo từ văn bản).

**Hai họ mô hình phải tách, đây là chỗ dễ sai nhất:**

| | Họ A — Rating predictor | Họ B — Tín hiệu aspect |
| --- | --- | --- |
| Nhiệm vụ | Dự đoán `score` từ văn bản | Cảm xúc cấp khía cạnh |
| Huấn luyện trên | Nhãn sao | Span cảm xúc do người gán |
| Dùng cho | Bước 5, tính phần dư, sensitivity analysis | Phép đo bất nhất — RQ2, RQ3 |
| Lý do tách | — | Nếu lấy họ A làm thước đo cảm xúc thì vi phạm yêu cầu cốt lõi của đề tài; hệ số hồi quy sẽ tái tạo lại chính biến phụ thuộc |

**Ba RQ kỹ thuật sinh ra từ nhánh dự báo (khớp Bước 5):**

- **RQ4** — Năm mô hình dự đoán điểm sao từ văn bản đạt macro-F1 bao nhiêu, và mô hình học sâu vượt baseline cổ điển bao nhiêu điểm khi chia tập **theo khách sạn** thay vì chia ngẫu nhiên?
- **RQ5** — Phần dư `score − score_dự_báo` phân bố thế nào giữa hai phía điểm, và có ổn định giữa các mức sao không?
- **RQ6** — Có dự đoán được review nào rơi vào nhóm trừng phạt ($D < 0$) từ đặc trưng khía cạnh và severity không?

Ba RQ nghiên cứu đã có trong [`notes/project_overview.md`](../../../notes/project_overview.md) mục 3: khám phá hình thái bất nhất · lượng hóa có dấu · kiểm định vai trò điều tiết.

---

## 4. Quyết định: Hướng app 1 — Bảng soát điểm sao

> Tách hai thứ mà các OTA đang gộp làm một: **điểm khách bấm** (observed rating) và **điểm mà nội dung review biện minh được** (text-implied rating).

**Người dùng:** quản lý vận hành / revenue manager khách sạn.

**Ba quyết định ứng dụng phải hỗ trợ:**

| Quyết định | Dữ liệu app đưa ra |
| --- | --- |
| Khách sạn đang được điểm cao hơn thực lực bao nhiêu? | Chênh lệch giữa điểm thực tế và điểm dự báo từ văn bản |
| Khoản chênh đó đến từ khía cạnh nào? | Signed aspect discrepancy $D_{i,a}$ theo từng khía cạnh |
| Sắp tới nên đầu tư vào đâu — CapEx hay đào tạo? | Xếp hạng khía cạnh **được tha thứ** so với **bị trừng phạt** |

**Cấu trúc màn hình:**

```
┌─ SOÁT ĐIỂM SAO ──────────────────────────────────┐
│ Khách sạn: [Sofitel Legend Metropole ▾] Năm:[▼]  │
│                                                  │
│ 4.0★ thực tế │ 3.2★ văn bản biện minh │  +0.8★   │
│                                                  │
│ Review #131571                                   │
│ "…beds were so comfortable…"        ← tích cực   │
│ "…wait staff were very slow…"       ← tiêu cực   │
│ → khách cho cao hơn nội dung 0.8 sao             │
│                                                  │
│ 3 review tương tự tháng này · ⚠ đã gửi cảnh báo  │
└──────────────────────────────────────────────────┘
```

**Bốn khối chức năng:**

1. Tra một review: dán văn bản → mô hình A dự đoán `score` + độ tin cậy.
2. Tô sáng span tích cực/tiêu cực trên câu gốc, tách theo khía cạnh — dữ liệu đã có `start`/`end`/`text`, nên đây vừa là phần "giải thích dự báo" của checklist #2, vừa rẻ hơn SHAP.
3. Kết luận lệch: điểm thực tế cao hơn hay thấp hơn mức văn bản biện minh, kèm $D$ theo khía cạnh.
4. Hàng đợi cảnh báo + email SNS khi tỷ lệ review bị trừng phạt của một khách sạn vượt ngưỡng; ô hỏi đáp Lex trả lời các câu hỏi kiểu "khách sạn X có bao nhiêu review bị trừng phạt trong 2023?".

**Đơn vị phân tích:** cấp **review và khía cạnh**. Chỉ hiển thị tổng hợp cấp khách sạn cho khách sạn đủ mẫu (≥20 review) — xem Mục 6.3.

### 4.1. Ánh xạ sáu bước → sản phẩm cụ thể

| Bước | Sản phẩm cho đề tài này |
| --- | --- |
| B1 | Problem Statement: điểm sao mất tính đại diện vì một phần khách chấm lệch với nội dung. Data Dictionary cho JSON của Label Studio, giải thích `meta_info` và phân biệt `annotations` với `drafts`. Ba bài baseline đã có sẵn trong [`refs/INDEX.md`](../../../refs/INDEX.md) |
| B2 | SQL dùng window function + CTE: tỷ lệ review bất nhất theo khách sạn, `LAG` so quý trước, `RANK` xếp khách sạn theo punitive rate |
| B3 | Sankey (khía cạnh → hướng cảm xúc → nhóm chênh lệch) · cột lệch theo khía cạnh · Choropleth/Folium (50 địa điểm) · Heatmap (khía cạnh × mức sao) · Word Cloud (span tiêu cực theo khía cạnh). **Không dùng radar** — lý do ở Mục 6 |
| B4 | SageMaker endpoint phục vụ họ A · Lambda tiền xử lý span và tính $D$ · API Gateway · DynamoDB lưu điểm · **SNS cảnh báo** khi punitive count vượt ngưỡng · Lex + Transcribe cho hỏi đáp |
| B5 | Họ A dự đoán `score`: TF-IDF + Logistic Regression · TF-IDF + SVM · LightGBM · BiLSTM · **DeBERTa** (học sâu). Metric macro-F1 và PR-AUC, **không dùng accuracy** |
| B6 | Streamlit hoặc Dash: ô tra một review, danh sách review rủi ro, highlight span gây lệch, chatbot, hàng chờ cảnh báo |

---

## 5. Các phương án đã cân nhắc và lý do chọn/loại

| Phương án | Mô tả | Kết luận |
| --- | --- | --- |
| **1 — Bảng soát điểm sao** | Màn hình chọn khách sạn → xem ca lệch → tô sáng span → hàng đợi cảnh báo | **CHỐT** |
| 2 — Tra một review | Chỉ một ô dán văn bản, trả điểm dự báo + phán quyết lệch | **Gộp vào 1** như tab tra cứu — dùng chung tầng dưới, demo vấn đáp rất mạnh |
| 3 — Hồ sơ radar theo khách sạn | Đa giác 6 khía cạnh cho từng khách sạn | **LOẠI** — lý do ở Mục 6.2 và 6.3 |
| 4 — Ghép 2 + 3 | Hai tab, radar xây sau khi công thức đo lường được chốt | **LOẠI** — không xóa được rủi ro, chỉ giới hạn thiệt hại; mà radar vốn không cần thiết |

**Phương án 3 bị loại vì hai lý do độc lập:**

- **Phụ thuộc công thức đo lường:** radar 6 cạnh chỉ vẽ được nếu công thức thắng là **Signed Aspect Gap $r^*-s_a^*$** (có một số cho từng khía cạnh). Nếu thắng là **3×3 Polarity Matrix** (chỉ có nhãn hướng) hoặc **$z(r)-z(s)$** (một số cho cả review) thì không có số theo khía cạnh để vẽ. Khung app phải có tuần 4, còn công thức chỉ được chốt sau validation study — tức là quyết định bị đặt cược trước khi biết kết quả.
- **Không có thông tin để hiển thị:** xem Mục 6.3 — phần lớn khách sạn cho ra hình gần tròn.

---

## 6. Bằng chứng số (tự tính trên `data/TripAdvisor_EN.json`, 2026-09-22)

### 6.1. Quy mô

| Chỉ số | Giá trị |
| --- | ---: |
| Review | 9.990 |
| Khách sạn | 2.622 (cao nhất 85 review/khách sạn) |
| Địa điểm | 50 |
| Giai đoạn | 2015–2023 |
| Phân bố điểm | 1★ 228 · 2★ 237 · 3★ 601 · 4★ 1.776 · **5★ 7.148 (71,6%)** |
| Span khía cạnh (`entities`) | 54.326 |
| Span cảm xúc (`entity_sentiment`) | 54.272 (Positive 46.772 · Negative 4.508 · Neutral 2.992) |

### 6.2. Số khía cạnh phân biệt trong một review

| Số khía cạnh | Số review |
| ---: | ---: |
| 0 | 123 |
| 1 | 293 |
| 2 | 1.492 |
| 3 | 3.488 |
| 4 | 3.347 |
| 5 | 1.170 |
| 6 | **77** |

Trung vị 3 khía cạnh; chỉ **0,8%** review phủ đủ 6 khía cạnh. Radar một review vì thế là một tam giác, và 1.492 review hai khía cạnh cho ra hình nêm dẹp — trong khi thư viện vẽ coi khía cạnh không nhắc tới là **0**, tức "tệ nhất", khác hoàn toàn với "không nhắc tới".

### 6.3. Độ trải hồ sơ ở cấp khách sạn

Tính trên 76 khách sạn có ≥20 review (net sentiment theo khía cạnh = (positive − negative) / tổng):

- Độ trải trung vị (max − min giữa các khía cạnh): **0,26**
- **46/76 khách sạn có độ trải < 0,3** → hình gần tròn, giống nhau
- Ví dụ Khu nghỉ dưỡng Salinda Phú Quốc: Service 0,90 · Facility 0,90 · Amenity 1,00 · Experience 0,70 · Loyalty 1,00 · Branding 0,71

Nguyên nhân: corpus 71,6% là 5 sao và span tích cực nhiều gấp ~10 lần tiêu cực, nên cảm xúc ròng gần +1 ở mọi khía cạnh.

### 6.4. Phân bố tiêu cực theo khía cạnh — nơi thông tin thật nằm

| Khía cạnh | Tổng span | % tiêu cực |
| --- | ---: | ---: |
| Branding | 1.337 | 17,1% |
| Facility | 12.636 | 12,9% |
| Experience | 9.098 | 9,6% |
| Service | 19.268 | 6,4% |
| Loyalty | 4.287 | 4,8% |
| Amenity | 7.644 | 4,5% |

Chênh nhau ~4 lần. Radar vẽ cảm xúc ròng nên **che mất** khác biệt này; biểu đồ cột lệch hiện ra ngay.

### 6.5. Bộ ca đáng ngờ và ứng viên demo

| Tập | Số lượng |
| --- | ---: |
| Review 5★ chứa ≥1 span `Negative` | 404 |
| Review 1–2★ chứa ≥1 span `Positive` | 199 |
| **Tổng ca đáng ngờ** | **603**, trải trên **468 khách sạn** |
| Ca đáng ngờ nằm trong khách sạn ≥20 review | 130, tại 58 khách sạn |

Top ứng viên demo (đủ mẫu và có ca đáng ngờ):

```
8 ca đáng ngờ / 85 review   Sofitel Legend Metropole Hà Nội
6 ca đáng ngờ / 39 review   Anantara Hội An Resort
4 ca đáng ngờ / 31 review   Khu nghỉ dưỡng Salinda Phú Quốc
4 ca đáng ngờ / 60 review   Lavender Central Hotel & Spa
4 ca đáng ngờ / 30 review   Indochine Palace (Huế)
```

Lưu ý: giới hạn ≥20 review **chỉ áp cho phần tổng hợp cấp khách sạn**. Tra một review và danh sách ca đáng ngờ hoạt động trên toàn bộ 9.990 review / 2.622 khách sạn.

---

## 7. Bẫy rò rỉ dữ liệu — đã xác minh trực tiếp

| # | Bẫy | Số liệu xác minh | Cách chặn |
| --- | --- | --- | --- |
| 1 | **Rò rỉ theo khách sạn** | 2.622 khách sạn; cao nhất 85 review/khách sạn | `GroupShuffleSplit` theo `hotel name` hoặc `id_url`, không chia ngẫu nhiên |
| 2 | **Rò rỉ nhãn qua span `Branding`** | 1.339 span khách tự viết số sao (*"give 5 star"*) | Xóa trước khi đưa vào mô hình |
| 3 | **Lệch lớp cực nặng** | 5 sao = 7.148/9.990 = 71,6% | Không báo accuracy; dùng macro-F1, PR-AUC, class weight hoặc SMOTE **chỉ trên train** |
| 4 | **Trường `drafts`** | 37 bản ghi có draft; `predictions` = 0; toàn bộ 108.598 span đều `origin: manual` | Chỉ dùng `annotations`, bỏ `drafts` |
| 5 | **Nhầm `meta_info.star` với nhãn** | `star` = hạng sao khách sạn (`3-star`, `5-star`), khác `score` = điểm review | `star` là thuộc tính khách sạn → xử lý cùng bẫy #1 |
| 6 | **Chuỗi thời gian** | Dữ liệu trải 2015–2023 | Nếu làm RQ theo thời gian: chia theo mốc thời gian, không shuffle; `lag`/`rolling` chỉ tính từ quá khứ |

**Tên control trong Label Studio JSON** (đã kiểm): khía cạnh là `entities`, cảm xúc là `entity_sentiment`. Hai control độc lập, khớp nhau bằng cặp `start`/`end`.

---

## 8. Thiết kế trực quan thay thế radar

| Mục đích | Biểu đồ | Phụ thuộc công thức đo lường? |
| --- | --- | --- |
| Khía cạnh nào bị chê nhiều | **Cột lệch** (khen/chê hai phía quanh trục) | Không — dựng trên span người gán |
| Khía cạnh × mức sao | **Heatmap** | Không |
| Theo tỉnh/thành | **Choropleth** (50 địa điểm) | Không |
| Luồng khía cạnh → hướng cảm xúc → nhóm lệch | **Sankey** | Có, ở nhánh phân nhóm lệch |
| Từ ngữ trong span tiêu cực | **Word Cloud** | Không |
| Review bị lệch | Tô sáng span trong câu gốc | Có, ở phần kết luận lệch |

CLO4 của guide liệt kê Waffle, Area, Histogram, Bar, Pie, Scatter, Word Cloud, Choropleth — **radar không nằm trong danh sách**, nên bỏ radar không mất điểm nào.

---

## 9. Phạm vi và điểm mở

### 9.1. Ranh giới phạm vi

`AGENTS.md` ghi out-of-scope: *"Xây dựng ứng dụng đặt phòng thương mại đầy đủ (Booking engine full-stack) hoặc hệ thống frontend/backend cho người dùng cuối."*

Ứng dụng đã chốt là **công cụ hỗ trợ ra quyết định phục vụ học thuật**, không phải sản phẩm thương mại cho end-user. Hai loại artifact khác bản chất, nhưng ranh giới này cần được ghi nhận tường minh trong `AGENTS.md` hoặc một `RDR` để các lần review sau không phải tranh luận lại.

### 9.2. Không làm

Booking flow · tài khoản người dùng · multi-tenant SaaS · scraping thời gian thực · app mobile · LLM sinh lời khuyên ở bản đầu.

### 9.3. Ba ràng buộc thứ tự thực hiện

1. **Nhánh dự báo (Bước 2–5) không phụ thuộc các quyết định đo lường còn mở** (Phụ lục A của proposal). Chạy song song với validation study. Chỉ phần hiển thị $D^{signed}_{i,a}$ mới phải chờ công thức đo lường được chốt.
2. **Ưu tiên review:** Review 1 ở tuần 5 cần "năm mô hình sơ bộ". Nếu Bước 5 trống ở tuần 5, điểm On-going Assessment (30 điểm) bị ảnh hưởng trước cả điểm Model.
3. **Chưa ship phần hiển thị $D$ trước khi công thức đo lường được chốt:** xây giao diện trên một công thức đang thay đổi sẽ phải viết lại tầng tính toán.

### 9.4. Việc tiếp theo

1. Cập nhật `AGENTS.md` (artifact ứng dụng vào in-scope) và `STATUS.md` theo quyết định này.
2. Cập nhật Mục 5 của `reports/md/research_proposal_draft.md` để có nhánh dự báo; thêm điểm mở #17–#18 vào Phụ lục A (chọn 5 mô hình nào · chọn AWS hay GCP).
3. Chốt 5 mô hình cho Bước 5: TF-IDF + Logistic · TF-IDF + SVM · LightGBM · BiLSTM · **DeBERTa** (học sâu), metric macro-F1 và PR-AUC.
4. Dựng khung app + endpoint sớm (mục tiêu tuần 4); làm cảnh báo SNS sớm vì đây là thứ duy nhất không thể mock.
5. Ghi nhánh dự báo vào `docs/logs/validation/` khi bắt đầu Bước 2.

---

## 10. Đọc thêm

- [`reports/templates/DAP391m_Guide_FA26.pdf`](../../../reports/templates/DAP391m_Guide_FA26.pdf) — nguồn của toàn bộ ràng buộc Mục 2 (Bảng 3, 14, 37; Hình 22; tr.25–33).
- [`notes/project_overview.md`](../../../notes/project_overview.md) — định hướng đề tài và các RQ nghiên cứu.
- [`notes/reference_map.md`](../../../notes/reference_map.md) — ref nào dùng cho phần nào, trạng thái full text.
- [`reports/md/research_proposal_draft.md`](../../../reports/md/research_proposal_draft.md) — proposal hiện tại và các điểm chưa chốt.
- [`docs/logs/validation/0001_manual_annotation_protocol.md`](../validation/0001_manual_annotation_protocol.md) — thiết kế evaluation set và quy chuẩn gán nhãn.
- [`docs/decisions/RDR-0003_review_and_reset_survey.md`](../../decisions/RDR-0003_review_and_reset_survey.md) — quyết định mở lại khảo sát và tái định hình RQ3.
- [`docs/decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md`](../../decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md) — quyết định chốt RQ3 và bốn kiểm định phụ.
