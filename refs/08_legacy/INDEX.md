# 08_legacy — Đã hạ ưu tiên (audit trail)

> **BẢN CHỤP CỦA `SOURCES.md` cùng thư mục.** Sửa dữ liệu ở `SOURCES.md`, không sửa trực tiếp tệp này. Script sinh đã gỡ khỏi repo nên phải cập nhật bằng tay cho khớp.

*Cập nhật: 2026-09-23 · 4 nguồn · 3 đọc được toàn văn*

| Nguồn | Năm | Mức | Trạng thái | Nhóm | Vai trò trong đề tài |
| --- | ---: | ---: | --- | --- | --- |
| **McMurry (2026)** | 2026 | VI | toàn văn | — | Pipeline transformer chuyên biệt cho review hostel |
| **Patil (2026)** | 2026 | VI | preprint (chưa phản biện) | — | Hồi quy khía cạnh → điểm; phần dư coi là sai số |
| **Topçu et al. (2026)** | 2026 | VI | toàn văn | — | Dự đoán mức điểm bằng transformer kèm random oversampling |
| **Yoruk et al. (2025)** | 2025 | V | toàn văn | — | Tổng quan 89 nghiên cứu về customer forgiveness |

## Chi tiết

### McMurry (2026)

- **Trích dẫn đầy đủ:** McMurry, I. W. (2026). Quantifying social sentiment in hostels using a domain-specific transformer pipeline. In Proceedings of WASSA 2026 (pp. 24–36).
- **Tệp:** `2026_mcmurry_hostel_social_sentiment.pdf`
- **DOI:** 10.18653/v1/2026.wassa-1.3
- **Nhóm trụ cột:** —
- **Vì sao giữ:** Loại — hội nghị, chủ đề hostel socialness, không có bất nhất điểm số

### Patil (2026)

- **Trích dẫn đầy đủ:** Patil, V., et al. (2026). Beyond the star rating: A scalable framework for aspect-based sentiment analysis using LLMs and text classification. arXiv preprint.
- **Tệp:** `2026_patil_llm_absa_beyond_stars.pdf`
- **Nhóm trụ cột:** —
- **Vì sao giữ:** Loại — preprint, domain nhà hàng, không operationalize bất nhất như tín hiệu

### Topçu et al. (2026)

- **Trích dẫn đầy đủ:** Topçu, A., Asar, M. A., & Orman, G. K. (2026). Improving hotel review rating prediction with transformer models. Sakarya University Journal of Computer and Information Sciences, 9(2), 451–464.
- **Tệp:** `2026_topcu_transformer_rating_prediction.pdf`
- **Nhóm trụ cột:** —
- **Vì sao giữ:** Loại khỏi nhánh đo lường — dùng chính điểm sao làm nhãn huấn luyện nên không tạo được tín hiệu cảm xúc độc lập
- **Ghi chú:** DOI trên trang nhà xuất bản bị lỗi nên không dùng làm định danh.

### Yoruk et al. (2025)

- **Trích dẫn đầy đủ:** Yoruk, I., Hsu, J.-H., & Lee, Z. W. Y. (2025). Consumer forgiveness: A literature review and research agenda. Psychology & Marketing, 42(2), 554–578.
- **Tệp:** `2025_yoruk_consumer_forgiveness_review.pdf`
- **DOI:** 10.1002/mar.22138
- **Nhóm trụ cột:** —
- **Vì sao giữ:** Loại khỏi lớp lý thuyết trung tâm — `RDR-0005` chốt không đo construct forgiveness
- **Ghi chú:** Chỉ được nêu trong phần văn hiến như construct liên quan nhưng cố ý không đo.
