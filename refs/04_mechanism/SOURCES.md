# Nguồn — 04_mechanism

> **TỆP NGUỒN — sửa tay ở đây.** `INDEX.md` cùng thư mục là bản chụp của tệp này; sửa ở đây rồi cập nhật `INDEX.md` bằng tay cho khớp (script sinh đã gỡ khỏi repo).
>
> Mỗi nguồn là một mục `## `. Các trường là dòng `- khoá: giá trị`. Phần chữ còn lại
> trong mục được chuyển nguyên vào `INDEX.md`. Các khoá đang dùng: `id`, `file`, `cite`,
> `doi`, `year`, `status`, `evidence_level`, `recency`, `pillars`, `round`, `code`,
> `owner`, `updated`, `role`, `keep_reason`, `note`.

## Regitz et al. (2026)

- id: 2026_regitz_kano_quality_features
- file: A1_regitz_kano_quality_features_reviews.pdf
- cite: Regitz, D., Höpken, W., & Fuchs, M. (2026). Online customer feedback for identifying KANO product quality features: A fine-grained topic detection and sentiment analysis approach. Information Technology & Tourism, 28(1), Article 20.
- doi: 10.1007/s40558-025-00354-y
- year: 2026
- status: full_text
- evidence_level: IV
- recency: in_window
- pillars: P2
- round: 4
- code: A1
- updated: 2026-09-23
- role: Phân loại Kano trực tiếp từ review bằng hồi quy cảm xúc dương/âm theo topic
- keep_reason: Gần nhu cầu của đề tài nhất — nhưng cũng là ranh giới tính mới mỏng nhất
- note: room quality = Must-Be; connectivity = Attractive. Khác đơn vị phân tích — hệ số hồi quy theo topic, không phải review có nhãn người gán.

Vừa là nền tảng cho phần phân loại vai trò khía cạnh, vừa là **giới hạn đối với tuyên bố tính mới** của đề tài. Bài này làm gần đúng việc đề tài dự định làm; khác biệt còn lại chỉ là thước đo có dấu ở cấp khía cạnh thay vì hệ số hồi quy theo topic, và đơn vị phân tích là review có nhãn người gán. Khác biệt thật nhưng **không lớn** — phải nói rõ trong phần đóng góp.

## Öztürk (2026)

- id: 2026_ozturk_aspect_sentiment_high_utility_rules
- file: 2026_ozturk_aspect_sentiment_high_utility_rules.pdf
- cite: Öztürk, A. C. (2026). Discovering aspect–sentiment drivers of hotel review ratings with interpretable high-utility rules. IEEE Access, 14, 39496–39511.
- doi: 10.1109/access.2026.3672490
- year: 2026
- status: full_text
- evidence_level: IV
- recency: in_window
- pillars: P2
- round: 3
- updated: 2026-09-23
- role: Luật khía cạnh–cảm xúc hữu ích cao theo từng mức điểm
- keep_reason: Mô tả trực tiếp các mẫu bù trừ đa khía cạnh mà không cần mô hình hộp đen
- note: 11.275 review TripAdvisor của 14 khách sạn 5 sao.

Tham chiếu cho hướng phân tích dễ diễn giải ở cấp khía cạnh, và là nguồn cho tầng giải thích của ứng dụng. Mức điểm thấp gắn với đồng xuất hiện của nhiều khía cạnh tiêu cực; mức trung bình gắn với bù trừ; mức cao gắn với nhiều khía cạnh tích cực. **Giới hạn:** chỉ 14 khách sạn 5 sao, không đại diện cho phân bố hạng sao của dữ liệu dự án.

## Li et al. (2025)

- id: 2025_li_bertopic_three_factor_prca
- file: 2025_li_bertopic_three_factor_prca.pdf
- cite: Li, J., Lee, B., & Kim, J. (2025). Analyzing factors affecting overall customer satisfaction using hotel ratings and reviews with BERTopic and three-factor theory. SAGE Open, 15(3).
- doi: 10.1177/21582440251335169
- year: 2025
- status: full_text
- evidence_level: IV
- recency: in_window
- pillars: P2, P4
- round: 4
- code: A3_D4
- updated: 2026-09-23
- role: BERTopic + PRCA — thuộc tính lõi giữ tác động gần đối xứng giữa các hạng sao
- keep_reason: Vừa ủng hộ vừa phản biện — bất đối xứng phụ thuộc bối cảnh, không phải quy luật toàn cục
- note: Hai nhóm quét độc lập cùng tìm ra bài này (A3 và D4) — đếm một lần, dùng ở cả hai vai trò.

Nguồn **hai vai**. Ở vai ủng hộ, nó củng cố hướng phân loại thuộc tính theo ba nhân tố. Ở vai phản biện, nó là bằng chứng cụ thể rằng thuộc tính lõi không penalty-dominant trên mọi hạng sao. Hệ quả: không được viết "penalty luôn thắng" — khung đúng là hai nhánh **có điều kiện**.

## Sharma et al. (2025)

