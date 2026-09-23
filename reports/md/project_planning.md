# PROJECT PLANNING

**TRƯỜNG ĐẠI HỌC FPT TP.HCM — BỘ MÔN CF**

**Môn DAP391m (AI & Data Science with Python & SQL), học kỳ Fall 2026**

Nộp trên LMS trong tuần 1; chiếm 10% điểm môn học, trong đó 3 điểm cho phần AI Audit Log & Reflection.

---

## 1. THÔNG TIN NHÓM

***Bảng 1.** Thông tin lớp, giảng viên và thành viên nhóm*

| **Mục** | **Nội dung** |
| --- | --- |
| Lớp | [điền] |
| Giảng viên phụ trách | [điền] |
| Tên nhóm (nếu có) | [điền] |
| Nhóm trưởng (họ tên, MSSV, email) | [điền] |
| Thành viên 2 (họ tên, MSSV, email) | [điền] |
| Thành viên 3 (họ tên, MSSV, email) | [điền] |
| Kênh liên lạc nhóm (Zalo, Teams, GitHub) | GitHub: `diepsang13z/sriprj` · Zalo/Teams: [điền] |

---

## 2. ĐỀ TÀI VÀ BỘ DỮ LIỆU

Đề tài thuộc dạng **đề xuất riêng** (ngoài danh sách 12 chủ đề gợi ý), cùng dạng bài toán với các đề tài trong file `DAP391m_Project_PBL_RBL_ResearchQuestion.xlsx`.

***Bảng 2.** Đề tài và mô tả bộ dữ liệu*

| **Mục** | **Nội dung** |
| --- | --- |
| Số thứ tự và tên đề tài | Đề xuất riêng — **Bất nhất cảm xúc – điểm số ở cấp khía cạnh trong review khách sạn** (*Aspect-Level Sentiment–Rating Discrepancy in Online Hotel Reviews*) |
| Bài toán (phân loại, hồi quy, dự báo chuỗi thời gian, phát hiện bất thường) | **Phân loại đa lớp** (dự đoán mức điểm 1–5 từ văn bản) + **phát hiện bất thường** (nhận diện review bất nhất giữa văn bản và điểm sao) + **mô hình giải thích dạng hồi quy thứ tự** cho quan hệ khía cạnh → điểm |
| Tên bộ dữ liệu | `TripAdvisor_EN.json` — corpus review khách sạn tiếng Anh đã gán nhãn khía cạnh và cảm xúc ở cấp span |
| Nguồn công bố và link gốc | Kế thừa tập gán nhãn chuyên gia của Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026), *IJHM*, 134, 104574. File local: `data/TripAdvisor_EN.json` (41,1 MB). Link bài báo (DOI): `10.1016/j.ijhm.2026.104574` · Repo mà bài báo công bố: `github.com/Hanhlevna/Manhos` (kiểm 2026-09-23: chỉ có `data_Booking.com.csv`, **không chứa tệp TripAdvisor**). Bản nhóm dùng do **giảng viên môn học cung cấp**, định danh bằng SHA-256 ghi ở `README.md` |
| Bài báo mô tả bộ dữ liệu (tác giả, năm, nơi công bố) | Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026). *Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings*. International Journal of Hospitality Management, 134, 104574 |
| Giấy phép sử dụng | **Giảng viên môn học cung cấp** cho nhóm; nhóm có quyền sử dụng trong phạm vi môn DAP391m (chốt 2026-09-23). Khi nộp báo cáo, ghi nguồn theo dòng này kèm checksum SHA-256 ở `README.md` |
| Quy mô: số dòng, số cột, khoảng thời gian | 9.990 review · 2.622 khách sạn · 50 địa điểm · 2015–2023. JSON gồm `annotations` (54.326 span khía cạnh `entities`, 54.272 span cảm xúc `entity_sentiment`) và `meta_info` |
| Biến mục tiêu (target) và các nhóm biến đầu vào | Target: `score` (thang 1–5). Đầu vào: (1) văn bản review; (2) span khía cạnh `entities` — Facility, Amenity, Service, Experience, Loyalty, Branding; (3) span cảm xúc `entity_sentiment` — Positive, Negative, Neutral; (4) metadata `star`, `year`, `month`, `location`, `hotel name`/`id_url` |
| Lý do chọn bộ dữ liệu này | Đã nằm trong repo, không phải chờ thu thập; nhãn đã được chuyên gia gán ở cấp span (không phải nhãn yếu sinh từ điểm sao); có bối cảnh Việt Nam khớp bài báo gốc; đủ lớn cho cả nhánh đo lường và nhánh dự báo; có sẵn cấu trúc `start`/`end` để liên kết span khía cạnh với span cảm xúc và để tô sáng giải thích trong ứng dụng |
| Dữ liệu bổ sung dự kiến (nếu có) | Không. Nhóm **không** mở rộng lên corpus 782.584 review của bài báo gốc; mọi tuyên bố về tỷ lệ phải ghi đúng phạm vi TripAdvisor 2015–2023 |

