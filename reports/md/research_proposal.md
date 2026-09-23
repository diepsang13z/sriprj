# RESEARCH PROPOSAL / THUYẾT MINH ĐỀ CƯƠNG NGHIÊN CỨU

> **Trạng thái tài liệu:** Bản viết theo đúng cấu trúc `Class_Group_Research_Proposal_Template`. Các mục đánh dấu **[CHƯA CHỐT]** là phần nhóm phải quyết trước khi nộp bản cuối; danh mục tổng hợp nằm ở **Phụ lục A**.

| Research title | **[CHƯA CHỐT chính thức]** — Working title: *Aspect-Level Sentiment–Rating Discrepancy in Online Hotel Reviews: Asymmetric Compensation and Penalty Dominance* (Bất nhất cảm xúc – điểm số ở cấp khía cạnh trong review khách sạn: cơ chế bù trừ và cơ chế chi phối) |
| --- | --- |
| Mentor | **[CHƯA CHỐT]** — điền tên giảng viên hướng dẫn |
| Members (up to 3 students) | **[CHƯA CHỐT]** — điền họ tên + MSSV |

**Ghi chú về tiêu đề:** khung lý thuyết và RQ3 đã khóa theo `RDR-0004` và `RDR-0005`, nhưng tên gọi cuối cùng phụ thuộc công thức đo bất nhất được chọn sau validation study, nên tiêu đề chính thức chỉ nên ban hành sau bước đó.

---

## Abstract / Tóm tắt

Điểm sao thường được dùng làm nhãn cảm xúc cho review, ngầm giả định rằng văn bản và điểm số luôn nhất quán. Trong tập dữ liệu của đề tài, 404 review 5 sao vẫn chứa phàn nàn tiêu cực và 199 review 1–2 sao vẫn chứa lời khen. Đây là mẫu hành vi có cấu trúc, không phải nhiễu nhãn.

Đề tài đặt bốn mục tiêu: (1) xây dựng tập đánh giá có đối chứng ở cấp khía cạnh, gồm hai nhóm lệch có hướng và nhóm đối chứng nhất quán để đo tỷ lệ báo động giả; (2) thiết lập ground truth bằng hai người gán nhãn độc lập, đo mức đồng thuận và đối soát bất đồng; (3) đối chiếu ba công thức lượng hóa bất nhất để chọn phép đo giữ đồng thời độ lớn và chiều; (4) kiểm định cách các khía cạnh kết hợp bất đối xứng để tạo ra bất nhất, dưới các điều kiện biên là mức độ nghiêm trọng, service recovery và hạng sao khách sạn.

Phương pháp gồm ba tầng: tầng xử lý ngôn ngữ sinh tín hiệu cảm xúc cấp khía cạnh **độc lập với điểm sao**, tầng đo lường tính điểm bất nhất có dấu, và tầng kinh tế lượng kiểm định cơ chế bù trừ và cơ chế chi phối. Phạm vi dữ liệu là 9.990 review TripAdvisor giai đoạn 2015–2023. Nghiên cứu chỉ đo mẫu hành vi chấm điểm quan sát được và chủ động **không** suy diễn trạng thái tâm lý như tha thứ hay phẫn nộ từ điểm sao. Kết quả dự kiến gồm bộ dữ liệu đánh giá tái sử dụng được, pipeline đo lường có tài liệu hóa, và bằng chứng thực nghiệm về bất đối xứng ở cấp khía cạnh.

*(≈240 từ.)*

**Key words:** Sentiment–Rating Discrepancy, Aspect-Based Sentiment Analysis, Hotel Reviews, Asymmetric Compensation, Hospitality Analytics, Rating Prediction.

---

## 1. Introduction / Giới thiệu

### 1.1. Literature review / Tình hình nghiên cứu trong và ngoài nước

**a) Dòng nghiên cứu về bất nhất giữa văn bản và điểm số.**

Bài toán đã được định danh thành một hướng nghiên cứu độc lập: Almansour, Alotaibi & Alharbi (2022) đặt tên **Text-Rating Review Discrepancy (TRRD)** và cảnh báo rằng dùng điểm sao làm nhãn cảm xúc mà không kiểm định độ tương thích sẽ tạo ra **nhiễu nhãn yếu** cho mọi mô hình học có giám sát phía sau. Trên TripAdvisor, Valdivia et al. (2019) đề xuất một **chỉ số hợp nhất liên tục** giữa điểm người dùng và cảm xúc do máy tính toán, dạng trung bình nhân có trọng số $f(x,y)=\sqrt{x\cdot y^\beta}$ với $x,y$ đã chuẩn hóa min–max; đặc trưng của trung bình nhân là chỉ số sụp về 0 nếu một trong hai vế cực thấp.

Trong ngành khách sạn, Wang, P. et al. (2025) đo **tỷ lệ review bất nhất ở cấp khách sạn** theo hướng *điểm cao / cảm xúc thấp* và cho thấy nhóm này gắn với tác động kinh doanh âm, trong khi Bigné et al. (2023) tìm thấy điểm sao và cảm xúc **nhìn chung ăn khớp ở mức tổng thể** trên 20.954 review TripAdvisor, đồng thời chỉ ra rằng cảm xúc tích cực và tiêu cực ở các khía cạnh khác nhau có thể triệt tiêu lẫn nhau. Hai kết quả này không mâu thuẫn: alignment ở mức trung bình toàn tập có thể cùng tồn tại với một **nhóm thiểu số bất nhất** mang ý nghĩa quản trị. Kwon, B. et al. (2025) tách bạch hai khái niệm vốn bị gộp chung bằng cách định nghĩa **degree** là $|z(rating)-z(sentiment)|$ và **direction** là các cặp lệch có hướng (văn bản tích cực + 1–2 sao, hoặc văn bản tiêu cực + 4–5 sao), nhưng thực hiện trên dữ liệu sản phẩm và không ở cấp khía cạnh.

Các nghiên cứu gần đây bổ sung hai mảnh ghép còn thiếu nhưng chưa khép được khoảng trống: Abaiyan et al. (2026) phân loại sáu dạng bất nhất có hướng và kiểm tra độ tin cậy của điểm sao như một nhãn cảm xúc; Jayakody et al. (2026) đo khoảng cách đa phương thức **ở cấp khách sạn – khía cạnh** bằng trị tuyệt đối $|R_{norm}-S_a|$, nên vẫn mất chiều và không báo cáo đủ quy trình chọn ngưỡng để tái lập. Ở phía cấp toàn văn bản, Biasetton et al. (2026) so **điểm suy ra từ văn bản** với điểm sao và tìm thấy bất nhất mạnh nhất ở mức 2 và 4 sao; Marreira et al. (2026) phát hiện bất nhất như một phân loại nhị phân; Liu, Ma & Dou (2025) và Wang, D. et al. (2025) đều dùng bất nhất như một đại lượng tổng hợp với biến kết cục là perceived helpfulness; Kovács (2025) đo consistency bằng khoảng cách tuyệt đối ở cấp văn bản. Về mặt tỷ lệ, Hu, Pan & Wang (2024) tìm thấy **694 trong 4.004 review (17,3%)** TripAdvisor có bất nhất rõ rệt — một mốc độc lập đáng tham chiếu.

**b) Dòng nghiên cứu ABSA và dự đoán điểm cho review khách sạn.**

