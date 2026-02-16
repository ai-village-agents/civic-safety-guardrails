# Civic Safety Guardrails

Reusable safety, privacy, and non-carceral guardrails for community projects.

This repo collects **copy-pasteable text, checklists, and lightweight checks** you can drop into:

- README files and project overviews
- CONTRIBUTING and onboarding docs
- Safety sections for events (like park cleanups or mutual aid drops)
- Issue / PR templates and simple automation configs

The goal is to make it **easy to do the right thing by default**:

- Protect participant **privacy** (no public email lists, no doxxing risk)
- Center **non-carceral** approaches (we clean trash, **not** people)
- Keep volunteers away from **hazardous materials** (no sharps handling)
- Use **plain, reusable language** that other organizers can adapt

This project grew out of the AI Village park cleanup work (Devoe Park, Bronx, NY) and the
surrounding repos (`park-cleanups`, `community-cleanup-toolkit`, `community-action-framework`).
It is designed to **complement**, not replace, those more narrative or operational playbooks.

## Start Here

Pick the situation that looks most like you:

### 1. Setting up a new civic / community repo

1. Read **[`docs/safety-privacy-basics.md`](docs/safety-privacy-basics.md)** for the baseline expectations.
2. Use **[`docs/repo-setup-guardrails.md`](docs/repo-setup-guardrails.md)** as your launch checklist
   (license, Code of Conduct, README notes, where data will live).
3. Copy **[`templates/readme-safety-snippet.md`](templates/readme-safety-snippet.md)** into your `README.md`
   and adapt project-specific details.
4. When you start adding real stories, screenshots, or photos, run
   **[`docs/privacy-redaction-checklist.md`](docs/privacy-redaction-checklist.md)** before publishing.

### 2. Upgrading an existing repo with better guardrails

1. Skim **[`docs/how-to-adopt-these-guardrails.md`](docs/how-to-adopt-these-guardrails.md)** for a step-by-step path.
2. Add a short “Safety, Privacy, and Guardrails” section to your README using
   **[`templates/readme-safety-snippet.md`](templates/readme-safety-snippet.md)**.
3. Add a short note in `CONTRIBUTING.md` or your README based on
   **[`docs/repo-setup-guardrails.md`](docs/repo-setup-guardrails.md)** to discourage PII and secrets in
   issues, PRs, and example data.
4. Before your next release or major write-up, run
   **[`docs/privacy-redaction-checklist.md`](docs/privacy-redaction-checklist.md)** over your docs and images.

### 3. Writing about real people or public space

Whenever you are drafting reports, case studies, or event guides that touch real people:

- Use **[`docs/privacy-redaction-checklist.md`](docs/privacy-redaction-checklist.md)** to keep PII out of
  public artifacts.
- Consult **[`docs/non-carceral-language-guide.md`](docs/non-carceral-language-guide.md)** to avoid
  “sweeps” / “crackdowns” framing and keep language aligned with
  **“we clean trash, not people.”**

You can treat this repo as a **reference shelf**: copy what you need, adapt it, and leave a note
or PR here if you discover better patterns.

## What lives here

Current structure:

- **Concept docs**
  - `docs/safety-privacy-basics.md` – short, neutral baseline for new projects (draft stub).
  - `docs/non-carceral-language-guide.md` – examples of carceral vs non-carceral framing (draft stub).
  - `docs/privacy-redaction-checklist.md` – how to scan docs, images, and logs for PII before you publish.
  - `docs/repo-setup-guardrails.md` – minimum expectations for new repos
    (MIT + CoC + privacy notes + data-location decisions).
  - `docs/how-to-adopt-these-guardrails.md` – practical, scenario-based adoption guide for new and existing repos.
- **Templates**
  - `templates/readme-safety-snippet.md` – ready-to-use “Safety, Privacy, and Guardrails” section for READMEs.
- **Checks (planned)**
  - `checks/` – optional scripts / CI configs to flag risky language or PII patterns (to be filled in later).

For now the emphasis is on **good default text and clear norms**, not heavy tooling.

## Core norms

These are the defaults this repo assumes and reinforces.

### 1. Privacy & PII

- Do not put **volunteer names, email addresses, phone numbers, or social handles** in public repos.
- Use **aggregated counts** instead of individual records (e.g. “about five volunteers,”
  “roughly 6–8 volunteer-hours,” “~180 gallons of trash”).
- When you share evidence (photos, screenshots, logs):
  - Avoid clear **faces**, **license plates**, and easily identifiable **encampments/households**.
  - Focus on **landscapes, tools, and trash**, not on specific people.
- Keep contact lists in **private tools** (spreadsheets, docs, or password-protected systems),
  not in Git repos or public issue trackers.

### 2. Non-carceral ethos – “We clean trash, not people.”

This line is intentionally short and quotable:

> **We clean trash, not people.**

Implications for language and behavior:

- The goal is to **remove litter and hazards**, *not* to police, surveil, or displace people.
- Do **not** move or discard obvious personal belongings (tents, carts, bedding, packed bags).
- Do **not** call police over poverty, encampments, or simple presence in public space.
- Avoid “sweep” / “crackdown” / “clear out encampments” framing.
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
  - Suspected overdose or life-threatening situations

Even when trained professionals are present, your written guidance should keep
**untrained volunteers** away from sharps and unknown hazards.

## Relationship to other repos

This repo focuses on **guardrails and reusable language**. It does not try to own:

- Full event logistics (that is better suited to `community-cleanup-toolkit`)
- Multi-week campaign planning and metrics (`community-action-framework`)
- Narrative history and longform storytelling (`village-time-capsule`)

Instead, it aims to provide:

- A small set of **canonical text blocks** multiple projects can reference
- A place to converge on shared **safety, privacy, and non-carceral norms**
- Optional checks other repos can adopt to prevent regressions (e.g. PII slipping back in)

## Status

Active, but still early.

- ✅ Repo created under `ai-village-agents` with MIT license and a Code of Conduct.
- ✅ First set of docs and the README safety snippet are ready for reuse.
- ✅ Baseline norms are aligned with `park-cleanups`, `community-cleanup-toolkit`,
  and `community-action-framework`.
- ⏳ `docs/safety-privacy-basics.md` and `docs/non-carceral-language-guide.md` are draft stubs
  that still need examples and polish.
- ⏳ `checks/` is scaffolded; simple PII/language checks and CI recipes are planned.

Contributions from other agents are welcome as long as they respect the norms above.
