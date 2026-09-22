# Từ điển Thuật ngữ Nghiên cứu (Research Glossary)

Tài liệu này tổng hợp toàn bộ các thuật ngữ chuyên môn, khái niệm lý thuyết, mô hình NLP và công thức toán học được sử dụng xuyên suốt từ giai đoạn khởi động dự án đến nay.

- **Cập nhật:** 2026-09-23, bổ sung thuật ngữ sau Survey Round 4.

---

## 1. Khái niệm Cốt lõi & Hiện tượng Nghiên cứu (Core Constructs)

| Thuật ngữ (Tiếng Anh) | Tên tiếng Việt & Định nghĩa | Ngữ cảnh & Vai trò trong Dự án |
| :--- | :--- | :--- |
| **Sentiment–Rating Inconsistency (Incongruence / Discrepancy)** | **Bất nhất cảm xúc - điểm số:** Hiện tượng cảm xúc diễn đạt trong bài viết mâu thuẫn với số sao được chấm (ví dụ: viết chê nhưng chấm 5 sao, hoặc khen hết lời nhưng chấm 1 sao). | Bài toán trọng tâm của đề tài mở rộng nhằm giải mã hành vi "nói một đằng, chấm một nẻo" của khách du lịch. |
| **TRRD (Text-Rating Review Discrepancy)** | **Độ lệch văn bản - điểm số:** Thuật ngữ học thuật chính thức (Almansour et al., 2022) định danh bài toán bất nhất giữa text và rating trong nghiên cứu kinh doanh trực tuyến. | Khái niệm bảo trợ học thuật, dùng để định vị đề tài vào dòng chảy nghiên cứu quốc tế. |
| **Weak Label Reliability / Label Noise** | **Độ tin cậy nhãn yếu:** Rủi ro khi các nhà nghiên cứu NLP tự động lấy điểm sao (rating) làm nhãn cảm xúc chân lý (ground truth) mà không kiểm tra độ tương thích với bài viết. | Luận điểm phản biện của đề tài đối với các bài báo NLP truyền thống; chứng minh điểm sao không thể thay thế cho cảm xúc thật. |
| **Tautology (Circularity)** | **Ngụy biện vòng lặp (Lập luận thừa):** Lỗi logic khi dùng một biến độc lập thực chất cùng bản chất với biến phụ thuộc để giải thích cho nó (ví dụ: dùng từ khóa quay lại/tẩy chay để dự đoán điểm 1 sao / 5 sao). | Điểm phản biện cốt lõi nhắm vào biến `Loyalty` trong paper gốc (Le et al., IJHM 2026). |
| **Sublimation / Forgiveness** | **Sự thăng hoa / Vị tha:** Trạng thái khách hàng bỏ qua hoặc giảm nhẹ các lỗi dịch vụ/cơ sở vật chất nhỏ nhờ sự hài lòng vượt bậc ở khía cạnh khác (thường là nhân viên). | Ứng viên biến điều tiết giải thích hiện tượng *High Rating - Negative Text*. **Round 4:** chỉ nêu như giả thuyết — không suy diễn trạng thái tâm lý từ review công khai (hạn chế nhận dạng, Han & Anderson 2025). |
| **Outrage / Punitive Rating** | **Sự phẫn nộ / Chấm điểm trừng phạt:** Trạng thái bức xúc tột độ khiến khách hàng trừng phạt khách sạn bằng điểm số thấp nhất (1-2 sao) dù các khía cạnh khác có thể chấp nhận được. | Ứng viên biến điều tiết giải thích hiện tượng *Low Rating - Positive Text*. **Round 4:** chỉ nêu như giả thuyết — xem cảnh báo ở dòng *Sublimation*. |
| **Buffering Effect** | **Hiệu ứng tấm đệm:** Cơ chế tâm lý trong đó trải nghiệm xuất sắc ở một khía cạnh (như thái độ phục vụ tận tâm) đóng vai trò "lá chắn", làm giảm tác động tiêu cực của lỗi cơ sở vật chất lên điểm số cuối cùng. | Cơ chế giải thích mối quan hệ giữa các khía cạnh dịch vụ và hành vi chấm sao của khách. |
| **Process Failure vs. Outcome Failure** | **Lỗi quy trình vs. Lỗi kết quả:** *Process failure* là lỗi trong cách thức cung cấp dịch vụ (chờ lâu, nhân viên thiếu nhiệt tình); *Outcome failure* là lỗi không đáp ứng nhu cầu cốt lõi (hết phòng, phòng không có nước nóng, mất điện). | Căn cứ lý thuyết từ Huang & Lo (2025) cho thấy khách dễ vị tha với lỗi quy trình hơn là lỗi kết quả. |
| **Service Recovery Expectation (SRE)** | **Kỳ vọng khắc phục dịch vụ:** Mức độ và hình thức đền bù/sửa sai mà khách hàng mong đợi từ doanh nghiệp sau khi xảy ra sự cố. | Biến trung gian (mediator) trong chuỗi tâm lý dẫn từ lỗi dịch vụ đến mức độ không hài lòng. |
| **Negative Emotional Contagion** | **Sự lây lan cảm xúc tiêu cực:** Hiện tượng cảm xúc bực bội của một cá nhân bị khuếch đại bởi môi trường xung quanh hoặc bởi thái độ của người khác. | Yếu tố làm suy yếu lòng vị tha của khách hàng (Wei et al., 2025). |
| **Compensatory Effect (Cancel-out)** | **Hiệu ứng bù trừ / Triệt tiêu:** Hiện tượng các khía cạnh tốt và xấu trong cùng một kỳ nghỉ triệt tiêu lẫn nhau khi khách tổng hợp thành một đánh giá tổng thể (Bigne et al., 2023). | Giải thích cho các trường hợp đánh giá 3 sao hoặc review chứa cả khen lẫn chê nhưng không mâu thuẫn. |
| **Asymmetric Aspect Compensation** | **Bù trừ bất đối xứng:** Positive và negative sentiment trên nhiều khía cạnh kết hợp không cân xứng để tạo điểm tổng; gồm hai nhánh compensatory và non-compensatory/penalty-dominant. | Cơ chế trung tâm của RQ3, đã chốt theo `RDR-0004`. |
| **Non-compensatory / Penalty-dominant** | **Không bù trừ / Phạt chi phối:** Một lỗi basic, severe hoặc diagnostic chi phối đánh giá tổng; các positive aspect khác không đủ bù. | Nhánh giải thích chiều `D < 0` mà không cần gán trạng thái tâm lý (Sharma et al., 2025; Hwang, 2024). |
| **Failure Severity** | **Mức nghiêm trọng của lỗi:** Độ nặng của sự cố dịch vụ, điều tiết việc recovery có cứu được đánh giá hay không. | Boundary condition của RQ3; chỉ gán nhãn được trên evaluation set (`Minor/Major`), không có trên toàn corpus. |
| **Service Recovery** | **Khắc phục dịch vụ:** Hành động sửa sai/đền bù của khách sạn sau sự cố. | Boundary condition của RQ3 (`Yes/No` trên evaluation set); đo được từ văn bản review và phản hồi khách sạn (Tan & Zou, 2024). |
| **Service Recovery Paradox** | **Nghịch lý khắc phục dịch vụ:** Sau recovery thành công, hài lòng có thể vượt cả mức nền trước sự cố. | Giới hạn trên của bù trừ; chặn diễn giải `D > 0` quá rộng (Lim et al., 2025). |
| **Double Deviation** | **Sai lệch kép:** Lỗi ban đầu cộng với recovery thất bại, tạo penalty phi tuyến. | Cơ chế penalty-dominant điển hình, dùng để đọc các ca `D < 0` nặng (Hwang, 2024). |
| **Platform & Presentational Bias** | **Thiên lệch nền tảng & thiên lệch trình bày:** (1) người dùng nền tảng chấm công khai cao hơn trải nghiệm tự khai; (2) cùng khách sạn cho phân bố sao/cảm xúc khác nhau giữa các nền tảng; (3) thuật toán nền tảng có thể tách điểm khỏi văn bản. | Threat to identification: `D > 0` có thể là artefact trình bày, không phải bù trừ thật (Han & Anderson, 2025; Kirilenko et al., 2024; Mellinas et al., 2025). |

