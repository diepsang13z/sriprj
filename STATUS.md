# Project Status Snapshot

_Cập nhật lần cuối: 2026-09-20 | Trạng thái: Đang khởi động (Kickoff)_

---

## 1. Giai đoạn Hiện tại & Trạng thái Đề tài
* **Trạng thái đề tài:** **ĐANG KHÁM PHÁ / CHƯA CHỐT CHÍNH THỨC (Exploratory Phase)**.
* **Tiến độ:** Đã bóc tách paper gốc, nhận diện tautology ở biến Loyalty, khảo sát dataset, ban hành `RDR-0001`, và hoàn tất vòng khảo sát văn hiến đầu tiên với 11 nguồn ngoài paper gốc.

## 2. Research Questions (Chưa chốt — Đang định hình)

* Hiện chưa chốt RQs chính thức; đang trong giai đoạn brainstorm và khảo sát văn hiến.
* Một số hướng giả thuyết tiềm năng đang thảo luận trong `docs/logs/brainstorm/0001_root_idea.md`:
  * Mâu thuẫn cảm xúc - điểm số (Sentiment–Rating Inconsistency / Discrepancy).
  * Tái định nghĩa Loyalty thành Sublimation (Thăng hoa / Vị tha) & Anger (Phẫn nộ / Trừng phạt).
  * Vai trò điều tiết / "tấm đệm" (Buffering Effect) của Service hoặc Sublimation trước các lỗi cơ sở vật chất.
## 3. Quyết định Kỹ thuật đã chốt (Decisions)

- Đã chốt `RDR-0001`: Mục tiêu và tiêu chí dừng khảo sát văn hiến (Literature Survey Endpoint).

## 4. Việc tiếp theo (Next Steps)

1. Khảo sát cấu trúc nhãn chi tiết trong `data/TripAdvisor_EN.json` và phân loại 402 mẫu 5 sao chứa negative span.
2. Thực hiện survey round 2: trích công thức của Valdivia et al. (2019), xác minh hai biến inconsistency của Wang et al. (2025, DSS), và tìm phép đo signed/continuous ở aspect level.
3. Soạn thảo Research Proposal sau khi đạt saturation và chốt operationalization.
4. Ban hành `RDR-0002` chốt theory, discrepancy measure và pipeline sau khi khảo sát đạt endpoint.
