# Nguồn — 07_baselines_methods

> **TỆP NGUỒN — sửa tay ở đây.** `INDEX.md` cùng thư mục là bản chụp của tệp này; sửa ở đây rồi cập nhật `INDEX.md` bằng tay cho khớp (script sinh đã gỡ khỏi repo).

## Ameur et al. (2024)

- id: 2024_ameur_hotel_reviews_sentiment_slr
- file: 2024_ameur_hotel_reviews_sentiment_slr.pdf
- cite: Ameur, A., Hamdi, S., & Ben Yahia, S. (2024). Sentiment analysis for hotel reviews: A systematic literature review. ACM Computing Surveys, 56(2), 1–38.
- doi: 10.1145/3605152
- year: 2024
- status: full_text
- evidence_level: I
- evidence_basis: refs_index
- recency: in_window
- pillars: P5
- updated: 2026-09-23
- role: Bản đồ kỹ thuật toàn bộ pipeline xử lý review khách sạn
- keep_reason: Dùng để chọn kiến trúc có căn cứ thay vì chạy theo độ mới

## Guidotti et al. (2025)

- id: 2025_guidotti_llm_tourism_review
- file: E3_guidotti_llm_tourism_review_analysis.pdf
- cite: Guidotti, D., Pandolfo, L., & Pulina, L. (2025). Discovering sentiment insights: Streamlining tourism review analysis with large language models. Information Technology & Tourism, 27(1), 227–261.
- doi: 10.1007/s40558-024-00309-9
- year: 2025
- status: full_text
- evidence_level: IV
- evidence_basis: matrix_round_4
- recency: in_window
- pillars: P5
- round: 4
- code: E3
- updated: 2026-09-23
- role: LLM zero-shot cho phân loại cảm xúc và trích từ khóa; đóng khung như công cụ hỗ trợ ra quyết định
- keep_reason: Prior art cho mục đích của ứng dụng — phân tích review phục vụ quản lý

## Pramono et al. (2026)

- id: 2026_pramono_explainable_absa
- file: E1_pramono_explainable_absa_shap_lime.pdf
- cite: Pramono, B. A., Gernowo, R., & Sofwan, A. (2026). Explainable multilingual aspect-based sentiment analysis for tourism using SHAP and LIME. Engineering, Technology & Applied Science Research, 16(3), 37077–37084.
- doi: 10.48084/etasr.18774
- year: 2026
- status: full_text
- evidence_level: VI
- evidence_basis: matrix_round_4
- recency: in_window
- pillars: P5
- round: 4
- code: E1
- updated: 2026-09-23
- role: Thiết kế tầng giải thích bằng SHAP và LIME, có kiểm định faithfulness
- keep_reason: Mẫu cho tầng giải thích của ứng dụng
- note: **Cảnh báo venue** — không nằm trong DOAJ, không phải core source. Chỉ dùng cho kỹ thuật, không dùng làm bằng chứng domain.

## Puh & Bagić Babac (2023)

- id: 2023_puh_predicting_sentiment_rating
- file: 2023_puh_predicting_sentiment_and_rating.pdf
- cite: Puh, K., & Bagić Babac, M. (2023). Predicting sentiment and rating of tourist reviews using machine learning. Journal of Hospitality and Tourism Insights, 6(3), 1188–1204.
- doi: 10.1108/JHTI-02-2022-0078
- year: 2023
- status: full_text
- evidence_level: VI
- evidence_basis: suy_tu_thiet_ke
- recency: in_window
- pillars: P5
- updated: 2026-09-23
- role: Baseline học máy cho dự đoán cảm xúc và điểm của review du lịch
- keep_reason: Baseline kỹ thuật cũ; không dùng trong lập luận về bất nhất

## You et al. (2024)

- id: 2024_you_multitask_plm_absa
- file: E2_you_multitask_plm_absa_hospitality.pdf
- cite: You, X.-Y., Chang, S.-C., Hung, S.-M., Ku, C.-H., & Chang, Y.-C. (2024). Using multitask learning with pre-trained language models for aspect-based sentiment analysis in the hospitality industry. In Proceedings of PACLIC 2024 (pp. 131–140).
- year: 2024
- status: full_text
- evidence_level: VI
- evidence_basis: matrix_round_4
- recency: in_window
- pillars: P5
- round: 4
- code: E2
- updated: 2026-09-23
- role: Mốc so kỹ thuật cho ABSA hospitality — RoBERTa đa nhiệm, 8 khía cạnh
- keep_reason: Số dùng được ngay: AUROC 0,9214 · AUPRC 0,6152 · F1 0,5817; so XGBoost 0,4938 và LSTM-attention 0,4208
- note: Hội nghị, không có DOI.

## Zhu et al. (2025)

- id: 2025_zhu_danet_multimodal_absa
- file: E6_zhu_danet_multimodal_absa.pdf
- cite: Zhu, A., et al. (2025). DaNet: Dual-aware enhanced alignment network for multimodal aspect-based sentiment analysis. In Findings of ACL 2025 (pp. 14369–14381).
- doi: 10.18653/v1/2025.findings-acl.741
- year: 2025
- status: full_text
- evidence_level: VI
- evidence_basis: matrix_round_4
- recency: in_window
- pillars: P5
- round: 4
- code: E6
- updated: 2026-09-23
- role: ABSA đa phương thức (ảnh + chữ)
- keep_reason: Chỉ tham khảo kỹ thuật xử lý khía cạnh ngầm — dữ liệu của đề tài chỉ có văn bản nên liên quan thấp
