# Task 11 live PayPal JS collection report

Date: 2026-07-18
Repository: `paypal/paypal-js`
Scope: collection only; no packet approval or wiki ingest

## Preflight no-write proof

Before the required dry-run:

- `git status --porcelain=v1 --untracked-files=all`: clean.
- `raw/github/paypal/paypal-js/`: absent.
- `tracking/github/repos/paypal/paypal-js/`: absent.
- `tracking/github/runs/`: absent.
- Generated-state hashes:
  - `tracking/github/status.json`: `4094b567e26c3d66719cb3416eb59b4ead7394cc7f6cc18098706922e6140a24`
  - `tracking/github/collection-status.md`: `d861843d92eef4af45eaf14c36cdd137bf942052633d15b3eecd1cc4a0a7c4f9`
  - `tracking/github/ingest-status.md`: `324c1ddc06e9a9f4cf34438f365f6ab2ef3d4171032406a19cebb03436276db5`

The brief's initial command could not enumerate releases because the registry row had no version tracks. Complete output:

```text
error: release mode requires configured version tracks for paypal/paypal-js
```

Live ref discovery was then attempted with:

```text
git ls-remote --tags https://github.com/paypal/paypal-js.git
```

The sandbox-denied attempt failed exactly as follows, so the same user-authorized command was rerun with approved network access:

```text
fatal: unable to access 'https://github.com/paypal/paypal-js.git/': Could not resolve host: github.com
```

After adding only the three audited version tracks, the required dry-run was rerun. Complete output:

```text
dry-run paypal/paypal-js state=collected-baseline versions=10.0.0,10.1.0,10.1.1,10.1.2,9.0.0,9.0.2,9.1.1,9.2.0,9.3.0,8.5.0,8.6.0,8.7.0,8.8.3,8.9.2 packets=-
```

After the successful dry-run:

- `git status --porcelain=v1 --untracked-files=all`: only `tracking/github/repo-registry.toml` was modified by the deliberate selector update.
- `raw/github/paypal/paypal-js/`: still absent.
- `tracking/github/repos/paypal/paypal-js/`: still absent.
- `tracking/github/runs/`: still absent.
- All three generated-state hashes remained exactly unchanged.

This proves the dry-run itself made no raw, run, packet, or generated-status writes.

## Package namespace and wiki audit

Live refs contain separate scoped streams for `@paypal/paypal-js` and `@paypal/react-paypal-js`. The v8/v9 migration evidence in the existing wiki belongs specifically to `@paypal/react-paypal-js`, so the three tracks are:

- `package:@paypal/react-paypal-js@10`
- `package:@paypal/react-paypal-js@9`
- `package:@paypal/react-paypal-js@8`

The separate `@paypal/paypal-js` stream is intentionally not selected by these tracks. The exact wiki audit found:

- `wiki/sources/source-github-paypal-js.md`: repository-level source covering both packages, with the detailed saved package focused on `@paypal/paypal-js`; it does not name an exact npm package version.
- `wiki/sources/source-github-paypal-js-v6.md`: repository commit `ffee35f`, describing `@paypal/react-paypal-js` v9.x and the SDK-v6 source tree.
- `wiki/sources/source-github-react-paypal-js-v8.md`: `@paypal/react-paypal-js` v8.x source on `release/react-paypal-js-v8`, commit `a074daa`.
- `wiki/sources/source-paypal-react-paypal-js-readme.md`: exact `@paypal/react-paypal-js` v8.9.2 reference.
- `wiki/sources/source-npm-react-paypal-js-v9.md`: exact `@paypal/react-paypal-js` v9.1.1 reference and the documented v8-to-v9 breaking migration boundary.

The migration changes from the v8 JS-SDK-v5 API (`PayPalScriptProvider`, `PayPalButtons`, and root-package imports) to the v9 JS-SDK-v6 API (`PayPalProvider`, payment button/session APIs, and `/sdk-v6` imports). Therefore `8.9.2` and `9.1.1` are retained as sorted exact pins in their respective tracks. There is no exact v10 wiki reference, so v10 has no pin.

## Pre-collection selected and excluded versions

Policy for all tracks: `future = "all-stable"` and `include_prerelease = false`.

- v10 `all-stable`, selected: `10.0.0`, `10.1.0`, `10.1.1`, `10.1.2`.
- v9 `minor-baselines`, selected: `9.0.0` (major earliest), `9.0.2` (latest 9.0), `9.1.1` (latest 9.1 and wiki pin), `9.2.0` (latest 9.2), `9.3.0` (latest 9.3 and major latest).
- v8 `minor-baselines`, selected: `8.5.0` (major earliest/latest 8.5), `8.6.0` (latest 8.6), `8.7.0` (latest 8.7), `8.8.3` (latest 8.8), `8.9.2` (latest 8.9, major latest, and wiki pin).
- Excluded stable v9 patch releases: `9.0.1`, `9.1.0`.
- Excluded stable v8 patch releases: `8.8.1`, `8.8.2`, `8.9.0`, `8.9.1`.
- Excluded matching prereleases: none exist in the live v8/v9/v10 `@paypal/react-paypal-js` refs; policy would exclude any future prerelease.

