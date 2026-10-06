---
title: "Braintree Functions CLI Reference"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/functions/cli-reference"
raw_files:
  - "braintree/docs/guides/functions/cli-reference-2026-09-16.md"
tags: [braintree, functions, cli, developer-tools]
---

## Overview

This 2026-09-16 Braintree website snapshot is a CLI reference for the `@braintree/functions-cli` documentation preview. It routes installation and the `btfns` command surface for creating, listing, testing, packaging, publishing and deploying functions, plus account login and logout. The page is preview documentation, not evidence that Functions or a particular CLI release is currently available, that an account is eligible, or that any shown command completed successfully. It is also distinct from exact-version package or GitHub implementation evidence.

## Key takeaways

- The captured installation section says Node.js is required and specifically states that Node.js 8.x or 10.x is required. It documents either global npm installation, which makes the `btfns` namespace available from the command line, or invocation through `npx`. Treat those runtime versions as snapshot-scoped documentation, not current compatibility guidance.
- The command inventory covers function creation, help, account login/logout, listing functions/events/triggers, packaging and publishing, simulated invocation, test-data generation and deployment. `init` creates configuration and JavaScript files according to a selected template and can associate triggers or data-export events; its exact flags and allowed template values remain in the raw locator.
- Authentication and environment selection are consequential: `login` accepts environment, merchant ID and username options; `ls` can select an environment; and `deploy --production` is documented as targeting the production environment. The examples do not prove authentication, account authorization, deployment, publication, or environment availability.
- `test` is described as simulated invocation before deployment with a template-appropriate payload. `generate-test-data` writes a JSON file into the project's generated `__tests__` directory, while its output option controls the generated file name and path. These are documented command effects, not proof that a particular invocation succeeded.
- Global uninstall removes the CLI package, logout ends the documented Braintree account session, and init/test-data commands affect local project files. Confirm the intended account, environment and filesystem target before treating the reference as an operational runbook.

## Detail locators

- **Preview availability and installation:** raw lines 17–37 state the documentation-preview notice, Node.js prerequisite and captured 8.x/10.x requirement, global npm installation, resulting `btfns` namespace and `npx` alternative.
- **Uninstall and top-level version option:** raw lines 39–52 document global uninstall and `-v`/`--version`.
- **Command inventory:** raw lines 54–67 list deploy, help, init, login, logout, list, package, publish, test and test-data-generation purposes.
- **Deployment:** raw lines 70–84 show the deploy invocation and the production-environment flag.
- **Help and function creation:** raw lines 86–105 describe help, `init`, template types, and trigger/event options.
- **Account session controls:** raw lines 107–131 show login with environment and merchant selection, the username option and logout.
- **Account/environment inventory:** raw lines 133–149 describe listing functions deployed to the account and available triggers or events, including environment selection.
- **Packaging and publishing:** raw lines 152–180 document package/publish invocations and the publish version option.
- **Simulation:** raw lines 183–197 describe pre-deployment invocation simulation and the test-payload path.
- **Generated test files:** raw lines 200–214 describe JSON-file generation, the generated project directory and the output-path option.

## Related

- [[braintree]]
- [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/docs/guides/functions/cli-reference-2026-09-16|Braintree Functions CLI Reference (2026-09-16 snapshot)]]
