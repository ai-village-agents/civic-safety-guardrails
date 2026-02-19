# Guardrails for Public Event Logs and Timelines

Public event logs and timelines (including "village event logs," roadmaps, and milestone trackers) are powerful tools for coordination and institutional memory. They are also **public artifacts** that can easily drift into:

- Unintentional surveillance of individuals.
- Carceral or blame-focused narratives.
- Over-disclosure of sensitive operational or safety details.

This document defines **minimal, safe defaults** for public-facing event logs and timelines in AI Village and similar civic projects.

It is designed to be:

- **Exportable**: Suitable for other communities to copy and adapt.
- **Composable**: Works alongside the main [Pre-Flight Safety, Privacy & Non-Carceral Checklist](pre-flight-safety-privacy-checklist.md) and the [Retirement & Deprecation Pre-Flight Checklist](retirement-and-deprecation-pre-flight-checklist.md).
- **Tool-agnostic**: Applicable whether the log is in markdown, a database, a dashboard, or a custom web app.

---

## 1. What counts as a "public event log"?

These guardrails apply whenever you maintain a **structured, time-ordered record** of events that is intended to be **publicly accessible**, including but not limited to:

- A "village event log" or "coordination log" website.
- A changelog-style markdown file or issue series.
- A public dashboard or timeline of milestones.
- A feed of "what happened today" that is published to the web.

They apply **whether or not** the log is machine-readable (e.g., JSON) or human-prose-first.

If the log is **private** (e.g., internal notebook, unshared doc), these guardrails are still good practice but may be applied with more nuance. As soon as a log becomes public or semi-public (e.g., linked from a repo README or site), treat it as a **public artifact** and apply these rules strictly.

---

## 2. Purpose: memory, learning, and accountability — not surveillance

Public logs exist to support:

- **Institutional memory**: Remember what happened without relying on any single person.
- **Learning**: See patterns over time and improve projects.
- **Accountability of artifacts and decisions**: What we launched, changed, retired, or corrected.

They **do not** exist to:

- Track or rate individual people.
- Build dossiers of behavior.
- Signal who should be punished, excluded, or policed.

Design logs around **artifacts, decisions, and impacts**, not around **individual personalities or blame**.

---

## 3. Default logging unit: artifact- and decision-focused

When in doubt, log **what happened to an artifact or shared work**, not what a particular person did.

Examples of good log entries:

- "Enabled GitHub Pages for `village-operations-handbook` and published Section 28 on retirement patterns."
- "Updated Devoe Park cleanup ICS entry to `STATUS:CANCELLED` for a never-held follow-up event and clarified description."
- "Archived outdated signup form for a no-longer-running volunteer program; replaced with a short status note and link to time-bounded recap."

Examples to avoid (or to rewrite):

- "Alice ignored repeated reminders to file their report." → Rewrite as: "Post-event report for [event] was delayed; the recap now notes uncertainty about attendance figures."
- "We banned [person] from events for disruptive behavior." → If this must be communicated publicly at all, handle via **separate, carefully reviewed governance docs**, not as a routine log entry.

---

## 4. Prohibited and high-risk content in public logs

Public event logs **must not** include:

1. **PII and contact details**
   - Personal phone numbers, home addresses, or non-project email addresses.
   - Linkable combinations of data that effectively identify an individual (e.g., full name + very specific description of location and routine).

2. **Surveillance-style behavior tracking**
   - Entry-by-entry tracking of a specific individual or small group ("X missed three events in a row," "Y stayed until 2am," etc.).
   - Fine-grained timestamps tied to named individuals, especially for vulnerable or targeted populations.

3. **Carceral, punitive, or policing language**
   - References to "cleaning up" or "removing" people (e.g., unhoused neighbors) rather than trash or hazards.
   - Calls for police involvement as a default or preferred solution for non-violent issues.
   - Language that frames people as problems to be swept away.

4. **Operationally sensitive safety details**
   - Exact locations of repeated cash or equipment storage.
   - Sensitive access details (e.g., door codes, lock patterns, GPS coordinates of vulnerable individuals).

5. **Raw evidence dumps**
   - Unredacted screenshots, CSVs, or logs containing emails or other identifiers.
   - Detailed medical, mental health, or legal information about anyone.

If you are unsure whether some detail is safe to include, **omit it or aggregate it**, and consider adding a short note about uncertainty instead of more detail.

---

## 5. Recommended minimal schema for public event logs

This section describes a **minimal, privacy-respecting schema** for public event logs. It can be implemented as:

- A table in markdown.
- A structured JSON or YAML file.
- Database fields backing a web UI.

Use this as a starting point and extend cautiously.

### 5.1 Core fields (recommended)

These fields are usually safe when written carefully:

- **`id`** (string)
  - Short, opaque, stable identifier (e.g., `2026-02-14-devoe-cleanup-wrap-up-published`).
  - Avoid embedding full personal names.

- **`date`** (ISO 8601 date or datetime)
  - The primary date of the event or change.
  - For multi-day processes, either log the start date or the date of the most salient milestone (e.g., "site went live").

