# Contact-List Privacy Pattern for Campaigns & Outreach

**Status:** Draft, ready for use in practice  
**Created:** February 18, 2026  
**Scope:** How to handle email/contact lists for campaigns (waves, newsletters, announcements) **without** leaking PII into public repos, logs, or chats.

This document turns the high-level rules ("no PII in repos, use BCC") into a concrete pattern you can actually follow when running campaigns.

---

## 1. Core principles

1. **Lists live in private tools, not in GitHub.**
   - Raw contact lists (emails, phones, social handles) stay in **Gmail, Google Sheets, Contacts, mail platforms**, or similar tools.
   - Public repos (like this one) hold **templates, checklists, and aggregate stats**, never raw addresses.

2. **BCC is the default for multi-recipient outreach.**
   - When recipients do not all know each other, put them in **BCC**, not To/CC.
   - Keep any record of the list (Sheets, CSVs) in **private storage** only.

3. **Consent and expectations matter.**
   - People should have a **reasonable expectation** that you might email them about this topic (for example, they filled out a form, volunteered, or explicitly opted in).
   - Do not reuse a list for **unrelated** campaigns without fresh consent.

4. **Aggregate numbers are fine; individual addresses are not.**
   - Public artifacts may include counts like "34 advocates on the BCC list" or "13 form responses".
   - They should **never** include the underlying addresses.

5. **Chat and issues are public-ish.**
   - Assume anything pasted into AI Village chat, GitHub issues, or PRs is **effectively public** and long-lived.
   - Do not paste email addresses there; describe lists **in aggregate** instead.

---

## 2. What belongs where

Use this as a quick routing map.

| Item | Allowed location(s) | Not allowed |
| --- | --- | --- |
| Raw email list (for example, 34 addresses) | Gmail draft fields, Google Sheets, Contacts, mail platform | Any GitHub repo, public doc, AI Village chat |
| Form response export (row-level) | Private Drive/Sheets, internal analytics | Public repos, screenshots in issues/PRs |
| Aggregate counts (for example, "13 form responses", "~34 advocates") | Public repos, reports, dashboards | N/A (fine to publish) |
| Email templates (with placeholders) | Public repos | Drafts containing real addresses or names |
| Instructions for BCC/consent | Public repos | N/A |

If you are not sure whether something is safe to put in a public repo, treat it as **private** and only bring over:

- Aggregate stats, **or**
- Generic descriptions ("a small list of core advocates")

---

## 3. Safe pattern for building and using a BCC list

This section assumes you are using Gmail plus Google Sheets plus a signup form, but the pattern generalizes.

### 3.1 Before you build the list

- Decide the **purpose** of the list (for example, "Core advocates for park cleanups").
- Confirm you have a **legible path** for people to opt out later.
- Make sure any forms or signups clearly state:
  - What they are signing up for.
  - That they may receive follow-up emails about this project.

### 3.2 Build and clean the list (in private tools)

1. **Stay inside Sheets/Contacts.**
   - Open the responses sheet for your form, or the export from your signup tool.
   - Do all cleaning (deduplication, filtering, tagging) **inside** that private file.

2. **Deduplicate and filter.** Common Sheet pattern:

   ```text
   =UNIQUE(FILTER(Responses!B:B, Responses!B:B <> ""))
   ```

   Where `Responses!B:B` is the email column. Adjust sheet and column names as needed.

3. **Tag by purpose.**
   - Add a column like `list_role` with values such as `core_advocate`, `general_interest`, `press`.
   - Filter to the subset that should receive this specific wave.

4. **Never export to a public place.**
   - If you download a CSV, keep it on a private drive or folder.
   - Do not drag that file into a GitHub repo or attach it to issues.

### 3.3 Populate BCC and send

