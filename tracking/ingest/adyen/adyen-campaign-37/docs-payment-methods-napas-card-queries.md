# docs-payment-methods-napas-card — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a Vietnam Napas-network card **overview**, describing Adyen's offering via partner MoMo, a shopper bank/gateway/OTP redirect sequence and channel navigation (source-adyen-docs-payment-methods-napas-card; raw lines 15–29, 35–65). It is not an instruction for the merchant to handle Napas ATM card number/PIN or OTP, does not state the integration endpoint/version or establish current merchant eligibility, and shopper return does not prove payment authorization (raw lines 23–29, 35–65).

Q2. What are its central capability, prerequisites and warnings?

The shopper selects Napas, chooses a local bank, enters ATM card number/PIN on the **Napas Payment Gateway**, authenticates with an email/SMS OTP, then returns to the site/app (raw lines 23–29). The historical matrix says Redirect, **VN/VND**, labels the type credit/debit cards, marks refunds positive with an unresolved “See note” and marks recurring, partial/multiple partial refunds and captures, and chargebacks with x (raw lines 31–33). No note explaining the refund check is present in the captured page; the markers are not actual refund or settlement proof. Web, iOS, Android, API-only and Pay by Link entries are child routes requiring separate implementation evidence (raw lines 35–65).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-napas-card]] → [[raw/adyen/docs/payment-methods/napas-card/2026-09-15]].
