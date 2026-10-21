# Retrieval checks — docs-payouts

Q1. What is the Payouts landing page for, and what distinguishes its two product routes?

A1. It is an outbound-to-outside-Adyen account service umbrella (raw lines 15–19). The Payments-combined route is offered to an Adyen merchant of record for a beneficiary not onboarded with Adyen, such as a supplier (raw line 21), while Adyen for Platforms pays processed-payment funds to a platform merchant or sub-merchant (raw line 22). Child routes are Payout Service and platform managed payouts (raw lines 24–30). This Payouts umbrella and Payout Service child are distinct from the legacy Online Payout API described in [[adyen-payouts]]; this hub does not establish that legacy API's rules for Payout Service. Route: [[index]] → [[adyen-index]] → [[adyen-payouts]] → [[source-adyen-docs-payouts]] → [[raw/adyen/docs/payouts/2026-09-15]].

Q2. Does the “global payouts in real time” heading establish timing or receipt, or carry legacy Online Payout API approval and staged-review rules into Payout Service?

A2. No. That phrase appears as a landing-page description (raw lines 15–17), while the body only defines the two combinations and links to separate child guides (raw lines 19–30). It provides no route-specific request, funding, status or receipt evidence, and states no legacy Online Payout API approval or staged-review rules for Payout Service; the two actors and money flows must be resolved in the respective child source (raw lines 21–30). Route: [[index]] → [[adyen-index]] → [[adyen-payouts]] → [[source-adyen-docs-payouts]] → [[raw/adyen/docs/payouts/2026-09-15]].
