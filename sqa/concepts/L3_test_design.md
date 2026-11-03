# L3｜Test Design：具體 test case 怎麼產生？

> 核心問題：**格子太多測不完，怎麼用最少的 case 抓最多的 bug？**

## 我已經會的

- 心智圖展開 Test Scope：Function / Performance / Stress / Interaction
- Feature × Mode 展開 Coverage

## 要補的 Test Design Techniques

| Technique | 用途 | 例子 |
|---|---|---|
| **Equivalence Partitioning** | 把輸入分組，每組測一個代表值 | 音量 0~100 → 分成 0、中間、100 |
| **Boundary Value Analysis** | bug 最常出現在邊界 | 0、1、99、100、101 |
| **State Transition** | 有狀態的系統，測狀態切換 | Sleep → Active → Streaming，以及非法切換 |
| **Pairwise / Combinatorial** | 參數組合爆炸時，只覆蓋兩兩組合 | Feature × Mode × 溫度 × 電壓 |
| **Fault Injection** | 主動製造異常 | 斷電、拔線、訊號中斷、記憶體不足 |
| **Error Guessing** | 憑經驗猜容易壞的地方 | 快速連續操作、極端值、重複觸發 |
| **Exploratory Testing** | 有目標、限時、邊測邊學 | 用 charter 定義範圍：「探索 X，找 Y 類問題」 |

## 跟 L1 串起來

> 不是每個格子都用同樣深度測。**L1 判斷的高 risk 區域 → 用更多 technique 深測；低 risk → equivalence partitioning 帶過**

## 面試時的說法

> "Full combination of features and modes isn't feasible, so I'd use pairwise to cover parameter interactions, boundary values for numeric inputs, and state transition testing for mode switching — and go deeper on the areas I flagged as high-risk."

## 我的筆記

<!-- 讀書、練習時補充 -->
