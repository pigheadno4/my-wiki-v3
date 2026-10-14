# C08 shopper-engagement overview — fixed retrieval checks

1. **Q: What does Adyen's pinned shopper-engagement overview mean by shopper engagement, and which examples does it give?**
   **A:** It means using the payment terminal to interact with customers. The page lists showing Terms and Conditions, asking for an opinion or contact details, and printing a ticket; it says these operations often appear in advanced flows such as loyalty. Evidence: `raw/adyen/docs/point-of-sale/shopper-engagement/2026-09-15.md:14-22`; canonical URL: https://docs.adyen.com/point-of-sale/shopper-engagement. The examples do not establish any completed interaction or payment.

2. **Q: Which detailed topics does this overview route to, and what does it establish about session and payment behavior?**
   **A:** It links to Display (data on terminal), Input (input on terminal), Print (data on terminal), and Session (a session spanning multiple requests). The overview gives no request fields, session lifetime, timeout or asynchronous result semantics, privacy/consent process for contact details, or payment/refund operation. Evidence: `raw/adyen/docs/point-of-sale/shopper-engagement/2026-09-15.md:24-40`; canonical URL: https://docs.adyen.com/point-of-sale/shopper-engagement. Those questions require the linked detailed guides and separate financial-operation evidence.