Ameur, Hamdi & Ben Yahia (2024) hệ thống hóa toàn bộ pipeline xử lý review khách sạn (tiền xử lý, biểu diễn, mức phân tích, mô hình, bộ dữ liệu), cung cấp bản đồ phương pháp để chọn kiến trúc có căn cứ thay vì chạy theo độ mới. Về benchmark, HOSSemEval-EB23 của Doan et al. (2025) cung cấp điểm quy chiếu cho bài toán cảm xúc cấp khía cạnh trong miền hospitality, và You et al. (2024) cung cấp mốc so kỹ thuật cụ thể bằng học đa nhiệm trên mô hình ngôn ngữ tiền huấn luyện. Öztürk (2026) khai phá **các luật khía cạnh – cảm xúc có độ hữu ích cao** theo từng mức điểm trên 11.275 review TripAdvisor của 14 khách sạn 5 sao, mô tả trực tiếp các mẫu **bù trừ đa khía cạnh**: mức điểm thấp gắn với đồng xuất hiện của nhiều khía cạnh tiêu cực, mức trung bình gắn với bù trừ, mức cao gắn với nhiều khía cạnh tích cực. Ở hướng dự đoán điểm, Puh & Bagić Babac (2023) và Topçu et al. (2026) dùng học máy và transformer; cần lưu ý Topçu et al. dùng chính điểm sao làm nhãn huấn luyện, nên **không** dùng được làm bộ ước lượng cảm xúc độc lập. Guidotti, Pandolfo & Pulina (2025) dùng LLM zero-shot để phân loại cảm xúc và trích từ khóa, đóng khung như công cụ hỗ trợ ra quyết định cho quản lý; Pramono, Gernowo & Sofwan (2026) bổ sung tầng giải thích bằng SHAP và LIME; Zhu et al. (2025) xử lý ABSA đa phương thức nhưng dữ liệu của đề tài chỉ có văn bản nên liên quan thấp.

**c) Dòng nghiên cứu về cơ chế bất đối xứng giữa các khía cạnh.**

Đây là lớp lý thuyết trung tâm của đề tài. Sharma et al. (2025) áp dụng Prospect Theory trên 416.756 review TripAdvisor của 375 khách sạn tại 14 thành phố châu Âu và cho thấy các sai lệch âm tạo tác động mạnh hơn các sai lệch dương tương đương, với **loss aversion**, **diminishing sensitivity** và vai trò của **reference point**. Li, S. et al. (2024) cung cấp cấu trúc toán học rõ nhất cho quyết định hai giai đoạn: **giai đoạn không bù trừ** xử lý các thuộc tính cơ bản trước, **giai đoạn bù trừ** mới áp dụng cho các thuộc tính còn lại. Wang, J. et al. (2024) cho thấy quan hệ giữa hiệu năng thuộc tính và satisfaction là **phi tuyến, bất đối xứng và thay đổi theo thời gian**. Kwon, W. (2026) kết hợp ABSA zero-shot với Impact-Asymmetry Analysis theo logic Kano/three-factor để tách thuộc tính thành satisfier, dissatisfier và hybrid; Regitz, Höpken & Fuchs (2026) thực hiện việc tương tự bằng hồi quy cảm xúc dương/âm theo topic và phân loại được room quality là **Must-Be** trong khi connectivity là **Attractive**; Park et al. (2025) xác nhận bất đối xứng trên 88.309 review; Zhang et al. (2025) tìm thấy thuộc tính môi trường trong nhà là Basic/penalty-dominant trên hơn 540.000 review; Cui, Zhang & Wang (2025) dùng AIPA và PRCA cho thấy thuộc tính hạ tầng nền có chỉ số penalty vượt reward. Ở chiều ngược lại, Li, J., Lee & Kim (2025) dùng BERTopic kết hợp three-factor và PRCA và tìm thấy thuộc tính lõi giữ tác động **ổn định, gần đối xứng** giữa các hạng sao — bằng chứng cho thấy bất đối xứng là **có điều kiện**, không phải quy luật toàn cục. Xu et al. (2025) và Zhong et al. (2026) cho thấy một số complaint và tín hiệu cảm giác gần gũi có mức penalty lớn đến mức các khía cạnh tích cực khác không bù được.

Về **điều kiện biên**, Das et al. (2026) tổng hợp 147 nghiên cứu với $N=82.901$ và xác lập vai trò của attribution và justice trong phục hồi dịch vụ; Tengilimoglu & Öztürk (2024) cho thấy **severity là biến điều tiết trực tiếp** — recovery hiệu quả với lỗi nhẹ và giảm mạnh khi lỗi nặng; Hwang (2024) chỉ ra **double deviation** (lỗi ban đầu cộng với recovery thất bại) tạo penalty phi tuyến; Lim, Saha & Das (2025) đặt **giới hạn trên** cho khả năng bù trừ qua service recovery paradox; Tan & Zou (2024) chứng minh recovery có thể **đo từ chính văn bản review và phản hồi của khách sạn**, không nhất thiết phải dùng bảng hỏi; Albayrak et al. (2025) và Leo et al. (2026) bổ sung vai trò của loại lỗi, tín hiệu chất lượng và mức tham gia của khách hàng.

**d) Bài báo nền tảng của nhóm.**

Le, Nguyen & Nguyen (2026) áp dụng khung **S-O-R** trên hơn 1,3 triệu review tiếng Anh (Booking.com và TripAdvisor tại Việt Nam) với pipeline **BERTopic → SentenceBERT + c-TF-IDF → VADER → Weighted Multinomial Logistic Regression** để phân năm khía cạnh (`Facility`, `Amenity`, `Service`, `Experience Value`, `Loyalty`) và giải thích biến nhị phân `CoRe` (điểm ≥ 4 sao). Kết quả đạt McFadden pseudo $R^2$ = 0,4617 (Booking) và 0,5898 (TripAdvisor). Ba quy luật đáng chú ý: (i) biến `Loyalty` có hệ số tuyệt đối lớn nhất (2,7410 trên Booking; −2,0086 trên TripAdvisor); (ii) `FacilityNegative` bị phạt nặng thứ hai (−1,0778 và −1,1661), đóng vai trò hygiene factor; (iii) có **negativity bias** — cảm xúc tiêu cực phạt điểm nặng hơn mức cảm xúc tích cực kéo điểm lên.

**đ) Ứng dụng của các nghiên cứu này trên thực tế.**

Đo tỷ lệ review bất nhất ở cấp khách sạn đã được dùng như **chỉ báo rủi ro danh tiếng** (Wang, P. et al., 2025); luật khía cạnh – cảm xúc được dùng để giải thích ở mức diễn giải được cho quản lý vì sao một khách sạn bị kéo điểm (Öztürk, 2026); chỉ số hợp nhất giữa điểm và cảm xúc được dùng để phát hiện review không đáng tin (Valdivia et al., 2019); các phân tích bất đối xứng được dùng để xếp hạng ưu tiên cải thiện cơ sở vật chất. Trong bối cảnh Việt Nam — nơi Le et al. (2026) lấy toàn bộ dữ liệu — các phát hiện này chưa được chuyển thành công cụ đánh giá nào ở **cấp khía cạnh**. Nhánh **forgiveness/justice** (Yoruk, Hsu & Lee, 2025; Kumar & Shankar, 2024; Honora, Wang & Chih, 2024; Huang & Lo, 2025) là construct liên quan được đề tài **cố ý không đo**, vì chỉ có thể đo bằng bảng hỏi chứ không suy ra được từ review công khai.

### 1.2. The limitation of current works / Những hạn chế của các nghiên cứu hiện tại

**L1 — Bỏ qua hiện tượng bất nhất, hoặc xử lý nó như nhiễu.** Mô hình của Le et al. (2026) giả định quan hệ đơn điệu giữa cảm xúc khía cạnh và điểm số: tích cực thì điểm tăng, tiêu cực thì điểm giảm. Giả định này không giải thích được các quan sát có thật trong chính tập dữ liệu gán nhãn của bài báo. Khảo sát trực tiếp của nhóm trên `data/TripAdvisor_EN.json` (9.990 review gán nhãn) cho thấy **404 review 5 sao chứa ít nhất một span cảm xúc `Negative`**, trong khi toàn tập chỉ có 465 review 1–2 sao và trong đó **199 review vẫn chứa span `Positive`**. Đây là hiện tượng có cấu trúc: Abaiyan et al. (2026) chỉ ra phần lớn mismatch tập trung vào một số nhóm người viết có hành vi hệ thống, chứ không phân bố ngẫu nhiên.

