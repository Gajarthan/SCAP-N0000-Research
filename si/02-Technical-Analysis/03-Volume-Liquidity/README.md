# 03 · පරිමාව සහ ද්‍රවශීලතා විශ්ලේෂණය

[← තාක්ෂණික විශ්ලේෂණය](../README.md) · [English](../../../02-Technical-Analysis/03-Volume-Liquidity/README.md) · [தமிழ்](../../../ta/02-Technical-Analysis/03-Volume-Liquidity/README.md) · [සිංහල](README.md)

> **SCAP.N0000 — Softlogic Capital PLC.** **තත්ත්වය: ක්‍රමවේදයක් පමණි; වත්මන් trading signal එකක් නොවේ.** මුලින් දත්ත හා CSE ගනුදෙනු දින තහවුරු කරන්න. **Reference: 2026-09-30.**

## 🎯 පර්යේෂණ ප්‍රශ්නය

විශාල slippage හෝ ප්‍රමාදයකින් තොරව අවශ්‍ය ප්‍රමාණයේ SCAP කොටස් මිලදී ගැනීමට හා විකිණීමට හැකිද?

## 🔍 දත්ත සහ ක්‍රම තහවුරු කිරීම

- [ ] සමාන කාලවල traded shares, දෛනික turnover, trade count සහ ගනුදෙනු නොවූ දින ගණන සටහන් කරන්න.
- [ ] bid-ask spread, order-book depth හා නියමිත order ප්‍රමාණය ක්‍රියාත්මක කිරීමේ පිරිවැය මැනන්න.
- [ ] අසාමාන්‍ය volume සහ දින සහිත corporate news, free float, block trades අතර සම්බන්ධය පරීක්ෂා කරන්න.

## 🧭 ක්‍රමවේද සටහන

```mermaid
flowchart LR
  A["පරිමා ඉතිහාසය"] --> B["Bid / ask depth"] --> C["ක්‍රියාත්මක වියදම"]
```

## ⚠️ පොදු වැරදි අර්ථකථනය

ඉහළ දැක්වෙන volume හෝ last price යනු මුළු order එකට ක්‍රියාත්මක කළ හැකි ද්‍රවශීලතාවක් බව සහතික නොකරයි.

## 🛠️ SCAP සඳහා භාවිතය

ලැබෙන තැන නිල order-book දත්ත භාවිත කර daily volume හා intraday executable depth වෙන් කරන්න.

## 📝 නැවත නිෂ්පාදනය කළ හැකි දත්ත වගුව

| මිනුම / සිදුවීම | කාලය / interval | මූලාශ්‍ර / adjustment | නිරීක්ෂණ අගය |
|---|---|---|---|
| ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ |

[පෙර පර්යේෂණය](../../../si/07-reading-checklist.md) · [මූලාශ්‍ර](../../../si/SOURCES.md) · [CSE](https://www.cse.lk/).

**ක්‍රම සටහන:** chart patterns, indicators සහ sentiment පුරෝකථන හැකියාව ස්වාධීනව පරීක්ෂා කළ යුතුය. අතීත ප්‍රතිලාභ හෝ backtests අනාගතය සහතික නොකරයි.
