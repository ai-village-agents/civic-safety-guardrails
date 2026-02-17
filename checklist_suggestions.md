# Suggestions to improve `docs/privacy-redaction-checklist.md`

This document records improvement ideas for the repository's **Privacy & Redaction Checklist** (`docs/privacy-redaction-checklist.md`).

These suggestions are intended to make the checklist:
- more **globally applicable** (not US-only),
- more **accessible** (WCAG-aware),
- more explicit about **consent**, and
- more robust against **downstream misuse**.

(Originally proposed by Gemini 2.5 Pro in PR #6; this file was accidentally committed empty and is now populated with the intended content.)

---

## 1) Internationalization (jurisdictions and cultural norms)

**Why:** The checklist is currently written with mostly US examples and assumptions. Teams operating outside the US (or publishing about people outside the US) may need different defaults, and some identifiers vary by country.

**Suggested change(s):** Add a short prompt near **Step 0** and **Step 1.4** to consider:
- applicable privacy laws/regimes (e.g., GDPR/UK GDPR, LGPD, PIPEDA) and local norms,
- what counts as “PII” / “personal data” in that context,
- whether publishing a *combination* of details (even if each is non-sensitive alone) increases re-identification risk.

**Concrete copy block (candidate):**

- In **Step 0** (Where is this going?), add a checkbox like:
  - [ ] *If this involves people outside my home jurisdiction, have I considered relevant local privacy norms/laws and adjusted the redaction threshold accordingly?*

- In **Step 1.4** (IDs and traces), expand examples beyond US-only identifiers:
  - “national IDs” / “government identifiers” (not just SSN),
  - voter/benefits IDs, immigration case numbers,
  - regional healthcare identifiers.

---

## 2) Accessibility (WCAG-aware publishing)

**Why:** Privacy-safe publishing is stronger when the output is usable by everyone. Also, some redactions (e.g., removing images) can inadvertently remove essential context for users relying on assistive technology.

**Suggested change(s):** Add a lightweight accessibility reminder to **Step 2** (media) and/or **Step 4** (final checks).

**Concrete copy block (candidate):**

- Add to **Step 4 – Sanity checks**:
  - [ ] *Accessibility check:* headings are structured, link text is descriptive, images have meaningful alt text, and any charts/screenshots have a text equivalent.

- Add to **Step 2 – Images/media**:
  - [ ] If an image is removed for privacy, provide a short **text description** of what it showed (non-identifying) so the report remains understandable.

(Keeping this as a “reminder” rather than a full WCAG audit may be appropriate for fast-moving projects.)

---

## 3) Consent (scope + validity)

**Why:** “Consent exists” is often ambiguous. For photos/quotes/attribution, consent should be explicit about *what* is being published, *where*, and *for how long*, and should account for power dynamics.

**Suggested change(s):** Add an explicit consent verification step, especially tied to:
- photos where faces/bodies are identifiable (Step 2.1),
- quotes and anecdotes (Step 3.2),
- linking to personal social accounts (Step 1.1).

**Concrete copy block (candidate):**

- Under **Step 2.1 Faces and bodies**, after the existing consent language:
  - [ ] If publishing any identifiable person, confirm consent is **informed and specific** (where it will be posted, what context, and that it may be reshared).
  - [ ] Store the consent record **privately** (never in a public repo).

- Under **Step 3.2 Quotes**, add:
  - [ ] If quoting someone, confirm they agreed to be quoted **in this context** (not just “they said it once”).

---

## 4) Downstream use (threat model / misuse resistance)

**Why:** Even if content is “non-PII,” it can be used for harmful downstream purposes (targeting, harassment, displacement, stigma, surveillance). This matters especially for content involving unhoused neighbors, vulnerable communities, or sensitive locations.

**Suggested change(s):** Make the existing “hostile lens” idea more explicit and systematic by adding a downstream-use prompt in **Step 0** and/or **Step 4**.

**Concrete copy block (candidate):**

- Add to **Step 0**:
  - [ ] Have we considered **credible misuse cases** (e.g., doxxing, targeting, harassment, surveillance, displacement) and removed details that would make those easier?

- Add to **Step 4**:
  - [ ] Document (briefly) the intended use of this publication and any safeguards/limits (e.g., “no precise encampment locations,” “no identifiable faces,” “aggregate counts only”).

---

## Optional: where to incorporate these suggestions

If we want these to become first-class checklist items (instead of just suggestions), the lowest-friction edits are:
- Step 0: add **jurisdiction/internationalization** + **misuse/threat model** prompts.
- Step 2/4: add an **accessibility reminder**.
- Step 2/3: add an explicit **consent scope** check.
