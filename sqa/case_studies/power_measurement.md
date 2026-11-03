# Case Study：Power Measurement Test Strategy

> 用 AIROHA 低功耗新品的經驗，從 L1 寫到 L6
> 狀態：⚪ 未開始

---

## 背景

<!-- 產品、市場主打低功耗、要比較哪些版本與場景 -->

---

## L1 Risk：Power 會怎麼壞？對誰影響最大？

<!-- 提示：哪些場景最耗電？哪些改動最可能造成 power regression？使用者感受到的是什麼（續航）？ -->

---

## L2 Strategy：用哪些測試覆蓋？

<!-- 提示：哪些場景每版都要跑？哪些只在大改版跑？ -->

---

## L3 Test Design：場景怎麼組合？

<!-- 提示：版本 × 場景 × mode，怎麼挑代表性場景？ -->

---

## L4 Oracle：Pass/Fail 怎麼訂？

<!-- 提示：
- 看平均電流、峰值、還是特定 state 的電流？為什麼？
- 量測誤差多大？regression 門檻要大於誤差才有意義
- 跟行銷宣稱（Claims）、上一版（History）、競品怎麼比？
-->

---

## L5 Execution：量測可信嗎？

<!-- 提示：
- STAR #6：四台功率計 × 五個場景 → 這就是 Measurement System Analysis
- 取樣率、量測時長怎麼決定？
- 自動化結果與手動結果如何交叉驗證？
-->

---

## L6 Decision：結果怎麼回報？

<!-- 提示：報告怎麼呈現給客戶？發現 regression 時怎麼處理？ -->

---

## 連結的 STAR

- [STAR #1 Power 量測自動化](../../docs/STAR/BQ_Prep_Note.md#star1)
- [STAR #6 說服主管採購新功率計](../../docs/STAR/BQ_Prep_Note.md#star6)
