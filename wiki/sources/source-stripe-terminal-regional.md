---
title: "Stripe Terminal: Regional Considerations (All Countries)"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-regional-2025.md"
tags: [stripe, terminal, in-person, regional, interac, eftpos, cartes-bancaires, girocard, sca, japan, germany, canada, australia, france]
---

## Stripe Terminal: Regional Considerations (All Countries)

Country-specific requirements for Terminal integration across 29 countries.

## Key Takeaways

### Universal rule

Stripe account AND Location must be in the same country; local currency only.

### Country-specific reader availability notes

- **DE (Germany)**: WisePOS E + S700 only — **no S710**
- **JP (Japan)**: S700 only — no WisePOS E, no S710, no Tap to Pay Android (iPhone only)
- **MY**: Tap to Pay on iPhone = public preview (not GA)
- **GI**: Tap to Pay on Android only (no smart or mobile readers)

### Canada (CA) — Interac

- Include `interac_present` in `payment_method_types`
- **Interac = automatic capture only** — no manual hold/capture
- Use `manual_preferred` to support both Interac (auto) and other cards (manual)
- `manual` capture → Interac always declined
- **In-person refund mandatory** for Interac — cannot refund via API or Dashboard; reader must re-read original card
- Interac Flash: 250 CAD max contactless; PIN required after 100 CAD or 4th consecutive contactless
- French language compliance required (Quebec); reader auto-translates based on card preference after card read
- As of API `2025-03-31.basil`: `capture_method` must be `automatic`, `automatic_async`, or `manual_preferred`

### Australia (AU) — eftpos

- eftpos = least-cost routing (auto-routes to eftpos, Visa, or MC)
- **Capture**: automatic, `manual_preferred`, or `automatic_delayed` only — no manual hold
- **Minimum SDK versions**: iOS 2.20.0, Android 2.20.0, React Native 0.0.1-beta.12
- Cash out transactions not supported on Terminal

### France (FR) — Cartes Bancaires

- Include `cartes_bancaires` in `payment_method_types` for co-branded CB cards

### Germany (DE) — girocard

- girocard: WisePad 3 + S700 only; reader prompts for account selection on co-branded cards

### EEA countries (GB, IE, FR, DE, etc.) — SCA

- Chip + PIN satisfies SCA (chip = possession, PIN = knowledge)
- Contactless may trigger SCA: reader prompts card insertion + PIN
- **Two-charge pattern**: first charge = soft decline (`offline_pin_required` or `online_or_offline_pin_required`) + contactless read; second = authorized/declined with contact EMV
- Tap to Pay: same two-charge pattern; if PIN not supported contactless → hard decline before PIN screen

### SCA thresholds (EEA)

- Low-value exemption: under 50 EUR (or local equivalent) — may be exempt
- Exemption limit: 5 consecutive uses OR cumulative sum > 150 EUR → authentication required

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-regional-2025]] — verbatim regional considerations guide (2615 lines; 29 countries)
