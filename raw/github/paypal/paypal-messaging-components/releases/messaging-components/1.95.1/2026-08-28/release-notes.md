### [1.95.1](https://github.com/paypal/paypal-messaging-components/compare/v1.95.0...v1.95.1) (2026-08-25)


### Bug Fixes

* filter qualifying offers before sort, ensure aprDisclaimer.default always resolves, add getAPRDetails unit tests ([379cffd](https://github.com/paypal/paypal-messaging-components/commit/379cffd14cbda19d53a39823183825b29ba987d3))
* guard against null target window in modal sendEvent ([#1381](https://github.com/paypal/paypal-messaging-components/issues/1381)) ([9afde0a](https://github.com/paypal/paypal-messaging-components/commit/9afde0ad868f28adacb7bbd7f919ecbbf90e2006))
* make offer sort direction explicit with warning for unrecognized values ([b90b106](https://github.com/paypal/paypal-messaging-components/commit/b90b10637eb0f65287cdc569335f22ab356cfe54))
* replace long-term offer reversal with explicit per-country sort direction ([da83f73](https://github.com/paypal/paypal-messaging-components/commit/da83f735f788372b6b5efb21fa7ba6f7e3589595))
* validate total_payments as numeric before sorting offers ([02a5aec](https://github.com/paypal/paypal-messaging-components/commit/02a5aec3112fede9c98ea01df0269fb135dfe711))


### Tests

* update long-term offer expectations for sort order change ([4ce0011](https://github.com/paypal/paypal-messaging-components/commit/4ce0011247657fa0df4e4e294609503439951297))


### Code Refactoring

* simplify TermsTable offer sort and disclaimer lookup ([b4349f7](https://github.com/paypal/paypal-messaging-components/commit/b4349f7a54bf68ec2c9b78c8795ab1c94f5019cf))
* use numeric sort direction constants with validation instead of asc/desc strings ([debee7f](https://github.com/paypal/paypal-messaging-components/commit/debee7f2d7eca20fd6c4ca27d9ccb86bae6380fb))