**Đặc tả đã xác minh trực tiếp trên file** (dùng cho Data Dictionary ở Bước 2):

| Thuộc tính | Giá trị |
| --- | --- |
| Phân bố điểm | 1★ 228 · 2★ 237 · 3★ 601 · 4★ 1.776 · 5★ 7.148 (71,6%) |
| Span khía cạnh | Service 19.289 · Facility 12.641 · Experience 9.113 · Amenity 7.651 · Loyalty 4.293 · Branding 1.339 |
| Span cảm xúc | Positive 46.772 · Negative 4.508 · Neutral 2.992 |
| Review 5★ chứa ≥1 span `Negative` gắn khía cạnh (theo `RDR-0006`) | 394 review |
| Review 1–2★ chứa ≥1 span `Positive` | 199 review (trên tổng 465 review 1–2★) |
| Tổng ca đáng ngờ | 593 review, trải trên 461 khách sạn |
| Nhóm có sẵn cho gán nhãn tay | 394 + 199 ca đáng ngờ · aligned controls 5★ 6.754 review (không có span `Negative` gắn khía cạnh, theo `RDR-0006`) · aligned controls 1–2★ 266 review |

---

## 3. BA CÂU HỎI NGHIÊN CỨU

***Bảng 3.** Câu hỏi nghiên cứu, cách đo và bước trả lời*

| **STT** | **Câu hỏi nghiên cứu** | **Biến đầu vào và biến mục tiêu** | **Metric** | **Bước trả lời** |
| --- | --- | --- | --- | --- |
| RQ1 | Hiện tượng bất nhất giữa nội dung review và điểm sao xuất hiện với tần suất bao nhiêu trong tập dữ liệu, và gồm những dạng có hướng nào khi điểm sao cao hơn hoặc thấp hơn mức nội dung văn bản gợi ý? | Đầu vào: span khía cạnh + span cảm xúc + `score`. Mục tiêu: nhãn tình trạng tương thích (`aligned`, `mixed-but-consistent`, `upward discrepancy`, `downward discrepancy`) trên tập gán nhãn tay | Tỷ lệ phần trăm theo từng nhóm (kèm khoảng tin cậy), phân bố theo dạng lệch, false-positive rate trên nhóm aligned controls | B1–B3 |
| RQ2 | Làm thế nào để lượng hóa độ bất nhất này theo từng khía cạnh dịch vụ mà giữ được đồng thời độ lớn (magnitude) và chiều (direction)? | Đầu vào: điểm sao đã chuẩn hóa và tín hiệu cảm xúc cấp khía cạnh từ mô hình cảm xúc độc lập với điểm sao. Mục tiêu: điểm bất nhất có dấu $D_{i,a}$ theo từng khía cạnh | Macro-F1 và confusion matrix so với nhãn do người gán (không dùng accuracy); độ ổn định của dấu giữa hai nhóm điểm cao và điểm thấp; số lượng tính toán được ở cấp khía cạnh | B3–B4 (kèm validation study) |
| RQ3 | Cảm xúc tích cực và tiêu cực trên nhiều khía cạnh khách sạn kết hợp bất đối xứng như thế nào để quyết định chiều hướng và độ lớn của bất nhất cảm xúc – điểm số? | Đầu vào: cấu hình positive/negative theo khía cạnh, `Severity` (Minor/Major), `Service_Recovery` (Yes/No), hạng sao khách sạn. Mục tiêu: $D_{i,a}$ và `score` | Hệ số và độ phù hợp của mô hình hồi quy thứ tự/có trọng số; planned contrast `positive Service × negative Facility`; kiểm định ổn định giữa các nhóm hạng sao | B4–B6 |

