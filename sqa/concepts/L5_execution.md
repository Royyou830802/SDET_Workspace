# L5｜Execution & Infra：環境、自動化、Observability

> 核心問題：**測試結果可信嗎？出錯時能不能定位？**

## 我已經會的

- Python 自動化框架（儀器控制 → 裝置監測 → 結果分析）
- CI pipeline（Bamboo、TestComplete）
- 讓 AE 能透過 UI 獨立執行

## 要補強的觀點

### 1. Test the test：測試本身可信嗎？

- **Measurement System Analysis**：量測誤差有沒有大到蓋過版本差異？（← STAR #6 功率計，其實就是這個）
- 自動化結果 vs 手動結果交叉驗證
- 環境一致性：韌體版本、設備校正、溫度

### 2. Observability：出錯時能不能定位？

- Log 要帶 **timestamp + test ID + 版本 + 環境參數**，post-processing 才對得起來（← Cirrus 有肯定這點）
- 時間同步：多台設備 / 儀器的 log 要能對齊
- 出錯時自動抓 snapshot：crash dump、系統狀態、前後 N 秒的 log
- Heartbeat / watchdog：判斷 DUT 是 hang 還是 crash

### 3. Reproducibility：intermittent failure 怎麼處理？

- 記錄足夠的條件以便重現
- 縮小範圍：bisect 版本、bisect 參數
- 統計重現率（例如 3/100）而不是只說「偶爾會發生」

### 4. Flaky test 管理

- 區分「產品不穩」和「測試不穩」
- Flaky test 要隔離並追蹤，不能直接忽略

## 面試時的說法

> "Before trusting the results, I validate the measurement setup itself — for example, I once compared four power meters across five scenarios to quantify instrument error. For long-running tests, I make sure every log line carries the test ID, build, and timestamp so failures can be correlated during post-processing."

## 我的筆記

<!-- 讀書、練習時補充 -->
