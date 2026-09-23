# Nguồn — 08_legacy

> **TỆP NGUỒN — sửa tay ở đây.** `INDEX.md` cùng thư mục là bản chụp của tệp này; sửa ở đây rồi cập nhật `INDEX.md` bằng tay cho khớp (script sinh đã gỡ khỏi repo).
>
> Đây là **audit trail**, không phải cụm dẫn dắt lập luận. Nguồn ở đây đã bị hạ ưu tiên
> nhưng không xoá, để giữ dấu vết của các quyết định loại bỏ.

## McMurry (2026)

- id: 2026_mcmurry_hostel_social_sentiment
- file: 2026_mcmurry_hostel_social_sentiment.pdf
- cite: McMurry, I. W. (2026). Quantifying social sentiment in hostels using a domain-specific transformer pipeline. In Proceedings of WASSA 2026 (pp. 24–36).
- doi: 10.18653/v1/2026.wassa-1.3
- year: 2026
- status: full_text
- evidence_level: VI
- evidence_basis: suy_tu_thiet_ke
- recency: in_window
- pillars:
- updated: 2026-09-23
- role: Pipeline transformer chuyên biệt cho review hostel
- keep_reason: Loại — hội nghị, chủ đề hostel socialness, không có bất nhất điểm số

## Patil et al. (2026)

- id: 2026_patil_llm_absa_beyond_stars
- file: 2026_patil_llm_absa_beyond_stars.pdf
- cite: Patil, V., et al. (2026). Beyond the star rating: A scalable framework for aspect-based sentiment analysis using LLMs and text classification. arXiv preprint.
- year: 2026
- status: preprint
- evidence_level: VI
- evidence_basis: matrix_round_4
- recency: in_window
- pillars:
- round: 4
- code: C5
- updated: 2026-09-23
- role: Hồi quy khía cạnh → điểm; phần dư coi là sai số
- keep_reason: Loại — preprint, domain nhà hàng, không operationalize bất nhất như tín hiệu

## Topçu et al. (2026)

- id: 2026_topcu_transformer_rating_prediction
- file: 2026_topcu_transformer_rating_prediction.pdf
- cite: Topçu, A., Asar, M. A., & Orman, G. K. (2026). Improving hotel review rating prediction with transformer models. Sakarya University Journal of Computer and Information Sciences, 9(2), 451–464.
- year: 2026
- status: full_text
- evidence_level: VI
- evidence_basis: suy_tu_thiet_ke
- recency: in_window
- pillars:
- updated: 2026-09-23
- role: Dự đoán mức điểm bằng transformer kèm random oversampling
- keep_reason: Loại khỏi nhánh đo lường — dùng chính điểm sao làm nhãn huấn luyện nên không tạo được tín hiệu cảm xúc độc lập
- note: DOI trên trang nhà xuất bản bị lỗi nên không dùng làm định danh.

## Yoruk et al. (2025)

- id: 2025_yoruk_consumer_forgiveness_review
- file: 2025_yoruk_consumer_forgiveness_review.pdf
- cite: Yoruk, I., Hsu, J.-H., & Lee, Z. W. Y. (2025). Consumer forgiveness: A literature review and research agenda. Psychology & Marketing, 42(2), 554–578.
- doi: 10.1002/mar.22138
- year: 2025
- status: full_text
- evidence_level: V
- evidence_basis: suy_tu_thiet_ke
- recency: in_window
- pillars:
- updated: 2026-09-23
- role: Tổng quan 89 nghiên cứu về customer forgiveness
- keep_reason: Loại khỏi lớp lý thuyết trung tâm — `RDR-0005` chốt không đo construct forgiveness
- note: Chỉ được nêu trong phần văn hiến như construct liên quan nhưng cố ý không đo.
