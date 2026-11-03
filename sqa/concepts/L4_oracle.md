# L4｜Oracle & Criteria：怎樣算 pass？依據是什麼？

> 核心問題：**spec 沒寫、RD 也沒答案的時候，你怎麼判斷？**

## 我的現況

- Pass/Fail 幾乎依照 feature 原本的設定
- RD 沒答案時，依使用者體驗訂
- → 其實有做判斷，但**沒有系統化，也沒講出依據**

---

## HICCUPPS：Oracle 從哪裡來

> 由 Michael Bolton / James Bach 提出。核心想法：**「跟什麼比會覺得不對勁」就是 oracle**

| Oracle 來源 | 意思 | 我做過的例子 |
|---|---|---|
| **H**istory | 跟上一版比 | Regression testing |
| **I**mage | 符合品牌形象嗎 | — |
| **C**omparable products | 跟競品比 | 韓國對標競品、Apple Watch 分析 |
| **C**laims | 跟 spec、文件、行銷宣稱比 | 低功耗新品 power 數據 |
| **U**ser expectations | 使用者會覺得不對嗎 | 「依使用者體驗訂」 |
| **P**roduct | 產品自身前後一致嗎 | 同一功能在不同 mode 行為一致 |
| **P**urpose | 符合產品用途嗎 | 車用 → 穩定性比速度重要 |
| **S**tandards | 法規、認證、業界標準 | 中國及車用認證 pre-check |

---

## 制定 Pass/Fail 的四個問題

1. **看哪個統計量？** 平均、P95、worst case → 取決於使用者在意什麼
2. **跑幾次？** 變異大的指標，跑 1 次沒意義 → 要看分佈
3. **跟誰比？** spec（絕對門檻）、上一版（regression 門檻）、競品（競爭力參考）
4. **不同等級的 fail 怎麼處理？** Block release / 回報為 risk / 只記錄

---

## 範例：GNSS Cold Start TTFF

**Junior 寫法**
> Cold start TTFF < 35s → Pass

**Senior 寫法**

| 判斷 | 內容 | 依據 |
|---|---|---|
| 統計量 | 看 **P95**，不看平均 | 使用者在意的是「偶爾要等很久」（User expectations） |
| 條件 | 訊號 -130 / -145 dBm × open sky / urban | 不同條件代表不同使用場景（Purpose） |
| 次數 | N ≥ 50 | TTFF 變異大，需要看分佈 |
| Spec 門檻 | P95 < 35s | Claims |
| Regression 門檻 | 比上一版 P95 慢 > X% 就標記，即使仍在 spec 內 | History |
| 競品 | 同條件下慢於競品 → 列為 risk 回報，不算 fail | Comparable products |
| 決策 | Spec fail → block；regression / 輸競品 → 交 PM、RD 決定 | 連到 L6 |

> 每一行都是**我自己做的判斷 + 依據**，這就是面試官想聽的

---

## Exit Criteria：什麼時候可以停止測試？

- 計畫內的 test case 執行率（例如 100%）
- 未解 bug 的嚴重度分佈（例如 0 個 critical、≤ N 個 major）
- 關鍵指標穩定（連續 N 輪無新 crash）
- 風險已被 stakeholder 知悉並接受

## 面試時的說法

> "When the spec doesn't define a threshold, I look for other oracles — the previous release, competitor products, and user expectations. For a metric like TTFF, I'd look at P95 rather than the mean, because users notice the occasional long wait. I'd also separate a spec failure, which blocks release, from a regression that's still in spec, which I'd flag as a risk for the team to decide."

## 我的筆記

<!-- 讀書、練習時補充 -->
