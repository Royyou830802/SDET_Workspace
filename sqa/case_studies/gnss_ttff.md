# Case Study：GNSS TTFF Test Strategy

> 用 AIROHA 的真實經驗，從 L1 寫到 L6，寫成一份完整的 test strategy
> 用途：面試時被問「How would you test X」或 STAR 被追問技術細節時的素材
> 狀態：🟡 草稿（L4 已有範例，其餘待補）

---

## 背景

<!-- 產品、TTFF 的定義（cold / warm / hot start）、為什麼重要、客戶是誰 -->

---

## L1 Risk：TTFF 會怎麼壞？對誰影響最大？

<!-- 提示：
- 哪些情境下 TTFF 會變差？（弱訊號、urban canyon、橋下、星曆過期、inject 順序）
- 誰受影響？（車用導航 vs 穿戴裝置，在意的點不同）
- 哪些改動最可能造成 TTFF regression？
-->

---

## L2 Strategy：用哪些測試覆蓋？

<!-- 提示：
- 實驗室（simulator，可控、可重現） vs road test（真實、不可控）各負責什麼？
- Full test 和 regression 各跑哪些情境？
- 時間不夠時先砍什麼？
-->

---

## L3 Test Design：情境怎麼組合？

<!-- 提示：start mode × 訊號強度 × 環境 × 輔助資料（AGNSS）
- 全組合太多時，怎麼挑？
-->

---

## L4 Oracle：Pass/Fail 怎麼訂？

| 判斷 | 內容 | 依據 |
|---|---|---|
| 統計量 | 看 **P95**，不看平均 | 使用者在意的是「偶爾要等很久」（User expectations） |
| 條件 | 訊號 -130 / -145 dBm × open sky / urban | 不同條件代表不同使用場景（Purpose） |
| 次數 | N ≥ 50 | TTFF 變異大，需要看分佈 |
| Spec 門檻 | P95 < 35s | Claims |
| Regression 門檻 | 比上一版 P95 慢 > X% 就標記，即使仍在 spec 內 | History |
| 競品 | 同條件下慢於競品 → 列為 risk 回報，不算 fail | Comparable products |

<!-- TODO：把上表的數字換成我在 AIROHA 實際用過的條件與門檻 -->

---

## L5 Execution：環境與 observability

<!-- 提示：
- simulator 設定、訊號校正
- 每次 run 要記錄什麼才能 post-process？
- 怎麼確認 cold start 真的是 cold（星曆清除）？
-->

---

## L6 Decision：結果怎麼回報？

<!-- 提示：
- Spec fail → block；regression / 輸競品 → 怎麼呈現給 PM、RD？
- 韓國客戶案例：最後怎麼影響 lock 版本的決策？
-->

---

## 連結的 STAR

- [STAR #2 韓國現場支援](../../docs/STAR/BQ_Prep_Note.md#star2)
- [STAR #10 Apple Watch 競品分析](../../docs/STAR/BQ_Prep_Note.md#star10)
