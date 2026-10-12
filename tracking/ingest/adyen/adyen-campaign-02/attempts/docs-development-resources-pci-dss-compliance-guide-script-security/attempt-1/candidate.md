---
title: "Adyen Docs: Script security for ecommerce"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/pci-dss-compliance-guide/script-security"
raw_files:
  - "adyen/docs/development-resources/pci-dss-compliance-guide/script-security/2026-09-15.md"
tags: [adyen, pci-dss, script-security, csp, sri, ecommerce]
---

## Overview

This Adyen website guide summarizes its PCI DSS v4.0.1 interpretation of payment-page script requirements 6.4.3 and 11.6.1 for **Web online payments** and recommends Content Security Policy (CSP), script inventory and authorization, Subresource Integrity (SRI), and violation reporting. It belongs under [[adyen-pci-dss-compliance]]. It is Adyen's captured guidance, not proof that a merchant page passes PCI assessment or that the example policy is suitable for a particular checkout.

## Key takeaways

- **Applicability is limited.** The page addresses merchants completing SAQ D or an onsite-assessment AoC, Adyen for Platforms partners, and partners implementing Adyen plugins. It says this page does **not** apply if the merchant is eligible for SAQ A; eligibility must be established from the relevant assessment route, not inferred from use of Adyen.
- Adyen describes requirement 6.4.3 as script authorization, integrity assurance, and an inventory with written justification. Its stated 3DS exemption applies to the **3D Secure script-validation process**; it does not remove the page's other script or tamper-detection responsibilities.
- Adyen describes requirement 11.6.1 as detection and alerting for unauthorized changes to security-impacting HTTP headers and payment-page script contents as received by the browser, with prompt investigation and resolution. Its CSP reporting recommendation includes collecting alerts through a configured reporting endpoint.
- A `Content-Security-Policy-Report-Only` header logs violations without blocking loads. Adyen then recommends a blocking CSP and SRI for Adyen-hosted JavaScript/CSS, plus a periodic script-inventory authorization sign-off. The displayed blocking example uses broad `frame-src: *` and other wildcards; the inventory separately lists Mastercard and Visa domains absent from its displayed `script-src` list. Adapt and verify the policy for the actual page and payment methods.
- **Example mismatch:** the SRI section calls its example v5.59.1 while both sample resource URLs contain `/sdk/5.59.0/` (raw lines 177–189). Use hashes for the exact deployed resources and version; this snapshot does not validate that example or a live CSP configuration.

## Detail locators

- **Requirements, raw lines 25–35** — SAQ D, onsite AoC, platform/plugin partner contexts and SAQ A exclusion.
- **PCI DSS requirement 6.4.3 / 3DS exemption, raw lines 37–49** — authorization, integrity and inventory controls; narrow 3DS script-validation scope.
- **PCI DSS requirement 11.6.1, raw lines 51–57** — browser-received header/script change detection and prompt handling.
- **Implement a Content Security Policy, raw lines 59–146** — Adyen's CSP/SRI recommendation, report-only versus blocking behavior, displayed domain policy, broad iframe allowance, and rationale.
- **Create an inventory / Check integrity, raw lines 148–190** — script source table, periodic authorization, SRI attributes, per-version hashes, and the v5.59.1 versus URL v5.59.0 discrepancy.
- **Implement detection mechanisms, raw lines 192–218** — CSP-alert collection, Reporting API endpoint, `Reporting-Endpoints`, and `report-to` route.

## Related

- [[adyen]]
- [[adyen-pci-dss-compliance]]
- [[adyen-online-payments]]
- [[adyen-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/development-resources/pci-dss-compliance-guide/script-security/2026-09-15|Adyen Docs — Script security for ecommerce (2026-09-15)]]
