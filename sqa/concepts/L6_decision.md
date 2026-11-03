# L6｜Decision：結果怎麼變成 ship / no-ship 的判斷？

> 核心問題：**你的報告讓決策者知道該怎麼做嗎？**

## 我的現況

- 會產出 MP Report、彙整結果
- → 缺少「**結論 + 建議 + 風險**」，比較像是列出數據

## 核心概念

### 報告的三層

| 層 | 內容 | 例子 |
|---|---|---|
| **結論** | 一句話：能不能出貨 | "Ready to ship with 2 known risks" |
| **風險** | 已知問題 + 影響 + 建議 | "TTFF regression 8% in urban, still within spec; recommend fix in next release" |
| **證據** | 數據、覆蓋率、未測範圍 | 表格、圖、**明確列出沒測的部分** |

> 決策者先看結論，有疑問才往下看證據。Junior 的報告順序通常是反過來的

### Bug 嚴重度 vs 優先度

- **Severity**：技術上多嚴重（crash > 功能錯 > UI）
- **Priority**：商業上多急（客戶場景、release 時程）
- 兩者不同：低 severity 但客戶 demo 會碰到 → 高 priority

### QA 的角色：提供資訊，不是守門員

- QA 負責讓風險**透明**，決策由 PM / RD / 主管共同做
- 但要給出**明確建議**，不是只丟數據

## 面試時的說法

> "My report leads with a clear recommendation — ship, ship with known risks, or block — followed by the risks with their user impact, and then the supporting data, including what we didn't cover. The final call is a team decision, but I make sure the risks are visible and I give a clear recommendation."

## 我的筆記

<!-- 讀書、練習時補充 -->
