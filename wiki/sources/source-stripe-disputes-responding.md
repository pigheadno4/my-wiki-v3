---
title: "Stripe — Respond to Disputes"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/disputes/responding
raw_files:
  - "stripe-disputes-responding-2026-11-07.md"
  - "stripe-disputes-responding-2026.md"
tags: [stripe, disputes, chargebacks, evidence, visa-ce-30, liability-shift, inquiries, dispute-response]
---

## Summary

Stripe's November 7, 2026 responding guide covers the Dashboard response window, inquiries, Visa and Mastercard compliance disputes, eligible Visa CE 3.0 and possible 3D Secure liability shift, final evidence submission, fees, and issuer-decided outcomes. The Mastercard compliance section is new relative to the May capture; the other response mechanics remain substantially the same. This page does not verify account-specific fees, network policy outside the capture, or the Mastercard API procedure linked from it.

## Notification and Deadline

Stripe lists email, Dashboard, `charge.dispute.created` **when the integration receives events**, and push notification **when subscribed** as notification channels. The Disputes tab and details page show the category and case. An API route is linked for programmatic management. The usual response window is **7–21 days**, depending on card network; missing the actual deadline means automatic loss and no retrieval of the disputed funds. Review the dispute's own deadline.

Dashboard automation options listed are Stripe Workflows for custom no-code logic and Stripe Apps for fraud or chargeback management. Their listing does not mean either is configured on an account.

## Review the Category and Complaint

Review the Dashboard category or the Dispute object's `reason`, then gather evidence responsive to that category. If the bank supplied claim documents and the dispute remains open, the details page may allow **Review the claim details**. The page may also offer an email route to the account owner. Keep communication records if contacting them.

An **inquiry** can appear as a disputed payment in the Dashboard but is a pre-dispute stage. Respond to try to prevent a formal escalation. **Accepting an inquiry does not resolve it**; submit evidence to counter it. If it escalates to a chargeback, submit a **separate response** for that dispute.

## Compliance Disputes

| Network | November 2026 captured guidance |
| --- | --- |
| Visa | A contested Visa compliance dispute incurs a **500 USD or local-equivalent network fee**, in addition to applicable Stripe dispute fee or fees. Stripe returns that network fee if the business wins. Issuer-filed cases are called pre-compliance. The page links a separate Visa compliance API procedure. |
| Mastercard | A contested Mastercard compliance dispute incurs a **500 USD or local-equivalent network fee**, in addition to applicable Stripe dispute fee or fees. Stripe returns that network fee if the business wins. Issuer-filed cases are called pre-compliance; a filing can escalate to a full compliance case. The page links a separate Mastercard compliance API procedure, whose parameters are not established by this capture. |

The Mastercard section appears in the November capture, not the May capture. These network fees are distinct from Stripe's dispute received and dispute countered fees. Neither route guarantees a particular case will be won or a fee returned.

## Fraudulent Disputes: CE 3.0 and Liability Shift

For a **Visa 10.4 card-absent fraud** dispute, Stripe evaluates transaction history for Visa CE 3.0 eligibility. **If eligible**, it notifies the business in the Dashboard and dispute email and encourages evidence submission because eligibility **typically improves** win likelihood. It is not an automatic win.

For a fraudulent dispute that **might** be covered by 3D Secure liability shift, Stripe provides most available evidence, such as ECI. The existence of 3DS data alone does not establish that liability has shifted in a particular case; consider adding relevant evidence.

For an eligible Visa CE 3.0 response, look for **Required for CE 3.0** badges. In **most cases**, Stripe pre-populates required fields from transaction history. Do not edit fields already populated, since this might affect eligibility; fill empty required fields with the requested information. For a dispute that might have liability shift, Stripe populates 3DS/ECI information.

## Accept or Counter

**Accept dispute** tells the issuing bank that the business is not contesting the refunded amount. It is distinct from accepting an inquiry, which does not close the inquiry. **Counter dispute** opens the Dashboard evidence response form. The business can also use the separately linked API for programmatic handling. A cardholder may be asked to withdraw a dispute after an amicable resolution, but a withdrawal request is not itself a bank decision or a substitute for responding to a formal dispute.

If a business counters, a **dispute countered fee** applies **in addition to** the dispute received fee, except that the countered fee does not apply to businesses in **Mexico and Japan**. Stripe returns the countered fee if the business wins. The **dispute received fee** is generally not returned unless the Stripe contract says otherwise. These are separate from the conditional 500 USD or local-equivalent compliance network fees above. The issuing bank decides the outcome; review can take up to three months, and Stripe emails the decision when received.

## Submit Evidence in the Dashboard

There is **one final submission opportunity**. Stripe says it forwards the response and supporting files to the issuing bank immediately; after submission, the business cannot edit or add evidence. Prepare before submitting:

1. Open **Counter dispute** and explain why the claim is wrong and what product type was purchased. The response category and type help Stripe recommend evidence; product type may be captured automatically when the integration supports it.
2. Add evidence relevant to the category and argument. The form's sections vary by case; available background shipping, refund-policy, customer, and product data can pre-populate when the integration supports it. Fill missing relevant fields.
3. Assign each uploaded file an evidence type. Only **one file per type** can be submitted, so combine same-type items. Keep the combined files within **4.5 MB**. This responding capture says Mastercard evidence files have a combined **19-page maximum**; consult the actual case's applicable limit because the separate November best-practices capture describes dispute-specific page-limit checks.
4. Do not rely on external audio/video, requests to call or email for more information, or links to downloads/tracking; banks will not review that external content.
5. Acknowledge that the response is final and submit. Stripe formats the evidence for issuer consideration. If one payment has multiple disputes, consider each separately.

Submitting evidence is not the same as winning or receiving funds. See [[source-stripe-disputes-best-practices]] for the separate API compiled-PDF page-limit error on evidence updates.

## Outcome and Status

After submission, Stripe describes the dispute as **under review**. This prose alone does not establish an exact API enum such as `under_review`. When the issuer decides, Stripe says it emails the outcome, emits `charge.dispute.closed`, and updates the Dashboard and Dispute object:

| Outcome | Meaning |
| --- | --- |
| `won` | Issuer overturned the dispute; the debited chargeback amount is returned through Stripe. The countered fee is returned where it applied. The received fee is generally retained unless the contract states otherwise; the page also says a dispute fee might be returned for Mexico businesses. |
| `lost` | Issuer upheld the dispute; the refund is permanent, and the dispute fee is not returned. |

The bank may provide additional decision documents under **View issuing bank response**. Neither a submitted packet nor the under-review stage proves bank acceptance, finality, or a win.

## Related Pages

- [[disputes]] — dispute concept and response context
- [[stripe]] — provider overview
- [[source-stripe-disputes-how-disputes-work]] — lifecycle and inquiry context
- [[source-stripe-disputes-best-practices]] — evidence formatting and page-limit guidance
- [[stripe-3d-secure]] — authentication and possible liability shift

## Raw Sources

- [[raw/stripe-disputes-responding-2026-11-07|Stripe respond to disputes, 2026-11-07 capture]] — includes Mastercard compliance section
- [[raw/stripe-disputes-responding-2026|Stripe respond to disputes, 2026-05-09 capture]] — earlier Visa and response guidance