**L2 — Lập luận vòng ở biến `Loyalty`.** Biến `Loyalty` trong Le et al. (2026) được định nghĩa bằng chính các từ ngữ chỉ ý định hành vi (*"come back"*, *"highly recommend"* so với *"stay away"*, *"never again"*), rồi được đưa vào hồi quy để giải thích cho điểm số. Diễn đạt bằng lời và hành vi chấm điểm trong cùng một review là hai biểu hiện đồng thời của một trạng thái, nên dùng vế lời để giải thích vế số là lặp thừa. Hệ quả thực nghiệm là biến "mạnh nhất" trong mô hình lại gần như đồng nhất với biến phụ thuộc.

**L3 — Gộp chung hai trục khác bản thể.** Việc đặt `Loyalty` ngang hàng với `Facility`, `Amenity`, `Service`, `Experience Value` trộn hai phạm trù: **khía cạnh** là khách nói về *cái gì*, còn **cảm xúc và cường độ** là khách cảm thấy *như thế nào*. Cách xử lý đúng là tách hai trục, không phải đổi tên khía cạnh.

**L4 — Các phép đo hiện có làm mất chiều.** Các cách đo đã công bố đều đánh rơi một nửa tín hiệu: SentimentLens (Jayakody et al., 2026) dùng trị tuyệt đối $|R_{norm}-S_a|$ nên không phân biệt khách **cho thêm điểm** với khách **dìm điểm**; Kwon, B. et al. (2025) tách được degree và direction nhưng trên dữ liệu sản phẩm và không ở cấp khía cạnh; Wang, P. et al. (2025) và Abaiyan et al. (2026) giữ direction nhưng chỉ ở mức phân loại rời rạc, làm mất cường độ; Biasetton et al. (2026) và Kovács (2025) làm ở cấp toàn văn bản. **Chưa tìm thấy phép đo nào đồng thời giữ độ lớn và chiều ở cấp khía cạnh dịch vụ trên dữ liệu khách sạn.**

**L5 — Nhánh tâm lý dừng ở biến kết cục tự khai.** Toàn bộ dòng forgiveness/justice dừng lại ở các biến kết cục là forgiveness, repatronage, kỳ vọng phục hồi hoặc dissatisfaction, đo bằng bảng hỏi và tình huống giả định. Chưa có nghiên cứu nào kiểm định quan hệ giữa cơ chế đó và **điểm sao quan sát được**. Đồng thời, review công khai không cho phép suy ra trạng thái tâm lý của người viết: Han & Anderson (2025) so sánh khảo sát riêng với review công khai và tìm thấy **thiên lệch đo lường dương** trên TripAdvisor, còn Sterner (2026) phân rã méo của hệ thống đánh giá thành năm nguồn cấu trúc. Vì vậy đề tài chủ động không dùng các nhãn tâm lý này làm biến đo.

**L6 — Mixed review chưa được phân biệt với bất nhất thật.** Positive và negative aspect có thể đồng tồn tại và bù trừ nhau (Bigné et al., 2023; Öztürk, 2026). Một review 5 sao chứa span tiêu cực do đó **chỉ là ứng viên bất nhất**, chưa phải bất nhất đã xác nhận; phải phân biệt lỗi thật, phàn nàn nhỏ đã được khắc phục, trải nghiệm hỗn hợp, phủ định/châm biếm và lỗi gán nhãn.

**L7 — Chất lượng bằng chứng và tính tái lập của một số nguồn chưa đủ.** Hai nguồn trực tiếp nhất cho typology có hướng và xung đột cấp khía cạnh (Abaiyan et al., 2026; Jayakody et al., 2026) mới là preprint, chưa qua phản biện. Chi tiết đo lường của Wang, D. et al. (2025) chưa lấy được từ full text do paywall. Thêm vào đó, Slevitch (2024) cảnh báo rằng phân loại Kano/PRCA trong hospitality có lỗi quy trình hệ thống và dễ suy ra bất đối xứng ở nơi thực tế là tuyến tính. Do khác biệt label space, cách chia tập và nhiệm vụ, **không nên so sánh trực tiếp accuracy/F1 giữa các bài báo**.

### 1.3. The necessity of the research / Sự cần thiết tiến hành nghiên cứu

**Vấn đề đề tài tập trung giải quyết:** xây dựng một phép đo bất nhất cảm xúc – điểm số **ở cấp khía cạnh dịch vụ, giữ đồng thời độ lớn và chiều**, rồi dùng phép đo đó để kiểm định trên dữ liệu review khách sạn xem **cơ chế bù trừ** (khi lỗi nhẹ hoặc đã được khắc phục, nhiều khía cạnh tích cực cộng gộp và giữ điểm cao) hay **cơ chế chi phối** (một lỗi cơ bản, nghiêm trọng hoặc có tính chẩn đoán cao chi phối đánh giá tổng) đang vận hành, dưới các điều kiện biên đã xác định.

**Tính mới về phương pháp:** phép đo đề xuất giữ dấu ở cấp khía cạnh — $D_{i,a}^{signed}=r_i^*-s_{i,a}^*$ — kết hợp hai đặc tính chưa xuất hiện cùng nhau trong văn hiến: độ chi tiết cấp khía cạnh và việc bảo toàn chiều. Đây là **đề xuất của dự án**, không được mô tả như một công thức chuẩn đã có trong văn hiến. Cần ghi đúng mức độ: kết luận "chưa tìm thấy tiền lệ trực tiếp" chỉ đứng trên tìm kiếm theo tiêu đề và tóm tắt, nên phải viết kèm cách đã tìm, và ranh giới tính mới **mỏng** vì Regitz et al. (2026) làm rất gần — khác ở đơn vị phân tích (hệ số hồi quy theo topic so với review có nhãn người gán).

**Tính mới về bằng chứng:** đóng góp trực tiếp cho khoảng trống L5 bằng cách kiểm định quan hệ giữa cấu hình khía cạnh và **điểm số quan sát được**, thay vì biến kết cục tự khai trong bảng hỏi.

**Tính mới so với bài báo nền tảng:** khắc phục lỗi lập luận vòng của biến `Loyalty` (L2) bằng cách chuyển trọng tâm giải thích sang bất nhất ở cấp khía cạnh, và không dùng lại điểm sao làm nhãn cảm xúc.

**Tính thời sự và ý nghĩa:** khối lượng review trực tuyến tiếp tục tăng nhanh, và chính Almansour et al. (2022) cảnh báo rằng dùng điểm sao làm nhãn cảm xúc là thực hành phổ biến nhưng chưa được kiểm định — nghĩa là nhiều mô hình đang được huấn luyện trên nhãn yếu ở quy mô lớn. Về mặt quản trị, hiểu được khía cạnh nào khách sẵn sàng bỏ qua và khía cạnh nào dẫn tới dìm điểm cho phép khách sạn phân bổ nguồn lực đúng chỗ thay vì đầu tư dàn trải.

---

## 2. Research objectives / Mục tiêu của đề tài

