---
title: "Stripe — ACS SFTP Catalog Ingestion (Agent Side)"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-agentic-commerce-sftp-catalog-2026.md"
tags: [stripe, agentic-commerce, sftp, catalog, product-feed, agent, ingestion, manifest]
---

## Summary

Guide for AI agents to receive and ingest seller product catalogs delivered by Stripe to the agent's SFTP server. Covers SFTP setup, directory structure, hybrid feed model, sharding/manifest, CSV format, deletion rules, and ingestion best practices.

## SFTP Configuration

- Port 22, Ed25519 SSH key auth, password disabled
- `stripe-verification.txt` challenge token in SFTP root (must stay in place)
- Directory: `/[stripe_profile_id]/catalog/` (daily) + `/updates/` (hourly delta, opt-in)
- `merchant_metadata.json` per business directory

## Hybrid Feed Model

| Feed | Frequency | Content |
| --- | --- | --- |
| Product Master Feed | Daily | Stable metadata (descriptions, images, taxonomy) |
| Delta Feed (opt-in) | Hourly | Price, availability, inventory changes |

## Manifest Pattern

Files: `full_catalog_part_N_of_Total.csv.gz` (shards for > 100k rows). `manifest.json` uploaded last — wait for it before ingesting. Contains `batch_timestamp`, `feed_type`, `total_shards`, `files[]`.

## CSV Format

`.csv.gz` (gzip), UTF-8, header row, standard CSV quoting. Empty = unset. Multi-value fields (e.g., `additional_image_link`) comma-separated within a single quoted field.

## Deletion Rules

- **Explicit**: `delete=true` in row → remove product
- **Implicit**: product absent from latest full Product Master Feed → remove/mark inactive
- **Reappearance**: product returns in later full feed → active again (unless `delete=true`)

## Ingestion Rules

- **Idempotency**: reprocessing same batch must not create duplicates
- **Timestamp validation**: only update if incoming record is newer
- **Auditability**: retain log of processed `batch_timestamp` values

## Related Pages

- [[stripe-agentic-commerce-product-feed]] — concept page (updated with SFTP ingestion details)
- [[source-stripe-agentic-commerce-for-agents]] — agent integration guide (SFTP mentioned in onboarding)

## Raw Sources

- [[stripe-agentic-commerce-sftp-catalog-2026]] — verbatim SFTP catalog ingestion guide (215 lines)
