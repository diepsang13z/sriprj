# Tổng quan Survey Round 3

- **Ngày thực hiện:** 2026-09-22
- **Loại khảo sát:** Targeted scoping review, không phải systematic review/PRISMA.
- **Mục đích:** kiểm tra lại RQ3 cũ và tìm một cơ chế rộng hơn nhưng vẫn đo được bằng dữ liệu dự án.

> **Trạng thái sau Round 4 (2026-09-23):** Round 4 đã kiểm chứng độc lập các kết luận dưới đây. Nội dung Round 3 giữ nguyên, nhưng ba điểm đã thay đổi: (a) bất đối xứng bị hạ xuống mức **có điều kiện**, kèm hạn chế nhận dạng và giới hạn phạm vi TripAdvisor; (b) kiểm định phụ #1 hạ xuống mức **phân tích khám phá**; (c) hàng đợi retrieval ở mục 6 được thay bằng danh sách mới. Chi tiết: [`docs/logs/literature_survey/0006_survey_matrix_round_4.md`](../docs/logs/literature_survey/0006_survey_matrix_round_4.md) và [`notes/reference_map.md`](reference_map.md) mục 6, 10.

## 1. Vì sao cần Survey Round 3?

RQ3 cũ tập trung vào một chiều duy nhất: `positive Service × negative Facility → rating được cứu`. Cách đặt này ngầm giả định rằng chỉ cặp Service–Facility quan trọng, mọi lỗi Facility có mức nghiêm trọng tương đương và các khía cạnh luôn bù trừ tuyến tính.

Round 3 được mở theo `RDR-0003` để kiểm tra các giả định đó. Trọng tâm không phải gom thêm thật nhiều bài, mà là tìm theory và empirical evidence đủ để quyết định có nên mở rộng RQ3 hay không.

## 2. Đã survey những gì?

- **Cửa sổ chủ động:** 2023-09-22 đến 2026-09-22.
- **Đối tượng ưu tiên:** journal articles về hotel/tourism rating, satisfaction, aspect asymmetry, compensatory/non-compensatory decision, failure severity và service recovery.
- **Thứ tự nguồn:** journal trước conference; publisher/DOI trước repository; nguồn đóng được sàng lọc trước nguồn mở.
- **Bốn câu hỏi quét:**
  1. Các hotel attributes tạo penalty và reward bất đối xứng như thế nào?
  2. Overall rating được hình thành theo cơ chế bù trừ hay không bù trừ?
  3. Severity, recovery, hotel class và reference point có tạo boundary conditions không?
  4. Cơ chế nào đo được mà không phải suy diễn trực tiếp `forgiveness`, `anger` hoặc `loyalty` từ rating?

## 3. Số liệu tổng quan

| Chỉ số | Kết quả |
|---|---:|
| Nguồn trong shortlist Round 3 | 9 journal articles |
| Journal / conference / preprint | 9 / 0 / 0 |
| Hospitality–tourism / cross-domain | 8 / 1 |
| Full text của shortlist Round 3 | 3/9 (Sharma, Li, Wang J.) |
| Full text chưa lấy được | 6/9 |
| Hàng đợi 8 bài ưu tiên | **3/8 đã có toàn văn** (Sharma, Öztürk, Wang J.) · 5 bài đóng còn thiếu · 2 đã bỏ |
| Nguồn truy cập mở đã lấy thêm | 4 (Öztürk, Wang J., Ameur, Yoruk) |
| Toàn thư viện `refs/` | **35 PDF, khoảng 81.7 MiB** (cập nhật 2026-09-23, sau Round 4 và đổi cấu trúc thư mục) |
| Cụm chức năng `refs/` | 8 cụm: 01_root · 02_definition · 03_phenomenon · 04_mechanism · 05_boundary_conditions · 06_counter_evidence · 07_baselines_methods · 08_legacy |
| Provenance/definition | 2 PDF ở `02_definition/` |
| Legacy/deprioritized PDF | 4 ở `08_legacy/` |

Ba nguồn Round 3 đã có toàn văn:

- Li et al. (2024): mô hình satisfaction hai giai đoạn, non-compensatory trước và compensatory sau.
- Sharma et al. (2025): Prospect Theory, loss aversion, diminishing sensitivity và reference point.
- Wang J. et al. (2024): XGBoost + SHAP cho quan hệ nonlinear/asymmetric giữa attribute performance và satisfaction.

Các con số Round 1–2 và Round 3 không nên cộng trực tiếp thành số bài unique: mỗi vòng có tiêu chí và vai trò curation khác nhau, một số nguồn được giữ lại hoặc tái phân loại giữa các vòng.

