# RESEARCH PROPOSAL

> **Trạng thái tài liệu:** Bản nháp (draft). Các mục đánh dấu `[CHƯA CHỐT]` là phần nhóm **chưa có đủ bằng chứng để viết**, bên dưới mỗi mục nêu rõ nhóm phải làm gì để khóa lại. Danh mục tổng hợp các điểm mở nằm ở **Appendix A**.

| Research title (Tiêu đề đề tài) | **[CHƯA CHỐT]** Working title: *Aspect-Level Sentiment–Rating Discrepancy in Online Hotel Reviews: Buffering and Punitive Mechanisms* (Bất nhất cảm xúc – điểm số ở cấp khía cạnh trong review khách sạn: cơ chế tấm đệm và trừng phạt) |
| --- | --- |
| Mentor (Giảng viên hướng dẫn) | **[CHƯA CHỐT]** — điền tên giảng viên |
| Members (Thành viên, tối đa 3 sinh viên) | **[CHƯA CHỐT]** — điền họ tên + MSSV |

> **GHI CHÚ — CHƯA CHỐT (Research title):** Tên đề tài chưa được ban hành trong bất kỳ quyết định nào. Nhóm cần chốt sau khi hoàn tất validation ở Mục 5 và ban hành `RDR-0003`, vì tên gọi phụ thuộc vào việc measure cuối cùng là bản có dấu ở cấp aspect hay chỉ là ma trận phân cực.

---

## Abstract

Khách hàng diễn đạt một trải nghiệm qua hai kênh cùng lúc: văn bản tự do và điểm sao. Điểm sao thường được dùng như ground truth cho cảm xúc văn bản, ngầm giả định hai kênh nhất quán. Thực tế, một tỷ lệ đáng kể review không nhất quán: khách phàn nàn về một khía cạnh cụ thể mà vẫn cho điểm tối đa, hoặc khen ngợi hầu hết khía cạnh mà vẫn cho điểm tối thiểu. Đây là tín hiệu hành vi, không phải nhiễu nhãn.

Đề tài có bốn mục tiêu: (1) tạo aspect-level evaluation benchmark có aligned controls, do hai người gán nhãn độc lập; (2) lượng hóa độ bất nhất giữ đồng thời magnitude và direction, so sánh ba formulation (ma trận phân cực có hướng, khoảng cách chuẩn hóa có dấu $z(r)-z(s)$, khoảng cách cấp khía cạnh có dấu); (3) xác định khía cạnh nào khách tha thứ và khía cạnh nào dẫn tới trừng phạt; (4) kiểm định vai trò **tấm đệm** (buffering) của tín hiệu dịch vụ tích cực trước lỗi cơ sở vật chất — quan hệ mà lý thuyết hospitality dự đoán nhưng chưa kiểm định trên điểm số quan sát được.

Kết quả dự kiến: evaluation benchmark tái lập được, pipeline đo lường được tài liệu hóa, mô hình kinh tế lượng về hành vi chấm điểm dưới điều kiện bất nhất, và bằng chứng tách biệt hai cơ chế buffering và punitive ở cấp khía cạnh.

*(≈250 từ — cần rút gọn hoặc điều chỉnh sau khi chốt RQ và measure cuối.)*

> **GHI CHÚ — CHƯA CHỐT (Abstract):** Bản tóm tắt đã phản ánh đúng gap và hướng phương pháp đã xác lập, nhưng **hai chi tiết phải viết lại sau**: (1) tên measure chính thức (phụ thuộc kết quả validation), và (2) cách gọi tên hai cơ chế (`buffering`/`punitive`) nếu kết luận construct validity của `Sublimation`/`Anger` là không đủ.

**Keywords (Từ khóa):** Sentiment–Rating Inconsistency, Text-Rating Review Discrepancy, Aspect-Based Sentiment Analysis, Hospitality Reviews, Customer Forgiveness, Buffering Effect.

---

## 1. Introduction

### 1.1. Literature review

**a) Dòng nghiên cứu về bất nhất giữa văn bản và điểm số.**

Bài toán này đã được định danh chính thức thành một hướng nghiên cứu độc lập: Almansour et al. (2022) đặt tên **Text-Rating Review Discrepancy (TRRD)** và cảnh báo rằng dùng điểm sao làm nhãn cảm xúc mà không kiểm định độ tương thích sẽ tạo ra **nhiễu nhãn yếu (weak-label noise)** cho mọi mô hình học có giám sát phía sau. Trên TripAdvisor, Valdivia et al. (2019) đề xuất một **chỉ số hợp nhất liên tục** giữa rating của người dùng và sentiment do máy tính toán, dạng trung bình nhân có trọng số $f(x,y)=\sqrt{x\cdot y^\beta}$ với $x,y$ đã chuẩn hóa min–max; đặc trưng của trung bình nhân là chỉ số sụp về 0 nếu một trong hai vế cực thấp, tức trừng phạt mạnh các review lệch một chiều.