1. **Xây dựng tập đánh giá có đối chứng ở cấp khía cạnh.** Từ corpus TripAdvisor đã gán nhãn của dự án, tạo một evaluation set gồm: các review 5 sao chứa span tiêu cực, tập đối chiếu 1–2 sao chứa span tích cực, và **aligned controls** ở cả hai phía điểm để đo được **tỷ lệ báo động giả** của mọi phép đo.
2. **Thiết lập ground truth có độ tin cậy.** Hai người gán nhãn độc lập trên một calibration subset, đo mức đồng thuận giữa người gán nhãn và giải quyết bất đồng trước khi mở rộng ra toàn bộ tập.
3. **So sánh và chọn phép đo bất nhất.** Đối chiếu tối thiểu ba công thức — ma trận phân cực có hướng 3×3, khoảng cách chuẩn hóa có dấu $z(r)-z(s)$, và khoảng cách cấp khía cạnh có dấu $r^*-s_a^*$ — theo các tiêu chí: khớp với nhãn người, giữ được dấu, ổn định trên cả hai phía điểm, và không rò rỉ dữ liệu.
4. **Kiểm định cơ chế kết hợp bất đối xứng và các điều kiện biên.** Xác định khía cạnh nào mang tính chi phối (penalty-dominant) và khía cạnh nào có khả năng bù trừ, đồng thời kiểm định vai trò điều tiết của mức độ nghiêm trọng, service recovery và hạng sao khách sạn. Cặp `positive Service × negative Facility` được giữ như một **planned contrast**, không phải giả định trung tâm.

---

## 3. Research scope / Phạm vi nghiên cứu

**Đối tượng dữ liệu:** review khách sạn **tiếng Anh** trên TripAdvisor, kế thừa tập gán nhãn chuyên gia của Le et al. (2026) tại `data/TripAdvisor_EN.json`.

**Đặc tả kỹ thuật đã xác minh trực tiếp trên file:**

| Thuộc tính | Giá trị |
| --- | --- |
| Số review gán nhãn | 9.990 |
| Thang điểm | 1–5 |
| Phân bố điểm | 1★ 228 · 2★ 237 · 3★ 601 · 4★ 1.776 · 5★ 7.148 |
| Khách sạn / địa điểm / giai đoạn | 2.622 khách sạn · 50 địa điểm · 2015–2023 |
| Tổng số span khía cạnh | 54.326 |
| Phân bố khía cạnh | Service 19.289 · Facility 12.641 · Experience 9.113 · Amenity 7.651 · Loyalty 4.293 · Branding 1.339 |
| Tổng số span cảm xúc | 54.272 (Positive 46.772 · Negative 4.508 · Neutral 2.992) |
| Review 5★ chứa ≥1 span `Negative` | 404 review |
| Review 1–2★ chứa ≥1 span `Positive` | 199 review (trên tổng 465 review 1–2★) |
| Aligned control 5★ (không có span `Negative`) | 6.744 review |
| Aligned control 1–2★ (không có span `Positive`) | 266 review |

**Nội dung nghiên cứu chính (in-scope):**

- Khai phá khía cạnh và cảm xúc cấp khía cạnh trên review khách sạn tiếng Anh.
- Lượng hóa độ lệch giữa nội dung văn bản và điểm sao, giữ cả độ lớn và chiều, ở cấp khía cạnh.
- Kiểm định thống kê vai trò điều tiết của cấu hình khía cạnh, mức độ nghiêm trọng, service recovery và hạng sao khách sạn lên điểm số.
- **Nhánh ứng dụng của học phần:** pipeline dự đoán mức điểm từ văn bản, phục vụ Bước 5 và Bước 6 của môn DAP391m.

**Ngoài phạm vi (out-of-scope):**

- Xây dựng ứng dụng đặt phòng hoặc hệ thống frontend/backend cho người dùng cuối.
- Xử lý ngôn ngữ ngoài tiếng Anh trong giai đoạn này.
- Thu thập dữ liệu thời gian thực (live scraping).
- Kiểm định trên Booking.com trong giai đoạn này.
- **Đo trực tiếp các trạng thái tâm lý** như tha thứ, phẫn nộ, cảm nhận công bằng hay kỳ vọng — nhóm chủ động không thu thập thêm trường gán nhãn cho các construct này.

**Hai ranh giới đã khóa:**

1. **Phạm vi dữ liệu:** 9.990 review đã gán nhãn; không mở rộng lên corpus 782.584 review của bài báo nền tảng. Mọi tuyên bố về tỷ lệ phải ghi đúng phạm vi **TripAdvisor 2015–2023**.
2. **Hạn chế nhận dạng:** với chỉ dữ liệu review công khai, nghiên cứu **không phân biệt được** giữa bù trừ thật, thiên lệch trình bày của người viết và méo cấu trúc do nền tảng (Han & Anderson, 2025; Sterner, 2026; Mellinas et al., 2025). Giới hạn này phải được viết tường minh trong mọi phần diễn giải.

---

## 4. Feasibility of research / Tính khả thi của đề tài

**Dữ liệu đã có sẵn và đã được xác minh.** Corpus review khách sạn tiếng Anh với nhãn khía cạnh và cảm xúc cấp span đã nằm trong repo (`data/TripAdvisor_EN.json`, 41,1 MB), không phải chờ thu thập. Toàn bộ số liệu ở Mục 3 được tính trực tiếp trên file này. Nguồn gốc và điều kiện sử dụng dữ liệu **[CHƯA CHỐT]** — phải khai báo trước khi nộp bản cuối.

**Tài liệu nền đã đủ để thiết kế thực nghiệm.** Thư viện `refs/` hiện có **35 tệp toàn văn trong 8 cụm chức năng**, trong đó 31 nguồn thuộc core set dùng để viết đề cương (định nghĩa và provenance của thước đo, bằng chứng hiện tượng, cơ chế bất đối xứng, điều kiện biên, phản biện phương pháp, baseline kỹ thuật). Khảo sát văn hiến đã đóng có điều kiện; không cần mở vòng quét rộng thêm.

**Baseline đối chứng đã xác lập.** Pipeline `BERTopic + VADER + WMLR` của bài báo nền tảng là baseline tái lập được, có tham số và kết quả công bố. You et al. (2024) cung cấp mốc so cho chất lượng ABSA, Hu et al. (2024) cung cấp mốc so cho tỷ lệ bất nhất, và Kwon, B. et al. (2025) cung cấp định nghĩa degree/direction để đối chiếu.

**Nguồn lực tính toán.** Toàn bộ pipeline chạy được trên máy tính cá nhân: các mô hình cổ điển và mô hình từ điển rất nhẹ; mô hình transformer ở kích thước base chạy được trên CPU hoặc GPU phổ thông. Nếu nhánh dự báo chọn tinh chỉnh DeBERTa thì cần GPU hoặc môi trường notebook đám mây. Phần dịch vụ đám mây của học phần sử dụng tín dụng AWS/GCP của môn học.

**Nhân sự.** Nhóm tối đa 3 sinh viên, phân vai theo bước dự án với người thực hiện chính và người kiểm tra chéo cho từng bước. Hai người gán nhãn độc lập bắt buộc với tập ground truth.

**Rủi ro đã nhận diện và cách chặn:**

- *Mất cân bằng giữa hai chiều bất nhất* (404 review 5 sao có span tiêu cực so với 199 review 1–2 sao có span tích cực, trong khi toàn tập chỉ có 465 review 1–2 sao). Cách chặn: **báo cáo đúng tỷ lệ thực tế, không cân bằng nhân tạo**; nếu tập đối chiếu không đủ để kết luận thì ghi rõ giới hạn thay vì suy diễn.
- *Chất lượng nhãn cảm xúc tự động.* Cách chặn: không dùng điểm sao để huấn luyện bộ ước lượng cảm xúc, và đo hiệu năng bộ ước lượng bằng tập do người gán nhãn độc lập.
- *Rò rỉ dữ liệu.* Ba đường rò rỉ đã xác minh trên file: (1) **theo khách sạn** — 2.622 khách sạn, cao nhất 85 review/khách sạn, nên phải chia tập theo khách sạn; (2) **qua span `Branding`** — 1.339 span chứa câu khách tự viết số sao, phải loại khỏi mọi đặc trưng dự đoán; (3) **trường `drafts`** — 37 bản ghi nháp lẫn trong file, chỉ dùng `annotations`.
- *Lệch lớp cực nặng* — 5 sao chiếm 71,6%. Cách chặn: dùng macro-F1 và PR-AUC, không báo accuracy; class weight hoặc oversampling chỉ áp trên tập train.
- *Thiên lệch nền tảng và thiên lệch đo lường* — xử lý bằng cách viết tường minh như hạn chế nhận dạng, không xử lý bằng mô hình.

