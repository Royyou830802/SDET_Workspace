# SQA Skill 學習地圖

> 目標：從「知道怎麼展開測試」（coverage-driven）進化到「能獨立做測試決策」（risk-driven）
> 起點：Cirrus Logic feedback（2026-11）— *"good approach / good intuition, but still maturing in testing capabilities"*

---

## 六層測試架構

| 層 | 回答的問題 | 筆記 | 起點自評 |
|---|---|---|---|
| **L1 Risk** | 這個產品會怎麼壞？壞了對誰影響多大？ | [L1_risk.md](concepts/L1_risk.md) | ❌ |
| **L2 Strategy** | 每個風險用哪種測試、在哪個階段處理？ | [L2_strategy.md](concepts/L2_strategy.md) | 🔺 |
| **L3 Test Design** | 具體 test case 怎麼產生？ | [L3_test_design.md](concepts/L3_test_design.md) | ✅ |
| **L4 Oracle** | 怎樣算 pass？依據是什麼？ | [L4_oracle.md](concepts/L4_oracle.md) | 🔺 |
| **L5 Execution** | 環境、自動化、observability | [L5_execution.md](concepts/L5_execution.md) | ✅ |
| **L6 Decision** | 結果怎麼變成 ship / no-ship 的判斷？ | [L6_decision.md](concepts/L6_decision.md) | 🔺 |

術語對照：[glossary.md](concepts/glossary.md)

---

## 評分標準（每份 drill 每層打 1~3 分）

| 分數 | 意義 |
|---|---|
| **0** | 完全沒提到 |
| **1** | 有提到，但只是列項目（"I would do stress testing"） |
| **2** | 有具體做法（"ramp load from 50% to 120% over 4 hours"） |
| **3** | 有具體做法 **+ 說出判斷依據與取捨**（"because field failures are mostly thermal, I prioritize..."） |

> Senior 的門檻：L1、L4、L6 穩定拿到 2 分以上，至少一層拿到 3 分

---

## 進度追蹤

### Drill 分數紀錄

| 日期 | 題目 | L1 | L2 | L3 | L4 | L5 | L6 | 總分 |
|---|---|---|---|---|---|---|---|---|
| — | — | | | | | | | |

### Case Study

| 主題 | 狀態 | 檔案 |
|---|---|---|
| GNSS TTFF | 🟡 草稿（已有 L4 範例） | [gnss_ttff.md](case_studies/gnss_ttff.md) |
| Power Measurement | ⚪ 未開始 | [power_measurement.md](case_studies/power_measurement.md) |

### 閱讀

見 [reading/README.md](reading/README.md)

---

## 資料夾結構

```
sqa/
├── README.md          # 本檔：學習地圖 + 進度總覽
├── log.md             # 學習日誌
├── concepts/          # 六層理論筆記 + 術語
├── drills/            # How would you test X 練習題（題庫 + 模板 + 作答）
├── case_studies/      # 用真實經歷寫完整 test strategy
└── reading/           # 讀書筆記
```

## 練習流程

1. 從 [question_bank.md](drills/question_bank.md) 選題
2. 複製 [_template.md](drills/_template.md) → `drills/YYYY-MM-DD_<slug>.md`
3. 限時 10 分鐘寫第一版（寫完不修改）
4. 用六層 checklist 自評 → 找 Claude mock 追問 → 改寫
5. 分數填回上方表格，心得寫進 [log.md](log.md)
