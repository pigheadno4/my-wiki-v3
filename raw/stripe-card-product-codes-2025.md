<!-- Source URL: https://docs.stripe.com/payments/cards/product-codes -->
<!-- Fetched: 2026-05-01 -->

# Card Product Codes

Learn about product codes for cards.

Product codes exist as a way to identify the specific program or product associated with a credit card.

## Retrieving product codes

When using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) for e-commerce payments, Stripe stores the product code on the [PaymentMethod](https://docs.stripe.com/api.md#payment_methods) object, in the `brand_product` field within the `card_present` hash. After successfully confirming a PaymentIntent, the `brand_product` field also includes the product code in the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) for the corresponding charge in the API response for [card_present](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present) payments (using [Terminal](https://docs.stripe.com/terminal.md)).

The `brand_product` field might be `null` if the product code hasn’t been collected yet (for example, when creating a card) or the product codes for the particular card network aren’t supported. We currently support Visa and Mastercard product codes only.

## Product codes

The following table lists product code values for each card brand:

#### Visa

| Product code | Product description               |
| ------------ | --------------------------------- |
| A            | Traditional                       |
| B            | Traditional Rewards               |
| B1           | Visa Secured Enhanced             |
| C            | Signature                         |
| D            | Signature Preferred               |
| DS           | Distribution                      |
| F            | Classic                           |
| F2           | Visa Flexible Credential          |
| F3           | Visa Flexible Credential Standard |
| G            | Business                          |
| G1           | Signature Business                |
| G3           | Platinum Business                 |
| G4           | Infinite Business                 |
| G5           | Business Rewards                  |
| GV           | Government Disbursement           |
| I            | Infinite                          |
| I1           | Visa Infinite Privilege           |
| I2           | Visa Ultra High Net Worth         |
| J3           | Healthcare                        |
| K            | Corporate                         |
| K1           | Government Corporate              |
| L            | Electron                          |
| N            | Platinum                          |
| N1           | Rewards                           |
| N2           | Select                            |
| P            | Gold                              |
| PP           | Payroll                           |
| Q            | Private Label                     |
| Q2           | Private Label Basic               |
| Q3           | Private Label Standard            |
| Q4           | Private Label Enhanced            |
| Q5           | Private Label Specialized         |
| Q6           | Private Label Premium             |
| R            | Proprietary                       |
| S            | Purchasing                        |
| S1           | Purchasing With Fleet             |
| S2           | Government Purchasing             |
| S3           | Government Purchasing With Fleet  |
| S4           | Commercial Agriculture            |
| S5           | Commercial Transport              |
| S6           | Commercial Marketplace            |
| S7           | Distribution                      |
| U            | Travel Money                      |
| V            | V Pay                             |
| X            | Visa Commercial Choice Travel     |
| X1           | Visa Commercial Choice Omni       |

#### Mastercard

| Product Code | Product Description                                            |
| ------------ | -------------------------------------------------------------- |
| ACS          | Digital Debit                                                  |
| BPC          | Bill Pay Commercial                                            |
| BPD          | Business Premium Debit                                         |
| BPE          | Mastercard World Elite Business                                |
| BPL          | Mastercard Business Credit Plus                                |
| CIR          | Cirrus                                                         |
| CPP          | Mastercard Credit Prepaid Platinum                             |
| CPS          | Mastercard Credit Prepaid Standard                             |
| DAG          | Global Debit Mastercard Salary                                 |
| DAP          | Platinum Debit Mastercard Salary                               |
| DAS          | Standard Debit Mastercard Salary                               |
| DBS          | Consumer Charge Card                                           |
| DCB          | Line of Credit or Offset Linked Card                           |
| DCO          | Consumer Elite Card                                            |
| DLA          | Business Executive Charge Card                                 |
| DLG          | Debit Mastercard Gold Delayed Debit                            |
| DLH          | Debit Mastercard World Embossed Delayed Debit                  |
| DLP          | Debit Mastercard Platinum Delayed Debit                        |
| DLS          | Debit Mastercard Card Delayed Debit                            |
| DOS          | Standard Debit Mastercard Social                               |
| DPP          | Mastercard Debit Prepaid Platinum                              |
| DPS          | Mastercard Debit Prepaid Standard                              |
| ETA          | Mastercard Installment Payments A                              |
| ETB          | Mastercard Installment Payments B                              |
| ETC          | Mastercard Installment Payments C                              |
| ETD          | Mastercard Installment Payments D                              |
| ETE          | Mastercard Installment Payments E                              |
| ETF          | Mastercard Installment Payments F                              |
| ETG          | Mastercard Installment Payments G                              |
| ETH          | Prepaid Installment Payments A                                 |
| ETI          | Prepaid Installment Payments B                                 |
| ETJ          | Prepaid Installment Payments C                                 |
| ETK          | Prepaid Installment Payments D                                 |
| ETL          | Prepaid Installment Payments E                                 |
| ETM          | Prepaid Installment Payments F                                 |
| ETN          | Prepaid Installment Payments G                                 |
| FIA          | Mastercard B2B VIP 27                                          |
| FIB          | Mastercard B2B VIP 28                                          |
| FIC          | Mastercard B2B VIP 29                                          |
| FID          | Mastercard B2B VIP 30                                          |
| FIE          | Mastercard B2B VIP 31                                          |
| FIF          | Mastercard B2B VIP 32                                          |
| FIG          | Mastercard B2B VIP 33                                          |
| FIH          | Mastercard B2B VIP 34                                          |
| GCP          | Mastercard Installments Card Premium                           |
| GCS          | Mastercard Shop & Split Standard                               |
| GPP          | Mastercard Prepaid Installments Card Premium                   |
| GPS          | MasterCard Prepaid Installment Payments Card U                 |
| MAB          | World Elite Mastercard for Business Card                       |
| MAC          | Mastercard World Elite Corporate Card                          |
| MAJ          | Mastercard World Legend Business Card                          |
| MAP          | MAP Mastercard Commercial Payments Account                     |
| MAQ          | Mastercard Prepaid Commercial Payments Account                 |
| MBA          | Mastercard B2B Product 2                                       |
| MBB          | Mastercard Prepaid Consumer                                    |
| MBC          | Mastercard Prepaid Voucher                                     |
| MBD          | Mastercard Professional Debit BusinessCard Card                |
| MBE          | Mastercard Electronic Business Card                            |
| MBF          | Prepaid MC Food                                                |
| MBG          | Mastercard B2B Product 3                                       |
| MBH          | Mastercard B2B Product 4                                       |
| MBI          | Mastercard B2B Product 5                                       |
| MBJ          | Mastercard B2B Product 6                                       |
| MBL          | Mastercard B2B Product 28                                      |
| MBN          | Mastercard B2B Product 29                                      |
| MBO          | Mastercard B2B Product 30                                      |
| MBQ          | Mastercard B2B Product 31                                      |
| MBR          | Mastercard B2B Product 32                                      |
| MBK          | Mastercard Black Card                                          |
| MBP          | Mastercard Corporate Prepaid                                   |
| MBT          | Mastercard B2B Product 33                                      |
| MBU          | Mastercard B2B Product 34                                      |
| MBV          | Mastercard B2B Product 35                                      |
| MBX          | Mastercard B2B Product 36                                      |
| MBY          | Mastercard B2B Product 37                                      |
| MBZ          | Mastercard B2B Product 38                                      |
| MCB          | Mastercard BusinessCard Card                                   |
| MCC          | Mastercard Credit Card (mixed BIN)                             |
| MCE          | Mastercard Electronic Card                                     |
| MCF          | Mastercard Fleet Card                                          |
| MCG          | Gold Mastercard Card                                           |
| MCH          | Mastercard Premium Charge                                      |
| MCO          | Mastercard Corporate Card                                      |
| MCP          | Mastercard Purchasing Card                                     |
| MCS          | Standard Mastercard Card                                       |
| MES          | Mastercard Enterprise Solutions                                |
| MBS          | Mastercard B2B Product                                         |
| MBW          | World Mastercard Black Edition Debit                           |
| MET          | Titanium Debit Mastercard Card                                 |
| MCT          | Titanium Mastercard Card                                       |
| MCV          | Merchant-Branded Program                                       |
| MCW          | World Mastercard Card                                          |
| MDA          | Mastercard World Legend Debit                                  |
| MDB          | Debit Mastercard BusinessCard Card                             |
| MDD          | Mastercard CoBadge Debit                                       |
| MDE          | Mastercard Essential Prepaid                                   |
| MDG          | Gold Debit Mastercard Card                                     |
| MDH          | World Debit Embossed Mastercard Card                           |
| MDJ          | Debit Mastercard (Enhanced)                                    |
| MDL          | Business Debit Other                                           |
| MDO          | Debit Other                                                    |
| MDP          | Platinum Debit Mastercard Card                                 |
| MDR          | Debit Brokerage                                                |
| MDS          | Debit Mastercard                                               |
| MDT          | Commercial Debit Mastercard Card                               |
| MDW          | World Elite Debit Mastercard                                   |
| MEB          | Mastercard Executive BusinessCard Card                         |
| MEC          | Mastercard Electronic Commercial                               |
| MEE          | Mastercard Essential Prepaid Credit                            |
| MEF          | Mastercard Electronic Payment Account                          |
| MEO          | Mastercard Corporate Executive Card                            |
| MFB          | Flex World Elite                                               |
| MFD          | Flex Platinum                                                  |
| MFE          | Flex Charge World Elite                                        |
| MFH          | Flex World                                                     |
| MFI          | Mastercard Debit Financial Inclusion                           |
| MFL          | Flex Charge Platinum                                           |
| MFW          | Flex Charge World                                              |
| MGF          | Mastercard Government Commercial Card                          |
| MGS          | Platinum Mastercard Prepaid General Spend                      |
| MGP          | Mastercard Prepaid Gold Payroll                                |
| MHA          | Mastercard Healthcare Prepaid Non-Tax                          |
| MHB          | Mastercard HSA Substantiated (Debit Mastercard)                |
| MHD          | HELOC Debit Standard                                           |
| MHH          | Mastercard HSA Non-Substantiated (Debit Mastercard)            |
| MHK          | Magna Health Access Card                                       |
| MHL          | HELOC Debit Gold                                               |
| MHM          | HELOC Debit Platinum                                           |
| MHN          | HELOC Debit Premium                                            |
| MIA          | Prepaid Mastercard Unembossed Student Card                     |
| MIK          | Prepaid Mastercard Electronic Student (Non-US) Card            |
| MIL          | Unembossed Mastercard Student Card (Non-US)                    |
| MIP          | Prepaid Debit Mastercard Student Card                          |
| MIU          | Debit Mastercard Unembossed (Non-US)                           |
| MKA          | Digital Gold Debit                                             |
| MKB          | Digital Platinum Debit                                         |
| MKC          | Digital World Debit                                            |
| MKD          | Digital World Elite Debit                                      |
| MKE          | Digital Platinum                                               |
| MKF          | Digital World                                                  |
| MKG          | Digital World Elite                                            |
| MKH          | Digital World Elite Exclusive                                  |
| MLA          | Mastercard Central Travel Solutions Air Card                   |
| MLB          | Mastercard Brazil Benefit for Home Improvement                 |
| MLD          | Mastercard Distribution Card                                   |
| MLE          | Mastercard Brazil General Benefits                             |
| MLF          | Mastercard Agro                                                |
| MLL          | Mastercard Central Travel Solutions Land Card                  |
| MNF          | Mastercard Public Sector Commercial Card                       |
| MNW          | Mastercard World Card                                          |
| MOC          | Standard Maestro Social                                        |
| MOG          | Maestro Gold Card                                              |
| MOP          | Maestro Platinum                                               |
| MOW          | World Maestro                                                  |
| MPA          | Prepaid Debit Standard Payroll                                 |
| MPB          | Mastercard Preferred Business Card                             |
| MPD          | Mastercard Flex Prepaid                                        |
| MPF          | Mastercard Prepaid Debit Standard Gift                         |
| MPG          | Debit Mastercard Standard Prepaid General Spend                |
| MPH          | Mastercard Cash                                                |
| MPJ          | Prepaid Debit Mastercard Card Gold                             |
| MPK          | Mastercard Prepaid Government Commercial Card                  |
| MPL          | Platinum Mastercard Card                                       |
| MPM          | Mastercard Prepaid Debit Standard Consumer Incentive           |
| MPN          | Mastercard Prepaid Debit Standard Insurance                    |
| MPO          | Mastercard Prepaid Debit Standard Offer                        |
| MPP          | Mastercard Prepaid Card                                        |
| MPQ          | White Label Routing                                            |
| MPR          | Mastercard Prepaid Debit Standard Travel                       |
| MPT          | Mastercard Prepaid Debit Standard Teen                         |
| MPV          | Mastercard Prepaid Debit Standard Government                   |
| MPW          | Debit Mastercard Business Card Prepaid Workplace Business      |
| MPX          | Mastercard Prepaid Debit Standard Flex Benefit                 |
| MPY          | Mastercard Prepaid Debit Standard Employee Incentive           |
| MPZ          | Mastercard Prepaid Debit Standard Government Consumer          |
| MRB          | Mastercard Prepaid Electronic Business Card (Non-US)           |
| MRC          | Prepaid Mastercard Electronic Card (Non-US)                    |
| MRD          | Mastercard Prepaid Platinum Debit General Spend (Asia-Pacific) |
| MRF          | Standard Deferred                                              |
| MRG          | Mastercard Prepaid Card (Non-US)                               |
| MRH          | Mastercard Platinum Prepaid Travel (US)                        |
| MRJ          | Prepaid Mastercard Gold Card                                   |
| MRK          | Prepaid Mastercard Public Sector Commercial Card               |
| MRL          | Prepaid Mastercard Electronic Commercial Card (Non-US)         |
| MRO          | Mastercard Rewards Only                                        |
| MRP          | Standard Retailer Centric Payments                             |
| MRS          | Prepaid Mastercard ISIC Student Card                           |
| MRW          | Prepaid Mastercard Business Card (Non-US)                      |
| MSA          | Prepaid Maestro Payroll Card                                   |
| MSB          | Maestro Small Business Card                                    |
| MSF          | Prepaid Maestro Gift Card                                      |
| MSG          | Prepaid Maestro Consumer Reloadable Card                       |
| MSI          | Maestro Small Business Card                                    |
| MSJ          | Prepaid Maestro Gold                                           |
| MSM          | Prepaid Maestro Consumer Promotion Card                        |
| MSN          | Prepaid Maestro Insurance Card                                 |
| MSO          | Prepaid Maestro Other Card                                     |
| MSQ          | Reserved for Future Use                                        |
| MSR          | Prepaid Maestro Travel Card                                    |
| MST          | Prepaid Maestro Teen Card                                      |
| MSV          | Prepaid Maestro Government Benefit Card                        |
| MSW          | Prepaid Maestro Corporate Card                                 |
| MSX          | Prepaid Maestro Flex Benefit Card                              |
| MSY          | Prepaid Maestro Employee Incentive Card                        |
| MSZ          | Prepaid Maestro Emergency Assistance Card                      |
| MTA          | Mastercard B2B Product 7                                       |
| MTB          | Mastercard B2B Product 8                                       |
| MTC          | Mastercard B2B Product 9                                       |
| MTD          | Mastercard B2B Product 10                                      |
| MTE          | Mastercard B2B Product 11                                      |
| MTF          | Mastercard B2B Product 12                                      |
| MTG          | Mastercard B2B Product 13                                      |
| MTH          | Mastercard B2B Product 14                                      |
| MTI          | Mastercard B2B Product 15                                      |
| MTJ          | Mastercard B2B Product 16                                      |
| MTK          | Mastercard B2B Product 17                                      |
| MTL          | Mastercard B2B Product 18                                      |
| MTM          | Mastercard B2B Product 19                                      |
| MTN          | Mastercard B2B Product 20                                      |
| MTO          | Mastercard B2B Product 21                                      |
| MTQ          | Mastercard B2B Product 22                                      |
| MTR          | Mastercard B2B Product 23                                      |
| MTS          | Mastercard B2B Product 24                                      |
| MTT          | Mastercard B2B Product 25                                      |
| MTU          | Mastercard B2B Product 26                                      |
| MTV          | Mastercard B2B Product 27                                      |
| MTW          | Mastercard B2B Product 39                                      |
| MTX          | Mastercard B2B Product 40                                      |
| MTY          | Mastercard B2B Product 41                                      |
| MTZ          | Mastercard B2B Product 42                                      |
| MTP          | Mastercard Platinum Prepaid Travel (UK and Brazil)             |
| MUS          | Prepaid Unembossed Mastercard Card                             |
| MUW          | Mastercard World Domestic Affluent                             |
| MVA          | Mastercard B2B VIP 1                                           |
| MVB          | Mastercard B2B VIP 2                                           |
| MVC          | Mastercard B2B VIP 3                                           |
| MVD          | Mastercard B2B VIP 4                                           |
| MVE          | Mastercard B2B VIP 5                                           |
| MVF          | Mastercard B2B VIP 6                                           |
| MVG          | Mastercard B2B VIP 7                                           |
| MVH          | Mastercard B2B VIP 8                                           |
| MVI          | Mastercard B2B VIP 9                                           |
| MVJ          | Mastercard B2B VIP 10                                          |
| MVK          | Mastercard B2B VIP 11                                          |
| MVL          | Mastercard B2B VIP 12                                          |
| MVM          | Mastercard B2B VIP 13                                          |
| MVN          | Mastercard B2B VIP 14                                          |
| MVO          | Mastercard B2B VIP 15                                          |
| MVP          | Mastercard B2B VIP 16                                          |
| MVQ          | Mastercard B2B VIP 17                                          |
| MVR          | Mastercard B2B VIP 18                                          |
| MVS          | Mastercard B2B VIP 19                                          |
| MVT          | Mastercard B2B VIP 20                                          |
| MVU          | Mastercard B2B VIP 21                                          |
| MVV          | Mastercard B2B VIP 22                                          |
| MVW          | Mastercard B2B VIP 23                                          |
| MVX          | Mastercard B2B VIP 24                                          |
| MVY          | Mastercard B2B VIP 25                                          |
| MVZ          | Mastercard B2B VIP 26                                          |
| MWA          | Mastercard B2B Product 43                                      |
| MWB          | World Elite Mastercard Business Card                           |
| MWC          | Mastercard B2B Product 44                                      |
| MWD          | Mastercard B2B Product 45                                      |
| MWE          | World Elite Mastercard Card                                    |
| MWF          | Mastercard Humanitarian Prepaid                                |
| MWG          | Mastercard B2B Product 46                                      |
| MWH          | Mastercard B2B Product 47                                      |
| MWJ          | Mastercard World Legend                                        |
| MWK          | Mastercard Consumer Plus                                       |
| MWL          | Mastercard Consumer Plus Flex                                  |
| MWO          | World Elite Mastercard Corporate Card                          |
| MWP          | World Prepaid                                                  |
| MWR          | World Retailer Centric Payments                                |
| MXG          | Gold Debit Mastercard Card                                     |
| MXP          | Digital Enablement Program                                     |
| OLB          | Maestro Small Business Delayed Debit                           |
| OLG          | Maestro Gold Delayed Debit                                     |
| OLP          | Maestro Platinum Delayed Debit                                 |
| OLS          | Maestro Delayed Debit                                          |
| OLW          | World Maestro Delayed Debit                                    |
| PVA          | Private Label A                                                |
| PVB          | Private Label B                                                |
| PVC          | Private Label C                                                |
| PVD          | Private Label D                                                |
| PVE          | Private Label E                                                |
| PVF          | Private Label F                                                |
| PVG          | Private Label G                                                |
| PVH          | Private Label H                                                |
| PVI          | Private Label I                                                |
| PVJ          | Private Label J                                                |
| PVL          | Private Label L                                                |
| PVT          | Private Label T                                                |
| SAG          | Gold Mastercard Salary Immediate Debit                         |
| SAL          | Standard Maestro Salary                                        |
| SAP          | Platinum Mastercard Salary Immediate Debit                     |
| SAS          | Standard Mastercard Salary Immediate Debit                     |
| SBJ          | Prepaid Installment Payments H                                 |
| SBK          | Prepaid Installment Payments I                                 |
| SBP          | Small Business Prepaid                                         |
| SOL          | UK Domestic Solo brand                                         |
| SPP          | Mastercard Installment Payments P                              |
| SPS          | Mastercard Installment Payments S                              |
| SOS          | Standard Mastercard Salary Immediate Debit                     |
| SWI          | UK Domestic Switch brand                                       |
| SUR          | Prepaid Unembossed Mastercard Card (Non-US)                    |
| TBE          | Mastercard Electronic Business Immediate Debit                 |
| TCB          | Mastercard Corporate Immediate Debit                           |
| TCC          | Mastercard (mixed BIN) Immediate Debit                         |
| TCE          | Mastercard Electronic Immediate Debit                          |
| TCF          | Mastercard Fleet Card Immediate Debit                          |
| TCG          | Gold Mastercard Card Immediate Debit                           |
| TCM          | Mastercard Titanium II                                         |
| TCO          | Mastercard Corporate Immediate Debit                           |
| TCP          | Mastercard Purchasing Card Immediate Debit                     |
| TCS          | Mastercard Standard Card Immediate Debit                       |
| TCW          | World Signia Immediate Debit                                   |
| TEB          | Mastercard Executive BusinessCard Card                         |
| TEC          | Mastercard Electronic Commercial Immediate Debit               |
| TEO          | Mastercard Corporate Executive Card Immediate Debit            |
| TNF          | Mastercard Public Sector Commercial Card Immediate Debit       |
| TNW          | Mastercard New World Immediate Debit                           |
| TPB          | Mastercard Preferred Business Card Immediate Debit             |
| TPM          | Mastercard Titanium Prepaid                                    |
| TPL          | Platinum Mastercard Immediate Debit                            |
| TWB          | World Mastercard Black Edition Immediate Debit                 |
| WAA          | MasterCard Commercial B2B Product 1                            |
| WAB          | MasterCard Commercial B2B Product 2                            |
| WAC          | MasterCard Commercial B2B Product 3                            |
| WAD          | MasterCard Commercial B2B Product 4                            |
| WAE          | MasterCard Commercial B2B Product 5                            |
| WAF          | MasterCard Commercial B2B Product 6                            |
| WAG          | MasterCard Commercial B2B Product 7                            |
| WAH          | MasterCard Commercial B2B Product 8                            |
| WAI          | MasterCard Commercial B2B Product 9                            |
| WAJ          | MasterCard Commercial B2B Product 10                           |
| WAK          | MasterCard Commercial B2B Product 11                           |
| WAL          | MasterCard Commercial B2B Product 12                           |
| WAM          | MasterCard Commercial B2B Product 13                           |
| WAN          | MasterCard Commercial B2B Product 14                           |
| WAO          | MasterCard Commercial B2B Product 15                           |
| WAP          | MasterCard Commercial B2B Product 16                           |
| WAQ          | MasterCard Commercial B2B Product 17                           |
| WAT          | MasterCard Commercial B2B Product 18                           |
| WAU          | MasterCard Commercial B2B Product 19                           |
| WAV          | MasterCard Commercial B2B Product 20                           |
| WAW          | MasterCard Commercial B2B Product 21                           |
| WAX          | MasterCard Commercial B2B Product 22                           |
| WAY          | MasterCard Commercial B2B Product 23                           |
| WAZ          | MasterCard Commercial B2B Product 24                           |
| WBA          | MasterCard Commercial B2B Product 25                           |
| WBB          | MasterCard Commercial B2B Product 26                           |
| WBC          | MasterCard Commercial B2B Product 27                           |
| WBD          | MasterCard Commercial B2B Product 28                           |
| WBF          | MasterCard Commercial B2B Product 29                           |
| WBG          | MasterCard Commercial B2B Product 30                           |
| WBH          | MasterCard Commercial B2B Product 31                           |
| WBI          | MasterCard Commercial B2B Product 32                           |
| WBJ          | MasterCard Commercial B2B Product 33                           |
| WBK          | MasterCard Commercial B2B Product 34                           |
| WBL          | MasterCard Commercial B2B Product 35                           |
| WBE          | World Mastercard Black Edition                                 |
| WPD          | World Prepaid Debit                                            |

## Testing

While you’re testing, use the following test cards to simulate purchases made with specific card product codes, which are returned in the `brand_product` field. Each test card takes any future date as the expiration, any three-digit value as the CVV, and any postal code.

#### Card numbers

| Description                                | Number           | Product code |
| ------------------------------------------ | ---------------- | ------------ |
| Mastercard Standard Debit                  | 5555050360000007 | MDS          |
| Mastercard Platinum Debit                  | 5555050360000015 | MDP          |
| Mastercard World Credit                    | 5200000360000076 | MCW          |
| Mastercard World Elite Credit              | 5200000360000068 | MWE          |
| Mastercard World Elite for Business Credit | 5200500000100004 | MAB          |

#### PaymentMethods

| Description                                | Number                                                                | Product code |
| ------------------------------------------ | --------------------------------------------------------------------- | ------------ |
| Mastercard Standard Debit                  | `pm_card_mastercard_au_debit_mastercardStandardDebitProductCode`      | MDS          |
| Mastercard Platinum Debit                  | `pm_card_mastercard_au_debit_mastercardPlatinumDebitProductCode`      | MDP          |
| Mastercard World Credit                    | `pm_card_mastercard_au_mastercardWorldCreditProductCode`              | MCW          |
| Mastercard World Elite Credit              | `pm_card_mastercard_au_mastercardWorldEliteCreditProductCode`         | MWE          |
| Mastercard World Elite for Business Credit | `pm_card_mastercard_au_mastercardWorldEliteBusinessCreditProductCode` | MAB          |