The selected set is the deterministic union required by the configured all-stable and minor-baseline policies, including exact audit pins.

## Collection results

The live commands completed with these exact terminal summaries:

```text
paypal/paypal-js state=collected-change versions=10.0.0,10.1.0,10.1.1,10.1.2,9.0.0,9.0.2,9.1.1,9.2.0,9.3.0,8.5.0,8.6.0,8.7.0,8.8.3,8.9.2 packets=<14 packet IDs printed by the collector>
paypal/paypal-js state=collected-baseline versions=main packets=baseline-main-508ee02108e35755589d259dc1363d64933a5e2abc1445e181d4085ff24ea530
```

Run manifests:

- `tracking/github/runs/20260717T170936088370Z-paypal-paypal-js-b2f43bfce9df481f8de2d52896be5a51.jsonl`: 14 selected events and 14 successful release terminals (3 `collected-baseline`, 11 `collected-change`).
- `tracking/github/runs/20260717T171230463363Z-paypal-paypal-js-1ae1b83d8dc64616ae849402e90cde76.jsonl`: one selected event and one `collected-baseline` terminal for `main` at `d5c5074bd37903e5108c956a08696dfd7b1173e9`.

Every release terminal names the exact `@paypal/react-paypal-js` tag, version, full commit SHA, and one packet. There are 14 release packets plus one independent default-branch packet; all 15 state histories contain only their initial `awaiting-review` event.

### Snapshot and release-evidence sizes

`saved bytes` is the exact sum of the manifest-declared upstream files. `notes bytes` is the exact GitHub release-note evidence size. The validator checked every declared SHA-256, size, and local path.

| Snapshot | Saved files | Saved bytes | Notes bytes | Exclusions |
| --- | ---: | ---: | ---: | ---: |
| `10.0.0-4bd05ab` | 12 | 187,683 | 794 | 0 |
| `10.1.0-59cb2ce` | 13 | 214,062 | 3,387 | 0 |
| `10.1.1-3d72ac9` | 14 | 209,055 | 476 | 3 |
| `10.1.2-3caece5` | 13 | 209,015 | 469 | 0 |
| `9.0.0-007a8d9` | 13 | 135,162 | 5,276 | 0 |
| `9.0.2-6944ab9` | 13 | 150,138 | 327 | 16 |
| `9.1.1-561eef1` | 13 | 145,845 | 274 | 0 |
| `9.2.0-9c3e71d` | 23 | 161,100 | 998 | 2 |
| `9.3.0-31eb658` | 15 | 192,720 | 1,084 | 0 |
| `8.5.0-a2140bb` | 10 | 76,565 | 448 | 0 |
| `8.6.0-5bd68be` | 11 | 78,133 | 596 | 2 |
| `8.7.0-40420ef` | 10 | 77,678 | 166 | 0 |
| `8.8.3-a2e716e` | 11 | 79,592 | 342 | 0 |
| `8.9.2-77487d6` | 11 | 82,919 | 299 | 0 |
| `main-d5c5074` | 13 | 209,015 | 0 | 0 |

Totals: 195 saved upstream files / 2,208,682 bytes, 14 release-note files / 14,936 bytes, and 2,338,085 physical bytes under the raw repository namespace including manifests. Every release has GitHub release notes plus both `packages/paypal-js/CHANGELOG.md` and `packages/react-paypal-js/CHANGELOG.md`; `main` has both changelogs and correctly has no release notes.

Every retained `packages/react-paypal-js/package.json` was parsed and matched both package name `@paypal/react-paypal-js` and the indexed version exactly.

### Same-commit package companions

No two selected React releases share a commit, so each selected release has its own canonical snapshot. Live refs showed these unselected `@paypal/paypal-js` release identities at the same commits:

- React `10.0.0`, `10.1.0`, `10.1.1`, `10.1.2` share commits with paypal-js `10.0.0`, `10.0.1`, `10.0.2`, `10.0.3` respectively.
- React `9.0.2`, `9.1.1`, `9.2.0`, `9.3.0` share commits with paypal-js `9.4.1`, `9.6.0`, `9.7.0`, `9.8.0` respectively.
- React `8.6.0`, `8.7.0`, `8.9.2` share commits with paypal-js `8.1.1`, `8.1.2`, `9.0.0` respectively.
- React `8.5.0`, `8.8.3`, and `9.0.0` have no same-commit paypal-js tag in the live ref set.

