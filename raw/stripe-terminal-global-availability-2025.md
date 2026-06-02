<!-- Source: Stripe Terminal — Global availability (countries + payment methods) -->
<!-- Fetched: 2026-04-23 -->

# Stripe Terminal global availability

Learn about where you can use Terminal and which payment methods you can accept.

Terminal is available in the following countries:

- AT
- AU
- BE
- CA
- CH
- CZ
- DE
- DK
- ES
- FI
- FR
- GB
- IE
- IT
- LU
- MY
- NL
- NO
- NZ
- PT
- SE
- SG
- US

### Available in (Preview)

- BG\*
- CY\*
- EE\*
- GI\*
- HR\*
- HU\*
- JP
- LI\*
- LT\*
- LV\*
- MT\*
- PL
- RO\*
- SI\*
- SK\*

> In countries marked with an asterisk (\*), only Tap to Pay is available.

## Payment method availability

When you integrate Stripe Terminal, you can accept a variety of payment methods. Your reader automatically configures itself to accept the payment methods relevant for its region. When processing an in-person transaction, Terminal requires you to use local currency. Terminal supports NFC-based mobile wallets (Apple Pay, Google Pay, and Samsung Pay).

| Payment method                                                                                                             | Payment method type | Terminal location and Stripe account country                                                                                                                                                            | Reader types                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Visa                                                                                                                       | Card                | All countries where Terminal is supported                                                                                                                                                               | All                                                                                                                                                                                                                                                                                                                                                                |
| Mastercard                                                                                                                 | Card                | All countries where Terminal is supported                                                                                                                                                               | All                                                                                                                                                                                                                                                                                                                                                                |
| American Express                                                                                                           | Card                | All countries where Terminal is supported, except Malaysia                                                                                                                                              | All                                                                                                                                                                                                                                                                                                                                                                |
| Discover & Diners                                                                                                          | Card                | United States, Canada, Japan2, and EMEA                                                                                                                                                                 | **US**: Verifone P400, Stripe M2, Chipper 2X BT, WisePOS E, Stripe Reader S700, Stripe Reader S710, Tap to Pay on iPhone, and Tap to Pay on Android**CA, EMEA**: WisePad 3, WisePOS E, Stripe Reader S700, Stripe Reader S710, Tap to Pay on iPhone, and Tap to Pay on Android**JP**2: WisePad 3, Stripe Reader S700, Stripe Reader S710, and Tap to Pay on iPhone |
| China Union Pay3                                                                                                           | Card                | United States, Canada                                                                                                                                                                                   | **US, CA**: Stripe M2, WisePad 3, WisePOS E4, Stripe Reader S700, and Stripe Reader S710                                                                                                                                                                                                                                                                           |
| [eftpos](https://docs.stripe.com/terminal/payments/regional.md?integration-country=AU#eftpos-payments)                     | Card                | Australia                                                                                                                                                                                               | WisePad 3, WisePOS E, Stripe Reader S700, Stripe Reader S710, Tap to Pay on iPhone, and Tap to Pay on Android                                                                                                                                                                                                                                                      |
| [girocard](https://docs.stripe.com/terminal/payments/regional.md?integration-country=DE#girocard-payments)                 | Card                | Germany                                                                                                                                                                                                 | WisePad 3, Stripe Reader S700                                                                                                                                                                                                                                                                                                                                      |
| [Cartes Bancaires](https://docs.stripe.com/terminal/payments/regional.md?integration-country=FR#cartes-bancaires-payments) | Card                | France                                                                                                                                                                                                  | WisePad 3, Stripe Reader S700, Stripe Reader S710, Tap to Pay on iPhone, and Tap to Pay on Android 5                                                                                                                                                                                                                                                               |
| [Interac](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#interac-payments)                   | Card                | Canada                                                                                                                                                                                                  | WisePad 3, WisePOS E, Verifone P400, Stripe Reader S700, Stripe Reader S710, Tap to Pay on iPhone, and Tap to Pay on Android5                                                                                                                                                                                                                                      |
| JCB6                                                                                                                       | Card                | United States, Canada, Australia, New Zealand, and Japan                                                                                                                                                | **US**: Stripe M2, WisePad 3, WisePOS E4, Stripe Reader S700, Stripe Reader S710, and Tap to Pay on iPhone**CA, AU, NZ**: Stripe M2, WisePad 3, WisePOS E4, Stripe Reader S700, and Stripe Reader S710**JP**: WisePad 3, Stripe Reader S700, Stripe Reader S710, and Tap to Pay on iPhone                                                                          |
| Maestro                                                                                                                    | Card                | All non-US countries where Terminal is supported. As of July 2023, new Maestro cards aren’t issued. Expired cards will be replaced with Debit Mastercard.                                               | WisePad 3, WisePOS E, Verifone P400, Stripe Reader S700, Stripe Reader S710, Tap to Pay on iPhone, and Tap to Pay on Android                                                                                                                                                                                                                                       |
| [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md)                                                               | Wallet              | Australia, Austria, Belgium, Canada, Denmark, Finland, France, Germany, Ireland, Italy, Luxembourg, Netherlands, Norway, Portugal, Singapore, Spain, Sweden, Switzerland, United Kingdom, United States | WisePOS E, Stripe Reader S700, Stripe Reader S710, Tap to Pay on Android, Tap to Pay on iPhone                                                                                                                                                                                                                                                                     |
| [Affirm](https://docs.stripe.com/payments/affirm.md)                                                                       | Buy now, pay later  | United States, Canada, and United Kingdom                                                                                                                                                               | WisePOS E, Stripe Reader S700, Stripe Reader S710, Tap to Pay on Android, Tap to Pay on iPhone                                                                                                                                                                                                                                                                     |
| [PayNow](https://docs.stripe.com/payments/paynow.md)                                                                       | Real-time payments  | Singapore                                                                                                                                                                                               | WisePOS E, Stripe Reader S700, Stripe Reader S710, Tap to Pay on Android, Tap to Pay on iPhone                                                                                                                                                                                                                                                                     |

1Review the [region specific requirements](https://docs.stripe.com/terminal/payments/regional.md) of the country you’re integrating in.

2Diners isn’t supported in [Japan](https://docs.stripe.com/terminal/payments/regional.md?integration-country=JP).

3China Union Pay is supported over the Discover network in the United States and Canada.

4The WisePOS E only supports China Union Pay and JCB for EMV chip transactions where the card is inserted into the reader. Contactless isn’t supported.

5This payment method is in public preview.

6JCB is accepted through the Discover network in the United States and the American Express network in Canada, Australia, and New Zealand.