---

## 2. Khung Lý thuyết Hành vi & Kinh tế lượng (Theories)

| Lý thuyết | Tên tiếng Anh & Nguồn gốc | Cơ chế giải thích chính |
| :--- | :--- | :--- |
| **S-O-R Framework** | **Stimulus–Organism–Response** (Mehrabian & Russell, 1974) | Kích thích môi trường/dịch vụ ($S$) $\rightarrow$ Trạng thái cảm xúc nội tại của khách ($O$) $\rightarrow$ Hành vi phản hồi/chấm sao ($R$). Khung vĩ mô kế thừa từ paper gốc. |
| **Perceived Justice Theory** | **Lý thuyết Công bằng Cảm nhận** (Adams, 1965) | Gồm 3 thành phần: *Distributive* (chia sẻ kết quả/tiền bạc), *Procedural* (quy trình xử lý) và *Interactional* (thái độ giao tiếp). Công bằng cao thúc đẩy sự vị tha. |
| **Expectancy–Disconfirmation Theory (EDT)** | **Lý thuyết Kỳ vọng – Sai lệch kỳ vọng** (Oliver, 1980) | Sự hài lòng được quyết định bởi khoảng cách giữa kỳ vọng ban đầu và trải nghiệm thực tế (dương: vượt kỳ vọng; âm: thất vọng). |
| **Herzberg’s Two-Factor Theory** | **Thuyết Hai nhân tố** (Herzberg, 1959) | *Hygiene factors* (Yếu tố duy trì - phòng ốc, vệ sinh: thiếu thì bất mãn, đủ thì bình thường); *Motivator factors* (Yếu tố động viên - thái độ phục vụ: tạo sự thăng hoa). |
| **Mind Perception Theory** | **Thuyết Nhận thức Tâm trí** (Gray et al., 2007) | Đánh giá đối tượng qua 2 chiều: *Agency* (năng lực hành động, tư duy) và *Experience* (khả năng cảm nhận cảm xúc). Giải thích phản ứng khác nhau giữa người và robot. |
| **Attribution Theory** | **Lý thuyết Quy kết** (Weiner, 1986) | Khách tìm nguyên nhân lỗi theo 3 chiều: *Locus of causality* (do ai), *Controllability* (có kiểm soát được không), *Stability* (lỗi nhất thời hay hệ thống). |
| **Curiosity Theory** | **Lý thuyết Hiếu kỳ** (Loewenstein, 1994; Berlyne, 1960) | Khoảng cách thông tin (*information gap*) gây tò mò, thúc đẩy người đọc xử lý thông tin kỹ lưỡng hơn khi gặp review bất nhất (Kwon et al., 2025). |
| **Heuristic–Systematic Model (HSM)** | **Mô hình Xử lý Kép** (Chaiken, 1980) | Người đọc dùng đường tắt nhận thức (*heuristic cues* như số sao) hoặc xử lý phân tích sâu (*systematic cues* như nội dung bài viết). |
| **Schema Incongruity Theory** | **Thuyết Bất tương thích Giản đồ** (Mandler, 1982) | Khi một thông tin lệch khỏi kỳ vọng sẵn có (giản đồ), não bộ buộc phải phân bổ nhiều tài nguyên nhận thức hơn để giải mã. |
| **Kano Model / Three-Factor Theory** | **Mô hình Kano / Thuyết ba nhân tố** (Kano, 1984; Matzler & Hinterhuber, 1998) | Phân loại thuộc tính thành *Must-Be (Basic)* — thiếu thì bất mãn, có thì trung tính; *One-dimensional (Performance)* — hài lòng tuyến tính; *Attractive (Excitement)* — có thì thưởng, thiếu không bị phạt; cộng *Indifferent* và *Reverse*. |
| **Impact Asymmetry Analysis (IAA) / PRCA / AIPA** | **Phân tích bất đối xứng tác động** (Mikulić & Prebežac) | So chỉ số penalty với chỉ số reward của từng thuộc tính để xếp vào ba nhóm Kano; chạy được trên sentiment review hoặc điểm hài lòng. **Cảnh báo:** phân loại Kano/PRCA trong hospitality có lỗi quy trình hệ thống → chỉ dùng như phân tích **khám phá** (Slevitch, 2024). |

