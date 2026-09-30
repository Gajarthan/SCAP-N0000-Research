# 02 — தொழில்நுட்பப் பகுப்பாய்வு

[← முதன்மை ஆய்வு](../../ta/README.md) · [English](../../02-Technical-Analysis/README.md) · [தமிழ்](README.md) · [සිංහල](../../si/02-Technical-Analysis/README.md)

> **SCAP.N0000 · Softlogic Capital PLC**  
> **Reference date: 2026-09-30 · Research framework, not a completed investment assessment.**

**சந்தைத் தரவை மையமாகக் கொண்ட ஆய்வு:** SCAP-ன் வரலாற்று விலை, volume, வாங்க/விற்க வசதி, குறியீடுகள் மற்றும் sentiment ஆகியவற்றை மீண்டும் கணக்கிடக்கூடிய முறையில் ஆய்வு செய்தல். இங்கு தற்போதைய விலையோ trading signal-ஓ தரப்படவில்லை.

## 🧭 ஆய்வுமுறை

```mermaid
flowchart LR
  A["தேதியுள்ள OHLCV"] --> B["Charts / execution"] --> C["புதிய தரவில் சோதனை"]
```

## 📁 அனைத்து ஆய்வுப் பிரிவுகள்

| # | ஆய்வு பிரிவு | ஆய்வுக் கேள்வி |
|---|---|---|
| 01 | [விலை நடத்தை](01-Price-Action/README.md) | உண்மையில் நடந்த விலை வரம்புகள் என்ன? |
| 02 | [போக்கு மற்றும் உந்தம்](02-Trend-Momentum/README.md) | முந்தைய trend மற்றும் momentum எப்படி அளவிடலாம்? |
| 03 | [பரிவர்த்தனை அளவு / பணமாக்கல் வசதி](03-Volume-Liquidity/README.md) | பெரிய slippage இன்றி உண்மையான order முடிக்க முடியுமா? |
| 04 | [Chart வடிவங்கள் / குறியீடுகள்](04-Patterns-Indicators/README.md) | முடிவைப் பார்க்குமுன் chart விதியை வரையறுத்துச் சோதிக்கலாமா? |
| 05 | [அளவியல் / சந்தை மனநிலை](05-Quantitative-Sentiment/README.md) | Price, volume, செய்திகளில் noise-ஐத் தாண்டிய தகவல் உள்ளதா? |

## 📚 தொடர்புடைய ஆவணங்கள்

[முந்தைய trading checklist](../../ta/07-reading-checklist.md) · [தமிழ் காட்சி அறிக்கை](../../ta/reports/README.md) · [ஆதாரப் பட்டியல்](../../ta/SOURCES.md) · [அடிப்படைப் பகுப்பாய்வு](../01-Fundamental-Analysis/README.md) · [CSE](https://www.cse.lk/).

> ⚠️ **வகைப்பாட்டு குறிப்பு:** Technical indicator கடந்த சந்தை நடவடிக்கையை விளக்குகிறது; எதிர்காலப் பலனை உறுதி செய்யாது. Sentiment/quantitative பல ஆய்வு வகைகளுடன் தொடர்புடையது. சரிசெய்யப்பட்ட தேதியுள்ள தரவு, brokerage செலவு, liquidity, தரநிலை அவசியம்.
>
> SCAP-க்கான உண்மையான live OHLCV, தற்போதைய சந்தை விலை அல்லது உறுதி செய்த indicator இங்கு இல்லை. அசல் தரவு கிடைத்த பிறகே கணக்கிட வேண்டும்.

**பொதுக் களஞ்சிய எச்சரிக்கை:** உங்கள் தனிப்பட்ட தரகர் கணக்கெண், பங்கு வைத்திருப்பு மற்றும் வர்த்தக ரசீதுகளைப் பொது repo-வில் வெளியிட வேண்டாம்.
