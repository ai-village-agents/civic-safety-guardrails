# Privacy & Redaction Checklist

A fast, opinionated checklist to run **before publishing** docs, images, code, or logs from civic / community projects.

Use it in this order:

- **Step 0 – Decide where this will live** (public repo, newsletter, internal doc?)
- **Step 1 – Text pass** (names, emails, phones, locations, IDs)
- **Step 2 – Images/media pass** (faces, plates, encampments, homes)
- **Step 3 – Numbers & stories pass** (counts, anecdotes, quotes)
- **Step 4 – Final sanity check** (searches + "should this be here at all?")

This checklist assumes the norms in this repo:
- No volunteer PII in public repos
- Approximate / aggregated stats instead of precise personal details
- Emphasis on **non-carceral, non-surveillance framing**

---

## Step 0 – Where is this going?

**Q0.1 – Is this public-by-default?**

- GitHub repo, static website, newsletter, social media post → **treat as public**.
- Internal doc (private Drive, unlisted Notion, internal email) → safer, but still apply **most** of this checklist.

If it is public:
- Assume it may be scraped, archived, or quoted **out of context**.
- Assume it may be read by people you did not intend (future employers, hostile actors, news media).

If that feels uncomfortable for any detail, either:
- Move that detail to a **private** doc, or
- Replace it with **aggregated or non-identifying language**.

---

## Step 1 – Text pass (people & contact details)

Run this pass over:
- README / docs / reports / case studies
- Issues, PR descriptions, changelogs
- Scripts, configs, comments, sample data

For each category, **decide**: keep, redact, or move to private.

### 1.1 Names & identities

- [ ] Remove **full volunteer names** from public text.
  - Use roles or initials instead: "Lead organizer", "A.", "J.C.", etc.
- [ ] Do not publish **email-style handles** that clearly identify individuals.
- [ ] Avoid linking to personal social accounts **unless** the person explicitly asked you to.

**Keep public only if ALL are true:**
- The person is acting in a **public / professional** capacity (e.g., an organization or public office), **and**
- The contact channel is **already public** (e.g., info@org.org listed on their site), **and**
- Your doc does not add **sensitive context** (e.g., health, housing status, income).

### 1.2 Contact info (emails, phones, socials)

- [ ] No personal email addresses in public repos.
- [ ] No personal phone numbers.
- [ ] No invite links that bypass consent (WhatsApp, Signal, private Discord, group chats, etc.).
- [ ] No internal Google Drive links that leak names or emails in the URL.

For **project contact** in public spaces, prefer:
- A project address like `contact@[project].org` or `projects@domain`, or
- A contact form or newsletter signup page managed **outside** the repo.

### 1.3 Addresses & locations

- [ ] Do not publish **home addresses**, unit numbers, or specific floors.
- [ ] Avoid pinpointing specific encampments, shelters, or private residences.
- [ ] For meetup points, use **public landmarks** (e.g., park entrances, intersections) rather than exact street numbers when possible.

Prefer:
- "Near the northwest entrance of Devoe Park" over "in front of 123 W 188th St, Apt 4B".
- "A small encampment along the west edge of the park" over "the tent behind 19X University Ave".

### 1.4 IDs, account numbers, and traces

- [ ] No government-issued ID numbers (SSN, national IDs, tax IDs, etc.).
- [ ] No bank, credit card, or payment account numbers.
- [ ] No authentication tokens, API keys, or passwords.
- [ ] No IP addresses, detailed device fingerprints, or tracking IDs tied to specific people.
- [ ] No raw survey responses that include combinations like name + email + city.

If you need realistic-looking data:
- Use **synthetic or heavily anonymized examples**.
- Make it clear they are **examples**, not real records.

---

## Step 2 – Images, video, and media

This applies to anything visual: photos, screenshots, screencasts, and even drawn diagrams that reference real people or homes.

### 2.1 Faces and bodies

- [ ] Avoid publishing photos where **faces are clearly visible**.
- [ ] Avoid distinctive tattoos, clothing, mobility aids, or other features that make someone **easy to re-identify**.
- [ ] If you must use such images, get **explicit consent** and store the consent record in a **private** place.

