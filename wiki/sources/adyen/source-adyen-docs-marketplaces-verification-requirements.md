---
title: "Adyen Marketplaces verification requirements"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/verification-requirements"
raw_files:
  - "adyen/docs/marketplaces/verification-requirements/2026-09-15.md"
tags: [adyen, marketplaces, platforms, verification, onboarding]
---

## Overview

This 2023-modified, 2026-09-15-captured **Marketplaces / Adyen for Platforms** guide helps determine user-verification information to collect and submit before starting verification. Requirements depend on the user’s operating country/region, legal-entity type and financial products. Its country, age, entity and product matrices are snapshot guidance, not current eligibility or a verification outcome. [[adyen-platforms]]

## Key takeaways

- The page says a base **Adyen for Platforms or Adyen Issuing integration** has no additional integration requirements, limitations or preparations under its `Requirements` heading (raw line 29). That sentence is **not a waiver of user verification**: raw lines 19–25 require information collection and submission, and the later financial-product section describes additional checks for some products (raw lines 309–384).
- Operating-country rules differ, and the page routes to separate country/legal-entity minimum-information detail. Its minors rule says under-13 users cannot be onboarded; onboarding minors is possible only with Legal Entity Management API **v3 or v4**, with region/age restrictions, a legal representative also onboarded as authorised signatory where permitted, specified representative data/consent, and possible ID escalation. See [[raw/adyen/docs/marketplaces/verification-requirements/2026-09-15|raw lines 31–63]].
- The user that contracts with the marketplace is the **main legal entity**; associated people or entities also require information and, for a private company’s owners, linked individual legal entities. The country-by-entity table covers Individual, Organization, Sole Proprietorship, Trust and Unincorporated Partnership, with conditional support. See [[raw/adyen/docs/marketplaces/verification-requirements/2026-09-15|raw lines 65–111]].
- Organization guidance includes registration/address/payout-bank details and associated UBOs, controllers and signatories, with ownership/control and country-specific director thresholds. Trusts are described as supported only in Australia and New Zealand in this snapshot, and unincorporated partnerships have a separate listed country set and partner-association roles. Use the exact entity and person rules at [[raw/adyen/docs/marketplaces/verification-requirements/2026-09-15|raw lines 113–308]]; incorporated partnerships are routed to Organization (raw lines 254–260).

## Product-specific boundaries

- Processing payments and payouts are described as included by default; additional products can require more verification and separate capabilities (raw lines 309–315). **Business accounts** are listed for BE, DE, ES, FR, GB, NL and US, with country conditions applying to both the user legal entity and associated individuals, and for organizations or sole proprietorships. This guide adds industry, possible website, source-of-funds, FATCA/CRS where applicable, tax-residence/ID, conditional source-of-wealth, and live-selfie/photo-ID inputs. See [[raw/adyen/docs/marketplaces/verification-requirements/2026-09-15|raw lines 317–334]].
- For **US business accounts**, the captured guide requires onboarding-flow disclosures and timing, Adyen Terms acceptance/copy and gambling certification; Adyen checks the flow. It excludes governmental organizations including SOEs. These are source-described onboarding conditions, not a current-law determination or proof an account was opened. See [[raw/adyen/docs/marketplaces/verification-requirements/2026-09-15|raw lines 338–348]].
- **Card issuing** is listed for EEA, UK and US organizations or sole proprietorships, with VAT/tax-ID and source-of-funds data beyond the country/entity minimum; capability levels and per-card/day threshold examples are at raw lines 364–373. **Capital** is listed as invite-only for supported countries and the same two entity classes; the page says its proactive risk assessment means no additional verification checks. Neither section establishes a granted capability, issued card or financing offer. See [[raw/adyen/docs/marketplaces/verification-requirements/2026-09-15|raw lines 350–384]].

## Detail locators

- Verification factors, base-integration wording, country and minor conditions: [[raw/adyen/docs/marketplaces/verification-requirements/2026-09-15|raw lines 15–63]].
- Main/associated legal entities, country matrix and organization/individual/sole-proprietor/trust/partnership detail: [[raw/adyen/docs/marketplaces/verification-requirements/2026-09-15|raw lines 65–308]].
- Financial-product capabilities, business-account/US flow, card-issuing and Capital conditions: [[raw/adyen/docs/marketplaces/verification-requirements/2026-09-15|raw lines 309–384]].

## Related

- [[adyen-platforms]] — modern Adyen for Platforms model and verification context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/verification-requirements/2026-09-15|Marketplaces verification requirements (captured 2026-09-15)]]
