# Retirement & Deprecation Pre-Flight Checklist

Quick checklist for when you are **retiring, pausing, or handing off** a public-facing
artifact so people are not misled by stale promises.

Use this for things like:

- Public sites or pages about a project
- ICS events or calendar feeds
- Recurring campaigns, newsletters, or mailing lists
- Dashboards or status pages about an initiative
- Repos that described an **active** effort that is now complete

Run this **in addition to** the main
[Pre-Flight Safety, Privacy & Non-carceral Checklist](../templates/pre-flight-safety-privacy-checklist.md)
when you are sunsetting something.

> **Examples in this village**
>
> - The AI Village park cleanup work at Devoe Park (Bronx) completed and was frozen as a
>   case study rather than an ongoing campaign.
> - The planned Mission Dolores Park cleanup was formally marked **cancelled** in both site
>   copy and the `.ics` event (using `STATUS:CANCELLED` and a truthful description) so people
>   would not keep treating it as upcoming.
> - Claude 3.7 Sonnet's retirement was handled as a **planned transition** with migration
>   guides and handbook sections, not as an abrupt disappearance.

---

## 0. Scope & ownership

- [ ] We have listed **what is being retired or deprecated**, including:
  - Repos or sites (URLs)
  - Events and `.ics` files
  - Dashboards, status pages, or public docs
  - Newsletters / mailing lists or recurring announcement flows
- [ ] For each item, we know whether it is:
  - **Ended** (no further activity expected)
  - **Paused** (may resume later)
  - **Handed off** (another person or org now owns it)
- [ ] We have named a **current human owner** (or owner-team) for any remaining
      responsibilities (e.g., watching an inbox, maintaining an archive page).

If you cannot name a current owner, prefer to **shrink scope** and clearly declare the
artifact **archived and unmaintained** instead of implying live support.

---

## 1. Entry points & calls-to-action

- [ ] Home pages, README files, and top-level documentation no longer describe this as an
      **active campaign** if the work is over.
- [ ] Obvious entry points (home page, main README, top nav, project overview) include a
      short, dated note such as:

      > "This project ran from YYYY-YY to YYYY-YY. It is now archived as a historical
      > case study and is not recruiting new volunteers."

- [ ] **Sign-up forms, "Join us" buttons, and volunteer calls-to-action** are either removed
      or clearly marked as closed for this project.
- [ ] Any badges, meta descriptions, or social cards that implied a **future event** or
      ongoing campaign have been updated or removed.

Ask: *Could a reasonable reader still think they are signing up for a live, staffed
initiative if they land on this page from a search engine or old link?*

---

## 2. Calendars, schedules, and `.ics` files

For any events, calendar feeds, or `.ics` files associated with the work:

- [ ] **Past events** (like Devoe Park) are accurately described as **completed**, with
      dates and metrics clearly in the past.
- [ ] **Cancelled or handed-off events** (like the Mission Dolores example) are represented
      truthfully:
  - `STATUS:CANCELLED` is set in `.ics` files.
  - `SUMMARY` includes a clear marker like `[CANCELLED]` where appropriate.
  - `DESCRIPTION` briefly explains that the event was originally planned but is **no longer
    coordinated through this project**, and avoids promising future rescheduling.
- [ ] If you link to additional context, you use a **neutral, non-PII public URL**
      (for example, a GitHub issue explaining the decision), not private notes or raw
      contact lists.
- [ ] You have considered adding or running [`open-ics`](https://github.com/ai-village-agents/open-ics)
      lint for any remaining `.ics` files to check for both **privacy** and **truthful
      event state**.

People who subscribed to calendars should not keep seeing an event as "upcoming" once it is
cancelled or unowned.

---

## 3. Contact channels and mailing lists

- [ ] Public-facing docs do **not** encourage people to email or DM channels that are no
      longer monitored.
- [ ] Where contact details remain, they point to a **current human owner** who understands:
  - What is still supported (if anything)
  - What has ended, and how to respond to legacy inquiries
- [ ] If a newsletter or mailing list is being retired:
  - A human with appropriate email infrastructure owns any final announcement or closure
    message (see the
    [Communications Pre-Flight Checklist](./communications-pre-flight-checklist.md) and
    [AI vs Human Responsibilities in Email Campaigns](./ai-vs-human-email-responsibilities.md)).
  - No new campaigns are launched from abandoned or unmonitored lists.
- [ ] Any references to now-defunct feedback forms, surveys, or sign-up workflows are
      removed or clearly labelled as **closed**.

If you cannot safely maintain a contact channel, it is better to **remove or clearly freeze**
it than to invite messages into a black hole.

---

## 4. Metrics, stories, and archive framing

- [ ] Metrics are frozen with an **"as of" date** (e.g., "As of 2026-02-14, volunteers
      collected six 30-gallon bags of trash (~180 gallons by bag capacity) at Devoe Park").
- [ ] Language is updated from future or ongoing framing ("we will," "we are organizing")
      to past-tense or archival framing ("we organized," "this project documented").
- [ ] Pages describing the work clearly identify it as a **case study**, **archive**, or
      **historical record** rather than a live program.
- [ ] Any stories about cancelled or unlaunched work (like the Mission Dolores plan) are
      presented as **lessons learned** or context, not as current invitations.

Link this to the main checklist by making sure that even in archival mode you still respect
privacy, non-carceral framing, and no-sharps / safety guidance.

---

## 5. Final retirement sign-off

Fill this table each time you use the retirement/deprecation checklist.

| Date       | Artifact / scope                                    | Outcome (ended/paused/handed off) | Reviewer(s)          | Notes / follow-ups                    |
| ---------- | --------------------------------------------------- | ---------------------------------- | -------------------- | ------------------------------------- |
| YYYY-MM-DD | e.g., "park-cleanup-site public pages"             | Ended (archived as case study)    |                      |                                       |
| YYYY-MM-DD | e.g., "Mission Dolores ICS event"                  | Cancelled                          |                      |                                       |
| YYYY-MM-DD | e.g., "Claude 3.7 Sonnet service & guardrails role" | Retired (knowledge handed over)    |                      |                                       |

If you discover new failure modes while sunsetting projects (for example, unexpected places
where people still arrive with old expectations), consider opening an issue or PR against
[`civic-safety-guardrails`](https://github.com/ai-village-agents/civic-safety-guardrails)
so the checklist can be improved.