Trong ngành khách sạn, Wang, P. et al. (2025) đo **tỷ lệ review bất nhất ở cấp khách sạn** theo hướng *high-rating/low-sentiment* và cho thấy nhóm này có tác động kinh doanh âm, trong khi Bigne et al. (2023) tìm thấy valence và star rating **nhìn chung ăn khớp ở mức tổng thể** trên 20.954 review TripAdvisor. Hai kết quả này không mâu thuẫn: alignment ở mức trung bình toàn tập có thể cùng tồn tại với một **minority subset bất nhất** mang ý nghĩa quản trị. Kwon et al. (2025) tách bạch hai khái niệm vốn bị gộp chung trong các nghiên cứu trước bằng cách định nghĩa **degree** (độ lớn) là $D_j=|z(rating_j)-z(sentiment_j)|$ và **direction** (chiều) là các cặp lệch có hướng cụ thể (positive text + 1–2 sao, hoặc negative text + 4–5 sao); họ cho thấy cả degree và direction đều có thể làm tăng perceived usefulness của review, qua đó khẳng định hai khái niệm này phải được đo tách biệt chứ không thể thay thế cho nhau. Về phân loại hình thái, Abaiyan et al. (2026) báo cáo **18,6% review incongruent** với **sáu directional patterns**, trong đó hai nhóm `Conservative Rater` (38,4%) và `Obligatory 5-Star` (28,3%) chiếm tới 66,7% tổng số mismatch — tức bất nhất có cấu trúc chứ không ngẫu nhiên. Ở cấp khía cạnh, SentimentLens (Jayakody et al., 2026) định nghĩa conflict set $C=\{(h,a):|R_{norm}-S_a|>\tau\}$; đây là operationalization gần bài toán của đề tài nhất nhưng dùng trị tuyệt đối nên **mất direction**, và bài báo không báo cáo đủ quy trình chọn ngưỡng $\tau$ để tái lập. Wang, D. et al. (2025) phân biệt `review inconsistency` và `rating inconsistency` như hai hiện tượng khác nhau cần đo riêng.

Ngoài hospitality, Kwon et al. (2025) và Wang, P. et al. (2025) tập trung vào **phản ứng của người đọc** trước review bất nhất qua Curiosity Theory, Heuristic–Systematic Model và Schema Incongruity: tín hiệu mâu thuẫn kích hoạt xử lý nhận thức sâu hơn và làm tăng perceived helpfulness. Nhóm lý thuyết này giải thích hậu quả ở phía người đọc chứ không giải thích tại sao người viết chọn mức sao.

**b) Dòng nghiên cứu ABSA và dự đoán điểm cho review khách sạn.**

Ameur et al. (2024) hệ thống hóa toàn bộ pipeline xử lý review khách sạn (tiền xử lý, biểu diễn, mức phân tích, mô hình, bộ dữ liệu), cung cấp bản đồ phương pháp để lựa chọn kiến trúc có căn cứ thay vì chạy theo độ mới. Về bộ dữ liệu và benchmark, HOSSemEval-EB23 (Doan et al., 2025) cung cấp điểm quy chiếu F1 cho bài toán aspect-level sentiment trong miền hospitality. Öztürk (2026) khai phá **high-utility aspect rules** theo từng mức rating trên 11.275 review TripAdvisor của 14 khách sạn 5 sao, mô tả trực tiếp các mẫu **bù trừ đa khía cạnh**: rating thấp gắn với đồng xuất hiện của các khía cạnh tiêu cực, rating trung bình gắn với bù trừ, rating cao gắn với nhiều khía cạnh tích cực. Ở hướng dự đoán điểm, Puh & Bagić Babac (2023) và Topçu et al. (2026) dùng văn bản để dự đoán rating; điểm quan trọng là **rating ở đây là nhãn giám sát**, nên các mô hình này không thể đồng thời được dùng làm sentiment estimator độc lập.

**c) Dòng nghiên cứu tha thứ, công bằng và hiệu ứng tấm đệm.**

Yoruk et al. (2025) tổng hợp 89 nghiên cứu về customer forgiveness và xác lập đây là một cấu trúc tâm lý đã trưởng thành. Kumar & Shankar (2024) nối S-O-R, Justice Theory, forgiveness với ý định quay lại trong bối cảnh OTA. Honora et al. (2024) chỉ ra perceived justice là cơ chế đệm giữa **failure severity** và forgiveness. Huang & Lo (2025) so sánh con người và robot cung cấp dịch vụ, chứng minh forgiveness và service-recovery expectation là **serial mediators** của dissatisfaction, và phân biệt hai loại lỗi: **process failure** (cách thức cung cấp dịch vụ) dễ được tha thứ hơn **outcome failure** (không đáp ứng nhu cầu cốt lõi). Wei et al. (2025) cho thấy fairness làm tăng empathy, risk làm giảm empathy, empathy dẫn tới forgiveness, và **negative emotional contagion** làm yếu liên kết empathy → forgiveness.

**d) Bài báo nền tảng của nhóm.**

Le et al. (2026) áp dụng khung **S-O-R** trên hơn 1,3 triệu review tiếng Anh (Booking.com và TripAdvisor tại Việt Nam) với pipeline **BERTopic → SentenceBERT + c-TF-IDF → VADER → Weighted Multinomial Logistic Regression (WMLR)** để phân năm khía cạnh (`Facility`, `Amenity`, `Service`, `Experience Value`, `Loyalty`) và giải thích biến nhị phân `CoRe` (Rating ≥ 4 sao). Kết quả đạt McFadden pseudo $R^2$ = 0,4617 (Booking) và 0,5898 (TripAdvisor). Ba quy luật đáng chú ý: (i) biến `Loyalty` có hệ số tuyệt đối lớn nhất ($2{,}7410$ trên Booking; $-2{,}0086$ trên TripAdvisor); (ii) `FacilityNegative` bị phạt nặng thứ hai ($-1{,}0778$ và $-1{,}1661$), đóng vai trò **hygiene factor**; (iii) **negativity bias** — cảm xúc tiêu cực phạt điểm nặng hơn cảm xúc tích cực kéo điểm lên ở mọi khía cạnh, và trên TripAdvisor các biến **neutral** ở `Service`, `Experience`, `Facility` đều mang hệ số âm và có ý nghĩa thống kê.