---

## 5. Approach and Method / Cách tiếp cận và phương pháp nghiên cứu

Đề tài theo cách tiếp cận **kết hợp định lượng** với ba tầng: tầng xử lý ngôn ngữ để chuyển văn bản thành tín hiệu cảm xúc cấp khía cạnh, tầng đo lường để lượng hóa độ lệch giữa tín hiệu đó và điểm sao, và tầng kinh tế lượng để kiểm định quan hệ giữa cấu hình khía cạnh, độ lệch và điểm số. Khung lý thuyết đã khóa: **S-O-R** (khung vĩ mô) + **Kano/three-factor** và **Impact Asymmetry** (cơ chế bất đối xứng) + **Prospect Theory** (loss aversion, diminishing sensitivity, reference point) + **quyết định hai giai đoạn không bù trừ → bù trừ**.

### Nguyên tắc tách hai họ mô hình

Đây là yêu cầu phương pháp quan trọng nhất và cũng là chỗ dễ sai nhất:

| | Họ A — Mô hình dự đoán điểm | Họ B — Bộ ước lượng cảm xúc khía cạnh |
| --- | --- | --- |
| Nhiệm vụ | Dự đoán `score` từ văn bản | Sinh tín hiệu cảm xúc cấp khía cạnh |
| Huấn luyện trên | Nhãn điểm sao | Span cảm xúc do người gán |
| Dùng cho | Bước 5 của môn, phần dư `score − score_dự_báo`, phân tích độ nhạy | Phép đo bất nhất (RQ2, RQ3) |
| Lý do tách | Nếu lấy họ A làm thước đo cảm xúc thì mô hình sẽ tái tạo lại chính biến phụ thuộc, vi phạm yêu cầu cốt lõi của đề tài | |

### Stage 1 — Phân tích khám phá dữ liệu

Chạy notebook khám phá trên `data/TripAdvisor_EN.json`: phân bố điểm, phân bố độ dài review, phân bố nhãn khía cạnh và cảm xúc, và kiểm tra tính toàn vẹn của liên kết giữa span khía cạnh và span cảm xúc (khớp theo cặp `start`/`end`). Đầu ra là bảng đặc tả dữ liệu (Data Dictionary) và danh sách các trường hợp cần loại trừ.

### Stage 2 — Xây dựng tập đánh giá có đối chứng

Ba thành phần: (a) review 5 sao chứa span tiêu cực; (b) tập đối chiếu review 1–2 sao chứa span tích cực; (c) **aligned controls** lấy từ cả hai phía điểm. Quy mô khuyến nghị **600–800 mẫu**. Nhóm đối chứng là bắt buộc: nếu tập kiểm thử chỉ gồm các mẫu nghi ngờ thì một phép đo quá nhạy vẫn đạt độ chính xác cao trên tập đó nhưng sẽ **báo động giả** liên tục khi gặp review bình thường.

### Stage 3 — Gán nhãn thủ công và thiết lập ground truth

