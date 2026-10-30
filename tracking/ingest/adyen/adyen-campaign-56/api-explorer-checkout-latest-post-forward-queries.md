# Checkout POST /forward query audit

Source: `source-adyen-api-explorer-checkout-latest-post-forward` — https://docs.adyen.com/api-explorer/Checkout/latest/post/forward. Fully read pinned raw lines 1–60 and 61–111; SHA-256 `2a05768d5eb5988728ba0f3f61444f60a87f6e4f93f05e7abbd623909cd6bea1`.

## Q1: For `post/forward`, what is the endpoint purpose and object identity, and which central required or conditional inputs/prerequisites govern using it?

It forwards Adyen-stored card details or network tokens to a specified third-party API and returns that party's response (raw lines 5–7). The request table requires `baseUrl`, `merchantAccount`, `request`, and `shopperReference`; `request.body` and `request.httpMethod` are required within the request object (lines 20–55). The body uses placeholders replaced by Adyen; network-token forwarding calls for a conditional body that checks token existence (line 50). `storedPaymentMethodId` is marked optional in this schema, as are card details and forwarding options (lines 29–56). Raw card-number collection carries a full PCI-compliance qualification (line 47). The broader forwarding guide covers setup and eligibility.

## Q2: For `post/forward`, what does the documented response or failure establish, and which lifecycle, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?

The page documents `200 Success` for the forwarding request and a required `response` object containing what Adyen received from the third party; its status, headers, and body fields are optional (lines 78–92). Its example third-party `success` string is sample data (lines 94–111), not proof of authorization or settlement. No failure-response table appears in this capture. `dryRun` is test-only and masks sensitive response information (line 31). The listed server is Checkout test v72 (lines 9–10); `latest` in the URL does not prove current or live behavior.
