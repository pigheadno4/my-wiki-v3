---
title: Google Pay test card suite
slug: /docs/checkout/apm/test-cards/google-pay/
createTime: "2024-08-15T08:01:01.674Z"
updateTime: "2025-05-09T16:01:35.054Z"
---

# Google Pay test card suite

Test Google Pay card payments in an [Expanded Checkout](/docs/checkout/advanced/) integration using test card numbers.

Visit the [Card testing](/tools/sandbox/card-testing/) page for more information about testing.

**Tip:** Enter any future expiration date and any 3-digit CVV, or 4-digit CVV for American Express, to proceed.

## Successful scenarios

Use the test cards in the following tables to test successful payments using Google Pay:

### Cards by country and brand

| Issuing country | Card band        | Card number      |
| --------------- | ---------------- | ---------------- |
| US              | American Express | 431719448528954  |
| CA              | American Express | 345383818559761  |
| GB              | American Express | 989888724064749  |
| IT              | American Express | 342825837040184  |
| FR              | American Express | 308201374214461  |
| FR              | Cartes Bancaire  | 4360000001000005 |
| US              | Discover         | 6504843087456605 |
| US              | Mastercard       | 5413291068719504 |
| CA              | Mastercard       | 5350364446374865 |
| GB              | Mastercard       | 5330400000646077 |
| IT              | Mastercard       | 5317626620232578 |
| FR              | Mastercard       | 5131015074177287 |
| US              | Visa             | 4566201562849481 |
| CA              | Visa             | 4551211304930496 |
| GB              | Visa             | 4698461667090156 |
| IT              | Visa             | 4951749275359506 |
| FR              | Visa             | 4820201095803320 |

### Step-up authentication success: 3D Secure cards by country and brand

| Issuing country | Card band        | Type of auth                     | Card number      |
| --------------- | ---------------- | -------------------------------- | ---------------- |
| US              | Visa             | 3D Secure step-up authentication | 4653041108355344 |
| US              | Mastercard       | 3D Secure step-up authentication | 5147552104214336 |
| US              | American Express | 3D Secure step-up authentication | 378678310596793  |
| CA              | Visa             | 3D Secure step-up authentication | 4536041103779848 |
| CA              | Mastercard       | 3D Secure step-up authentication | 4500022107836596 |
| CA              | American Express | 3D Secure step-up authentication | 373380310297697  |
| GB              | Visa             | 3D Secure step-up authentication | 4832061100371226 |
| GB              | Mastercard       | 3D Secure step-up authentication | 5330402102195045 |
| GB              | American Express | 3D Secure step-up authentication | 374259310290598  |
| IT              | Visa             | 3D Secure step-up authentication | 4877181102050176 |
| IT              | Mastercard       | 3D Secure step-up authentication | 5331462108067555 |
| IT              | American Express | 3D Secure step-up authentication | 375255310069395  |
| FR              | Visa             | 3D Secure step-up authentication | 4973971109225018 |
| FR              | Mastercard       | 3D Secure step-up authentication | 5130372106022002 |
| FR              | American Express | 3D Secure step-up authentication | 374982310011116  |

### 3D Secure Frictionless success

| Issuing country | Card band       | Type of auth                | Card number      |
| --------------- | --------------- | --------------------------- | ---------------- |
| FR              | Cartes Bancaire | Frictionless authentication | 4979498016380375 |

## Unsuccessful scenarios

Use the test cards in the following table to test unsuccessful payments using Google Pay:

### 3D Secure failure: cards by failure type

| Issuing country | Card band | Type of auth                     | Card number      |
| --------------- | --------- | -------------------------------- | ---------------- |
| US              | Visa      | 3D Secure step-up authentication | 4653041116908548 |
| US              | Visa      | 3D Secure step-up authentication | 4653041127085534 |
| US              | Visa      | 3D Secure step-up authentication | 4653041133398285 |
| US              | Visa      | 3D Secure step-up authentication | 4653041149505584 |
| US              | Visa      | 3D Secure step-up authentication | 4653041158020079 |
