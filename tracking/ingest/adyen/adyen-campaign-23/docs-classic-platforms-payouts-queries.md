# C23 worker retrieval checks — docs-classic-platforms-payouts

## Q1: Which Classic payout modes exist and what gates their use?

The page covers payouts from a Classic account holder's funded account subject to their current **payout tier** and a **positive balance** (raw lines 19–23). Scheduled payouts have a per-account cadence, pay the full available balance and go to bank accounts only; manual payouts specify an amount, may be partial, and go to bank accounts or eligible cards (lines 25–26). The guide mentions standard regional rails and optional premium faster routes (lines 28–29). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-payouts]] → [[raw/adyen/docs/classic-platforms/payouts/2026-09-15]].

## Q2: What location/currency constraints or source conflicts affect a payout decision?

The page normally requires payout-method country to match account-holder country, with a European bank-account exception, and caps associated bank accounts at 200 (raw lines 31–35). Its dated rule says local-currency payouts, with EUR in SEPA non-eurozone countries and USD in Canada as exceptions (lines 37–44). It cites USD in the United States in prose (line 39), yet the table has no United States row (lines 46–80). The overview does not show any completed payout or receiving-bank credit. Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-payouts]] → [[raw/adyen/docs/classic-platforms/payouts/2026-09-15]].
