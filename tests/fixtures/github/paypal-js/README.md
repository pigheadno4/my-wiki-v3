# Offline PayPal JS release fixture

The test builds this fixture dynamically in a temporary Git repository. No
network request or workspace raw evidence is used.

Release sequence:

1. `@paypal/paypal-js@8.1.0` and `@paypal/react-paypal-js@8.9.2` share a SHA.
2. `@paypal/paypal-js@9.8.0` and `@paypal/react-paypal-js@9.3.0` share a SHA.
3. Both packages publish `10.0.0` at one SHA.
4. `@paypal/paypal-js@10.0.1` and `@paypal/react-paypal-js@10.1.0` share a SHA.
5. `@paypal/paypal-js@10.0.2` and `@paypal/react-paypal-js@10.1.1` share a SHA.

The expected ingest recommendations are full for package baselines and major
transitions, then delta for contained v10 patch and minor changes. A later
`@paypal/paypal-js@10.0.3` release is added after backfill to exercise failed
snapshot publication, explicit retry, and successful recovery.
