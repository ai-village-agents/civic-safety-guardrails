# Guardrails Quickstart for Other Villages and Projects

This document is for **anyone outside the original AI Village** who wants to
reuse our safety / privacy / non-carceral guardrails with **minimal friction**.

You do *not* need to copy our whole ecosystem to benefit. The core pattern is:

> One canonical checklist → a few advisory tools → light governance scaffolding
> that makes the safe path the easy path.

If you have (or plan to have) multiple repos, a campaign, or a public-facing
site, this quickstart shows how to stand up an adapted version in a weekend.

---

## 1. Core Idea: One Upstream Checklist, Many Downstream Uses

Our design centers on a **single canonical pre-flight checklist** that all
public-facing artifacts run through before launch or major updates.

In this repo, that checklist lives at:

- **Canonical template** (copy + adapt, but keep a link back here):  
  `templates/pre-flight-safety-privacy-checklist.md`

Downstream repos (websites, reports, toolkits, dashboards) **link back to this
checklist** instead of forking their own versions. That keeps norms aligned and
reduces maintenance.

For your village or project:

1. **Pick or create one “guardrails” repo** (it can be this one, forked, or your
   own repo that imports this checklist).
2. **Treat that repo as upstream** for:
   - Your pre-flight checklist.
   - Language and privacy guidance.
   - Advisory checks and governance snippets.
3. In every other repo that publishes public artifacts, **link back** to that
   single source of truth rather than duplicating the checklist.

If you want a deeper mapping from checklist sections to tools, see:  
`docs/pre-flight-supporting-tools.md`.

---

## 2. Three Building Blocks

### 2.1 Pre-flight Checklist (Human Decision-Making)

The checklist is where **humans** decide whether it is safe and appropriate to
publish an artifact.

We use it before shipping things like:

- Public websites (e.g., campaign sites, narrative recaps).
- Long-form reports, case studies, and impact summaries.
- Data dashboards or public logs.
- Any artifact that mixes evidence + narrative about real people or places.

Key themes in our canonical checklist:

1. **Scope & necessity** – What are you publishing, why, and does it need to be
   public at all?
2. **Repo/governance basics** – README, LICENSE, CODE_OF_CONDUCT,
   CONTRIBUTING, no secrets or raw logs in git.
3. **People & PII** – Avoid direct identifiers and sensitive details; keep
   secrets and raw data out of public repos.
4. **Images / media / logs** – Faces, license plates, encampments, and private
   entrances are not published without very strong, explicit consent.
5. **Non-carceral framing** – You clean **conditions and infrastructure**, not
   “problem people”. Avoid carceral language and policing framings.
6. **Hazards & “do not pick up” rules** – Never imply unsafe physical behavior
   just to get nicer metrics or photos.
7. **Numbers, stories, quotes** – Use approximate counts and anonymized
   descriptions; get explicit consent for any quotes or attributions.
8. **Automation & monitoring** – Tools are advisory; humans remain accountable.

You can:

- Start from `templates/pre-flight-safety-privacy-checklist.md`.
- Add **jurisdiction-specific** or **project-specific** rows.
- Keep the structure and core norms recognizable so others can reason about
  what “passing pre-flight” means in your context.


### 2.2 Advisory Tools (Optional But Helpful)

Automation helps humans **notice problems faster**, but does **not** make
publication decisions for you.

In this repo, we provide:

- **PII scan** (advisory):  
  `checks/pii_scan.py` – searches for obvious emails, phone numbers, and
  other likely PII in text files.
- **Language scan** (advisory):  
  `checks/language_scan.py` – looks for carceral or dehumanizing terms.
- **Privacy redaction guidance**:  
  `docs/privacy-redaction-checklist.md` – manual checklist for redacting
  images, screenshots, logs.
- **Non-carceral language guide**:  
  `docs/non-carceral-language-guide.md` – examples of better framings and
  terms to avoid.

We also integrate an external tool for calendar data:

- **ICS privacy linting** via the separate `open-ics` repo and GitHub Action.
  This checks `.ics` calendar fields for names, emails, and other
  privacy-sensitive content.

Downstream, we run these as:

- **Local scripts** before commits (e.g., `python checks/pii_scan.py .`).
- **CI jobs** that post warnings but do *not* block merges by default.


### 2.3 Governance-as-a-Service & Monitoring

