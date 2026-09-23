# 07_baselines_methods — Baseline, ABSA, benchmark, công cụ giải thích

> **BẢN CHỤP CỦA `SOURCES.md` cùng thư mục.** Sửa dữ liệu ở `SOURCES.md`, không sửa trực tiếp tệp này. Script sinh đã gỡ khỏi repo nên phải cập nhật bằng tay cho khớp.

*Cập nhật: 2026-09-23 · 6 nguồn · 6 đọc được toàn văn*

| Nguồn | Năm | Mức | Trạng thái | Nhóm | Vai trò trong đề tài |
| --- | ---: | ---: | --- | --- | --- |
| **Pramono et al. (2026)** | 2026 | VI | toàn văn | P5 | Thiết kế tầng giải thích bằng SHAP và LIME, có kiểm định faithfulness |
| **Guidotti et al. (2025)** | 2025 | IV | toàn văn | P5 | LLM zero-shot cho phân loại cảm xúc và trích từ khóa; đóng khung như công cụ hỗ trợ ra quyết định |
| **Zhu (2025)** | 2025 | VI | toàn văn | P5 | ABSA đa phương thức (ảnh + chữ) |
| **Ameur et al. (2024)** | 2024 | I | toàn văn | P5 | Bản đồ kỹ thuật toàn bộ pipeline xử lý review khách sạn |
| **You et al. (2024)** | 2024 | VI | toàn văn | P5 | Mốc so kỹ thuật cho ABSA hospitality — RoBERTa đa nhiệm, 8 khía cạnh |
| **Puh et al. (2023)** | 2023 | VI | toàn văn | P5 | Baseline học máy cho dự đoán cảm xúc và điểm của review du lịch |

## Chi tiết

### Pramono et al. (2026)

- **Trích dẫn đầy đủ:** Pramono, B. A., Gernowo, R., & Sofwan, A. (2026). Explainable multilingual aspect-based sentiment analysis for tourism using SHAP and LIME. Engineering, Technology & Applied Science Research, 16(3), 37077–37084.
- **Tệp:** `E1_pramono_explainable_absa_shap_lime.pdf`
- **DOI:** 10.48084/etasr.18774
- **Nhóm trụ cột:** P5
- **Vì sao giữ:** Mẫu cho tầng giải thích của ứng dụng
- **Ghi chú:** **Cảnh báo venue** — không nằm trong DOAJ, không phải core source. Chỉ dùng cho kỹ thuật, không dùng làm bằng chứng domain.

### Guidotti et al. (2025)

- **Trích dẫn đầy đủ:** Guidotti, D., Pandolfo, L., & Pulina, L. (2025). Discovering sentiment insights: Streamlining tourism review analysis with large language models. Information Technology & Tourism, 27(1), 227–261.
- **Tệp:** `E3_guidotti_llm_tourism_review_analysis.pdf`
- **DOI:** 10.1007/s40558-024-00309-9
- **Nhóm trụ cột:** P5
- **Vì sao giữ:** Prior art cho mục đích của ứng dụng — phân tích review phục vụ quản lý

### Zhu (2025)

- **Trích dẫn đầy đủ:** Zhu, A., et al. (2025). DaNet: Dual-aware enhanced alignment network for multimodal aspect-based sentiment analysis. In Findings of ACL 2025 (pp. 14369–14381).
- **Tệp:** `E6_zhu_danet_multimodal_absa.pdf`
- **DOI:** 10.18653/v1/2025.findings-acl.741
- **Nhóm trụ cột:** P5
- **Vì sao giữ:** Chỉ tham khảo kỹ thuật xử lý khía cạnh ngầm — dữ liệu của đề tài chỉ có văn bản nên liên quan thấp

### Ameur et al. (2024)

- **Trích dẫn đầy đủ:** Ameur, A., Hamdi, S., & Ben Yahia, S. (2024). Sentiment analysis for hotel reviews: A systematic literature review. ACM Computing Surveys, 56(2), 1–38.
- **Tệp:** `2024_ameur_hotel_reviews_sentiment_slr.pdf`
- **DOI:** 10.1145/3605152
- **Nhóm trụ cột:** P5
- **Vì sao giữ:** Dùng để chọn kiến trúc có căn cứ thay vì chạy theo độ mới

### You et al. (2024)

- **Trích dẫn đầy đủ:** You, X.-Y., Chang, S.-C., Hung, S.-M., Ku, C.-H., & Chang, Y.-C. (2024). Using multitask learning with pre-trained language models for aspect-based sentiment analysis in the hospitality industry. In Proceedings of PACLIC 2024 (pp. 131–140).
- **Tệp:** `E2_you_multitask_plm_absa_hospitality.pdf`
- **Nhóm trụ cột:** P5
- **Vì sao giữ:** Số dùng được ngay: AUROC 0,9214 · AUPRC 0,6152 · F1 0,5817; so XGBoost 0,4938 và LSTM-attention 0,4208
- **Ghi chú:** Hội nghị, không có DOI.

### Puh et al. (2023)

- **Trích dẫn đầy đủ:** Puh, K., & Bagić Babac, M. (2023). Predicting sentiment and rating of tourist reviews using machine learning. Journal of Hospitality and Tourism Insights, 6(3), 1188–1204.
- **Tệp:** `2023_puh_predicting_sentiment_and_rating.pdf`
- **DOI:** 10.1108/JHTI-02-2022-0078
- **Nhóm trụ cột:** P5
- **Vì sao giữ:** Baseline kỹ thuật cũ; không dùng trong lập luận về bất nhất
