<!-- Source URL: https://docs.stripe.com/payments/managed-payments/tax-compliance -->
<!-- Fetched: 2026-04-23 -->

# Tax compliance

Learn about the tax offering that Managed Payments provides.

Managed Payments handles indirect tax compliance (sales tax, VAT, and GST) in more than 80 countries. In [these countries](https://docs.stripe.com/payments/managed-payments/tax-compliance.md#cross-border-sales), Stripe:

- Calculates and collects the correct tax amount for sales of digital products where required
- Registers and files tax returns with local tax authorities
- Remits collected taxes to local tax authorities
- Issues tax invoices for sales of digital products where required

No action is required from you to satisfy indirect tax compliance requirements on the sale of digital products in these countries.

In countries where local regulations prevent Managed Payments from assuming liability for indirect taxes, you’re responsible for handling tax compliance. We recommend that you speak to your tax advisor with any questions or concerns.

## Supported countries for tax coverage

Managed Payments handles indirect tax compliance for you on domestic sales and cross-border sales of digital products in certain countries.

### Domestic sales

Managed Payments handles indirect tax compliance for domestic sales of digital goods in all [countries where Managed Payments is available](https://docs.stripe.com/payments/managed-payments/eligibility.md#supported-business-locations), except Singapore (B2B domestic transactions specifically) and Japan (all domestic transactions). If your business is based in Singapore and sells to other businesses, or if your business is based in Japan, you’re responsible for calculating, collecting, filing, and remitting taxes on domestic sales to customers in your home country. For Singapore, a transaction is considered a B2B sale if the buyer indicates that they’re purchasing as a business at checkout.

### Cross-border sales

Managed Payments handles indirect tax compliance when you sell digital products to customers in the following countries.

### Africa

- CM
- EG
- GH
- KE
- NG
- UG
- ZA
- ZM
- ZW

### Asia Pacific

- AM
- AU
- AZ
- BN
- GE
- HK
- ID
- IL
- IN
- JP
- KG
- KR
- KW
- KZ
- LA
- MO
- MY
- NP
- NZ
- PH
- QA
- SA
- SG
- TH
- TJ
- TR
- TW
- VN

### Europe

- AL
- BY
- CH
- GB
- GI
- IS
- LI
- MD
- NO
- RS
- UA

### European Union

- AT
- BE
- BG
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
- GR
- HR
- HU
- IE
- IT
- LT
- LU
- LV
- MT
- NL
- PL
- PT
- RO
- SE
- SI
- SK

### Latin America and the Caribbean

- BB
- BM
- KY
- MX
- VG

### North America

- CA
- US

> Managed Payments only supports cross-border sales to customers in Serbia for sellers that aren’t registered for VAT in Serbia.

## Unsupported countries for tax coverage

For sales to customers in countries where Managed Payments can’t assume liability for tax compliance, you’re responsible for handling all compliance requirements for indirect taxes (sales tax, VAT, and GST). This includes registering your business locally, calculating and collecting tax on transactions, and filing and remitting taxes to local tax authorities.

You can use [Stripe Tax](https://docs.stripe.com/tax.md) to manage these compliance requirements, with no additional charge for Stripe Tax calculation fees on Managed Payments transactions.

You can still use Managed Payments as the merchant of record on these transactions to manage payments, fraud prevention, disputes, and customer support.

### Use Stripe Tax for unsupported countries

Stripe Tax is the only tax solution that’s compatible with Managed Payments. Other tax providers aren’t supported.

1. In the Dashboard, go to **Settings** > **Tax** > [Integrations](https://dashboard.stripe.com/settings/tax/integrations) to enable Stripe Tax.

1. On the [Tax](https://dashboard.stripe.com/settings/tax) page, you can do the following:
   - **Monitor thresholds**: Stripe Tax tracks when you reach tax registration thresholds in each country.
   - **Register with tax authorities**: Stripe Tax offers registration support through third-party partners to register with tax authorities when you reach a certain threshold.
   - **Upload your registration**: Upload your registration to Stripe Tax to begin calculating and collecting taxes automatically.
   - **File and remit taxes**: Stripe Tax offers support through third-party partners for filing and remitting taxes according to local requirements.

### Send invoices for tax-unsupported transactions

Managed Payments sends invoices to your customers for the transactions where you’re responsible for tax compliance. These invoices use your business name and tax details, instead of _Sold through Link, LLC_. Managed Payments will send a receipt email and PDF to your customer, which include details from _[Sold through Link](https://support.link.com/topics/sold-through-link)_.

You can configure the information for these invoices on the [Invoices settings](https://dashboard.stripe.com/settings/billing/invoices/general) page in the Dashboard. You must keep this information up to date, so that your invoices meet local tax documentation requirements.
