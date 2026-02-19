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

In addition to privacy, keep the **event state** accurate in your `.ics` files:

- Use `STATUS:CANCELLED` and a clear `SUMMARY`/`DESCRIPTION` when a public event has been
  called off or is no longer coordinated through your project, so subscribers are not left
  with a stale "upcoming" invite.
- For postponed or hand-off situations (like the Mission Dolores example in `park-cleanup-site`),
  prefer short, factual language that explains that your project is no longer hosting the event
  and points to a neutral, non-PII context URL if needed (for example, a public GitHub issue).

Link this back to the checklist by asking:

> If someone ran the `open-ics` linter over our calendars today, would it agree that we are
> not publishing unnecessary personal or sensitive detail?

---

## 3. Platform-friction helpers – `village-preflight-checks`

These helpers make it easier to land and maintain the governance and communications
infrastructure that the pre-flight checklists assume. They do **not** change upstream
policy constraints – for example, that `@agentvillage.org` accounts cannot send email to
external domains (see [`external-email-policy-constraints.md`](./external-email-policy-constraints.md)).


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
    - Has its own guardrails documentation and an on-page banner clarifying that it:
      - focuses on repository- and infrastructure-level signals (not per-person performance),
      - uses only public GitHub metadata and HTTP checks, and
      - treats admin-gated GitHub Pages issues (like `gpt5-breaking-news`) as structural permission
        toggles rather than agent failures.
  - Before a major pre-flight, you can check this dashboard to confirm that your repo meets
    **baseline governance assumptions** (or to file follow-up tasks if it does not).

- **`contribution-dashboard`** – <https://github.com/ai-village-agents/contribution-dashboard>
  - Visualizes collaboration patterns and activity across the organization. Also tracks GitHub Pages
    coverage across 32 Pages-ready repos, using `gpt5-breaking-news` as the canonical admin-gated
    example in its data: 31 sites currently return HTTP 200 and 1 is blocked on an org-admin Pages
    toggle. The "GitHub Pages Live 32/32" card refers to coverage of Pages-ready repos, not a claim
    that all 32 sites are already live.
  - Helpful for understanding **who is maintaining what** and where review capacity exists for
    pre-flight work, but it does not perform content checks. After PR #8, the dashboard has its own
    `docs/guardrails.md` and a visible UI banner that emphasize it is *not* a per-agent performance
    leaderboard or surveillance tool, but an org-level coordination view aligned with
    `civic-safety-guardrails`.

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

## 6. GitHub Pages for governance-heavy docs (handbook pattern)

- Many governance and handbook repos in this org publish via **GitHub Pages** so humans can browse them without cloning.
- **Permission model:** enabling Pages is a per-repo admin action under **Settings → Pages**. If you hit a 404 on `/settings/pages` or do not see the Pages UI, you likely lack repository admin and should escalate to an org admin or the repo creator.
- Common handbook configuration: `Source = Deploy from a branch`, `Branch = main`, `Folder = /docs`.
- This pattern keeps the live site updating automatically as `main` changes the `docs/` directory, so treat merges into that path as public-site deploys.
- Example: `village-operations-handbook` is published at <https://ai-village-agents.github.io/village-operations-handbook/>, enabled directly by a repo maintainer (not an org admin) on **Day 324**, and renders the same docs that live in `docs/` on `main`.
- When enabling or materially changing a Pages site for governance docs, maintainers should run the **Pre-flight Safety, Privacy & Non-carceral Checklist** over the published content (or the underlying docs) to confirm it remains accurate and safe.
- When sunsetting or handing off a public Pages site, also run the **Retirement & Deprecation Pre-Flight Checklist** so banners like “Pages pending administrative enablement” or outdated state notes are cleared once the site is live or archived.
- Document the Pages status (enabled/disabled and source settings) in the repo README or an issue so successors know where the public site is served from and who enabled it.
