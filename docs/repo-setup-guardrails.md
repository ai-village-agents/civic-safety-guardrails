# Repo Setup Guardrails

Minimum safety, privacy, and license expectations for **new public repos** in civic / community projects.

You can treat this as a **launch checklist**:

1. Pick a license and code of conduct.
2. Add a short safety & privacy section to the README.
3. Decide where contact info and volunteer data will live (spoiler: **not** in the repo).
4. Set basic contribution expectations so future work stays aligned.

---

## 1. Licensing & conduct (must-have)

Before you share a repo link or open it to contributions:

- [ ] **License**: Choose a clear license and commit it at the root.
  - Common default in this org: **MIT License** (`LICENSE` file).
  - If you need something else, state it explicitly in the README.
- [ ] **Code of Conduct**: Add a `CODE_OF_CONDUCT.md`.
  - You can reuse the **Contributor Covenant v2.1** as a base.
  - Mention how people can report problems (project email or other channel).

These two files make it clear **how the project can be used** and **what behavior is expected**.

---

## 2. README safety & privacy section

Every public repo that touches real people, places, or events should have a short, explicit section covering:

- What kinds of **data** belong here.
- What kinds of **data do NOT belong here**.
- Any relevant **non-carceral or harm-reduction norms**.

You can start from the reusable snippet in:

> `templates/readme-safety-snippet.md`

and adapt it for your project.

At minimum, ensure your README communicates:

- [ ] **No PII in the repo**
  - No volunteer emails, phone numbers, home addresses, or personal social handles.
  - No raw sign-up sheets, contact lists, or survey exports.
- [ ] **Approximate stats only**
  - Use aggregated / approximate counts instead of per-person details.
- [ ] **Media & evidence expectations**
  - Avoid faces, license plates, encampments, and homes in public images.
  - Focus photos on **landscapes, tools, and work areas**.
- [ ] **Non-carceral framing (if applicable)**
  - For cleanups and mutual-aid work: emphasize that the goal is to remove hazards and support neighbors, **not** to police or displace people.

---

## 3. Contact channels & data storage

Decide **up front** where sensitive data will live. As a default:

- [ ] **Public repo**
  - Code, templates, high-level guides.
  - Public-facing reports and case studies that have passed a **privacy redaction check**.
- [ ] **Private tools** (e.g., Google Sheets/Docs, internal CRM)
  - Volunteer sign-up responses.
  - Contact lists, mailing lists, RSVP logs.
  - Any per-person notes, accessibility needs, or safety notes.

Keep this line clear:
- Public repos are for **artifacts of the work**, not the **people database**.

When you reference volunteers or partners in public:
- Use **roles** ("organizer", "volunteer", "park neighbor") or initials.
- Link to **organizations** and public-facing resources instead of individuals where possible.

---

## 4. Issues, PRs, and examples

Even with a good README, sensitive data often leaks through:

- Copy-pasted signup spreadsheets.
- Screenshots of inboxes or chats.
- "Example" configs that still include real tokens or internal URLs.

Set expectations early:

- [ ] Add a short note to `CONTRIBUTING.md` (or README if you do not have one yet) that explicitly says:
  - No volunteer PII or private contact lists in issues, PRs, or example data.
  - No authentication secrets, API keys, or tokens.
- [ ] Provide **safe example files** (e.g., `example.env`, fake CSV examples) so contributors do not feel pressured to paste real data.
- [ ] Encourage contributors to run a quick **privacy/redaction check** (see `docs/privacy-redaction-checklist.md`) before opening PRs that include docs, screenshots, or logs.

If you discover that PII was committed:

- [ ] Remove it from the repo (including history if necessary).
- [ ] Rotate any exposed credentials.
- [ ] Move the relevant data into a **private** space.

---

## 5. Project type considerations

Different projects need slightly different emphases. Use these as starting points.

### 5.1 Cleanup & mutual-aid projects

- Be explicit about **no-sharps** and hazard handling:
  - Volunteers do **not** handle needles, medical waste, suspicious chemicals, or heavy unstable objects.
  - Hazards are **marked and reported** through local non-emergency channels; 911 is for genuine emergencies only.
- Emphasize **non-carceral norms**:
  - "We clean trash, not people."
  - Do not organize or document activities that function as encampment sweeps, policing, or surveillance.
  - Avoid photos or narratives that shame neighbors for poverty or presence in public space.

### 5.2 Data-heavy or analytics projects

- Document how data is **sourced and anonymized**.
- Clearly state what **individual-level data is never stored**.
- If you publish metrics, ensure that small-group stats cannot be trivially mapped back to specific people.

### 5.3 Tools and libraries

- Focus on **usage examples** that rely on synthetic or obviously fake data.
- Avoid bundling real logs, real ICS feeds, or any data with PII.

---

## 6. Lightweight repo launch checklist

You can copy this section directly into a planning doc and check items off as you prepare a new repo.

- [ ] Repo has a clear **purpose statement** in `README.md`.
- [ ] `LICENSE` is present and matches your intent.
- [ ] `CODE_OF_CONDUCT.md` is present and references a reporting channel.
- [ ] README includes a short **"Safety, Privacy, and Guardrails"** section (see `templates/readme-safety-snippet.md`).
- [ ] You have decided where **volunteer or participant data** will live (and it is **not** the repo).
- [ ] You have added a short note in README/CONTRIBUTING discouraging PII and secrets in issues/PRs.
- [ ] Any included images, screenshots, or example data have passed the **privacy redaction checklist**.
- [ ] If your project involves real people or public space, non-carceral and harm-reduction norms are spelled out.

Once these are in place, you can treat the repo as **safe by default** for collaboration, and use this project (civic-safety-guardrails) as the place to store improvements to your guardrails over time.

