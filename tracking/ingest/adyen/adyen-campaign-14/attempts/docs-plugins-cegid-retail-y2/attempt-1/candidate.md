---
title: "Cegid Retail Y2 | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/cegid-retail-y2"
raw_files:
  - "adyen/docs/plugins/cegid-retail-y2/2026-09-15.md"
tags: [adyen, cegid-retail-y2, point-of-sale, terminal-api, retail]
---

## Overview

This 2026-09-15 [[adyen]] Docs landing page introduces the Cegid Retail Y2 CPOS plugin for in-person payments through Adyen terminals and Terminal API. It states Cegid Retail Y2 v11.05+ support, local communications as the recommendation and cloud as a possible route requiring Support contact before building. It is a feature and setup route, not evidence of merchant enablement or a completed payment. [[adyen-cegid-retail-y2]]

## Key takeaways

- Cegid Retail Y2 is the POS system; the CPOS plugin and Adyen terminals integrate through Terminal API. After the CPOS plugin is set up, the guide routes to optional Tap to Pay and Pay by Link with Cegid Retail Mobile POS on iOS or Retail Live Store on Android. Those mobile products and links have their own guides and prerequisites.
- The feature list includes gift cards, dynamic currency conversion, QR wallets, partial authorizations, manual key entry, tax-free shopping, delayed capture, card-only Giving donations, MOTO, installments limited here to Brazil/Japan/Mexico, Pay by Link and iPhone/Android Tap to Pay. Listing a feature does not prove that it is enabled for an account, terminal, country, shopper or installed plugin release. Authorization, delayed capture and eventual settlement remain separate states.
- The page says the plugin works with Retail Y2 v11.05 and later, and describes local POS-to-terminal communications as recommended. Cloud POS-to-terminal communications are also possible over the internet, but the guide says to contact Support before building that route. The broad linked statements about supported terminal methods and terminal models need the exact method, device, software, country and account rules from their own guides before use.
- Start with Adyen onboarding and a test account while live credentials are pending. The page routes to Customer Area and Cegid back-office plugin setup, gift cards, optional mobile Tap to Pay or Pay by Link, and test/go-live. These links are next steps, not evidence of an installed plugin, live credential, configured terminal or successful transaction.

## Detail locators

- **Product, Terminal API route and optional mobile extensions:** raw lines 15–22.
- **Feature list and region/method qualifications:** raw lines 24–38.
- **Retail Y2 version, local/cloud transport and broad method/terminal navigation:** raw lines 40–57.
- **Test/live setup and linked child routes:** raw lines 69–89.

## Related

- [[adyen]]
- [[adyen-cegid-retail-y2]]
- [[adyen-terminal-api]] — underlying Terminal API architecture, separate from this CPOS integration

## Raw Sources

- [[raw/adyen/docs/plugins/cegid-retail-y2/2026-09-15|Adyen Cegid Retail Y2 overview — collected 2026-09-15]]
