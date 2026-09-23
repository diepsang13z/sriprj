# Bản đồ tài liệu tham khảo

- **Cập nhật:** 2026-09-23 (sau Survey Round 4).
- **Dùng khi:** cần biết nhanh một ref nói gì, được dùng ở đâu trong đề tài, và đã có toàn văn local hay chưa.
- **Catalog chính thức:** [`refs/INDEX.md`](../refs/INDEX.md). Note này không thay thế catalog, decision record hay literature_survey log.

## 1. Cách đọc trạng thái

| Trạng thái | Ý nghĩa |
|---|---|
| **Đã kéo — local PDF** | Có file PDF local; version cụ thể được nêu thêm nếu xác minh được. |
| **Đã kéo — accepted manuscript** | Có toàn văn tác giả chấp nhận; dùng để đọc phương pháp/kết quả, không gọi là version of record. |
| **Đã kéo — preprint** | Có bản preprint local; chưa coi là evidence peer-reviewed. |
| **Chưa kéo** | Chỉ có DOI/publisher metadata hoặc abstract đã xác minh; chi tiết ngoài abstract cần giữ ở `pending full-text audit`. |
| **Chưa kéo — tải tay** | Truy cập mở nhưng publisher chặn bot, hoặc còn thiếu; link tải và đích lưu ở log `0006` mục 7.2. |
| **Legacy** | Giữ audit trail hoặc provenance; không dùng để dẫn dắt lập luận RQ hiện tại. |

## 2. Toàn cảnh `refs/`

- **35 PDF local, xếp theo chức năng:** `01_root` 1 · `02_definition` 2 · `03_phenomenon` 8 · `04_mechanism` 7 · `05_boundary_conditions` 6 · `06_counter_evidence` 1 · `07_baselines_methods` 6 · `08_legacy` 4. Cộng 2 file markdown ở `01_root` (factsheet, full_paper).
- **Không có file mồ côi:** mọi PDF local đều được ghi trong `refs/INDEX.md`; trạng thái toàn văn ở Mục 9 của file đó.
- **Trục active hiện tại:** signed sentiment–rating discrepancy và RQ3 về cross-aspect asymmetric compensation (đã chốt theo `RDR-0004`), đọc kèm hai điều chỉnh bắt buộc của Round 4 (mục 10).
- **Full text Round 3:** 3/9 nguồn shortlist đã có local full text: Sharma et al. (2025), Li et al. (2024), Wang J. et al. (2024).
- **Round 4 (2026-09-23):** xác minh **26 nguồn mới** qua 5 cluster targeted (A–E); **16/26 đã có toàn văn** (9 tự tải + 7 tải tay), **2 bài truy cập mở còn lại** (C3 Liu, D5 Slevitch), **14 bài đóng** chờ thư viện trường (8 Round 4 + 6 Round 3). Ma trận, mức bằng chứng, checkpoint phản biện và kết quả kiểm tra tính mới: xem [`docs/logs/literature_survey/0006_survey_matrix_round_4.md`](../docs/logs/literature_survey/0006_survey_matrix_round_4.md). Danh sách tải tay/đóng: [`refs/INDEX.md`](../refs/INDEX.md) mục 9.
- **Hai cụm từng được đề xuất đã thành cụm thật**, đổi tên theo chức năng: `05_boundary_conditions/` (thay cho đề xuất `severity-recovery/`) và `06_counter_evidence/` (thay cho `method-critique/`). Sơ đồ 8 cụm: `refs/INDEX.md` mục 0.

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
| **Wang, D. et al. (2025)** | Phân biệt review inconsistency và rating inconsistency trong TripAdvisor helpfulness. | Giữ để tránh trộn hai construct; outcome helpfulness không dẫn dắt RQ. | **Chưa kéo** — đóng, cần thư viện trường. |

## 5. Round 3: asymmetric compensation

Round 3 không nhằm xác nhận `positive Service × negative Facility → rating được cứu`. Nó khảo sát liệu rating hình thành qua **penalty-dominant/non-compensatory** hay **compensatory** combinations giữa nhiều aspects, và điều kiện nào thay đổi cơ chế đó.

