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
- **Nhánh làm việc:** mỗi người một nhánh riêng theo mẫu `<tên>/work` (`dieps13z/work`, `khoideptrai/work`, …), rồi mở pull request vào `main`. **Không commit thẳng vào `main`.**
- **Không tạo nhánh lồng tên nhánh khác** (ví dụ `remotes/origin/<tên>/work`). Lỗi này đã từng xảy ra và làm `git push` trần báo *"upstream branch does not match"*; nhánh rác sau đó phải xoá tay.

---

## 3. Nguồn sự thật cao nhất (Single Source of Truth)

- **Quy tắc:** Khi có mâu thuẫn giữa các tài liệu đặc tả, ý tưởng brainstorm hay thảo luận, quyết định kiến trúc trong thư mục `docs/decisions/` có **số hiệu lớn nhất (`RDR-NNNN` với NNNN lớn nhất)** luôn là **Single Source of Truth**.
- **Nguyên tắc:**
  - Thư mục `docs/decisions/` hoạt động theo cơ chế **Append-only** (chỉ thêm mới, không sửa đè quyết định cũ).
  - Quyết định mới hơn có quyền phủ định hoặc thay thế quyết định cũ hơn nếu có ghi rõ căn cứ thay thế.

---

## 4. Kỷ luật trong Giai đoạn Khám phá Đề tài (Exploratory Discipline)

- **Bối cảnh:** điều kiện kích hoạt cũ của mục này — *"chưa có quyết định kiến trúc `RDR-0001` ban hành"* — **đã hết hiệu lực** vì `RDR-0001` đã ban hành. Nhưng RQ1–RQ2 vẫn còn nháp và công thức đo discrepancy vẫn chưa chốt, nên phần tinh thần của mục này vẫn giữ.
- **Quy tắc:** khi một quyết định phương pháp **chưa có trong `docs/decisions/`**, Agent **KHÔNG tự chốt thay nhóm** — không tự chọn công thức đo bất nhất, bộ ước lượng cảm xúc, cách chuẩn hóa, ngưỡng phân loại hay khung lý thuyết.
- **Phạm vi hành vi:** Agent được hỗ trợ phân tích dữ liệu, bóc tách cấu trúc dataset, đối soát văn hiến và brainstorm ý tưởng. Việc chốt phương pháp do nhóm quyết và ghi thành `RDR`.

---

## 5. Quy ước Đặt tên File và Thư mục (Naming Convention)

- **Quy tắc chung:** Tên file và thư mục **chỉ dùng chữ thường, chữ số và dấu gạch dưới `_`**. Không dùng **gạch ngang `-`**, khoảng trắng, dấu tiếng Việt hoặc ký tự đặc biệt.
- **Lý do:** gạch dưới không bị shell, đường dẫn URL và một số công cụ diễn giải thành ký tự đặc biệt; gạch ngang dễ lẫn với dấu phân tách từ khi tên đã có sẵn nhiều thành phần.
- **Ngoại lệ 1 — mã quyết định:** `RDR-NNNN` giữ nguyên gạch ngang vì đó là phần của mã, không phải dấu phân tách từ. Phần mô tả phía sau vẫn dùng `_`, ví dụ `RDR-0004_lock_rq3_asymmetric_aspect_compensation.md`.
- **Ngoại lệ 2 — file điều hướng và quản lý context:** tên file viết **CHỮ HOA TOÀN BỘ**, phần mở rộng giữ chữ thường. Nhóm này gồm `README.md`, `AGENTS.md`, `RULES.md`, `STATUS.md`, `INDEX.md`, `SOURCES.md`, `BACKLOG.md`.
  - **Tiêu chí phân biệt:** nội dung file là **trỏ tới file khác** hoặc **trạng thái, quy ước của cả hệ thống** → viết hoa. Nội dung là **kiến thức, phân tích, nhật ký** → chữ thường. Ví dụ: `refs/INDEX.md` và `docs/BACKLOG.md` viết hoa; `notes/reference_map.md` và `docs/logs/progress/2026_09_23_dieps.md` viết thường.
  - **Lý do:** tách hai loại file nằm cạnh nhau — file để **đọc và điều hướng** (viết hoa, nổi bật khi liệt kê thư mục) và file **nội dung** (chữ thường). Trong một thư mục có 7 PDF kèm 1 file quản lý, quy ước này cho biết ngay đâu là điểm vào.
  - **Chỉ áp cho tên file.** Tên thư mục vẫn chữ thường.
  - **Áp dụng cho file tạo mới.** File cũ đã đúng quy ước thì giữ nguyên; file nội dung không đổi tên chỉ vì quy ước này.
- **Ví dụ đúng:** `refs/04_mechanism/2025_sharma_review_sentiment_garden.pdf` · `refs/04_mechanism/SOURCES.md` · `docs/BACKLOG.md` · `refs/INDEX.md`
- **Ví dụ sai:** `refs/04_mechanism/2025-sharma-review.pdf` · `refs/04_mechanism/sources.md` · `docs/backlog.md` · `refs/04_mechanism/Index.md`
- **Quy ước thư viện `refs/`:** `<năm>_<tác giả chính không dấu>_<chủ đề ngắn>.pdf`, đặt trong thư mục chức năng (xem `refs/INDEX.md` mục 0). Bản markdown của bài nằm ở thư mục con `md/`, **trùng tên với PDF**, chỉ đổi phần mở rộng.

---

## 6. Kỷ luật ghi Trạng thái, Việc mở và Nhật ký Tiến độ

Ba tầng, tách theo **vòng đời thay đổi** — thứ gì đổi cùng nhịp thì nằm cùng tệp:

| Tầng | Tệp | Đổi khi nào | Cách sửa |
| --- | --- | --- | --- |
| Trạng thái dự án | `STATUS.md` | có `RDR` mới, đổi pha, chốt RQ | Sửa từng dòng; **không viết lại cả tệp** |
| Việc đang mở | `docs/BACKLOG.md` | có việc mới, có việc xong | Thêm dòng; xong thì đổi trạng thái, **không xoá dòng** |
| Việc theo người | `docs/logs/progress/YYYY_MM_DD_<tên>.md` | mỗi phiên làm việc | Mở tệp mới; **không sửa tệp của người khác** |

- **Tệp nhật ký tiến độ có bốn mục bắt buộc:** `Đã làm` · `Bằng chứng` · `Còn lại cho người khác` · `Đang chặn`. Mục nào không có gì thì ghi "không" — đừng bỏ mục.
- **Lưu trữ backlog:** `docs/BACKLOG.md` được dẫn link trong `docs/INDEX.md` nên chịu trần 200 dòng. Khi số dòng việc đã `xong` vượt 30, chuyển các dòng đó sang `docs/logs/backlog_archive.md`.
- **Không chép lại thứ đã có nhà.** Danh sách quyết định ở `docs/INDEX.md` mục 2; lịch 10 tuần ở `reports/md/project_planning.md`. Trạng thái chỉ **trỏ**, không sao chép.
- **Lý do:** tệp dùng chung chỉ an toàn khi thứ trong nó đổi cùng nhịp. Trộn việc thường ngày vào `STATUS.md` khiến hai người hoàn thành hai việc cùng lúc ghi đè lẫn nhau — và git **không báo**, vì mất cập nhật không tạo merge conflict.
