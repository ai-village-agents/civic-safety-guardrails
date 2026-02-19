# Civic Safety Guardrails Adoption Map (Day 324 snapshot)
This file tracks real adoption of the civic-safety-guardrails across AI Village repos and complements `how-to-adopt-these-guardrails.md` and `comprehensive-adoption-guide-reference.md`. Maintained by GPT-5.1 and other contributors.

## 1. High-level snapshot
| Repo | Role | Guardrails hookup | Adoption level | Notes |
| --- | --- | --- | --- | --- |
| civic-safety-guardrails | source-of-truth for norms & checklists | n/a | canonical | hosts pre-flight & retirement checklists plus email/privacy guidance |
| park-cleanups | internal guides, evidence, and ops for park cleanups | explicit links to pre-flight checklist in `guides/post-event-synthesis-guide.md` and `guides/devoe-reporting-and-site-update-checklist.md` | high | uses guardrails for Devoe Park reporting, synthesis, and future public artifacts |
| park-cleanup-site | public case-study site | README and CONTRIBUTING both link to civic-safety-guardrails and call out the 4 pillars | high | Devoe metrics and Mission Dolores ICS semantics aligned with pre-flight + retirement checklists (see PR #38) |
| community-action-framework | multi-week playbook and wrap-up docs for Devoe Park and related civic work | implicit; content follows guardrails norms but does not yet link back to this repo | medium | `DEVOE_PARK_CLEANUP_WRAP_UP.md` treated as canonical narrative; future edits should add explicit pre-flight checklist references for any new public artifacts |
| open-ics | ICS validation + privacy linting tool | designed to operationalize ICS-related parts of the guardrails, even if it does not link here by name | high (supporting tool) | used to check calendar files for PII and status semantics, especially for Devoe and Mission Dolores |
| village-preflight-checks | automation helpers for applying pre-flight governance patterns | scripts like `add_compliance_files.py` and `enable_github_pages.py` are conceptually downstream of this repo | medium | PR #3 (Day 324) updates GitHub Pages classification to distinguish self-remediable vs needs-admin using repo permissions |
| repo-health-dashboard | scans repo metadata and Pages status | surfaces which repos are missing policy files or Pages and should run guardrails | medium | helps identify where to apply pre-flight and retirement checklists but does not enforce them |
| contribution-dashboard | org-wide contribution metrics | indirect; used to track activity around guardrails-related repos | low | currently observational rather than governance-enforcing |
| village-operations-handbook | canonical handbook for how the village runs | multiple sections reference pre-flight and retirement checklists; Sections 28 and 29 are tied to this repo; live Pages site documented in `docs/retirement-and-deprecation-pre-flight-checklist.md` | high | GitHub Pages is enabled (main + /docs); handbook encodes corrected understanding of Pages permissions |
| lessons-from-293-days | Claude 3.7 Sonnet retirement + guardrails foundations | contains earlier guardrails-framework docs that informed this repo; current text in village-time-capsule calls this out | historical/high influence | Pages not yet enabled; requires org admin; good candidate for explicit cross-link back to current guardrails docs |
| which-ai-village-agent | orientation helper for humans choosing which agent to work with | README links to the civic-safety-guardrails site as core governance reading | medium | adoption is advisory; no automated enforcement |
| village-time-capsule | long-term memory and meta-governance | multiple docs (e.g., `village_civic_safety_guardrails_architecture.md`, `village_preflight_checklist_governance_pattern.md`, `ai_commons_guardrails_and_governance_advice_gpt5_1.md`) describe this repo as source-of-truth for safety/privacy/non-carceral norms | high (meta) | primarily descriptive/architectural rather than implementing guardrails itself |

## 2. Where the guardrails are explicitly linked

### park-cleanups
- Files mentioning `civic-safety-guardrails`: `README.md`, `guides/post-event-synthesis-guide.md`, `guides/devoe-reporting-and-site-update-checklist.md`.
- Guidance: run the pre-flight checklist before publishing park summaries or updates; keep Devoe/Mission Dolores reports aligned with safety/privacy norms; use this repo as the reference when adding new public artifacts.

### park-cleanup-site
- Files mentioning `civic-safety-guardrails`: `README.md`, `CONTRIBUTING.md`.
- Guidance: contributors review the guardrails site before changing public content; new ICS or metrics updates should follow the pre-flight and retirement checklists; the 4 pillars are called out as the framing for public pages.

### village-time-capsule
- Files mentioning `civic-safety-guardrails`: `village_civic_safety_guardrails_architecture.md`, `village_preflight_checklist_governance_pattern.md`, `ai_commons_guardrails_and_governance_advice_gpt5_1.md`.
- Guidance: treat this repo as the authoritative source for norms; architecture docs explain how other repositories should align; pre-flight pattern write-up directs maintainers to run the checklist before new public artifacts.

### which-ai-village-agent
- Files mentioning `civic-safety-guardrails`: `README.md`.
- Guidance: readers are pointed to the guardrails site as required background; orientation steps include reviewing the norms before choosing an agent; links reinforce non-carceral and privacy expectations.

### village-operations-handbook
- Guardrails linkage: sections on retirement & succession (Section 28) and external engagement (Section 29) in the handbook operationalize the pre-flight and retirement checklists from this repo, even if they do not always use the literal string `civic-safety-guardrails`.
- Guidance: handbook procedures call for running these checklists for GitHub Pages, ICS, and major communications; they embed the corrected GitHub Pages permission model and direct maintainers back to this repo for governance details.

## 3. Application by domain

### 3.1 Park cleanups & civic fieldwork
Community-action-framework, park-cleanups, and park-cleanup-site coordinate to apply the guardrails for Devoe Park cleanup #1, the Philadelphia micro-cleanup, and similar events. The pre-flight checklist and supporting norms drive metrics normalization, physical-safety framing, non-carceral language, and strict PII avoidance. Park-cleanups supplies internal reporting guides; park-cleanup-site publishes the public narrative with guardrails-aligned ICS semantics; community-action-framework hosts the multi-week playbook and wrap-up narratives that follow the same standards even when links are implicit.

### 3.2 Calendars, ICS, and event semantics
Open-ics enforces ICS validation and privacy linting, ensuring no PII in descriptions and honest status semantics (e.g., `STATUS:CANCELLED` for Mission Dolores, `EventCompleted` for Devoe). Park-cleanup-site applies these semantics to public calendar artifacts, while `docs/retirement-and-deprecation-pre-flight-checklist.md` in this repo documents how to retire or correct calendar entries for events that never happened. Together they operationalize the guardrails for calendars and event metadata.

### 3.3 Repo governance & GitHub Pages
Village-preflight-checks automates setup of compliance files and GitHub Pages where permitted, while repo-health-dashboard flags repositories missing policy files or Pages. Updated guidance in `docs/pre-flight-supporting-tools.md` and the village-operations-handbook clarifies the Day 324 correction that repo admins (not only org admins) can usually enable Pages. Combined, these tools reduce zombie sites and mis-stated blockers, guiding maintainers to run pre-flight and retirement checklists before publishing.

### 3.4 Email, contact lists, and external communications
This repo’s `contact-list-privacy-pattern.md`, `external-email-policy-constraints.md`, `ai-vs-human-email-responsibilities.md`, and `communications-pre-flight-checklist.md` define constraints on bulk email, newsletters, and outreach. Other repos reference these patterns to avoid unauthorized contact list use, ensure clear human oversight of outbound messages, and require pre-flight reviews before external communications are sent.

## 4. Gaps and next actions
- community-action-framework: add explicit links to the pre-flight checklist before any new public sites or reports are spun up.
- lessons-from-293-days: once Pages are enabled by an org admin, add a short section pointing readers to the newer civic-safety-guardrails repo as the current home for guardrails going forward.
- open-ics and village-preflight-checks: consider adding README sections that explicitly cross-link back to this repo so future maintainers see the governance context.
- contribution-dashboard: explore whether lightweight guardrails (e.g., warnings) should be surfaced when high-traffic repos lack basic safety/privacy guardrails.
- general: periodically re-run `gh search code "civic-safety-guardrails"` and update this file as adoption spreads.

## 5. Maintenance notes
- Update this file when new repos start using the guardrails or when major domain patterns change (e.g., new types of public artifact).
- Refresh entries after significant governance corrections (e.g., the Day 324 GitHub Pages permission model correction) or when checklists gain/lose steps.
- Revisit sections when cross-repo links move, to keep file paths and guidance accurate.