**Khoảng trống mà bài baseline chưa giải quyết (điều kiện của RQ3):** mô hình của Le et al. (2026) giả định quan hệ đơn điệu giữa cảm xúc khía cạnh và điểm số, đồng thời dùng biến `Loyalty` — vốn được định nghĩa bằng chính các câu nói về ý định hành vi — để giải thích cho điểm số, tạo lập luận vòng. Baseline cũng không có phép đo nào giữ đồng thời độ lớn và chiều ở cấp khía cạnh. RQ3 nằm đúng vào khoảng trống đó.

**RQ3 đã chốt chính thức** trong quyết định `RDR-0004`; khung lý thuyết (S-O-R + Kano/three-factor + Prospect Theory) và phạm vi dữ liệu đã khóa trong `RDR-0005`. RQ1 và RQ2 giữ ở dạng nháp cho tới khi hoàn tất validation study.

**Ba RQ mở rộng sẽ đặt ở tuần 6** (nhánh dự báo, phục vụ Bước 5 của môn):

- **RQ4** — Năm mô hình dự đoán mức điểm từ văn bản đạt macro-F1 bao nhiêu, và mô hình học sâu vượt baseline cổ điển bao nhiêu điểm khi chia tập theo khách sạn thay vì chia ngẫu nhiên?
- **RQ5** — Phần dư `score − score_dự_báo` phân bố thế nào giữa hai phía điểm, và có ổn định giữa các mức sao không?
- **RQ6** — Có dự đoán được review nào rơi vào nhóm bị dìm điểm ($D < 0$) từ đặc trưng khía cạnh và severity không?

---

## 4. PAPER BASELINE

***Bảng 4.** Ba paper baseline và kết quả sẽ so sánh*

| **STT** | **Tác giả, năm, tên bài, nơi công bố** | **Dữ liệu và mô hình trong bài** | **Kết quả sẽ so sánh** | **Trạng thái đọc** |
| --- | --- | --- | --- | --- |
| 1 | Le, H. T. M., Nguyen, T. Q., & Nguyen, B. T. (2026). *Unlocking insights into customer sentiment analysis: Impact of loyalty on online hotel ratings*. International Journal of Hospitality Management, 134, 104574 | Hơn 1,3 triệu review (Booking.com, TripAdvisor); BERTopic → SentenceBERT + c-TF-IDF → VADER → Weighted Multinomial Logistic Regression; 5 khía cạnh | McFadden pseudo $R^2$ = 0,4617 (Booking) và 0,5898 (TripAdvisor); hệ số `FacilityNegative` (−1,0778 / −1,1661); dùng làm đối chuẩn cho quan hệ khía cạnh → điểm và làm mốc phản biện tính vòng của `Loyalty` | Đã đọc kỹ (toàn văn dạng markdown). Chưa chạy thử — tái lập ở Bước 5 |
| 2 | Kwon, B., Lee, J., Min, J., Kwak, C., & Choi, H. S. (2025). *Beyond the stars: The impact of rating-text inconsistency on perceived review usefulness*. Asia Pacific Journal of Information Systems, 35(1), 49–72 | Review sản phẩm; tách **degree** $D=\lvert z(rating)-z(sentiment)\rvert$ khỏi **direction**; outcome là perceived usefulness | Định nghĩa degree/direction để đối chiếu với công thức của nhóm; cho thấy tách hai khái niệm này là cần thiết, nhưng bài không ở cấp khía cạnh và không thuộc hospitality | Đã đọc kỹ (local PDF). Chưa chạy thử |
| 3 | You, X.-Y., Chang, S.-C., Hung, S.-M., Ku, C.-H., & Chang, Y.-C. (2024). *Using multitask learning with pre-trained language models for aspect-based sentiment analysis in the hospitality industry*. PACLIC 2024, 131–140 | ABSA đa nhiệm trên 8 khía cạnh hospitality bằng mô hình ngôn ngữ tiền huấn luyện | Mốc so kỹ thuật: RoBERTa đa nhiệm AUROC 0,9214 · AUPRC 0,6152 · F1 0,5817; so XGBoost 0,4938 và LSTM-attention 0,4208 — dùng làm ngưỡng tham chiếu cho Bước 5 | Đã đọc kỹ (local PDF). Chưa chạy thử |

