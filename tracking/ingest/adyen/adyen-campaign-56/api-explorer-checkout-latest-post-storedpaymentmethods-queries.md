# Checkout POST /storedPaymentMethods query audit

Source: `source-adyen-api-explorer-checkout-latest-post-storedpaymentmethods` — https://docs.adyen.com/api-explorer/Checkout/latest/post/storedPaymentMethods. Fully read pinned raw lines 1–90 and 91–168; SHA-256 `8f1b51e1023bd4f480b1f38091493fb3cff8d2a7fa89380bfd27ad501ae4e43c`.

## Q1: For `post/storedPaymentMethods`, what is the endpoint purpose and object identity, and which central required or conditional inputs/prerequisites govern using it?

`POST /storedPaymentMethods` creates a token storing a shopper's payment details for potential future payments (raw lines 5–7). This is a stored payment method, not a payment authorization. The request table requires `merchantAccount`, `paymentMethod`, `recurringProcessingModel`, and `shopperReference` (lines 20–40). It lists the three recurring model values at line 37. The nested card fields are marked optional individually, with raw `cvc`, expiry, and number collection restricted to fully PCI-compliant collectors (lines 25–36). The page does not establish consent or account eligibility; the broader tokenization concept routes to those guides.

## Q2: For `post/storedPaymentMethods`, what does the documented response or failure establish, and which lifecycle, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?

The documented `201 Success` says a resource was created (lines 81–84). The response table marks stored-method `id` optional and describes it as the identifier; examples include the ID, masked card details, and shopper reference (lines 108, 140–168). This capture lists no error response or later payment outcome, and does not establish token reuse, authorization, or settlement. The only listed server is Checkout **test v72** (lines 9–10); `latest` in the retrieval URL does not establish a current version or live behavior.
