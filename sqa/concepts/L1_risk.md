# L1｜Risk：這個產品會怎麼壞？

> 核心問題：**如果只能測一件事，你測哪個？為什麼？**

## 核心概念

### Risk = Impact × Likelihood

| | 低機率 | 高機率 |
|---|---|---|
| **高影響** | 要測，但可以用較少次數 | **最優先，深測** |
| **低影響** | 可以砍 | 輕量測、自動化帶過 |

- **Impact**：對使用者（體驗、安全）、對客戶（退貨、lock 版本）、對公司（認證、商譽）
- **Likelihood**：新功能 > 舊功能、改動多的模組、歷史上 bug 多的地方、複雜的 interaction

### Failure Model：先想「怎麼壞」，再想「怎麼測」

| Failure 類型 | 例子 |
|---|---|
| Functional | 功能錯誤、狀態錯亂 |
| Performance degradation | 長時間跑後變慢、TTFF 變長 |
| Resource exhaustion | memory leak、handle leak、buffer overflow |
| Timing / Race | 快速切換 mode、中斷時序 |
| Environmental | 溫度、電壓、訊號強度、干擾 |
| Recovery | 異常後能不能恢復、資料會不會損毀 |

### Risk 的資訊來源

- 這版改了什麼（change log、diff）
- 過去的 bug 分佈（JIRA 統計）
- 客戶抱怨 / field issue
- 架構上的弱點（共用資源、外部依賴）

## 面試時的說法

> "Before designing test cases, I'd first ask what failure would hurt the user most, and which areas are most likely to break — for example, newly changed modules or areas with a history of field issues. That tells me where to go deep and where a light check is enough."

## 我的筆記

<!-- 讀書、練習時補充 -->
