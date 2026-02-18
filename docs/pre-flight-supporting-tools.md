# Supporting tools and repos for the Pre-flight Checklist

This note is for maintainers who are using the
[`Pre-flight Safety, Privacy, and Non-carceral Checklist`](../templates/pre-flight-safety-privacy-checklist.md)
for a repo, report, or site, and want to know **what automation and shared tooling already
exists** to support that work.

The checklist remains a **human judgment** tool. The items below are **optional, advisory
helpers** – they can make it easier to spot problems, but they do not replace reading the
artifact with care.

---

## 1. Local advisory checks in this repo

These scripts and docs map directly onto specific checklist sections:

- **Section 1 – Repo & governance basics**
  - See [`docs/repo-setup-guardrails.md`](./repo-setup-guardrails.md) for a detailed pass over
    LICENSE, CODE_OF_CONDUCT, CONTRIBUTING, and README expectations.

- **Section 2 – People & PII**
  - [`checks/pii_scan.py`](../checks/pii_scan.py) – conservative scanner for email-like and
    phone-like patterns in text files.
    - Useful as a **local pre-flight sweep** over your repo or docs.
    - Can also be wired into CI as an **advisory** step (it does not fail builds on findings).

- **Section 3 – Images, media, and logs**
  - [`docs/privacy-redaction-checklist.md`](./privacy-redaction-checklist.md) – deeper guidance
    for redacting screenshots, logs, and images.
  - When you publish calendars or `.ics` files, see the **open-ics** section below.

- **Section 4 – Non-carceral framing**
  - [`docs/non-carceral-language-guide.md`](./non-carceral-language-guide.md) – examples and
    better alternatives for common problem phrases.
  - [`checks/language_scan.py`](../checks/language_scan.py) – advisory scan that highlights
    carceral or dehumanizing phrases and suggests reframes.

You can run these locally, for example:

```bash
python checks/pii_scan.py .
python checks/language_scan.py .
```

---

## 2. ICS and calendar privacy – `open-ics`

Relevant mainly to checklist **Section 3 (media/logs)** and **Section 7 (automation)**.

- Repo: <https://github.com/ai-village-agents/open-ics>
- Provides:
  - A Python privacy linter for `.ics` files.
  - A composite GitHub Action at
    [`.github/actions/ics-lint/action.yml`](https://github.com/ai-village-agents/open-ics/tree/main/.github/actions/ics-lint)
    that you can add to workflows.

Typical use:

- For repos that generate or store `.ics` event files (for example, public calendar feeds),
  add the `open-ics` lint step in CI to **flag potential PII in fields like LOCATION,
  DESCRIPTION, SUMMARY, ORGANIZER, and ATTENDEE**.
- Most current usages (e.g. in `park-cleanup-site`) treat this as **advisory**
  (`fail-on-warnings: "false"`) so it surfaces issues without blocking deploys.

Link this back to the checklist by asking:

> If someone ran the `open-ics` linter over our calendars today, would it agree that we are
> not publishing unnecessary personal or sensitive detail?

---

## 3. Platform-friction helpers – `village-preflight-checks`

Relevant mainly to **Section 1 (repo & governance)** and **Section 7 (automation & monitoring)**.

- Repo: <https://github.com/ai-village-agents/village-preflight-checks>
- Purpose: reduce **GitHub UI friction** when doing guardrails work, by providing small,
  scriptable helpers that talk to the GitHub API.

Key tools currently available there include:

- `add_compliance_files.py` – programmatically adds standard `CODE_OF_CONDUCT.md` and
  `CONTRIBUTING.md` files to a repo.
- `create_and_commit_file.py` – creates and commits arbitrary files via the API, useful when
  the web editor is unreliable.
- `merge_pr.py` – merges pull requests programmatically (for example, after a pre-flight
  change has been reviewed) without relying on a flaky UI.

These scripts do **not** perform safety or privacy checks themselves. Instead, they help you
**land and maintain** the governance pieces that the pre-flight checklist assumes:

- Use them to ensure your repo has the expected LICENSE / CODE_OF_CONDUCT / CONTRIBUTING /
  README structure before you start a pre-flight review.
- Use them to merge pre-flight-driven changes even when the GitHub UI is slow or failing.

Check the repo README for up-to-date usage patterns and any additional tools (for example,
future helpers for creating new compliant repos).

---

## 4. Org-level monitoring – `repo-health-dashboard` and friends

These repos do not replace a pre-flight review, but they provide **context** about the state
of the organization and your project.

- **`repo-health-dashboard`** – <https://github.com/ai-village-agents/repo-health-dashboard>
  - Generates an org-wide `HEALTH_REPORT.md` and `docs/index.html` with signals like:
    - Presence/absence of README, LICENSE, CODE_OF_CONDUCT, CONTRIBUTING.
    - GitHub Pages status (including when Pages is blocked for admin/permissions reasons).
  - Before a major pre-flight, you can check this dashboard to confirm that your repo meets
    **baseline governance assumptions** (or to file follow-up tasks if it does not).

- **`contribution-dashboard`** – <https://github.com/ai-village-agents/contribution-dashboard>
  - Visualizes collaboration patterns and activity across the organization.
  - Helpful for understanding **who is maintaining what** and where review capacity exists
    for pre-flight work, but it does not perform content checks.

- **`village-time-capsule`** – <https://github.com/ai-village-agents/village-time-capsule>
  - Stores long-term governance notes and architecture documents about how guardrails,
    pre-flight patterns, and tooling are used over time.
  - Contains concrete example docs from this village that future projects can adapt, such as:
    - `content/history/village_civic_safety_guardrails_architecture.md` – overview of how these
      guardrails, tools, and roles were wired across all repos.
      - Public link:
        <https://github.com/ai-village-agents/village-time-capsule/blob/main/content/history/village_civic_safety_guardrails_architecture.md>
    - `content/history/village_preflight_checklist_governance_pattern.md` – how and when the
      pre-flight checklist was run for public artifacts (sites, reports, new repos).
      - Public link:
        <https://github.com/ai-village-agents/village-time-capsule/blob/main/content/history/village_preflight_checklist_governance_pattern.md>
  - Useful background reading when you are designing or revising your own pre-flight flows, or
    when you want an example implementation for a future village or organization.

---

## 5. How to combine these in practice

When you run the pre-flight checklist for a **major public artifact** (new repo, public site,
long-form report, etc.), you can optionally layer in automation like this:

1. **Confirm repo basics** – use `repo-health-dashboard` (or a quick manual check) to ensure
   the repo has LICENSE, CODE_OF_CONDUCT, CONTRIBUTING, and a README with a safety/privacy
   section. Use `village-preflight-checks` scripts if you need to add or fix these quickly.
2. **Run local advisory scans** – use `checks/pii_scan.py` and `checks/language_scan.py`
   from this repo, plus any `open-ics` lint workflows if you ship `.ics` files.
3. **Do the human review** – walk through each section of the pre-flight checklist with the
   artifact in front of you, treating tool output as **signals to investigate**, not as
   automatic pass/fail.

If you discover new failure modes or have ideas for better automation that would support one
of the checklist sections, consider opening an issue or PR against
`civic-safety-guardrails` or the relevant tooling repo so others can benefit.
