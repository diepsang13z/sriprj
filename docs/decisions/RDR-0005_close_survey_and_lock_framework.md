# RDR-0005: Đóng khảo sát văn hiến & Chốt khung cho Research Proposal

- **Trạng thái:** ACCEPTED
- **Ngày quyết định:** 2026-09-23
- **Người đề xuất:** Nghiên cứu viên
- **Phạm vi áp dụng:** Điểm dừng khảo sát, cấu trúc cụm tài liệu, phạm vi dữ liệu và khung lý thuyết của đề tài
- **Căn cứ:** `RDR-0001` (endpoint), `RDR-0002` (cửa sổ 36 tháng), `RDR-0003` (mở lại khảo sát), `RDR-0004` (chốt RQ3), và [`docs/logs/literature_survey/0006_survey_matrix_round_4.md`](../logs/literature_survey/0006_survey_matrix_round_4.md)

---

## 1. Bối cảnh (Context)

`RDR-0001` đặt 4 tiêu chí dừng khảo sát. Sau Round 3 và Round 4, trạng thái thực tế là:

| # | Tiêu chí | Trạng thái |
| --- | --- | --- |
| 1 | Bão hòa: 3–5 bài mới liên tiếp không sinh lý thuyết/phương pháp mới | **Không đạt, và không thể đạt** |
| 2 | 10–15 bài hạt nhân chia đều 3 cụm | Đạt về số lượng, **sai cấu trúc cụm** |
| 3 | Đủ nguyên liệu viết proposal | Đạt |
| 4 | ≥1 baseline đối chứng | Đạt |

Tiêu chí 1 không đạt vì lý do cấu trúc, không phải vì thiếu nỗ lực: Round 3 sinh thêm Kano/three-factor, Prospect Theory và mô hình hai giai đoạn; Round 4 sinh thêm phân loại Kano từ review, Impact Asymmetry Analysis, AIPA, Service Recovery Paradox, cộng 6 nguồn phản biện. **Cửa sổ 36 tháng theo `RDR-0002` đang sinh công bố liên tục**, nên một tiêu chí viết cho đợt quét rộng sẽ không bao giờ khởi động với các vòng quét targeted.

Đồng thời tiêu chí 2 không còn đúng trên giấy: cụm thứ ba mà `RDR-0001` định nghĩa là *Customer Forgiveness/Buffering*, nhưng `RDR-0004` đã chốt RQ3 không dùng construct forgiveness làm cơ chế trung tâm — cụm đó không còn nội dung.

---

## 2. Quyết định (Decision)

### 2.1. Miễn tiêu chí bão hòa, thay bằng tiêu chí đo được

Tiêu chí 1 của `RDR-0001` được **miễn**, kèm lý do ghi tại Mục 1. Thay bằng tiêu chí:

> **Không còn phát hiện nào làm đổi thiết kế nghiên cứu.**

Round 4 đạt tiêu chí thay thế này: trong 26 nguồn mới được xác minh, **không nguồn nào làm đổi cơ chế hay RQ** — 8 nguồn chỉ thêm ràng buộc diễn giải hoặc phản biện, 18 nguồn bổ sung baseline/kỹ thuật/mốc so sánh.

### 2.2. Định nghĩa lại ba cụm tài liệu

Ba cụm dùng để đánh giá tiêu chí 2 được định nghĩa lại, ánh xạ trực tiếp vào cấu trúc thư mục chức năng của `refs/`:

| Cụm | Thư mục | Nội dung | Số nguồn có toàn văn |
| --- | --- | --- | ---: |
| C1 — Hiện tượng & định nghĩa | `01_root`, `02_definition`, `03_phenomenon` | Bài gốc đối chuẩn, định nghĩa/provenance thước đo, bằng chứng bất nhất | 11 |
| C2 — Cơ chế & điều kiện biên | `04_mechanism`, `05_boundary_conditions` | Lý thuyết bất đối xứng; severity, recovery, hạng sao | 13 |
| C3 — Phản biện, phương pháp & baseline | `06_counter_evidence`, `07_baselines_methods` | Phản biện cơ chế, phê bình công cụ, baseline đối chuẩn | 7 |

`08_legacy` **không tính vào cụm endpoint** — đó là audit trail, không phải nguồn dẫn dắt lập luận.

Cụm Forgiveness/Justice của `RDR-0001` được **bãi bỏ** ở vai trò cụm endpoint.

### 2.3. Đóng băng core set

Core set hiện tại là **31 nguồn có toàn văn** (11 + 13 + 7) cộng 4 tệp audit trail, tổng 35 PDF trong 8 cụm chức năng.

Nguồn còn thiếu toàn văn được chia hai nhóm và **không mở thêm vòng quét rộng**:

- **2 bài truy cập mở tải tay:** Liu et al. (2025, IP&M), Slevitch (2024, JHTR).
- **14 bài đóng, ưu tiên theo mức cần:** Kwon, W. (2026) · Han & Anderson (2025) · Park et al. (2025) · Kirilenko et al. (2024) · Cui et al. (2025) · Kovács (2025) · Tan & Zou (2024) · Mellinas et al. (2025) · Xu et al. (2025) · Zhong et al. (2026) · Albayrak et al. (2025) · Wang, D. et al. (2025) · Doan et al. (2025) · Kumar et al. (2024).

