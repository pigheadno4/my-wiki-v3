# C21 worker queries — manage cards

Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-cards]] → [[raw/adyen/docs/issuing/manage-cards/2026-09-15]].

## Q1. What card-management actions does this page document and what must be true before changing the linked balance account?

For an already created Issuing card represented by a payment instrument, the page covers balance-account reassignment, activation, suspension, permanent closure, and viewing card payments (raw lines 19–25). A `balanceAccountId` change via Balance Platform `PATCH /paymentInstruments/{id}` is allowed only while the card is `inactive` (raw lines 27–31); the response carries the updated payment instrument (raw line 223). Activation, suspension, and closure are also offered via the API or Customer Area (raw lines 229, 442, 670).

## Q2. Which lifecycle or failure boundaries matter?

Suspension temporarily stops payment processing and can be reversed by setting the card back to `active` (raw lines 440, 664). API suspension requires a listed `statusReason`; `other` also requires `statusComment` (raw lines 459–463). Closure cannot be reversed and uses `status: closed` with one of the listed closure reasons (raw lines 668, 686–689). Physical cards are recommended to stay inactive until received (raw line 227), and activating a card only means it can start processing payments (raw line 436). The Customer Area payment list defaults to six months (raw lines 894–903). The page's samples use test endpoints and older named SDK versions; they do not prove live card or payment outcomes (raw lines 37–44, 49–50, 71–72, 123–124).
