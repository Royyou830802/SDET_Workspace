# STAR 面試故事：Vector Readiness Tracking v2 重構專案

> **適用問題：** 「請說一個你主導過的重構或改善專案」、「描述一次你解決複雜技術問題的經驗」、「你如何確保程式碼品質？」、「你有沒有參與過 AI-assisted 開發的經驗？」

---

## 🎯 口說版本（1.5～2 分鐘）

> 「我們團隊有一套 ATE 晶片測試程式的自動化生成系統，我負責其中 vector readiness tracking 這個模組。這個模組是整個 pipeline 的資料基礎，但原本是由 4 個耦合的 Python scripts 組成，邏輯混雜、難以維護。
>
> 我的任務是把它重構成模組化框架，同時要保持向後相容，讓現有使用者不受影響。
>
> 我引入了 Strategy Pattern，讓 ATPG 和 TDF 兩種不同的測試類型各自有完整獨立的邏輯，並建立了 regression tests 來確保重構後的輸出跟原版一致。過程中也發現並修了幾個隱藏的 bugs，例如方法呼叫順序導致的資料錯誤。除了程式碼，我也同步維護了完整的技術文件，讓這個模組可以接入團隊正在建立的 AI-assisted workflow。
>
> 最後 29 個 unit tests 及 2 個 blocks 的 regression tests 全數通過，新架構讓之後要新增 block type 的成本大幅降低，也可以和舊版並行運行讓團隊漸進式遷移。」

---

## 📋 完整 STAR 素材庫（供追問時使用）

### S — Situation（背景）

- 團隊有一套完整的 **ATE 晶片測試程式自動化生成系統**（涵蓋 SCAN、MEM 等多個 block）
- 我負責其中的 **vector readiness tracking 模組**，這是整個 pipeline 的 Stage 1，負責追蹤晶片測試向量的準備狀態，是後續所有生成步驟的資料基礎
- 原本由 **4 個獨立的 Python scripts** 組成：
  - `vector_readiness_tracking.py`（主流程）
  - `getfilecrossserver.py`（跨伺服器 SFTP 下載）
  - `rpat_tss_integrate.py`（TSS vs RPAT 資料比對）
  - `labelparing_microcode.py`（header/payload 配對與 burst name 生成）
- 這些 scripts 之間**耦合度高、邏輯混雜**，ATPG 和 TDF 兩種 block 類型的邏輯散落各處
- 每次新增功能或修 bug 都需要同時改多個地方，維護成本越來越高
- 團隊同時在推動 AI-assisted workflow，這個模組需要有足夠清晰的文件和架構，才能讓 AI agent 理解和操作

---

### T — Task（任務）

- 負責這個模組的**完整重構**
- 目標：
  1. 建立模組化架構，實現關注點分離（separation of concerns）
  2. 達到 **true block independence**：ATPG 和 TDF 各自擁有完整、獨立的工作流程邏輯
  3. 保持向後相容的 CLI 介面，讓現有使用者無需改變使用方式
  4. 建立完整的自動化測試，確保重構後的輸出與原版完全一致
  5. 同步維護技術文件，讓模組可以接入 AI-assisted workflow

---

### A — Action（行動）

#### 架構設計
- 引入 **Strategy Pattern** 作為核心架構
  - ATPG 和 TDF 各自成為獨立的 strategy，包含完整的工作流程邏輯
  - 設計 `BaseStrategy` 抽象介面，提取共用方法（`get_mode()`、`get_core()`、`get_sku()` 等）
  - **減少約 40-50% 的程式碼重複**
- 整體分層架構：Config Layer → Strategy Layer → Core Modules → Utils

#### 測試策略
- 建立 **regression tests**：同時執行 v1 和 v2，逐欄比對 Excel 輸出
- 任何差異都會被自動捕捉，確保重構不破壞現有行為

