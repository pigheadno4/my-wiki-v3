---
title: "Deprecation of classic libraries | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/classic-library-deprecation"
raw_files:
  - "adyen/docs/point-of-sale/classic-library-deprecation/2026-09-15.md"
tags: [adyen, point-of-sale, classic-libraries, terminal-api, payment-terminals, deprecation]
---

## Overview

This Adyen Docs deprecation notice concerns classic POS integrations in which an Adyen library is embedded in cash-register software. It presents Terminal API and newer PCI-approved terminal software as the replacement path, with OPI offered instead for Xstore POS integrations using the JNI library. The notice also addresses replacement of Verifone Verix (eVo) terminal fleets. Its timeline is a dated documentation snapshot, not proof of a merchant's present integration or terminal state. See [[adyen]], [[adyen-terminal-api]], and [[adyen-payment-terminals]].

## Key takeaways

- Adyen says classic-library users need to migrate to a different integration type. The announced library timeline bars new integrations from January 1, 2022 and onboarding new merchants on a library in 2022. It sets March 29, 2024 as the end of support and maintenance and directs merchants needing classic-library transaction processing past that date to their Adyen Account Manager. Read these as the page's announced dates; the snapshot does not verify current processing availability or account-specific exceptions.
- The Xstore POS system with the Java Native Interface (JNI) library has an explicit alternative: Adyen offers OPI instead of Terminal API. The page describes OPI as XML request/response messaging. Do not apply the general Terminal API replacement route to this exception without checking the merchant's POS setup.
- Adyen separately says Verifone Verix/eVo users need to replace their terminal fleet because PCI approvals expire and Verifone support/repair ends. The page names the Verifone Engage/VOS range as the alternative and lists model examples. Its model and PCI status descriptions are tied to this dated notice; check current hardware support before procurement or operation.
- For PCI 4 eVo e355 and VX690, the notice lists no new orders after March 31, 2021, repair end March 31, 2023, PCI expiry in April 2023, and end of support with transactions no longer allowed March 29, 2024. For PCI 3 eVo e315, MX925, VX675, VX680, VX820, and VX820 Duet, it lists no new orders after January 1, 2020, PCI expiry April 30, 2021, repair end March 31, 2023, and the same March 29, 2024 end of support/transactions. These terminal prohibitions are distinct from the classic-library line's Account Manager instruction.

## Detail locators

- `Deprecation of classic libraries`, pinned raw lines 19–25: classic-library identity, Terminal API/new terminal software path, PCI approval condition, and fleet update warning.
- `Why you should switch to Terminal API`, lines 27–49: Adyen's comparison, example features, and the Xstore JNI/OPI exception.
- `Why you may need new payment terminals`, lines 51–69: eVo PCI/Verifone rationale and example eVo-to-VOS model table.
- `Time line for the deprecation`, lines 71–91: separate dates for libraries, PCI 4 eVo, and PCI 3 eVo.

## Related

- [[adyen-terminal-api]] — successor POS messaging route for the general classic-library case.
- [[adyen-payment-terminals]] — physical-terminal models and dated replacement context.
- [[adyen-terminal-management]] — fleet administration; this notice does not establish an ordering or rollout procedure.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/classic-library-deprecation/2026-09-15|Adyen classic-library deprecation notice, fetched 2026-09-15]]
