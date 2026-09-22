# Literature Survey — Round 3: RQ3 Rescoping

- **Ngày quét:** 2026-09-22
- **Cửa sổ chủ động:** 2023-09-22 đến 2026-09-22 theo `RDR-0002`
- **Chế độ:** Targeted scoping review; không tuyên bố PRISMA/systematic review
- **Điểm xuất phát:** `RDR-0003` xác định RQ3 hiện tại (`Service` cứu `Facility`) quá hẹp và một chiều.
- **Mục tiêu:** tìm cơ chế rộng hơn nhưng vẫn kiểm định được trên `TripAdvisor_EN.json`, ưu tiên journal và publisher record; ưu tiên nguồn đóng trước nguồn mở.

---

## 1. Search Protocol

### 1.1. Câu hỏi quét

1. Văn hiến mới mô hình hóa tác động **bất đối xứng** của các thuộc tính khách sạn lên satisfaction/rating như thế nào?
2. Có bằng chứng cho quyết định **bù trừ** và **không bù trừ** giữa nhiều khía cạnh hay không?
3. Những boundary conditions nào giải thích khi một lỗi bị bỏ qua hoặc chi phối điểm tổng: severity, recovery, hotel class, expectation/reference point hay vị trí của critical episode?
4. Cơ chế nào đo được bằng dữ liệu hiện có mà không phải suy diễn trực tiếp `forgiveness`, `anger` hoặc `loyalty` từ rating?

### 1.2. Nguồn và truy vấn

- **Nguồn:** DOI/Crossref, ScienceDirect, Emerald, SAGE, publisher metadata và institutional repository khi publisher full text không truy cập được.
- **Truy vấn chính:**
  - `hotel review aspect sentiment asymmetric effects rating penalty reward journal hospitality`
  - `online hotel reviews aspect compensation trade-off overall rating journal`
  - `hotel reviews negativity bias critical incident peak-end overall rating journal`
  - `hospitality service failure recovery forgiveness failure severity type observed rating journal`
  - `hotel reviews compensatory non-compensatory attributes satisfaction asymmetry`
  - `hotel review failure severity aspect sentiment rating nonlinear journal`
- **Thứ tự:** journal trước conference; publisher/DOI trước repository; nguồn đóng được sàng lọc trước nguồn mở.

### 1.3. Inclusion / Exclusion

**Include:** journal article trong cửa sổ 36 tháng; liên hệ trực tiếp với hotel/tourism rating, satisfaction, aspect asymmetry, compensatory rule, failure severity/recovery hoặc một theory thay thế có thể operationalize.

**Exclude khỏi shortlist:** conference/preprint; outcome chỉ là helpfulness/booking intention mà không giúp tái định hình RQ3; moderator không có trong dữ liệu và không thể gắn nhãn thủ công hợp lý; nguồn trước cửa sổ nếu chưa có citation-chain justification.

**Giới hạn truy xuất:** phần lớn nguồn ưu tiên là publisher-closed. DOI, tác giả, venue và ngày công bố đã được xác minh bằng Crossref/publisher record; các chi tiết không xuất hiện trong abstract được giữ ở mức `pending full-text audit`, không dùng làm căn cứ duy nhất cho quyết định.

---

## 2. Evidence Matrix

