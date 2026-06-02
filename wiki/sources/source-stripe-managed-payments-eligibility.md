---
title: "Managed Payments Eligibility"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-managed-payments-eligibility-2025.md"
tags: [stripe, managed-payments, merchant-of-record, tax-codes, eligibility, digital-goods, buyer-countries]
---

## Summary

Detailed eligibility requirements for Stripe Managed Payments: which business locations, product types, tax codes, buyer countries, and performance standards are required. Primary reference for the tax code list.

## Account Eligibility

- **Business types**: Direct integrations only — no Connect platforms, Express accounts, or platform-controlled accounts
- **Supported business locations**: ~38 countries across North America, Europe, and Asia Pacific

### Supported Business Locations

**North America**: CA, US

**Europe** (32 countries): AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK

**Asia Pacific**: AU, HK, JP, SG

## Product Eligibility

### Supported Categories

- Software (IaaS, PaaS, SaaS, downloadable)
- Video games
- Digital media (audiobooks, ebooks, magazines, newspapers, audio/video works, images)
- Online courses and training (self-study, on-demand)
- Electronically supplied business/web services (website hosting, information services)

### Unsupported Categories

- Physical goods
- Professional services (consulting, marketing, design, development, tech support)
- Live in-person events

### Critical Rule: Fully Automated Only

Product must be **fully automated** — no human intervention:
> "If your service involves human intervention (such as live 1-1 coaching), it doesn't qualify."

If Stripe determines ineligibility after the fact → you're responsible for indirect tax liability and must stop using Managed Payments for that product.

### Eligible Tax Codes (Summary by Category)

Must assign one of 60+ eligible `txcd_` codes. Key codes by category:

| Category | Tax codes |
| --- | --- |
| General digital services | `txcd_10000000` |
| IaaS (personal/business) | `txcd_10010001`, `txcd_10101000` |
| PaaS (personal/business) | `txcd_10102001`, `txcd_10102000` |
| SaaS (personal/business, download variants) | `txcd_10103000`–`txcd_10103101` |
| Video games (download/stream, perm/limited/subscription) | `txcd_10201000`–`txcd_10201004` |
| Downloadable software | `txcd_10202000`, `txcd_10202001`, `txcd_10202003` |
| Audiobook | `txcd_10301000` |
| Digital books | `txcd_10302000`–`txcd_10302003` |
| Digital magazines/periodicals | `txcd_10303000`–`txcd_10303104` |
| Digital newspapers | `txcd_10304000`–`txcd_10304102` |
| Digital school textbooks | `txcd_10305000`, `txcd_10305001` |
| Digital audio works | `txcd_10401000`–`txcd_10401200` |
| Digital audio-visual works | `txcd_10402000`–`txcd_10402200` |
| Digital photos/images | `txcd_10501000` |
| Digital news/documents | `txcd_10503000`–`txcd_10503005` |
| Software documentation/manuals | `txcd_10504003` |
| Digital finished artwork | `txcd_10505000`–`txcd_10505002` |
| Digital greeting cards | `txcd_10506000`–`txcd_10506002` |
| Website advertising/hosting/info services | `txcd_10701000`–`txcd_10701411` |
| Digital AV/audio bundles | `txcd_10804001`–`txcd_10804010` |
| Online courses (self-study, on-demand) | `txcd_20060058`–`txcd_20060358` |
| Software maintenance agreements | `txcd_37071001` |

**US note**: business/personal use distinction on tax codes only relevant if you have US sales.

## Buyer Eligibility

- **195+ countries and territories** supported
- **9 restricted countries**: Ascension Island, China, Cuba, Iran, Kosovo, North Korea, Russia, Syria, Tristan da Cunha

## Ongoing Performance Requirements

- **Dispute rate**: must maintain low historical dispute rate, no prior risk issues
- **Refunds**: Stripe can issue refunds within **60 days** of purchase in certain cases to reduce chargebacks
- **Consumer protection**: Stripe applies regional cooling off periods and other applicable consumer protection requirements

## Related Pages

- [[stripe-managed-payments]] — concept page
- [[source-stripe-managed-payments-overview]] — overview (integration paths, feature comparison)

## Raw Sources

- [[stripe-managed-payments-eligibility-2025]] — verbatim eligibility page (212 lines, complete with buyer eligibility and ongoing requirements)
