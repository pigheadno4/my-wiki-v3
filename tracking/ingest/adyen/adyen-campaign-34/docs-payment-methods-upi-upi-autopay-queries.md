# UPI Autopay retrieval check

Q1. What recurring use cases and signup flow does this UPI Autopay guide describe?

It covers fixed subscriptions with the Subscription model and non-fixed top-ups with UnscheduledCardOnFile. Signup choices are UPI Collect, QR and mobile/mobile-web Intent; the shopper reviews mandate details in a participating UPI app and enters a PIN. Initial mandate creation and first charge are separate, with tokenization conditioned on the successful first payment. See raw lines 19–54. Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-upi-upi-autopay]] → [[raw/adyen/docs/payment-methods/upi/upi-autopay/2026-09-15]].

Q2. What happens if the first charge or free-trial refund fails, and what conditions govern later debits?

The page says Adyen automatically cancels a newly created mandate if its first payment fails; a fresh signup can be initiated, and details are tokenized only after a successful initial payment (raw lines 48–54). For later debits it describes at least 24-hour pre-debit notice, debit below ₹15,000, and a new PIN prompt at ₹15,000 or above (raw lines 43–46). A zero-INR mandate is unsupported; the free-trial workaround authorizes at least 2 INR and starts an automatic refund after successful authorization. On auto-refund failure, `REFUND_FAILED` is sent and the standard refund flow should be retried (raw lines 77–87). These steps do not prove any mandate, debit or refund completed. Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-upi-upi-autopay]] → [[raw/adyen/docs/payment-methods/upi/upi-autopay/2026-09-15]].
