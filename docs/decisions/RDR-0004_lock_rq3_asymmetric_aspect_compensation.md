# RDR-0004: Chốt RQ3 — Asymmetric Aspect Compensation

- **Trạng thái:** ACCEPTED
- **Ngày quyết định:** 2026-09-23
- **Người đề xuất:** Nghiên cứu viên
- **Phạm vi áp dụng:** RQ3 và các kiểm định phụ của đề tài
- **Căn cứ:** `RDR-0003` (mở lại khảo sát để tái định hình RQ3) và [`docs/logs/literature_survey/0005_survey_matrix_round_3_rq3_rescoping.md`](../logs/literature_survey/0005_survey_matrix_round_3_rq3_rescoping.md) (evidence matrix, cross-source synthesis, endpoint check)

---

## 1. Bối cảnh (Context)

`RDR-0003` mở lại khảo sát vì RQ3 cũ `positive Service × negative Facility → rating được cứu` bị đánh giá là quá hẹp và một chiều.

Targeted Survey Round 3 đã hoàn tất với **9 journal candidates**. Kết luận chính: RQ3 cũ trộn ba giả định chưa được chứng minh.

1. Chỉ có một cặp aspect đáng quan tâm.
2. Mọi negative facility event có severity tương đương.
3. Overall rating được hình thành bằng một quan hệ compensatory tuyến tính.

Round 3 không hỗ trợ ba giả định này như quy luật chung: Kwon (2026), Wang et al. (2024) và Li et al. (2024) phân biệt basic/dissatisfier với performance/excitement attributes; Sharma et al. (2025) cho thấy loss aversion và diminishing sensitivity; Albayrak et al. (2025) cho thấy failure severity và recovery tạo boundary conditions; Xu et al. (2025) và Zhong et al. (2026) cho thấy một số complaint/sensory failure có penalty lớn đến mức positive service không bù được.

Evidence hội tụ về một **quyết định bù trừ bất đối xứng** (asymmetric compensatory/non-compensatory decision) — cấu trúc này giải thích đồng thời cả hai chiều của discrepancy mà không cần coi `Service` là moderator duy nhất, và không cần suy diễn trực tiếp trạng thái tâm lý `forgiveness/anger` từ rating.

---

## 2. Quyết định (Decision)

### 2.1. RQ3 chính thức

> **RQ3 (tiếng Việt):** Cảm xúc tích cực và tiêu cực trên nhiều khía cạnh khách sạn kết hợp bất đối xứng như thế nào để quyết định chiều hướng và độ lớn của sentiment–rating discrepancy?

> **RQ3 (English, dùng cho Final Report mẫu Springer):** How do positive and negative sentiments across multiple hotel aspects combine asymmetrically to determine the direction and magnitude of the sentiment–rating discrepancy?

**Trạng thái: CHỐT.** Ngôn ngữ giữ nguyên như phương án A — Cross-aspect asymmetry trong `0005` mục 4, phương án được đánh giá "Khuyến nghị" với fit dữ liệu cao và novelty cao.

### 2.2. Cơ chế được kiểm định

Hai nhánh đối lập trong cùng một cơ chế:

- **Non-compensatory / penalty-dominant:** một basic, severe hoặc diagnostic failure có thể chi phối đánh giá tổng; các positive aspect khác không đủ bù.
- **Compensatory:** khi lỗi nhẹ hoặc đã được recovery, nhiều positive aspect có thể cộng gộp và giữ rating cao.

### 2.3. Bốn kiểm định phụ (giữ gọn)

1. Aspect nào có tính **penalty-dominant/non-compensatory**, aspect nào có khả năng **reward/compensation**?
2. `Severity` và `Service_Recovery` có làm đổi cơ chế này trên evaluation set không?
3. Hiệu ứng có ổn định giữa các nhóm hotel class không?
4. `positive Service × negative Facility` được giữ như một **planned contrast**, không phải giả định trung tâm.

### 2.4. Boundary conditions dùng và loại