| Ref | Tóm tắt ngắn | Tác dụng trong RQ3 | Trạng thái |
|---|---|---|---|
| **Kwon, W. (2026)** | Zero-shot ABSA kết hợp Impact-Asymmetry Analysis/Kano. | Trục trực tiếp nhất để phân loại aspect thành satisfier, dissatisfier hoặc hybrid. | **Chưa kéo** — đóng, cần thư viện trường. Priority 1. |
| **Sharma et al. (2025)** | Prospect Theory trên 416,756 TripAdvisor reviews; kiểm tra loss aversion và diminishing sensitivity so với reference point. | Lý giải loss/penalty dominance mà không gán `anger` từ rating. | **Đã kéo — accepted manuscript**, 32 trang. |
| **Wang, J. et al. (2024)** | XGBoost + SHAP cho quan hệ nonlinear, asymmetric và dynamic giữa hotel attributes và satisfaction. | Hỗ trợ không mô hình hóa tất cả aspect bằng một hệ số tuyến tính/đối xứng. | **Đã kéo — local PDF**. |
| **Öztürk (2026)** | High-utility rules tìm aspect–sentiment combinations gắn với rating classes. | Hỗ trợ nhận diện multi-aspect trade-off/rule dễ diễn giải. | **Đã kéo — local PDF**. |
| **Albayrak et al. (2025)** | Service failure type, perceived severity, service recovery và negative engagement. | Căn cứ giữ `Severity` và `Service_Recovery` làm boundary conditions trên evaluation set. | **Chưa kéo** — đóng, cần thư viện trường. Priority 3. |
| **Xu et al. (2025)** | BERT–BiLSTM–CRF trên >400k negative hotel reviews; complaint aspects có penalty không đồng đều. | Counter-evidence: Service quan trọng nhưng không đủ để làm moderator trung tâm duy nhất. | **Chưa kéo** — đóng, cần thư viện trường. |
| **Zhong et al. (2026)** | Sensory clues, attribution/responsibility và asymmetric effect lên hotel rating. | Gợi ý negative proximal Facility cues cần tách theo severity/diagnosticity. | **Chưa kéo** — đóng, cần thư viện trường. |
| **Doan et al. (2025)** | HOSSemEval-EB23, dataset/model benchmark cho hospitality ABSA. | Benchmark kỹ thuật cho ABSA, không phải evidence chính về discrepancy. | **Chưa kéo** — đóng, cần thư viện trường. |
| **Li et al. (2024)** | Kano utility và two-stage nonlinear satisfaction: non-compensatory trước, compensatory sau. | Cấu trúc phương pháp rõ cho RQ3; khác domain nên chỉ supporting method. | **Đã kéo — local PDF**, 25 trang. |

**Tình trạng hàng đợi 8 bài:** **3/8 đã có toàn văn** (Sharma, Wang J., Öztürk); 5 bài còn lại đều là bài đóng — Kwon, Albayrak, Xu, Zhong, Doan. Ngoài hàng đợi còn 1 bài đóng khác là Wang D. (DSS) và Li (JTAER) đã có toàn văn như supporting method. Không cào rộng ngoài hàng đợi; quyết định RQ3 đã có trong `RDR-0004`.

> **Đã bị thay thế sau Round 4:** hàng đợi retrieval ở trên không còn là danh sách hiện hành. Round 4 thay bằng 9 bài truy cập mở (7 đã tải) + 14 bài đóng (log `0006` mục 7.2 và `refs/INDEX.md` mục 9); Kwon (2026) vẫn là ưu tiên 1 nhưng phải đọc kèm cảnh báo phương pháp của Slevitch (2024), và Albayrak (2025) vẫn đóng trong `refs/INDEX.md` mục B2.

## 6. Round 4: kiểm chứng và phản biện (2026-09-23)

Round 4 không mở rộng phạm vi: vá hai lỗ hổng bằng chứng (severity/recovery, baseline cho artifact) cộng một nhánh phản biện bắt buộc. 26 nguồn mới đã xác minh qua 5 cluster; trích dẫn đầy đủ, DOI, mức bằng chứng I–VII và kết quả kiểm chứng nằm ở [`docs/logs/literature_survey/0006_survey_matrix_round_4.md`](../docs/logs/literature_survey/0006_survey_matrix_round_4.md) — không chép lại toàn bộ ở đây.

