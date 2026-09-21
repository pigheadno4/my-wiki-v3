<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/general/currencies -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Currencies
slug: /docs/reference/general/currencies/
createTime: '2025-04-01T23:01:23.361Z'
updateTime: '2026-01-09T17:46:31.013Z'
---



# Currencies

**NOTE**
The following currency types are supported in the Braintree API. Available currencies will differ depending on your account setup and the country your company is located in. [Restrictions that prohibit transactions from specific countries](/braintree/articles/risk-and-security/compliance/prohibited-transactions) may also be in place.    [Learn more about currencies and how to accept multiple currencies.](/braintree/articles/get-started/currencies)


- AED - United Arab Emirates Dirham
- AMD - Armenian Dram
- AOA - Angolan Kwanza
- ARS - Argentine Peso
- AUD - Australian Dollar
- AWG - Aruban Florin
- AZN - Azerbaijani Manat
- BAM - Bosnia and Herzegovina Convertible Mark
- BBD - Barbadian Dollar
- BDT - Bangladeshi Taka
- BIF - Burundian Franc*
- BMD - Bermudian Dollar
- BND - Brunei Dollar
- BOB - Bolivian Boliviano
- BRL - Brazilian Real
- BSD - Bahamian Dollar
- BWP - Botswana Pula
- BYN - Belarusian Ruble
- BZD - Belize Dollar
- CAD - Canadian Dollar[1](#scheme-currency)
- CHF - Swiss Franc1
- CLP - Chilean Peso*
- CNY - Chinese Renminbi Yuan
- COP - Colombian Peso
- CRC - Costa Rican Colón
- CVE - Cape Verdean Escudo
- CZK - Czech Koruna1
- DJF - Djiboutian Franc*
- DKK - Danish Krone1
- DOP - Dominican Peso
- DZD - Algerian Dinar
- EGP - Egyptian Pound
- ETB - Ethiopian Birr
- EUR - Euro1
- FJD - Fijian Dollar
- FKP - Falkland Pound
- GBP - British Pound1
- GEL - Georgian Lari
- GHS - Ghanaian Cedi
- GIP - Gibraltar Pound
- GMD - Gambian Dalasi
- GNF - Guinean Franc*
- GTQ - Guatemalan Quetzal
- GYD - Guyanese Dollar
- HKD - Hong Kong Dollar[1](#scheme-currency)
- HNL - Honduran Lempira
- HRK - Croatian Kuna[2](#exotic-currency)
- HTG - Haitian Gourde
- HUF - Hungarian Forint[2](#exotic-currency)
- IDR - Indonesian Rupiah
- ILS - Israeli New Sheqel
- INR - Indian Rupee
- ISK - Icelandic Króna*
- JMD - Jamaican Dollar
- JPY - Japanese Yen*[1](#scheme-currency)
- KES - Kenyan Shilling
- KGS - Kyrgyzstani Som
- KHR - Cambodian Riel
- KMF - Comorian Franc*
- KRW - South Korean Won*
- KYD - Cayman Islands Dollar
- KZT - Kazakhstani Tenge
- LAK - Lao Kip*
- LBP - Lebanese Lira
- LKR - Sri Lankan Rupee
- LRD - Liberian Dollar
- LSL - Lesotho Loti
- LTL - Lithuanian Litas
- MAD - Moroccan Dirham
- MDL - Moldovan Leu
- MKD - Macedonian Denar
- MNT - Mongolian Tögrög
- MOP - Macanese Pataca
- MUR - Mauritian Rupee
- MVR - Maldivian Rufiyaa
- MWK - Malawian Kwacha
- MXN - Mexican Peso
- MYR - Malaysian Ringgit
- MZN - Mozambican Metical
- NAD - Namibian Dollar
- NGN - Nigerian Naira
- NIO - Nicaraguan Córdoba
- NOK - Norwegian Krone1
- NPR - Nepalese Rupee
- NZD - New Zealand Dollar[1](#scheme-currency)
- PAB - Panamanian Balboa
- PEN - Peruvian Nuevo Sol
- PGK - Papua New Guinean Kina
- PHP - Philippine Peso
- PKR - Pakistani Rupee
- PLN - Polish Złoty
- PYG - Paraguayan Guaraní*
- QAR - Qatari Riyal
- RON - Romanian Leu[2](#exotic-currency)
- RSD - Serbian Dinar
- RUB - Russian Ruble
- RWF - Rwandan Franc*
- SAR - Saudi Riyal
- SBD - Solomon Islands Dollar
- SCR - Seychellois Rupee
- SEK - Swedish Krona[1](#scheme-currency)
- SGD - Singapore Dollar[2](#exotic-currency)
- SHP - Saint Helenian Pound
- SLL - Sierra Leonean Leone
- SOS - Somali Shilling
- SRD - Surinamese Dollar
- STD - São Tomé and Príncipe Dobra
- SVC - Salvadoran Colón
- SYP - Syrian Pound
- SZL - Swazi Lilangeni
- THB - Thai Baht
- TJS - Tajikistani Somoni
- TOP - Tongan Paʻanga
- TRY - Turkish Lira
- TTD - Trinidad and Tobago Dollar
- TWD - New Taiwan Dollar
- TZS - Tanzanian Shilling
- UAH - Ukrainian Hryvnia
- UGX - Ugandan Shilling*
- USD - United States Dollar[1](#scheme-currency)
- UYU - Uruguayan Peso
- UZS - Uzbekistani Som
- VES - Bolívar Soberano
- VND - Vietnamese Đồng*
- VUV - Vanuatu Vatu*
- WST - Samoan Tala
- XAF - Central African Cfa Franc*
- XCD - East Caribbean Dollar
- XOF - West African Cfa Franc*
- XPF - Cfp Franc*
- YER - Yemeni Rial
- ZAR - South African Rand[1](#scheme-currency)
- ZMK - Zambian Kwacha
- ZWD - Zimbabwean Dollar

*Zero-decimal currencies are marked with an asterisk.




**NOTE**
Effective January 1, 2026, Bulgaria is a member of the Euro area, and the Euro (EUR) replaces the domestic currency of the Bulgarian Lev (BGN). BGN is no longer supported for authorization or settlement. Use EUR for all transactions involving Bulgaria. If your integration currently uses BGN, update your code to use EUR immediately.




##### 1Scheme currency

Scheme currency means a currency made available by the Acquirer and/or card scheme(s) for settlement purposes.



- AED - United Arab Emirates Dirham
- CAD - Canadian Dollar
- CHF - Swiss Franc
- CZK - Czech Koruna
- DKK - Danish Krone
- EUR - Euro
- GBP - British Pound
- HKD - Hong Kong Dollar
- JPY - Japanese Yen
- NOK - Norwegian Krone
- NZD - New Zealand Dollar
- SEK - Swedish Krona
- USD - United States Dollar
- ZAR - South African Rand



##### 2Exotic currency

Exotic currency means a currency sourced by Braintree, which is not provided by the Acquirer and/or card scheme(s) for settlement purposes.



- HRK - Croatian Kuna2
- HUF - Hungarian Forint
- RON - Romanian Leu
- SGD - Singapore Dollar


