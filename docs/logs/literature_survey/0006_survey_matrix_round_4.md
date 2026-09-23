# Literature Survey — Round 4: Verification Round

- **Ngày quét:** 2026-09-23
- **Cửa sổ chủ động:** 2023-09-23 đến 2026-09-23 theo `RDR-0002`
- **Chế độ:** Targeted scoping round; **không** phải systematic review, không tuyên bố PRISMA
- **Điểm xuất phát:** Round 3 đã chốt cơ chế asymmetric compensation và RQ3 đã được khóa trong `RDR-0004`. Nhóm chưa tự tin nên mở Round 4 để **kiểm chứng** chứ không phải để mở rộng phạm vi.
- **Mục tiêu:** vá đúng hai lỗ hổng bằng chứng đã xác định trong thư viện, cộng một nhánh phản biện bắt buộc.
- **Tiêu chí đã cố định trước khi quét** (Mục 1), kết quả điền ở Mục 2–7 sau khi xác minh.

---

## 1. Search Protocol

### 1.1. Năm câu hỏi quét

| # | Nhóm | Câu hỏi |
| --- | --- | --- |
| A | Aspect asymmetry | Nguồn nào phân loại thuộc tính khách sạn theo **vai trò bất đối xứng** (penalty-dominant / dissatisfier / basic vs reward / satisfier / excitement) và có mô hình hóa được trên dữ liệu hiện có? |
| B | Severity & recovery | **Severity** của lỗi và **service recovery** thay đổi khả năng bù trừ như thế nào, và đo được bằng **văn bản review** hay chỉ bằng bảng hỏi? |
| C | Novelty check | Đã có ai công bố thước đo discrepancy **có dấu ở cấp khía cạnh** chưa? Đây là câu hỏi **điều tra âm tính** — tìm được thứ đã tồn tại là kết quả có giá trị, không phải thất bại. |
| D | Counter-evidence | Bằng chứng nào **chống lại** cơ chế penalty-dominant (bù trừ cân xứng, positivity bias, hoặc inconsistency chỉ là nhiễu đo lường)? |
| E | Baseline & prior art | Baseline dự báo/giải thích cấp aspect nào dùng lại được cho artifact ứng dụng của môn DAP391m? |

Nhóm D là **bắt buộc** theo checkpoint devil's advocate của quy trình: không được chỉ tìm nguồn ủng hộ giả thuyết.

### 1.2. Nguồn và truy vấn

- **Nguồn:** Crossref API, OpenAlex, Semantic Scholar, DOAJ, trang landing page của nhà xuất bản; web search để mở rộng.
- **Truy vấn chính:**
  - `hotel attributes asymmetric impact satisfaction penalty reward Kano three-factor journal`
  - `impact asymmetry analysis penalty reward contrast hotel satisfaction`
  - `negative attribute performance hurts more than positive helps hotel rating`
  - `service failure severity moderating effect overall satisfaction hotel rating`
  - `service recovery paradox hotel review rating attenuation`
  - `failure severity detected from online review text star rating hotel`
  - `signed aspect-level sentiment rating discrepancy measure hotel`
  - `aspect-implied rating versus observed rating hotel reviews`
  - `customer ratings as weak sentiment labels noise annotation`
  - `positivity bias star ratings online reviews`
  - `interpretable aspect-based rating prediction hotel review SHAP explainable`
  - `hospitality ABSA benchmark dataset aspect sentiment`
- **Thứ tự:** journal trước conference/preprint; publisher/DOI trước repository; nguồn đóng được sàng lọc song song nguồn mở.

### 1.3. Inclusion / Exclusion

**Include:**

1. Bài **journal**, tiếng Anh, trong cửa sổ 2023-09-23 → 2026-09-23.
2. Có liên hệ trực tiếp tới một trong năm câu hỏi ở Mục 1.1.
3. Có DOI xác minh được, hoặc tối thiểu xác minh được tồn tại qua trang nhà xuất bản/hội nghị đã mở.
4. Nguồn cũ hơn cửa sổ chỉ nhận khi là **provenance** của construct/thang đo mà bài mới chỉ trích dẫn lại — và phải ghi rõ lý do ngoại lệ.

**Exclude:**

1. Khác domain mà **không** chuyển giao được cấu trúc phương pháp (ví dụ sentiment analysis cho sản phẩm điện tử không có rating text).
2. Không xác minh được DOI hoặc không mở được trang xác nhận → `UNVERIFIABLE`, **không** vào matrix.
3. Venue predatory, không có peer review, hoặc không index.
4. Trùng với 30 nguồn đã có trong `refs/INDEX.md` (dedupe theo DOI rồi theo title).
5. Chỉ ở mức abstract mà **không** bổ sung khái niệm mới so với nguồn đã có — ngoại lệ nếu nguồn đã có cũng chỉ ở mức abstract và nguồn mới là journal cùng chủ đề.

### 1.4. Mức bằng chứng (evidence level)

Mọi nguồn vào matrix nhận một mức theo thang I–VII của quy trình:

| Mức | Loại |
| --- | --- |
| I | Systematic review / meta-analysis |
| II | Thí nghiệm ngẫu nhiên |
| III | Nghiên cứu có đối chứng, không ngẫu nhiên |
| IV | Dữ liệu quan sát quy mô lớn / longitudinal |
| V | Systematic review của nghiên cứu mô tả |
| VI | Nghiên cứu mô tả/định tính đơn lẻ |
| VII | Ý kiến chuyên gia |

### 1.5. Quy tắc xác minh (bắt buộc trước khi vào matrix)

1. Mọi DOI phải tra **Crossref** và **OpenAlex**; khớp title (similarity ≥ 0,70) và năm ±1.
2. DOI resolve nhưng title lệch nặng → gắn `DOI_MISMATCH` và **loại**.
3. Không xác minh được → `UNVERIFIABLE` và loại. **Vùng xám tính là thất bại**, không được ghi vào matrix như "chưa chắc".
4. Không tự suy đoán DOI, số trang, hay tên tạp chí. Thiếu thì ghi thiếu.

### 1.6. Baseline để dedupe

30 mục đã có trong `refs/INDEX.md` (19 PDF toàn văn + 6 bài đóng + 5 mục metadata/đã bỏ), trong đó 22 DOI đã đăng ký:

```
10.1016/j.ijhm.2026.104574  10.1016/j.ijhm.2025.104397  10.1016/j.ijhm.2025.104170
10.1016/j.dsm.2024.01.003   10.1016/j.ijhm.2024.104057  10.1016/j.annals.2026.104208
10.1016/j.ijhm.2025.104242  10.1007/s11042-024-19518-9  10.1016/j.ijhm.2025.104271
10.14329/apjis.2025.35.1.49 10.1007/s11628-023-00524-0  10.1109/access.2026.3672490
10.3390/jtaer19010015       10.1145/3605152             10.1002/mar.22138
10.1007/s40558-025-00314-6  10.1016/j.dss.2025.114450   10.1016/j.neucom.2018.09.096
10.1186/s43093-022-00114-y  10.1108/JHTI-02-2022-0078   10.1016/j.jbusres.2024.114899
10.1108/JHTI-06-2024-0591   arXiv:2606.25518             arXiv:2606.00084
```

---

## 2. Evidence Matrix

### Cluster B — Severity & service recovery (đã xác minh)

