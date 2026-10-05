Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Khai phá Luật Kết hợp (Association Rules: Support & Confidence)**:

---

### 1. Cơ bản về Luật Kết hợp (Association Rules)

* **Khái niệm:** Luật kết hợp thể hiện mối quan hệ giữa các tập mục dưới dạng dạng mệnh đề $X \Rightarrow Y$ (Nếu xuất hiện tập mục $X$ thì nhiều khả năng tập mục $Y$ cũng sẽ xuất hiện).
* **Mục tiêu:** Phát hiện các **luật mạnh (strong rules)** thỏa mãn đồng thời cả hai tiêu chuẩn: **Độ hỗ trợ tối thiểu (Minimum Support)** và **Độ tin cậy tối thiểu (Minimum Confidence)**.

---

### 2. Hai Chỉ số Đo lường Cốt lõi: Support & Confidence

* **Độ hỗ trợ (Support - $Supp(X \Rightarrow Y)$):**
* Đo lường mức độ xuất hiện đồng thời của cả $X$ và $Y$ trong toàn bộ cơ sở dữ liệu.
* *Công thức / Ý nghĩa:* Xác suất $P(X \cup Y)$ — mang tính đối xứng ($Supp(X \Rightarrow Y) = Supp(Y \Rightarrow X)$).


* **Độ tin cậy (Confidence - $Conf(X \Rightarrow Y)$):**
* Đo lường xác suất điều kiện tập $Y$ xuất hiện khi đã biết tập $X$ xuất hiện.
* *Công thức / Ý nghĩa:* $P(Y \vert{} X) = \frac{Supp(X \cup Y)}{Supp(X)}$.
* *Tính hướng (Directionality):* Confidence mang tính **một chiều** ($Conf(X \Rightarrow Y) \neq Conf(Y \Rightarrow X)$).



---

### 3. Ví dụ Minh họa về Tính Hướng của Confidence

* Xét hai mục $B$ và $E$ trong tập giao dịch:
* **Support của cặp $\{B, E\}$:** Là $0.8$ (xuất hiện trong $80\%$ tổng số giao dịch).
* **Confidence của luật $B \Rightarrow E$:** $Conf(B \Rightarrow E) = \frac{Supp(B \cup E)}{Supp(B)} = 1.0$ ($100\%$ các giao dịch mua $B$ đều mua $E$).
* **Confidence của luật $E \Rightarrow B$:** $Conf(E \Rightarrow B) = \frac{Supp(B \cup E)}{Supp(E)} = 0.8$ (Chỉ có $80\%$ các giao dịch mua $E$ là có mua $B$).



---

> **Kết luận:** Khai phá luật kết hợp mở rộng kết quả của các thuật toán như Apriori hay FP-Growth bằng cách không chỉ tìm ra các tập sản phẩm đi cùng nhau, mà còn định lượng được **độ mạnh** và **chiều tác động** của các mối quan hệ đó.