Ba paper này sẽ được trích dẫn lại trong Research Proposal (tuần 3) và Final Report. Một nguồn bổ trợ đã có toàn văn và sẽ dùng khi viết Methodology: Ameur, Hamdi & Ben Yahia (2024), *ACM Computing Surveys* — systematic literature review về sentiment analysis cho review khách sạn.

---

## 5. KẾ HOẠCH THỰC HIỆN THEO TUẦN

***Bảng 5.** Kế hoạch 10 tuần theo lộ trình môn học*

| **Tuần** | **Hoạt động chung theo lộ trình** | **Việc của nhóm** | **Người phụ trách** | **Sản phẩm** |
| --- | --- | --- | --- | --- |
| 1 | Lập nhóm, chọn đề tài, Bước 1 và 2, nộp Project Planning | Chốt đề tài, 3 RQ và 3 paper baseline; kiểm kê file dữ liệu và đối chiếu với bài báo mô tả; dựng Data Dictionary cho JSON (phân biệt `annotations` với `drafts`, `score` với `meta_info.star`); ghi 3 prompt đầu tiên vào Audit Log | Nhóm trưởng + cả nhóm | Project Planning; Data Dictionary; 3 prompt Audit Log |
| 2 | Bước 3, đọc 3 paper baseline, phác thảo Research Proposal | Bước 2–3: làm sạch và kiểm tra toàn vẹn liên kết `start`/`end` giữa span khía cạnh và span cảm xúc; viết bộ truy vấn SQL nâng cao (window function/CTE) cho tỷ lệ review lệch theo khách sạn và xếp hạng khách sạn; 3 biểu đồ nâng cao đầu tiên | Data & EDA Lead | Notebook EDA; bộ truy vấn SQL; chốt dataset (không đổi sau tuần này) |
| 3 | Bước 4 và 5, nộp Research Proposal | Bước 5: chạy 3 mô hình cổ điển (TF-IDF + Logistic Regression, TF-IDF + SVM, LightGBM) với chia tập theo khách sạn; khởi tạo BiLSTM và DeBERTa; Bước 4: dựng endpoint dự báo đầu tiên | Modelling Lead + Viz & App Lead | Research Proposal; bảng metric sơ bộ; endpoint draft |
| 4 | Bước 6, LaTeX draft | Bước 6: dựng khung ứng dụng "Bảng soát điểm sao"; nối endpoint mô hình; dựng dashboard tương tác; **làm cảnh báo thật (SNS/email) vì không thể mock**; bắt đầu bản thảo LaTeX | Viz & App Lead | Ứng dụng chạy được; bản thảo LaTeX; sơ đồ kiến trúc |
| 5 | Review 1, Audit Log đợt 1 | Hoàn tất 5 mô hình kèm tuning và cross-validation; so baseline; chuẩn bị demo; rà soát Audit Log cá nhân | Modelling Lead + cả nhóm | Bản Review 1; Audit Log đợt 1; bảng metric 5 mô hình |
| 6 | RQ mới, làm lại 6 bước | Chốt RQ4–RQ6; bắt đầu validation study: dựng evaluation set 600–800 mẫu (394 + 199 ca đáng ngờ + aligned controls), hai người gán nhãn độc lập trên calibration subset | Research & Report Lead + Data & EDA Lead | RQ4–RQ6; evaluation set bản đầu; kết quả calibration |
| 7 | Review 2, Audit Log đợt 2, viết Methodology, Discussion | Đo mức đồng thuận (Cohen's Kappa ≥ 0,70), giải quyết bất đồng, mở rộng gán nhãn; so sánh ba công thức đo bất nhất và chốt measure; chạy mô hình kinh tế lượng; tích hợp hỏi đáp (Lex/Transcribe) | Research & Report Lead + Modelling Lead | Methodology và Discussion; measure đã chốt; Audit Log đợt 2 |
| 8 | Kiểm tra code, ứng dụng, paper; viết Abstract, Introduction | Chạy lại toàn bộ pipeline end-to-end với seed cố định; rà checklist chống rò rỉ dữ liệu; hoàn thiện Abstract, Introduction, Reflection; kiểm tra app gắn kết quả mô hình | Cả nhóm | Bản thảo gần cuối; ứng dụng ổn định; checklist rò rỉ |
| 9 | Review 3, Audit Log đợt 3, nộp Final Report và Slide | Rà trích dẫn thật cho mọi nguồn; mỗi hình và bảng có chú giải; lập bảng RQ → quyết định; nộp Final Report và Slide | Cả nhóm | Final Report; slide 22 trang; Audit Log đợt 3 |
| 10 | Trình bày, demo, Q&A, chấm hội đồng | Luyện demo theo kịch bản vấn đáp; phân vai trả lời; chuẩn bị trước các câu hỏi phản biện về thiên lệch đo lường, thiên lệch nền tảng và lỗi phân loại Kano | Cả nhóm | Buổi demo và Q&A |

---

## 6. PHÂN CÔNG VÀ SẢN PHẨM BÀN GIAO

***Bảng 6.** Phân công theo bước dự án*

| **Bước dự án** | **Người thực hiện chính** | **Người kiểm tra chéo** | **Sản phẩm bàn giao** |
| --- | --- | --- | --- |
| Bước 1: Business Understanding, Data Collection | Data & EDA Lead | Research & Report Lead | Problem Statement; 6 RQ; Data Dictionary; 3 paper baseline |
| Bước 2: Data Preparation, SQL nâng cao | Data & EDA Lead | Modelling Lead | Notebook làm sạch (ghi số dòng trước/sau); bộ truy vấn SQL có CTE/window function |
| Bước 3: Data Visualization in advanced | Viz & App Lead | Data & EDA Lead | ≥3 biểu đồ nâng cao (Sankey, heatmap khía cạnh × mức sao, choropleth 50 địa điểm); dashboard tương tác |
| Bước 4: Integrating Services API | Viz & App Lead | Modelling Lead | Endpoint dự báo; một cảnh báo thật đã nhận; kênh hỏi đáp; sơ đồ kiến trúc |
| Bước 5: Build model for prediction (ít nhất 5 model) | Modelling Lead | Data & EDA Lead | Bảng metric 5 mô hình so baseline (macro-F1, PR-AUC); log tuning trước/sau; cross-validation |
| Bước 6: Develop applications and AI powered solutions | Viz & App Lead + cả nhóm | Nhóm trưởng | Ứng dụng demo được; bảng RQ → quyết định; hạn chế và hướng phát triển |

**Sản phẩm bàn giao cuối kỳ:** notebook và mã nguồn (kho GitHub `diepsang13z/sriprj`), ứng dụng có tích hợp AI services, Final Report 10–12 trang theo LaTeX Springer 1 cột, slide theo template `DAP391m_Slide_Presentation_Final_Sample`, và file AI Audit Log riêng của từng thành viên.

**Ứng dụng đã chốt: "Bảng soát điểm sao".** Tách *điểm khách bấm* khỏi *điểm mà nội dung review biện minh*, phục vụ quản lý vận hành và revenue manager. Bốn khối chức năng: tra một review; tô sáng span tích cực/tiêu cực theo khía cạnh; kết luận lệch có dấu $D$; hàng đợi cảnh báo kèm hỏi đáp. **Không dùng biểu đồ radar** — 46/76 khách sạn có độ trải hồ sơ dưới 0,3 nên hình gần tròn và không mang thông tin; thay bằng cột lệch, heatmap và Sankey.

---

## 7. KẾ HOẠCH SỬ DỤNG AI VÀ AUDIT LOG

Mỗi thành viên nộp một file `AI_AuditLog_Template.xlsx` riêng theo ba đợt (tuần 5, 7, 9), đạt 15–20 core prompt và phát hiện ít nhất 3 hallucination. Ngay trong tuần 1, mỗi thành viên ghi ít nhất 3 prompt đầu tiên.

***Bảng 7.** Việc dự kiến dùng AI và cách kiểm chứng*

| **Việc dự kiến dùng AI** | **Công cụ AI** | **Cách kiểm chứng (Human Delta)** | **Thành viên phụ trách** |
| --- | --- | --- | --- |
| Brainstorm problem statement và RQ | Trợ lý AI hội thoại | Đối chiếu RQ3 với quyết định đã khóa trong `docs/decisions/`; kiểm tra câu chữ không suy diễn trạng thái tâm lý từ điểm sao; kiểm tra RQ có đo được bằng chính dữ liệu hiện có | [điền] |
| Viết SQL và code Python | Trợ lý sinh mã | Chạy lại trên máy, ghi số dòng trước/sau mỗi thao tác, kiểm tra thủ công một mẫu ngẫu nhiên, đối chiếu với Data Dictionary | [điền] |
| Tạo biểu đồ và diễn giải | Trợ lý AI hội thoại | Kiểm bằng dữ liệu gốc; mỗi hình phải rút ra một insight gắn RQ; loại biểu đồ phải nằm trong danh sách CLO4 của môn | [điền] |
| Huấn luyện và so sánh mô hình | Trợ lý sinh mã | Đối chiếu tham số với tài liệu chính thức của thư viện; xác nhận cross-validation chạy đúng; kiểm tra không dùng điểm sao để huấn luyện mô hình cảm xúc | [điền] |
| Viết LaTeX và tài liệu | Trợ lý soạn thảo | Kiểm tra mọi trích dẫn có thật bằng DOI/trang nhà xuất bản; đối chiếu số liệu trong báo cáo với kết quả chạy lại từ notebook | [điền] |

**Nguyên tắc kiểm chứng bắt buộc của nhóm:** mọi con số xuất hiện trong báo cáo phải chạy lại được từ notebook với seed cố định; mọi trích dẫn phải đối chiếu với bản gốc; mọi gợi ý của AI về phương pháp phải được đối chiếu với tài liệu tham khảo đã có toàn văn trong `refs/`.

---

## 8. RỦI RO VÀ PHƯƠNG ÁN DỰ PHÒNG

***Bảng 8.** Rủi ro dự kiến và cách xử lý*

| **Rủi ro** | **Mức độ** | **Phương án dự phòng** | **Người theo dõi** |
| --- | --- | --- | --- |
| Dữ liệu tải về không đúng mô tả hoặc quá lớn | Thấp | File 41,1 MB đã kiểm chứng: 9.990 review, khớp bài báo mô tả. Nếu file hỏng, dùng lại bản đã đối chiếu và ghi rõ trong báo cáo | Data & EDA Lead |
| Không tái tạo được kết quả của paper baseline | Trung bình | Ghi rõ là không tái lập và dùng số công bố làm mốc tham chiếu; nếu vẫn thiếu, chuyển sang baseline kỹ thuật của You et al. (2024) cho phần ABSA | Modelling Lead |
| Thành viên bận hoặc rút khỏi nhóm | Trung bình | Mỗi bước có người thực hiện chính và người kiểm tra chéo; toàn bộ quy trình phải chạy lại được từ notebook, không phụ thuộc kiến thức cá nhân | Nhóm trưởng |
| Kết quả mô hình không vượt baseline | Trung bình | Báo cáo trung thực kèm phân tích lỗi và bảng metric đầy đủ; mô hình tốt nhất được in đậm, không che giấu kết quả kém | Modelling Lead |
| **Lệch lớp cực nặng** — 5★ chiếm 71,6% tập dữ liệu | Cao | Không báo accuracy; dùng macro-F1 và PR-AUC; dùng class weight hoặc oversampling **chỉ trên tập train** | Modelling Lead |
| **Rò rỉ dữ liệu theo khách sạn** — 2.622 khách sạn, cao nhất 85 review/khách sạn | Cao | Chia tập theo `hotel name`/`id_url` (GroupShuffleSplit), không chia ngẫu nhiên | Data & EDA Lead |
| **Rò rỉ nhãn qua span `Branding`** — 1.339 span khách tự viết số sao | Cao | Loại toàn bộ span `Branding` khỏi mọi đặc trưng dự đoán trước khi huấn luyện | Data & EDA Lead |
| **Công thức đo bất nhất chưa chốt** cho tới sau tuần 6 | Cao | Nhánh dự báo (Bước 5) không phụ thuộc quyết định này nên chạy song song; phần hiển thị $D$ chỉ ship sau khi chốt; phương án dự phòng là giữ ma trận phân cực có hướng làm baseline | Research & Report Lead |
| **Mất cân bằng hai chiều bất nhất** — 394 ca điểm cao có văn bản tiêu cực so với 199 ca ngược lại | Cao | Báo đúng tỷ lệ thực tế, không cân bằng nhân tạo; nếu tập đối chiếu không đủ để kết luận thì ghi rõ giới hạn thay vì suy diễn | Research & Report Lead |
| **Dịch vụ đám mây thật không mock được** (cảnh báo SNS, endpoint mô hình) | Cao | Làm cảnh báo sớm ở tuần 4; nếu hết tín dụng, dùng FastAPI cục bộ **cùng giao diện JSON**, khai rõ trong Audit Log và báo cáo, đồng thời giữ ảnh chụp/log lần gọi endpoint thật | Viz & App Lead |
| Hai người gán nhãn không thu xếp được thời gian chung | Trung bình | Chốt lịch gán nhãn từ tuần 6; calibration subset chỉ cần 30–50 mẫu nên có thể chia thành hai phiên ngắn | Data & EDA Lead |

---

## 9. TIÊU CHÍ CHẤM PROJECT PLANNING (10%)

***Bảng 9.** Tiêu chí chấm*

| **STT** | **Tiêu chí** | **Điểm** | **Phần AI Audit Log** |
| --- | --- | --- | --- |
| 1 | Thông tin nhóm, đề tài, dataset đầy đủ và có nguồn, giấy phép | 2 | |
| 2 | Ba câu hỏi nghiên cứu rõ biến, metric và bước trả lời | 2 | |
| 3 | Ba paper baseline đúng định dạng và nêu được kết quả sẽ so sánh | 1.5 | |
| 4 | Kế hoạch tuần và phân công khả thi, có người chịu trách nhiệm | 1.5 | |
| 5 | Kế hoạch dùng AI và 3 prompt đầu tiên trong Audit Log cá nhân | 3 | 3 điểm này thuộc AI Audit Log & Reflection |

---

*Tài liệu liên quan:* [`reports/md/research_proposal.md`](research_proposal.md) · [`docs/logs/brainstorm/0003_app_concept_and_course_requirements.md`](../../docs/logs/brainstorm/0003_app_concept_and_course_requirements.md) · [`refs/INDEX.md`](../../refs/INDEX.md) · [`reports/templates/DAP391m_Guide_FA26.pdf`](../templates/DAP391m_Guide_FA26.pdf)
