---
title: "GitHub: braintree/restricted-input"
type: source
date_ingested: 2026-08-30
original_format: github-repo
raw_files:
  - "github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/manifest.json"
  - "github/braintree/restricted-input/snapshots/2026-08-30-79053ef/manifest.json"
tags: [braintree, restricted-input, input-formatting, typescript, browser-compatibility, github-repository]
---

## Overview

`braintree/restricted-input` is a standalone browser utility that filters and formats `input` or `textarea` values from a declarative pattern. The retained current snapshot is default branch `main` at exact commit `8dcc6ea9e6cea44eef2b02fbc3f7569a602fa089`, whose package metadata identifies `restricted-input@4.2.0`.

The utility can support card-number presentation, but it is not a card-brand detector, validator, masking control, tokenizer, or payment SDK. It accepts characters, inserts separators, preserves selection state, and exposes the unformatted value; downstream code remains responsible for validation and payment handling.

Repository: <https://github.com/braintree/restricted-input>

## Evidence and Identity Boundary

- The repository is commit-tracked because its Git tags do not provide a reliable exact package-version history. The retained `8dcc6ea` source says `4.2.0`, but no package release record was collected, so this page does not claim npm publication from the snapshot alone.
- The historical comparison starts at exact commit `79053ef3a0843d2c68a167a4830159bb787f6fb1`, whose package metadata says `4.1.3`, and ends at `8dcc6ea`.
- The current 24-file capsule includes the complete non-test `src/` tree, README, changelog, package metadata, TypeScript configuration, root formatting-support entry point, and license. Tests, mocks, fixtures, generated `dist/`, lock data, and CI or development tooling are excluded.
- The published package entry points target generated `dist/` files, which are not retained. The TypeScript source is the implementation authority in this capsule, not proof of byte-for-byte packaged output.
- Browser classification is delegated to `@braintree/browser-detection@^2.1.1`; that dependency's implementation is outside this evidence.

## Grounding Excerpts

> "Allow restricted character sets in `input` elements."
>
> `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/README.md:6`

> "Disallow arbitrary characters based on patterns"
>
> `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/README.md:14`

> "Patterns are a mixture of [`Placeholder`](#placeholder)s and [`PermaChar`](#permachar)s."
>
> `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/README.md:96`

> "If an input is changed via a paste event, you may want to adjust the pattern before input formatting occurs."
>
> `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/README.md:131`

> `return !isSamsungBrowser();`
>
> `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/src/supports-input-formatting.ts:5`

## Pattern Model

A pattern is parsed into placeholders and permanent characters:

- An alphabetic placeholder accepts one ASCII letter through `/[A-Za-z]/`.
- A numeric placeholder accepts one ASCII digit through `/[0-9]/`.
- `*` accepts any single character through `/./`.
- Every non-placeholder character is a permanent character inserted into the formatted value.

For example, `{{9999}} {{9999}} {{9999}} {{9999}}` groups up to 16 accepted digits with spaces. The parser rejects placeholder characters outside the alpha, digit, and wildcard classes. The formatter scans input against the pattern, drops disallowed characters, inserts permanent characters, and adjusts the start and end selection positions as characters are removed or added.

`unformat()` removes permanent characters while preserving a corresponding selection range. `simulateDeletion()` converts backspace, forward-delete, or range deletion into an unformatted state before the value is formatted again.

## Public Construction and API

Construction requires:

| Option | Role |
| --- | --- |
| `element` | An `HTMLInputElement` or `HTMLTextAreaElement` to manage |
| `pattern` | The placeholder and permanent-character pattern |
| `onPasteEvent` | Optional callback receiving `unformattedInputValue` before final paste formatting |

The public class exposes:

- `getUnformattedValue()` to return the accepted value without permanent characters;
- `setPattern(pattern)` to unformat the current value, replace the formatter, and reformat a non-empty value; and
- static `supportsFormatting()` to report whether active formatting is enabled for the detected browser.

The paste callback can select a new pattern from the complete unformatted pasted value before reformatting. The README illustrates card-number grouping changes, but any brand inference used to choose a grouping is external to this package.

## Event and Selection Handling

The base strategy listens for keyboard, input, keyup, and paste events. It handles autofill and simulated events by marking the value unformatted, maintains selection around inserted separators, prevents duplicate paste insertion, invokes the optional paste callback, reformats the value, and dispatches an `input` event after paste.