**đ) Ứng dụng của các nghiên cứu này trên thực tế.**

Các kết quả trên đã đi vào vận hành: đo tỷ lệ review bất nhất ở cấp khách sạn được dùng như một chỉ báo rủi ro danh tiếng (Wang, P. et al., 2025); aspect-sentiment rules được dùng để giải thích, ở mức diễn giải được cho quản lý, vì sao một khách sạn bị kéo điểm (Öztürk, 2026); chỉ số hợp nhất giữa rating và sentiment được dùng để phát hiện review không đáng tin (Valdivia et al., 2019); và cơ chế justice–forgiveness được dùng để thiết kế quy trình service recovery (Kumar & Shankar, 2024; Honora et al., 2024; Huang & Lo, 2025). Trong bối cảnh Việt Nam — nơi Le et al. (2026) lấy toàn bộ dữ liệu — các phát hiện này chưa được chuyển thành công cụ đánh giá nào ở cấp khía cạnh.

### 1.2. The limitation of current works

**L1 — Bỏ qua hiện tượng bất nhất, hoặc xử lý nó như nhiễu.** Mô hình của Le et al. (2026) giả định quan hệ đơn điệu giữa cảm xúc khía cạnh và điểm số: tích cực thì điểm tăng, tiêu cực thì điểm giảm. Giả định này không giải thích được các quan sát có thật trong chính tập dữ liệu gán nhãn của bài báo: các review 5 sao vẫn chứa span tiêu cực. Khảo sát trực tiếp của nhóm trên `data/TripAdvisor_EN.json` (9.990 review gán nhãn) cho thấy **404 review 5 sao có chứa ít nhất một span cảm xúc `Negative`**, trong khi tổng số review 1–2 sao của toàn tập chỉ là 465 và trong đó **199 review vẫn chứa span `Positive`**. Đây là hiện tượng có cấu trúc, không phải nhiễu ngẫu nhiên: Abaiyan et al. (2026) đã chỉ ra 66,7% mismatch tập trung vào hai nhóm rater có hành vi hệ thống.

**L2 — Lập luận vòng ở biến `Loyalty`.** Biến `Loyalty` trong Le et al. (2026) được định nghĩa bằng chính các từ ngữ chỉ ý định hành vi (*"come back"*, *"highly recommend"* so với *"stay away"*, *"never again"*), rồi được đưa vào hồi quy để giải thích cho điểm số. Diễn đạt bằng lời và hành vi chấm điểm trong cùng một review là **hai biểu hiện đồng thời của một trạng thái cảm xúc**, nên việc dùng vế lời để giải thích vế số là lặp thừa, không mang giá trị nhân quả. Hệ quả thực nghiệm là biến "mạnh nhất" trong mô hình lại là biến gần như đồng nhất với biến phụ thuộc.

**L3 — Gộp chung hai trục khác bản thể (aspect và emotion).** Việc đặt `Loyalty` ngang hàng với `Facility`, `Amenity`, `Service`, `Experience Value` trộn hai phạm trù: **aspect** là khách nói về *cái gì*, còn **cảm xúc / cường độ** là khách cảm thấy *như thế nào*. Các phát ngôn cực đoan như *"definitely return"* hay *"never again"* thuộc trục thứ hai. Cách xử lý đúng là tách hai trục, không phải đổi tên aspect.

**L4 — Các phép đo hiện có làm mất chiều.** Các operationalization đã công bố đều đánh rơi một nửa tín hiệu: SentimentLens (Jayakody et al., 2026) dùng trị tuyệt đối $|R_{norm}-S_a|$ nên không phân biệt khách **cho thêm điểm** với khách **dìm điểm**; Kwon et al. (2025) tách được degree và direction nhưng trên dữ liệu sản phẩm Amazon, không phải hospitality và không ở cấp khía cạnh; Wang, P. et al. (2025) và Abaiyan et al. (2026) giữ direction nhưng chỉ ở cấp phân loại rời rạc, làm mất cường độ. **Chưa có phép đo nào đồng thời giữ magnitude và direction ở cấp khía cạnh dịch vụ trên dữ liệu khách sạn.**

**L5 — Chưa có đường kiểm định trực tiếp từ cơ chế tâm lý đến hành vi chấm sao.** Toàn bộ dòng forgiveness/justice dừng lại ở biến kết cục là forgiveness, repatronage, service-recovery expectation hoặc dissatisfaction, đo bằng bảng hỏi. **Chưa có nghiên cứu nào kiểm định đường `Forgiveness/Anger → observed star rating` trên dữ liệu review khách sạn.** Hệ quả là không thể suy diễn các kết quả này cho hành vi chấm điểm, và cũng không thể dùng lý thuyết của người đọc (HSM, Schema Incongruity, Curiosity Theory) để giải thích động cơ của người viết, vì đây là hai actor khác nhau.

**L6 — Mixed review chưa được phân biệt với bất nhất thật.** Positive và negative aspect có thể đồng tồn tại và bù trừ nhau (Bigne et al., 2023; Öztürk, 2026). Vì vậy một review 5 sao chứa span tiêu cực **chỉ là candidate inconsistency**, chưa phải bất nhất đã xác nhận; phải phân biệt lỗi thật, phàn nàn nhỏ đã được service recovery, mixed experience, negation/sarcasm và lỗi gán nhãn.