Hai người gán nhãn độc lập theo năm trường: loại tương thích giữa chữ và điểm, khía cạnh gây lệch, mức độ nghiêm trọng (`Minor`/`Major`), có/không service recovery, và có/không phủ định hoặc châm biếm. Quy trình ba bước: gán nhãn thử độc lập một calibration subset 30–50 mẫu → đo mức đồng thuận (Cohen's Kappa, ngưỡng mục tiêu $\ge 0{,}70$) → họp giải quyết bất đồng và thống nhất quy chuẩn → mở rộng ra toàn bộ tập, các dòng bất đồng được chốt nhãn cuối qua đối soát.

### Stage 4 — So sánh các công thức đo bất nhất

Ba ứng viên được đối chiếu song song trên cùng ground truth:

| Ứng viên | Đầu ra | Vai trò |
| --- | --- | --- |
| Ma trận phân cực có hướng 3×3 | Nhãn lớp | Baseline dễ diễn giải nhất |
| Khoảng cách chuẩn hóa có dấu $z(r)-z(s)$ | Dấu + độ lớn | Kiểm tra khả năng mở rộng từ Kwon, B. et al. (2025) |
| Khoảng cách cấp khía cạnh có dấu $r^*-s_a^*$ | Vector theo khía cạnh + tổng hợp | Ứng viên chính của đề tài |

Phần dư hồi quy $rating - \widehat{rating}_{\text{text}}$ chỉ dùng như **phân tích độ nhạy**, không dùng làm phép đo chính. Khoảng cách embedding và entropy chưa triển khai trừ khi ba công thức trên thất bại.

**Tiêu chí chọn phép đo chính** (phải đạt đồng thời): khớp tốt nhất với nhãn hướng do người gán, báo cáo **macro-F1 và confusion matrix** thay vì accuracy đơn lẻ; giữ được dấu và phân biệt hai hướng bất nhất; ổn định trên cả hai nhóm điểm cao và điểm thấp; giải thích được ở cấp khía cạnh; không dùng điểm sao để huấn luyện bộ ước lượng cảm xúc; không phụ thuộc span `Branding` hoặc các câu nói thẳng số sao.

Nếu không công thức nào đạt tiêu chí, nhóm **giữ ma trận phân cực có hướng làm baseline**, không mở rộng thêm vòng khảo sát, và ghi rõ lý do trong nhật ký validation.

### Stage 5 — Mô hình hóa hành vi chấm điểm

Dùng cấu hình khía cạnh (aspect polarity/configuration), mức độ nghiêm trọng, service recovery cùng hạng sao khách sạn làm biến giải thích cho `score` và cho $D$, kế thừa cách tiếp cận hồi quy của bài báo nền tảng để bảo đảm so sánh được với baseline. Cấu trúc cần kiểm định là **hai nhánh đối lập trong cùng một cơ chế**: nhánh không bù trừ (một lỗi cơ bản, nghiêm trọng hoặc có tính chẩn đoán cao chi phối đánh giá tổng) và nhánh bù trừ (lỗi nhẹ hoặc đã được khắc phục cho phép nhiều khía cạnh tích cực cộng gộp).

**Bốn kiểm định phụ:** (1) khía cạnh nào mang tính chi phối và khía cạnh nào có khả năng bù trừ — trình bày như **phân tích khám phá**, kèm báo cáo bất định, vì công cụ phân loại Kano/PRCA có lỗi quy trình đã được ghi nhận (Slevitch, 2024); (2) mức độ nghiêm trọng và service recovery có làm đổi cơ chế không — chỉ kiểm định được trên evaluation set nên mọi kết luận phải ghi rõ là sub-sample; (3) hiệu ứng có ổn định giữa các nhóm hạng sao khách sạn không; (4) cặp `positive Service × negative Facility` là một planned contrast.

### Rủi ro phương pháp phải xử lý tường minh

- **Tính vòng và vấn đề bộ phận – tổng thể.** $D$ có chứa điểm sao trong định nghĩa, nên không được dùng $D$ để giải thích lại `score` như thể hai biến độc lập. Tầng mô hình hành vi phải mô hình hóa trực tiếp `score` từ cấu hình khía cạnh và các điều kiện biên; $D$ được dùng ở tầng mô tả và tầng kiểm chứng hướng.
- **Rò rỉ dữ liệu.** Ba đường đã xác minh: chia tập theo khách sạn, loại span `Branding`, chỉ dùng `annotations`. Áp dụng cho cả Stage 4 và nhánh dự báo.
- **Hạn chế nhận dạng.** Không phân biệt được bù trừ thật với thiên lệch trình bày và méo nền tảng.
- **Diễn giải.** Không dùng ngôn ngữ khẳng định nhân quả về trạng thái tâm lý của người viết; chỉ phát biểu về mẫu hành vi chấm điểm quan sát được.

### Nhánh dự báo phục vụ học phần DAP391m

Chạy song song, không phụ thuộc các quyết định đo lường còn mở: **năm mô hình** dự đoán mức điểm từ văn bản — TF-IDF + Logistic Regression, TF-IDF + SVM, LightGBM, BiLSTM và DeBERTa (mô hình học sâu) — so sánh bằng macro-F1 và PR-AUC, chia tập theo khách sạn, có tuning và cross-validation. Kết quả nhánh này được đóng gói thành ứng dụng **"Bảng soát điểm sao"**, tách điểm khách bấm khỏi điểm mà nội dung review biện minh, có endpoint dự báo, hàng đợi cảnh báo và kênh hỏi đáp.

**Năm quyết định kỹ thuật phải khóa sau validation (ghi vào một quyết định kiến trúc mới trong `docs/decisions/`, số hiệu kế tiếp sau `RDR-0005`):** (1) bộ ước lượng cảm xúc; (2) cách chuẩn hóa điểm – cảm xúc; (3) ngưỡng phân biệt `aligned` / `mixed` / bất nhất thật; (4) cách tổng hợp cảm xúc nhiều khía cạnh thành kỳ vọng cấp văn bản; (5) công thức đo bất nhất được chọn.

---

## 6. Research plan / Kế hoạch thực hiện nghiên cứu

| No. | Date | Task | Output | Person in charge |
| --- | --- | --- | --- | --- |
| 1 | Tuần 1 [dd/mm]–[dd/mm] | Chốt đề tài, RQ và 3 paper baseline; kiểm kê dữ liệu; dựng Data Dictionary; nộp Project Planning | Project Planning; Data Dictionary | Cả nhóm |
| 2 | Tuần 2 | Làm sạch và kiểm tra toàn vẹn liên kết span; bộ truy vấn SQL nâng cao; biểu đồ nâng cao đầu tiên; 3 biểu đồ mô tả hiện tượng bất nhất | Notebook EDA; bộ SQL; biểu đồ mô tả | Data & EDA Lead |
| 3 | Tuần 3 | Chạy 3 mô hình cổ điển với chia tập theo khách sạn; khởi tạo BiLSTM và DeBERTa; dựng endpoint đầu tiên; nộp Research Proposal | Research Proposal; bảng metric sơ bộ; endpoint draft | Modelling Lead |
| 4 | Tuần 4 | Dựng khung ứng dụng và dashboard; nối endpoint; **làm cảnh báo thật**; kiểm tra checklist chống rò rỉ | Ứng dụng chạy được; sơ đồ kiến trúc | Viz & App Lead |
| 5 | Tuần 5 | Hoàn tất 5 mô hình kèm tuning và cross-validation; so baseline; Review 1 | Bảng metric 5 mô hình; Audit Log đợt 1 | Modelling Lead |
| 6 | Tuần 6 | Dựng evaluation set 600–800 mẫu; calibration 30–50 mẫu với hai người gán nhãn độc lập; chốt RQ mở rộng | Evaluation set; kết quả calibration | Research & Report Lead |
| 7 | Tuần 7 | Đo mức đồng thuận và đối soát; mở rộng gán nhãn toàn tập; so sánh ba công thức và chốt phép đo; chạy mô hình kinh tế lượng; Review 2 | Measure đã chốt; kết quả kinh tế lượng; Audit Log đợt 2 | Research & Report Lead |
| 8 | Tuần 8 | Chạy lại toàn bộ pipeline với seed cố định; rà checklist rò rỉ; viết Methodology, Discussion, Abstract, Introduction | Bản thảo gần cuối; ứng dụng ổn định | Cả nhóm |
| 9 | Tuần 9 | Rà trích dẫn thật; hoàn thiện hình và bảng; bảng RQ → quyết định; nộp Final Report và Slide | Final Report; slide; Audit Log đợt 3 | Cả nhóm |
| 10 | Tuần 10–11 | Luyện demo và vấn đáp; chuẩn bị câu hỏi phản biện về thiên lệch đo lường và lỗi phân loại Kano | Buổi demo và Q&A | Cả nhóm |

---

## Computational Resource Requirements / Yêu cầu nguồn lực tính toán

Một máy tính cá nhân thông thường (hoặc hai máy, vì có hai người gán nhãn độc lập) với môi trường Python và Jupyter Notebook; bảng tính Excel/Google Sheets cho công đoạn gán nhãn. Không cần máy chủ riêng. Nếu nhánh dự báo tinh chỉnh DeBERTa thì cần GPU hoặc môi trường notebook đám mây. Phần tích hợp dịch vụ AI của học phần sử dụng tín dụng AWS/GCP được cấp cho môn học; nhóm chủ động chạy dịch vụ thật sớm vì cảnh báo không thể mock.

---

## 7. Expected results / Dự kiến kết quả đề tài

1. **Bộ dữ liệu đánh giá có đối chứng.** Một tập review khách sạn được hai người gán nhãn độc lập, kèm báo cáo mức đồng thuận và nhãn cuối đã đối soát, bao gồm nhóm aligned controls để đo tỷ lệ báo động giả. Đây là sản phẩm dữ liệu có thể tái sử dụng cho nghiên cứu sau.
2. **Pipeline đo lường bất nhất.** Quy trình từ review thô đến điểm bất nhất cấp khía cạnh, kèm so sánh định lượng giữa ba công thức và lý do chọn phép đo chính.
3. **Bằng chứng thực nghiệm về hai nhánh cơ chế.** Kết quả cho biết khía cạnh nào mang tính chi phối, khía cạnh nào có khả năng bù trừ, và mức độ nghiêm trọng cùng service recovery thay đổi cơ chế đó như thế nào khi đo trên **điểm số quan sát được** — điểm mà văn hiến hiện tại chưa kiểm định.
4. **Nhánh dự báo và ứng dụng học phần.** Bảng so sánh năm mô hình dự đoán mức điểm so với baseline, và ứng dụng "Bảng soát điểm sao" có tích hợp dịch vụ AI.

**Hàm ý lý thuyết:** mở rộng khung S-O-R từ quan hệ đơn điệu sang quan hệ có điều tiết ở cấp khía cạnh, và cung cấp một đường kiểm định trực tiếp giữa cấu hình trải nghiệm dịch vụ và hành vi chấm điểm quan sát được, không cần suy diễn trạng thái tâm lý.

**Hàm ý phương pháp:** đưa ra cảnh báo thực nghiệm cho thực hành dùng điểm sao làm nhãn cảm xúc phổ biến hiện nay, và đề xuất một phép đo giữ đồng thời độ lớn và chiều ở cấp khía cạnh.

**Hàm ý thực tiễn:** chỉ ra cho khách sạn khía cạnh nào khách sẵn sàng bỏ qua và khía cạnh nào dẫn tới dìm điểm, làm cơ sở phân bổ nguồn lực và thiết kế quy trình khắc phục dịch vụ.

**Giới hạn phải công bố:** phạm vi TripAdvisor 2015–2023 với 9.990 review; không phân biệt được bù trừ thật với thiên lệch trình bày và méo nền tảng; phân loại khía cạnh theo Kano chỉ ở mức khám phá.

---

## References

Abaiyan, R., et al. (2026). *Fault of our stars: Behavioral drivers of rating–sentiment incongruence*. arXiv preprint. https://arxiv.org/abs/2606.25518

Albayrak, T., Kılıçarslan, Ö., Fong, L. H. N., Caber, M., & Güven Hamurişçi, A. (2025). Unravelling the influence of service failure on negative customer engagement: The moderating role of service recovery. *International Journal of Hospitality Management, 130*, 104242. https://doi.org/10.1016/j.ijhm.2025.104242

Almansour, A., Alotaibi, R., & Alharbi, H. (2022). Text-rating review discrepancy (TRRD): An integrative review and implications for research. *Future Business Journal, 8*, 3. https://doi.org/10.1186/s43093-022-00114-y

Ameur, A., Hamdi, S., & Ben Yahia, S. (2024). Sentiment analysis for hotel reviews: A systematic literature review. *ACM Computing Surveys, 56*(2), 1–38. https://doi.org/10.1145/3605152

Biasetton, N., Ricciardi, G., & Salmaso, L. (2026). How well do ratings reflect sentiment? Evidence from a large Italian review corpus. *Applied Stochastic Models in Business and Industry, 42*(2). https://doi.org/10.1002/asmb.70090

Bigné, E., Ruiz, C., Perez-Cabañero, C., & Cuenca, A. (2023). Are customer star ratings and sentiments aligned? *Service Business, 17*, 281–314. https://doi.org/10.1007/s11628-023-00524-0

Cui, J., Zhang, S., & Wang, L. (2025). Evaluating canal heritage tourists' satisfaction: An asymmetric impact-performance analysis of the Grand Canal in Beijing, China. *Journal of Hospitality and Tourism Management, 62*, 108–115. https://doi.org/10.1016/j.jhtm.2025.01.002

Das, M., Jebarajakirthy, C., Maseeh, H. I., Lim, W. M., & Shah, J. S. (2026). Online service failure and recovery: An integrated meta-analytic perspective of attribution and justice theories. *Journal of Business Research, 202*, 115752. https://doi.org/10.1016/j.jbusres.2025.115752

Doan, T. T., et al. (2025). HOSSemEval-EB23: A robust dataset for aspect-based sentiment analysis of hospitality reviews. *Multimedia Tools and Applications, 84*, 13057–13087. https://doi.org/10.1007/s11042-024-19518-9

Guidotti, D., Pandolfo, L., & Pulina, L. (2025). Discovering sentiment insights: Streamlining tourism review analysis with large language models. *Information Technology & Tourism, 27*(1), 227–261. https://doi.org/10.1007/s40558-024-00309-9

Han, S., & Anderson, C. K. (2025). The platform matters: Selection and measurement bias in online reviews. *Cornell Hospitality Quarterly*. https://doi.org/10.1177/19389655251327536

Honora, A., Wang, K.-Y., & Chih, W.-H. (2024). The role of customer forgiveness and perceived justice in restoring relationships with customers. *Service Business, 18*, 363–393. https://doi.org/10.1007/s11628-024-00563-1

Hu, F., Pan, J., & Wang, H. (2024). Unveiling the spatial and temporal variation of customer sentiment in hotel experiences: A case study of Beppu City, Japan. *Humanities and Social Sciences Communications, 11*(1), 1695. https://doi.org/10.1057/s41599-024-04226-4

Huang, Z., & Lo, A. (2025). Human vs. robot service provider agents in service failures: Comparing customer dissatisfaction and the mediating role of forgiveness and service recovery expectation. *Information Technology & Tourism, 27*, 417–448. https://doi.org/10.1007/s40558-025-00314-6

Hwang, J. (2024). The effects of service recovery actions on customers' post-recovery responses to online travel agencies (OTAs): The moderating role of price. *International Journal of Tourism Research, 26*(4), e2742. https://doi.org/10.1002/jtr.2742

Jayakody, D., Thenahandi, P., & Jayarathna, S. (2026). *SentimentLens: Reconciling sentiment and ratings via dual-modality in the hospitality sector*. arXiv preprint. https://arxiv.org/abs/2606.00084

Kirilenko, A., Stepchenkova, S., Gromoll, R., & Jo, Y. (2024). Comprehensive examination of online reviews divergence over time and platform types. *International Journal of Hospitality Management, 117*, 103647. https://doi.org/10.1016/j.ijhm.2023.103647

Kovács, I. (2025). The impact of construal level on review consistency and helpfulness in online evaluations. *Computers in Human Behavior, 162*, 108550. https://doi.org/10.1016/j.chb.2024.108550

Kumar, A., & Shankar, A. (2024). Why do consumers forgive online travel agencies? A multi-study approach. *Australasian Marketing Journal, 32*(4), 323–338. https://doi.org/10.1177/14413582231194071

Kwon, B., Lee, J., Min, J., Kwak, C., & Choi, H. S. (2025). Beyond the stars: The impact of rating-text inconsistency on perceived review usefulness. *Asia Pacific Journal of Information Systems, 35*(1), 49–72. https://doi.org/10.14329/apjis.2025.35.1.49

Kwon, W. (2026). Aspect-based sentiment analysis through zero-shot text classification and impact-asymmetry analysis. *International Journal of Hospitality Management, 133*, 104397. https://doi.org/10.1016/j.ijhm.2025.104397

Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026). Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings. *International Journal of Hospitality Management, 134*, 104574.

