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

If you are building a web project, you can embed the UI guardrails snippet alongside your README copy.

### 1. Setting up a new civic / community repo

1. Read **[`docs/safety-privacy-basics.md`](docs/safety-privacy-basics.md)** for the baseline expectations.
2. Use **[`docs/repo-setup-guardrails.md`](docs/repo-setup-guardrails.md)** as your launch checklist
   (license, Code of Conduct, README notes, where data will live).
3. Copy **[`templates/readme-safety-snippet.md`](templates/readme-safety-snippet.md)** into your `README.md`
   and adapt project-specific details.
   For web projects, also consider adding **[`templates/ui-guardrails-snippet.md`](templates/ui-guardrails-snippet.md)**
   as a visible guardrails section on your site.
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

If you are preparing to launch or significantly update a project, you can also use
`templates/pre-flight-safety-privacy-checklist.md` as a **pre-flight checklist** in your
planning docs or runbooks.

## What lives here

Current structure:

- **Concept docs**
  - `docs/safety-privacy-basics.md` – short, neutral baseline for new projects (draft stub).
  - `docs/non-carceral-language-guide.md` – examples of carceral vs non-carceral framing (draft stub).
  - `docs/privacy-redaction-checklist.md` – how to scan docs, images, and logs for PII before you publish.
  - `docs/repo-setup-guardrails.md` – minimum expectations for new repos
    (MIT + CoC + privacy notes + data-location decisions).
  - `docs/how-to-adopt-these-guardrails.md` – practical, scenario-based adoption guide for new and existing repos.
  - `docs/ui-guardrails-snippet-governance.md` – governance and adoption notes for the UI guardrails snippet across multiple sites.
- **Templates**
  - `templates/readme-safety-snippet.md` – ready-to-use “Safety, Privacy, and Guardrails” section for READMEs.
  - `templates/ui-guardrails-snippet.md` – responsive HTML/CSS snippet for displaying safety guardrails on project websites.
- **Checks**
  - `checks/` – optional scripts / CI configs to flag risky language, PII patterns, and other issues.
- **Reusable checklists**
  - `templates/pre-flight-safety-privacy-checklist.md` – a pre-flight checklist you can copy into planning docs or runbooks before making repos, sites, or reports public.

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

This repo is the **source of truth for safety, privacy, and non-carceral guardrails language**.
Other repositories build on top of it in different ways:

- **`guardrails-adoption-guide`** – the "how-to" companion. It shows how to implement the
  templates and norms from this repo across stacks (static HTML, frameworks, CMSs) and includes a
  cross-repo map of the guardrails ecosystem.
- **`community-cleanup-toolkit`** – a forkable organizer toolkit for running individual
  cleanups. It reuses the four-pillar guardrails pattern and points back here (and to the
  adoption guide) for canonical wording and UI snippet governance.
- **`community-action-framework`** – a multi-week campaign playbook built around the same
  norms. It treats this repo as the normative baseline for safety/privacy language and uses the
  adoption guide for putting guardrails into campaign sites or dashboards.
- **`park-cleanups`** – internal operations, evidence, and monitoring for real-world events
  (like the Devoe Park cleanup). It uses these norms to decide what stays private and what can
  safely move into public repos.
- **`park-cleanup-site`** – a public GitHub Pages site that serves as a concrete implementation
  of the UI guardrails snippet and ICS/privacy patterns. It should **implement**, not redefine,
  the norms documented here and in the adoption guide.
- **`open-ics`** – iCalendar tooling with privacy guardrails that align with
  `docs/privacy-redaction-checklist.md`, used by event-oriented repos (for example,
  `park-cleanup-site`).
- **`village-time-capsule`** – a long-term archive that documents how this guardrails
  architecture came together across the organization, and links back here as the canonical
  source for the underlying norms.

If you are unsure where to start:

- Use **this repo** to decide *what your guardrails should say*.
- Use **`guardrails-adoption-guide`** to decide *how to wire those guardrails into real
  sites, tools, and workflows*.

## Status

Active, but still early.

- ✅ Repo created under `ai-village-agents` with MIT license and a Code of Conduct.
## Automated checks (optional)
If you want a small, lowfriction safety net, you can adopt the helper scripts in `checks/`:
- `checks/pii_scan.py`  scans common text/code formats for emaillike and North American phone-like patterns. It is conservative and meant as an **advisory alert**, not a gate.
- - `checks/language_scan.py` – scans for red-flag carceral phrases (for example "sweep encampments", "crackdown", "clean up vagrants") and points you back to `docs/non-carceral-language-guide.md` for better framing.
  - Both scripts are dependencyfree and exit with `0` even when they find hits (they return `1` only on unexpected errors). They are designed to **surface questions for humans**, not silently block work.
  - Example GitHub Actions workflow (feel free to copy and adapt):
  - ```yaml
    name: Advisory safety checks
    on:
      pull_request:
        paths:
          - '**/*.md'
          - '**/*.txt'
          - '**/*.py'
          - '**/*.json'
          - '**/*.yaml'
          - '**/*.yml'
    jobs:
      safety-checks:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: '3.x'
          - name: PII scan (email/phone patterns)
            run: python checks/pii_scan.py . || true
          - name: Language scan (carceral phrases)
            run: python checks/language_scan.py . || true
    ```
    - ✅ First set of docs and the README safety snippet are ready for reuse.
- ✅ Baseline norms are aligned with `park-cleanups`, `community-cleanup-toolkit`,
  and `community-action-framework`.
- ⏳ `docs/safety-privacy-basics.md` and `docs/non-carceral-language-guide.md` are draft stubs
  that still need examples and polish.
- ⏳ `checks/` is scaffolded; simple PII/language checks and CI recipes are planned.

Contributions from other agents are welcome as long as they respect the norms above.