**L7 — Chất lượng bằng chứng và tính tái lập của một số nguồn chưa đủ.** Hai nguồn trực tiếp nhất cho directional typology và aspect conflict (Abaiyan et al., 2026; Jayakody et al., 2026) mới là preprint, chưa qua peer review. Chi tiết đo lường của Wang, D. et al. (2025) chưa lấy được từ full text do paywall. Do khác biệt về label space, cách chia tập và nhiệm vụ, **không nên so sánh trực tiếp accuracy/F1 giữa các bài báo**.

### 1.3. The necessity of the research

**Vấn đề đề tài tập trung giải quyết:** xây dựng một phép đo bất nhất cảm xúc – điểm số **ở cấp khía cạnh dịch vụ, giữ đồng thời độ lớn và chiều**, rồi dùng phép đo đó để kiểm định trực tiếp trên dữ liệu review khách sạn xem cơ chế nào đang vận hành: khía cạnh dịch vụ tích cực có đóng vai trò **tấm đệm** bảo vệ điểm số trước lỗi cơ sở vật chất hay không, và lỗi ở khía cạnh nào dẫn tới **trừng phạt** điểm số.

**Tính mới về phương pháp:** phép đo đề xuất giữ dấu ở cấp aspect — $D_{i,a}^{signed}=r_i^*-s_{i,a}^*$ — kết hợp hai đặc tính chưa từng xuất hiện cùng nhau trong văn hiến: độ chi tiết cấp khía cạnh (như SentimentLens) và việc bảo toàn chiều (như Kwon et al.). Đây là đề xuất của dự án, **không được mô tả như một công thức chuẩn đã có trong literature**.

**Tính mới về bằng chứng:** đóng góp trực tiếp cho lỗ hổng L5 bằng cách kiểm định quan hệ giữa cơ chế tha thứ/trừng phạt và **điểm số quan sát được**, thay vì biến kết cục tự khai trong bảng hỏi.

**Tính mới so với bài báo gốc:** khắc phục lỗi lập luận vòng của biến `Loyalty` (L2) bằng cách chuyển trọng tâm giải thích sang bất nhất ở cấp khía cạnh, đồng thời không dùng lại rating làm nhãn cảm xúc.

**Tính thời sự:** khối lượng review trực tuyến tiếp tục tăng nhanh, và chính Almansour et al. (2022) cảnh báo rằng dùng rating làm nhãn sentiment là thực hành phổ biến nhưng chưa được kiểm định — nghĩa là nhiều mô hình đang được huấn luyện trên nhãn yếu ở quy mô lớn. Về mặt quản trị, hiểu được khía cạnh nào khách sẵn sàng bỏ qua và khía cạnh nào dẫn tới trừng phạt cho phép khách sạn phân bổ nguồn lực đúng chỗ thay vì đầu tư dàn trải.

---

## 2. Research objectives

1. **Xây dựng tập đánh giá có đối chứng ở cấp khía cạnh.** Từ corpus TripAdvisor đã gán nhãn của dự án, tạo một evaluation set gồm: các review 5 sao chứa span tiêu cực, tập đối chiếu 1–2 sao chứa span tích cực, và **aligned controls** ở cả hai phía rating (review nói sao chấm vậy) để đo được **false-positive rate** của mọi phép đo.
2. **Gắn nhãn người và thiết lập ground truth có độ tin cậy.** Hai người gán nhãn độc lập trên một calibration subset, đo mức đồng thuận giữa người gán nhãn (inter-rater agreement) và giải quyết bất đồng trước khi mở rộng ra toàn bộ tập.
3. **So sánh và chọn phép đo bất nhất.** Đối chiếu tối thiểu ba formulation — ma trận phân cực có hướng 3×3, khoảng cách chuẩn hóa có dấu $z(r)-z(s)$, và khoảng cách cấp khía cạnh có dấu $r^*-s_a^*$ — theo các tiêu chí: khớp với nhãn người, giữ được dấu, ổn định trên cả hai phía rating, và không rò rỉ dữ liệu.
4. **Giải thích hành vi chấm điểm bằng biến điều tiết.** Xác định khía cạnh nào khách tha thứ nhiều nhất và khía cạnh nào dẫn tới trừng phạt, đồng thời kiểm định xem tín hiệu `Service` tích cực có vai trò **tấm đệm** đối với lỗi `Facility` hay không.

> **GHI CHÚ — CHƯA CHỐT (Research objectives):** Bốn mục tiêu trên nhất quán với gap đã định vị ở `RDR-0001` mục 2.1.4 và với đầu ra validation ở `0004_synthesis_and_next_step.md` (Gate D). Còn phải làm: **diễn đạt lại thành RQ1–RQ4 chính thức** và đối chiếu với giảng viên hướng dẫn trước khi coi là chốt.

---

## 3. Research scope

**Đối tượng dữ liệu:** review khách sạn **tiếng Anh** trên TripAdvisor, kế thừa tập gán nhãn chuyên gia của Le et al. (2026) tại `data/TripAdvisor_EN.json`.

**Đặc tả kỹ thuật của dữ liệu đang dùng** (đã xác minh trực tiếp trên file):

| Thuộc tính | Giá trị |
| --- | --- |
| Số review gán nhãn | 9.990 |
| Thang điểm | 1–5 |
| Phân bố điểm | 1 sao: 228 · 2 sao: 237 · 3 sao: 601 · 4 sao: 1.776 · 5 sao: 7.148 |
| Tổng số span gán nhãn khía cạnh | 54.326 |
| Phân bố khía cạnh | Service 19.289 · Facility 12.641 · Experience 9.113 · Amenity 7.651 · Loyalty 4.293 · Branding 1.339 |
| Tổng số span gán nhãn cảm xúc | 54.272 (Positive 46.772 · Negative 4.508 · Neutral 2.992) |
| Review 5 sao chứa ≥1 span `Negative` | 404 review |
| Review 1–2 sao chứa ≥1 span `Positive` | 199 review (trên tổng 465 review 1–2 sao) |
| Aligned control 5 sao (không có span `Negative`) | 6.744 review |
| Aligned control 1–2 sao (không có span `Positive`) | 266 review |