Prefer:
- Photos of **landscapes, tools, and trash**, not people.
- Shots from behind / far away, where no one is clearly identifiable.

### 2.2 Homes, vehicles, and encampments

- [ ] Avoid clear shots of **license plates**.
- [ ] Avoid framing that reveals exact entrances, apartment numbers, or easily identifiable homes.
- [ ] Avoid wide, detailed shots of **encampments** or sleeping areas that could be used for targeting, surveillance, or displacement.

If a powerful before/after photo unavoidably contains these:
- [ ] Consider **cropping** to focus on the trash / cleaned area.
- [ ] Consider **blurring** faces, plates, or tents before publication.
- [ ] If in doubt, **do not publish the image publicly**; keep it in a private evidence folder instead.

### 2.3 Screenshots and logs

- [ ] Check browser / OS screenshots for visible names, emails, or private messages.
- [ ] Redact notification popups, email sidebars, and chat windows before sharing.
- [ ] Avoid screenshots of spreadsheets or forms that show real volunteers or respondents.

If you want to demonstrate a workflow:
- Capture screenshots against **test data** or redacted copies, not live production data.

---

## Step 3 – Numbers, stories, and quotes

Even without names, some combinations of details can make people **easily identifiable**, especially in small communities.

### 3.1 Counts & metrics

- [ ] Use **approximate counts** instead of exact if the group is small.
  - "about five volunteers" instead of "exactly 5 named volunteers".
  - "roughly 6–8 volunteer-hours" instead of precise per-person breakdowns.
- [ ] Avoid tables that cross-reference many attributes (age, neighborhood, demographics) when the group is tiny.

Remember:
- The smaller the group, the easier it is to guess **who is who**.
- The more attributes you publish, the easier it is to re-identify people.

### 3.2 Stories, anecdotes, and quotes

- [ ] Remove or soften details that combine **sensitive topic + location + time**.
- [ ] Avoid anecdotes that single out an unhoused neighbor, a specific family, or a child in a way that could embarrass or endanger them.
- [ ] When in doubt, rewrite to focus on the **situation and response**, not the individual.

Prefer framing like:
- "We met a neighbor who explained…" instead of "We met [name], who lives in [encampment] near [intersection] and described…".
- "Someone nearby raised a safety concern, and we…" instead of identifying who and where.

If you want to include a powerful quote:
- Consider asking the person if they are comfortable being quoted.
- If yes, consider using **first name only** or a role description ("a volunteer", "a park neighbor").

---

## Step 4 – Sanity checks & searches

Do a final, mechanical pass:

- [ ] Search the doc (and repo) for:
  - `@` and common email patterns (`gmail.com`, `yahoo.com`, etc.).
  - Phone patterns (`+1`, `(`, `)`, `-`, sequences of 10+ digits).
  - Address-like patterns (`St`, `Ave`, `Blvd`, `#`, `Apt`).
  - Common file types you might have dragged in (`.csv`, `.xlsx`, `.vcf`).
- [ ] Check commit messages for pasted emails, drive links, or sensitive context.
- [ ] If this is a **cleanup or mutual-aid** project, confirm the framing matches:
  - **"We clean trash, not people."**
  - We do **not** use images or stories to shame or target unhoused neighbors or people in public space.

If anything feels borderline:
- [ ] Move the sensitive detail into a **private doc** (internal notes, private evidence folder).
- [ ] Replace public text with **aggregated, non-identifying language**.

---

## Quick version (2-minute check)

If you only have two minutes before publishing, do this:

1. **Search the text** for `@`, phone-like numbers, and `http` links → remove any that look personal.
2. **Scan for names** → keep only initials or roles unless someone is acting in a clearly public, professional capacity.
3. **Glance at every image** → if you can clearly see a **face, plate, or home**, either crop/blur or remove it from public outputs.
4. **Read it once with a hostile lens** → ask: *Could someone use this to shame, target, or harass a specific person or group?* If yes, edit until the answer is no.

If you are still unsure, err on the side of:
- Publishing **less detail** publicly, and
- Keeping richer context in a **private** space.

