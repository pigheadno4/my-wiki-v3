---
title: "GitHub: Metronome-Industries/terraform-provider-metronome"
type: source
date_ingested: 2026-08-15
original_format: github-repo
raw_files:
  - "github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/manifest.json"
tags: [metronome, terraform, infrastructure-as-code, provider, experimental, github-repository]
---

## Overview

`Metronome-Industries/terraform-provider-metronome` is a Stainless-generated Terraform provider intended to connect Terraform to the Metronome REST API. This baseline covers prerelease `terraform-provider-metronome@0.1.0-alpha.3` at exact SHA `f06da6d6afee448e9fe9bad77d213cf6159d11f8`, released on 2026-06-01.

Repository: <https://github.com/Metronome-Industries/terraform-provider-metronome>

## Evidence Boundary

- The repository explicitly labels the provider experimental and says not to use it in production.
- At `0.1.0-alpha.3`, the implementation registers no Terraform resources and no data sources. Configuration and client construction do not establish that Terraform can manage any Metronome object.
- The provider is generated from an OpenAPI description by Stainless and depends on `metronome-go/v3@3.7.0`. Internal serializers, custom field helpers, validators, and generic release-note entries do not independently prove supported Metronome API or product behavior.
- The retained capsule excludes tests and fixtures under the approved policy. It proves the selected source and documentation at this exact release, not the complete upstream repository.
- The repository says it generally follows semantic versioning but permits some backward-incompatible minor releases. Prerelease consumers should not infer stable compatibility from the `0.1.0` prefix.

## Grounding Excerpts

> "This terraform provider is experimental. DO NOT use in production."
>
> `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/README.md:3-4`

> "This provider requires Terraform CLI 1.0 or later."
>
> `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/README.md:11-14`

> "The bearer_token field is required. Set it in provider configuration or via the \"METRONOME_BEARER_TOKEN\" environment variable."
>
> `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/internal/provider.go:81-85`

> `return []func() resource.Resource{}`
>
> `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/internal/provider.go:107-109`

> `return []func() datasource.DataSource{}`
>
> `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/internal/provider.go:111-113`

## Provider Configuration at `0.1.0-alpha.3`

The provider requires Terraform CLI 1.0 or later and declares Terraform protocol version 6.0. Its schema exposes three optional attributes: `base_url`, `bearer_token`, and `webhook_secret`. Although `bearer_token` is optional at schema level, configuration fails unless it is supplied directly or through `METRONOME_BEARER_TOKEN`.

`base_url` falls back to `METRONOME_BASE_URL`, and `webhook_secret` falls back to `METRONOME_WEBHOOK_SECRET`. The configured values are passed to a `metronome-go/v3` client and attached as both resource and data-source client data. The code does not mark token or secret attributes as sensitive in the retained schema, so repository guidance recommends environment variables for sensitive values.

The README's example pins `~> 0.1.0-alpha.3`, configures bearer token and webhook secret, and then leaves the resource example empty. The generated provider documentation likewise lists only provider attributes.

## Empty Management Surface

The decisive implementation boundary is in `internal/provider.go`: `Resources()` and `DataSources()` each return an empty slice. Therefore this release can initialize and construct an API client but exposes no resource or lookup block that a Terraform configuration can use to manage or read Metronome entities.

Release notes mention per-resource permission descriptions, data-source identifiers, dynamic values, patch serialization, and API updates. Those are generator or framework capabilities in this baseline; they must not be reported as usable Metronome Terraform resources when the exact provider registration lists remain empty.

## Runtime and Generation Shape

The Go module targets Go 1.25.8, uses Terraform Plugin Framework 1.19.0, and depends on `github.com/Metronome-Industries/metronome-go/v3` version `3.7.0`. The registry manifest declares protocol `6.0`.

Most retained source implements generic form/JSON encoding, dynamic custom-field handling, semantic validation, import-path parsing, logging, and type conversion. These internals may become infrastructure for future generated resources, but they do not expand the management surface at this version.

## Query Guidance

Use this source for exact questions about provider maturity, Terraform compatibility, configuration fields, environment-variable fallbacks, generation dependencies, and the resource/data-source surface at `0.1.0-alpha.3`. For update questions, also search [[changelog-github-terraform-provider-metronome]]. For Metronome REST operations or supported product behavior, use dedicated documentation and SDK sources rather than inferring capabilities from generic provider internals.

## Related

- Company: [[metronome]]
- Concept: [[metronome-integrations]]
- Server SDK evidence: [[source-github-metronome-node]]
- History: [[changelog-github-terraform-provider-metronome]]

## Raw Sources

- Snapshot manifest: `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/manifest.json`
- Release manifest: `raw/github/metronome/terraform-provider-metronome/releases/terraform-provider-metronome/0.1.0-alpha.3/2026-08-15/manifest.json`
- Release notes: `raw/github/metronome/terraform-provider-metronome/releases/terraform-provider-metronome/0.1.0-alpha.3/2026-08-15/release-notes.md`
- Repository README: `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/README.md`
- Provider implementation: `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/internal/provider.go`
- Generated provider documentation: `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/docs/index.md`
- Package dependencies: `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/go.mod`
- Terraform registry manifest: `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/terraform-registry-manifest.json`
- Repository changelog: `raw/github/metronome/terraform-provider-metronome/snapshots/2026-08-15-f06da6d/files/CHANGELOG.md`