Tình trạng toàn văn sau Round 4: **16 bài đã tải** (9 tự tải + 7 tải tay), **2 bài truy cập mở còn lại** (C3 Liu, D5 Slevitch), **14 bài đóng** chờ thư viện trường (8 từ Round 4 + 6 từ Round 3). Đích lưu file và link tải: log `0006` mục 7.2 và `refs/INDEX.md` mục 9. Thư viện hiện có 35 PDF, khoảng 81,7 MiB — trong đó 7 bài tải tay đã xếp vào cụm ngày 2026-09-23.

### 6.1. Cluster A — vai trò bất đối xứng của aspect

| Ref | Tóm tắt ngắn | Vai trò | Trạng thái |
|---|---|---|---|
| **Regitz et al. (2026)** | Hồi quy sentiment dương/âm theo topic để phân loại Kano: Room quality = Must-Be (âm làm sập điểm, dương gần như không thưởng); connectivity = Attractive. | **Gần nhu cầu nhất** nhưng khác đơn vị phân tích (topic khai phá, không phải review có nhãn người gán) → làm mỏng ranh giới tính mới. | **Đã kéo — local PDF** |
| **Park et al. (2025)** | Impact Asymmetry Analysis trên 88.309 review: information quality = satisfier, system quality = dissatisfier. | Bằng chứng quy mô lớn cho bất đối xứng trong hospitality. | **Chưa kéo** — đóng |
| **Zhang et al. (2025)** | >540.000 review: thuộc tính môi trường trong nhà (sạch sẽ, không khí, âm thanh) là Basic/penalty-dominant. | Penalty-dominant từ dữ liệu quan sát, không dùng bảng hỏi. | **Đã kéo — local PDF** |
| **Cui et al. (2025)** | AIPA + PRCA trên Grand Canal: thuộc tính hạ tầng nền có penalty vượt reward. | Củng cố hướng; khác domain (heritage tourism). | **Chưa kéo** — đóng |
| **Li, Lee & Kim (2025)** | BERTopic + three-factor + PRCA: thuộc tính lõi giữ tác động **gần đối xứng** giữa các hạng sao. | **Vừa ủng hộ vừa phản biện** — cùng một bài nằm ở cluster A và D (A3 = D4). | **Đã kéo — local PDF** |

### 6.2. Cluster B — severity & service recovery

| Ref | Tóm tắt ngắn | Vai trò | Trạng thái |
|---|---|---|---|
| **Das et al. (2026)** | Meta-analysis 147 nghiên cứu, N=82.901, attribution + justice. | **Mức bằng chứng I** — cao nhất thư viện. | **Đã kéo — local PDF** |
| **Tengilimoglu & Öztürk (2024)** | Severity là moderator trực tiếp: recovery hiệu quả với lỗi nhẹ, giảm mạnh khi lỗi nặng. | Chặn việc coi recovery là biến nền. | **Đã kéo — local PDF** |
| **Leo et al. (2026)** | Customer participation in recovery; quality signal đảo chiều trách nhiệm recovery. | Ứng viên `Severity` trong bối cảnh khách sạn. **Ca biên về ngày công bố** (`created` 2026-06-29 vs `published-print` 2027-01). | **Đã kéo — local PDF** |
| **Hwang (2024)** | Double deviation: lỗi ban đầu + recovery thất bại tạo penalty phi tuyến. | Cơ chế penalty-dominant, không cần suy diễn tâm lý. | **Đã kéo — local PDF** |
| **Lim, Saha & Das (2025)** | Service recovery paradox — khi recovery vượt cả mức nền. | Giới hạn trên của bù trừ; chặn diễn giải `D > 0` quá rộng. | **Đã kéo — local PDF** |
| **Tan & Zou (2024)** | Recovery đo **từ văn bản review và phản hồi khách sạn**, không phải bảng hỏi. | Đúng dạng đo cần cho boundary condition. | **Chưa kéo** — đóng |

### 6.3. Cluster C — lân cận vùng tính mới (điều tra âm tính)

