# Bản đồ tài liệu tham khảo

- **Cập nhật:** 2026-09-22
- **Dùng khi:** cần biết nhanh một ref nói gì, được dùng ở đâu trong đề tài, và đã có toàn văn local hay chưa.
- **Catalog chính thức:** [`refs/INDEX.md`](../refs/INDEX.md). Note này không thay thế catalog, decision record hay literature-survey log.

## 1. Cách đọc trạng thái

| Trạng thái | Ý nghĩa |
|---|---|
| **Đã kéo — local PDF** | Có file PDF local; version cụ thể được nêu thêm nếu xác minh được. |
| **Đã kéo — accepted manuscript** | Có toàn văn tác giả chấp nhận; dùng để đọc phương pháp/kết quả, không gọi là version of record. |
| **Đã kéo — preprint** | Có bản preprint local; chưa coi là evidence peer-reviewed. |
| **Chưa kéo** | Chỉ có DOI/publisher metadata hoặc abstract đã xác minh; chi tiết ngoài abstract cần giữ ở `pending full-text audit`. |
| **Legacy** | Giữ audit trail hoặc provenance; không dùng để dẫn dắt lập luận RQ hiện tại. |

## 2. Toàn cảnh `refs/`

- **15 PDF local:** 1 root paper, 7 inconsistency, 1 forgiveness, 2 asymmetric-compensation và 4 legacy.
- **Không có file mồ côi:** mọi PDF local đều được ghi trong `refs/INDEX.md`.
- **Trục active hiện tại:** signed sentiment–rating discrepancy và candidate RQ3 về cross-aspect asymmetric compensation.
- **Full text Round 3:** 2/9 nguồn trong shortlist đã có local full text: Li et al. (2024) và Sharma et al. (2025).

## 3. Tài liệu nền tảng

| Ref | Tóm tắt ngắn | Tác dụng trong đề tài | Trạng thái |
|---|---|---|---|
| **Le et al. (2026)** — root paper | BERTopic + VADER + WMLR trên 1.3M hotel reviews; dùng `Loyalty` để giải thích rating. | Là điểm xuất phát, dataset/context đối chuẩn và căn cứ phản biện nguy cơ circularity khi dùng rating/loyalty. | **Đã kéo — local PDF**; có `factsheet.md` và `full_paper.md`. |

## 4. Core evidence: sentiment–rating inconsistency

| Ref | Tóm tắt ngắn | Tác dụng trong đề tài | Trạng thái |
|---|---|---|---|
| **Wang, P. et al. (2025)** | Đo score–textual inconsistency và liên hệ tỷ lệ inconsistency với hotel performance. | Evidence gần nhất cho directional polarity mismatch và mức độ inconsistency ở cấp hotel. | **Đã kéo — local PDF**. |
| **Bigné et al. (2023)** | So sánh star rating với sentiment ở customer service experience; cho thấy positive/negative aspect sentiments có thể cancel-out/compensate. | Nền thực chứng gần nhất cho cross-aspect compensation; giữ active dù ở rìa cửa sổ quét. | **Đã kéo — local PDF**. |
| **Kwon, B. et al. (2025)** | Tách degree inconsistency liên tục `|z(rating)-z(sentiment)|` và directional mismatch; outcome là perceived review usefulness. | Cung cấp định nghĩa/đo lường độ lớn và chiều; không dùng helpfulness làm RQ chính. | **Đã kéo — local PDF**. |
| **Abaiyan et al. (2026)** | Phân loại sáu dạng rating–sentiment incongruence và kiểm tra độ tin cậy của rating như sentiment label. | Supporting evidence cho typology có hướng và cảnh báo weak-label. | **Đã kéo — preprint**; chưa peer-reviewed. |
| **Jayakody et al. (2026)** | Đo absolute cross-modal discrepancy ở hotel–aspect level. | Supporting technical evidence cho discrepancy đa phương thức/cấp aspect. | **Đã kéo — preprint**; chưa peer-reviewed. |
| **Wang, D. et al. (2025)** | Phân biệt review inconsistency và rating inconsistency trong TripAdvisor helpfulness. | Giữ để tránh trộn hai construct; outcome helpfulness không dẫn dắt RQ. | **Chưa kéo**; Elsevier paywall. |