Bổ sung tài liệu sau quyết định này **chỉ** qua citation-chain hoặc full-text audit của nguồn đã nằm trong danh sách, không qua quét chủ đề mới.

### 2.4. Khóa khung lý thuyết

Lớp lý thuyết chính thức của đề tài:

| Lớp | Nguồn |
| --- | --- |
| Khung vĩ mô | **S-O-R** (Le et al., 2026 — kế thừa bài gốc) |
| Cơ chế bất đối xứng | **Kano / three-factor theory** + **Impact Asymmetry / PRCA / AIPA** (Regitz et al., 2026; Park et al., 2025; Zhang et al., 2025; Cui et al., 2025; Li, J. et al., 2025) |
| Cơ chế tâm lý – kinh tế lượng | **Prospect Theory**: loss aversion, diminishing sensitivity, reference point (Sharma et al., 2025) |
| Cấu trúc quyết định | **Non-compensatory → compensatory hai giai đoạn** (Li, S. et al., 2024) |

**Nhánh Forgiveness/Justice bị loại khỏi lớp lý thuyết trung tâm.** Nguồn của nhánh này (Yoruk et al., 2025) nằm ở `08_legacy` và chỉ được nêu trong phần văn hiến như construct liên quan nhưng cố ý không đo.

### 2.5. Boundary conditions chính thức

Boundary conditions đo trên evaluation set là:

1. **Failure severity** — trường `Severity` (`Minor`/`Major`), đã có trong protocol gán nhãn.
2. **Service recovery** — trường `Service_Recovery` (`Yes`/`No`), đã có trong protocol.
3. **Hotel class** — trường `star`, đầy đủ 9.990/9.990 bản ghi.

`trip type` (chỉ 658/9.990 bản ghi có giá trị), `reviewer experience` và `brand equity` (không có biến) bị loại, như đã ghi trong Round 3.

**Forgiveness không được đo.** Không thêm trường gán nhãn cho nó. Lý do: (a) review công khai không cho phép suy ra trạng thái tâm lý — hạn chế nhận dạng do Round 4 xác lập (Han & Anderson, 2025; Sterner, 2026); (b) thêm trường sẽ kéo dài đường găng gán nhãn mà không giải quyết được vấn đề nhận dạng.

### 2.6. Phạm vi dữ liệu

Phạm vi dữ liệu chính thức là **9.990 review đã gán nhãn** trong `data/TripAdvisor_EN.json`.

- **Không mở rộng** lên corpus 782.584 review của bài gốc trong phạm vi đề tài này.
- Mọi tuyên bố prevalence phải ghi đúng phạm vi: **TripAdvisor, 2015–2023, 9.990 review đã gán nhãn**.
- Ghi chú hiệu chỉnh: nghiên cứu viên ghi "9.900" khi chốt; đối chiếu file cho **9.990**. Số chính thức là 9.990. Trong 9.990 review, 9.867 review có ít nhất một span khía cạnh.

---

## 3. Hệ quả (Consequences)

1. **Khảo sát đóng có điều kiện.** Proposal viết được ngay; không cần vòng quét thêm.
2. **Công thức đo discrepancy vẫn chưa chốt** — ba ứng viên do validation study quyết định. Quyết định này không khóa công thức, chỉ khóa khung.
3. **Toàn văn còn thiếu là việc kiểm chứng, không phải việc khám phá.** Danh sách ưu tiên ở Mục 2.3 không thể tạo hướng nghiên cứu mới; rủi ro duy nhất là chi tiết phương pháp.
4. **Thay đổi này thay thế** cụm tài liệu số 3 của `RDR-0001` và tiêu chí bão hòa của cùng quyết định đó. Các phần còn lại của `RDR-0001` (4 mục tiêu khảo sát, sản phẩm bàn giao) giữ nguyên hiệu lực.
5. `RDR-0002` giữ nguyên hiệu lực cho mọi bổ sung tài liệu sau này.

---

## 4. Không nằm trong quyết định này

- Công thức đo discrepancy, cách chuẩn hóa, ngưỡng phân loại và sentiment estimator.
- Câu chữ chính thức của RQ1 và RQ2 (vẫn ở dạng nháp).
- Thiết kế chi tiết của evaluation set, thiết kế ứng dụng DAP391m và ngưỡng cảnh báo.
- Tên đề tài và các mục còn mở trong Phụ lục A của proposal.

---

## 5. Đọc thêm

- [`docs/logs/literature_survey/0006_survey_matrix_round_4.md`](../logs/literature_survey/0006_survey_matrix_round_4.md) — ma trận Round 4, checkpoint phản biện, endpoint check và kiểm tra tính mới.
- [`refs/INDEX.md`](../../refs/INDEX.md) — sơ đồ 8 cụm chức năng và trạng thái toàn văn.
- [`notes/reference_map.md`](../../notes/reference_map.md) — trạng thái và vai trò từng nguồn.
- [`notes/project_overview.md`](../../notes/project_overview.md) — bản đồ một trang của đề tài.