| Ref | Tóm tắt ngắn | Vì sao KHÔNG trùng niche | Trạng thái |
|---|---|---|---|
| **Biasetton et al. (2026)** | So text-implied rating (AlBERTo + CORAL ordinal regression) với sao; bất nhất mạnh nhất ở mức 2 và 4 sao. | Cấp **toàn văn bản**, sản phẩm bán lẻ; không có chiều khía cạnh. | **Đã kéo — local PDF** |
| **Marreira et al. (2026)** | Bất nhất như phân loại nhị phân cấp văn bản (1 sao vs 5 sao) bằng zero-shot LLM. | Không có dấu liên tục, không theo khía cạnh. | **Đã kéo — local PDF** |
| **Liu, Ma & Dou (2025)** | Bất nhất là **scalar tổng hợp**, outcome là perceived helpfulness. | Không tách theo khía cạnh; outcome ngoài RQ. | **Chưa kéo** — đóng |
| **Kovács (2025)** | Đo consistency text–sao bằng khoảng cách tuyệt đối cấp văn bản; moderator là construal level. | Mất dấu; moderator không có trong dữ liệu dự án. | **Chưa kéo** — đóng |

*(Patil et al. (2026) cluster C đề xuất đã có sẵn trong thư viện ở nhóm legacy — không tính là nguồn mới.)*

### 6.4. Cluster D — phản biện cơ chế penalty-dominant

| Ref | Đòn phản biện | Mức độ | Trạng thái |
|---|---|---|---|
| **Han & Anderson (2025)** | Người dùng TripAdvisor thiên lệch đo lường dương so với trải nghiệm tự khai → `D > 0` có thể là artefact trình bày, không phải bù trừ. | **Cao nhất** | **Chưa kéo** — đóng |
| **Kirilenko et al. (2024)** | 75.000 review / 4 nền tảng: cùng khách sạn cho phân bố sao và cảm xúc khác nhau theo nền tảng. | Vừa — chặn khái quát ngoài TripAdvisor. | **Chưa kéo** — đóng |
| **Sterner (2026)** | Phân rã méo thành 5 nguồn cấu trúc; can thiệp nền tảng thường làm tăng phương sai. | Cao | **Đã kéo — local PDF** |
| **Slevitch (2024)** | Phân loại Kano/PRCA trong hospitality có lỗi quy trình hệ thống, dễ suy ra bất đối xứng ở nơi thực tế tuyến tính. | **Cao với kiểm định phụ #1.** | **Chưa kéo** — còn thiếu, tải tay (SAGE) |
| **Mellinas et al. (2025)** | Thuật toán Booking.com dồn 85% trọng số vào 12 tháng gần nhất → điểm số tách rời khỏi văn bản. | Vừa–cao | **Chưa kéo** — đóng |

### 6.5. Cluster E — baseline & prior art cho artifact DAP391m

| Ref | Giá trị dùng lại | Trạng thái |
|---|---|---|
| **You et al. (2024)** | Baseline số dùng ngay: RoBERTa đa nhiệm AUROC 0,9214 · AUPRC 0,6152 · F1 0,5817 trên 8 khía cạnh (so XGBoost 0,4938 và LSTM-attention 0,4208). Hội nghị PACLIC. | **Đã kéo — local PDF** |
| **Guidotti et al. (2025)** | Zero-shot LLM cho phân loại cảm xúc + trích từ khóa, đóng khung như công cụ hỗ trợ ra quyết định → prior art cho mục đích của app. | **Đã kéo — local PDF** |
| **Hu et al. (2024)** | 4.004 review TripAdvisor / 233 khách sạn: **694 review (17,3%)** bất nhất rõ rệt, tách theo hạng khách sạn và nhóm khách → mốc so sánh prevalence cho RQ1. | **Đã kéo — local PDF** |
| **Pramono et al. (2026)** | SHAP + LIME + kiểm định faithfulness bằng eraser → thiết kế tầng giải thích. **Venue chưa xác lập** (không DOAJ, không core): chỉ dùng kỹ thuật. | **Đã kéo — local PDF** |
| **Kumar et al. (2024)** | TF-IDF + logistic/ensemble đạt 61% dự đoán đúng mức sao. **Venue lệch domain** — hạ mức tin cậy. | **Chưa kéo** — đóng |
| **Zhu et al. (2025)** | DaNet — ABSA đa phương thức (ảnh + chữ); dữ liệu dự án chỉ có text → **liên quan thấp**, chỉ tham khảo kỹ thuật. | **Đã kéo — local PDF** |

## 7. Supporting theory và technical map