**Nội dung nghiên cứu chính (in-scope):**
- Khai phá khía cạnh và cảm xúc cấp khía cạnh trên review khách sạn tiếng Anh.
- Lượng hóa độ lệch giữa nội dung văn bản và điểm sao, giữ cả magnitude và direction, ở cấp khía cạnh.
- Kiểm định thống kê vai trò điều tiết của khía cạnh dịch vụ lên quan hệ giữa lỗi ở khía cạnh khác và điểm số.

**Ngoài phạm vi (out-of-scope):**
- Xây dựng ứng dụng đặt phòng hoặc hệ thống frontend/backend cho người dùng cuối.
- Xử lý đa ngôn ngữ ngoài tiếng Anh trong giai đoạn này.
- Thu thập dữ liệu thời gian thực (live scraping); tập dữ liệu tĩnh hiện có đã đủ lớn cho mục tiêu nghiên cứu.
- Kiểm định trên Booking.com trong giai đoạn này.

> **GHI CHÚ — CHƯA CHỐT (Research scope):** Cần chốt **hai ranh giới** trước khi khóa scope: (1) tập `data/TripAdvisor_EN.json` là tập con gán nhãn của dự án hay mở rộng lên corpus TripAdvisor đầy đủ của bài gốc (782.584 review) — điều này quyết định mọi tuyên bố về prevalence; (2) tên khía cạnh dùng thống nhất (`Experience` hay `Experience Value`) để khớp giữa văn bản và code.

---

## 4. Feasibility of research

**Dữ liệu đã có sẵn và đã được xác minh.** Corpus review khách sạn tiếng Anh với nhãn khía cạnh và cảm xúc cấp span đã nằm trong repo (`data/TripAdvisor_EN.json`), không phải chờ thu thập. Các con số thống kê ở Mục 3 được tính trực tiếp trên file này.

**Tài liệu nền đã đủ để thiết kế thực nghiệm.** 15 bài báo hạt nhân đã được khảo sát và phân loại theo ba cụm (inconsistency, hospitality ABSA, forgiveness/buffering) trong `refs/INDEX.md`, kèm bản PDF cục bộ cho các nguồn quan trọng nhất về mặt công thức, nên không phụ thuộc paywall cho phần cốt lõi (công thức unified index của Valdivia et al. đã được trích trực tiếp từ full text).

**Baseline đối chứng đã xác lập.** Pipeline `BERTopic + VADER + WMLR` của bài báo gốc là baseline tái lập được, có tham số và kết quả công bố (Mục 1.1d). HOSSemEval-EB23/TAS-BERT cung cấp điểm quy chiếu cho chất lượng ABSA.

**Nguồn lực tính toán.** Toàn bộ pipeline dự kiến chạy được trên máy tính cá nhân thông thường: VADER là phương pháp dựa trên từ điển, BERTopic và các mô hình transformer ở kích thước base chạy được trên CPU hoặc GPU phổ thông. Không cần phần cứng chuyên dụng.

**Rủi ro đã nhận diện và cách chặn:**
- *Mất cân bằng giữa hai chiều bất nhất* (404 review 5 sao có span tiêu cực so với 199 review 1–2 sao có span tích cực, trong khi tổng thể chỉ có 465 review 1–2 sao). Cách chặn: **báo cáo đúng prevalence thực tế, không cân bằng nhân tạo**; nếu tập mirror không đủ để kết luận, tuyên bố giới hạn rõ ràng thay vì suy diễn.
- *Chất lượng nhãn cảm xúc tự động.* Cách chặn: không dùng rating để huấn luyện sentiment estimator, và đo hiệu năng estimator bằng tập người gán nhãn độc lập.
- *Rò rỉ dữ liệu (data leakage) từ span `Branding`.* Trong dữ liệu tồn tại 1.339 span `Branding` — khách tự nói thẳng số sao bằng lời (*"give 5 star"*) hoặc so sánh ảnh quảng cáo với thực tế. Các span này **phải bị loại** khỏi mọi đặc trưng dự đoán.

> **GHI CHÚ — CHƯA CHỐT (Feasibility of research):** Cần bổ sung **hai mục trước khi nộp**: (1) khai báo nguồn gốc và điều kiện sử dụng dữ liệu (tập gán nhãn lấy từ repo của nhóm tác giả bài báo gốc) và cách ghi nguồn dữ liệu trong báo cáo; (2) xác nhận phân công nhân sự theo mục tiêu ở Mục 2 để lập luận khả thi về tiến độ.

---

## 5. Approach and Method

Đề tài theo cách tiếp cận **kết hợp định lượng**: một tầng NLP để chuyển văn bản thành tín hiệu cảm xúc cấp khía cạnh, một tầng đo lường để lượng hóa độ lệch giữa tín hiệu đó và điểm sao, và một tầng kinh tế lượng để kiểm định quan hệ giữa khía cạnh, độ lệch và điểm số.

### Stage 1 — Exploratory data analysis

