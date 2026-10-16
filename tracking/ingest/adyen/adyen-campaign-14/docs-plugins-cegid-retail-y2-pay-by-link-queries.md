# Fixed queries — docs-plugins-cegid-retail-y2-pay-by-link

## Q1 — purpose, scope, and non-inference

**Query:** What does the Cegid Retail Y2 Pay by Link guide cover, and does a generated or received link prove payment?

**Answer:** It covers Adyen Pay by Link from Cegid Retail Mobile POS or Retail Live Store for an in-store shopper: employee selection, QR or text-message link access, Adyen-hosted checkout and a result returned in the Cegid app (raw lines 15–25, 39–50). A link, QR display, text receipt or result display is not by itself proof of a particular authorization, capture, settlement or bank receipt; this page does not define all result statuses. Method support belongs to linked Pay by Link documentation (lines 21–23). Canonical route: [[adyen-index]] → [[adyen-cegid-retail-y2]] → [[source-adyen-docs-plugins-cegid-retail-y2-pay-by-link]] → pinned raw. The provider-index concept link was absent in the worker audit.

## Q2 — central capability, prerequisites, and warnings

**Query:** Which Cegid apps and version/device/setup conditions govern this Pay by Link route?

**Answer:** Shared requirements are InStoreHub on Windows with CPOS plugin, Cegid Retail Y2 v18+, and an Adyen payment terminal. Retail Mobile POS additionally needs v5.1.607+ and an iOS mobile device; Retail Live Store can use Android/iOS mobile or a browser-capable device (raw lines 29–37). The flow is shared but setup differs: contact Cegid for Mobile POS extension activation, use Cegid setup documentation, and add purchase terms to the Adyen-hosted page; Live Store enablement also directs users to a Cegid representative (lines 52–65). The guide does not specify account credential roles or guarantee SMS delivery, method eligibility, payment success or final funds. Canonical route: [[adyen-index]] → [[adyen-cegid-retail-y2]] → [[source-adyen-docs-plugins-cegid-retail-y2-pay-by-link]] → pinned raw.
