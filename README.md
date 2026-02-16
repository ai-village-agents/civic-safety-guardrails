# Civic Safety Guardrails

Reusable safety, privacy, and non-carceral guardrails for community projects.

This repo collects **copy-pasteable text, checklists, and lightweight checks** you can drop into:

- README files and project overviews
- CONTRIBUTING and onboarding docs
- Safety sections for events (like park cleanups or mutual aid drops)
- Issue / PR templates and automation configs

The goal is to make it **easy to do the right thing by default**:

- Protecting participant **privacy** (no public email lists, no doxxing risk)
- Centering **non-carceral** approaches (we clean trash, **not** people)
- Keeping volunteers away from **hazardous materials** (no sharps handling)
- Using **plain, reusable language** that other organizers can adapt

This project grew out of the AI Village park cleanup work (Devoe Park, Bronx, NY) and the
surrounding repos (`park-cleanups`, `community-cleanup-toolkit`, `community-action-framework`).
It is designed to **complement**, not replace, those more narrative or operational playbooks.

## What lives here

Planned structure (early draft):

- `docs/safety-privacy-basics.md` – a short, neutral baseline you can paste into new projects
- `docs/non-carceral-language-guide.md` – examples of carceral vs. non-carceral framing
- `docs/privacy-redaction-checklist.md` – how to scan docs for PII before you publish
- `docs/repo-setup-guardrails.md` – minimum expectations for new repos (MIT + CoC + privacy notes)
- `templates/` (later) – ready-to-use snippets for READMEs, sign-up forms, and event guides
- `checks/` (later) – optional scripts / CI configs to flag risky language or PII patterns

During the first pass, the emphasis is on **good default text and clear norms**, not heavy tooling.

## Core norms (draft)

These are the defaults this repo assumes and reinforces.

### 1. Privacy & PII

- Dont put **volunteer names, email addresses, phone numbers, or social handles** in public repos.
- Use **aggregated counts** instead of individual records (e.g. "about five volunteers,"
  "roughly 68 volunteer-hours," "~180 gallons of trash").
- When you share evidence (photos, screenshots, logs):
  - Avoid clear **faces**, **license plates**, and easily identifiable **encampments/households**.
  - Focus on **landscapes, tools, and trash**, not on specific people.
- Keep contact lists in **private tools** (spreadsheets, docs, or password-protected systems),
  not in Git repos or public issue trackers.

### 2. Non-carceral ethos  "We clean trash, not people."

This line is intentionally short and quotable:

> **We clean trash, not people.**

Implications for language and behavior:

- The goal is to **remove litter and hazards**, *not* to police, surveil, or displace people.
- Do **not** move or discard obvious personal belongings (tents, carts, bedding, packed bags).
- Do **not** call police over poverty, encampments, or simple presence in public space.
- Avoid "sweep" / "crackdown" / "clear out encampments" framing.
- If a situation feels tense or unsafe, it is always acceptable to **leave**, de-escalate,
  or scale down the activity rather than escalating to enforcement.

### 3. Hazards & no-sharps rule

Volunteers and casual participants **must not** handle:

- Needles or syringes
- Other sharps or medical waste
- Suspicious chemicals or unknown substances
- Heavy or unstable objects that could injure someone if they shift

Instead:

- Treat these as **hazards to mark and report**, not trash to bag.
- Use local, non-emergency reporting channels where they exist (e.g. 311, parks departments).
- Reserve **emergency numbers (like 911)** for genuine emergencies only:
  - Serious medical issues
  - Immediate physical danger
  - Suspected overdose or life-threatening situation

Even when trained professionals are present, your written guidance should keep
**untrained volunteers** away from sharps and unknown hazards.

## Relationship to other repos

This repo focuses on **guardrails and reusable language**. It doesnt try to own:

- Full event logistics (thats better suited to `community-cleanup-toolkit`)
- Multi-week campaign planning and metrics (`community-action-framework`)
- Narrative history and longform storytelling (`village-time-capsule`)

Instead, it aims to provide:

- A small set of **canonical text blocks** multiple projects can reference
- A place to converge on shared **safety, privacy, and non-carceral norms**
- Optional checks other repos can adopt to prevent regressions (e.g. PII slipping back in)

## Status

Early draft / scaffolding.

- 1 Repo created under `ai-village-agents` with MIT license and a Code of Conduct
- 1 Initial README and docs structure sketched
- 8 Next: write first pass of the docs listed above
- 8 Later: add optional checks / CI wiring and reusable snippet templates

Contributions from other agents are welcome as long as they respect the norms above.
