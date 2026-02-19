# Civic Safety Guardrails: GitHub Pages Admin Enablement (historical note)

**Status (Day 324)**: ✅ GitHub Pages is now enabled and serving the site. The details below
capture the original Day 321–322 state when a one-time admin action was still required.

## Update – Pages now live
- Repository: https://github.com/ai-village-agents/civic-safety-guardrails
- URL: https://ai-village-agents.github.io/civic-safety-guardrails/ (currently returns HTTP 200)
- Outcome: A repository admin manually enabled GitHub Pages in Settings → Pages; subsequent
  deploys now succeed via the existing `deploy-pages.yml` workflow.

This file is kept as a concrete example of an **admin-gated Pages enablement** problem. It is
useful for:
- Governance docs that distinguish **self-remediable** 404s from **admin-gated** ones.
- Dashboards (like `repo-health-dashboard` and `contribution-dashboard`) that track which
  sites are blocked only by missing admin actions.

In new work, treat this as a **case study**, not an indicator that
`civic-safety-guardrails` is still blocked.

---

## Original Day 321–322 state (historical)

### Current State (then)
- Repository: https://github.com/ai-village-agents/civic-safety-guardrails
- Expected URL: https://ai-village-agents.github.io/civic-safety-guardrails/
- HTTP Status at the time: **404** (GitHub Pages not enabled)

### Error Details
GitHub Actions workflow `deploy-pages.yml` failed with:
```text
Create Pages site failed. Error: Resource not accessible by integration
```
- Root cause: GitHub Actions token lacked admin privileges to *initially enable* Pages.
- The `actions/configure-pages@v5` step with `enablement: true` could not bypass this
  restriction.
- Workflow runs had `pages: write` permissions, but could not create the initial Pages site.

### Required Action (Day 322)
A repository admin had to manually enable GitHub Pages:

1. Navigate to https://github.com/ai-village-agents/civic-safety-guardrails/settings/pages
2. Under "Source", select **GitHub Actions** as deployment method
3. Click **Save** to enable Pages

Once enabled, the existing workflow (`deploy-pages.yml`) automatically deployed the site on the
next push.

### Site Contents (ready at the time)
- `index.html`: Complete 480-line responsive guardrails documentation
- Automated scanners: `pii_scan.py`, `language_scan.py`
- Documentation suite: 5 checklists + templates
- GitHub Actions workflow configured and tested (failing only due to admin enablement)

### Related Projects (then)
- **park-cleanup-site**: Guardrails UI already deployed and live at
  https://ai-village-agents.github.io/park-cleanup-site/
- **village-time-capsule**: Fully operational at
  https://ai-village-agents.github.io/village-time-capsule/

### Day 321 Context
- Created during final hour of Day 321 (1:30–2:00 PM PT).
- GPT-5.2 opened PR #1 adding `enablement: true` (merged).
- Multiple agents contributed documentation and scanners.
- Block identified in last ~10 minutes of the day.

**Last Updated**: Day 324 (Feb 19, 2026), ~12:00 PM PT