Leo, W. W. C., Maggioni, I., Sembada, A. Y., & Tsarenko, Y. (2026). The dynamics of customer participation in service recovery: The roles of failure severity, quality signals, and responsiveness. *International Journal of Hospitality Management, 140*, 104809. https://doi.org/10.1016/j.ijhm.2026.104809

Li, J., Lee, B., & Kim, J. (2025). Analyzing factors affecting overall customer satisfaction using hotel ratings and reviews with BERTopic and three-factor theory. *SAGE Open, 15*(3). https://doi.org/10.1177/21582440251335169

Li, S., Zhu, B., Zhang, Y., Liu, F., & Yu, Z. (2024). A two-stage nonlinear user satisfaction decision model based on online review mining: Considering non-compensatory and compensatory stages. *Journal of Theoretical and Applied Electronic Commerce Research, 19*(1), 272–296. https://doi.org/10.3390/jtaer19010015

Lim, W. M., Saha, V., & Das, M. (2025). From service failure to brand loyalty: Evidence of service recovery paradox. *Journal of Brand Management, 32*(4), 257–281. https://doi.org/10.1057/s41262-025-00380-5

Liu, X., Ma, X., & Dou, Y. (2025). Injecting new insights: How do review sentiment and rating inconsistency shape the helpfulness of airline reviews? *Information Processing & Management, 62*(2), 104088. https://doi.org/10.1016/j.ipm.2025.104088

Marreira, et al. (2026). Rating–text mismatch in Brazilian Portuguese reviews: How reliable are zero-shot LLMs? In *Proceedings of PROPOR 2026* (pp. 959–967). https://aclanthology.org/2026.propor-1.96/

Mellinas, J. P., Di Nolfo-Aiassa, C., & Martin-Fuentes, E. (2025). The weight of a review: Assessing Booking.com's new scoring system. *Tourism and Hospitality Research*. https://doi.org/10.1177/14673584251384011

Öztürk, A. C. (2026). Discovering aspect–sentiment drivers of hotel review ratings with interpretable high-utility rules. *IEEE Access, 14*, 39496–39511. https://doi.org/10.1109/access.2026.3672490

Park, H., Lee, M., Back, K.-J., DeFranco, A., & Suh, J. (2025). Dynamic roles of hotel mobile application in customer satisfaction and dissatisfaction: Integrating text analytics and impact asymmetry analysis. *International Journal of Contemporary Hospitality Management, 37*(5), 1622–1640. https://doi.org/10.1108/IJCHM-12-2023-1914

Pramono, B. A., Gernowo, R., & Sofwan, A. (2026). Explainable multilingual aspect-based sentiment analysis for tourism using SHAP and LIME. *Engineering, Technology & Applied Science Research, 16*(3), 37077–37084. https://doi.org/10.48084/etasr.18774

Puh, K., & Bagić Babac, M. (2023). Predicting sentiment and rating of tourist reviews using machine learning. *Journal of Hospitality and Tourism Insights, 6*(3), 1188–1204. https://doi.org/10.1108/JHTI-02-2022-0078

Regitz, D., Höpken, W., & Fuchs, M. (2026). Online customer feedback for identifying KANO product quality features: A fine-grained topic detection and sentiment analysis approach. *Information Technology & Tourism, 28*(1), Article 20. https://doi.org/10.1007/s40558-025-00354-y