These are distinct package-scoped release identities, not aliases of the selected semantic releases. They were not indexed or packetized because the registry deliberately selects the React package stream. The selected snapshots' alias arrays therefore contain only their exact React tag.

### Required-reading sizes

All exact required-reading paths are retained in each packet's `packet.json` and rendered `ingest-packet.md`. Release baselines contain the snapshot manifest, release notes, and two changelogs; the main baseline contains its snapshot manifest and two changelogs. Delta packets add both endpoints and the changed public files.

| Packet endpoint | Files | Bytes |
| --- | ---: | ---: |
| `main` baseline | 3 | 63,625 |
| `10.0.0` baseline | 4 | 59,671 |
| `10.0.0 -> 10.1.0` | 13 | 242,169 |
| `10.1.0 -> 10.1.1` | 14 | 144,806 |
| `10.1.1 -> 10.1.2` | 12 | 140,523 |
| `9.0.0` baseline | 4 | 57,863 |
| `9.0.0 -> 9.0.2` | 18 | 215,476 |
| `9.0.2 -> 9.1.1` | 15 | 212,446 |
| `9.1.1 -> 9.2.0` | 28 | 228,584 |
| `9.2.0 -> 9.3.0` | 16 | 226,791 |
| `8.5.0` baseline | 4 | 40,592 |
| `8.5.0 -> 8.6.0` | 14 | 123,749 |
| `8.6.0 -> 8.7.0` | 10 | 91,528 |
| `8.7.0 -> 8.8.3` | 11 | 93,101 |
| `8.8.3 -> 8.9.2` | 12 | 107,622 |

The largest required-reading set is 242,169 bytes and the largest file count is 28. All are reasonably complete-readable, so no supplement or key-path change is required.

### Exclusions and repository findings

There are no registry policy or size-limit exclusions. The 23 manifest-recorded changed-path exclusions are:

- `10.1.1`: three paths marked `changed path could not be read safely` (`packages/react-paypal-js/.storybook/main.js`, `.storybook/preview.js`, and `src/stories/GettingStarted.stories.mdx`).
- `8.6.0`: two deleted/missing changed paths (`packages/react-paypal-js/.nvmrc` and `lint-staged.config.js`).
- `9.0.2`: 16 changed paths, consisting of deleted/missing configuration/scripts and package-local `.github` paths that could not be read safely; the exact paths and reasons are preserved in its `snapshot.md`.
- `9.2.0`: two deleted/missing changed paths (`.prettierrc.json` and `packages/react-paypal-js/src/v6/types/PayPalProviderEnums.ts`).

No submodule, Git LFS, or secret indicator appears in the retained evidence. The collector computes submodule/LFS capability flags during live inspection but does not persist them in run or snapshot metadata, so this result cannot be independently reconstructed from the committed artifacts. A separate filtered audit clone was attempted but denied because the approval system reported that its usage limit had been reached.

`gitleaks` is unavailable. A local heuristic scan of all retained raw files for private-key headers, AWS access-key IDs, GitHub tokens, Stripe-style secret keys, and assigned client secrets/access tokens found no candidate secret matches.

## Validation and concerns

- Baseline before collection: `python3 -m unittest discover -s tests` -> `Ran 304 tests in 14.875s`, `OK`.
- `python3 scripts/validate_github_collection.py` -> `validate_github_collection: OK (15 snapshots, 15 pending packets, no structural errors)`.
- `python3 scripts/collect_github_repos.py status` -> exit 0; regenerated `status.json`, `collection-status.md`, and `ingest-status.md`.
- Final full suite: `python3 -m unittest discover -s tests` -> `Ran 304 tests in 14.807s`, `OK`.
- `git diff --check` -> exit 0 with no output.
- Packet states: exactly 15 `awaiting-review`; none approved or ingested.

Exact concerns:

1. The brief's first dry-run cannot enumerate live package namespaces with an unconfigured row; it exits before network discovery. Namespace resolution required a separate live ref audit and then a second dry-run after the track-only registry edit.
2. Initial sandbox networking failed with `Could not resolve host: github.com`; approved live-network execution succeeded for ref discovery and both collection commands.
3. Submodule/LFS inspection flags are not persisted by the current collector. The later independent audit clone was denied due to the approval system usage limit, so the committed evidence supports only "no indicator in retained files," not a separately reproducible full-tree capability result.
4. Secret scanning was a documented local regex heuristic because `gitleaks` is not installed; it found no candidates.
5. Final staging and commit are blocked by worktree Git-index permissions. The normal `git add` failed with `Unable to create '/Users/tengtao/Development/wiki-v2/.git/worktrees/github-repository-collection/index.lock': Operation not permitted`. The required escalated retry was rejected because the approval system reported its usage limit was exhausted. No indirect workaround was attempted, no files were staged, and no commit was created.
