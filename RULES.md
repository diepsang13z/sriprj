# Project Rules

Tài liệu này quy định các nguyên tắc vận hành, quản lý context và kỹ thuật áp dụng xuyên suốt dự án. Mọi Agent và cộng tác viên phải tuân thủ nghiêm ngặt.

---

## 1. Giới hạn độ dài Context File (Line Budget)

- **Quy tắc:** Mọi file context được dẫn link trong `docs/INDEX.md` (bao gồm `RULES.md`, `AGENTS.md`, `STATUS.md` và các tài liệu kiến trúc/đặc tả) phải có độ dài **$\le 200$ dòng**.
- **Ngoại lệ:** Thư mục nhật ký và khảo sát chi tiết `docs/logs/**` không áp dụng giới hạn này.
- **Mục đích:** Giữ context ngắn gọn, tránh tràn bộ nhớ đệm (context window) của mô hình và đảm bảo thông tin luôn sắc bén, dễ tra cứu.

---

## 2. Kỷ luật Thao tác Git (Git Operations)

- **Quy tắc:** **Tuyệt đối không tự ý chạy các lệnh ghi hoặc thay đổi trạng thái git** (`git add`, `git commit`, `git push`, `git checkout`, `git rebase`, `git reset`...) trừ khi có chỉ thị hoặc yêu cầu rõ ràng từ người dùng.
- **Quy trình:**
  1. Chỉ thực hiện chỉnh sửa, bổ sung nội dung trên working tree.
  2. Báo cáo các thay đổi, đề xuất commit message.
  3. Chỉ thực thi lệnh git khi người dùng xác nhận phê duyệt.

---

## 3. Nguồn sự thật cao nhất (Single Source of Truth)

- **Quy tắc:** Khi có mâu thuẫn giữa các tài liệu đặc tả, ý tưởng brainstorm hay thảo luận, quyết định kiến trúc trong thư mục `docs/decisions/` có **số hiệu lớn nhất (`RDR-NNNN` với NNNN lớn nhất)** luôn là **Single Source of Truth**.
- **Nguyên tắc:**
  - Thư mục `docs/decisions/` hoạt động theo cơ chế **Append-only** (chỉ thêm mới, không sửa đè quyết định cũ).
  - Quyết định mới hơn có quyền phủ định hoặc thay thế quyết định cũ hơn nếu có ghi rõ căn cứ thay thế.

---

## 4. Kỷ luật trong Giai đoạn Khám phá Đề tài (Exploratory Discipline)
* **Quy tắc:** Khi đề tài và Research Questions (RQs) chưa được chốt chính thức (chưa có quyết định kiến trúc `RDR-0001` ban hành trong `docs/decisions/`), **Agent KHÔNG tự ý sinh code triển khai hay tự chốt khung phương pháp luận**.
* **Phạm vi hành vi:** Agent chỉ tập trung hỗ trợ phân tích dữ liệu, bóc tách cấu trúc dataset, đối soát văn hiến và brainstorm ý tưởng theo yêu cầu của người dùng.
