# Fixed query answers — api-explorer-document-collector-latest-post-crossborderinvoices

## Q1

The captured [`POST /crossBorderInvoices`](https://docs.adyen.com/api-explorer/Document-Collector/latest/post/crossBorderInvoices) belongs to **Document Collector latest**, with test and live `/v1` servers, and uploads a document for the request's `merchantAccount`. Required request fields are `context=paCbInvoice`, PDF `file` named `{pspReference}.pdf`, and `merchantAccount`. The PSP reference is a filename-derived identity in the optional success response, not a separate required request field. The page does not define a device/session identity, size limit, retention period, processing lifecycle, reversal or timing rule. Source: [[source-adyen-api-explorer-document-collector-latest-post-crossborderinvoices]]; raw lines 5–47.

## Q2

The [contract](https://docs.adyen.com/api-explorer/Document-Collector/latest/post/crossBorderInvoices) says `201 Success` means the document was uploaded successfully; `context`, `fileName`, `merchantAccount` and filename-extracted `pspReference` are optional response properties. It also documents `400`, `401`, `403`, `422`, and `500` problem responses; examples include account-access denial and invalid PDF filename. It does not specify an authentication method, idempotency/correlation beyond optional error `requestId`, asynchronous review/result, version transition or deprecation. Upload receipt does not prove invoice acceptance/reconciliation, payment authorization, settlement or bank receipt. Source: [[source-adyen-api-explorer-document-collector-latest-post-crossborderinvoices]]; raw lines 36–224.
