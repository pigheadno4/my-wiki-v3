# Fixed retrieval queries — Cegid Retail Y2 CPOS setup

## Q1 — Purpose, scope, and what it does not infer

**Question:** What does Adyen’s Cegid Retail Y2 setup page cover, and what cannot be inferred from it?

**Answer:** It is the v2.1.33 CPOS plugin setup guide for installation, local/cloud Adyen Terminal API and Cegid EPT configuration, payment-method mapping, refunds, test transactions, and live setup steps. It is a dated documentation snapshot, not proof of merchant eligibility, a completed integration, or successful live payments. See [[source-adyen-docs-plugins-cegid-retail-y2-set-up-the-plugin]] → [[adyen-cegid-retail-y2]] (overview-worker concept pending), with the root [[index]] → [[adyen-index]] route. Raw: `raw/adyen/docs/plugins/cegid-retail-y2/set-up-the-plugin/2026-09-15.md`, lines 15–21, 23–31, 286–318.

## Q2 — Central capability, prerequisites, and warnings

**Question:** What must a merchant configure for local versus cloud CPOS communications, and what warnings qualify refunds, upgrades, and going live?

**Answer:** Company-level Adyen account setup requires Merchant POS Terminal Management Admin. Local uses Terminal API plus encryption key values stored securely and copied into Cegid EPT, a local terminal IP endpoint, Sale ID and POI ID. Cloud uses a Web service API credential/API key stored securely, Terminal API, Support-enabled WebSockets, and a test sync or geographically appropriate live endpoint. The terminal must carry Adyen software, and Cegid payment methods and the `paymentMethodVariant` mapping must be configured. An existing integration’s upgrade to a later version requires uninstall/reboot before install; changing CPOS installation directory later also requires uninstall/reinstall. Refund configuration has referenced/unreferenced defaults, but partial and multiple-method refunds can be unreferenced regardless. Unknown-result booking can accept a payment after failed transaction; leave Legacy Mode off absent Cegid instruction. Device test is followed by a separate test-card payment, and live setup requires live terminals, live Customer Area configuration and retest; documentation does not prove completion. Raw lines 27–45, 57–115, 116–187, 202–265, 286–318. Canonical route: [[index]] → [[adyen-index]] → [[adyen-cegid-retail-y2]] → [[source-adyen-docs-plugins-cegid-retail-y2-set-up-the-plugin]].
