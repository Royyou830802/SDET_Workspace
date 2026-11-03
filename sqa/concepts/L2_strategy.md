# L2｜Strategy：用什麼測試、在哪個階段處理哪個風險？

> 核心問題：**每個 risk 用哪種測試覆蓋？Full test 和 Regression 各測什麼？**

## 核心概念

### Risk → Test Type 對應

| Risk（L1） | Test Type |
|---|---|
| 功能錯誤 | Functional |
| 效能不達標 / 退化 | Performance、Benchmark |
| 長時間或高負載下失效 | Stress、Soak / Endurance |
| 模組間互動問題 | Integration、Interaction |
| 環境條件 | Environmental / Corner（PVT、訊號、溫度） |
| 異常後無法恢復 | Fault injection、Recovery |
| 版本間退化 | Regression |

### Test Level：在哪一層抓最便宜

Unit → Integration → System → Field / Customer

> 越早抓越便宜；但有些問題（如 road test、真實訊號環境）只能在 system / field 層出現

### Full Test vs Regression：選擇的依據

| | Full Test | Regression |
|---|---|---|
| 時機 | 新功能、大改版、MP 前 | 每次發版、小改動 |
| 範圍 | 全部 | **依 change impact + risk 挑選** |
| 關鍵判斷 | — | 改了什麼？影響到哪些模組？歷史上哪裡常壞？ |

### 資源有限時的取捨

- 先保 **高 impact × 高 likelihood**
- 自動化的部分全跑，手動的部分依 risk 砍
- **明確寫下沒測什麼、為什麼**（這是 senior 訊號）

## 面試時的說法

> "Given limited time, I'd map each risk to a test type and prioritize by impact and likelihood. For regression, I'd select tests based on what changed and where we've historically seen failures — and I'd explicitly document what we're not covering and why."

## 我的筆記

<!-- 讀書、練習時補充 -->