| Ref | Tóm tắt ngắn | Tác dụng | Trạng thái |
|---|---|---|---|
| **Ameur et al. (2024)** | Systematic literature review về hotel-review sentiment analysis. | Bản đồ kỹ thuật để đối chiếu pipeline/ABSA. | **Đã kéo — local PDF**. |
| **Huang & Lo (2025)** | So sánh service failure do human/robot provider; forgiveness và recovery expectation. | Supporting evidence cho failure severity/recovery; không dùng để suy diễn forgiveness từ rating. | **Đã kéo — local PDF**. |
| **Yoruk et al. (2025)** | Literature review và research agenda về consumer forgiveness. | Chỉ dùng khi RQ cuối cùng thực sự cần construct forgiveness. | **Đã kéo — local PDF**. |

## 8. Provenance và legacy

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

## 9. Cách dùng theo công việc

| Nếu cần làm gì? | Đọc trước |
|---|---|
| Định nghĩa/mã hóa discrepancy có direction và magnitude | Wang P. (2025), Kwon B. (2025), Almansour (2022). |
| Viết gap và RQ3 | Bigné (2023), Sharma (2025), Li (2024), Round 3 matrix, và Round 4 log `0006` mục 4–5. |
| Thiết kế aspect-level analysis | Kwon W. (2026), Wang J. (2024), Doan (2025); full text còn thiếu cần audit. |
| Giải thích penalty-dominant, severity, recovery | Sharma (2025), B1–B6 (mục 6.2), Albayrak (2025), Xu (2025), Zhong (2026). |
| Trả lời phản biện về thiên lệch đo lường / nền tảng | D1 Han & Anderson, D2 Kirilenko, D3 Sterner, D6 Mellinas; D5 + D4 dùng để phòng thủ phương pháp. |
| Chốt tuyên bố prevalence cho RQ1 | E4 Hu et al. (17,3% trên 4.004 review), đọc kèm D1/D2 để ghi đúng giới hạn phạm vi. |
| Chọn baseline và tầng giải thích cho app DAP391m | E2 (số baseline F1 0,5817), E1 (SHAP/LIME), E3 (prior art mục đích), E5. |
| Tránh leakage/circularity khi xây sentiment estimator | Root paper, Valdivia (2019), Almansour (2022), Topçu (2026), D1. |
| Chuẩn bị proposal sau khi RQ3 được duyệt | `notes/project_overview.md`, `notes/survey_overview.md`, rồi literature logs. |

## 10. Giới hạn sử dụng

- RQ3 đã chốt theo `RDR-0004`; khảo sát đã đóng có điều kiện và khung lý thuyết đã khóa theo `RDR-0005` (2026-09-23). Công thức đo discrepancy vẫn chưa chốt — chờ validation study. Phạm vi dữ liệu: 9.990 review gán nhãn.
- **Round 4 đặt bốn điều kiện không thương lượng cho mọi văn bản của đề tài:** (1) không phân biệt được bù trừ thật với thiên lệch trình bày khi chỉ dùng review công khai — đây là hạn chế nhận dạng, phải viết tường minh (D1, D3, D6); (2) mọi tuyên bố prevalence ghi rõ phạm vi TripAdvisor 2015–2023 (D2); (3) phân loại Kano/PRCA chỉ trình bày như phân tích khám phá, kèm bất định (D5, D4); (4) giữ khung hai nhánh compensatory/non-compensatory, không viết "penalty luôn thắng" (D4).
- **Tính mới:** câu "chưa tìm thấy thước đo discrepancy có dấu ở cấp khía cạnh" chỉ đứng trên tìm kiếm title/abstract — phải viết kèm cách đã tìm, không viết "chưa ai làm". A1 (Regitz et al. 2026) làm ranh giới này mỏng đi.
- **16 nguồn Round 4 đã có toàn văn và xếp vào cụm chức năng** (9 tự tải + 7 tải tay, log `0006` mục 7.2 và 8). Sơ đồ thư mục: `refs/INDEX.md` mục 0.
- Full-text availability không đồng nghĩa mức evidence: preprint và accepted manuscript phải được nêu đúng version.
- Với bài chưa kéo, chỉ dùng DOI/publisher metadata và abstract đã xác minh; không suy diễn chi tiết phương pháp/kết quả ngoài phần có thể kiểm chứng.
- `refs/INDEX.md` là nơi cập nhật file path và access state; cập nhật note này khi vai trò hoặc access state thay đổi.
