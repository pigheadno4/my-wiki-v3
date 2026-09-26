# Braintree C16 Query Audit — Group D

- Scope: Transaction Issues + Email Receipts.
- Audited: `2026-09-23` UTC after both source promotions.
- Evidence: both selected raw pages read completely; current source and root/provider-index → concept routes inspected.

## Transaction Issues

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-control-panel-transaction-issues]]` → `[[raw/braintree/articles/control-panel/transactions/transaction-issues-2026-09-16]]`.

1. **Query:** Where is Braintree Control Panel Transaction Issues documented?
   - **Object/action match:** Rare additional processing issues and their notification route, not standard processor decline or gateway rejection.
   - **Direct answer:** The source above links the complete collected Transaction Issues article.
   - **Exact raw locator:** `# Transaction Issues`, lines 14–16; `## Notifications`, lines 19–36.
   - **Verdict:** PASS; direct provider-index cataloging awaits aggregate close.

2. **Query:** How are transaction issues distinguished from declines/rejections, and which notification or investigation routes are documented?
   - **Object/action match:** Separate category and delivery/recipient configuration; investigation detail is absent.
   - **Direct answer:** The article calls issues rare, unexpected processing problems beyond standard processor declines and gateway rejections. It permits webhook notification alongside email and gives a Control Panel API → Webhooks creation route after permissions/destination preparation. User Recipients receive notifications only for transactions accessible to their role; Email Recipients can be any address and receive all issue notices even if the same address belongs to a limited-permission user. The page documents no cause-specific investigation workflow, remediation or resolution result; those cannot be supplied from this raw.
   - **Exact raw locator:** category distinction line 16; optional webhook/setup route lines 19–30; recipient alternatives and scopes lines 32–36.
   - **Verdict:** PASS, including an explicit evidence gap rather than an invented investigation route.

## Email Receipts

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-control-panel-email-receipts]]` → `[[raw/braintree/articles/control-panel/transactions/email-receipts-2026-09-16]]`.

3. **Query:** Where is Braintree Control Panel Email Receipts documented?
   - **Object/action match:** Gateway transaction/refund receipt activation and configuration, distinct from subscription failed-payment notification.
   - **Direct answer:** The source above links the complete collected Email Receipts raw.
   - **Exact raw locator:** `# Email Receipts`, lines 14–30; `## Enabling email receipts`, lines 38–87.
   - **Verdict:** PASS; direct provider-index cataloging awaits aggregate close.

4. **Query:** Which transaction/refund receipt triggers, configuration and delivery limitations does this article document?
   - **Object/action match:** Successfully submitted-for-settlement transactions/refunds, signer activation, Control Panel options, manual versus merchant-built receipts.
   - **Direct answer:** The gateway can email receipts for successfully submitted-for-settlement transactions/refunds if receipts are enabled and customer email is present. An authorized signer asks Support to activate the feature, then the merchant configures it in Control Panel Processing. With default sending enabled, missing email causes validation error. Sender address is fixed; Reply To, BCC and up to 1,000 plain-text characters can be configured, but HTML/broader custom delivery requires merchant logic. PayPal transactions may yield both PayPal and Braintree receipts. A manual receipt can be generated from Transaction Details, while custom merchant-built receipts are a separate route. Subscription failed-charge alerts belong to another article.
   - **Exact raw locator:** subscription distinction lines 17–18; trigger/prerequisites lines 22–30; PayPal double receipt lines 33–35; activation lines 38–50; options/error/customization lines 53–74; manual/custom distinction lines 99–114.
   - **Verdict:** PASS.

## Bounded gap sweep

- Inspected selected raw and source/concept links for transaction-issue notifications and receipt behavior. Adjacent decline, gateway-rejection, webhook and subscription-notification pages remain navigation-only here.
- Both source/raw backlinks and reciprocal Control Panel concept entries resolve; the Issues source also has a reciprocal Webhooks concept entry. No wrong-object route, receipt/manual conflation, missing recipient-scope warning or invented investigation answer remains. Group D: **4/4 PASS**.
