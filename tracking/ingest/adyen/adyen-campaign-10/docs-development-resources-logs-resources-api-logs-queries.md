# Fixed retrieval checks: Adyen API logs

## Q1 — Access, scope and retention

**Query:** Which Adyen API requests appear in Customer Area API logs, who can view them, and how long are they retained?

**Expected answer:** This dated page says API logs support JSON API requests in test or live from the preceding 30 days; older requests are removed. It names Customer Area user roles **Merchant admin** and **Technical integrator**. The page places ordinary logs under company or merchant account **Developers > API logs**, while APIs used in a balance-platform integration are available on the company account. The exact role label differs from the Developer dashboard guide's **Merchant technical integrator** label and should not be silently equated. These are user-access roles, separate from API credential roles.

**Raw locators:** log purpose and retention, lines 17–23; JSON, roles, account placement and navigation, lines 25–38. **Canonical retrieval route:** [[adyen-developer-dashboard]] → [[source-adyen-docs-development-resources-logs-resources-api-logs]] → [[raw/adyen/docs/development-resources/logs-resources/api-logs/2026-09-15|pinned raw]].

## Q2 — Search, response detail and evidence boundary

**Query:** What can an investigator see or search in API logs, and does an absent log item or a displayed response establish a final payment outcome?

**Expected answer:** An item shows its timestamp, API, PSP reference or resource ID, and request/response details. Search accepts a PSP reference or request ID, with date, API, endpoint and HTTP-method filters. Request and response bodies can help debug failures; the page's 422 invalid-input example is illustrative. API exchanges are technical evidence, not proof of final authorization, capture or settlement. Absence outside JSON support, 30-day retention or the relevant account context cannot prove no call or payment occurred. Full details may be sensitive; the page does not promise redaction. The 30-day API-log window is distinct from the dashboard's default seven-day trend view.

**Raw locators:** fields and filters, lines 34–38; troubleshooting and 422 example, lines 40–56. **Canonical retrieval route:** [[adyen-developer-dashboard]] → [[source-adyen-docs-development-resources-logs-resources-api-logs]] → [[raw/adyen/docs/development-resources/logs-resources/api-logs/2026-09-15|pinned raw]].
