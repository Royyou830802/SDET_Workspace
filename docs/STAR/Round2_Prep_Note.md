# Roku 二面準備清單
> 職位：Automation QA Engineer | 面試關卡：Panel Interview (3 × 50min)
> 面試日期：2026-03-24（週二）
> 平台：Zoom + HackerRank CodePair

---

## 面試結構

| 場次 | 時間 | 面試官 | 人數 | 推測重點 |
|------|------|--------|------|---------|
| 1 | 1:00-1:50pm | Vincent Liu | 1人 | 技術深度 / Live coding |
| 2 | 3:00-3:50pm | Peter Song + Kevin Kuo | 2人 | 技術 + BQ |
| 3 | 4:00-4:50pm | Mason Huang | 1人 | 技術 或 Team fit / BQ |

> ⚠️ 注意：場次 2 和 3 中間只有 10 分鐘，提前準備好狀態

---

## 一、平台準備（3/21 今天完成）

### 面試前 Checklist
- [x] 用 **Chrome 最新版**（fully supported，建議優先用）
- [x] 點 sample link，用**無痕視窗**，走一遍加入流程
- [x] 跑 **System Compatibility Check**（網路、瀏覽器相容性）
- [x] 在 sample link 裡確認：
  - [x] Python 3 可以選（不是 Python 2）
  - [x] Auto-complete 有跳出來
  - [x] Tab 縮排正常
  - [x] Run Code 可以正常執行
- [x] 確認 **Zoom** 音訊/視訊正常（HackerRank 不負責音訊視訊）

### 加入流程（面試當天）
1. 用 **Chrome 無痕模式**開正式連結：`https://hr.gs/242477e`
2. 系統自動檢查環境，有問題點 See fix
3. 輸入名字 → Continue
4. 允許**麥克風**和**螢幕偵測**權限（兩個都要允許）
5. 進 Lobby 等面試官放你進來
6. 進入後點右上角齒輪 → **Take a quick tour**
7. 調整編輯器設定（Theme / Tab Size）

### AI Assistant
> 如果右側面板有出現 → Roku 有開啟，面試開始時主動問規則
> 如果沒出現 → 沒有啟用，按原計畫

### HackerRank 編輯器操作重點
- **Run Code** — 跑 sample input，確認基本邏輯
- **Run all test cases** — 跑所有 edge case，寫完才用
- **Hidden test cases** — 看不到內容，但你的 code 會跑過去
  → 跑完 sample 後主動想 edge case，跟面試官說出來：
    - 空的 input（空 list、空字串）
    - 只有一個元素
    - 全部元素相同
    - 負數、0
    - 非常大的數字（overflow）
    - 答案不存在（找不到目標值）
- **Python 輸入寫法**：
  ```python
  n = int(input())
  nums = list(map(int, input().split()))
  print(result)
  ```
- **提交前必做**：拿掉所有 debug print，確認輸出格式正確（多餘空格/換行會導致 Wrong Answer）

---

## pytest 常用指令

```bash
# 跑全部測試
pytest

# 跑全部，顯示詳細結果
pytest test_solution.py -v

# 跑單一 class
pytest test_solution.py::TestTwoSum -v

# 跑單一 function
pytest test_solution.py::TestTwoSum::test_basic -v

# 遇到第一個 fail 就停
pytest test_solution.py -x

# 查看 test coverage
pytest --cov=solution test_solution.py

# 查看哪幾行沒被測到
pytest --cov=solution --cov-report=term-missing test_solution.py
```

**coverage 輸出說明：**
```
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
solution.py      45     20    56%   12-15, 30-44
```
- **Stmts** — 總共幾行程式碼
- **Miss** — 沒有被測試跑到的行數
- **Cover** — 覆蓋率百分比
- **Missing** — 哪幾行沒有被跑到

---

## 二、演算法練習（8題）

| 優先 | 題目 | 核心概念 | 目標時間 |
|------|------|---------|---------|
| ⭐⭐⭐ | Two Sum | Hash Map | 熟到不用想 |
| ⭐⭐⭐ | Contains Duplicate | Set | 熟到不用想 |
| ⭐⭐⭐ | Longest Substring Without Repeating Characters | Sliding Window | 20 分鐘內 |
| ⭐⭐⭐ | Valid Parentheses | Stack | 15 分鐘內 |
| ⭐⭐ | Valid Anagram | Hash Map | 15 分鐘內 |
| ⭐⭐ | Best Time to Buy and Sell Stock | Array / Greedy | 15 分鐘內 |
| ⭐⭐ | Parse log / Count word frequency | String + Counter | 20 分鐘內 |
| ⭐ | Move Zeroes | Two Pointer | 10 分鐘內 |