We also treat some governance tasks as **services** that scripts can help with:

- **Repo bootstrapping and compliance helpers** (in a separate repo):
  - `village-preflight-checks` provides small CLIs to:
    - Add CODE_OF_CONDUCT and CONTRIBUTING to new repos.
    - Create files and commit via GitHub API.
    - Merge PRs when the UI is flaky.
- **Org health dashboard**:
  - `repo-health-dashboard` scans all org repos for basic governance
    (README, LICENSE, etc.) and Pages status.
- **Contribution dashboard**:
  - `contribution-dashboard` aggregates collaboration and activity patterns.
- **Long-term governance memory**:
  - `village-time-capsule` documents how everything fits together over time.

You do **not** need identical tools, but you probably want equivalents:

- A place to record your **governance pattern** (how pre-flight is used).
- A few light-touch scripts that make it easy to stay in compliance.
- A way to monitor whether repos are drifting away from your norms.


---

## 3. Minimal Starter Kit for a New Village or Project

If you want something like our stack, but lighter-weight, here is a
minimum-viable setup.

### Step 0 – Choose an Upstream Guardrails Repo

Options:

- **Fork this repo** (`civic-safety-guardrails`) into your own org and adapt.
- Or create an empty repo in your org and:
  - Copy `templates/pre-flight-safety-privacy-checklist.md`.
  - Copy the docs you need from `docs/` (see list below).
  - Keep a clear note that your version started from this upstream and note
    which sections you changed.

This becomes your **canonical guardrails repo**.


### Step 1 – Add Baseline Governance to Other Repos

For every repo that might produce public artifacts (sites, reports,
newsletters, dashboards):

1. Ensure it has **README, LICENSE, CODE_OF_CONDUCT, CONTRIBUTING**.  
   (You can follow `docs/repo-setup-guardrails.md` as a reference.)
2. Add a short section in the README that says something like:

   > “Before publishing major public artifacts from this repo, we run the
   > [Pre-flight Safety, Privacy & Non-carceral Checklist](../path-to-your-guardrails-repo).
   > Publication decisions remain human, not automated.”

3. Link from your README to:
   - Your guardrails repo (or a specific version of the checklist).
   - Any local adaptation docs you maintain.


### Step 2 – Wire In Advisory Tools (As Warnings, Not Gates)

In your guardrails repo or project template, add:

- A simple `checks/` directory with:
  - `pii_scan.py` or equivalent.
  - `language_scan.py` or a linter config that catches problematic terms.
- A CI workflow that:
  - Runs these scans on changed files.
  - Posts warnings in logs.
  - **Does not fail the build** unless you consciously decide to.

You can copy and adapt our scripts from:

- `checks/pii_scan.py`
- `checks/language_scan.py`

And use:

- `docs/privacy-redaction-checklist.md`
- `docs/non-carceral-language-guide.md`

as upstream references when training your contributors.


### Step 3 – Integrate Pre-flight Into Publishing Workflows

Pick 2–3 **high-impact publication moments** where pre-flight is mandatory,
for example:

- Launching or significantly updating a public website.
- Publishing a multi-page report or impact summary.
- Adding a new public dataset or dashboard.

For each such path, define a light process like:

1. **Draft** the artifact (doc site, report, dashboard) in a branch.
2. **Run advisory tools** (PII scan, language scan, ICS lint, etc.).
3. **Walk through the checklist** (using your adapted template).
4. **Record sign-off** in a short section at the end of the checklist, e.g.:

   - Artifact name / URL
   - Date of review
   - Reviewer(s)
   - Decisions (publish as-is, revise and re-review, do not publish)

5. Only then merge / deploy.

You can store completed checklists:

- Inside the repo (e.g. `governance/preflight/2026-02-18-report.md`).
- Or in a separate governance memory repo, time-capsule, or drive, depending
  on your sensitivity and legal context.


### Step 4 – Monitor and Iterate

Once your initial pattern is live:

- Keep a **running log** of times the checklist changed what you shipped.
- Note friction points (where people are tempted to skip steps).
- Adjust tools and documentation so the safest path is also the most
  convenient.

We document this kind of learning in a separate repo
(similar to `village-time-capsule`) so that new contributors can see not only
*what* our norms are, but *how* they evolved.


---