| ID | Nguồn | Dữ liệu / thiết kế | Construct / method | Phát hiện dùng được | Giá trị cho RQ3 | Evidence level / access |
|---|---|---|---|---|---|---|
| R3-J1 | Kwon (2026), *IJHM*. [DOI](https://doi.org/10.1016/j.ijhm.2025.104397) | TripAdvisor hotel reviews trong bối cảnh COVID-19; computational study | Zero-shot ABSA + Impact-Asymmetry Analysis; Kano/three-factor logic | Tách attribute thành satisfier, dissatisfier và hybrid thay vì giả định positive/negative có tác động đối xứng | Cơ sở trực tiếp để thay `Service × Facility` bằng **asymmetric effects trên mọi aspect** | Level VI; peer-reviewed; DOI/publisher metadata verified; publisher full text closed (Elsevier paywall, chưa có OA/preprint công khai) |
| R3-J2 | Sharma, Shin, Nicolau, & Park (2025), *IJHM*. [DOI](https://doi.org/10.1016/j.ijhm.2025.104170) | 416,756 TripAdvisor reviews, 375 hotels, 14 European cities; longitudinal secondary data | Prospect Theory; loss aversion; diminishing sensitivity; reference point | Negative deviations tạo tác động mạnh hơn positive deviations tương đương; marginal impact không tuyến tính | Giải thích punitive direction bằng **loss dominance**, không cần gán nhãn tâm lý `Anger` | Level IV; peer-reviewed; DOI verified; đã có bản accepted manuscript toàn văn (32 trang, 1.3MB) tại `refs/04_mechanism/2025_sharma_review_sentiment_garden_accepted_manuscript.pdf` |
| R3-J3 | Wang, Wu, Sun, & Wang (2024), *Data Science and Management*. [DOI](https://doi.org/10.1016/j.dsm.2024.01.003) | TripAdvisor attribute ratings của khách sạn New York | XGBoost + SHAP + dynamic asymmetric analysis | Quan hệ attribute–satisfaction là nonlinear, asymmetric và thay đổi theo thời gian; basic attributes tạo penalty mạnh khi kém | Hỗ trợ kiểm tra penalty/reward riêng theo aspect và tránh mô hình tuyến tính một chiều | Level IV/VI; peer-reviewed OA (KeAi/Elsevier); DOI verified; direct PDF download bị chặn bởi Cloudflare challenge/bot verification |
| R3-J4 | Xu, Yao, Ma, & Li (2025), *IJHM*. [DOI](https://doi.org/10.1016/j.ijhm.2024.104057) | Hơn 400,000 negative hotel reviews trên Ctrip | BERT–BiLSTM–CRF + econometric/dominance analysis | Bảy complaint aspects; service và cleanliness có penalty mạnh, nhưng mức quan trọng không đồng đều giữa aspects | Counter-evidence cần giữ: `Service` vẫn quan trọng, nhưng không đủ lý do khóa toàn bộ RQ vào một cặp `Service–Facility` | Level IV/VI; peer-reviewed; DOI/publisher metadata verified; publisher full text closed (Elsevier paywall) |
| R3-J5 | Kalnaovakul, Balasubramanian, & Chuah (2024), *Journal of Hospitality and Tourism Insights*. [DOI](https://doi.org/10.1108/JHTI-06-2024-0591) | 102,179 TripAdvisor reviews, 187 beach hotels tại Thái Lan | SVM + LDA; SmartPLS + PROCESS moderation | Text sentiment liên hệ mạnh với satisfaction rating; brand affiliation và reviewer experience làm thay đổi quan hệ này | Cho thấy aspect/rating relationship có boundary conditions; đồng thời cảnh báo không chọn moderator mà dữ liệu không có | Level IV/VI; peer-reviewed; Crossref abstract verified; Emerald full page trả 403 Forbidden |
| R3-J6 | McCullough et al. (2024), *Journal of Business Research*. [DOI](https://doi.org/10.1016/j.jbusres.2024.114899) | 5,497 hotel stays trong 5 năm; field data | First-impression effect vs. Peak-End Rule; retrospective delay moderation | First, peak và end đều ảnh hưởng đánh giá tổng; first impression mạnh nhất trong study này | Một critical episode có thể chi phối rating, nhưng review text hiện tại không bảo đảm tái dựng đúng trình tự trải nghiệm | Level IV; peer-reviewed; DOI/publisher metadata verified; publisher full text closed (Elsevier/JBR paywall) |
| R3-J7 | Albayrak et al. (2025), *IJHM*. [DOI](https://doi.org/10.1016/j.ijhm.2025.104242) | Qualitative study + scenario experiment trong hotel service failure | Failure type, perceived severity, recovery satisfaction, negative engagement | Failure type ảnh hưởng perceived severity; recovery phù hợp có điều kiện; một số quan hệ là curvilinear | Hỗ trợ dùng `Severity` và `Service_Recovery` như boundary conditions đã có trong annotation protocol | Level III/VI; peer-reviewed; DOI/publisher metadata verified; publisher full text closed (Elsevier paywall) |
| R3-J8 | Zhong, Liu, Gao, & Liu (2026), *Annals of Tourism Research*. [DOI](https://doi.org/10.1016/j.annals.2026.104208) | Large-scale hotel review text analysis | Sensory clues; attribution/responsibility; asymmetric rating impact | Negative proximal cues như smell/touch gây penalty lớn hơn positive cues tương ứng | Gợi ý `Facility` cần tách severity/diagnosticity thay vì xem mọi negative facility span như nhau | Level IV/VI; peer-reviewed; DOI verified; publisher full text closed (Elsevier/Annals of Tourism Research paywall) |
| R3-S1 | Li, Zhu, Zhang, Liu, & Yu (2024), *JTAER*. [DOI](https://doi.org/10.3390/jtaer19010015) | Online product reviews, ngoài hospitality | Kano utility + two-stage nonlinear satisfaction model | Basic attributes được xét ở non-compensatory stage; các thuộc tính còn lại mới đi vào compensatory utility stage | Cung cấp cấu trúc toán học rõ nhất cho RQ rộng hơn; chỉ dùng làm supporting method vì khác domain | Level VI; peer-reviewed OA; đã kéo và lưu trữ PDF toàn văn tại `refs/04_mechanism/2024_li_two_stage_satisfaction_decision_model.pdf` |

**Phân bố nguồn:** 9 journal articles, 0 conference, 0 preprint; 8/9 thuộc hotel/tourism/hospitality, 1/9 là phương pháp cross-domain. Shortlist được hình thành từ publisher-closed records trước; OA chỉ bổ sung cấu trúc phương pháp chưa thấy mô tả đủ rõ ở abstract nguồn đóng.

---

## 3. Cross-Source Synthesis

### 3.1. RQ3 hiện tại đang trộn ba giả định chưa được chứng minh

RQ `positive Service × negative Facility → rating được cứu` mặc định rằng:

1. chỉ một cặp aspect đáng quan tâm;
2. mọi negative facility event có severity tương đương;
3. overall rating được hình thành bằng một quan hệ compensatory tuyến tính.

Round 3 không hỗ trợ ba giả định này như quy luật chung. Kwon, Wang và Li phân biệt basic/dissatisfier với performance/excitement attributes; Sharma cho thấy loss aversion và diminishing sensitivity; Albayrak cho thấy failure severity và recovery tạo boundary conditions. Xu và Zhong còn cho thấy một số complaint/sensory failures có penalty lớn đến mức positive service có thể không bù được.

### 3.2. Cơ chế rộng hơn: asymmetric compensatory decision

Evidence hội tụ vào mô hình hai nhánh:

- **Non-compensatory / penalty-dominant:** một basic, severe hoặc diagnostic failure có thể chi phối đánh giá tổng; positive aspects khác không đủ bù.
- **Compensatory:** khi lỗi nhẹ hoặc được recovery, nhiều positive aspects có thể cộng gộp và giữ rating cao.

Cấu trúc này giải thích đồng thời hai direction của discrepancy mà không cần coi `Service` là moderator duy nhất và không cần suy diễn trực tiếp trạng thái tâm lý `forgiveness/anger` từ rating.

### 3.3. `Service × Facility` vẫn có giá trị, nhưng chỉ là một planned contrast

Xu et al. và Wang et al. cho thấy service thường có ảnh hưởng lớn; Zhong et al. cho thấy negative facility/sensory clues có thể penalty-dominant. Vì vậy cặp `positive Service × negative Facility` nên được giữ như **một interaction được đăng ký trước**, không phải toàn bộ RQ3.

### 3.4. Boundary conditions khả thi với dữ liệu dự án

| Candidate | Dữ liệu sẵn có | Quyết định |
|---|---|---|
| Aspect polarity/configuration | Span aspect + sentiment đầy đủ | Dùng làm trục chính |
| Failure severity | Đã có schema gắn nhãn `Minor/Major` | Dùng trên evaluation set |
| Service recovery | Đã có schema `Yes/No` | Dùng trên evaluation set |
| Hotel class | `star` có đủ 9,990/9,990 records; 1–5 sao và nhóm `0-star` | Dùng làm boundary/robustness analysis |
| Time | `year/month` đầy đủ nhưng review phân bố lệch | Chỉ robustness; không biến thành RQ chính |
| Trip type | Chỉ 658/9,990 records có giá trị | Loại khỏi moderator chính |
| Reviewer experience | Không có trường đáng tin cậy | Loại |
| Brand affiliation/equity | Không có biến trực tiếp; `Branding` spans thưa và không tương đương brand equity | Loại khỏi causal claim |
| First/peak/end episode | Thứ tự câu không bảo đảm là thứ tự trải nghiệm | Không chọn làm hướng chính |

---

## 4. Candidate RQ3 Alternatives

| Phương án | Câu hỏi | Fit dữ liệu | Novelty | Rủi ro | Đánh giá |
|---|---|---:|---:|---|---|
| A. Cross-aspect asymmetry | Positive và negative sentiments giữa các aspect kết hợp bất đối xứng như thế nào để tạo direction và magnitude của sentiment–rating discrepancy? | Cao | Cao: literature chủ yếu giải thích satisfaction, chưa trực tiếp signed aspect discrepancy | Cần giới hạn interaction để tránh combinatorial explosion | **Khuyến nghị** |
| B. Severity/recovery boundary | Severity và service recovery làm thay đổi khả năng bù trừ giữa các aspect như thế nào? | Cao trên evaluation set | Trung bình–cao | Nhãn thủ công; không có cho toàn corpus | Sub-question / boundary condition |
| C. Reference-point loss aversion | Deviation khỏi expected hotel rating tạo loss aversion và discrepancy như thế nào? | Trung bình–thấp | Trung bình | 2,622 hotels/9,990 reviews làm hotel-month reference point rất thưa | Không chọn làm RQ chính |
| D. Peak/critical episode | Critical episode ở đầu/đỉnh/cuối chi phối rating như thế nào? | Thấp | Trung bình | Không quan sát được event chronology đáng tin cậy | Loại |
| E. Brand/reviewer moderator | Brand equity hoặc reviewer experience điều tiết sentiment→rating ra sao? | Thấp | Thấp–trung bình | Dataset thiếu biến | Loại |

### RQ3 đề xuất sau Round 3

> **RQ3:** Các cảm xúc tích cực và tiêu cực trên nhiều khía cạnh khách sạn kết hợp bất đối xứng như thế nào để quyết định chiều hướng và độ lớn của sentiment–rating discrepancy?

**→ Đã được nghiên cứu viên chấp nhận và chốt trong [`RDR-0004`](../../decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md) ngày 2026-09-23. Bảng phương án ở mục 4 được giữ nguyên làm audit trail.**

Các kiểm định phụ nên giữ gọn:

1. Aspect nào có tính **penalty-dominant/non-compensatory** và aspect nào có khả năng **reward/compensation**?
2. `Severity` và `Service_Recovery` có làm đổi cơ chế này trên evaluation set không?
3. Hiệu ứng có ổn định giữa các nhóm hotel class không?
4. `positive Service × negative Facility` được giữ như một planned contrast, không phải giả định trung tâm.

---

## 5. Endpoint Check

| Tiêu chí | Trạng thái sau Round 3 | Bằng chứng / thiếu hụt |
|---|---|---|
| Journal-first / auditability | **Đạt cho vòng này** | 9 journal, 0 conference/preprint; từng nguồn có DOI và access state |
| Tìm hướng thay thế RQ3 | **Đạt** | Asymmetric compensatory vs. non-compensatory mechanism |
| Theory bổ sung | **Đạt cục bộ** | Kano/three-factor, Prospect Theory, Peak-End/first-impression, severity/recovery boundary |
| Data feasibility | **Đạt cho phương án A+B** | Aspect/sentiment/rating sẵn có; severity/recovery đã nằm trong annotation schema; hotel class đầy đủ |
| Full-text verification | **Đạt một phần** | 2/9 nguồn (Li et al., 2024; Sharma et al., 2025 accepted manuscript) đã có toàn văn; 7/9 nguồn còn lại chưa kéo được do paywall/bot challenge |
| Saturation theo `RDR-0001` | **Chưa chứng minh** | Các nguồn mới vẫn thêm theory/method; không nên tuyên bố 3–5 nguồn liên tiếp không sinh insight mới |

**Quyết định vận hành đề xuất:** dừng broad search tại đây và xin author decision về RQ3 đề xuất. Nếu chấp nhận, vòng tiếp theo chỉ làm citation-chain/full-text audit cho Kwon (2026), Wang et al. (2024) và Albayrak et al. (2025), rồi cập nhật Proposal; không tiếp tục gom thêm nguồn chung chung.

---

## 6. APA References — Round 3 Shortlist

Albayrak, T., Kılıçarslan, Ö., Fong, L. H. N., Caber, M., & Güven Hamurişçi, A. (2025). Unravelling the influence of service failure on negative customer engagement: The moderating role of service recovery. *International Journal of Hospitality Management, 130*, 104242. https://doi.org/10.1016/j.ijhm.2025.104242

Kalnaovakul, K., Balasubramanian, K., & Chuah, S. H.-W. (2024). Service quality, customer sentiment and online ratings of beach hotels: An analysis of moderating factors. *Journal of Hospitality and Tourism Insights*. https://doi.org/10.1108/JHTI-06-2024-0591

Kwon, W. (2026). Aspect-based sentiment analysis through zero-shot text classification and impact-asymmetry analysis. *International Journal of Hospitality Management, 133*, 104397. https://doi.org/10.1016/j.ijhm.2025.104397

Li, S., Zhu, B., Zhang, Y., Liu, F., & Yu, Z. (2024). A two-stage nonlinear user satisfaction decision model based on online review mining: Considering non-compensatory and compensatory stages. *Journal of Theoretical and Applied Electronic Commerce Research, 19*(1), 272–296. https://doi.org/10.3390/jtaer19010015

McCullough, H., Padgett, D., Han, S., Lee, K., Martin, D. S., & Bourdeau, B. L. (2024). First impressions vs. the peak-end rule: Episodic evaluations in a service experience and the moderating effect of retrospective delay. *Journal of Business Research, 185*, 114899. https://doi.org/10.1016/j.jbusres.2024.114899

Sharma, A., Shin, S., Nicolau, J. L., & Park, S. (2025). The review sentiment garden: Blossoming loss aversion and diminishing sensitivity across time and crisis. *International Journal of Hospitality Management, 129*, 104170. https://doi.org/10.1016/j.ijhm.2025.104170

Wang, J., Wu, J., Sun, S., & Wang, S. (2024). The relationship between attribute performance and customer satisfaction: An interpretable machine learning approach. *Data Science and Management, 7*(3), 164–180. https://doi.org/10.1016/j.dsm.2024.01.003

Xu, W., Yao, Z., Ma, Y., & Li, Z. (2025). Understanding customer complaints from negative online hotel reviews: A BERT-based deep learning approach. *International Journal of Hospitality Management, 126*, 104057. https://doi.org/10.1016/j.ijhm.2024.104057

Zhong, K., Liu, K., Gao, X., & Liu, Y. (2026). Impact of sensory clues in reviews on hotel ratings. *Annals of Tourism Research, 119*, 104208. https://doi.org/10.1016/j.annals.2026.104208

---

## 7. Curation & Kế hoạch xử lý tài liệu sau Round 3

### 7.1. Bài cũ hoặc không còn cần cho hướng hiện tại

#### A. Cũ nhưng vẫn phải giữ

| Bài | Xử lý |
|---|---|
| Valdivia et al. (2019) | Giữ làm provenance của unified index; không dùng làm evidence hiện hành |
| Almansour et al. (2022) | Giữ cho định nghĩa TRRD và weak-label warning |
| Bigne et al. (2023) | Ngoài/giáp cửa sổ chủ động nhưng rất hợp RQ3 mới; vẫn dùng |
| Puh & Bagić Babac (2023) | Legacy technical baseline; không đưa vào lập luận discrepancy chính |

#### B. Có thể loại khỏi active reading set

- **Topçu et al. (2026):** rating prediction dùng chính rating làm label.
- **McMurry (2026):** conference paper, implicit hostel socialness, không có discrepancy.
- **Patil et al. (2026):** preprint, Yelp/restaurant, không có rating discrepancy.
- **McCullough et al. (2024):** theory thú vị nhưng không operationalize được bằng dataset hiện tại.
- **Kalnaovakul et al. (2024):** moderators chính không tồn tại trong dataset.
- **Nhánh forgiveness/justice/empathy:** giữ 1–2 bài nền, không cần lấy toàn bộ nếu nhóm chốt RQ3 mới.

> **Nguyên tắc:** Không nên xóa file đã tải; toàn bộ file cũ/lệch hướng (Topçu, McMurry, Patil, Puh) đã được chuyển về thư mục `refs/08_legacy/` (trước 2026-09-23 tên là `refs/legacy/`) để giữ trọn vẹn audit trail.

### 7.2. Tình trạng hàng đợi lấy toàn văn

- **Đã lấy (1/8):** Sharma et al. (2025), accepted manuscript.
- **Còn lại (7/8), theo thứ tự ưu tiên:**
  1. Kwon (2026)
  2. Wang et al. (2024)
  3. Öztürk (2026)
  4. Albayrak et al. (2025)
  5. Xu et al. (2025)
  6. Zhong et al. (2026)
  7. Doan et al. (2025)

Không tiếp tục cào rộng ngoài hàng đợi này. Các nguồn forgiveness, helpfulness và Peak-End chỉ lấy khi RQ3 cuối cùng thực sự sử dụng construct tương ứng.