| # | Nguồn | Venue | Loại | Truy cập | Mức | Vì sao vào Round 4 |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | Das, M., Jebarajakirthy, C., Maseeh, H. I., Lim, W. M., & Shah, J. S. (2026). *Online service failure and recovery: An integrated meta-analytic perspective of attribution and justice theories*. [10.1016/j.jbusres.2025.115752](https://doi.org/10.1016/j.jbusres.2025.115752) | Journal of Business Research, 202, 115752 | journal | đóng (hybrid) | **I** | Meta-analysis 147 nghiên cứu, N=82.901 — mức bằng chứng cao nhất thư viện đang có cho cơ chế recovery |
| B2 | Tengilimoglu, E., & Öztürk, Y. (2024). *The effects of eWOM triggered service recovery on customer citizenship behavior in the hospitality industry: The moderating role of failure severity*. [10.1002/jtr.2673](https://doi.org/10.1002/jtr.2673) | International Journal of Tourism Research, 26(4), e2673 | journal | mở | III | **Severity là moderator trực tiếp**: recovery hiệu quả với lỗi nhẹ, giảm mạnh khi lỗi nặng |
| B3 | Leo, W. W. C., Maggioni, I., Sembada, A. Y., & Tsarenko, Y. (2026). *The dynamics of customer participation in service recovery: The roles of failure severity, quality signals, and responsiveness*. [10.1016/j.ijhm.2026.104809](https://doi.org/10.1016/j.ijhm.2026.104809) | International Journal of Hospitality Management, 140, 104809 | journal | mở (hybrid) | III | Severity trong bối cảnh khách sạn; quality signal đảo chiều trách nhiệm recovery — ứng viên cho `Severity` |
| B4 | Hwang, J. (2024). *The effects of service recovery actions on customers' post-recovery responses to online travel agencies (OTAs): The moderating role of price*. [10.1002/jtr.2742](https://doi.org/10.1002/jtr.2742) | International Journal of Tourism Research, 26(4), e2742 | journal | mở | III | **Double deviation** — lỗi ban đầu + recovery thất bại tạo penalty phi tuyến; đúng cơ chế penalty-dominant |
| B5 | Lim, W. M., Saha, V., & Das, M. (2025). *From service failure to brand loyalty: evidence of service recovery paradox*. [10.1057/s41262-025-00380-5](https://doi.org/10.1057/s41262-025-00380-5) | Journal of Brand Management, 32(4), 257–281 | journal | mở | IV | Giới hạn trên của bù trừ: khi nào recovery vượt cả mức nền — chặn việc diễn giải `D > 0` quá rộng |
| B6 | Tan, K. P.-S., & Zou, S. (2024). *The profitable art of managerial responses to online reviews: A justice-based investigation of service recovery and firm-level operating performance*. [10.1080/1528008X.2024.2410214](https://doi.org/10.1080/1528008X.2024.2410214) | Journal of Quality Assurance in Hospitality & Tourism, 1–26 | journal | đóng | IV | Recovery đo **từ văn bản review và phản hồi của khách sạn**, không phải bảng hỏi — đúng dạng ta cần |

### Cluster E — Baseline giải thích được & prior art cho artifact

| # | Nguồn | Venue | Loại | Truy cập | Mức | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | Pramono, B. A., Gernowo, R., & Sofwan, A. (2026). *Explainable multilingual aspect-based sentiment analysis for tourism using SHAP and LIME*. [10.48084/etasr.18774](https://doi.org/10.48084/etasr.18774) | Engineering, Technology & Applied Science Research, 16(3), 37077–37084 | journal | mở (gold) | VI | Bản thiết kế cho tầng giải thích của app: SHAP + LIME + kiểm định faithfulness bằng eraser. **Cảnh báo venue:** không nằm trong DOAJ, không phải core source — dùng cho kỹ thuật, không dùng làm bằng chứng domain |
| E2 | You, X.-Y., Chang, S.-C., Hung, S.-M., Ku, C.-H., & Chang, Y.-C. (2024). *Using multitask learning with pre-trained language models for aspect-based sentiment analysis in the hospitality industry*. [ACL Anthology 2024.paclic-1.12](https://aclanthology.org/2024.paclic-1.12/) | PACLIC 2024, 131–140 | **conference** | mở | VI | Số baseline dùng được ngay: RoBERTa đa nhiệm AUROC 0,9214 · AUPRC 0,6152 · F1 0,5817 trên 8 khía cạnh; so XGBoost 0,4938 và LSTM-attention 0,4208. Không có DOI |
| E3 | Guidotti, D., Pandolfo, L., & Pulina, L. (2025). *Discovering sentiment insights: streamlining tourism review analysis with large language models*. [10.1007/s40558-024-00309-9](https://doi.org/10.1007/s40558-024-00309-9) | Information Technology & Tourism, 27(1), 227–261 | journal | mở (hybrid) | IV | Zero-shot LLM cho phân loại cảm xúc + trích từ khóa, đóng khung như **công cụ hỗ trợ ra quyết định cho quản lý** — prior art cho mục đích của app |
| E4 | Hu, F., Pan, J., & Wang, H. (2024). *Unveiling the spatial and temporal variation of customer sentiment in hotel experiences: a case study of Beppu City, Japan*. [10.1057/s41599-024-04226-4](https://doi.org/10.1057/s41599-024-04226-4) | Humanities and Social Sciences Communications, 11(1), 1695 | journal | mở (gold, DOAJ, core) | IV | **Giá trị cao nhất cluster**: 4.004 review TripAdvisor / 233 khách sạn, phát hiện **694 review (17,3%)** có bất nhất cảm xúc–điểm rõ rệt, tách theo hạng khách sạn và nhóm khách. Mốc so sánh trực tiếp cho prevalence của RQ1 |
| E5 | Kumar, M., Kumar, C., Kumar, N., & Kavitha, S. (2024). *Efficient hotel rating prediction from reviews using ensemble learning technique*. [10.1007/s11277-024-11457-w](https://doi.org/10.1007/s11277-024-11457-w) | Wireless Personal Communications, 137(2), 1161–1187 | journal | đóng | IV | Baseline dự báo điểm: TF-IDF + logistic/ensemble đạt 61% dự đoán đúng mức sao. **Cảnh báo venue-fit:** tạp chí viễn thông đăng bài hospitality ML — hạ mức tin cậy khi trích |
| E6 | Zhu, A., et al. (2025). *DaNet: dual-aware enhanced alignment network for multimodal aspect-based sentiment analysis*. [10.18653/v1/2025.findings-acl.741](https://doi.org/10.18653/v1/2025.findings-acl.741) | Findings of ACL 2025, 14369–14381 | **conference** | mở (gold) | VI | Đa phương thức (ảnh + chữ); dữ liệu ta chỉ có text nên **liên quan thấp** — chỉ tham khảo kỹ thuật xử lý aspect ngầm |

### Cluster D — Phản biện cơ chế penalty-dominant (checkpoint bắt buộc)

| # | Nguồn | Venue | Loại | Truy cập | Mức | Đòn phản biện |
| --- | --- | --- | --- | --- | --- | --- |
| D1 | Han, S., & Anderson, C. K. (2025). *The platform matters: Selection and measurement bias in online reviews*. [10.1177/19389655251327536](https://doi.org/10.1177/19389655251327536) | Cornell Hospitality Quarterly | journal | đóng | IV | **Nguy hiểm nhất**: so sánh khảo sát riêng với review công khai cho thấy người dùng TripAdvisor có **thiên lệch đo lường dương** — chấm cao hơn hẳn so với trải nghiệm tiêu cực họ tự khai. Nghĩa là `D > 0` có thể là artefact trình bày, không phải cơ chế bù trừ |
| D2 | Kirilenko, A., Stepchenkova, S., Gromoll, R., & Jo, Y. (2024). *Comprehensive examination of online reviews divergence over time and platform types*. [10.1016/j.ijhm.2023.103647](https://doi.org/10.1016/j.ijhm.2023.103647) | IJHM, 117, 103647 | journal | đóng | IV | 75.000 review trên 4 nền tảng: cùng một khách sạn cho ra phân bố sao và cảm xúc **khác nhau theo nền tảng** → bất nhất do cơ chế khơi gợi + tự chọn, không phải quy luật hành vi bất biến |
| D3 | Sterner, M. (2026). *Biases in online reputation systems: A survey of the empirical literature*. [10.1007/s10660-026-10176-7](https://doi.org/10.1007/s10660-026-10176-7) | Electronic Commerce Research | journal | mở (hybrid) | V | Phân rã méo thành 5 nguồn cấu trúc (tự chọn, có đi có lại, ảnh hưởng xã hội, hành động người bán, nhiễu); can thiệp nền tảng thường **làm tăng phương sai** thay vì sửa lỗi |
| D4 | Li, J., Lee, B., & Kim, J. (2025). *Analyzing factors affecting overall customer satisfaction using hotel ratings and reviews with BERTopic and three-factor theory*. [10.1177/21582440251335169](https://doi.org/10.1177/21582440251335169) | SAGE Open, 15(3), 1–15 | journal | mở (gold) | IV | PRCA trên TripAdvisor cho thấy thuộc tính lõi giữ **tác động ổn định/gần đối xứng** giữa các hạng sao, **không** penalty-dominant toàn cục |
| D5 | Slevitch, L. (2024). *Kano model categorization methods: Typology and systematic critical overview for hospitality and tourism academics and practitioners*. [10.1177/10963480241230957](https://doi.org/10.1177/10963480241230957) | Journal of Hospitality & Tourism Research | journal | bronze OA | V | **Đòn vào phương pháp**: phân loại Kano/PRCA trong hospitality có lỗi quy trình hệ thống, dễ suy ra "bất đối xứng" ở nơi thực tế là tuyến tính |
| D6 | Mellinas, J. P., Di Nolfo-Aiassa, C., & Martin-Fuentes, E. (2025). *The weight of a review: Assessing Booking.com's new scoring system*. [10.1177/14673584251384011](https://doi.org/10.1177/14673584251384011) | Tourism and Hospitality Research | journal | đóng | IV | 74.882 review: thuật toán mới của Booking.com dồn **85% trọng số vào 12 tháng gần nhất** → điểm số bị tách rời khỏi văn bản bởi chính thuật toán nền tảng |

### Cluster A — Vai trò bất đối xứng của aspect (đã xác minh)

| # | Nguồn | Venue | Loại | Truy cập | Mức | Đóng góp |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | Regitz, D., Höpken, W., & Fuchs, M. (2026). *Online customer feedback for identifying KANO product quality features: A fine-grained topic detection and sentiment analysis approach*. [10.1007/s40558-025-00354-y](https://doi.org/10.1007/s40558-025-00354-y) | Information Technology & Tourism, 28(1), Article 20 | journal | mở (hybrid) | IV | **Gần nhu cầu nhất**: hồi quy sentiment dương/âm theo topic trên TripAdvisor để phân loại Kano. Room quality = Must-Be (âm làm sập điểm, dương gần như không thưởng); connectivity = Attractive |
| A2 | Park, H., Lee, M., Back, K.-J., DeFranco, A., & Suh, J. (2025). *Dynamic roles of hotel mobile application in customer satisfaction and dissatisfaction: Integrating text analytics and impact asymmetry analysis*. [10.1108/IJCHM-12-2023-1914](https://doi.org/10.1108/IJCHM-12-2023-1914) | IJCHM, 37(5), 1622–1640 | journal | đóng | IV | Impact Asymmetry Analysis trên **88.309 review**: information quality = satisfier, system quality/failure = dissatisfier. Bằng chứng quy mô lớn cho bất đối xứng trong hospitality |
| A3 | Li, J., Lee, B., & Kim, J. (2025). *Analyzing factors affecting overall customer satisfaction using hotel ratings and reviews with BERTopic and three-factor theory*. [10.1177/21582440251335169](https://doi.org/10.1177/21582440251335169) | SAGE Open, 15(3), 1–17 | journal | mở (gold) | IV | **Trùng với D4** — cùng một bài do hai cluster tìm độc lập. Ghi một lần; dùng ở cả hai vai trò: ủng hộ PRCA và làm phản biện |
| A4 | Zhang, F., Seshadri, K., Liu, S., & Santamouris, M. (2025). *The impact of indoor environmental quality on tourist accommodation ratings using guest reviews*. [10.1016/j.buildenv.2025.113135](https://doi.org/10.1016/j.buildenv.2025.113135) | Building and Environment, 280, 113135 | journal | đóng (hybrid) | IV | **>540.000 review**: thuộc tính môi trường trong nhà (sạch sẽ, không khí, âm thanh) là Basic/penalty-dominant. Dữ liệu vật lý, không bảng hỏi |
| A5 | Cui, J., Zhang, S., & Wang, L. (2025). *Evaluating canal heritage tourists' satisfaction: An asymmetric impact-performance analysis of the Grand Canal in Beijing, China*. [10.1016/j.jhtm.2025.01.002](https://doi.org/10.1016/j.jhtm.2025.01.002) | Journal of Hospitality and Tourism Management, 62, **108–115** | journal | đóng | IV | AIPA + PRCA: chỉ số penalty vượt chỉ số reward với thuộc tính hạ tầng nền. **Đính chính:** scout ghi trang 172–184, Crossref xác nhận **108–115** |

### Cluster A — bị loại

| Nguồn | Lý do |
| --- | --- |
| Yousaf, S., & Kim, J. M. (2023). *Did COVID-19 change preferences for hygiene-related service attributes as satisfiers and dissatisfiers?* [10.1016/j.jhtm.2023.07.001](https://doi.org/10.1016/j.jhtm.2023.07.001) · JHTM 56, 264–271 | **Ngoài cửa sổ**: công khai lần đầu 2023-07-05, trước mốc 2023-09-23. Không phải provenance của construct nào ta đang dùng → loại theo `RDR-0002`, không cần ngoại lệ citation-chain |

### Cluster C — Lân cận vùng tính mới (kiểm tra điều tra âm tính)

| # | Nguồn | Venue | Loại | Truy cập | Mức | Vì sao KHÔNG trùng niche |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | Biasetton, N., Ricciardi, G., & Salmaso, L. (2026). *How well do ratings reflect sentiment? Evidence from a large Italian review corpus*. [10.1002/asmb.70090](https://doi.org/10.1002/asmb.70090) | Applied Stochastic Models in Business and Industry, 42(2) | journal | đóng (hybrid) | IV | So **text-implied rating** (AlBERTo + CORAL ordinal regression) với sao → **đúng ý tưởng nhưng ở cấp toàn văn bản**, trên sản phẩm bán lẻ. Không có chiều khía cạnh |
| C2 | Marreira et al. (2026). *Rating–text mismatch in Brazilian Portuguese reviews: How reliable are zero-shot LLMs?* [ACL Anthology 2026.propor-1.96](https://aclanthology.org/2026.propor-1.96/) | PROPOR 2026, 959–967 | **conference** | mở | VI | Phát hiện bất nhất như **phân loại nhị phân cấp văn bản** (1 sao vs 5 sao) — không có dấu liên tục, không theo khía cạnh |
| C3 | Liu, X., Ma, X., & Dou, Y. (2025). *Injecting new insights: How do review sentiment and rating inconsistency shape the helpfulness of airline reviews?* [10.1016/j.ipm.2025.104088](https://doi.org/10.1016/j.ipm.2025.104088) | Information Processing & Management, 62(2), 104088 | journal | đóng (hybrid) | IV | Bất nhất là **scalar tổng hợp**, outcome là helpfulness. Không tách theo khía cạnh |
| C4 | Kovács, I. (2025). *The impact of construal level on review consistency and helpfulness in online evaluations*. [10.1016/j.chb.2024.108550](https://doi.org/10.1016/j.chb.2024.108550) | Computers in Human Behavior, 162, 108550 | journal | đóng | IV | Đo consistency text–sao như **khoảng cách tuyệt đối cấp văn bản**, biến điều tiết là mức construal |
| C5 | Patil et al. (2026). *Beyond the star rating*. arXiv:2602.21082 | arXiv preprint | preprint | mở | VI | Hồi quy aspect → rating; phần dư là **sai số**, không phải tín hiệu có dấu. **Đã có trong thư viện** ở nhóm legacy |

Kết luận nhóm này và giới hạn của nó: xem Mục 4.3.

## 3. Verification & Grading

### 3.1. Phương pháp

Mỗi DOI tra độc lập qua **Crossref** và **OpenAlex**; đối chiếu title và năm. Ngưỡng: similarity ≥ 0,70 **hoặc** một chuỗi chứa chuỗi kia (luật containment, dùng khi nguồn được trích bằng title rút gọn). Lệch cả hai → loại.

**Bài học phương pháp:** lần chạy đầu dùng title rút gọn nên hai bài B3 và B6 bị gắn cờ `CHECK` giả (similarity 0,63 và 0,58). Khi tra lại bằng title đầy đủ, cả hai khớp 1,00. Từ đây: **luôn xác minh bằng title đầy đủ**.

### 3.2. Kết quả Cluster B

| DOI | Crossref | OpenAlex | OA | Kết luận |
| --- | --- | --- | --- | --- |
| 10.1016/j.jbusres.2025.115752 | JBR, 2026, khớp 1,00 | JBR, 2025, khớp 1,00 | hybrid | **VERIFIED** |
| 10.1002/jtr.2673 | IJTR, 2024, khớp 0,80 | IJTR, 2024, khớp 0,84 | hybrid | **VERIFIED** |
| 10.1016/j.ijhm.2026.104809 | IJHM, khớp 1,00 | IJHM, 2026, khớp 1,00 | hybrid | **VERIFIED** |
| 10.1002/jtr.2742 | IJTR, 2024, khớp 0,80 | IJTR, 2024, khớp 0,83 | hybrid | **VERIFIED** |
| 10.1057/s41262-025-00380-5 | JBM, 2025, khớp 1,00 | JBM, 2025, khớp 1,00 | hybrid | **VERIFIED** |
| 10.1080/1528008X.2024.2410214 | JQAH&T, 2024, khớp 1,00 | JQAH&T, 2024, khớp 1,00 | closed | **VERIFIED** |

Không bài nào trùng thư viện hiện có (đã dedupe theo DOI). Không bài nào bị retract.

### 3.3. Ca biên về ngày xuất bản — cần người quyết

**B3 (Leo et al., IJHM 140, 104809)** có dữ liệu ngày không nhất quán:

- Crossref `created` = **2026-06-29** (bài được đăng ký và công khai)
- Crossref `published-print` / `issued` = **2027-01** (số tạp chí gán cho năm sau)
- OpenAlex `publication_year` = 2026

`RDR-0002` mục 2.1 quy định dùng **ngày công bố công khai đầu tiên, online-first nếu có, nếu không thì dùng ngày phát hành số tạp chí**. Ở đây `published-online` trống, nên luật dự phòng cho ra **2027-01** → nằm **ngoài** cửa sổ 2023-09-23 → 2026-09-23. Nhưng bài đã truy cập được công khai từ 2026-06-29 → nằm **trong** cửa sổ.

Đây là lỗ hổng của luật hiện hành, không phải lỗi dữ liệu. Đề xuất: ghi nhận B3 là **ca biên**, giữ trong matrix kèm ghi chú, và làm rõ luật trong `RDR-0002` (nhận `created` khi `published-online` trống).

## 4. Cross-Source Synthesis

### 4.1. Round 4 trả lời được gì

| Câu hỏi quét | Kết luận sau Round 4 |
| --- | --- |
| A — vai trò bất đối xứng của aspect | **Trả lời được.** Bất đối xứng được xác nhận trên nhiều bối cảnh và quy mô lớn (A2 88.309 review; A4 >540.000 review), với cơ chế phân loại dùng được (Must-Be / Attractive / Basic). Vùng này từ mỏng thành dày |
| B — severity & recovery | **Trả lời được.** Severity là moderator thật (B2, B3); double deviation tạo penalty phi tuyến (B4); recovery đo được **từ văn bản** chứ không chỉ bảng hỏi (B6) |
| C — kiểm tra tính mới | **Không tìm thấy tiền lệ trực tiếp** cho thước đo có dấu ở cấp khía cạnh (chi tiết 4.3) |
| D — phản biện | **Có đòn đáng kể** — xem Mục 5; cơ chế sống sót nhưng phải hạ giọng |
| E — baseline cho artifact | **Có số dùng ngay** (E2: RoBERTa đa nhiệm F1 0,5817 cho 8 khía cạnh) và prior art cho mục đích hỗ trợ ra quyết định (E3) |

### 4.2. Điều hội tụ và điều xung đột

**Hội tụ mạnh:**

1. **Bất đối xứng là có thật nhưng có điều kiện.** A1 (room = Must-Be), A2 (system quality = dissatisfier), A4 (môi trường trong nhà = Basic), A5 (hạ tầng nền: penalty > reward) nhất quán với B1 (meta-analysis: justice quyết định mức phục hồi) và với C1 (bất nhất mạnh nhất ở mức 2 và 4 sao — nơi đánh giá hỗn hợp bị nén vào một điểm).
2. **Điểm sao không phải nhãn cảm xúc hợp lệ.** C1 nói thẳng: không được dùng star rating làm ground truth cảm xúc nếu chưa kiểm chứng bằng văn bản. E4 và D1 đo được bất nhất ở hai mẫu độc lập (17,3% và thiên lệch dương trên TripAdvisor). Nguyên tắc tách hai họ mô hình của đề tài được củng cố.
3. **Severity và recovery là biến điều kiện, không phải biến nền.** B2, B3, B4, B6 đều cho cùng hướng.

**Xung đột thật cần ghi nhận:**

- **A4 nói thuộc tính vật lý là penalty-dominant; D4 nói thuộc tính lõi gần đối xứng.** Hai kết quả này không mâu thuẫn về dữ liệu mà khác **đơn vị phân tích và cách phân loại**: A4 dùng thuộc tính môi trường trong nhà, D4 dùng thuộc tính dịch vụ ở cấp hạng sao. Điều này **ủng hộ** khung "vai trò phụ thuộc bối cảnh" thay vì "penalty luôn thắng".
- **D5 cảnh báo chính công cụ** mà A1/A2/A4/A5 dùng (Kano/PRCA) là dễ phân loại sai. Nghĩa là nhóm A đáng tin về **hướng**, nhưng danh tính từng aspect cụ thể phải coi là khám phá.

### 4.3. Kiểm tra tính mới — kết luận và giới hạn của nó

Scout kết luận **không có nghiên cứu nào định nghĩa thước đo discrepancy có dấu ở cấp khía cạnh trong review khách sạn**, và chia văn hiến thành hai nhánh không nối nhau: (1) bất nhất cấp văn bản, (2) ABSA dự báo điểm — nhánh (2) coi phần dư là sai số chứ không phải tín hiệu hành vi có dấu.

**Tôi tự kiểm chứng lại độc lập** (không nhận thẳng kết luận của scout) bằng truy vấn OpenAlex trên `title_and_abstract.search`, cửa sổ 2023–2026, với 5 truy vấn mở rộng. Kết quả:

- Không bài nào đo khoảng cách **có dấu theo từng khía cạnh cho từng review**.
- Các bài gần nhất và lý do không trùng: *Consistency Matters: Dimension-Level Characteristics* (2025) — cấp chiều nhưng outcome là helpfulness · *Does Online Review Inconsistency Matter?* (2024) — outcome là doanh số · *Understanding the Impact of Inconsistency on the Helpfulness of Online Reviews* (2025) — cấp văn bản · *Identification of Inconsistent Reviews and Ratings on Apps* (2025) — cấp ứng dụng, không theo khía cạnh.

**Giới hạn phải ghi:** tìm kiếm theo từ khóa trên title/abstract **không chứng minh được sự vắng mặt**. Đây là bằng chứng ủng hộ tính mới, không phải giấy chứng nhận. Cách xử lý đúng: viết trong proposal là "chưa tìm thấy công thức nào đo discrepancy có dấu ở cấp khía cạnh", kèm mô tả cách đã tìm — chứ không viết "chưa ai làm".

**Ranh giới tính mới đang mỏng hơn tưởng.** A1 (Regitz et al. 2026) làm gần đúng việc ta dự định: hồi quy sentiment dương/âm theo topic để phân loại Kano. Khác biệt còn lại của ta chỉ là: (a) thước đo **có dấu ở cấp khía cạnh** thay vì hệ số hồi quy theo topic, và (b) đơn vị là review có nhãn người gán chứ không phải topic khai phá. Đây là khác biệt thật nhưng **không lớn**, và phải được nói rõ trong phần đóng góp.

### 4.4. Đính chính metadata trong Round 4

| Vấn đề | Scout báo | Xác minh lại |
| --- | --- | --- |
| C3 (Information Processing & Management) | "Li et al." | Tác giả thật: **Liu, Ma, Dou** — Crossref |
| A5 (JHTM) | trang 172–184 | Crossref: **108–115** |
| D6, A5 bị cờ title | nghi lệch | Do dấu nháy Unicode; title khớp chính xác |
| C5 (Patil, arXiv:2602.21082) | đề xuất mới | **Đã có trong thư viện** ở nhóm legacy |
| A3 và D4 | hai mục riêng | **Cùng một bài** (SAGE Open) — hai cluster tìm độc lập |

## 5. Devil's Advocate Check

Checkpoint bắt buộc: tìm bằng chứng **chống lại** cơ chế mà đề tài đang dựa vào. Cluster D trả về 6 nguồn, và chúng tấn công ở ba hướng khác nhau. Đánh giá thẳng từng hướng.

### 5.1. Ba đòn phản biện và mức độ nguy hiểm

**Đòn 1 — "Đó là thiên lệch đo lường, không phải cơ chế bù trừ" (D1 Han & Anderson; D3 Sterner; D6 Mellinas)**

Đây là đòn nặng nhất. Nếu người dùng TripAdvisor vốn có thiên lệch dương khi chấm công khai so với trải nghiệm riêng, thì `D > 0` (điểm cao hơn văn bản biện minh) có thể chỉ là **hiệu ứng trình bày xã hội**, không phải khách "thăng hoa" hay "bỏ qua lỗi". D3 còn cho thấy méo đến từ 5 nguồn cấu trúc, còn D6 cho thấy chính thuật toán nền tảng dồn 85% trọng số vào 12 tháng gần nhất khiến điểm số tách rời khỏi văn bản.

*Mức độ:* **Cao.** Nhưng lưu ý nó tấn công cách **diễn giải**, không tấn công hiện tượng: bất nhất vẫn đo được, chỉ là nguyên nhân không được khẳng định.

**Đòn 2 — "Bất nhất phụ thuộc nền tảng, không phải quy luật" (D2 Kirilenko)**

Cùng một khách sạn cho ra phân bố sao và cảm xúc khác nhau giữa TripAdvisor, Expedia, Hotels.com, Booking.com.

*Mức độ:* **Vừa.** Nó không phủ định phát hiện của ta, nhưng chặn mọi tuyên bố khái quát ra ngoài TripAdvisor.

**Đòn 3 — "Công cụ phân loại của các anh có lỗi" (D5 Slevitch; D4 Li et al.)**

D5 nói thẳng: phân loại Kano/PRCA trong hospitality có lỗi quy trình hệ thống và **hay suy ra bất đối xứng nơi thực tế là tuyến tính**. D4 thì đưa bằng chứng cụ thể ngược lại: thuộc tính lõi giữ tác động ổn định/gần đối xứng giữa các hạng sao.

*Mức độ:* **Cao đối với kiểm định phụ #1.** Kiểm định phụ #1 của RQ3 chính là "aspect nào penalty-dominant, aspect nào reward" — và D5 nói rằng công cụ để trả lời câu đó có thể sai. Đòn này cũng trúng vào `Kwon (2026)`, nguồn Kano mà ta đang chờ.

### 5.2. Hệ quả — bốn thay đổi phải đưa vào kế hoạch

| # | Thay đổi | Vì sao |
| --- | --- | --- |
| 1 | Thêm hạn chế tường minh: **không phân biệt được bù trừ thật với thiên lệch trình bày** khi chỉ dùng review công khai | D1, D3, D6. Đây là hạn chế về nhận dạng (identification), không phải lỗi cẩu thả |
| 2 | Mọi tuyên bố prevalence phải **ghi phạm vi TripAdvisor 2015–2023** | D2 |
| 3 | Phân loại aspect theo Kano chỉ được trình bày như **phân tích khám phá**, kèm báo cáo bất định; không dùng như construct đã kiểm định | D5 |
| 4 | Khung **hai nhánh** (compensatory vs non-compensatory) là cách đặt đúng, **không** được viết thành "penalty luôn thắng" | D4 — chính nguồn phản biện xác nhận khung có điều kiện của ta |

### 5.3. Điều đòn phản biện KHÔNG phá được

Cluster D **không** nguồn nào phủ định rằng:

1. Bất nhất cảm xúc–điểm tồn tại với tỷ lệ đáng kể (D1 và D2 đều đo được nó, chỉ khác cách giải thích).
2. Cần một thước đo có dấu ở cấp khía cạnh — ngược lại, D2 và D6 là lập luận **ủng hộ** việc không dùng điểm sao thô làm thước đo cảm xúc.
3. Đề tài phải tách mô hình cảm xúc khỏi nhãn sao. D1 chính là bằng chứng mạnh nhất cho nguyên tắc này.

### 5.4. Phán quyết checkpoint

**PASS có điều kiện.** Cơ chế asymmetric compensation sống sót, nhưng chỉ ở dạng **có điều kiện, giới hạn nền tảng, và có ý thức về đo lường**. Hai điều chỉnh không thương lượng: (a) bỏ mọi ngôn ngữ khẳng định nhân quả về "khách tha thứ" khi chỉ có dữ liệu công khai; (b) hạ kiểm định phụ #1 xuống mức khám phá.

Điểm tích cực: D5 và D4 là **vũ khí phòng thủ** khi bảo vệ đề tài. Nếu người phản biện nói "Kano asymmetry là hiển nhiên", ta có sẵn nguồn nói rằng nó không hiển nhiên chút nào và thường bị suy diễn sai. Việc nhóm tự tìm ra đòn chống lại mình trước là điểm cộng khi vấn đáp.

## 6. Endpoint Check

Đối chiếu bốn tiêu chí dừng của `RDR-0001` sau Round 4:

| # | Tiêu chí | Trước Round 4 | Sau Round 4 |
| --- | --- | --- | --- |
| 1 | Bão hòa lý thuyết & phương pháp | Không đạt | **Vẫn không đạt** — Round 4 sinh thêm Kano/three-factor, PRCA, AIPA, service recovery paradox, và 6 nguồn phản biện. Điều này xác nhận: cửa sổ 36 tháng còn nhiều nguồn mới, nên tiêu chí này không thể đạt bằng cách quét trong cửa sổ |
| 2 | 10–15 bài hạt nhân chia đều 3 cụm | Lệch cụm | **Đạt về số lượng, lệch về cấu trúc cụm** — cần `RDR-0005` định nghĩa lại cụm 3 (Asymmetric/Non-compensatory thay Forgiveness) |
| 3 | Đủ nguyên liệu Proposal | Đạt một phần (thiếu biến phụ thuộc) | **Đạt** — biến phụ thuộc có 3 ứng viên + tiêu chí chọn đăng ký trước; RQ3 đã khóa |
| 4 | ≥1 baseline đối chứng | Đạt | **Đạt vững hơn** — thêm E2 (F1 0,5817 cho 8 khía cạnh), E5 (61% dự đoán đúng mức sao), A1 (phân loại Kano từ review) |

**Đọc kết quả này cho đúng:** Round 4 **không** đưa khảo sát tới endpoint theo nghĩa bão hòa, và điều đó là bình thường — vì tiêu chí 1 được viết cho một đợt quét rộng, còn từ `RDR-0003` trở đi ta chủ động quét targeted. Giá trị của Round 4 nằm ở tiêu chí 3 và 4: hai trụ cột từng mỏng nay đã đủ, và tính mới đã được kiểm tra độc lập.

**Kết luận vận hành:** đủ điều kiện đóng khảo sát **có điều kiện**, với hai việc phải ghi vào `RDR-0005`: miễn tiêu chí bão hòa kèm lý do, và định nghĩa lại ba cụm tài liệu.

## 7. Curation & Next Actions

### 7.1. Nguồn mới của Round 4

**26 nguồn mới đã xác minh** (sau khi trừ trùng lặp và 1 bài ngoài cửa sổ):

| Nhóm | Số nguồn | Ghi chú |
| --- | ---: | --- |
| A — aspect asymmetry | 5 | A3 trùng D4, đếm một lần |
| B — severity & recovery | 6 | gồm 1 meta-analysis mức I |
| D — phản biện | 5 | sau khi trừ D4 |
| E — baseline & prior art | 6 | 2 bài là hội nghị |
| C — lân cận vùng tính mới | 4 | C5 đã có trong thư viện |
| **Tổng** | **26** | thêm 1 bài bị loại vì ngoài cửa sổ |

Đối chiếu mức bằng chứng: thư viện trước Round 4 có 1 mức I · 2 mức III · 15 mức IV · 2 mức V · 5 mức VI. Round 4 thêm **1 mức I**, nhiều mức III–IV, và 4 mức V–VI (hội nghị, venue chưa xác lập).

### 7.2. Toàn văn

**A. Đã tự tải — 9 bài** (kiểm trang đầu, khớp DOI). Sau khi đổi cấu trúc thư mục ngày 2026-09-23, chúng nằm ở cụm chức năng tương ứng — xem mục 8:

1. `A1_regitz_kano_quality_features_reviews.pdf`
2. `B5_lim_service_recovery_paradox.pdf`
3. `C2_marreira_rating_text_mismatch_llm.pdf`
4. `D3_sterner_biases_online_reputation_survey.pdf`
5. `E1_pramono_explainable_absa_shap_lime.pdf`
6. `E2_you_multitask_plm_absa_hospitality.pdf`
7. `E3_guidotti_llm_tourism_review_analysis.pdf`
8. `E4_hu_sentiment_rating_inconsistency_beppu.pdf`
9. `E6_zhu_danet_multimodal_absa.pdf`

**B. Truy cập mở — tải bằng trình duyệt thật (9 bài).** `curl` và Chromium headless đều bị chặn 403; đây là chặn bot của Wiley/SAGE/Elsevier, **không phải paywall**.

> **Cập nhật sau khi tải (2026-09-23):** 7/9 đã tải và xếp vào cụm — Li (SAGE Open) · Zhang · Das · Tengilimoglu · Leo · Hwang · Biasetton. **Còn 2 bài: #8 C3 Liu et al. và #9 D5 Slevitch.**

1. **A3/D4 — Li, Lee & Kim (2025), SAGE Open**
   - Tải: <https://journals.sagepub.com/doi/pdf/10.1177/21582440251335169>
   - Lưu: `refs/04_mechanism/2025_li_bertopic_three_factor_prca.pdf`
2. **A4 — Zhang et al. (2025), Building and Environment**
   - Tải: <https://doi.org/10.1016/j.buildenv.2025.113135>
   - Lưu: `refs/04_mechanism/2025_zhang_indoor_environment_ratings.pdf`
3. **B1 — Das et al. (2026), Journal of Business Research** *(meta-analysis mức I)*
   - Tải: <https://doi.org/10.1016/j.jbusres.2025.115752>
   - Hoặc bản repository Griffith: <https://hdl.handle.net/10072/440334>
   - Lưu: `refs/05_boundary_conditions/2026_das_online_failure_recovery_meta.pdf`
4. **B2 — Tengilimoglu & Öztürk (2024), Int. J. Tourism Research**
   - Tải: <https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/jtr.2673>
   - Lưu: `refs/05_boundary_conditions/2024_tengilimoglu_ewom_recovery_severity.pdf`
5. **B3 — Leo et al. (2026), IJHM**
   - Tải: <https://doi.org/10.1016/j.ijhm.2026.104809>
   - Lưu: `refs/05_boundary_conditions/2026_leo_participation_recovery_severity.pdf`
6. **B4 — Hwang (2024), Int. J. Tourism Research**
   - Tải: <https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/jtr.2742>
   - Lưu: `refs/05_boundary_conditions/2024_hwang_double_deviation_ota.pdf`
7. **C1 — Biasetton et al. (2026), Applied Stochastic Models in Business and Industry** *(lân cận gần niche nhất)*
   - Tải: <https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/asmb.70090>
   - Hoặc bản repository Padova: <https://hdl.handle.net/11379/646585>
   - Lưu: `refs/03_phenomenon/2026_biasetton_ratings_reflect_sentiment.pdf`
8. **C3 — Liu, Ma & Dou (2025), Information Processing & Management**
   - Tải: <https://doi.org/10.1016/j.ipm.2025.104088>
   - Lưu: `refs/03_phenomenon/2025_liu_rating_inconsistency_airline.pdf`
9. **D5 — Slevitch (2024), J. Hospitality & Tourism Research**
   - Tải: <https://journals.sagepub.com/doi/pdf/10.1177/10963480241230957?download=true>
   - Lưu: `refs/06_counter_evidence/2024_slevitch_kano_categorization_critique.pdf`

**C. Đóng thật — cần thư viện trường hoặc nhờ giảng viên (8 bài).** OpenAlex xác nhận `is_oa = false`; xếp theo mức cần.

1. **D1 — Han & Anderson (2025), Cornell Hospitality Quarterly** — `10.1177/19389655251327536`
   Đòn phản biện mạnh nhất: thiên lệch đo lường dương trên TripAdvisor. **Ưu tiên số 1.**
2. **A2 — Park et al. (2025), IJCHM** — `10.1108/IJCHM-12-2023-1914`
   Impact Asymmetry Analysis trên 88.309 review.
3. **D2 — Kirilenko et al. (2024), IJHM** — `10.1016/j.ijhm.2023.103647`
   Bất nhất phụ thuộc nền tảng; chặn mọi khái quát ra ngoài TripAdvisor.
4. **A5 — Cui et al. (2025), JHTM** — `10.1016/j.jhtm.2025.01.002`
   AIPA + PRCA, chỉ số penalty vượt reward.
5. **C4 — Kovács (2025), Computers in Human Behavior** — `10.1016/j.chb.2024.108550`
   Consistency nội tại text–sao theo mức construal.
6. **B6 — Tan & Zou (2024), JQAH&T** — `10.1080/1528008X.2024.2410214`
   Recovery đo từ chính văn bản review.
7. **D6 — Mellinas et al. (2025), Tourism and Hospitality Research** — `10.1177/14673584251384011`
   Thuật toán nền tảng tách điểm khỏi văn bản. **Có bản repository, thử trước khi nhờ:** <https://hdl.handle.net/10459.1/469937> (file `tohore_a2025.pdf`, 410 KB).
8. **E5 — Kumar et al. (2024), Wireless Personal Communications** — `10.1007/s11277-024-11457-w`
   Baseline dự báo điểm; venue lệch domain nên ưu tiên thấp nhất.

Tổng kiểm chứng: **9 + 9 + 8 = 26**.

**Ba bài trọng yếu để quyết việc đóng khảo sát:** B1 và C1 hoá ra **truy cập mở** — chỉ cần trình duyệt, không cần thư viện. Trong ba bài, chỉ **D1** thật sự phải nhờ thầy.
### 7.3. Đề xuất phân loại cụm

Đây là quyết định của nhóm, không phải của agent. Đề xuất:

| Cụm đề xuất | Nguồn |
| --- | --- |
| **Mới: `severity-recovery/`** | B1–B6 + Huang & Lo (đang ở `forgiveness/`) |
| **Mới: `method-critique/`** | D5 Slevitch · D3 Sterner · D1 Han & Anderson |
| **Mở rộng `asymmetric-compensation/`** | A1, A2, A4, A5, D4/A3, E1, E2 |
| **Mở rộng `inconsistency/`** | C1, C2, C3, C4, D2, D6, E4 |
| **Mở rộng `supporting/`** | E3, E5, E6 |

Hai cụm mới cần thiết vì lý do trung thực: điều kiện biên và phê bình phương pháp hiện **không có chỗ đứng** trong cấu trúc cụm cũ, nên chúng bị xếp lẫn vào `forgiveness/` và `inconsistency/` — đúng cái đang làm vùng yếu trông như không tồn tại.

### 3.4. Kết quả Cluster E

5/5 DOI khớp cả Crossref và OpenAlex (containment = true, ratio 1,00); không bài nào trùng thư viện, không bài nào bị retract. Bài PACLIC không có DOI nên xác minh trực tiếp qua trang ACL Anthology: title, danh sách tác giả, số trang 131–140, PACLIC 2024, Tokyo — khớp đầy đủ.

**Cảnh báo chất lượng venue (theo hợp đồng source-verification):**

| Nguồn | Tín hiệu kiểm được | Kết luận |
| --- | --- | --- |
| E1 ETASR | `is_in_doaj = false`, `is_core = false` | Venue chưa xác lập; chỉ dùng cho kỹ thuật, không làm bằng chứng domain |
| E4 HSSC | `is_in_doaj = true`, `is_core = true`, Palgrave/Nature | Tin cậy |
| E5 Wireless Personal Communications | `is_core = true`, không trong DOAJ | Tạp chí hợp lệ nhưng **lệch domain** — hạ mức tin cậy |
| E2 PACLIC · E6 ACL Findings | ACL Anthology, gold OA | Hội nghị — theo `RDR-0003` phải gắn nhãn conference, không ngang hàng journal |

### 3.5. Kết quả Cluster D

6/6 DOI khớp cả Crossref và OpenAlex; không trùng thư viện; không bài nào bị retract. Toàn bộ nằm trong cửa sổ 36 tháng theo ngày công khai đầu tiên.

Hai điểm cần ghi lại:

- **D6** bị gắn cờ `CHECK` ở lần chạy tự động vì title thật dùng dấu nháy Unicode (`Booking.com’s`) còn chuỗi đối chiếu dùng ASCII (`Booking.com's`). Kiểm tay: title, tác giả, tạp chí, năm khớp chính xác → **VERIFIED**. Bài học: chuẩn hóa dấu câu trước khi so khớp title.
- **D2 (Kirilenko)** có `created` = 2023-12-09 (trong cửa sổ) nhưng OpenAlex ghi `publication_year` = 2023 và số tạp chí là 2024-02. Theo `RDR-0002` dùng ngày công khai đầu tiên → **hợp lệ**; ghi rõ để tra cứu sau khỏi nhầm.

### 3.6. Kết quả Cluster A

| DOI | Khớp title | Công khai lần đầu | Trong cửa sổ |
| --- | --- | --- | --- |
| 10.1007/s40558-025-00354-y | ✓ | 2026-02-26 | ✓ |
| 10.1108/IJCHM-12-2023-1914 | ✓ | 2025-01-20 | ✓ |
| 10.1177/21582440251335169 | ✓ | 2025-08-24 | ✓ (trùng D4) |
| 10.1016/j.buildenv.2025.113135 | ✓ | 2025-05-06 | ✓ |
| 10.1016/j.jhtm.2025.01.002 | ✓ | 2025-01-09 | ✓ |
| 10.1016/j.jhtm.2023.07.001 | ✓ | **2023-07-05** | **✗ — loại** |

Hai bài học bổ sung sau khi xác minh:

1. **Dấu nháy Unicode lại gây cờ giả** (A5: `tourists’` so với `tourists'`). Cùng nguyên nhân với D6. Quy trình từ giờ: chuẩn hóa `’ ‘ – —` trước khi so khớp title.
2. **Số trang do scout cung cấp có thể sai** (A5: 172–184 → thực tế 108–115). Metadata thư mục chỉ lấy từ Crossref/OpenAlex, không lấy từ báo cáo của scout.

### 3.7. Tải toàn văn Round 4

Tra OpenAlex lấy link PDF trực tiếp cho 22 nguồn đã xác minh: **10 nguồn có link tải trực tiếp**. Thử tải tự động bằng Python (user-agent trình duyệt), kết quả:

**Tải được 7/10** — đã kiểm trang đầu, khớp DOI và tạp chí:

| File | Nguồn | Trang |
| --- | --- | ---: |
| `A1_regitz_kano_quality_features_reviews.pdf` | Regitz et al. (2026), ITT | 31 |
| `D3_sterner_biases_online_reputation_survey.pdf` | Sterner (2026), ECR | 56 |
| `E1_pramono_explainable_absa_shap_lime.pdf` | Pramono et al. (2026), ETASR | 8 |
| `E2_you_multitask_plm_absa_hospitality.pdf` | You et al. (2024), PACLIC | 10 |
| `E3_guidotti_llm_tourism_review_analysis.pdf` | Guidotti et al. (2025), ITT | 35 |
| `E4_hu_sentiment_rating_inconsistency_beppu.pdf` | Hu et al. (2024), HSSC | 12 |
| `E6_zhu_danet_multimodal_absa.pdf` | Zhu et al. (2025), ACL Findings | 13 |

**Bị chặn 403 (phải tải tay bằng trình duyệt):** B2 Tengilimoglu (Wiley) · B4 Hwang (Wiley) · D5 Slevitch (SAGE).

Vị trí hiện tại: đã xếp vào cụm chức năng theo mục 8.

---

## 8. Đổi cấu trúc thư mục `refs/` theo chức năng (2026-09-23)

Thư mục trước đây trộn chủ đề (`inconsistency`, `asymmetric-compensation`, `forgiveness`) với vai trò (`root`, `supporting`, `legacy`), khiến điều kiện biên và phê bình phương pháp không có chỗ đứng và bị xếp lẫn. Đã chuyển sang sơ đồ **thuần theo chức năng**, có số thứ tự:

| Thư mục | Chức năng | File |
| --- | --- | ---: |
| `01_root/` | Bài gốc đối chuẩn | 2 |
| `02_definition/` | Định nghĩa construct & provenance | 2 |
| `03_phenomenon/` | Bằng chứng hiện tượng bất nhất | 7 |
| `04_mechanism/` | Lý thuyết & cơ chế bất đối xứng | 5 |
| `05_boundary_conditions/` | Severity, recovery, nền tảng, hạng sao | 2 |
| `06_counter_evidence/` | Phản biện & phê bình phương pháp | 1 |
| `07_baselines_methods/` | Baseline, ABSA, benchmark, giải thích | 6 |
| `08_legacy/` | Đã hạ ưu tiên | 4 |

**Ánh xạ cũ → mới:**

- `root/` → `01_root/`
- `inconsistency/` (Valdivia, Almansour) → `02_definition/`
- `inconsistency/` (còn lại) → `03_phenomenon/`
- `asymmetric-compensation/` → `04_mechanism/`
- `forgiveness/2025_huang...` → `05_boundary_conditions/`
- `forgiveness/2025_yoruk...` → `08_legacy/` (RQ3 không dùng forgiveness)
- `supporting/` + `legacy/2023_puh...` → `07_baselines_methods/`
- `legacy/` (còn lại) → `08_legacy/`
- `_round4_staging/` → phân vào cụm chức năng tương ứng

**Hệ quả:** B1 Das (meta-analysis) tải về sẽ vào `05_boundary_conditions/`, Slevitch vào `06_counter_evidence/` — hai cụm mới thay cho đề xuất `severity-recovery/` và `method-critique/` ở mục 7.3. Đường dẫn trong `refs/INDEX.md`, `AGENTS.md` và các log `0004`–`0005` đã cập nhật theo. Không file nào bị xoá.

**Cập nhật cùng ngày 2026-09-23:** `01_root/factsheet.md` đã xoá. Bản tóm tắt dẫn xuất này trùng nội dung với `full_paper.md` (phương trình 2a/2b nằm nguyên ở `full_paper.md:259-273`) và các số liệu EDA tự sinh đã có nhà khác: 1.339 span `Branding` ở `docs/logs/brainstorm/0001_root_idea.md` và `notes/glossary.md`, 394 review 5 sao có span tiêu cực ở `docs/logs/brainstorm/0001_root_idea.md` và `docs/logs/validation/0001_manual_annotation_protocol.md`, ba điểm phản biện ở mục Chi tiết của `refs/01_root/INDEX.md`. `01_root/` còn 2 tệp: PDF gốc và `full_paper.md`. Con trỏ đã trỏ về `full_paper.md` ở `AGENTS.md`, `refs/01_root/SOURCES.md`, `refs/01_root/INDEX.md`, `notes/project_overview.md`, `notes/reference_map.md`, `notes/pillar_strength.md`, log `0004` và `reports/md/project_planning.md`.

**Cập nhật cùng ngày 2026-09-23 (đợt 2) — gộp lớp thư viện:** xoá **8 tệp `INDEX.md` cấp cụm**. Chúng là bản render của `SOURCES.md` nhưng bị giữ bằng tay, và kiểm lịch sử cho thấy **chưa từng có script sinh nào trong repo** (`git log --all -- "*.py"` không ra kết quả), nên câu *"script sinh đã gỡ khỏi repo"* trong 17 tệp là sai — ba lớp đó xưa nay đều do người chép. Dữ liệu của cụm nay chỉ nằm ở `SOURCES.md`; danh mục cấp thư viện ở `refs/INDEX.md`. Cũng xoá `01_root/full_paper.md` (431 dòng) vì bản ở `01_root/md/` (610 dòng) đầy đủ hơn: có phương trình 2a/2b kèm hệ số và các bảng 3–8. Quy ước mới ghi ở `RULES.md` mục 5 và `refs/INDEX.md` mục 10: bản markdown của mỗi bài nằm ở `md/` trong cụm, trùng tên với PDF. Bản markdown đang được chuyển song song ngoài phiên agent — tại thời điểm ghi: 11/35 bài. Chuẩn hoá tên 9 PDF lệch quy ước (mã cụm `A1`, `B5`, `C2`, `D3`, `E1`, `E2`, `E3`, `E4`, `E6` đặt trước năm thay vì năm đứng đầu) đã xong 2 tệp ở `03_phenomenon`; **8 tệp còn lại hoãn** vì tiến trình chuyển markdown đang giữ tệp, đổi tên lúc này sẽ làm md lệch tên PDF — thành việc #7 và #8 ở `docs/BACKLOG.md`.

**Cập nhật cùng ngày 2026-09-23 (đợt 3):** tiến trình chuyển markdown chạy xong ngoài phiên agent — **35/35 bài có bản md trùng tên PDF**, không cụm nào lệch. Nhờ đó làm nốt việc #8: cả **9 tệp** lệch quy ước đã đổi sang năm đứng đầu (2 tệp `03_phenomenon` làm trước, 7 tệp còn lại sau khi tiến trình nhả tệp), kèm bản md và field `file:` trong `SOURCES.md`; mã cụm vẫn giữ ở field `code:`. Việc #7 và #8 đóng. Kiểm chứng sau cùng: 8 cụm khớp cả ba lớp PDF ↔ `md/` ↔ field `file:`, 74 tệp `.md` với 105 link nội bộ, 0 link hỏng.
