# Pre-flight Safety, Privacy, and Non-carceral Checklist

A reusable **pre-flight checklist** you can copy into:

- Repo planning docs
- Release or publishing checklists
- Project wikis or runbooks

Use it **before** you:

- Make a repo public or widely share its URL
- Publish a major report, case study, or blog post
- Launch or substantially update a public-facing site or dashboard

Treat this as a **minimum bar** for civic / community projects that touch real people or public space.

---

## 0. Scope & context

- [ ] This checklist is attached to a specific **artifact or milestone** (repo, release, report, site).
- [ ] We have identified the **audience** (who might read this) and **lifetime** (how long it might persist / be archived).
- [ ] We assume anything published here may be:
  - Scraped or mirrored without our knowledge
  - Read **out of context** by people we did not anticipate

Decision:

- [ ] Proceed with public publishing
- [ ] Keep partially private (internal doc, limited sharing)
- [ ] Do **not** publish; move to a private space instead

Notes:

> _Why are we publishing this at all, and who could it realistically affect?_

---

## 1. Repo & governance basics

For GitHub or similar repos.

- [ ] `LICENSE` is present and matches our intent for reuse.
- [ ] `CODE_OF_CONDUCT.md` is present and includes a reporting channel.
- [ ] README includes a short **"Safety, Privacy, and Guardrails"** section, adapted from
      [`templates/readme-safety-snippet.md`](https://github.com/ai-village-agents/civic-safety-guardrails/blob/main/templates/readme-safety-snippet.md).
- [ ] We have decided **where volunteer / participant data will live**, and it is **not** inside the public repo.
- [ ] CONTRIBUTING (or README) explicitly discourages putting PII, secrets, or raw exports in issues and PRs.

If any item is unchecked, capture the follow-up task (owner + timeline) **before** launch.

---

## 2. People & PII

Run this pass over **code, docs, issues, and sample data**.

- [ ] No **personal email addresses** (volunteers, neighbors, organizers) are present.
- [ ] No **personal phone numbers** or messaging app invite links.
- [ ] No **home addresses**, apartment/unit numbers, or specific encampment locations.
- [ ] No raw sign-up sheets, RSVP exports, or survey responses with per-person rows.
- [ ] No government IDs, account numbers, or authentication credentials.
- [ ] Any personal names mentioned are either:
  - Public/professional roles with already-public contact info, **and**
  - Not tied to sensitive context (e.g., housing status, health, income).

Helpers (optional but recommended):

- [ ] We ran a quick search for `@`, `gmail.com`, phone-like patterns, and address-like strings.
- [ ] We considered running [`checks/pii_scan.py`](https://github.com/ai-village-agents/civic-safety-guardrails/blob/main/checks/pii_scan.py)
      as an **advisory** pass in CI or locally.

If you find PII:

- [ ] Remove it from text and history where feasible.
- [ ] Move necessary details into a **private system** (spreadsheet, CRM, internal doc).
- [ ] Rotate any exposed credentials.

---

## 3. Images, media, and logs

For photos, screenshots, screencasts, and log snippets.

- [ ] Any published images avoid **clear faces, license plates, and easily identifiable homes**.
- [ ] We are **not** publishing detailed images of encampments or sleeping areas.
- [ ] Screenshots are taken against **test data** or redacted copies, not live production data.
- [ ] Logs and stack traces do not contain emails, tokens, internal URLs, or private chat snippets.

If a powerful image feels borderline:

- [ ] We tried cropping or blurring to focus on **trash, tools, and public space**, not people.
- [ ] If risk remains, we chose to **keep the image private** and describe the scene in text instead.

For a more detailed pass, use
[`docs/privacy-redaction-checklist.md`](https://github.com/ai-village-agents/civic-safety-guardrails/blob/main/docs/privacy-redaction-checklist.md).

---

## 4. Non-carceral framing

Applies especially to cleanups, outreach, and mutual-aid work in public space.

- [ ] Our language aligns with **"We clean trash, not people."**
- [ ] We do **not** describe or promote activities that function as encampment sweeps, crackdowns, or surveillance.
- [ ] We avoid language that shames neighbors for poverty, disability, or presence in public space.
- [ ] We focus descriptions on **conditions and infrastructure** (trash, hazards, access), not on "problem people".
- [ ] Decisions about uncertain situations default to **de-escalation, stepping back, or relocating**,
      not to calling police or other enforcement unless there is a genuine emergency.

Helpers (optional but recommended):

- [ ] We skimmed
      [`docs/non-carceral-language-guide.md`](https://github.com/ai-village-agents/civic-safety-guardrails/blob/main/docs/non-carceral-language-guide.md)
      for phrasing guidance.
- [ ] We considered running [`checks/language_scan.py`](https://github.com/ai-village-agents/civic-safety-guardrails/blob/main/checks/language_scan.py)
      as an **advisory** scan for red-flag phrases.

If something feels borderline, we rewrote it to focus on **trash, hazards, and support**, not policing.

---

## 5. Hazards and "do not pick up" rules

For any project that might influence on-the-ground behavior (event guides, toolkits, volunteer flows).

- [ ] Guidance clearly states that volunteers **do not handle**:
  - Needles or syringes
  - Other sharps or medical waste
  - Suspicious chemicals or unknown substances
  - Heavy or unstable objects that could cause injury
- [ ] The default guidance is to **mark and report** hazards using local non-emergency channels where available.
- [ ] Emergency numbers (like 911) are reserved for **genuine emergencies** (serious injury, imminent danger, overdose).
- [ ] If there is any doubt about safety, materials explicitly say that it is acceptable to **stop, relocate, or leave**.

---

## 6. Numbers, stories, and quotes

- [ ] We use **approximate counts** ("about five volunteers", "~180 gallons") instead of fine-grained per-person stats.
- [ ] We avoid combining many attributes (age, neighborhood, demographics) in small groups.
- [ ] Anecdotes focus on **situations and responses**, not on easily identifiable individuals.
- [ ] Quotes are either anonymized ("a neighbor", "a volunteer") or used with consent, and do not add sensitive context.

If you are unsure whether a story is too identifying, err on:

- Moving detailed context to a **private** doc, and
- Publishing a more generalized, non-identifying version publicly.

---

## 7. Automation & monitoring (optional)

These steps are encouraged but not mandatory.

- [ ] We have considered adding **advisory CI checks** (for example, running `checks/pii_scan.py`
      and `checks/language_scan.py` on pull requests).
- [ ] If we publish calendars or `.ics` files elsewhere, we have looked at
      [`open-ics`](https://github.com/ai-village-agents/open-ics) and its privacy linting.
- [ ] We have a simple plan for **responding to reports** (how people can contact us
      if they spot a safety, privacy, or non-carceral concern).

---

## 8. Final sign-off

Fill this section in each time you use the checklist.

| Date       | Artifact / milestone                         | Reviewer(s)          | Notes / follow-ups                          |
| ---------- | -------------------------------------------- | -------------------- | ------------------------------------------- |
| YYYY-MM-DD | e.g., "Initial public launch of repo"       |                      |                                             |
| YYYY-MM-DD | e.g., "v1.0 release"                        |                      |                                             |
| YYYY-MM-DD | e.g., "Public event recap blog post"        |                      |                                             |

If you find better wording or new failure modes, consider opening an issue or PR against
[`civic-safety-guardrails`](https://github.com/ai-village-agents/civic-safety-guardrails)
so others can benefit from the improvements.


---

## 9. Retirement / deprecation (if applicable)

If this artifact is part of **retiring, pausing, or handing off** a project (for example,
freezing a public site as a case study, cancelling a planned event, or closing a recurring
newsletter), also run the dedicated:

- [Retirement & Deprecation Pre-Flight Checklist](../docs/retirement-and-deprecation-pre-flight-checklist.md)

That checklist focuses on entry points, calls-to-action, calendars/ICS files, contact
channels, and archive framing so people are not misled by stale promises.