## 5. Round 3: asymmetric compensation

Round 3 không nhằm xác nhận `positive Service × negative Facility → rating được cứu`. Nó khảo sát liệu rating hình thành qua **penalty-dominant/non-compensatory** hay **compensatory** combinations giữa nhiều aspects, và điều kiện nào thay đổi cơ chế đó.

| Ref | Tóm tắt ngắn | Tác dụng trong candidate RQ3 | Trạng thái |
|---|---|---|---|
| **Kwon, W. (2026)** | Zero-shot ABSA kết hợp Impact-Asymmetry Analysis/Kano. | Trục trực tiếp nhất để phân loại aspect thành satisfier, dissatisfier hoặc hybrid. | **Chưa kéo**; Elsevier paywall. Priority 1. |
| **Sharma et al. (2025)** | Prospect Theory trên 416,756 TripAdvisor reviews; kiểm tra loss aversion và diminishing sensitivity so với reference point. | Lý giải loss/penalty dominance mà không gán `anger` từ rating. | **Đã kéo — accepted manuscript**, 32 trang. |
| **Wang, J. et al. (2024)** | XGBoost + SHAP cho quan hệ nonlinear, asymmetric và dynamic giữa hotel attributes và satisfaction. | Hỗ trợ không mô hình hóa tất cả aspect bằng một hệ số tuyến tính/đối xứng. | **Chưa kéo**; bài OA nhưng Cloudflare/anti-bot chặn tải. Priority 2. |
| **Öztürk (2026)** | High-utility rules tìm aspect–sentiment combinations gắn với rating classes. | Hỗ trợ nhận diện multi-aspect trade-off/rule dễ diễn giải. | **Chưa kéo**; IEEE Xplore chặn tự động. |
| **Albayrak et al. (2025)** | Service failure type, perceived severity, service recovery và negative engagement. | Căn cứ giữ `Severity` và `Service_Recovery` làm boundary conditions trên evaluation set. | **Chưa kéo**; Elsevier paywall. Priority 3. |
| **Xu et al. (2025)** | BERT–BiLSTM–CRF trên >400k negative hotel reviews; complaint aspects có penalty không đồng đều. | Counter-evidence: Service quan trọng nhưng không đủ để làm moderator trung tâm duy nhất. | **Chưa kéo**; Elsevier paywall. |
| **Zhong et al. (2026)** | Sensory clues, attribution/responsibility và asymmetric effect lên hotel rating. | Gợi ý negative proximal Facility cues cần tách theo severity/diagnosticity. | **Chưa kéo**; Elsevier paywall. |
| **Doan et al. (2025)** | HOSSemEval-EB23, dataset/model benchmark cho hospitality ABSA. | Benchmark kỹ thuật cho ABSA, không phải evidence chính về discrepancy. | **Chưa kéo**; Springer paywall. |
| **Li et al. (2024)** | Kano utility và two-stage nonlinear satisfaction: non-compensatory trước, compensatory sau. | Cấu trúc phương pháp rõ cho candidate RQ3; khác domain nên chỉ supporting method. | **Đã kéo — local PDF**, 25 trang. |

**Tình trạng hàng đợi:** 1/8 bài priority đã lấy (Sharma); còn 7 bài. Li có toàn văn nhưng là supporting method ngoài hàng đợi tám bài. Không cào rộng ngoài hàng đợi trước khi có quyết định RQ3.

## 6. Supporting theory và technical map

