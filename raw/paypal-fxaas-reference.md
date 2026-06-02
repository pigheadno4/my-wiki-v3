<!-- Source URL: https://developer.paypal.com/docs/checkout/fx-as-a-service/reference/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Reference
slug: /docs/checkout/fx-as-a-service/reference/
createTime: '2025-05-15T01:29:52.612Z'
updateTime: '2026-01-09T14:50:05.831Z'
---

# Reference

## Quote (presentment) currency codes

These are the possible `quote_currency` values for the Currency Exchange v2 API (`/v2/pricing/quote-exchange-rates`). ~100+ currencies.

Selected zero-digit currencies (no decimal places): BIF, XAF, XPF, CLP, COP, KMF, CRC, DJF, GNF, ISK, PYG, KRW, VND.

Full table (ISO-4217):

| Currency | Code | Notes |
| -------- | ---- | ----- |
| Afghan Afghani | AFN | |
| Albanian Lek | ALL | |
| Algerian Dinar | DZD | |
| Angolan Kwanza | AOA | |
| Armenian Dram | AMD | |
| Aruban Florin | AWG | |
| Azerbaijani Manat | AZN | |
| Bahamian Dollar | BSD | |
| Bangladeshi Taka | BDT | |
| Barbadian Dollar | BBD | |
| Belize Dollar | BZD | |
| Bermudian Dollar | BMD | |
| Bhutanese Ngultrum | BTN | |
| Bolivian Boliviano | BOB | |
| Bosnia and Herzegovina Convertible Mark | BAM | |
| Botswana Pula | BWP | |
| Burundian Franc | BIF | Zero-digit |
| Brunei Dollar | BND | |
| Cambodian Riel | KHR | |
| Cape Verdean Escudo | CVE | |
| Cayman Islands Dollar | KYD | |
| Central African CFA Franc | XAF | Zero-digit |
| CFP Franc | XPF | Zero-digit |
| Chilean Peso | CLP | Zero-digit |
| Colombian Peso | COP | Zero-digit |
| Comorian Franc | KMF | Zero-digit |
| Congolese Franc | CDF | |
| Costa Rican Colón | CRC | Zero-digit |
| Djiboutian Franc | DJF | Zero-digit |
| Dominican Republic Peso | DOP | |
| East Caribbean Dollar | XCD | |
| Egyptian Pound | EGP | |
| Eritrean Nakfa | ERN | |
| Ethiopian Birr | ETB | |
| Falkland Pound | FKP | |
| Fijian Dollar | FJD | |
| Gambian Dalasi | GMD | |
| Georgian Lari | GEL | |
| Ghanaian Cedi | GHS | |
| Gibraltar Pound | GIP | |
| Guatemalan Quetzal | GTQ | |
| Guinean Franc | GNF | Zero-digit |
| Guyanese Dollar | GYD | |
| Haitian Gourde | HTG | |
| Honduran Lempira | HNL | |
| Icelandic Króna | ISK | Zero-digit |
| Indonesian Rupiah | IDR | |
| Jamaican Dollar | JMD | |
| Kazakhstani Tenge | KZT | |
| Kenyan Shilling | KES | |
| Kyrgyzstani Som | KGS | |
| Lao Kip | LAK | |
| Lesotho Loti | LSL | |
| Liberian Dollar | LRD | |
| Macanese Pataca | MOP | |
| Macedonian Denar | MKD | |
| Malagasy Ariary | MGA | 2-decimal but must be multiples of 0.20; auto-rounded |
| Malawian Kwacha | MWK | |
| Maldivian Rufiyaa | MVR | |
| Mauritanian Ouguiya | MRU | |
| Mauritian Rupee | MUR | |
| Mongolian Tögrög | MNT | |
| Moldovian Leu | MDL | |
| Moroccan Dirham | MAD | |
| Mozambican Metical | MZN | |
| Namibian Dollar | NAD | |
| Nepalese Rupee | NPR | |
| Netherlands Antilles Guilder | ANG | |
| Nicaraguan Córdoba | NIO | |
| Nigerian Naira | NGN | |
| Pakistani Rupee | PKR | |
| Panamanian Balboa | PAB | |
| Papua New Guinean Kina | PGK | |
| Paraguayan Guaraní | PYG | Zero-digit |
| Peruvian Nuevo Sol | PEN | |
| Qatari Riyal | QAR | |
| Romanian Leu | RON | |
| Rwandan Franc | RWF | |
| Saint Helenian Pound | SHP | |
| Salvadoran Colon | SVC | |
| Samoan Tala | WST | |
| São Toméan Dobra | STN | |
| Saudi Riyal | SAR | |
| Serbian Dinar | RSD | |
| Seychellois Rupee | SCR | |
| Sierra Leonean Leone | SLE | |
| Solomon Islands Dollar | SBD | |
| Somali Shilling | SOS | |
| South African Rand | ZAR | |
| South Korean Won | KRW | Zero-digit |
| Sri Lankan Rupee | LKR | |
| Surinamese Dollar | SRD | |
| Swazi Lilangeni | SZL | |
| Tajikistani Sonomi | TJS | |
| Tanzanian Shilling | TZS | |
| Tongan Paʻanga | TOP | |
| Trinidad and Tobago Dollar | TTD | |
| Turkmenistani Manat | TMT | |
| Ugandan Shilling | UGX | |
| Ukrainian Hryvnia | UAH | |
| United Arab Emirates Dirham | AED | |
| Uruguayan Peso | UYU | |
| Uzbekistani Som | UZS | |
| Vanuatu Vatu | VUV | |
| Venezuelan Bolivar | VES | |
| Vietnamese Đồng | VND | Zero-digit |
| West African CFA Franc | XOF | |
| Yemeni Rial | YER | |
| Zambian Kwacha | ZMW | |

**BGN (Bulgarian Lev) deprecated**: Effective January 1, 2026, Bulgaria joined the Euro area. BGN is no longer supported. Use EUR for all Bulgaria transactions.

**MGA (Malagasy Ariary) special format**: 2-decimal format but amounts must be in multiples of 0.20. Auto-rounded: MGA 101.10 → 101.20; MGA 101.09 → 101.00.

## Settlement currency codes

These are the possible `base_currency` values (holding currencies) for the Currency Exchange v2 API. 24 currencies.

| Currency | Code | Notes |
| -------- | ---- | ----- |
| Australian Dollar | AUD | |
| Brazilian Real | BRL | In-country only (see note) |
| Canadian Dollar | CAD | |
| Chinese Renminbi | CNY | In-country only (see note) |
| Czech Koruna | CZK | |
| Danish Krone | DKK | |
| Euro | EUR | |
| Hong Kong Dollar | HKD | |
| Hungarian Forint | HUF | Zero-digit |
| Israeli New Shekel | ILS | |
| Japanese Yen | JPY | Zero-digit |
| Malaysian Ringgit | MYR | In-country only (see note) |
| Mexican Peso | MXN | |
| New Taiwan Dollar | TWD | Zero-digit |
| New Zealand Dollar | NZD | |
| Norwegian Krone | NOK | |
| Philippine Peso | PHP | |
| Polish Złoty | PLN | |
| Pound Sterling | GBP | |
| Singapore Dollar | SGD | |
| Swedish Krona | SEK | |
| Swiss Franc | CHF | |
| Thai Baht | THB | |
| United States Dollar | USD | |

**In-country restriction (BRL, CNY, MYR)**: These currencies are supported as payment or settlement currencies only for in-country PayPal accounts. If the settlement account is based outside the country, PayPal auto-converts to the account's primary currency at the applicable conversion rate (including spread/fee).
