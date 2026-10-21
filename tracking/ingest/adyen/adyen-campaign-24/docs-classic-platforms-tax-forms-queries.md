# C24 Classic tax-form retrieval checks

## Q1 — What does the Classic guide say about scope and retrieving a 1099-K?

It describes US-based merchants or sub-merchants with direct Adyen payouts and a processed-volume threshold, and notes state requirements (raw lines 23–28). Its **2024** federal figure is USD 5,000 gross processed volume per calendar year before fees, refunds or chargebacks; state thresholds vary (raw lines 30–33). For an eligible sub-merchant, the platform provides a UI link, sends a server-side `/getTaxForm` request with holder code, form type and year, then decodes Base64 content for a PDF (raw lines 35–57, 74–83). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-tax-forms]] → [[raw/adyen/docs/classic-platforms/tax-forms/2026-09-15]].

## Q2 — What cannot be concluded from the threshold or API example?

The USD 5,000 figure belongs to **2024**, not a current tax-law conclusion, and state rules may differ (raw lines 30–33). The page says a below-threshold holder receives an error rather than a generated form; its TEST v6 request with year 2019 is illustrative (raw lines 59–72). A Base64 response or decoded PDF does not prove a form was filed with the IRS or delivered to the sub-merchant; those outcomes are outside this API example (raw lines 74–83). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-tax-forms]] → [[raw/adyen/docs/classic-platforms/tax-forms/2026-09-15]].