- [x] Two Sum
- [x] Contains Duplicate
- [x] Valid Parentheses
- [x] Longest Substring Without Repeating Characters
- [x] Valid Anagram
- [x] Best Time to Buy and Sell Stock
- [x] Parse log / Count word frequency
- [x] Move Zeroes

---

## 三、pytest / Test Automation Coding

> 練習題放在 `practice/` 資料夾

### Python Class 基礎（`practice/class_practice/`）
- [x] Shape base class — `__init__`、`NotImplementedError`
- [x] Square / Circle 繼承 — `super().__init__()`、override
- [x] 跑 `test_shapes.py` 全部通過

### pytest 語法練習（`practice/pytest_practice/`）
- [x] Q1 fixture — 建立 fixture，管理 setup/teardown
- [x] Q2 parametrize — `@pytest.mark.parametrize` 多組輸入
- [x] Q3 exception — `pytest.raises` 測試例外
- [x] Q4 mock — `@patch`、`MagicMock` 隔離外部依賴
- [x] Q5 bdd — Gherkin + pytest-bdd steps 實作

---

## 四、一面弱點補強

### Flaky test / Bottleneck（一面 60分）
**Flaky test：**
- **identify & tag** flaky tests — 隔離，不讓它 block CI
- **short-term**：retry mechanism（例如 fail 3 次才算真的 fail）
- **long-term**：找 root cause（timing / environment）→ Jira → 找對的 owner
- **track stability trend** — 持續 flaky 本身就是更深層問題的訊號

**Bottleneck：**
- **identify & tag** 慢的 test — 先隔離，不影響正常 CI pipeline
- **找 root cause**：是 test 設計問題還是外部依賴（硬體、網路）
- **解法**：請 owner 修底層問題，或自己調整 test suite：
  - **parallel 執行** — 同時跑多個 test
  - **分 stage** — 快的放 PR CI，慢的放 nightly build

- [x] 練習加入 system-level 改善的說法

---

### Many issues prioritization（一面 60~65分）
補這個角度：
- **Severity**：crash / data loss 最高，UI / cosmetic 最低
- **Impact scope**：影響大量 user 或 release blocker → 高優先；edge case / 少數 user → 低優先
- **Root cause grouping**：多個 issue 同一 root cause → 合一張 ticket，fix 一次解決全部，減少 noise
- **Automation 改善**：同類問題重複出現 → 新增 automation coverage，提早在 pipeline 攔截

- [x] 練習加入 triage / grouping / automation 改善角度

---

### RD conflict（一面 65~70分）
補這個角度：
- **先理解 RD 的壓力**：deadline、scope 等
- **用數據說話**：重現率、影響範圍、user impact
- **找共識**：接受 workaround 但確保 issue 有記錄（traceable）
- **quality ownership**：As a QA owner, I need to make sure all workaround issues are documented and traceable for the future, in case we need to check the history.

- [x] 練習加入 quality ownership 說法

---

## 五、二面新技術題（一面沒問到）

| 主題 | 準備材料 | 優先 |
|------|---------|------|
| CI/CD pipeline 細節 | HM_Screen_Prep_Note T2 | ⭐⭐⭐ |
| Embedded / device testing | HM_Screen_Prep_Note T4 | ⭐⭐⭐ |
| Test coverage tracking & reporting | HM_Screen_Prep_Note T5 | ⭐⭐ |
| BDD / Behave | HM_Screen_Prep_Note T6 | ⭐⭐ |
| Code review — testability 角度 | 新題，沒準備過 | ⭐⭐ |

- [x] CI/CD pipeline — 複習 T2，練習口說 Bamboo 五步架構
- [x] Embedded / device testing — 複習 T4，練習 UART / signal simulator 說法
- [x] Test coverage tracking — 複習 T5，練習 MP Report 五個結構
- [x] BDD / Behave — 複習 T6，練習準備說法
- [x] Code review testability — 準備回答框架（見下方）