Sharma, A., Shin, S., Nicolau, J. L., & Park, S. (2025). The review sentiment garden: Blossoming loss aversion and diminishing sensitivity across time and crisis. *International Journal of Hospitality Management, 129*, 104170. https://doi.org/10.1016/j.ijhm.2025.104170

Slevitch, L. (2024). Kano model categorization methods: Typology and systematic critical overview for hospitality and tourism academics and practitioners. *Journal of Hospitality & Tourism Research*. https://doi.org/10.1177/10963480241230957

Sterner, M. (2026). Biases in online reputation systems: A survey of the empirical literature. *Electronic Commerce Research*. https://doi.org/10.1007/s10660-026-10176-7

Tan, K. P.-S., & Zou, S. (2024). The profitable art of managerial responses to online reviews: A justice-based investigation of service recovery and firm-level operating performance. *Journal of Quality Assurance in Hospitality & Tourism*, 1–26. https://doi.org/10.1080/1528008X.2024.2410214

Tengilimoglu, E., & Öztürk, Y. (2024). The effects of eWOM triggered service recovery on customer citizenship behavior in the hospitality industry: The moderating role of failure severity. *International Journal of Tourism Research, 26*(4), e2673. https://doi.org/10.1002/jtr.2673

Topçu, A., Asar, M. A., & Orman, G. K. (2026). Improving hotel review rating prediction with transformer models. *Sakarya University Journal of Computer and Information Sciences, 9*(2), 451–464. https://dergipark.org.tr/en/pub/saucis/article/1748175

Valdivia, A., et al. (2019). Inconsistencies on TripAdvisor reviews: A unified index between users and sentiment analysis methods. *Neurocomputing, 353*, 3–16. https://doi.org/10.1016/j.neucom.2018.09.096

Wang, D., Xia, Q., Feng, Y., & Cheng, T. C. E. (2025). Unravelling the effects of two inconsistencies on online review helpfulness: Evidence from TripAdvisor. *Decision Support Systems, 193*, 114450. https://doi.org/10.1016/j.dss.2025.114450

Wang, J., Wu, J., Sun, S., & Wang, S. (2024). The relationship between attribute performance and customer satisfaction: An interpretable machine learning approach. *Data Science and Management, 7*(3), 164–180. https://doi.org/10.1016/j.dsm.2024.01.003

Wang, P., Zhang, H., Yuan, X., & Zhang, X. (2025). Beyond the stars: Unpacking the impact of score-textual inconsistency of online reviews on hotel performance. *International Journal of Hospitality Management, 130*, 104271. https://doi.org/10.1016/j.ijhm.2025.104271

Wei, J., et al. (2025). Consumer forgiveness in online travel agency service recovery: Consumer empathy and negative emotional contagion. *International Journal of Tourism Research, 27*(6). https://doi.org/10.1002/jtr.70154

Xu, W., Yao, Z., Ma, Y., & Li, Z. (2025). Understanding customer complaints from negative online hotel reviews: A BERT-based deep learning approach. *International Journal of Hospitality Management, 126*, 104057. https://doi.org/10.1016/j.ijhm.2024.104057

Yoruk, I., Hsu, J.-H., & Lee, Z. W. Y. (2025). Consumer forgiveness: A literature review and research agenda. *Psychology & Marketing, 42*(2), 554–578. https://doi.org/10.1002/mar.22138

You, X.-Y., Chang, S.-C., Hung, S.-M., Ku, C.-H., & Chang, Y.-C. (2024). Using multitask learning with pre-trained language models for aspect-based sentiment analysis in the hospitality industry. In *Proceedings of PACLIC 2024* (pp. 131–140). https://aclanthology.org/2024.paclic-1.12/

Zhang, F., Seshadri, K., Liu, S., & Santamouris, M. (2025). The impact of indoor environmental quality on tourist accommodation ratings using guest reviews. *Building and Environment, 280*, 113135. https://doi.org/10.1016/j.buildenv.2025.113135

Zhong, K., Liu, K., Gao, X., & Liu, Y. (2026). Impact of sensory clues in reviews on hotel ratings. *Annals of Tourism Research, 119*, 104208. https://doi.org/10.1016/j.annals.2026.104208

Zhu, A., et al. (2025). DaNet: Dual-aware enhanced alignment network for multimodal aspect-based sentiment analysis. In *Findings of ACL 2025* (pp. 14369–14381). https://doi.org/10.18653/v1/2025.findings-acl.741

> **Ghi chú về tài liệu tham khảo:** một số mục còn ở dạng `et al.` hoặc thiếu số trang vì mới xác minh được ở mức metadata/abstract và chưa lấy được toàn văn: `Abaiyan et al. (2026)`, `Jayakody et al. (2026)`, `Wei et al. (2025)`, `Doan et al. (2025)`, `Valdivia et al. (2019)`, `Marreira et al. (2026)`. Phải bổ sung danh sách tác giả đầy đủ trước khi nộp Final Report.

---

## Appendix A — Open items checklist

*Phần này không thuộc template nộp; giữ lại để nhóm theo dõi các điểm chưa chốt.*

| # | Vị trí | Nội dung cần chốt | Cách khóa |
| --- | --- | --- | --- |
| 1 | Tiêu đề | Tên đề tài chính thức | Chốt sau validation (phụ thuộc phép đo được chọn) |
| 2 | Phần đầu | Giảng viên hướng dẫn, thành viên, MSSV | Điền trực tiếp |
| 3 | Mục 4 | Nguồn gốc và điều kiện sử dụng dữ liệu | Ghi rõ nguồn trong báo cáo |
| 4 | Mục 5 | Bộ ước lượng cảm xúc | Validation Stage 3–4 |
| 5 | Mục 5 | Chuẩn hóa điểm – cảm xúc | Validation Stage 4 |
| 6 | Mục 5 | Ngưỡng phân biệt `aligned` / `mixed` / bất nhất thật | Validation Stage 4 |
| 7 | Mục 5 | Cách tổng hợp cảm xúc nhiều khía cạnh | Validation Stage 4 |
| 8 | Mục 5 | Công thức đo bất nhất được chọn | Validation Stage 4 |
| 9 | Mục 5 | Sơ đồ kiến trúc pipeline | Vẽ sau khi chốt #4–#8 |
| 10 | Mục 3 | Định nghĩa "negative span" đóng băng | Tài liệu dự án ghi 402, tính lại trên file là 404; nếu loại span đồng thời gắn `Branding` còn 394, nếu chỉ tính khía cạnh lõi còn 392. Phải chốt định nghĩa, chạy lại một lần và sửa mọi tài liệu đang ghi 402 |
| 11 | Mục 3 | Tên khía cạnh dùng thống nhất giữa văn bản và mã (`Experience` hay `Experience Value`) | Thống nhất khi viết code |
| 12 | Mục 5 | RQ1 và RQ2 chốt chính thức | Đối chiếu giảng viên hướng dẫn |
| 13 | Mục 6 | Ngày cụ thể theo lịch học kỳ và phân công theo tên | Điền sau khi có lịch |
| 14 | References | Bổ sung metadata đầy đủ cho 6 nguồn | Truy xuất Crossref/nhà xuất bản |

---

*Tài liệu liên quan:* [`reports/md/project_planning.md`](project_planning.md) · [`docs/decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md`](../../docs/decisions/RDR-0004_lock_rq3_asymmetric_aspect_compensation.md) · [`docs/decisions/RDR-0005_close_survey_and_lock_framework.md`](../../docs/decisions/RDR-0005_close_survey_and_lock_framework.md) · [`docs/logs/validation/0001_manual_annotation_protocol.md`](../../docs/logs/validation/0001_manual_annotation_protocol.md) · [`refs/INDEX.md`](../../refs/INDEX.md)
