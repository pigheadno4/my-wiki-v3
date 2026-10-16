# Fixed queries — docs-plugins-salesforce-order-management-system-authorization-reversal

## Q1 — purpose, scope, and non-inference

**Query:** What does Salesforce OMS Authorization Reversal do in this Adyen guide, and does it cancel an order or prove funds were released?

**Answer:** It uses Salesforce's Payment Authorization Reversal Service API and the Adyen OMS package to cancel a payment authorization, such as when an order cannot be fulfilled (raw lines 15–21). The package only cancels the payment; cancelling the Salesforce order needs separate implementer logic (line 82). This setup page and its example webhooks are not proof of an actual cancellation, refund, capture, issuer hold release, or settlement. Canonical route: [[adyen-index]] → [[adyen-salesforce-order-management-system]] → [[source-adyen-docs-plugins-salesforce-order-management-system-authorization-reversal]] → pinned raw. The provider-index concept link was absent in the worker audit and needs coordinator completion.

## Q2 — capability, prerequisites, and warnings

**Query:** What conditions and outcome checks apply to OMS authorization reversal?

**Answer:** The guide requires a functioning OMS Org connected to SFCC, Adyen OMS package v3.1.0+, and the Salesforce API guidance (raw lines 23–27). Expose the Salesforce site non-payment webhook handler; OMS 3.3.0+ needs no additional reversal webhook, while the described manual route configures a standard JSON `CANCELLATION` webhook with the existing HMAC key at the Salesforce endpoint (lines 29–80). The request `amount` must equal Order Payment Summary **Available to Capture** (line 88). Salesforce gateway logs show request status, but the Adyen `CANCELLATION` webhook is the guide's final outcome and carries the original authorization PSP reference, success, and on failure a reason (lines 90–114). The failure paragraph says review/fix/resubmit where possible, while the page's last line directs failed reversals to manual Customer Area reversal; check the particular authorization/state before another action rather than inferring a safe unconditional retry (lines 111–114, 170). Canonical route: [[adyen-index]] → [[adyen-salesforce-order-management-system]] → [[source-adyen-docs-plugins-salesforce-order-management-system-authorization-reversal]] → pinned raw.
