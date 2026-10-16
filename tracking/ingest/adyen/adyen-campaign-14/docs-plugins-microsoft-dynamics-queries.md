# Fixed queries — Adyen Dynamics 365 Commerce connector

## Q1 — purpose, scope, and what must not be inferred

**Query:** Which Dynamics 365 product and channels does this Adyen connector guide cover, and what does setup prove?

**Answer:** It covers Dynamics 365 **Commerce**: MPOS uses local Terminal API communications and can operate offline, CPOS uses cloud Terminal API and cannot operate offline, and e-Commerce/Call Center use Checkout API. It does not describe every Dynamics ERP deployment, identify a seller or merchant of record, or prove an actual payment, refund, settlement or bank receipt. Raw: `raw/adyen/docs/plugins/microsoft-dynamics/2026-09-15.md:15-34`. Canonical route: `[[source-adyen-docs-plugins-microsoft-dynamics]]` → `[[adyen-microsoft-dynamics]]`.

## Q2 — central capability, prerequisites, and warnings

**Query:** What channel-specific account, credential, terminal, tokenization and live setup conditions matter?

**Answer:** Start with a test account; when using multiple channels, request a separate merchant account for each and create separate channel API credentials rather than configuring the default company credential. Store keys securely because they cannot be restored if lost. MPOS/CPOS require Adyen Support-enabled POS roles/back-office setup, Immediate POS Capture Delay, and Adyen-software terminals that are ordered and boarded. e-Commerce and Call Center have their own Checkout/payment role lists, with a V002 Origin Key step only for e-Commerce. The live Optional Domain differs: e-Commerce/Call Center need the Adyen merchant prefix, while CPOS uses the documented Terminal API sync URL; check current endpoint guidance. Tokenization needs Support-side enablement. Test each method/channel, then perform separate live account, terminal and Dynamics Headquarters configuration. These steps do not prove a live financial outcome. Raw: `raw/adyen/docs/plugins/microsoft-dynamics/2026-09-15.md:36-55,57-113,116-173,175-231,233-280,282-323,325-358`. Canonical route: `[[source-adyen-docs-plugins-microsoft-dynamics]]` → `[[adyen-microsoft-dynamics]]`.
