# C68 worker query answers: api-explorer-management-latest-delete-companies-companyid-terminalthemes-id

## Q1

The 2026-11-07-captured Management API `latest` `DELETE /companies/{companyId}/terminalThemes/{id}` lists TEST server `https://management-test.adyen.com/v3`. It deletes the terminal theme selected by required theme `id` under required company-account `companyId`; the caller's API credential needs **Management API - Terminal themes read and write**. If that theme is in use, it must first be deactivated through `/companies/{companyId}/terminalThemes/unapply`. There is no listed query parameter, request body, default, or numeric limit. The success response is `204`, “Theme deleted,” with no response fields. [[source-adyen-api-explorer-management-latest-delete-companies-companyid-terminalthemes-id]] https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id) (pinned raw lines 5–27).

## Q2

The reference labels `204` as successful theme deletion, after an in-use theme has first been unapplied. It does not state asset-deletion effects, terminal propagation or display state, idempotency, restoration, or a separate asynchronous activation or approval outcome. `401`, `403`, `404`, `409`, and `500` are listed, but the page does not tie `409` to a particular cause; the error bodies shown are examples. This TEST server snapshot does not establish current Live access, device application, compliance, or a payment or donation outcome. [[source-adyen-api-explorer-management-latest-delete-companies-companyid-terminalthemes-id]] https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id) (pinned raw lines 7–14, 21–47, 49–112).
