# 術語對照（面試用）

> 目標：能用英文精準講出自己的判斷，避免只說 "I would test it thoroughly"

| English | 中文 | 一句話說明 | 層 |
|---|---|---|---|
| Risk-based testing | 基於風險的測試 | 依 impact × likelihood 決定測試深度與順序 | L1 |
| Failure mode | 失效模式 | 產品可能壞掉的方式 | L1 |
| Change impact analysis | 變更影響分析 | 依改動範圍決定 regression 範圍 | L2 |
| Test level | 測試層級 | Unit / Integration / System / Acceptance | L2 |
| Soak / Endurance test | 長時間穩定性測試 | 長時間正常負載，找 leak、退化 | L2 |
| Stress test | 壓力測試 | 超出正常負載，找崩潰點與恢復行為 | L2 |
| Equivalence partitioning | 等價類劃分 | 同一類輸入只測一個代表值 | L3 |
| Boundary value analysis | 邊界值分析 | 測邊界與邊界 ±1 | L3 |
| State transition testing | 狀態轉換測試 | 測合法與非法的狀態切換 | L3 |
| Pairwise testing | 兩兩組合測試 | 覆蓋所有參數兩兩組合，減少 case 數 | L3 |
| Fault injection | 故障注入 | 主動製造異常，驗證處理與恢復 | L3 |
| Exploratory testing / Charter | 探索式測試 / 測試章程 | 限時、有目標的探索 | L3 |
| Test oracle | 測試判準 | 判斷結果對錯的依據 | L4 |
| Pass/fail criteria | 通過標準 | — | L4 |
| Exit criteria | 結束條件 | 什麼時候可以停止測試 | L4 |
| Percentile (P95) | 百分位數 | 95% 的結果優於此值 | L4 |
| Measurement System Analysis (MSA) | 量測系統分析 | 確認量測誤差夠小 | L5 |
| Observability | 可觀測性 | 出錯時能定位原因的能力 | L5 |
| Reproduction rate | 重現率 | 例如 3/100 | L5 |
| Flaky test | 不穩定測試 | 同條件下結果不一致的測試 | L5 |
| Bisect | 二分定位 | 二分搜尋找出引入 bug 的版本 / 參數 | L5 |
| Severity vs Priority | 嚴重度 vs 優先度 | 技術嚴重性 vs 商業急迫性 | L6 |
| Known issue / Waiver | 已知問題 / 豁免 | 帶著已知風險出貨 | L6 |
| Escape / Defect leakage | 漏測 | 出貨後才被發現的 bug | L6 |
| PVT corner | 製程 / 電壓 / 溫度極端組合 | 硬體驗證常用 | L3 |
| MTBF | 平均故障間隔 | stress / reliability 指標 | L4 |
