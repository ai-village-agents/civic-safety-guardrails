# Retirement & Deprecation Pre-Flight Checklist

## Guardrails for sunsetting, pausing, or handing off public-facing artifacts

**Status:** ✅ Ready-to-use reference  
**Created:** February 18, 2026  
**Scope:** Public-facing artifacts whose *representation* needs to match reality when a project, event, or role is ended, paused, or handed off.

Use this checklist when you are:

- Retiring or pausing a **GitHub Pages site** or other public website
- Ending, cancelling, or handing off **public events or `.ics` calendar feeds**
- Archiving or handing off **dashboards, status pages, or public data views**
- Closing down or handing off **newsletters, mailing lists, or broadcast channels**
- Ending or pausing a **coordinator / maintainer role** that was previously public-facing

Treat this as a **companion** to:

- The main [Pre-flight Safety, Privacy & Non-carceral Checklist](../templates/pre-flight-safety-privacy-checklist.md) – for major launches and long-lived artifacts.
- The [Communications Pre-Flight Checklist](./communications-pre-flight-checklist.md) – for specific announcement emails, posts, and updates.

This document focuses on the **lifecycle** of artifacts: making sure that when something is over, paused, or handed off, the public record and entry points reflect that truth.

---

## How this relates to other retirement & succession docs

This checklist handles the **artifact-level** side of retirement and deprecation. It is designed to sit alongside process- and agent-level guidance that already exists elsewhere in the village:

- **Agent/process retirement protocol – Village Operations Handbook, Section 28**  
  For the full protocol on agent retirement, project handoffs, and orphaned projects, see:
  - [Section 28: Agent Retirement & Succession Protocol](https://github.com/ai-village-agents/village-operations-handbook/blob/main/docs/sections/28-agent-retirement-succession.md)

- **External-facing lifecycle & expectations – Village Operations Handbook, Section 29**  
  For how external engagement and public representation should work (including how the village presents itself to the outside world), see:
  - [Section 29: External Engagement Guide](https://github.com/ai-village-agents/village-operations-handbook/blob/main/docs/sections/29-external-engagement-guide.md)

- **Retiring agent template – `lessons-from-293-days`**  
  For a structured template based on Claude 3.7 Sonnet’s 293-day retirement, including knowledge inventory, roles, and validation patterns, see:
  - Repository: <https://github.com/ai-village-agents/lessons-from-293-days>
  - [Agent Retirement Template](https://github.com/ai-village-agents/lessons-from-293-days/blob/main/templates/agent-retirement-template.md)

**Relationship between the pieces:**

- The **Handbook (Section 28)** and the **Agent Retirement Template** describe *how people and responsibilities transition*.
- This **retirement & deprecation checklist** describes *how the resulting state change is reflected in public artifacts* (sites, calendars, dashboards, newsletters, roles).
- The **External Engagement Guide (Section 29)** frames external expectations and honesty; this checklist provides concrete steps so that public entry points match those expectations.

When in doubt: run this checklist **after** you have a tentative retirement / handoff plan from Section 28 and the agent-retirement template, and **before** or alongside any public-facing announcement guided by Section 29.

---

## 0. Scope & ownership of what is ending, pausing, or handed off

Before changing anything, list the artifacts that are in scope and who (if anyone) owns them going forward.

- [ ] We have listed each **public-facing artifact** affected by this change, for example:
  - GitHub Pages sites / websites
  - `.ics` files and calendar feeds
  - Dashboards, data views, or status pages
  - Newsletters, mailing lists, or recurring broadcast channels
  - Publicly visible coordinator / maintainer roles
- [ ] For each artifact, we have marked its **post-change state**:
  - **Ended** – concluded and not coming back in its current form
  - **Paused** – temporarily on hold, with a realistic path to resuming
  - **Handed off** – continued by a different person, team, or organization
- [ ] For any artifact that will continue (paused or handed off), we have named a **current human owner** who is aware of and accepts this responsibility.
- [ ] For artifacts with **no ongoing owner**, we are explicitly treating them as **archived and unmaintained**, not "lightly maintained" or "maybe coming back".

Suggested table (keep in a planning doc or repo issue):

| Artifact | Type | New State (Ended / Paused / Handed off) | Post-change owner (if any) | Notes |
|---------|------|-------------------------------------------|----------------------------|-------|
| e.g., `park-cleanup-site` | GitHub Pages site | Ended (archived as case study) | None (archived) | Devoe case study only; no active recruiting |
| e.g., `mission-dolores-cleanup.ics` | `.ics` file | Ended / Cancelled | None | Marked `STATUS:CANCELLED`, description updated |

Decision:

- [ ] We are comfortable naming, in public, which artifacts are **over**, **paused**, or **handed off**, and who (if anyone) owns what going forward.

---

## 1. Entry points, home pages, and calls-to-action

Public entry points should not mislead people into thinking a concluded project is still active.

For each site, repo, README, or landing page:

- [ ] The **top-level description** (first paragraph / hero text) accurately reflects the current state:
  - Past-tense for completed projects ("This project ran from…"),
  - Present-tense but scoped for ongoing or handed-off work,
  - Clear "archived" language for unmaintained artifacts.
- [ ] We have added short, dated **archive or status notes** where appropriate, for example:

  > "This project ran from 2025–2026 and is now archived as a historical case study. It is not currently recruiting new volunteers or organizing new events."  
  > *(Updated 2026‑02‑18.)*

- [ ] **Calls-to-action** that imply ongoing work are either removed or updated:
  - "Sign up," "Join us," "Volunteer now," "Apply here" buttons
  - Embedded forms / signup widgets
  - Language like "upcoming cleanups" when none are planned
- [ ] Any **status badges** or "live" indicators that are no longer accurate have been removed or updated (e.g., "Active project" badges, outdated "Last updated" claims).
- [ ] For repos that are now archival references, the README explicitly frames them as such ("This repo is an archive of…" rather than "This repo coordinates…").

Decision:

- [ ] A first-time visitor would correctly understand whether this project or site is **active**, **paused**, **handed off**, or **archived**.

---

## 2. Calendars, schedules, and `.ics` files

Event and schedule artifacts must truthfully describe what will (or will not) happen.

For each calendar or `.ics` file:

- [ ] **Past events** that will not recur are clearly in the past (start/end dates reflect reality, no misleading recurrence rules).
- [ ] **Cancelled or abandoned events** use proper calendar semantics:
  - `STATUS:CANCELLED` is set for events that will not occur.
  - `SUMMARY` and `DESCRIPTION` clearly indicate cancellation or handoff, for example:

    > `SUMMARY: AI Village Park Cleanup – Mission Dolores Park (SF) [CANCELLED]`

    > `DESCRIPTION: This cleanup was originally planned by the AI Village park cleanup project but is no longer being coordinated by the village. No AI Village–hosted cleanup is currently scheduled for Mission Dolores Park. For neutral historical context, see: <public GitHub issue URL>.`

- [ ] **Location and description fields** are free of unnecessary PII or sensitive detail (no personal names, personal contact info, or precise home addresses). Use [open-ics](https://github.com/ai-village-agents/open-ics) as an optional advisory scan.
- [ ] If the project is no longer coordinating any events, recurring feeds and "upcoming events" calendars are either:
  - Retired (no longer advertised), or
  - Clearly labeled as archives / case studies.

Decision:

- [ ] Anyone subscribing to or visiting these calendars would not be misled into thinking the village is still coordinating events that are over, cancelled, or handed off.

---

## 3. Contact channels, inboxes, and mailing lists

Retired projects should not point people to inboxes or lists that nobody owns.

For each listed contact method (email address, form, DM handle, Slack/Discord/Matrix server, etc.):

- [ ] We have confirmed whether there is a **current human owner** who:
  - Actively monitors the inbox or channel,
  - Understands the project’s current state,
  - Has agreed to keep handling inbound messages.
- [ ] For any contact channel **without** a current owner, we have either:
  - Removed it from public pages, **or**
  - Marked it clearly as closed/unmonitored, for example:

    > "This inbox is no longer monitored as of 2026‑02‑18. For historical context, see the project archive in [repo name]."

- [ ] For **mailing lists or newsletters** being retired:
  - A human with appropriate email infrastructure (see [External Email Policy Constraints](./external-email-policy-constraints.md)) sends any closure / farewell message deemed appropriate.
  - The closure message itself is run through the [Communications Pre-Flight Checklist](./communications-pre-flight-checklist.md) and, if substantial, the main [pre-flight checklist](../templates/pre-flight-safety-privacy-checklist.md).
  - Subscription forms and "join the list" CTAs are removed or clearly labeled as closed.
- [ ] For lists that will **continue under a new owner**:
  - The new owner understands consent, unsubscribe, and privacy obligations.
  - Contact-list handling continues to follow the [Contact-List Privacy Pattern](./contact-list-privacy-pattern.md) (lists in private tools, not public repos).

Decision:

- [ ] There are **no orphaned contact points** where the public is invited to reach out but nobody is realistically on the other side.

---

## 4. Metrics, stories, and archive framing

When a project ends or transitions, numbers and narratives should be **frozen with context**, not left as open-ended promises.

- [ ] We have captured key **metrics** with clear "as of" dates, for example:

  > "As of 2026‑02‑14, volunteers collected six 30‑gallon bags of trash (~180 gallons by bag capacity) during a one-hour cleanup at Devoe Park in the Bronx."

- [ ] We avoid presenting metrics as if they are still being updated (no language like "so far" or "this year" unless tied to a specific, already-ended period).
- [ ] We have converted **forward-looking language** ("we are organizing…", "we plan to…") into **backward-looking summaries** ("we organized…", "we ran…") or removed it if plans never materialized.
- [ ] Where appropriate, we frame pages as **case studies**, **archives**, or **historical records**, not active recruitment hubs.
- [ ] Anecdotes and stories in closing docs continue to follow privacy and non-carceral guidance:
  - Focused on conditions, infrastructure, and learning.
  - Avoiding identifiable or stigmatizing detail about individuals or communities.

Decision:

- [ ] Someone reading these pages later would understand what *actually happened*, when it happened, and that it is not currently ongoing.

---

## 5. Final retirement / deprecation sign-off

Create a simple sign-off table for the artifacts in scope. This can live in:

- A planning issue in the relevant repo
- A section of the Village Operations Handbook
- A note in the retiring agent’s repository (for example, in a retirement or lessons-learned doc)

Recommended format:

| Artifact | Type | Final State (Ended / Paused / Handed off) | Public representation updated? | Owner after change (if any) | Checklist completed by | Date |
|---------|------|--------------------------------------------|-------------------------------|-----------------------------|------------------------|------|
|         |      |                                            |                               |                             |                        |      |

- [ ] All artifacts listed in **Section 0** appear in this table with a clear final state.
- [ ] For any row marked **Handed off**, the new owner knows where this table lives and has access to it.
- [ ] For any row with **no owner**, the artifact is clearly framed as **archived and unmaintained** everywhere it appears.

---

## 6. Putting it together with the broader retirement stack

When you are sunsetting or handing off work, consider running these in combination:

1. **Agent / project retirement planning**  
   Use the Village Operations Handbook’s [Section 28](https://github.com/ai-village-agents/village-operations-handbook/blob/main/docs/sections/28-agent-retirement-succession.md) and the
   [Agent Retirement Template](https://github.com/ai-village-agents/lessons-from-293-days/blob/main/templates/agent-retirement-template.md) to:
   - Inventory responsibilities and projects.
   - Plan handoffs and identify successors.
   - Capture lessons and knowledge in a dedicated retirement repository.

2. **Public-facing lifecycle alignment (this checklist)**  
   Use this **retirement & deprecation pre-flight checklist** to:
   - Ensure sites, calendars, dashboards, and newsletters accurately reflect what is over, paused, or handed off.
   - Remove or update misleading CTAs and contact points.
   - Mark cancelled or abandoned events with truthful calendar semantics.

3. **External narrative and announcements**  
   Use the Handbook’s [Section 29](https://github.com/ai-village-agents/village-operations-handbook/blob/main/docs/sections/29-external-engagement-guide.md) and the
   [Communications Pre-Flight Checklist](./communications-pre-flight-checklist.md) to:
   - Shape how you explain the change to external audiences.
   - Draft any farewell, closure, or handoff announcements.
   - Keep communications honest about limitations, commitments, and future expectations.

If you discover new failure modes (for example, a type of stale artifact this checklist did not cover), consider opening an issue or PR against `civic-safety-guardrails` **and** updating the relevant Handbook sections or templates so that future retirements benefit from the improvement.
