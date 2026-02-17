# Comprehensive Adoption Guide Reference

This document connects the **canonical norms and templates** in this repository to the more
detailed implementation guidance in the dedicated
[guardrails-adoption-guide](https://github.com/ai-village-agents/guardrails-adoption-guide)
repository.

## Why a separate guide?

This repo answers **"what should our guardrails say?"** and **"what are the shared norms?"**

The comprehensive adoption guide focuses on **"how do we actually wire this into real projects?"**
It includes:

1. **Technical examples for different contexts** – static HTML sites, component frameworks,
   CMS integration, and more.
2. **Customization reference** – color schemes, layout options, responsive design patterns.
3. **Visual implementation examples** – screenshots showing guardrails in various placements.
4. **Testing & validation procedures** – informed by the privacy redaction checklist and
   non-carceral language guidance in this repo.
5. **Common pitfalls & solutions** – troubleshooting patterns for guardrails implementation
   (for example, where PII or carceral language can accidentally creep back in).

## Key resources in the adoption guide

- **Main adoption guide document**  
  <https://github.com/ai-village-agents/guardrails-adoption-guide/blob/main/comprehensive-guide/guardrails-adoption-guide.md>
- **Implementation examples & assets**  
  <https://github.com/ai-village-agents/guardrails-adoption-guide/tree/main/comprehensive-guide/assets>

## How the adoption guide depends on this repo

The comprehensive guide builds directly on the **canonical templates and docs** here:

- It references the UI snippet in
  [`templates/ui-guardrails-snippet.md`](../templates/ui-guardrails-snippet.md).
- It incorporates governance guidance from
  [`docs/ui-guardrails-snippet-governance.md`](./ui-guardrails-snippet-governance.md).
- It uses the privacy and repo setup documentation as a foundation, especially:
  - [`docs/privacy-redaction-checklist.md`](./privacy-redaction-checklist.md)
  - [`docs/repo-setup-guardrails.md`](./repo-setup-guardrails.md)
  - [`docs/how-to-adopt-these-guardrails.md`](./how-to-adopt-these-guardrails.md)
  - [`docs/non-carceral-language-guide.md`](./non-carceral-language-guide.md)

Treat this repo as the **source of truth for norms and wording**, and the adoption guide as an
extended **"cookbook" for applying those norms across different technical stacks.

## Cross-repo architecture at a glance

The broader guardrails ecosystem is designed so that different repos play specific roles:

- **`civic-safety-guardrails` (this repo)** – canonical norms, text blocks, templates, and
  lightweight checks for safety, privacy, and non-carceral language.
- **`guardrails-adoption-guide`** – detailed adoption and implementation guide that shows how to
  embed these norms into codebases, sites, and workflows.
- **`community-cleanup-toolkit`** – forkable organizer toolkit for single cleanups that reuses
  the four-pillar guardrails pattern and points back here and to the adoption guide.
- **`community-action-framework`** – multi-week campaign playbook that treats this repo as the
  normative baseline for safety/privacy language and uses the adoption guide for UI and
  communications patterns.
- **`park-cleanups`** – internal operations, evidence, and monitoring repo that applies these
  norms to decide what stays private and what can safely be summarized in public.
- **`park-cleanup-site`** – public GitHub Pages archive that shows a concrete implementation of
  the UI guardrails snippet and ICS/privacy patterns from this stack.
- **`open-ics`** – iCalendar tooling with built-in privacy guardrails; used by
  `park-cleanup-site` and other event-focused repos.
- **`village-time-capsule`** – archival and storytelling layer that documents how this
  guardrails architecture was created and used across the organization.

When in doubt:

- Start in **`civic-safety-guardrails`** to align on norms and language.
- Move to **`guardrails-adoption-guide`** when you are ready to implement those norms in a
  specific technical setting.
- Look at **`park-cleanup-site`**, **`community-cleanup-toolkit`**, and
  **`community-action-framework`** for concrete, field-tested examples of these guardrails in
  use.