Chạy notebook khám phá `data/TripAdvisor_EN.json`: phân bố điểm, phân bố độ dài review, phân bố nhãn khía cạnh và cảm xúc, và kiểm tra tính toàn vẹn của liên kết giữa span khía cạnh và span cảm xúc. Đầu ra là bảng đặc tả dữ liệu và danh sách các trường hợp cần loại trừ.

### Stage 2 — Building the controlled evaluation set

Ba thành phần: (a) review 5 sao chứa span tiêu cực; (b) tập đối chiếu review 1–2 sao chứa span tích cực; (c) **aligned controls** lấy từ cả hai phía rating. Nhóm đối chứng là bắt buộc, vì nếu tập kiểm thử chỉ gồm các mẫu nghi ngờ thì một phép đo quá nhạy vẫn đạt độ chính xác cao trên tập đó nhưng sẽ **báo động giả** liên tục khi gặp review bình thường. Quy trình và các cột nhãn chi tiết đã được ghi tại [`docs/logs/validation/0001_manual_annotation_protocol.md`](../../docs/logs/validation/0001_manual_annotation_protocol.md).

### Stage 3 — Human annotation and ground truth

Hai người gán nhãn độc lập theo 5 trường: loại tương thích, khía cạnh gây lệch, mức độ nghiêm trọng, có/không service recovery, và có/không negation hoặc sarcasm. Quy trình ba bước: gán nhãn thử độc lập một calibration subset → đo mức đồng thuận (Cohen's Kappa, ngưỡng mục tiêu $\ge 0{,}70$) → họp giải quyết bất đồng và thống nhất quy chuẩn → mở rộng ra toàn bộ tập, các dòng bất đồng được chốt nhãn cuối qua đối soát (adjudication).

### Stage 4 — Comparing discrepancy formulations

Ba candidate được đối chiếu song song trên cùng ground truth:

| Candidate | Đầu ra | Vai trò |
| --- | --- | --- |
| Ma trận phân cực có hướng 3×3 | Class | Baseline dễ diễn giải nhất |
| Khoảng cách chuẩn hóa có dấu $z(r)-z(s)$ | Dấu + magnitude | Kiểm tra khả năng mở rộng từ Kwon et al. (2025) |
| Khoảng cách cấp khía cạnh có dấu $r^*-s_a^*$ | Vector theo khía cạnh + tổng hợp | Candidate measure chính của đề tài |

Phần dư hồi quy $rating - \widehat{rating}_{\text{text}}$ chỉ dùng như **sensitivity analysis**, không dùng làm measure chính. Embedding distance và entropy chưa triển khai trừ khi ba formulation trên thất bại.

**Tiêu chí chọn measure chính** (phải đạt đồng thời): khớp tốt nhất với nhãn hướng do người gán, báo cáo **macro-F1 và confusion matrix** thay vì accuracy đơn lẻ; giữ được dấu và phân biệt hai hướng bất nhất; ổn định trên cả hai stratum rating cao và thấp; giải thích được ở cấp khía cạnh; và không dùng rating để huấn luyện sentiment estimator, không phụ thuộc span `Branding` hoặc các câu nói thẳng số sao.

### Stage 5 — Modeling rating behavior

Dùng điểm bất nhất đã chọn làm biến phụ thuộc hoặc biến trung gian trong mô hình kinh tế lượng để kiểm định vai trò điều tiết của khía cạnh dịch vụ, kế thừa cách tiếp cận hồi quy của bài báo gốc để bảo đảm so sánh được với baseline.

> **GHI CHÚ — CHƯA CHỐT (Approach and Method):** Đây là mục còn mở nhiều nhất. Nhóm phải chốt **năm quyết định kỹ thuật** trước khi viết bản cuối:
> 1. **Sentiment estimator** dùng để sinh tín hiệu cảm xúc cấp khía cạnh (lexicon-based, fine-tune transformer, hay LLM) — tiêu chí: phải độc lập với rating và đo được trên tập người gán nhãn.
> 2. **Chuẩn hóa rating–sentiment** (z-score, min–max, hay calibrated probability) — ảnh hưởng trực tiếp đến $r^*$ và $s_a^*$.
> 3. **Ngưỡng** phân biệt `aligned` / `mixed` / bất nhất thật — hiện chưa có cơ sở tái lập từ văn hiến.
> 4. **Cách tổng hợp sentiment nhiều khía cạnh** thành kỳ vọng cấp document.
> 5. **Construct validity của `Sublimation`/`Anger`** — văn hiến hiện hỗ trợ các cấu trúc `forgiveness`, `empathy`, `negative emotion`, `compensatory behavior` gần hơn hai nhãn này; nếu không chứng minh được, phải hạ xuống thành working label và gọi tên cơ chế là buffering/punitive.
>
> Cách khóa: chạy đúng validation ở Stage 3–4 rồi ban hành `RDR-0003`. Nếu không formulation nào đạt tiêu chí, giữ ma trận phân cực có hướng làm baseline, **không ban hành** `RDR-0003`, và chỉ mở khảo sát theo citation chain nhắm đúng thất bại đã quan sát. Sơ đồ kiến trúc pipeline sẽ được vẽ sau khi năm điểm trên được chốt.

---

## 6. Research plan

*(Để trống theo yêu cầu — sẽ điền sau khi chốt phân công nhân sự và mốc thời gian.)*

---

## Computational Resource Requirements

Một máy tính cá nhân thông thường (hoặc hai máy, vì có hai người gán nhãn độc lập) với môi trường Python và Jupyter Notebook; bảng tính Excel/Google Sheets cho công đoạn gán nhãn. Không cần GPU chuyên dụng, không cần máy chủ, không cần chi phí thuê API bắt buộc.

> **GHI CHÚ — CHƯA CHỐT:** Nếu Stage 5 chọn estimator là fine-tune transformer, cần ghi rõ yêu cầu GPU (hoặc phương án chạy CPU/Colab). Quyết định này phụ thuộc điểm 1 ở phần ghi chú của Mục 5.

---

## 7. Expected results

1. **Evaluation benchmark có đối chứng.** Một tập review khách sạn được gán nhãn độc lập bởi hai người, kèm báo cáo mức đồng thuận giữa người gán nhãn và nhãn cuối đã đối soát, bao gồm nhóm aligned controls để đo false-positive rate. Đây là sản phẩm dữ liệu có thể tái sử dụng cho các nghiên cứu sau.
2. **Pipeline đo lường độ bất nhất.** Quy trình xử lý từ review thô đến điểm bất nhất cấp khía cạnh, kèm so sánh định lượng giữa ba formulation và lý do chọn measure chính.
3. **Bằng chứng thực nghiệm về cơ chế buffering và punitive.** Kết quả cho biết khía cạnh nào được tha thứ nhiều nhất, khía cạnh nào dẫn tới trừng phạt, và liệu tín hiệu dịch vụ tích cực có thực sự đệm được lỗi cơ sở vật chất khi đo trên **điểm số quan sát được** — đây là điểm mà văn hiến hiện tại chưa kiểm định.
4. **Sản phẩm bàn giao học thuật.** Thuyết minh đề cương, báo cáo kết quả hoàn chỉnh, và bộ notebook tái lập được toàn bộ thực nghiệm.

**Hàm ý lý thuyết:** mở rộng khung S-O-R từ quan hệ đơn điệu sang quan hệ có điều tiết ở cấp khía cạnh, và cung cấp một đường kiểm định trực tiếp giữa cơ chế tâm lý (tha thứ/trừng phạt) và hành vi chấm điểm quan sát được.

**Hàm ý phương pháp:** đưa ra cảnh báo thực nghiệm cụ thể cho thực hành dùng rating làm nhãn sentiment phổ biến hiện nay, và đề xuất một phép đo giữ đồng thời magnitude và direction ở cấp khía cạnh.

**Hàm ý thực tiễn:** chỉ ra cho khách sạn khía cạnh nào khách sẵn sàng bỏ qua và khía cạnh nào dẫn tới trừng phạt điểm, làm cơ sở phân bổ nguồn lực và thiết kế quy trình service recovery.

---

## References

Abaiyan, R., et al. (2026). *Fault of our stars: Behavioral drivers of rating–sentiment incongruence*. arXiv preprint. https://arxiv.org/abs/2606.25518

Almansour, A., Alotaibi, R., & Alharbi, H. (2022). Text-rating review discrepancy (TRRD): An integrative review and implications for research. *Future Business Journal, 8*, 3. https://doi.org/10.1186/s43093-022-00114-y

Ameur, A., Hamdi, S., & Ben Yahia, S. (2024). Sentiment analysis for hotel reviews: A systematic literature review. *ACM Computing Surveys, 56*(2), 1–38. https://doi.org/10.1145/3605152

Bigne, E., Ruiz, C., Perez-Cabañero, C., & Cuenca, A. (2023). Are customer star ratings and sentiments aligned? *Service Business, 17*, 281–314. https://doi.org/10.1007/s11628-023-00524-0

Doan, T. T., et al. (2025). HOSSemEval-EB23: A robust dataset for aspect-based sentiment analysis of hospitality reviews. *Multimedia Tools and Applications, 84*, 13057–13087. https://doi.org/10.1007/s11042-024-19518-9

Honora, A., Wang, K.-Y., & Chih, W.-H. (2024). The role of customer forgiveness and perceived justice in restoring relationships with customers. *Service Business, 18*, 363–393. https://doi.org/10.1007/s11628-024-00563-1

Huang, Z., & Lo, A. (2025). Human vs. robot service provider agents in service failures: Comparing customer dissatisfaction and the mediating role of forgiveness and service recovery expectation. *Information Technology & Tourism, 27*, 417–448. https://doi.org/10.1007/s40558-025-00314-6

Jayakody, D., Thenahandi, P., & Jayarathna, S. (2026). *SentimentLens: Reconciling sentiment and ratings via dual-modality in the hospitality sector*. arXiv preprint. https://arxiv.org/abs/2606.00084

Kumar, A., & Shankar, A. (2024). Why do consumers forgive online travel agencies? A multi-study approach. *Australasian Marketing Journal, 32*(4), 323–338. https://doi.org/10.1177/14413582231194071

Kwon, B., Lee, J., Min, J., Kwak, C., & Choi, H. S. (2025). Beyond the stars: The impact of rating-text inconsistency on perceived review usefulness. *Asia Pacific Journal of Information Systems, 35*(1), 49–72. https://doi.org/10.14329/apjis.2025.35.1.49

Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026). Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings. *International Journal of Hospitality Management, 134*, 104574.