- id: 2025_sharma_review_sentiment_garden
- file: 2025_sharma_review_sentiment_garden_accepted_manuscript.pdf
- cite: Sharma, A., Shin, S., Nicolau, J. L., & Park, S. (2025). The review sentiment garden: Blossoming loss aversion and diminishing sensitivity across time and crisis. International Journal of Hospitality Management, 129, 104170.
- doi: 10.1016/j.ijhm.2025.104170
- year: 2025
- status: accepted_manuscript
- evidence_level: IV
- recency: in_window
- pillars: P2
- round: 3
- updated: 2026-09-23
- role: Lý thuyết triển vọng — loss aversion, diminishing sensitivity, reference point
- keep_reason: Lý giải nhánh chi phối mà không cần gán trạng thái tâm lý cho người viết
- note: 416.756 review TripAdvisor, 375 khách sạn, 14 thành phố châu Âu. Bản local là accepted manuscript, KHÔNG phải version of record.

Một trong bốn lớp của khung lý thuyết đã khóa trong `RDR-0005`. Các sai lệch âm tạo tác động mạnh hơn sai lệch dương tương đương, và tác động biên không tuyến tính. Cho phép giải thích chiều bị dìm điểm bằng *loss dominance* thay vì suy diễn cảm xúc.

## Zhang et al. (2025)

- id: 2025_zhang_indoor_environment_ratings
- file: 2025_zhang_indoor_environment_ratings.pdf
- cite: Zhang, F., Seshadri, K., Liu, S., & Santamouris, M. (2025). The impact of indoor environmental quality on tourist accommodation ratings using guest reviews. Building and Environment, 280, 113135.
- doi: 10.1016/j.buildenv.2025.113135
- year: 2025
- status: full_text
- evidence_level: IV
- recency: in_window
- pillars: P2
- round: 4
- code: A4
- updated: 2026-09-23
- role: Thuộc tính môi trường trong nhà là Basic / penalty-dominant trên quy mô lớn
- keep_reason: Bằng chứng penalty-dominant từ dữ liệu quan sát, không dùng bảng hỏi
- note: Hơn 540.000 review. Dữ liệu vật lý (sạch sẽ, không khí, âm thanh), không phải cảm nhận tự khai.

Củng cố nhánh penalty-dominant ở cấp thuộc tính vật lý, với quy mô lớn nhất trong nhóm A. Dùng đúng cách: đây là bằng chứng cho **hướng** của hiệu ứng, không phải cho danh tính từng khía cạnh trong dữ liệu dự án — danh tính khía cạnh vẫn phải coi là kết quả khám phá.

## Li et al. (2024)

- id: 2024_li_two_stage_satisfaction_decision_model
- file: 2024_li_two_stage_satisfaction_decision_model.pdf
- cite: Li, S., Zhu, B., Zhang, Y., Liu, F., & Yu, Z. (2024). A two-stage nonlinear user satisfaction decision model based on online review mining: Considering non-compensatory and compensatory stages. Journal of Theoretical and Applied Electronic Commerce Research, 19(1), 272–296.
- doi: 10.3390/jtaer19010015
- year: 2024
- status: full_text
- evidence_level: VI
- recency: in_window
- pillars: P2
- round: 3
- updated: 2026-09-23
- role: Cấu trúc quyết định hai giai đoạn — không bù trừ trước, bù trừ sau
- keep_reason: Cấu trúc toán học rõ nhất cho cơ chế hai nhánh của RQ3
- note: Khác domain (review sản phẩm) nên chỉ dùng làm supporting method, không dùng làm bằng chứng hospitality.

Khuôn khổ cho mô hình hành vi ở Stage 5 — thuộc tính cơ bản được xét ở giai đoạn không bù trừ, các thuộc tính còn lại mới vào giai đoạn bù trừ. **Giới hạn khi trích:** đơn vị phân tích là review sản phẩm, không phải khách sạn; phải ghi rõ khi dùng làm căn cứ phương pháp.

## Wang et al. (2024)

- id: 2024_wang_attribute_performance_satisfaction
- file: 2024_wang_attribute_performance_satisfaction.pdf
- cite: Wang, J., Wu, J., Sun, S., & Wang, S. (2024). The relationship between attribute performance and customer satisfaction: An interpretable machine learning approach. Data Science and Management, 7(3), 164–180.
- doi: 10.1016/j.dsm.2024.01.003
- year: 2024
- status: full_text
- evidence_level: IV
- recency: in_window
- pillars: P2
- round: 3
- updated: 2026-09-23
- role: Quan hệ thuộc tính–hài lòng là phi tuyến, bất đối xứng và thay đổi theo thời gian
- keep_reason: Chặn việc mô hình hóa mọi khía cạnh bằng một hệ số tuyến tính đối xứng
- note: XGBoost + SHAP trên attribute ratings của khách sạn New York.

Biện minh cho việc không dùng một mô hình tuyến tính duy nhất cho mọi khía cạnh; hỗ trợ hướng phân tích penalty/reward riêng theo từng khía cạnh. Điểm mấu chốt: hiệu ứng bất đối xứng **thay đổi theo thời gian**, nên mọi kết luận phải gắn với khung thời gian của dữ liệu.
