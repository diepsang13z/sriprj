# 05_boundary_conditions — Điều kiện biên: severity, recovery, nền tảng, hạng sao

> **BẢN CHỤP CỦA `SOURCES.md` cùng thư mục.** Sửa dữ liệu ở `SOURCES.md`, không sửa trực tiếp tệp này. Script sinh đã gỡ khỏi repo nên phải cập nhật bằng tay cho khớp.

*Cập nhật: 2026-09-23 · 6 nguồn · 6 đọc được toàn văn*

| Nguồn | Năm | Mức | Trạng thái | Nhóm | Vai trò trong đề tài |
| --- | ---: | ---: | --- | --- | --- |
| **Das et al. (2026)** | 2026 | I | toàn văn | P3 | Meta-analysis về thất bại dịch vụ và phục hồi theo attribution và justice |
| **Leo et al. (2026)** | 2026 | III | toàn văn | P3 | Mức nghiêm trọng trong bối cảnh khách sạn; tín hiệu chất lượng đảo chiều trách nhiệm phục hồi |
| **Huang et al. (2025)** | 2025 | III | toàn văn | P3 | Phân biệt process failure và outcome failure; kỳ vọng phục hồi là biến trung gian |
| **Lim et al. (2025)** | 2025 | IV | toàn văn | P3 | Nghịch lý phục hồi dịch vụ — khi phục hồi vượt cả mức nền |
| **Hwang (2024)** | 2024 | III | toàn văn | P3 | Double deviation — lỗi ban đầu cộng phục hồi thất bại tạo mức phạt phi tuyến |
| **Tengilimoglu et al. (2024)** | 2024 | III | toàn văn | P3 | Mức nghiêm trọng là biến điều tiết trực tiếp của hiệu quả phục hồi |

## Chi tiết

### Das et al. (2026)

- **Trích dẫn đầy đủ:** Das, M., Jebarajakirthy, C., Maseeh, H. I., Lim, W. M., & Shah, J. S. (2026). Online service failure and recovery: An integrated meta-analytic perspective of attribution and justice theories. Journal of Business Research, 202, 115752.
- **Tệp:** `2026_das_online_failure_recovery_meta.pdf`
- **DOI:** 10.1016/j.jbusres.2025.115752
- **Nhóm trụ cột:** P3
- **Vì sao giữ:** Mức bằng chứng cao nhất trong thư viện cho cơ chế phục hồi — 147 nghiên cứu, N = 82.901

### Leo et al. (2026)

- **Trích dẫn đầy đủ:** Leo, W. W. C., Maggioni, I., Sembada, A. Y., & Tsarenko, Y. (2026). The dynamics of customer participation in service recovery: The roles of failure severity, quality signals, and responsiveness. International Journal of Hospitality Management, 140, 104809.
- **Tệp:** `2026_leo_participation_recovery_severity.pdf`
- **DOI:** 10.1016/j.ijhm.2026.104809
- **Nhóm trụ cột:** P3
- **Vì sao giữ:** Ứng viên trực tiếp cho biến `Severity` trên evaluation set
- **Ghi chú:** Ca biên về ngày công bố — `created` 2026-06-29 nhưng `published-print` 2027-01; xem ghi chú trong log Round 4 mục 3.3.

### Huang et al. (2025)

- **Trích dẫn đầy đủ:** Huang, Z., & Lo, A. (2025). Human vs. robot service provider agents in service failures: Comparing customer dissatisfaction and the mediating role of forgiveness and service recovery expectation. Information Technology & Tourism, 27, 417–448.
- **Tệp:** `2025_huang_service_failure_forgiveness_robots.pdf`
- **DOI:** 10.1007/s40558-025-00314-6
- **Nhóm trụ cột:** P3
- **Vì sao giữ:** Bằng chứng cho điều kiện biên severity và recovery
- **Ghi chú:** Nhánh forgiveness/justice. Chỉ dùng làm construct liên quan — **đề tài cố ý không đo** construct này.

### Lim et al. (2025)

- **Trích dẫn đầy đủ:** Lim, W. M., Saha, V., & Das, M. (2025). From service failure to brand loyalty: Evidence of service recovery paradox. Journal of Brand Management, 32(4), 257–281.
- **Tệp:** `B5_lim_service_recovery_paradox.pdf`
- **DOI:** 10.1057/s41262-025-00380-5
- **Nhóm trụ cột:** P3
- **Vì sao giữ:** Giới hạn trên của khả năng bù trừ; chặn việc diễn giải điểm lệch dương quá rộng

### Hwang (2024)

- **Trích dẫn đầy đủ:** Hwang, J. (2024). The effects of service recovery actions on customers' post-recovery responses to online travel agencies (OTAs): The moderating role of price. International Journal of Tourism Research, 26(4), e2742.
- **Tệp:** `2024_hwang_double_deviation_ota.pdf`
- **DOI:** 10.1002/jtr.2742
- **Nhóm trụ cột:** P3
- **Vì sao giữ:** Mô tả cơ chế chi phối mà không cần suy diễn trạng thái tâm lý

### Tengilimoglu et al. (2024)

- **Trích dẫn đầy đủ:** Tengilimoglu, E., & Öztürk, Y. (2024). The effects of eWOM triggered service recovery on customer citizenship behavior in the hospitality industry: The moderating role of failure severity. International Journal of Tourism Research, 26(4), e2673.
- **Tệp:** `2024_tengilimoglu_ewom_recovery_severity.pdf`
- **DOI:** 10.1002/jtr.2673
- **Nhóm trụ cột:** P3
- **Vì sao giữ:** Chặn việc coi phục hồi dịch vụ là biến nền — hiệu quả giảm mạnh khi lỗi nặng