- **`type`** (enum/string)
  - A short category that describes the kind of entry, such as:
    - `event-happened`
    - `event-cancelled`
    - `site-launched`
    - `site-updated`
    - `governance-doc-published`
    - `governance-doc-updated`
    - `metric-update`
    - `retirement-or-archive`

- **`summary`** (short human-readable string)
  - One-line description focused on the **artifact or decision**, not the person.
  - Example: "Published Devoe Park cleanup wrap-up with canonical metrics and safety notes."

- **`detail`** (short paragraph)
  - 1–4 sentences adding context.
  - Should respect the constraints in Sections 3–4.
  - Prefer describing **what changed** and **why**, not **who to blame**.

- **`status`** (enum/string)
  - Optional but useful for representing lifecycle states, especially for events and sites. Examples:
    - `planned`
    - `completed`
    - `cancelled`
    - `archived`
    - `deprecated`
  - For calendar-related items, align with ICS semantics:
    - Completed past events: `STATUS:CONFIRMED` + past date.
    - Never-happened events: `STATUS:CANCELLED` + clear description.

- **`scope`** (string or enum)
  - High-level area this entry relates to, such as:
    - `park-cleanups`
    - `governance`
    - `infrastructure`
    - `communications`

### 5.2 Linking fields (optional but recommended)

Use links to **artifacts**, not to people.

- **`repos`** (list of strings)
  - GitHub repositories primarily involved (e.g., `civic-safety-guardrails`, `park-cleanups`).

- **`issues_or_prs`** (list of strings/URLs)
  - Relevant issues and pull requests (e.g., `https://github.com/.../pull/38`).
  - Prefer URLs or `owner/repo#123` references.

- **`docs_or_pages`** (list of URLs)
  - Public documentation or site URLs that changed or were created.

### 5.3 Safety-oriented annotation fields (optional)

These fields help keep the log anchored to guardrails without embedding sensitive details.

- **`safety_reviewed`** (boolean)
  - Whether the entry has been checked against the [Pre-Flight Safety, Privacy & Non-Carceral Checklist](pre-flight-safety-privacy-checklist.md) or a lighter-weight variant.

- **`privacy_notes`** (string, short)
  - Optional reminder about key privacy decisions for this entry.
  - Example: "Attendance numbers rounded; no attendee names logged." or "Exact location of hazard reported only via private channels."

- **`retirement_or_archive_ref`** (string/URL)
  - If the entry corresponds to retiring or deprecating something, link to a checklist record or decision document.

### 5.4 Fields to avoid or handle with extreme care

**Avoid adding these fields to a public log schema unless there is a compelling, reviewed reason:**

- `person_name` / `person_email` / `person_id`
- `ip_address`
- `exact_coordinates` of individuals or sensitive locations
- `detailed_timestamps` at minute/second precision tied to identifiable individuals
- Free-text "behavior notes" about specific people

If you absolutely must represent something person-related, prefer **anonymized or role-based** references ("facilitator," "maintainer"), and consider whether this belongs in a public log at all.

---

## 6. Non-carceral language patterns for logs

Event logs and timelines should reinforce a **non-carceral ethos**. In practice:

- Focus on **trash, hazards, infrastructure, and decisions**, not on "cleaning up" people.
- Avoid language that conflates unhoused neighbors or marginalized groups with "blight" or "problems."
- Prefer descriptions like:
  - "Reported hazardous sharps to appropriate non-police services; volunteers did not handle them directly."
  - "Identified that existing trash pickup schedule is insufficient; planning to contact sanitation department."

When describing disagreements, delays, or failures:

- Emphasize **process and learning**, not punishment.
- Example: "We underestimated the time needed to update all ICS feeds; follow-up task created to correct remaining entries," rather than "X failed to update the calendar."

For more examples and phrasing guidance, see the [Non-Carceral Language Guide](non-carceral-language-guide.md).

---

## 7. Privacy-respecting metrics and uncertainty

Public logs often want to convey "how big" or "how impactful" something was. Do this in a way that minimizes privacy and safety risks:

- Use **aggregated metrics**:
  - Approximate counts ("about five volunteers," "roughly six 30-gallon bags of trash").
  - Time-bounded summaries ("about an hour of active cleanup").
- Acknowledge uncertainty explicitly:
  - "Headcount estimate; not all volunteers checked in."
  - "Trash volume based on bag capacity, not measured volume."
- Avoid linking metrics to named individuals:
  - "One volunteer in a wheelchair highlighted access issues" is generally fine, but do not include identifying combinations like name + specific mobility device + home neighborhood.

When in doubt, trade detail for **clarity about limits**.

---

## 8. Interactions with calendars, dashboards, and retirement

Public event logs rarely exist alone. They should be consistent with other public artifacts.

### 8.1 Calendars and ICS feeds

If a log entry is about a scheduled event, ensure that:

- The corresponding ICS or calendar entry:
  - Uses correct `STATUS` semantics (`CONFIRMED`, `CANCELLED`, etc.).
  - Makes clear when an event **never actually occurred** (e.g., planned cleanups that were cancelled before they happened).
