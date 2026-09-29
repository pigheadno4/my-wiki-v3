# C20 fixed query audit — Group D

## Kount Custom

**Route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-kount-custom.md` → `wiki/sources/braintree/source-braintree-fraud-tools-premium-kount-custom.md` → `raw/braintree/articles/guides/fraud-tools/premium/kount-custom-2026-09-16.md`

**Evidence pin:** embedded URL `https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/kount-custom` matches the manifest; SHA-256 `f7b7ab3b8baaf8b10af276704eea982ab032e5ae63217a53d118cb41fc501170` matches the pinned hash. The raw was read completely (125 lines).

### Where is Kount Custom documented?

- **Object/action match:** Kount Custom product documentation and its retrieval location; the route reaches the Kount Custom concept, source, and exact pinned Kount Custom raw rather than a sibling Braintree fraud product.
- **Direct answer:** It is documented by `source-braintree-fraud-tools-premium-kount-custom`, backed by the pinned Braintree Kount Custom guide at the raw path in the route above.
- **Exact raw locator:** `raw/braintree/articles/guides/fraud-tools/premium/kount-custom-2026-09-16.md`, `# Kount Custom` (line 14), with the page-scoped availability statement at lines 17–18; canonical source URL at line 1.
- **Verdict:** **PASS**

### Which integration and decision responsibilities does this page assign, with what limits?

- **Object/action match:** Kount Custom transaction-risk handoff, fixed gateway actions, integration/support ownership, and limits; this is gateway risk decisioning, not 3D Secure cardholder authentication.
- **Direct answer:** For a new transaction, Braintree sends transaction information to Kount and waits within a small communication window. Kount Custom account rules and matching Braintree custom fields/UDFs influence Kount's risk decision, but Braintree's action mapping is fixed: **Decline** is gateway rejected; **Approve**, **Review**, and **Escalate** are sent to the processor; **Not Evaluated** is sent to the processor by default. Sending to the processor is not processor approval or settlement. Braintree finalizes the received decision when its communication window closes and does not re-evaluate; Kount may continue, leaving a persistent Braintree/Kount discrepancy. **Not Evaluated** can follow a timeout or evaluation error, but this page documents configurable gateway rejection only for the timeout case. Kount Account Managers own questions about scores, fraud rules, Kount reporting/console, and UDFs; Braintree owns device-data issues, Braintree custom-field mapping, and integration issues. The page also says Kount Custom is no longer offered to new merchants, without establishing migration, equivalence, or current eligibility for Fraud Protection Advanced.
- **Exact raw locator:** interaction/finality at `### Braintree and Kount interaction`, lines 23–31; mappings and rule influence at `### Risk decisions`, lines 36–50; Not Evaluated and discrepancy limits at lines 53–68; UDF/custom-field integration prerequisite at lines 71–93; support ownership at `### Getting help`, lines 108–124; new-merchant availability at lines 17–18.
- **Verdict:** **PASS**

## 3D Secure

**Route:** `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-3d-secure.md` → `wiki/sources/braintree/source-braintree-fraud-tools-3d-secure.md` → `raw/braintree/articles/guides/fraud-tools/3d-secure-2026-09-16.md`

**Evidence pin:** embedded URL `https://developer.paypal.com/braintree/articles/guides/fraud-tools/3d-secure` matches the manifest; SHA-256 `bc144e139ba14960957def77027a1e8adc562253dc70fbfd4f772ca6958dd589` matches the pinned hash. The raw was read completely (98 lines).

### Where is Braintree 3D Secure documented?

- **Object/action match:** Braintree 3D Secure documentation and its retrieval location; the route reaches the 3D Secure authentication concept, source, and exact pinned 3D Secure raw rather than a gateway risk-decision product.
- **Direct answer:** It is documented by `source-braintree-fraud-tools-3d-secure`, backed by the pinned Braintree 3D Secure article at the raw path in the route above.
- **Exact raw locator:** `raw/braintree/articles/guides/fraud-tools/3d-secure-2026-09-16.md`, `# 3D Secure` (lines 14–16); canonical source URL at line 1.
- **Verdict:** **PASS**

### What authentication purpose, integration route and limits does this page itself explain?

- **Object/action match:** 3D Secure cardholder-authentication purpose, checkout/setup route, compatibility, enrollment, fees, and conditional liability-shift limits; this is not Kount/Braintree gateway risk decisioning or payment authorization.
- **Direct answer:** The page defines 3DS as an added authentication step for online credit- and debit-card purchases. During checkout Braintree performs a 3DS lookup; for an enrolled cardholder, the issuer decides whether supplied data is sufficient or an additional challenge is needed, and the Braintree SDK displays the issuer's dialog/iframe when required. The setup route is to read the linked 3DS developer docs and then contact Braintree to enroll, with Control Panel confirmation available afterward. The collected page limits compatibility to credit-card, debit-card, and Secure Remote Commerce transactions, says production accounts outside the EEA are not automatically enrolled, and says only certain configurations are compatible; American Express SafeKey needs separate confirmation/enabling and fees may depend on pricing. Fraud-chargeback liability shifts only in certain status-code cases, not for every 3DS transaction, and a shift does not always trigger automatic representation, so merchants must still monitor and act on chargebacks. Authentication therefore does not establish payment authorization, processor approval, a gateway fraud decision, or guaranteed chargeback protection.
- **Exact raw locator:** purpose at `# 3D Secure`, line 16; lookup/issuer challenge and status scope at `## Processing`, lines 26–30; compatibility/enrollment/configuration at lines 33–39; SafeKey at lines 42–54; fee qualification at lines 59–61; conditional liability shift and continuing merchant duties at `### Chargebacks`, lines 64–74; developer-doc/enrollment route and Control Panel confirmation at lines 79–95.
- **Verdict:** **PASS**

## Shared bounded checks

- **Gap sweep / extra reads:** A bounded filename and content sweep covered Kount, 3D Secure, and fraud-tool raw under `raw/braintree/`. No additional raw was selected for full reading: the two pinned pages fully answer the four fixed questions, each detail question expressly asks what that page itself documents, and the other hits concern sibling premium products, generic fraud-tool navigation, SDK-specific 3DS implementation/options, regional requirements, or adjacent payment methods. The source pages' related raw references remain navigation-only: Fraud Protection Advanced is a separate Kount sibling product; the 3DS developer overview is the linked implementation route; the fraud-tools overview does not establish that 3DS performs gateway decisioning. No historical version was needed.
- **Reciprocal links:** `wiki/index.md` routes to `wiki/braintree-index.md`; the provider index lists both concepts and both sources; each concept links its matching source; each source links its matching main concept and exact pinned raw. All required reciprocal retrieval links resolve. **PASS**

**Group D verdict: PASS — 4/4 fixed questions are directly answerable through the required routes with matching object/action, exact pinned evidence, and no material retrieval gap.**
