# C22 worker retrieval checks — docs-issuing-components-overview

## Q1: What components and integration shape does this Issuing-path page describe?

It lists Transfer Instrument before payment for bank-account add/update/delete, instant or document verification and verification-status display, and Transactions after payment for filtering/export and details such as fees, IDs and refunds (raw lines 36–54). A suitable platform has an embeddable UI and backend API layer; the server validates the logged-in user and creates a role-bearing session token, which the client uses to initialize the component (lines 23–26, 56–74). Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-components-overview]] → [[raw/adyen/docs/issuing/components-overview/2026-09-15]].

## Q2: What are the component-scope and outcome boundaries?

The captured page says components are generally available where **Adyen for Platforms** is supported (raw line 78), and lists browser minima Chrome 98, Safari 15.4 and Firefox 94 (lines 80–88). That dated statement alone does not prove Issuing eligibility for any platform. The listed UI functions and simplified session flow do not prove that a transfer instrument became verified or that any payment or refund succeeded; the page says some components have additional steps or conditions in their integration guides (lines 40–54, 67–69). Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-components-overview]] → [[raw/adyen/docs/issuing/components-overview/2026-09-15]].
