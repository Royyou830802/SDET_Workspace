# Roku HM Screen 準備筆記
> 職位：Automation QA Engineer | 面試關卡：Hiring Manager Screen (Zoom 45~60min)
> HR Tips：把自己的 resume 跟 JD 看熟

---

## 面試結構預估
- Technical 問答（主）
- BQ / Behavioral 問答
- 時間：45min ~ 1hr

---

## Part 1：Technical

### 主題分類

| # | 主題 | 對應 JD | Roy 的彈藥 |
|---|------|---------|-----------|
| 1 | [Automation framework design](#t1automation-framework-design) | 核心職責 | AIROHA Python 腳本、個人 SDET_Workspace repo |
| 2 | [CI/CD pipeline](#t2cicd-pipeline) | 加分項 | Bamboo + Bitbucket（Zealogics）、GitHub Actions（個人 repo）|
| 3 | [Debugging / failure analysis](#t3debugging--failure-analysis) | 核心職責 | AIROHA 外測失敗分析、韓國客戶支援（STAR #2）|
| 4 | [Embedded / device testing](#t4embedded--device-testing) | 核心職責 | AIROHA GNSS 晶片測試、NCSIST 嵌入式 C |
| 5 | [Test coverage tracking & reporting](#t5test-coverage-tracking--reporting) | JD 明確提到 | AIROHA MP Report、甘特圖進度管理（STAR #8）|
| 6 | [BDD](#t6bdd備用如果被問到) | 加分項 | 概念懂，沒有 production 經驗，學習意願高 |
| 7 | [Flaky test / Bottleneck](#t7flaky-test--bottleneck) | 核心職責 | AIROHA 硬體時序問題、CI pipeline 穩定性 |
| 8 | [Many issues prioritization](#t8many-issues-prioritization) | 核心職責 | AIROHA 多版本並行、issue triage 經驗 |
| 9 | [RD conflict](#t9rd-conflict) | 核心職責 | AIROHA RD 溝通、說服主管買儀器（STAR #6）|
| 10 | [Code review — testability](#t10code-review--testability) | 加分項 | 新題，二面可能出現 |

**變化球：**

| # | 題目 |
|---|------|
| V1 | [If you join Roku, how would you approach testing a new TV OS firmware feature?](#v1if-you-join-roku-how-would-you-approach-testing-a-new-tv-os-firmware-feature) |
| V2 | [What's the hardest part of your job?](#v2whats-the-hardest-part-of-your-job) |
| V3 | [How do you work with RD when they disagree with your bug report?](#v3how-do-you-work-with-rd-when-they-disagree-with-your-bug-report) |

---

### T1：Automation Framework Design

**可能被問：**
- How do you design automated tests for a system?
- How do you design an automation framework from scratch?
- Walk me through a test framework you've built.
- How do you make tests maintainable and scalable?

**完整回答（主）：**

**Step 1 — 分析自動化優先順序**
先評估哪些測試最值得自動化：高頻執行的 regression test、需要長時間跑的 performance/stress test、還有手動很難穩定重現的場景。這些是投資報酬率最高的起點。

**Step 2 — 設計框架結構**
分層設計：test case 只描述「測什麼」，底層的操作邏輯、設備控制、log 收集抽出來變成共用的 utilities。test case 好讀好維護，底層改動也不會影響所有 test。

**Step 3 — 保留彈性，支援參數化**
透過參數化讓使用者可以選擇韌體版本、測試場景、模式，不需要改程式碼就能跑不同組合，減少人為設定錯誤。

**Step 4 — 涵蓋完整流程**
自動化不只是執行，同時處理 log 收集、結果分析、報告產出，減少手動整理跟人為失誤。

**Step 5 — 整合 CI**
接上 CI pipeline，每次 commit 自動觸發測試，結果自動回報。在 Zealogics 用 Bamboo、個人專案用 GitHub Actions 都有這樣的經驗。

---

**追問時的舉例（AIROHA UI）：**
在 AIROHA，腳本是給 AE 使用的，所以在參數化的基礎上多做了一層 UI。使用者可以選擇要測的韌體版本、場景、模式，UI 最後產出一份 task list 給 script 吃。這樣 AE 不需要懂程式也能靈活跑不同組合，降低設定錯誤，也讓我不需要每次幫他們改腳本。（對應 JD："develop new tools to improve the team's productivity"）

**關鍵字要提：**
PyTest, fixtures, parameterized tests, test utilities, CI integration

---

**四題的回答策略：**

| 題目 | 策略 |
|------|------|
| How do you design automated tests for a system? | 用完整 5 steps 回答 |
| How do you design an automation framework from scratch? | 同上，強調 Step 2（分層結構）|
| Walk me through a test framework you've built. | 用 AIROHA Power 量測自動化完整說明（見下方 Q3 完整回答）|
| How do you make tests maintainable and scalable? | 抽 Step 2（分層）+ Step 3（參數化）回答 |

> 注意：Q1 跟 Q2 幾乎可以用同一份答案，Q3 需要具體例子，Q4 是 Q1 的子集。

---

**Q3 完整回答（AIROHA Power 量測自動化）：**

**背景：**
在 AIROHA 測試 GNSS chip 的 power 時，整個測試是多層巢狀組合：SW 版本 × 電力模式 × 場景，每一輪都要手動控制儀器、等待 chip 穩定、量測、記錄，非常耗時。

**腳本分三層：**

- **儀器控制層**：用 Python 控制 Signal Simulator（播放衛星場景）、Relay Board（切斷路）、Power Meter（量測電流），把手動操作儀器的部分完全自動化。

- **裝置控制 + 狀態監測層**：控制 GNSS chip 進入指定電力模式，並即時監測 chip 回傳的 log，確認定位穩定後才觸發量測，避免在不穩定狀態下取到錯誤數據。

- **結果記錄 + 分析層**：量測完成後自動讀取 log，換算成 power（電流 × 對應斷路的理論電壓），並對應 SW 版本、電力模式、場景自動填入結果報表，省去人工換算和填表可能產生的失誤。

**使用者介面整合：**
搭配 UI，使用者只需要架設好測試環境（接好儀器、燒好 firmware），在 UI 選定 task list，整個多層巢狀的組合就會自動依序跑完，不需要人在旁邊盯著或手動切換。

**成果：**
測試時間從一週縮短至三天，並可利用晚上和週末無人值守執行，同時消除人工量測和填表的人為誤差。

**關於 CI/CD 的說明（如果被追問）：**
AIROHA 的測試需要實體硬體（Signal Simulator、Relay Board、Power Meter），沒辦法像純軟體一樣 commit 觸發自動跑，所以 issue triage 和 JIRA 還是跟 RD 討論後手動處理。這是 hardware-in-the-loop 測試的現實限制。CI/CD 的經驗來自 Zealogics（Bamboo regression pipeline）和個人專案（GitHub Actions）。

---

### T2：CI/CD Pipeline

**可能被問：**
- What CI/CD tools have you used?
- How do you integrate automation tests into a pipeline?
- Have you used Jenkins?
- Walk me through a CI/CD pipeline you've worked with.

**完整回答（主）：**

我用五個步驟來說明 CI/CD pipeline 的運作，以我在 Zealogics 的 Bamboo pipeline 為例：

**Step 1 — Code change trigger**
QA 在自己的 branch 新增或維護完 test cases 後，pull main branch 確認沒有 conflict，commit 後在 Bamboo 開 PR，手動 trigger pipeline 選擇要跑的 SW 版本。另外每天也有 daily automated run 自動執行。

**Step 2 — Run automated tests**
Pipeline 裡有兩個 stage 平行執行：
- **E2E test**：驗證 UI 上的欄位、按鈕、元件是否如規格運作
- **Regression test**：驗證使用者完整操作一個 feature 的流程是否正常

**Step 3 — Collect and analyze results**
Daily test 有 fail 時會收到通知，分析是 test case 本身的問題、環境問題，還是真正的 product bug，再決定對應處理方式。

**Step 4 — Report results and track failures**
確認是 bug 後開 JIRA 票，追蹤到 RD 修復並驗證通過。

**Step attach — Build the software**
這步由 DevOps / RD 負責，QA 不直接參與，但我們的 test cases 會被 RD 的 PR pipeline 抓去跑，確認 pass 才能 merge。
---

**我的角色定位：**
主要參與 Step 1、3、4、5。pipeline 本身的建置是 DevOps 負責，但我對整個流程很熟，理解 QA 的 test cases 怎麼卡在開發流程裡發揮作用。

**Jenkins gap 處理：**
> 「沒有直接用過 Jenkins，但 Bamboo 是同類工具，概念相同：trigger、stage、artifact、report。個人專案也有用 GitHub Actions 寫 YAML workflow。相信可以快速上手 Jenkins。」

---

**四題的回答策略：**

| 題目 | 策略 |
|------|------|
| What CI/CD tools have you used? | 直接回答：Bamboo（production）、GitHub Actions（個人專案），Jenkins 沒用過但概念相同 |
| How do you integrate automation tests into a pipeline? | 用五步架構說明，重點在 Step 1、3 |
| Have you used Jenkins? | Jenkins gap 處理說法 |
| Walk me through a CI/CD pipeline you've worked with. | 用完整五步 + Zealogics Bamboo 例子回答 |

> 注意：Q1 需要簡短直答，Q4 才展開五步。不要每題都講五步。

---

### T3：Debugging / Failure Analysis

**可能被問：**
- How do you approach a test failure you've never seen before?
- Walk me through a time you found a tricky bug.
- How do you prioritize which failures to investigate?

---

**Q1 完整回答：How do you approach a test failure you've never seen before?**

**Step 1 — Reproduce**
確認問題能不能穩定重現，排除偶發性。

**Step 2 — Version comparison**
比對前後版本，確認是不是新版本才出現的，縮小問題引入點。

**Step 3 — Log analysis**
看 log 找異常點，觀察問題發生時有沒有其他異常同時發生。

**Step 4 — 三分法判斷**
根據以上資訊判斷根本原因屬於哪一類，決定後續處理方向：
- **環境問題** → QA 自己修測試環境
- **Test case 問題** → 修 test case（例如 spec 更新但 test 沒跟上）
- **Software defect** → 帶資料找 RD 討論

**Step 5 — 同步 RD（若是 software defect）**
整理好：重複性、版本比對結果、log 異常資訊，帶著數據找 RD，不是空手去問，然後開 JIRA 追蹤到修復驗證通過。

---

**Q2 完整回答（STAR #2）：Walk me through a time you found a tricky bug.**

**S（情境）：**
在韓國外測期間，SW 版本即將 lock，需要針對 GNSS 定位品質跟競品進行對標，測試項目包含定位軌跡與 TTFF（Time to First Fix）。

**T（任務）：**
分析 road test 數據，找出定位品質差於競品的根本原因，整理出有效的 debug 資訊給 RD。

**A（行動）：**

1. **發現異常**：對標後發現兩類問題：
   - 定位軌跡：橋下場景失去定位、玻璃帷幕場景軌跡偏移，競品兩者皆正常
   - TTFF：HTTFF / CTTFF 在部分場景明顯慢於競品

2. **系統性分析：**
   - 用自行開發的分析工具，檢查 TTFF 差的時候是否有資訊沒有正確 inject
   - 分析收星數量與訊號強度是否符合預期
   - 判斷問題根源屬於哪一類：場景本身的訊號限制 / 收星不足 / software defect

3. **整理結論給 RD：**
   將可能原因分類，帶著數據找 RD 討論，明確區分哪些是環境限制、哪些需要程式修正

**R（結果）：**
- **定位軌跡**：RD 補強橋下場景的 dead reckoning（失去定位後以速度外差持續打點），玻璃帷幕場景則根據實際道路將定位 snap 回路線
- **TTFF**：RD 調整資料 inject 順序；同時發現某些功能開啟會干擾 GPS 訊號，測試手法同步更新，要求測試時關閉所有非 GPS 功能確保數據有效性

---

**三題的回答策略：**

| 題目 | 策略 |
|------|------|
| How do you approach a test failure you've never seen before? | 用 Q1 五步流程回答 |
| Walk me through a time you found a tricky bug. | 用 STAR #2（韓國 road test）回答 |
| How do you prioritize which failures to investigate? | 用三分法 + 影響範圍判斷（見下方備註）|

**Q3 完整回答：How do you prioritize which failures to investigate?**

我用兩個維度來判斷優先順序：**影響對象** 和 **影響範圍**。

**第一優先 — 客戶回報 / 外部測試問題**
直接影響真實使用者，有明確的 deadline 壓力，必須最快處理。在同一層裡，再用影響範圍排序：關鍵功能失效（例如定位完全喪失）優先於效能問題（例如 TTFF 慢一點）、影響多個場景的問題優先於單一 edge case。

在 AIROHA，我曾被派駐韓國客戶現場，整個期間就是全力處理外部測試發現的問題，定位軌跡和 TTFF 這些客戶在意的指標都要優先收斂。

**第二優先 — 影響版本驗證的內部 failure**
例如 regression failure 或 block 整個 test suite 的問題，不修就沒辦法過版，必須快速處理。

**第三優先 — 其他內部 failure**
單一 edge case 或不影響 release 的問題，記錄下來，有資源再排進去處理。

---

### T4：Embedded / Device Testing

**可能被問：**
- What's different about testing embedded products vs. software?
- How do you test hardware-dependent features?
- Have you worked with serial/UART communication, hardware setup?

---

**Q1 完整回答：What's different about testing embedded products vs. software?**

最大的差別是引入了 **hardware 變數**，帶來兩個核心挑戰：

**1. 測試前需要先排除環境和手法問題**
- 純 software testing：發現問題 → 重現 → 找 RD 討論
- Embedded testing：發現問題 → **先確認自己的測試環境和手法沒問題** → 再找 RD
- 例如測 GNSS chip 前，需確認：firmware 版本、硬體接線、SOP 前置設定、UART log 顯示 chip 進入預期狀態
- 任何一步沒做好，測出來的結果都可能是假的

**2. 重現性需要主動控制**
- 真實環境難以穩定重現極端狀況，或根本沒辦法控出相同條件
- 解法：用 signal simulator 建立受控環境，確保測試條件一致、結果可重複
- 真實環境測試則用來驗證產品在實際場景下的表現
- 兩種環境互補，缺一不可

---

**Q2 回答策略：How do you test hardware-dependent features?**
→ 與 Q1 高度重疊，用同樣的 AIROHA 例子回答，強調分層測試（受控環境 + 真實環境）和自動化控制儀器的部分。

---

**Q3 完整回答：Have you worked with serial/UART communication, hardware setup?**

有，在 AIROHA 有三種 hardware communication 經驗：
- **UART**：AG3335 開發板透過 UART to USB 跟電腦溝通，用來控制 chip 和即時監測 log
- **Serial（EagleCom）**：接收競品的 NMEA 資料，用於對標分析
- **Serial port（Relay Board）**：用 bit 值控制要開哪個 channel，切斷路進行 power 量測

---

**三題的回答策略：**

| 題目 | 策略 |
|------|------|
| What's different about testing embedded products vs. software? | 用 Q1 兩個核心挑戰回答 |
| How do you test hardware-dependent features? | 同 Q1，強調分層測試和儀器自動化 |
| Have you worked with serial/UART communication, hardware setup? | 直接列三種 communication 經驗 |

**HDMI/HDCP/Audio/Video 未接觸：**
> "I don't have direct experience with HDMI/HDCP, but HR mentioned this can be trained on the job. My background in signal-level testing with GNSS and hardware setup gives me a solid foundation to learn."

---

### T5：Test Coverage Tracking & Reporting

**可能被問：**
- How do you track test coverage across firmware components?
- How do you report test results to stakeholders?
- What does your test report typically include?

---

**Q1 完整回答：How do you track test coverage across firmware components?**

在 embedded 環境下，傳統 code coverage 工具很難直接套用。我的做法是維護一份完整的測試項目清單，對應各個 firmware component、測試模式和測試類別（Functional、Edge、Performance、Stress、Concurrency），用執行狀態和 pass rate 來追蹤覆蓋程度。

本質上這就是一個 **traceability matrix**：每條測試對應到一個 feature 或 component，可以清楚看出哪些覆蓋了、哪些還沒跑到。這份清單最後整理成 Excel 附件，確保每一條測試都有步驟和結果可追溯。

---

**Q2 完整回答：How do you report test results to stakeholders?**

我在 AIROHA 製作的 MP Report 結構：

1. **甘特圖**：呈現測試期程和完成度，讓 stakeholder 快速掌握進度；並簡述功能、標註各測試類別的規劃數量
2. **Brief table**：對應 mode × chip × test category 展開的 pass rate 總覽表
3. **詳細圖表**：將可量化的結果視覺化，例如 HTTFF 在不同 signal power 下是否符合 spec
4. **JIRA ticket 彙整**：所有 defect 的追蹤狀態
5. **Excel 附件**：完整測項、步驟、結果，確保可追溯

---

**Q3 回答策略：What does your test report typically include?**
→ 同 Q2，直接引用 MP Report 五個結構回答即可。

---

**三題的回答策略：**

| 題目 | 策略 |
|------|------|
| How do you track test coverage across firmware components? | traceability matrix 概念 + Excel 附件說明 |
| How do you report test results to stakeholders? | MP Report 五個結構 |
| What does your test report typically include? | 同上 |

---

### T6：BDD（備用，如果被問到）

**Roy 目前狀況：** 概念懂，沒有實際 framework 經驗

**BDD 核心概念**

測試用人類可讀的語言描述，格式叫 **Gherkin**：

```gherkin
Feature: GNSS Power Measurement

  Scenario: Measure power in acquisition mode
    Given the chip firmware version is "v2.3.1"
    And the signal simulator is broadcasting GPS scenario "urban"
    When the chip enters acquisition mode
    Then the current measured by power meter should be below 50mA
```

三個關鍵字：
- **Given**：前置條件（環境設定好）
- **When**：觸發動作
- **Then**：預期結果

**Behave 框架運作方式**

`.feature` 檔案寫 Gherkin 描述，Python 的 `steps` 檔案對應執行：

```python
from behave import given, when, then

@given('the chip firmware version is "{version}"')
def step_set_firmware(context, version):
    context.firmware = version

@when('the chip enters acquisition mode')
def step_enter_acquisition(context):
    context.chip.set_mode("acquisition")

@then('the current measured should be below {threshold}mA')
def step_check_current(context, threshold):
    assert context.power_meter.read() < float(threshold)
```

**pytest-bdd 框架運作方式**

pytest-bdd 是 pytest 的 plugin，讓 pytest 支援 Gherkin 寫法。底層邏輯不變，還是找 `test_` function 來跑：

```python
from pytest_bdd import scenario, given, when, then

# @scenario 把這個 test function 綁定到 .feature 裡的特定 Scenario
# test_power 本身是空的，實際邏輯在 @given/@when/@then 裡
@scenario('power.feature', 'Measure power in acquisition mode')
def test_power():
    pass

@given('the chip enters acquisition mode')
def enter_mode(chip):
    chip.set_mode("acquisition")

@when('the power meter starts measuring')
def start_measure(power_meter):
    power_meter.start()

@then('the current should be below 50mA')
def check_current(power_meter):
    assert power_meter.read() < 50
```

執行流程：
```
pytest 跑 test_power()
  → @scenario 說：去 power.feature 找對應 Scenario
  → 依序執行 @given → @when → @then
```

**Behave vs pytest-bdd**

| | Behave | pytest-bdd |
|--|--------|-----------|
| 進入點 | `.feature` 檔 | `test_` function |
| 需要 pytest | ❌ | ✅ |
| 執行指令 | `behave` | `pytest` |
| 關係 | 獨立工具 | pytest plugin |

兩者都支援 Gherkin，各自獨立開發，沒有繼承關係。

**準備說法：**
> "I'm familiar with the BDD concept — writing test cases in Gherkin format (Given/When/Then) to align QA, dev, and PM on expected behavior. I haven't used Behave in production, but I've read through examples and understand the structure. I'd be comfortable picking it up."

**BDD 核心價值（口說重點）：**
- feature file 用純英文寫，PM / system engineer 都能直接讀懂
- 讓所有人都能參與定義測試場景，驗證測試內容是否符合 requirements
- 沒有 production 經驗，但有用 pytest-bdd 練習過，可以快速上手

---

## 變化球題目

### [V1：If you join Roku, how would you approach testing a new TV OS firmware feature?](#v1if-you-join-roku-how-would-you-approach-testing-a-new-tv-os-firmware-feature)

這題考的是你能不能把自己的框架套用到新產品。

**Step 1 — 理解 feature 的影響範圍**
先確認這個 feature 涉及哪些 OS 層面：UI、network stack、hardware interface、還是 audio/video pipeline。

**Step 2 — 從測試金字塔規劃（先手動）**
- **Functional test**：feature 是否按規格運作
- **Regression test**：新版本是否影響舊功能
- **Performance test**：啟動時間、記憶體使用、response time
- **Stress test**：長時間運行、極端條件下的穩定性
- **Edge case**：網路不穩、低記憶體、異常輸入

先手動跑，確認測試手法有效、結果符合預期，再評估自動化優先順序。

**Step 3 — 評估自動化優先順序**
高頻執行的 regression 優先自動化，然後是 performance/stress。套用 T1 的 5 steps framework。

**Step 4 — 接上 CI pipeline**
自動化測試整合進 CI，commit 觸發自動跑，結果自動回報。

**Step 5 — 類比 GNSS 經驗**
TV OS 跟 GNSS 晶片類似：都是 embedded system，都需要 controlled environment + real world validation 兩種測試互補。

---

### [V2：What's the hardest part of your job?](#v2whats-the-hardest-part-of-your-job)

用 STAR #2（韓國）回答，重點放在：困難 + 我怎麼克服 + 我學到什麼。

> 「在韓國現場，版本即將 lock，大量數據需要快速分析，沒有現成工具，時間壓力極大。我跟台灣同事合作開發分析工具、建立 SOP、建立共享平台加速資訊流通。我學到 QA 在關鍵時刻能快速建立分析能力、跟客戶需求直接對接，才是真正的價值所在。」

---

### [V3：How do you work with RD when they disagree with your bug report?](#v3how-do-you-work-with-rd-when-they-disagree-with-your-bug-report)

直接用 **STAR #5（RD 意見分歧）**，詳見 [BQ_Prep_Note.md](BQ_Prep_Note.md)。

---

## Part 2：BQ

> 詳細內容請見 [BQ_Prep_Note.md](BQ_Prep_Note.md)

---

## 面試準備 Checklist

- [x] T1 Automation Framework：練習口頭說一遍 STAR #1 + SDET_Workspace
- [x] T2 CI/CD：準備 Jenkins gap 說法，練習 Bamboo + GitHub Actions 的描述
- [x] T3 Debugging：練習 STAR #2（韓國）分析步驟版本
- [x] T4 Embedded：整理 GNSS 測試流程的英文說法
- [x] T5 Coverage Reporting：整理 MP Report 的結構
- [x] BDD：讀一遍 Behave 基本用法
- [ ] BQ STAR：選 3~4 個主力故事，練習英文版
- [ ] 自我介紹：準備 2 分鐘英文版（技術重點）

---

## 關鍵 Gap 處理總結

| Gap | 說法 |
|-----|------|
| Jenkins | 有 Bamboo + GitHub Actions，概念相同，可快速上手 |
| BDD / Behave | 了解概念，沒有 production 經驗，學習意願高 |
| HDMI/HDCP/Audio/Video | HR 確認可進去培養，類比 GNSS signal testing 背景 |
| CI/CD pipeline dev | Bamboo pipeline 操作 + GitHub Actions YAML 有經驗 |

---

## 測試基礎概念複習

### 測試金字塔（Testing Pyramid）

```
        /\
       /E2E\        ← 少量，跑完整流程，慢
      /------\
     /Integr- \     ← 中量，測模組間互動
    / ation    \
   /------------\
  /  Unit Tests  \  ← 大量，測最小單元，快
 /________________\
```

| 層級 | 測什麼 | 特性 |
|------|--------|------|
| Unit | 最小單元（函式、模組） | 快、穩定、數量最多 |
| Integration | 模組之間的互動 | 中等速度、測介面和資料流 |
| E2E | 完整使用者流程 | 慢、最接近真實場景、數量最少 |

**重要觀念：**
- 金字塔層級（Unit/Integration/E2E）= 測試的**範圍**
- 測試類型（Functional/Edge/Performance/Stress...）= 測試的**目的**
- 兩個維度獨立，可以任意組合。例如同一個測試可以同時是 API test + Functional test + Regression test

---

### 測試類型總覽

**按目的分類：**

| 類型 | 測什麼 | 問的問題 |
|------|--------|---------|
| Functional | 功能是否如規格運作 | 「這個功能有沒有做到？」|
| Edge case | 邊界條件、極端輸入 | 「在異常情況下會不會壞？」|
| Performance | 速度、反應時間、資源使用 | 「夠不夠快？夠不夠省？」|
| Stress | 極限負載下的穩定性 | 「壓爆它會怎樣？」|
| Regression | 新版本是否影響舊功能 | 「改了這裡，其他地方有沒有壞？」|
| Smoke | 最基本功能是否正常 | 「這個版本能不能跑？」|
| Sanity | 特定修改是否有效 | 「這個 bug fix 有沒有修好？」|
| Compatibility | 不同環境/版本下是否正常 | 「換了硬體或 OS 還能跑嗎？」|
| Usability | 使用者體驗是否合理 | 「好不好用？」|
| Security | 是否有安全漏洞 | 「會不會被攻擊？」|

**按對象/範圍分類：**

| 類型 | 測什麼 | 說明 |
|------|--------|------|
| API test | API 的行為是否正確 | 廣義，涵蓋 functional/edge/performance 等各目的 |
| Contract test | 兩個服務之間的介面約定是否被遵守 | API test 的子集，專注在格式和結構一致性 |
| UI test | 使用者介面的操作行為 | 通常在 E2E 層 |

> **Contract test vs Output validation：**
> Output validation 是單方面驗證自己的輸出是否正確；Contract test 強調雙方都要遵守同一個介面約定。概念相近但 contract test 多了「雙方約定」的維度。

---

**Roy 的實際經驗對照：**

| 測試類型 | 對應經歷 |
|---------|---------|
| Performance | AIROHA Power 量測、TTFF 測試 |
| Stress | AIROHA 長時間定位穩定性測試 |
| Edge case | AIROHA 橋下/玻璃帷幕極端場景 |
| Regression | AIROHA 每季發版、Zealogics Bamboo pipeline |
| Smoke | 每次新版本燒錄後確認基本功能 |
| Sanity | RD 修完 bug 後驗證修正有效 |
| Compatibility | GNSS 晶片跨 SDK 版本驗證、跨客戶平台驗證 |
| Contract / Output validation | Zealogics：UI 操作後驗證 recipe 檔案格式是否符合規格 |

> JD 特別提到 Non-Functional Testing（Performance + Stress）→ Roy 兩個都有實際經驗，可以大方說。

---

### T7：Flaky Test / Bottleneck

**可能被問：**
- How do you handle flaky tests in your automation suite?
- What do you do when your CI pipeline has performance bottlenecks?
- How do you ensure test stability?

**Flaky Test 回答框架：**

**Step 1 — Identify & tag**
先把 flaky tests 標記出來，隔離，不讓它們 block 正常的 CI pipeline。

**Step 2 — Short-term**
加入 retry mechanism。例如 fail 3 次才算真的 fail，避免偶發性失敗造成誤報。

**Step 3 — Long-term**
找 root cause：可能是 timing issue（硬體回應時間不穩定）、environment dependency（外部服務不穩定）、或 test order dependency（test 之間有隱性依賴）。找到後開 Jira、找對的 owner 解決，直到問題關閉。

**Step 4 — Track stability trend**
持續追蹤 flaky test 的穩定性趨勢。如果修完還是持續 flaky，本身就是訊號——可能有更深層的架構問題需要處理。

---

**Bottleneck 回答框架：**

**Step 1 — Identify & tag**
先找出哪些 test 最慢，標記出來，不讓它們拖慢主要的 CI pipeline。

**Step 2 — 找 root cause**
是 test 設計問題（不必要的 sleep、重複 setup）還是外部依賴（硬體、網路）造成的？

**Step 3 — 解法**
- 請 owner 修底層問題
- 或自己調整 test suite：
  - **Parallel 執行** — 同時跑多個 test
  - **分 stage** — 快的放 PR CI，慢的移到 nightly build

**Roy 的實際經驗：**
AIROHA 硬體測試常遇到硬體時序問題導致 flaky，會先看 log 找 timing 差異，再跟 RD 確認硬體 spec，調整 timeout 設定或加 retry 邏輯。

---

### T8：Many Issues Prioritization

**可能被問：**
- How do you prioritize when there are many bugs at the same time?
- How do you decide what to fix first before a release?
- Walk me through your bug triage process.

**回答框架：**

**Step 1 — Severity**
Crash 或 data loss 最高優先；functional issue 次之；UI / cosmetic 最低。

**Step 2 — Impact scope**
影響大量 user 或 release blocker → 高優先；edge case 或少數 user → 低優先。

**Step 3 — Root cause grouping**
找 pattern：多個 issue 同一 root cause → 合一張 ticket，fix 一次解決全部，減少 noise。

**Step 4 — Automation 改善**
同類問題重複出現 → 新增 automation coverage，下次提早在 pipeline 攔截。

**Roy 的實際經驗：**
AIROHA 多版本並行時常有大量 issue 同時出現，會先依 severity 分類，再找 RD 確認 root cause，把同源問題合票處理。

---

### T9：RD Conflict

**可能被問：**
- How do you handle disagreements with RD about bug priority?
- Tell me about a time you had a conflict with a developer.
- What do you do when RD says your bug is not a bug?

**回答框架：**

**Step 1 — 理解 RD 的壓力**
先表達理解：deadline、scope 的壓力是真實的，不是對立關係。

**Step 2 — 用數據說話**
拿出重現率、影響範圍、user impact 的數據，讓討論有依據而不是主觀爭論。

**Step 3 — 找共識、接受妥協**
可以接受 workaround 或延後修復，但底線是：所有 issue 必須有 Jira 記錄，traceable。

**Step 4 — Quality ownership**
> "As a QA owner, I need to make sure all workaround issues are documented and traceable for the future, in case we need to check the history."

**Roy 的實際經驗：**
→ **STAR #5**：AIROHA 每季發版後 RD 對提出的 issue 有不同看法，甚至質疑測試手法。用數據說話、整理提案在正式會議上討論，建立雙方都能遵循的測試標準並文件化。
→ **STAR #6**（備用）：說服主管採購新功率計，用實驗數據讓對方沒辦法反駁。

---

### T10：Code Review — Testability

**可能被問：**
- When you review code, what do you look for from a testability perspective?
- How do you make sure the code your team writes is easy to test?
- What makes code hard to test?

**回答框架：**

> "When I review code for testability, I look for three things:"

**1. Dependency injection**
Are dependencies hardcoded or injectable? Hardcoded dependencies make mocking impossible.
```python
# ❌ hardcoded — 無法 mock
def get_firmware():
    return requests.get("https://api.example.com/firmware")

# ✅ injectable — 測試時可以傳 mock
def get_firmware(client=requests):
    return client.get("https://api.example.com/firmware")
```

**2. Single responsibility**
Does each function do one thing? Functions that do too much are hard to unit test — you can't isolate the logic you want to verify.

**3. Edge case visibility**
Are boundary conditions and error paths clear from the code structure? If error handling is buried or implicit, it's easy to miss in tests.

**Roy 的實際經驗：**
這題以概念回答為主，強調你看 code 時會主動從 testability 角度思考，是 QA 的附加價值。面試時不需要舉具體 project 例子，說清楚三個框架就夠。