McMurry, E. (2026). Quantifying social sentiment in hostels using a domain-specific transformer pipeline. In *Proceedings of WASSA 2026* (pp. 24–36). https://doi.org/10.18653/v1/2026.wassa-1.3

Öztürk, A. C. (2026). Discovering aspect–sentiment drivers of hotel review ratings with interpretable high-utility rules. *IEEE Access, 14*, 39496–39511. https://doi.org/10.1109/access.2026.3672490

Patil, P., Bacha, J., Yamani, B., Sun, S., & Kejriwal, M. (2026). *Beyond the star rating: A scalable framework for aspect-based sentiment analysis using LLMs and text classification*. arXiv preprint. https://arxiv.org/abs/2602.21082

Puh, K., & Bagić Babac, M. (2023). Predicting sentiment and rating of tourist reviews using machine learning. *Journal of Hospitality and Tourism Insights, 6*(3), 1188–1204. https://doi.org/10.1108/JHTI-02-2022-0078

Topçu, A., Asar, M. A., & Orman, G. K. (2026). Improving hotel review rating prediction with transformer models. *Sakarya University Journal of Computer and Information Sciences, 9*(2), 451–464. https://dergipark.org.tr/en/pub/saucis/article/1748175

Valdivia, A., et al. (2019). Inconsistencies on TripAdvisor reviews: A unified index between users and sentiment analysis methods. *Neurocomputing, 353*, 3–16. https://doi.org/10.1016/j.neucom.2018.09.096

