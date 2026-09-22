# Project Status Snapshot

_Cập nhật lần cuối: 2026-09-23 | Trạng thái: RQ3 chốt, khảo sát đóng có điều kiện_

---

## 1. Giai đoạn Hiện tại & Trạng thái Đề tài
* **Trạng thái đề tài:** **ĐANG KHÁM PHÁ / RQ3 ĐÃ CHỐT, RQ1–RQ2 CÒN NHÁP**.
* **Tiến độ:** Đã hoàn tất targeted Survey Round 3 theo `RDR-0003` và chốt RQ3 theo `RDR-0004`. Đã chốt hướng artifact ứng dụng cho môn DAP391m (Bảng soát điểm sao).

## 2. Research Questions

* **Khung lý thuyết — ĐÃ KHÓA (`RDR-0005`):** S-O-R + Kano/three-factor + Prospect Theory. Nhánh forgiveness không còn là cơ chế trung tâm.
* **RQ3 — ĐÃ CHỐT (`RDR-0004`):** Cảm xúc tích cực và tiêu cực trên nhiều khía cạnh khách sạn kết hợp bất đối xứng như thế nào để quyết định chiều hướng và độ lớn của sentiment–rating discrepancy?
* RQ1–RQ2 chưa chốt chính thức; tiếp tục giữ hướng prevalence/typology và signed aspect-level discrepancy.
* RQ3 dùng cơ chế asymmetric compensatory/non-compensatory. `Service × Facility` chỉ còn là planned contrast.
* `Severity` và `Service_Recovery` chỉ kiểm định được trên evaluation set (sub-sample); hotel class dùng cho robustness.
* Ba RQ kỹ thuật RQ4–RQ6 sinh từ nhánh dự báo phục vụ Bước 5 của môn (`0003` brainstorm log).

## 3. Quyết định Kỹ thuật đã chốt (Decisions)

- Đã chốt `RDR-0001`: Mục tiêu và tiêu chí dừng khảo sát văn hiến.
- Đã chốt `RDR-0002`: Quét chủ động trong cửa sổ 36 tháng, nguồn cũ chỉ theo citation chain có lý do.
- Đã chốt `RDR-0003`: Mở lại khảo sát để tái định hình RQ3; ưu tiên journal và nguồn đóng.
- Đã chốt `RDR-0004` (2026-09-23): Chốt RQ3 theo cơ chế asymmetric aspect compensation.
- Đã chốt `RDR-0005` (2026-09-23): Đóng khảo sát có điều kiện; khóa khung lý thuyết S-O-R + Kano + Prospect Theory; phạm vi dữ liệu 9.990 review; forgiveness không đo.
- Survey Round 3 đã sàng lọc 9 journal candidates; 2/9 nguồn đã có toàn văn. Hàng đợi ưu tiên ban đầu 8 bài, đã lấy Sharma và còn 7 bài.
- Chưa chốt công thức đo discrepancy — chờ validation study quyết định.

## 4. Việc tiếp theo (Next Steps)

1. Nhờ thư viện trường/giảng viên lấy 6 bài đóng trong `refs/INDEX.md` mục B2 (ưu tiên Kwon 2026) — 4 bài truy cập mở đã lấy xong.
2. Cập nhật Research Proposal theo RQ3 đã chốt và theo nhánh dự báo; giữ nguyên audit trail `refs/`.
3. Chạy validation study để chốt công thức đo discrepancy, rồi mới khóa mô hình econometric.
4. Tải 5 bài truy cập mở còn thiếu + nhờ thư viện 12 bài đóng (xem `refs/INDEX.md` mục D và log `0006` mục 7.2).
5. Viết Research Proposal trên khung đã khóa: phạm vi 9.990 review, boundary conditions = Severity + Service_Recovery + hotel class.
6. Dựng khung ứng dụng + endpoint sớm (mục tiêu tuần 4); cảnh báo SNS làm sớm vì không thể mock.