## 4. Survey được gì?

### 4.1. Không ủng hộ cách nhìn một cặp aspect

Evidence hiện có không ủng hộ việc coi `Service × Facility` là quy luật tổng quát. Service vẫn quan trọng, nhưng các aspect khác có penalty/reward khác nhau và mức ảnh hưởng có thể phi tuyến.

### 4.2. Cơ chế giải thích rộng hơn

Round 3 hội tụ vào hai nhánh:

- **Penalty-dominant / non-compensatory:** một lỗi basic, severe hoặc diagnostic có thể chi phối rating; các điểm tích cực khác không bù được.
- **Compensatory:** khi lỗi nhẹ hoặc đã được recovery, nhiều positive aspects có thể cộng gộp và giữ rating cao.

Cơ chế này giải thích cả hai chiều sentiment–rating discrepancy mà không cần gán trạng thái tâm lý trực tiếp cho người review.

### 4.3. RQ3 đã chốt

> Các cảm xúc tích cực và tiêu cực trên nhiều khía cạnh khách sạn kết hợp bất đối xứng như thế nào để quyết định chiều hướng và độ lớn của sentiment–rating discrepancy?

Đã được nghiên cứu viên chốt theo [`RDR-0004`](../docs/decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md) ngày 2026-09-23.

### 4.4. Boundary conditions phù hợp dữ liệu

- Dùng được: aspect polarity/configuration, failure severity, service recovery và hotel class.
- Chỉ dùng cho robustness: time.
- Không chọn làm moderator chính: trip type, reviewer experience, brand equity và first/peak/end episode vì dữ liệu thiếu hoặc không quan sát được đáng tin cậy.

Dữ liệu hiện có hỗ trợ quyết định này: `star` đầy đủ 9,990/9,990 records; trip type chỉ có 658/9,990 records; 2,622 hotels làm hotel-month reference point quá thưa cho RQ chính.

## 5. Chưa kết luận được gì?

- Chưa chứng minh literature saturation theo `RDR-0001`.
- 6/9 nguồn Round 3 chưa có full text; các claim chỉ có trong abstract vẫn phải giữ ở mức `pending full-text audit`.
- Round 4 (2026-09-23) xác nhận các điểm trên vẫn mở và bổ sung một hạn chế mới: không phân biệt được bù trừ thật với thiên lệch trình bày khi chỉ dùng review công khai. Tiêu chí bão hòa của `RDR-0001` vẫn không đạt → đề xuất miễn bằng `RDR-0005` (chưa ban hành).
- Chưa khóa công thức đo discrepancy, econometric model hoặc validation design.

## 6. Bước tiếp theo

1. ✅ RQ3 đã chốt theo [`RDR-0004`](../docs/decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md).
2. Ưu tiên full-text audit ba nguồn trực tiếp còn thiếu: Kwon (2026), Wang et al. (2024) và Albayrak et al. (2025).
3. Duy trì hàng đợi bảy bài còn lại nhưng không cào rộng ngoài danh sách.
4. Cập nhật Research Proposal theo RQ3 đã chốt rồi mới khóa validation/econometric model.

> **Đã thay thế sau Round 4 (2026-09-23):** mục 2–3 ở trên không còn hiệu lực. Wang J. (2024) đã có toàn văn; Kwon (2026) và Albayrak (2025) vẫn đóng trong `refs/INDEX.md` mục B2; Round 4 thay hàng đợi rộng bằng 9 bài truy cập mở (7 đã tải) + 14 bài đóng (log `0006` mục 7.2, `refs/INDEX.md` mục 9). Kwon (2026) vẫn là ưu tiên 1 nhưng phải đọc kèm cảnh báo phương pháp của Slevitch (2024). Mục 1 và 4 giữ nguyên hiệu lực.

## 7. Nguồn chi tiết

- [`RDR-0003`](../docs/decisions/RDR-0003_review_and_reset_survey.md) — quyết định mở lại khảo sát và tái định hình RQ3.
- [`Survey Round 3 matrix`](../docs/logs/literature_survey/0005_survey_matrix_round_3_rq3_rescoping.md) — search protocol, evidence matrix, synthesis và endpoint check.
- [`refs/INDEX.md`](../refs/INDEX.md) — trạng thái toàn văn, active/legacy curation và hàng đợi retrieval.
- [`notes/project_overview.md`](project_overview.md) — bản đồ ngắn của toàn dự án.