Selection is changed only when the managed element is active and supports `setSelectionRange`. Keys that cannot mutate the value are ignored, including navigation keys and backspace or delete at the applicable boundary.

## Platform Strategies

The constructor chooses one strategy in this order: iOS, KitKat Chromium WebView, Android Chrome or ChromeOS, IE9, then the base strategy.

- iOS simulates deletion from selection state and includes special handling for autofill and an empty-input cursor issue.
- Android Chrome temporarily unformats on keydown, reformats on keyup and input, and uses delayed selection correction for keyboard behavior.
- KitKat Chromium WebView delays format and unformat operations because input values are unavailable in the relevant event loop.
- IE9 prevents the native key event, constructs the prospective value itself, and formats it before restoring selection.
- Detected Samsung browser cases return false from `supportsFormatting()` because the source notes that digits can be dropped.

> [!warning] Browser-support documentation conflict
> The README feature list says the utility "Works in IE11+", but its browser-support section lists IE9, IE10, and IE11, and the retained source contains a dedicated IE9 strategy. Treat the exact source as evidence that legacy paths exist, not proof that current merchant environments are officially supported or tested.

## `4.1.3` to `4.2.0` Transition

The selected source comparison changes 13 retained paths. The implementation changes are primarily TypeScript import modernization, formatting, lint annotations, and compiler configuration. The public constructor and three public methods remain unchanged in the retained source.

Package metadata changes the version from `4.1.3` to `4.2.0`, updates TypeScript and development tooling, replaces WebdriverIO integration-test commands with Playwright, and changes the runtime `@braintree/browser-detection` dependency from `^1.17.2` to `^2.1.1`. The repository changelog describes `4.1.4` as workflow fixes and `4.2.0` as test, Node 24, and dependency modernization.

No deliberate formatter behavior change is documented for `4.2.0`, but behavior delegated to the browser-detection major-version update cannot be proven unchanged from this repository alone. Tests are excluded, so the snapshot also does not prove cross-browser execution results.

## Historical Behavior in the Retained Changelog

The current changelog records several earlier behavior changes without separate exact-SHA snapshots:

- `4.0.3` fixes iOS Safari focus-time pattern changes and restores the public formatting-support method.
- `4.0.1` fixes Samsung-browser date input.
- `3.0.3` fixes duplicated Android Chrome paste input; `3.0.2` improves server-side rendering safety; and `3.0.0` adds TypeScript types while making private methods private.
- `2.1.0` adds the paste callback, while `2.0.1` avoids formatting an empty value when the pattern changes.
- `2.0.0` formats preset values on initialization and fixes iOS Chrome autofill behavior.
- The v1 history records fixes for autofill, Samsung and third-party keyboards, Android Chrome selection, iOS paste, legacy browser event behavior, and server-context loading.

These entries are historical statements from the retained changelog, not independently collected implementation snapshots.

## Related

- [[changelog-github-restricted-input]] - commit-qualified transition and retained package history
- [[payment-input-formatting]] - generic formatter, event, and validation boundaries
- [[card-brand-detection]] - separate brand inference used to select presentation metadata
- [[braintree-web-sdk]] - independently tracked browser payment SDK
- [[braintree]] - company and repository catalog

## Raw Sources

- Current snapshot manifest: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/manifest.json`
- Historical snapshot manifest: `raw/github/braintree/restricted-input/snapshots/2026-08-30-79053ef/manifest.json`
- Comparison: `tracking/github/repos/braintree/restricted-input/comparisons/default-branch/79053ef--8dcc6ea/comparison.json`
- Exact patch: `tracking/github/repos/braintree/restricted-input/comparisons/default-branch/79053ef--8dcc6ea/diff.patch`
- README: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/README.md`
- Repository changelog: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/CHANGELOG.md`
- Package metadata: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/package.json`
- Public class: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/src/lib/restricted-input.ts`
- Pattern parser: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/src/lib/formatter/parse-pattern.ts`
- Formatter: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/src/lib/formatter/index.ts`
- Base event strategy: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/src/lib/strategies/base.ts`
- Browser detection and support decision: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/src/lib/device.ts`
- Formatting support export: `raw/github/braintree/restricted-input/snapshots/2026-08-30-8dcc6ea/files/src/supports-input-formatting.ts`