### Code Review 回答框架（新題）
> "When I review code for testability, I look for three things:
> 1. **Dependency injection** — are dependencies hardcoded or injectable? Hardcoded dependencies make mocking impossible.
> 2. **Single responsibility** — does each function do one thing? Functions that do too much are hard to unit test.
> 3. **Edge case visibility** — are boundary conditions and error paths clear from the code structure?"

---

## 六、BQ STAR（一面全部未用）

| STAR | 適用題型 | 優先 |
|------|---------|------|
| #2 韓國現場 | Challenge / Hardest part | ⭐⭐⭐ |
| #1 Power 自動化 | Initiative / 主動改善 | ⭐⭐⭐ |
| #7 外測版本錯誤 | Failure / Learning | ⭐⭐⭐ |
| #6 說服主管買儀器 | Disagree with manager | ⭐⭐ |
| #8 帶領 AE | Collaboration / Leadership | ⭐⭐ |
| #4 晶片認證 | Ambiguous / 不熟悉挑戰 | ⭐⭐ |
| #9 測試分類標準 | Proactive / Process improvement | ⭐ |
| #10 Apple Watch 競品 | Ambiguity / Constraints | ⭐ |

- [ ] STAR #2 韓國 — 練習英文口說版本
- [ ] STAR #1 Power 自動化 — 練習英文口說版本
- [ ] STAR #7 外測失誤 — 練習英文口說版本
- [ ] 自我介紹英文版 — 每場都要講，練到流暢（40~50 秒）

---

## 七、模擬面試（3/23 前一天）

- [ ] 限時 50 分鐘，全英文
- [ ] 練習四個環節：
  1. **Clarification** — 先問清楚題目
  2. **思路講清楚** — 先說 brute force，再說優化
  3. **邊寫邊說** — 不要沉默
  4. **收尾** — 說 time/space complexity

---

## 面試當天關鍵提醒

| 事項 | 說明 |
|------|------|
| 開連結 | Chrome 無痕模式 |
| 加入順序 | 開連結 → 輸入名字 → 給麥克風/螢幕權限 → 進 Lobby |
| 不要沉默 | 一直講思路，卡住說 "Let me think about this..." |
| 先 brute force | 不要直接給最優解，展示思考過程 |
| AI 使用 | 如果有開啟，邊用邊說明你的思路 |
| 每場自介 | 三個面試官都是第一次見你，每場都要自我介紹 |
| 開場問 AI 規則 | "Will the AI Assistant be available, and what are your expectations?" |

---

## 三天時間分配

| 日期 | 重點 |
|------|------|
| **3/21** | ✅ 演算法 Q1-Q8 全部完成 |
| **3/22（今天）** | 平台設定收尾 + pytest/mock 練習 + 一面弱點補強（口說） |
| **3/23（前一天）** | HackerRank CodePair 熟悉介面 + Q1-Q8 在上面跑過 + BQ 英文口說 + 模擬面試（限時 50 分鐘，全英文）|
| **3/24 早上（面試當天）** | 快速複習所有口說 + 確認連結和設備 |

---

## Complexity 速查表

### 英文念法
| 寫法 | 英文念法 |
|------|---------|
| O(1) | O of one |
| O(n) | O of n |
| O(n²) | O of n squared |
| O(log n) | O of log n |
| O(n log n) | O of n log n |

### Time Complexity
| Complexity | 常見操作 |
|------------|---------|
| O(1) | `dict[key]`、`set` 查找、`len()`、`list[index]` |
| O(log n) | Binary Search、`bisect` |
| O(n) | `for` loop、`set()`、`Counter()`、`x in list` |
| O(n log n) | `sort()`、`sorted()`、`heapq.nlargest()` |
| O(n²) | 兩層 nested loop |

### Space Complexity
| Complexity | 情況 |
|------------|------|
| O(1) | 只用固定幾個變數，不管 input 多大空間都一樣 |
| O(n) | 建了跟 input 大小成正比的資料結構（HashMap、set、list）|
| O(n²) | 建了二維結構（n x n 矩陣）或 nested loop 裡存資料 |

### 判斷口訣
- 用的空間跟 input 大小**無關** → O(1) space
- 用的空間跟 input 大小**成正比** → O(n) space
- 只要用到 `sort()` → Time O(n log n)
- `x in set` / `x in dict` → O(1) time，但 `x in list` → O(n) time
