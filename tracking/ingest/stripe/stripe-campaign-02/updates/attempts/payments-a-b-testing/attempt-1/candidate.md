---
title: "Stripe Docs — A/B testing a payment method"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/a-b-testing"
raw_files:
  - "stripe-payments-a-b-testing-2026-11-07.md"
  - "stripe-a-b-testing-payment-methods-2025.md"
tags: [stripe, a-b-testing, dynamic-payment-methods, payment-element, checkout, conversion, experimentation]
---

## Summary

Stripe's captured guide describes a no-code Dashboard experiment that offers selected payment methods to treatment traffic and compares outcomes with control traffic. It requires dynamic payment methods and either Payment Element Web with the Payment Intents API or Checkout in payment mode (new raw lines 17–19, 115–125). Starting, stopping, and managing experiments is Dashboard-only; the page does not report an actual merchant experiment or outcome.

## Setup and experiment boundaries

1. In Dashboard Payment method settings, choose a payment-method configuration, create an experiment, select treatment methods, optionally add payment-method eligibility rules, name the experiment, and choose the traffic allocation. Only one experiment can run per configuration (new raw lines 21–32).
2. Stripe recommends a 50% treatment allocation as a balance between speed and risk, but permits a smaller or larger choice. The **80,000-session figure is an illustration for an even 50/50 split, a 100-basis-point conversion-rate difference, and 5% significance**, not a general minimum or enforced default (new raw line 30). Stripe's methodology separately says required sessions are calculated dynamically from the selected split for 80% power to detect a 1% difference at 5% significance (new raw line 111). Actual needed sessions vary.
3. The guide says Stripe randomizes sessions with UserAgent, IP address, and date and aggregates each unique user's sessions daily to reduce double counting. After starting, traffic allocation can change but control or treatment payment-method settings cannot be toggled without ending the experiment (new raw lines 31–33). The BNPL messaging element is a recommendation for BNPL experiments (new raw line 34).
4. While active, the merchant can adjust treatment traffic to 1–99%, view the report, pause/resume, or end and adopt treatment/revert to control. Pausing shows only control methods and stops report capture. After 180 days Stripe says it ends the experiment and enables control settings (new raw lines 36–44).

## Results and interpretation

The guide treats an experiment as complete when average revenue per session is statistically significant and enough sessions have accrued; the needed session count depends on the treatment/control split (new raw lines 51–55). Average revenue per session includes converting and non-converting sessions. The report also shows projected revenue at 100% treatment traffic, gross revenue, conversion rate, and average order value. Conversion rate uses **eligible sessions**: at least one treatment method eligible and the payment UI rendered (new raw lines 56–66). Projected revenue is a model, not observed lift.

The guide describes a z-test at 5% significance and a dynamic 80%-power sample calculation (new raw line 111). Green denotes a statistically significant increase; yellow a statistically significant decrease; gray means too few sessions to determine significance reliably. The page says green/yellow differences display once at least 80% of estimated required sessions is reached, but reaching that threshold alone does not guarantee significance or a colored badge (new raw lines 68–76). Statistical indicators are not independently verified causal business outcomes.

Downloadable raw-data dimensions include `experiment_session_id`, treatment assignment, conversion, method used, eligible-session flag, rendered/visible methods, and connected-account ID. Group by `experiment_session_id` to avoid refresh double counting (new raw lines 84–107). The page notes that IP and User Agent analytics may require disclosures or consent under applicable law and advises legal review (new raw line 113).

## Captured payment-method table and Connect scope

Each capture lists **34 payment-method rows** in its Payment Element and Connect Payment Element A/B-test table (old raw lines 133–166; new raw lines 130–163). The 2026-05-08 table names a **Crypto** row linking to `/crypto`; the 2026-11-07 table instead names **Stablecoins** linking to `/stablecoins`. Both rows show support in the two table columns (old raw line 146; new raw line 143). This is a dated table-label/link change, not proof of general stablecoin availability, any merchant's eligibility, or a production test result.

Nine rows show Connect Payment Element A/B testing unsupported in both captures: ACH Direct Debit, ACSS Debit, Alipay, BECS Direct Debit, Bacs Direct Debit, FPX, Konbini, SEPA Debit, and WeChat Pay (new raw lines 130–163). The footnote explains that some methods require off-Stripe actions that platforms cannot complete on behalf of connected accounts (new raw line 165). The table is experiment support guidance for this integration scope, not universal payment-method support.

Connect experiments belong to platforms, not individual connected accounts. Selected control/treatment methods apply to eligible connected accounts; the platform can opt out account IDs. A connected account's own payment-method preference applies in both groups and can hide a method the platform selected (new raw lines 167–171).

## Historical local assets

The 2026-05-08 raw capture refers to local images `raw/assets/stripe-ab-test-create-experiment.png`, `raw/assets/stripe-ab-test-manage-experiment.png`, `raw/assets/stripe-ab-test-experiment-report.png`, `raw/assets/stripe-ab-test-gray-indicator.png`, and `raw/assets/stripe-ab-test-green-indicator.png`. The November capture uses remote image URLs. These are presentation references, not evidence of tested functionality.

## Related pages

- [[stripe-ab-testing-payment-methods]] — concept page
- [[stripe-dynamic-payment-methods]] — prerequisite dynamic payment methods
- [[stripe]] — provider

## Raw Sources

- [[raw/stripe-payments-a-b-testing-2026-11-07|2026-11-07 A/B testing guide]]
- [[raw/stripe-a-b-testing-payment-methods-2025|2026-05-08 earlier guide]]