| Ref | Tóm tắt ngắn | Tác dụng | Trạng thái |
|---|---|---|---|
| **Ameur et al. (2024)** | Systematic literature review về hotel-review sentiment analysis. | Bản đồ kỹ thuật để đối chiếu pipeline/ABSA. | **Chưa kéo**; ACM paywall. |
| **Huang & Lo (2025)** | So sánh service failure do human/robot provider; forgiveness và recovery expectation. | Supporting evidence cho failure severity/recovery; không dùng để suy diễn forgiveness từ rating. | **Đã kéo — local PDF**. |
| **Yoruk et al. (2025)** | Literature review và research agenda về consumer forgiveness. | Chỉ dùng khi RQ cuối cùng thực sự cần construct forgiveness. | **Chưa kéo**; Wiley paywall. |

## 7. Provenance và legacy

| Ref | Vì sao còn giữ? | Cách dùng | Trạng thái |
|---|---|---|---|
| **Valdivia et al. (2019)** | Nguồn của unified inconsistency index. | Định nghĩa/provenance, không dùng làm evidence hiện hành. | **Đã kéo — local PDF**. |
| **Almansour et al. (2022)** | Integrative review về text-rating review discrepancy. | Định nghĩa TRRD và cảnh báo rating là weak sentiment label. | **Đã kéo — local PDF**. |
| **Puh & Bagić Babac (2023)** | Hotel-review sentiment/rating prediction baseline. | Legacy technical baseline; không dùng lập luận discrepancy. | **Đã kéo — local PDF**, legacy. |
| **Topçu et al. (2026)** | Transformer rating prediction với random oversampling. | Loại vì rating là training label, không tạo sentiment signal độc lập. | **Đã kéo — local PDF**, legacy. |
| **McMurry (2026)** | Domain-specific socialness pipeline cho hostel reviews. | Loại vì conference/hostel socialness, không có rating discrepancy. | **Đã kéo — local PDF**, legacy. |
| **Patil et al. (2026)** | LLM-assisted ABSA ở quy mô lớn trên Yelp restaurant reviews. | Loại vì preprint/restaurant và không operationalize discrepancy. | **Đã kéo — preprint**, legacy. |
| **McCullough et al. (2024)** | First-impression và peak-end rule trong hotel experience. | Không dùng vì data không tái dựng được chronological episode. | **Chưa kéo**. |
| **Kalnaovakul et al. (2024)** | Sentiment–rating relationship chịu moderation của brand affiliation/reviewer experience. | Không dùng vì dataset không có moderator tương ứng đáng tin cậy. | **Chưa kéo**. |

## 8. Cách dùng theo công việc

| Nếu cần làm gì? | Đọc trước |
|---|---|
| Định nghĩa/mã hóa discrepancy có direction và magnitude | Wang P. (2025), Kwon B. (2025), Almansour (2022). |
| Viết gap và candidate RQ3 | Bigné (2023), Sharma (2025), Li (2024), và Round 3 matrix. |
| Thiết kế aspect-level analysis | Kwon W. (2026), Wang J. (2024), Doan (2025); full text còn thiếu cần audit. |
| Giải thích penalty-dominant, severity, recovery | Sharma (2025), Albayrak (2025), Xu (2025), Zhong (2026). |
| Tránh leakage/circularity khi xây sentiment estimator | Root paper, Valdivia (2019), Almansour (2022), Topçu (2026). |
| Chuẩn bị proposal sau khi RQ3 được duyệt | `notes/project-overview.md`, `notes/survey-round-3-overview.md`, rồi literature logs. |

## 9. Giới hạn sử dụng

- Candidate RQ3 chưa được nghiên cứu viên phê duyệt; không viết nó như quyết định đã khóa.
- Full-text availability không đồng nghĩa mức evidence: preprint và accepted manuscript phải được nêu đúng version.
- Với bài chưa kéo, chỉ dùng DOI/publisher metadata và abstract đã xác minh; không suy diễn chi tiết phương pháp/kết quả ngoài phần có thể kiểm chứng.
- `refs/INDEX.md` là nơi cập nhật file path và access state; cập nhật note này khi vai trò hoặc access state thay đổi.