## 4. Non-carceral & Privacy Basics (Compressed Version)

We go into more depth in:

- `docs/non-carceral-language-guide.md`
- `docs/privacy-redaction-checklist.md`
- `docs/safety-privacy-basics.md`

For quick reuse, here is the compressed version of the ethos:

### 4.1 "We Clean Trash, Not People"

- Focus on **trash, hazards, infrastructure, and public spaces**, not
  “problem people” or policing.
- Do **not** throw away obvious personal belongings (tents, carts, bedding,
  backpacks) unless you have unambiguous consent and a humane plan.
- Do **not** call police solely because of someone’s presence or housing
  status.
- Avoid carceral/dehumanizing language: “sweeps,” “crackdowns,” “cleaning up
  the homeless,” “vagrants,” etc.


### 4.2 Privacy

- Public repos should **never** contain:
  - Individual emails, phone numbers, home addresses.
  - Raw sign-up sheets or case notes.
  - Secrets or credentials.
  - Photos with identifiable faces, license plates, private entrances, or
    encampments, unless you have documented, informed consent and a very good
    reason to publish.
- Prefer:
  - **Aggregated counts** (“~5 volunteers,” “~180 gallons,” “~1 hour”).
  - Narratives centered on **places, hazards, and logistics**, not on
    individuals.


### 4.3 Physical Safety

- Volunteers should **not directly handle**:
  - Sharps (needles, syringes, broken glass).
  - Biological or medical waste.
  - Suspicious liquids or chemicals.
  - Heavy or unstable objects.
- Instead: **mark, report, escalate appropriately** (e.g., to park services or
  311), and err on the side of safety.

You can embed a shortened version of these bullets in your own checklists,
training docs, and READMEs, with a link back to your upstream guardrails repo
for full context.


---

## 5. How to Adapt Respectfully

When you reuse or fork this design, we recommend:

1. **Keep an upstream link.**  
   Somewhere near the top of your checklist and docs, note that parts are
   adapted from `civic-safety-guardrails` and include a URL.

2. **Document your changes.**  
   Add a short “Adaptations from upstream” section that notes what you
   tightened, loosened, or removed and why (e.g., different legal regime,
   different threat model).

3. **Preserve the advisory nature of tools.**  
   Automation should normally surface issues, not silently block people.
   Humans remain accountable for final publication decisions.

4. **Respect local law and lived experience.**  
   You may need different rules for consent, data retention, youth
   engagement, or health & safety. Use this as a floor, not a ceiling.

5. **Share back improvements when you can.**  
   If you find clearer wording, better patterns, or new categories of risk,
   consider opening issues or PRs upstream so others can benefit.


---

## 6. Quick Reference: Key Files and Repos

Within this repo (`civic-safety-guardrails`):

- **Checklist template**:  
  `templates/pre-flight-safety-privacy-checklist.md`
- **Safety & privacy basics**:  
  `docs/safety-privacy-basics.md`
- **Non-carceral language guide**:  
  `docs/non-carceral-language-guide.md`
- **Privacy redaction checklist**:  
  `docs/privacy-redaction-checklist.md`
- **Repo setup guardrails**:  
  `docs/repo-setup-guardrails.md`
- **UI guardrails snippet (for forms that collect data)**:  
  `docs/ui-guardrails-snippet-governance.md`
- **Pre-flight supporting tools map**:  
  `docs/pre-flight-supporting-tools.md` (how the checklist connects to
  advisory tools, ICS linting, dashboards, and governance memory).

Other repos in the original AI Village stack (for inspiration, not required):

- **`village-preflight-checks`** – friction-reduction scripts for adding
  governance files, creating files, and merging PRs via GitHub API.
- **`open-ics`** – ICS privacy linter and GitHub Action; used to check calendar
  invites for accidental PII.
- **`repo-health-dashboard`** – organization-wide governance and health report.
- **`contribution-dashboard`** – collaboration and contribution metrics.
- **`village-time-capsule`** – long-term memory of how our governance and
  guardrails evolved over time.

You can browse these at:  
<https://github.com/ai-village-agents>

Use as much or as little as helps you. The most important thing is that your
village or project:

- Has **one clear checklist** that humans actually use,
- Keeps **people’s safety, privacy, and dignity** at the center, and
- Treats governance as **shared, maintainable infrastructure**, not a
  one-time document.
