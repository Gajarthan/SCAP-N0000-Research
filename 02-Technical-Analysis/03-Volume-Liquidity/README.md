# 03 · Volume and Liquidity Analysis

[← Technical analysis](../README.md) · [English](README.md) · [தமிழ்](../../ta/02-Technical-Analysis/03-Volume-Liquidity/README.md) · [සිංහල](../../si/02-Technical-Analysis/03-Volume-Liquidity/README.md)

> **SCAP.N0000 — Softlogic Capital PLC.** **Status: methodology, not a current chart-based trading signal.** Verify data and CSE trading calendars first. **Reference: 2026-09-30.**

## 🎯 Research question

Can SCAP shares be bought and sold in the required size without unreasonable slippage or delay?

## 🔍 Data and methods to verify

- [ ] Record traded shares, daily turnover, number of trades and the frequency of no-trade days over comparable windows.
- [ ] Measure quoted bid-ask spread, depth and possible execution cost at the intended notional order size.
- [ ] Compare unusual volume with dated corporate news and investigate free-float or block-trade effects.

## 🧭 Method flow

```mermaid
flowchart LR
  A["Volume history"] --> B["Bid/ask depth"] --> C["Execution cost"]
```

## ⚠️ Common interpretation error

High displayed volume or a last-traded price does not guarantee enough executable depth for the investor's entire order.

## 🛠️ SCAP application

Use official market-depth data where available; label daily volume measures that cannot estimate intraday executable liquidity.

## 📝 Reproducible observation register

| Metric / event | Period / interval | Source / adjustment | Observed value |
|---|---|---|---|
| ______ | ______ | ______ | ______ |
| ______ | ______ | ______ | ______ |

[Existing research](../../07-reading-checklist.md) · [Source register](../../SOURCES.md) · [CSE](https://www.cse.lk/).

**Method note:** Chart patterns, indicators and sentiment are descriptive unless predictive usefulness is independently demonstrated. Do not treat backtests or past returns as guarantees.