| Candidate | Dữ liệu sẵn có | Quyết định |
| --- | --- | --- |
| Aspect polarity/configuration | Span aspect + sentiment đầy đủ | **Trục chính** |
| Failure severity | Schema gắn nhãn `Minor/Major` | Dùng trên evaluation set |
| Service recovery | Schema `Yes/No` | Dùng trên evaluation set |
| Hotel class | `star` đủ 9.990/9.990 records | Boundary/robustness analysis |
| Time | `year`/`month` đầy đủ nhưng phân bố lệch | Chỉ robustness, không thành RQ chính |
| Trip type | Chỉ 658/9.990 records có giá trị | **Loại** khỏi moderator chính |
| Reviewer experience | Không có trường đáng tin cậy | **Loại** |
| Brand affiliation/equity | Không có biến trực tiếp; span `Branding` thưa và không tương đương brand equity | **Loại** khỏi causal claim |
| First/peak/end episode | Thứ tự câu không bảo đảm thứ tự trải nghiệm | **Không chọn** làm hướng chính |

### 2.5. Quan hệ với RQ3 cũ

Cách diễn đạt cũ `positive Service × negative Facility → rating được cứu` bị **thay thế** bởi RQ3 trong mục 2.1. Cặp `Service × Facility` chỉ còn là planned contrast theo mục 2.3 điều 4.

---

## 3. Hệ quả (Consequences)

1. **RQ3 không còn phụ thuộc `RDR-0003`.** Vòng khảo sát tiếp theo chỉ còn citation-chain/full-text audit cho Kwon (2026), Wang et al. (2024) và Albayrak et al. (2025), rồi cập nhật Research Proposal.
2. **Biến phụ thuộc của RQ3 là signed discrepancy — công thức cụ thể vẫn chưa chốt.** Ba ứng viên (3×3 Polarity Matrix · $z(r)-z(s)$ · signed aspect gap $r^*-s_a^*$) do validation study quyết định theo `docs/logs/validation/0001_manual_annotation_protocol.md` mục 5. RQ3 vì thế phải được đọc kèm RQ2.
3. **`Severity` và `Service_Recovery` chỉ tồn tại trên evaluation set**, không có trên toàn corpus. Mọi kiểm định dùng chúng phải báo cáo là sub-sample, không phát biểu cho toàn bộ 9.990 review.
4. **Ứng dụng (DAP391m):** phần hiển thị theo khía cạnh dựa trên span người gán làm được ngay; phần hiển thị $D$ có dấu chờ công thức ở mục 3.2.
5. **RQ3 đã dùng ngôn ngữ đo lường được** (“chiều hướng và độ lớn”), không suy diễn trạng thái tâm lý, nên nhất quán với cách diễn đạt lại RQ1.

---

## 4. Không nằm trong quyết định này

- Công thức đo discrepancy và ngưỡng phân loại — chờ validation study.
- RQ1 và RQ2 vẫn ở dạng nháp, chưa chốt chính thức.
- Ngưỡng cảnh báo trong ứng dụng.
- Việc mở rộng hay thu hẹp cửa sổ thời gian của dữ liệu.

---

## 5. Đọc thêm

- [`docs/logs/literature_survey/0005_survey_matrix_round_3_rq3_rescoping.md`](../logs/literature_survey/0005_survey_matrix_round_3_rq3_rescoping.md) — search protocol, evidence matrix, candidate alternatives, endpoint check.
- [`notes/survey_round_3_overview.md`](../../notes/survey_round_3_overview.md) — bản giải thích ngắn về Round 3.
- [`notes/reference_map.md`](../../notes/reference_map.md) — ref nào dùng cho phần nào, trạng thái full text.
- [`docs/logs/brainstorm/0003_app_concept_and_course_requirements.md`](../logs/brainstorm/0003_app_concept_and_course_requirements.md) — hướng ứng dụng đã chốt cho artifact của môn DAP391m.
- [`docs/logs/validation/0001_manual_annotation_protocol.md`](../logs/validation/0001_manual_annotation_protocol.md) — thiết kế evaluation set và tiêu chí chốt công thức đo lường.
