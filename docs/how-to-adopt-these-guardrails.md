# How to Adopt These Guardrails

Practical steps for using this repo in your own projects.

This guide is written for:

- Maintainers spinning up **new civic or community repos** (park cleanups, mutual aid, benefit screeners, tenant support, etc.).
- People inheriting or maintaining **existing repos** that already have users.
- Authors of **libraries and tools** that are used inside civic projects and want to avoid accidental harm.

You don’t need to adopt everything at once. The goal is to make **small, safe improvements** that
stack over time.

---

## 1. The building blocks in this repo

At a glance:

- **Safety & privacy baseline**
  - [`docs/safety-privacy-basics.md`](safety-privacy-basics.md) – short neutral framing for new projects
    (currently a draft stub).
  - [`docs/repo-setup-guardrails.md`](repo-setup-guardrails.md) – launch checklist for new repos
    (license, Code of Conduct, README notes, data location).
- **Language and stories**
  - [`docs/non-carceral-language-guide.md`](non-carceral-language-guide.md) – examples of carceral vs
    non-carceral framing (currently a draft stub).
- **Pre-publication checks**
  - [`docs/privacy-redaction-checklist.md`](privacy-redaction-checklist.md) – step-by-step pass over text,
    images, logs, and example data before you publish.
- **Drop-in templates**
  - [`templates/readme-safety-snippet.md`](../templates/readme-safety-snippet.md) – ready-to-paste
    “Safety, Privacy, and Guardrails” section for your README.

The scenarios below tell you **which pieces to use first**.

---

## 2. Scenario A – New civic / community repo

Example projects: park cleanups, mutual aid logistics, community health outreach, benefit screeners.

### Step A1 – Set baseline project expectations

1. Add a `LICENSE` file (MIT is a good default for this org).
2. Add `CODE_OF_CONDUCT.md` based on the Contributor Covenant.
3. Optionally link back to this repo so contributors know which norms you are using.

Use: [`docs/repo-setup-guardrails.md`](repo-setup-guardrails.md), sections 1 and 6.

### Step A2 – Add a README safety section

1. Open [`templates/readme-safety-snippet.md`](../templates/readme-safety-snippet.md).
2. Copy the whole snippet into your `README.md`.
3. Customize:
   - The project name.
   - Any project-specific examples (e.g., “park cleanups” vs “benefit screener”).
4. Keep the **no PII**, **approximate stats**, and **non-carceral** language intact unless you have a strong,
   well-documented reason to change it.

This gives collaborators a clear, visible statement of what belongs in the repo and what does not.

### Step A3 – Decide where data about people will live

Before you share a repo link:

- Decide which **private tools** you will use (e.g., Google Sheets/Docs, internal CRM, helpdesk).
- Explicitly **do not** store:
  - Volunteer signups or contact lists.
  - Per-person notes, accessibility needs, safety notes.
  - Raw survey or form exports.

Use: [`docs/repo-setup-guardrails.md`](repo-setup-guardrails.md), sections 3 and 5.

### Step A4 – Add contribution expectations

In `CONTRIBUTING.md` (or the README if you don’t have one yet), add a short section that:

- Bans volunteer PII and secrets from issues, PRs, and example data.
- Encourages contributors to run the privacy checklist before adding docs or screenshots.
- Reminds people of the non-carceral and no-sharps norms if your project touches public space.

Use: [`docs/repo-setup-guardrails.md`](repo-setup-guardrails.md), sections 4 and 5.

### Step A5 – Use the privacy checklist before you publish

Before you:

- Publish a major report or case study,
- Upload photos to a repo or website, or
- Share logs, screenshots, or example datasets,

run through [`docs/privacy-redaction-checklist.md`](privacy-redaction-checklist.md).

If time is tight, use the **“Quick version (2-minute check)”** at the bottom of that doc.

---

## 3. Scenario B – Existing repo you want to upgrade

Maybe you already have a repo for an event series, mutual-aid group, or public-facing tool.

You can adopt these guardrails in **one small PR**:

### Step B1 – Add or update the README safety section

- Copy [`templates/readme-safety-snippet.md`](../templates/readme-safety-snippet.md) into your `README.md`.
- If you already have a safety/privacy section, reconcile and keep the strongest language from both.

### Step B2 – Add contribution guidance

- Add a short “Contributing safely” subsection to `CONTRIBUTING.md` or the README.
- Base it on the guidance in [`docs/repo-setup-guardrails.md`](repo-setup-guardrails.md), section 4.

### Step B3 – Run a privacy pass over existing content

1. Pick the most visible public artifacts:
   - README, key docs, and any public reports.
   - Image folders or assets used on a website.
2. Run the passes in [`docs/privacy-redaction-checklist.md`](privacy-redaction-checklist.md).
3. Open a follow-up issue list for anything that needs more work (e.g., older photos to be replaced).

If your project is about cleanups, encampments, or public space, also skim
[`docs/non-carceral-language-guide.md`](non-carceral-language-guide.md) and adjust wording that
sounds like surveillance, sweeps, or crackdowns.

### Step B4 – Optionally plan checks or CI

If you use CI:

- Note that `checks/` is currently a placeholder; future versions of this repo will include sample
  scripts and GitHub Actions to:
  - scan for obvious email patterns and secrets, and
  - flag certain phrases or patterns for manual review.

You can prepare by:

- Adding a short item to your backlog: “Integrate privacy/language checks from
  `civic-safety-guardrails/checks/` when they are ready.”

---

## 4. Scenario C – Libraries and tools

If your project is a **library, CLI, or service** that may be used in civic contexts, you can still
benefit from these guardrails:

1. Add a brief “Safety & privacy” note to your README:
   - Emphasize that examples use **synthetic data**.
   - Discourage using the project to collect or publish sensitive personal data unless users have
     a clear plan for handling it safely.
2. Avoid shipping real logs, ICS feeds, or datasets that contain PII, even in “examples”.
3. If your tool can be pointed at real-world communities (e.g., mapping, scraping, analytics),
   skim [`docs/non-carceral-language-guide.md`](non-carceral-language-guide.md) to avoid suggesting
   uses that look like surveillance or targeting.

You can still reuse pieces like [`templates/readme-safety-snippet.md`](../templates/readme-safety-snippet.md),
but you may want to trim or adapt the parts about volunteers and public events.

---

## 5. Minimal adoption checklist

If you only have an hour, aim for this:

- [ ] README has a short “Safety, Privacy, and Guardrails” section, based on the template.
- [ ] Repo clearly states **what data belongs** here and what should stay in private systems.
- [ ] CONTRIBUTING (or README) tells contributors **not to add PII or secrets**.
- [ ] You have run at least the **2-minute version** of the privacy checklist on the most visible docs.
- [ ] For projects that touch public space or vulnerable neighbors, you have checked that your language
      matches **“We clean trash, not people.”**

Once this is in place, your project is aligned with the core norms here, and you can adopt more
pieces over time as needed.
