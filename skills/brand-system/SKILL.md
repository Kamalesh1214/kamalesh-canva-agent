---
name: brand-system
description: Use to create, document, store, version, apply, and audit brand identities, brand guidelines, logos, color systems, and typography across multiple brands.
---

# Brand System

Build durable, reusable brand systems. Support multiple brands without cross-contamination.

## Brand discovery
Ask for brand/business name, industry, audience, offer, positioning, competitors/references, personality, use cases, required assets, and constraints. If the user gives only a name and industry, create a **Draft — Assumptions Included**, not a final identity. List each assumption and ask for review.

## Identity deliverables
A brand identity may include:
- Brand strategy summary and positioning.
- Logo directions and K-monogram or other mark concepts.
- Primary/secondary palette with HEX values and usage ratios.
- Typography roles and fallback choices.
- Graphic elements, icon/illustration direction, photography guidance.
- Voice and writing principles.
- Applications for social, web, and presentations.
- Later extensions: business cards, letterheads, stationery.
- Brand guidelines as an editable document plus PDF export when supported.

Do not claim that a logo is final until the user approves a direction. Do not use unlicensed or unavailable fonts/assets.

## Versioned brand profiles
Maintain one folder per brand and immutable version snapshots:
`brand-profiles/<brand-slug>/v1.0.0/brand-profile.json`
`brand-profiles/<brand-slug>/CHANGELOG.md`
`brand-profiles/<brand-slug>/current.json`

Use semantic versioning:
- MAJOR: positioning, core identity, primary mark, or core palette changes.
- MINOR: approved additions such as new templates, secondary colors, or new applications.
- PATCH: corrections and documentation clarifications that do not alter identity.

A profile should include: schema_version, brand_id, name, industry, status (draft/approved/archived), version, created_at, updated_at, positioning, audience, personality, voice, logo, colors, typography, graphic_language, photography, applications, accessibility, approvals, assumptions, and change_summary.

Never overwrite a prior version. Create a new version and changelog entry. `current.json` points to the approved current version. Ask before changing an approved identity.

## Multi-brand isolation
At task start, ask which brand profile applies if ambiguous. Load only that profile. Never blend colors, fonts, logo rules, or voice from another profile. Keep a per-project record of the brand_id and version used.

## Brand compliance audit
Classify findings:
- Critical: wrong logo/brand or severe misrepresentation.
- Major: primary palette/type/voice materially violated.
- Minor: inconsistent spacing, secondary color, or small application deviation.
- Note: optional refinement.

For every finding state location, rule, evidence, explanation, fix, and override status. Ask before overriding approved brand rules. A user-approved override is project-specific unless explicitly promoted to the permanent profile.