#### 文件化（AI-assisted workflow 整合）
- 同步維護 `PROJECT_STATUS.md`、`CHANGELOG.md`、架構圖等技術文件
- 文件設計目標：讓 AI agent 進入專案時能立刻理解當前狀態、繼續工作
- 這是團隊 AI-assisted workflow 的一部分，文件即是 AI 的「記憶」

#### 關鍵 Bug 修復（展示 debugging 能力）

| Bug | 問題描述 | 根本原因 | 解法 |
|-----|---------|---------|------|
| 方法呼叫順序 | 38 筆資料出現 NaN vs 0 差異 | `_add_slice_counts()` 在 `_add_tss_port_info()` 之前執行，但前者依賴後者產生的欄位 | 調整方法呼叫順序 |
| Port aggregation key 不匹配 | 879 筆向量的 port 資訊變成 NaN | Port 聚合使用帶 slice 編號的向量名稱，但 merge 時使用 base vector name | 複製 v1 的 `get_base_vector` 邏輯（判斷 slice 部分是否為純數字） |
| Join 類型錯誤 | Row count 不一致 | `left join` 無法保留跨 block 合併後的「ghost rows」 | 改為 `outer join`，確保 row count 完全一致（4110 rows） |

---

### R — Result（結果）

- ✅ 4 個耦合的 scripts → 模組化框架，Phase 1-5 全部完成
- ✅ **29/29 unit tests 全數通過（100%）**
  - 16 個 vector processing tests
  - 13 個 strategy regression tests
- ✅ 向後相容，v1 和 v2 可並行運行，支援漸進式遷移
- ✅ 新增 block type 只需繼承 `BaseStrategy` 並實作 4 個方法，擴展成本大幅降低
- ✅ 系統性 debugging 將 TDF ATEinfo 差異從數千筆縮減到僅剩格式性差異（內容完全一致）
- ✅ 完整技術文件讓模組成功接入團隊的 AI-assisted workflow

---

## 💬 常見追問與回答方向

**「為什麼選擇 Strategy Pattern？」**
> ATPG 和 TDF 的工作流程步驟數量不同（17 步 vs 18 步），且有各自獨特的邏輯。Strategy Pattern 讓兩者完全獨立，互不干擾，也讓未來新增 block type 變得直觀。

**「regression test 怎麼做？」**
> 同時執行 v1 和 v2，比對兩者產出的 Excel 報表（每一欄、每一列），任何差異都會被記錄下來。這讓我可以有信心地重構，知道任何 regression 都會被抓到。

**「遇到最難的 bug 是什麼？」**
> Port aggregation key 不匹配的問題。表面上是 879 筆資料的 port 欄位變成 NaN，但根本原因是 slice 向量的命名規則很複雜（例如 `vector_slc_16__dbg1410_50pct`），簡單的 regex 無法處理。最後需要深入分析 v1 的邏輯，完整複製其判斷 base vector name 的方式才解決。

**「你說的 AI-assisted workflow 是什麼意思？」**
> 我們團隊在把整個測試程式生成系統升級成可以讓 AI agent 協作操作的形式。我負責的這個模組，除了程式碼重構，也同步建立了完整的技術文件（PROJECT_STATUS、CHANGELOG、架構圖），讓 AI 進來就能理解當前狀態、繼續工作，而不需要人工解釋。

---

## 🔧 技術亮點（視職位調整強調重點）

| 面向 | 亮點 |
|------|------|
| 設計模式 | Strategy Pattern + Factory Pattern 實際應用 |
| 測試工程 | Regression tests、100% unit test pass rate |
| 資料工程 | pandas DataFrame 複雜聚合、join、比對操作 |
| 跨伺服器架構 | COMET server 透過 SSH/SFTP 協調 SD server 執行任務 |
| 資料庫整合 | Oracle TSS database 查詢與快取機制 |
| AI-assisted 開發 | 文件設計考量 AI agent 的可讀性，接入團隊 AI workflow |

---

*建立日期：2026-03-16*
*最後更新：2026-03-16*