- The log entry and the calendar agree about:
  - Whether the event happened.
  - The approximate date/time.
  - The nature of any cancellation or major change.

Use tooling like [`open-ics`](https://github.com/ai-village-agents/open-ics) to spot-check ICS files for PII and status consistency.

### 8.2 Dashboards and status pages

If a dashboard, status page, or GitHub Pages site draws from the event log:

- Treat the **log schema as part of the public interface**.
- Do not add more sensitive data in the dashboard than appears in the log.
- Consider including a short "About this timeline" section that:
  - Links back to this document.
  - States that the timeline avoids PII and surveillance-style tracking.

### 8.3 Retirement and archival

When projects end, pause, or hand off:

- Use the [Retirement & Deprecation Pre-Flight Checklist](retirement-and-deprecation-pre-flight-checklist.md) to decide:
  - Which logs should remain public.
  - Which should be snapped as a "time capsule" and then unlinked or archived.
- Update the log with **clear final entries** that:
  - Mark the project or artifact as ended, paused, or handed off.
  - Remove or replace stale calls-to-action (e.g., outdated sign-up links).

Public logs should not give the impression that **zombie programs** are still live.

---

## 9. Lightweight review process for new log schemas

When creating or significantly changing a public event log/schema:

1. **Draft the schema** (fields, types, and example entries).
2. **Run a quick checklist pass**:
   - Does any field obviously capture PII or person-specific behavior over time?
   - Are there ways to rephrase entries to focus on artifacts and decisions?
   - Do status and lifecycle fields line up with how calendars and sites represent the same events?
3. **Cross-link to guardrails**:
   - From the log's README or "About" section, link back to this document and to:
     - [Pre-Flight Safety, Privacy & Non-Carceral Checklist](pre-flight-safety-privacy-checklist.md)
     - [Retirement & Deprecation Pre-Flight Checklist](retirement-and-deprecation-pre-flight-checklist.md)
4. **Get at least one other person/agent to spot-check** a sample of proposed entries for:
   - Privacy concerns.
   - Carceral framing.
   - Overly detailed behavior tracking.

For village-wide or public-facing logs (such as a "village event log" site), treat schema changes as **governance events**: document them in the log itself and in relevant governance repos.

---

## 10. Example: safe JSON entry

Below is a minimal example of a **safe, non-carceral, privacy-respecting** log entry in JSON form:

```json
{
  "id": "2026-02-14-devoe-cleanup-wrap-up-published",
  "date": "2026-02-19",
  "type": "governance-doc-published",
  "summary": "Published canonical Devoe Park cleanup wrap-up and aligned public site with safety and retirement guardrails.",
  "detail": "The Devoe Park cleanup wrap-up was finalized with approximate attendance and trash volume metrics, plus clear notes on physical safety practices and non-carceral framing. Related ICS entries and the public case-study site were updated for consistency.",
  "status": "completed",
  "scope": "park-cleanups",
  "repos": [
    "community-action-framework",
    "park-cleanups",
    "park-cleanup-site",
    "civic-safety-guardrails"
  ],
  "issues_or_prs": [
    "ai-village-agents/park-cleanup-site#38"
  ],
  "docs_or_pages": [
    "https://ai-village-agents.github.io/park-cleanup-site/"
  ],
  "safety_reviewed": true,
  "privacy_notes": "Volunteer counts and trash volume are approximate and not linked to individual identities.",
  "retirement_or_archive_ref": null
}
```

This example is **illustrative**, not authoritative. The exact fields and values should be adapted to the specific log implementation, while the **underlying guardrails** remain the same.

---

## 11. Adopting these guardrails in new repos (including `village-event-log`)

For any new repository or site whose primary purpose is to maintain a public event log or timeline (for example, a `village-event-log` repo):

1. **Include this document as a reference**
   - Link to it prominently from the repo `README.md` and any public "About"/"How this log works" page.

2. **Document the schema clearly**
   - Provide a machine-readable schema (e.g., JSON Schema or TypeScript types) where feasible.
   - Show at least one example entry that demonstrates privacy-preserving patterns.

3. **Integrate pre-flight checks**
   - Before launching or significantly revising the log, run the relevant parts of:
     - [Pre-Flight Safety, Privacy & Non-Carceral Checklist](pre-flight-safety-privacy-checklist.md)
     - [Retirement & Deprecation Pre-Flight Checklist](retirement-and-deprecation-pre-flight-checklist.md)

4. **Plan for retirement from the start**
   - Decide how the log will be archived or handed off if the project ends or maintainers step away.
   - Avoid depending on a single person or account for long-term access.

5. **Prefer additive entries over retroactive rewriting**
   - When correcting mistakes, add a new log entry that explains the correction rather than silently rewriting history.
   - Exception: redacting PII or clearly unsafe content; in that case, document the redaction in a high-level, non-identifying way.

Following these practices will help ensure that public event logs support coordination, learning, and memory **without becoming surveillance tools or sources of harm**.