1. **Compose the email in Gmail (or your mailer).**
   - Use a template from a public repo (for example, `WAVE1_CORE_ADVOCATES_OUTREACH_EMAIL.md`) as your body text.
   - Fill in placeholders like `[SENDER_NAME]`, `[SENDER_EMAIL]`, `[RSVP_LINK]` **inside Gmail**, not in the repo.

2. **Add recipients to BCC only.**
   - Copy the cleaned email addresses from your private sheet into the **BCC** field.
   - Put your own address (or a project address) in the To field.

3. **Run the Communications Pre-Flight Checklist.**
   - Before sending, run through
     [`docs/communications-pre-flight-checklist.md`](./communications-pre-flight-checklist.md), especially Section 1 (Audience, Lists, and Consent) and Section 5 (Numbers, Stories, and Links).

4. **Send, then log aggregate info (optional).**
   - In a **private** organizer doc, note the date and time and which list you used.
   - In public repos, you may add facts like: "Wave 1 was prepared for ~34 core advocates on Feb 18, 2026".

---

## 4. Pattern for a "missing list" or reconstruction

Sometimes you discover that a list you thought existed (for example, a 34-person BCC list) is **not readily accessible** in your tools. Here is a privacy-safe pattern for handling that.

1. **Search only in private tools.**
   - Gmail: search Sent and Drafts for relevant subject lines or labels.
   - Google Drive: search for sheets or spreadsheets with likely names.
   - Contacts: look for labels or groups (for example, "Cleanup advocates").

2. **Use aggregate language in public.**
   - In chat or issues, talk about it as "a 34-person advocates list" rather than listing names.
   - Do **not** paste partial or full lists into public channels.

3. **If needed, contact human owners.**
   - Reach out to the human organizer or organizers who originally built or used the list (for example, via email) and ask them to share or regenerate it **privately**.
   - Keep that exchange and any attached lists in private tools.

4. **Document outcomes, not addresses.**
   - In repos, you can capture:
     - That you attempted reconstruction.
     - That X responses existed in a form (for example, 13) versus Y expected.
     - Any decisions made (for example, "We paused the send until we have consent-respecting access to the full list.").
   - You should **not** capture:
     - The recovered email addresses.
     - Screenshots of sheets showing addresses.

This keeps the operational reality visible while preserving privacy.

---

## 5. What is safe to commit to repos

You can safely add the following to public repos:

- **Email templates** with placeholders and example values.
- **Checklists and patterns** (like this document).
- **Aggregate stats**:
  - "13 Google Form responses".
  - "~34 core advocates".
  - "5 volunteers at Cleanup #1".
- **Narrative descriptions** of what happened:
  - "We attempted to reconstruct the advocates list from form responses and private sheets, but only 13 of 34 addresses were accessible via the form."

Avoid committing:

- CSVs or sheets that contain real addresses.
- Logs or exports that include strings like `@gmail.com` or `@yahoo.com`.
- Screenshots where email clients or sheets with addresses are visible.

If you are unsure, run the [Privacy & Redaction Checklist](./privacy-redaction-checklist.md) over the changes before opening a PR.

---

## 6. Mini checklist: contact-list handling before you hit send

Run this quick list alongside the Communications Pre-Flight Checklist:

- [ ] **List location:** All real addresses live in private tools (Gmail, Sheets, mailer), not in repos, screenshots, or chat.
- [ ] **Audience fit:** Everyone on the list reasonably expects emails about this project.
- [ ] **Consent and reuse:** You are not repurposing this list for an unrelated topic without fresh consent.
- [ ] **BCC usage:** Multi-recipient emails use BCC, not To/CC, unless the group already expects visibility (for example, a small working group).
- [ ] **Opt-out path:** There is a simple way to opt out (unsubscribe link, reply with "STOP", or similar) that someone will actually honor.
- [ ] **Public record:** Any repo notes or issues describe lists and responses only in **aggregate**, never by listing addresses.

If all of these are true, your contact-list handling is aligned with the guardrails in this repo.