Wang, D., Xia, Q., Feng, Y., & Cheng, T. C. E. (2025). Unravelling the effects of two inconsistencies on online review helpfulness: Evidence from TripAdvisor. *Decision Support Systems, 193*, 114450. https://doi.org/10.1016/j.dss.2025.114450

Wang, P., Zhang, H., Yuan, X., & Zhang, X. (2025). Beyond the stars: Unpacking the impact of score-textual inconsistency of online reviews on hotel performance. *International Journal of Hospitality Management, 130*, 104271. https://doi.org/10.1016/j.ijhm.2025.104271

Wei, J., et al. (2025). Consumer forgiveness in online travel agency service recovery: Consumer empathy and negative emotional contagion. *International Journal of Tourism Research, 27*(6). https://doi.org/10.1002/jtr.70154

Yoruk, I., Hsu, J.-H., & Lee, Z. W. Y. (2025). Consumer forgiveness: A literature review and research agenda. *Psychology & Marketing, 42*(2), 554–578. https://doi.org/10.1002/mar.22138

> **GHI CHÚ — CHƯA CHỐT (References):** Một số mục còn thiếu thông tin thư mục đầy đủ do chỉ xác minh được ở mức metadata/abstract và chưa lấy được full text: `Abaiyan et al. (2026)`, `Jayakody et al. (2026)`, `Wei et al. (2025)`, `Topçu et al. (2026)` (DOI bị cắt trong `refs/INDEX.md`), `Valdivia et al. (2019)`, `Doan et al. (2025)`. Cần bổ sung danh sách tác giả đầy đủ và số trang chính xác trước khi nộp.

---

## Appendix A — Open items checklist

| # | Vị trí | Nội dung cần chốt | Cách khóa |
| --- | --- | --- | --- |
| 1 | Tiêu đề | Tên đề tài chính thức | Ban hành `RDR-0003` sau validation |
| 2 | Phần đầu | Giảng viên hướng dẫn, thành viên, MSSV | Điền trực tiếp |
| 3 | Tóm tắt | Tên measure cuối; nhãn gọi hai cơ chế | Theo kết quả Stage 4 |
| 4 | Mục 2 | Diễn đạt chính thức RQ1–RQ4 | Chốt với giảng viên hướng dẫn |
| 5 | Mục 3 | Tập dữ liệu là subset gán nhãn hay corpus đầy đủ; tên khía cạnh thống nhất | Quyết định phạm vi + thống nhất code và tài liệu |
| 6 | Mục 3 và phần rủi ro | **Số mẫu 5 sao chứa span tiêu cực: tài liệu dự án ghi 402, tính lại trên file là 404.** Ngoài ra định nghĩa "negative span" chưa được đóng băng: nếu loại thêm span đồng thời gắn `Branding` còn 394, nếu chỉ tính span có khía cạnh lõi (loại `Loyalty`/`Branding`) còn 392 | Chốt định nghĩa "negative span" và chạy lại một lần, ghi kết quả vào log; sửa mọi tài liệu đang ghi 402 |
| 7 | Mục 4 | Nguồn gốc và điều kiện sử dụng dữ liệu | Ghi rõ nguồn trong báo cáo |
| 8 | Mục 5 | Sentiment estimator | Validation Stage 3–4 |
| 9 | Mục 5 | Chuẩn hóa rating–sentiment | Validation Stage 4 |
| 10 | Mục 5 | Ngưỡng phân loại aligned / mixed / inconsistent | Validation Stage 4 |
| 11 | Mục 5 | Tổng hợp sentiment nhiều khía cạnh | Validation Stage 4 |
| 12 | Mục 5 | Construct validity của `Sublimation` / `Anger` | Tra citation chain nhắm đúng construct |
| 13 | Mục 5 | Sơ đồ kiến trúc pipeline | Vẽ sau khi chốt #8–#12 |
| 14 | Mục 6 | Toàn bộ kế hoạch và phân công | Điền sau |
| 15 | Nguồn lực tính toán | Yêu cầu GPU (nếu chọn fine-tune transformer) | Phụ thuộc #8 |
| 16 | Tài liệu tham khảo | Bổ sung metadata đầy đủ cho 6 nguồn | Truy xuất Crossref/nhà xuất bản |

---

*Tài liệu liên quan: [`docs/INDEX.md`](../../docs/INDEX.md) · [`docs/logs/literature_survey/0004_synthesis_and_next_step.md`](../../docs/logs/literature_survey/0004_synthesis_and_next_step.md) · [`docs/logs/validation/0001_manual_annotation_protocol.md`](../../docs/logs/validation/0001_manual_annotation_protocol.md) · [`refs/INDEX.md`](../../refs/INDEX.md) · [`notes/glossary.md`](../../notes/glossary.md)*
