<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/ -->
<!-- Fetched: 2026-04-13 -->
<!-- Note: Demo GIF (mobile-3ds-cursor.gif) is CDN-restricted and could not be saved -->

Online / Checkout / Expanded / Customize / 3D Secure authentication

# 3D Secure authentication

Use 3D Secure to authenticate card holders through card issuers. It reduces the likelihood of fraud when you use supported cards and improves transaction performance. A successful 3D Secure authentication can shift liability for fraudulent chargebacks from you to the card issuer.

3D Secure authentication is performed only if the card is enrolled for the service. When your customer submits their card details on your website for processing, you have the option of triggering 3D Secure. When triggered, customers are prompted by their card issuing bank to complete an additional verification step to enter a one-time or static password, depending on the implementation.

## How it works

[Demo GIF not saved — CDN-restricted. View at: https://www.paypalobjects.com/devdoc/img/docs/3ds/mobile-3ds-cursor.gif]

This demo shows a checkout flow that triggers authentication with 3D Secure.

## How do you want to integrate?

- **JavaScript SDK** — See the JavaScript SDK page for parameters.
- **Orders API** — See the Orders API documentation.

## Eligibility

3D Secure is available for advanced Checkout payment integrations.

Advanced Checkout payments are available for **36 countries** and **22 currencies**.

### Card brand currency table

| Country | Card brands | Currencies |
| ------- | ----------- | ---------- |
| Australia (AU) | Mastercard, Visa, American Express, eftpos (AUD only) | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Austria (AT) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Belgium (BE) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Bulgaria (BG) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Canada (CA) | Mastercard, Visa, American Express (CAD and USD only), JCB (CAD only) | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Cyprus (CY) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Czech Republic (CZ) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Denmark (DK) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Estonia (EE) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Finland (FI) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| France (FR) | Mastercard, Visa, American Express, Carte Bancaire (EUR only) | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Germany (DE) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Greece (GR) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Hong Kong (HK) | Mastercard, Visa | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Hungary (HU) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Ireland (IE) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Italy (IT) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Japan (JP) | Mastercard, Visa, American Express (JPY only), JCB (JPY only) | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Latvia (LV) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Liechtenstein (LI) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Lithuania (LT) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Luxembourg (LU) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Malta (MT) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Mexico (MX) | Mastercard, Visa, American Express | MXN only |
| Netherlands (NL) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Norway (NO) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Poland (PL) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Portugal (PT) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Romania (RO) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Singapore (SG) | Mastercard, Visa | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Slovakia (SK) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Slovenia (SI) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Spain (ES) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| Sweden (SE) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| United Kingdom (GB) | Mastercard, Visa, American Express | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |
| United States (US) | Mastercard, Visa, American Express, Discover (USD only), Debit networks — Star/Star Access, Pulse, Nyce, Accel (USD only), China Union Pay (USD only), JCB (USD only), Diners (USD only) | AUD, BRL, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, ILS, JPY⁰, MXN, NOK, NZD, PHP, PLN, SEK, SGD, THB, TWD⁰, USD |

⁰ Indicates a 0-digit denomination currency (JPY, TWD).
