<!-- Source: Stripe Terminal — Mail order and telephone order (MOTO) payments -->
<!-- Fetched: 2026-04-24 -->

# Mail order and telephone order (MOTO) payments

Learn how to process mail order and telephone order payments using Stripe Terminal.

Mail order and telephone order (MOTO) enables you to take payments over the phone or by mail by entering card details on a Stripe Terminal reader.

**Supported readers**: [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md), [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md)

> #### Requesting access
>
> To begin taking MOTO payments, contact [Stripe support](https://support.stripe.com/) for access.

Stripe Terminal provides you a user interface to input card details when taking payments or saving cards with MOTO. When using MOTO, the reader prompts you to enter the cardholder’s card number, CVC, expiration date, and postal code. The reader then displays a summary of the card details, before submitting them for confirmation.

MOTO transactions are card-not-present (CNP) transactions, and features available to card-present transactions (such as _liability shifts_ (With some 3D Secure transactions, the liability for fraudulent chargebacks (stolen or counterfeit cards) shifts from you to the card issuer) and [pricing](https://stripe.com/terminal#pricing)) don’t apply to these subsequent charges.

> #### Security awareness
>
> When receiving card details over the phone or mail, you’re responsible for verifying the identity of the customer.

## Integration options

You can collect MOTO payments in two ways, depending on your business needs:

- [Process MOTO payments](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments.md)
- [Save card with MOTO for future payments](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly.md)

## Compliance

You can only submit MOTO transactions when the cardholder isn’t present and they initiate the instruction over the phone or by mail. You must only submit transactions as MOTO transactions if you have determined they’re eligible. When building your checkout flow, make sure you obtain all necessary customer consents and agreements to save card details for future use. You must comply with all applicable laws and rules in your region. Review your compliance obligations, [including PCI requirements](https://stripe.com/guides/pci-compliance#how-stripe-helps-organizations-achieve-and-maintain-pci-compliance).

## Availability

> MOTO isn’t available in Malaysia.
