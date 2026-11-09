---
title: "Stripe — Best Practices for Preventing Fraud"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/prevention/best-practices"
raw_files:
  - "stripe-disputes-prevention-best-practices-2026-11-07.md"
  - "stripe-disputes-prevention-best-practices-2026.md"
tags: [stripe, fraud, disputes, best-practices, radar, auth-capture, 3ds, statement-descriptor, shipping]
---

## Summary

The May 10 and November 7, 2026 same-URL captures organize dispute and fraud prevention practices into tools for everyone, tools for users of Radar, and developer tools. The November heading says **Radar** rather than May's **Radar for Fraud Teams**, and explicitly conditions manual review and review-process capture on plan support. These are recommendations and captured feature descriptions, not proof that a particular account has the feature or that a payment will avoid fraud or disputes. See [[disputes]]. [May capture](../../raw/stripe-disputes-prevention-best-practices-2026.md#L10-L12); [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L11-L13); [November Radar sections](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L85-L93)

## Tools for everyone

- **Customer clarity and policy evidence:** keep service contact and order updates accessible; explain refund/cancellation policies. Stripe says businesses *can* require agreement to terms. It recommends displaying the full policy at checkout or in a popup rather than only a link. For a link-only checkbox, an issuer *might* reject it as evidence; the guide calls for reasonable evidence that the full policy was presented before purchase. This is advice about issuer evidence, not a universal checkout mandate or guaranteed dispute outcome. [May capture](../../raw/stripe-disputes-prevention-best-practices-2026.md#L16-L24); [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L17-L25)
- **Shipping and descriptors:** for physical goods, use tracked delivery when possible and provide screenshots rather than tracking links as dispute evidence. Use a recognizable statement descriptor (captured constraints: 5–22 characters, at least five letters, and no `<`, `>`, `'`, or `"`) and separate Stripe accounts for distinct businesses. [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L27-L36)
- **Refund and shipping judgment:** the guide advises refunding when certain a payment is fraud unless covered by a form of liability shift; an aggressive refund approach for suspected fraud depends on fulfillment, dispute activity, monitoring status and low volume. Fully and partially refunded payments have different dispute implications. For physical goods, consider a 24–48-hour shipping delay and closer review of expedited orders. These are conditional choices, not guarantees that a dispute is avoided. [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L38-L65)
- **Address checks:** shipping to an AVS-verified billing address is described as safest, but the guide permits a different destination with risk mitigation and order/address review. A differing or unverified address is a risk signal, not proof the recipient is fraudulent. Review account dispute-rate trends when assessing prevention methods. [May capture](../../raw/stripe-disputes-prevention-best-practices-2026.md#L66-L82); [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L67-L83)

## Tools for users of Radar

If the account's **plan supports manual review**, certain payments can be placed in the review queue. Ordinarily these payments are already processed and the card charged; a separate authorization and capture flow changes that payment state. The guide suggests reviewing queued and elevated-risk payments promptly and using rules to allow, block or review payments based on chosen criteria such as country or card type. The May capture called this tier **Radar for Fraud Teams**; the November capture calls it **Radar** and makes review plan-conditional. The capture does not establish which plans support it or a particular account's entitlement. [May capture](../../raw/stripe-disputes-prevention-best-practices-2026.md#L84-L115); [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L85-L116)

## Tools for developers

- **Visa CE 3.0 evidence:** Stripe recommends processing transactions on its platform and including customer IP, email, shipping address and product descriptions, because it cannot determine eligibility or submit evidence for externally processed transactions. For a Visa fraud dispute, it *can* identify qualifying historical transactions on Stripe and pre-populate much of the required response evidence. Processing on Stripe alone does not establish CE 3.0 eligibility, liability shift, or a win. [May capture](../../raw/stripe-disputes-prevention-best-practices-2026.md#L121-L128); [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L122-L129)
- **Payment information and verification:** collect relevant name, email, CVC, billing/shipping and tracking data where applicable. A failed verification *might* indicate fraud; the guide says to *consider* rejecting the payment. Identity verification can help some businesses but adds friction for legitimate customers. [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L131-L152)
- **3D Secure:** authenticated card payments *might* be protected from most fraudulent disputes through liability shift. Early Fraud Warnings can still arrive and count toward card-brand monitoring. Authentication is not a universal liability shift or dispute-free guarantee. [May capture](../../raw/stripe-disputes-prevention-best-practices-2026.md#L143-L145); [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L144-L146)
- **Authorization and capture:** the guide describes card authorization as a hold without movement of money, with capture later completing the charge; an uncaptured authorization cannot be disputed, while a fully captured payment can. The page gives a general up-to-seven-day capture example, not a method-specific authorization window. Manual capture *in the Radar review process* is available only if the account plan supports it. A normal Radar review does not itself leave the payment uncaptured. [May capture](../../raw/stripe-disputes-prevention-best-practices-2026.md#L153-L159); [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L154-L160)
- **Additional tools:** a dynamic descriptor can carry a customer verification code, though it adds friction and is not foolproof. Fraud-rate health alerts list `spike` and `sustained_attack`, with an explicit accuracy and reliance caveat. [November capture](../../raw/stripe-disputes-prevention-best-practices-2026-11-07.md#L162-L181)

## Related Pages

- [[disputes]] — concept with reciprocal prevention-practices route
- [[source-stripe-disputes-verification]] — CVC and AVS guidance
- [[source-stripe-radar-reviews]] — Radar review-queue detail
- [[stripe-3d-secure]] — card authentication context

## Raw Sources

- [[raw/stripe-disputes-prevention-best-practices-2026-11-07|November 7, 2026 best-practices capture]] — verbatim webpage text (187 lines)
- [[raw/stripe-disputes-prevention-best-practices-2026|May 10, 2026 best-practices capture]] — historical webpage text (180 lines)
