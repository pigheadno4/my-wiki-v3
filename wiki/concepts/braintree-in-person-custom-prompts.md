---
title: "Braintree In-Person Custom Prompts"
type: concept
category: technology
tags: [braintree, in-person, custom-prompts, graphql, card-reader]
---

## Braintree In-Person Custom Prompts

Braintree Custom Prompts are reader interactions outside payment collection. A caller starts a prompt-specific GraphQL mutation for multiple-choice, text, amount, signature or confirmation input, receives an in-store context ID, and polls that context for the result. The captured guide explicitly requires PayPal/Braintree Solutions Engineer or Integration Engineer enablement in both Sandbox and Production for multiple-choice, text and amount prompts; device, firmware and version qualifications vary by prompt. It does not establish current merchant enablement, reader compatibility or successful completion, and it does not state the same enablement requirement for signature or confirmation prompts.

## Sources

- [[source-braintree-in-person-guides-custom-prompts]] - unversioned Braintree website guide collected 2026-09-16 for reader prompt purpose, prompt/result families, enablement and hardware/version conditions, cancellation, offline exclusion and result-lifecycle boundaries