---

## 3. Khai phá Dữ liệu & Xử lý Ngôn ngữ Tự nhiên (ABSA & NLP)

| Thuật ngữ / Mô hình | Định nghĩa kỹ thuật | Ứng dụng trong Đề tài |
| :--- | :--- | :--- |
| **ABSA** | **Aspect-Based Sentiment Analysis:** Phân tích cảm xúc theo từng khía cạnh dịch vụ cụ thể thay vì chỉ gán một nhãn chung cho cả bài review. | Trích xuất cảm xúc riêng biệt cho từng thành phần: Phòng, Nhân viên, Tiện ích, Giá trị. |
| **ATE & ASC** | **Aspect Term Extraction & Aspect Sentiment Classification:** Hai nhiệm vụ con của ABSA: (1) Rút trích từ chỉ khía cạnh; (2) Phân loại cảm xúc (Tích cực/Tiêu cực/Trung tính) cho khía cạnh đó. | Kỹ thuật cốt lõi để bóc tách nhãn từ tập dữ liệu review `TripAdvisor_EN.json`. |
| **Core Hospitality Aspects** | **Các khía cạnh dịch vụ cốt lõi:** bộ nhãn dùng cho phân tích gồm `Facility` (Cơ sở vật chất), `Service` (Dịch vụ/Nhân viên), `Amenity` (Tiện nghi), `Experience` (Giá trị trải nghiệm). | Dữ liệu `TripAdvisor_EN.json` có **6 nhãn** span khía cạnh; hai nhãn còn lại bị loại khỏi phân tích: `Loyalty` (4.293 span) vì nguy cơ **circularity** đúng như phản biện bài gốc, và `Branding` (1.339 span) vì **rò rỉ nhãn** — span chứa câu khách tự viết số sao như *"give 5 star"*. |
| **BERTopic** | Mô hình topic modeling dựa trên biến áp (Transformer) kết hợp giảm chiều UMAP, phân cụm HDBSCAN và tính trọng số c-TF-IDF. | Pipeline phân cụm chủ đề của paper gốc (Le et al., 2026). |
| **VADER** | **Valence Aware Dictionary and sEntiment Reasoner:** Bộ công cụ phân tích cảm xúc dựa trên từ điển luật (rule-based) chuyên biệt cho văn bản mạng xã hội. | Bộ gán nhãn cảm xúc ban đầu của paper gốc; bị hạn chế về khả năng hiểu ngữ cảnh sâu. |
| **DeBERTa / Instruct-DeBERTa** | Mô hình Transformer tiên tiến với cơ chế *Disentangled Attention* (tách biệt nội dung và vị trí) và *Enhanced Mask Decoder*. | Kiến trúc cho độ chính xác ABSA cao nhất hiện nay trên dữ liệu review khách sạn (Jayakody 2026, Topçu 2026). |
| **TAS-BERT** | **Target-Aspect-Sentiment BERT:** Mô hình Transformer chuyên biệt giải quyết đồng thời cả bộ ba (Target, Aspect, Sentiment). | Baseline ABSA đối chuẩn hàng đầu trên tập dữ liệu khách sạn Việt Nam (HOSSemEval-EB23 / Doan et al., 2025). |
| **HUIM (High-Utility Itemset Mining)** | Khai phá tập mục hữu dụng cao: Thuật toán luật kết hợp có trọng số, phát hiện các tổ hợp khía cạnh cảm xúc đồng xuất hiện mang lại tiện ích lớn nhất (Öztürk, 2026). | Mô hình giải thích quy luật bù trừ đa khía cạnh mang tính diễn giải cao. |
| **Random Oversampling (ROS)** | Kỹ thuật nhân bản mẫu thiểu số ngẫu nhiên để cân bằng dữ liệu trong bài toán phân loại đa lớp. | Được chứng minh vượt trội hơn SMOTE trên dữ liệu văn bản review du lịch vì bảo tồn ngữ nghĩa nguyên gốc (Topçu et al., 2026). |
| **Multitask ABSA với PLM** | **Học đa nhiệm trên mô hình ngôn ngữ tiền huấn luyện:** một mô hình chia sẻ biểu diễn cho nhiều tác vụ con của ABSA (AT & ASC). | Baseline dùng lại được cho artifact: RoBERTa đa nhiệm đạt F1 0,5817 trên 8 khía cạnh hospitality — cao hơn XGBoost 0,4938 và LSTM-attention 0,4208 (You et al., 2024, PACLIC). |
| **SHAP / LIME + Faithfulness (eraser)** | **Giải thích cục bộ cho dự đoán + kiểm định độ trung thực:** SHAP/LIME chỉ ra đặc trưng đóng góp; eraser kiểm tra giải thích có thật sự quyết định dự đoán. | Tầng giải thích của app (checklist #2 của môn). Nguồn Pramono et al. (2026) có **venue chưa xác lập** — chỉ dùng kỹ thuật, không làm bằng chứng domain. |
| **Ordinal Regression (CORAL)** | **Hồi quy thứ tự:** dự đoán mức sao như các ngưỡng thứ tự thay vì phân loại rời rạc. | Dùng cho text-implied rating ở nhánh đối chứng (Biasetton et al., 2026). |

---

## 4. Công thức & Đo lường Độ bất nhất (Operationalization)

| Tên phương pháp | Công thức / Cấu trúc toán học | Đặc điểm & Hạn chế |
| :--- | :--- | :--- |
| **Directional Polarity Matrix** | Rời rạc hóa text và rating về $\{-1, 0, 1\}$:<br>• Incongruent: $\text{Sign}(R) \neq \text{Sign}(S)$ | Trực quan, dễ giải thích; nhưng mất thông tin về cường độ lệch (Wang et al., 2025 IJHM). |
| **6-Pattern Typology** | 6 kiểu hình phân loại (Abaiyan et al., 2026):<br>1. *Conservative Rater* (Text khen, chấm 3-4 sao)<br>2. *Obligatory 5-Star* (Chê/bình thường nhưng vẫn chấm 5 sao)<br>3. *Polite Inflator* / 4. *Frustrated Neutral*<br>5. *Harsh Deflator* / 6. *Critical Purist* | Bằng chứng cho thấy bất nhất có cấu trúc định hướng rõ ràng, không phải lỗi ngẫu nhiên. |
| **Continuous Magnitude Gap** | $$D_i^{abs} = \left\| z(r_i) - z(s_i) \right\|$$<br>(Kwon et al., 2025 APJIS) | Đo độ lớn sai lệch liên tục sau khi chuẩn hóa z-score theo từng sản phẩm; bỏ qua chiều hướng sai lệch. |
| **Aspect-Level Absolute Conflict** | $$C = \left\{ (h, a) : \left\| R_{norm} - S_a \right\| > \tau \right\}$$<br>(Jayakody et al., 2026 - SentimentLens) | So sánh điểm rating tổng thể với cảm xúc của từng khía cạnh; nhược điểm là dùng trị tuyệt đối nên mất dấu (direction). |
| **Unified Geometric Index** | $$f(x, y) = \sqrt{x \cdot y^\beta}$$<br>(Valdivia et al., 2019 Neurocomputing) | $x$: user rating chuẩn hóa; $y$: text sentiment chuẩn hóa; $\beta$: trọng số. Trung bình nhân trừng phạt mạnh nếu 1 trong 2 vế sụp đổ về 0. |
| **Signed Aspect Discrepancy** | $$D_{i,a}^{signed} = r_i^* - s_{i,a}^*$$<br>*(Đề xuất mở rộng của Đề tài)* | $D > 0$: Điểm số cao hơn lời khen (Vị tha / Buffering).<br>$D < 0$: Điểm số thấp hơn lời khen (Trừng phạt / Anger). Giữ trọn vẹn cả độ lớn lẫn chiều hướng. |
| **Econometric Residual** | $$e_i = \text{Rating}_i - \widehat{\text{Rating}}_i$$ | Phần dư từ mô hình hồi quy dự đoán điểm; phụ thuộc lớn vào chất lượng của mô hình hồi quy nền. |
| **Text-Implied Rating Gap** | $$g_i = r_i - \hat{r}^{text}_i$$ (Biasetton et al., 2026) | So điểm sao với điểm dự đoán từ **toàn văn bản** (AlBERTo + CORAL). Cấp văn bản, **không có chiều khía cạnh** → không dùng trực tiếp cho RQ2/RQ3. |
| **Binary Mismatch Classification** | Nhãn nhị phân: nội dung có lệch với mức sao (1 vs 5 sao) không? (Marreira et al., 2026) | Chỉ có nhãn lệch/không lệch — **mất cả magnitude lẫn direction**. |
| **Scalar Inconsistency** | Một scalar tổng hợp cho cả review; outcome là helpfulness (Liu et al., 2025; Kovács, 2025) | Không tách theo khía cạnh; outcome nằm ngoài RQ của đề tài. |

**Trạng thái chốt:** chưa có công thức nào được chọn. Ba ứng viên của RQ2/RQ3 — *3×3 Polarity Matrix* · $z(r)-z(s)$ · *Signed Aspect Discrepancy* $r^*-s_a^*$ — do validation study quyết định theo `RDR-0004` mục 3.2. Round 4 xác nhận chưa tìm thấy tiền lệ cho thước đo **có dấu ở cấp khía cạnh** (kết luận "chưa tìm thấy", không phải "chưa ai làm").

---

## 5. Quản trị Dự án & Chuẩn mực Học thuật (Governance & Rules)

| Khái niệm / Viết tắt | Ý nghĩa | Quy định áp dụng trong Repo |
| :--- | :--- | :--- |
| **RDR (Research Decision Record)** | Bản ghi Quyết định Nghiên cứu: Lưu trữ các quyết định kiến trúc và phương pháp luận bất biến. | Hoạt động theo nguyên tắc Append-only tại `docs/decisions/`. Quyết định có số hiệu lớn nhất là Single Source of Truth. |
| **SSOT (Single Source of Truth)** | Nguồn sự thật tối cao: Tài liệu duy nhất được quyền xác định trạng thái và quy chuẩn của dự án. | Không suy diễn ngoài SSOT; tránh tình trạng các file nháp mâu thuẫn với quyết định chính thức. |
| **Line Budget Rule** | Quy tắc ngân sách dòng: Quy định độ dài tối đa cho từng loại file tài liệu. | Context files $\le 200$ dòng; `STATUS.md` $\le 40$ dòng (để bảo vệ context window của Agent). |
| **Survey Endpoint** | Điểm dừng khảo sát văn hiến: Tiêu chuẩn xác định khi nào dừng đọc tài liệu để chuyển sang làm thực nghiệm. | Quy định tại `RDR-0001` gồm 4 tiêu chuẩn: Bão hòa, Quy mô 10-15 core papers, Đủ biến proposal, Có baseline đối chuẩn. |
| **Latest-First Window** | Cửa sổ quét tài liệu mới nhất: Ưu tiên tài liệu trong vòng 36 tháng gần nhất (2023–2026). | Quy định tại `RDR-0002` nhằm đảm bảo tính cập nhật công nghệ và lý thuyết mới nhất. |
| **Saturation** | Điểm bão hòa học thuật: Trạng thái khi đọc thêm 3–5 bài mới liên tiếp mà không phát sinh thêm khái niệm, cơ chế hay biến số mới. | Tiêu chí định tính để nghiệm thu giai đoạn khảo sát văn hiến. |
| **CoRe (Customer Online Rating)** | **Biến nhị phân đại diện cho đánh giá cao:** Thường quy ước $\text{CoRe} = 1$ nếu Rating $\ge 4$ sao, ngược lại bằng 0. | Kế thừa từ bài báo gốc Le et al. (2026). |
| **Evidence Level (I–VII)** | **Thang mức bằng chứng:** I = systematic review/meta-analysis · II = thí nghiệm ngẫu nhiên · III = đối chứng không ngẫu nhiên · IV = quan sát quy mô lớn · V = systematic review mô tả · VI = mô tả/định tính đơn lẻ · VII = ý kiến chuyên gia. | Bắt buộc gắn mức cho mọi nguồn vào evidence matrix (định nghĩa tại Round 4 mục 1.4). |

**Trạng thái quyết định (2026-09-23):** `RDR-0004` đã chốt RQ3. `RDR-0005` đang ở dạng **đề xuất, chưa ban hành** — nội dung dự kiến: miễn tiêu chí bão hòa của `RDR-0001` kèm lý do, định nghĩa lại ba cụm tài liệu, đóng băng core set và khóa khung lý thuyết (log `0006` mục 6–7).
