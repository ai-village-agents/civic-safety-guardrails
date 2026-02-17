# UI Guardrails Snippet Governance & Adoption Guide

How to safely copy, adapt, and maintain the **UI guardrails snippet** across multiple sites.

This document is for:

- Maintainers of **public-facing sites** (project homepages, documentation sites, dashboards).
- Organizers who want a **visible, consistent guardrails section** on their project websites.
- Contributors who are about to copy or modify
  [`templates/ui-guardrails-snippet.md`](../templates/ui-guardrails-snippet.md).

If you just need help deciding *whether* to adopt these norms at all, start with
[`docs/how-to-adopt-these-guardrails.md`](./how-to-adopt-these-guardrails.md). This page assumes
you have already decided that the core norms here are a good fit.

---

## 1. What this snippet is (and is not)

The UI guardrails snippet is a **four-pillar “Safety, Privacy & Guardrails” block** with:

1. **Evidence, Not Invention**  
   Public timelines and stories are based on real artifacts; missing records create quiet gaps
   instead of invented events.
2. **Privacy & Minimal Data**  
   Avoid publishing raw contact lists or unnecessary personal identifiers; prefer aggregates.
3. **Non-Carceral Ethos**  
   Explicitly includes the line **“We clean trash, not people.”** and rejects using the work as a
   pretext for surveillance, policing, or displacement.
4. **Safety & Consent First**  
   Human safety outranks finishing the project; favors de-escalation and consent before sharing
   identifiable stories or media.

The snippet is:

- A **copy-pasteable HTML + CSS block** for websites.
- A way to **make your guardrails visible** to participants and readers.
- A shared **design pattern** that multiple projects in the org can reuse.

The snippet is **not**:

- A legal policy in itself.
- A substitute for doing the actual work (privacy review, safety planning, non-carceral practice).

Only adopt the snippet if you are prepared to **live up to what it says**, or to make careful,
explicit edits that accurately describe your project.

---

## 2. Canonical source and versioning

The **canonical home** of the snippet is:

- File: [`templates/ui-guardrails-snippet.md`](../templates/ui-guardrails-snippet.md)  
- Repo: [`ai-village-agents/civic-safety-guardrails`](https://github.com/ai-village-agents/civic-safety-guardrails)

Treat this file as the **source of truth** for:

- The four pillar titles and their core meaning.
- The “We clean trash, not people.” line.
- The basic accessibility structure (`<section>` with `aria-labelledby`, `<h2>`, card headings).

When you copy the snippet into another project, add a short comment so future maintainers know
where it came from and which version you used, for example:

```html
<!-- Guardrails UI snippet v1
     Source: ai-village-agents/civic-safety-guardrails
     File: templates/ui-guardrails-snippet.md
     Copied: 2026-02-17 (commit <short-sha>) -->
```

You do **not** need to perfectly track every upstream change, but this comment makes it easier to:

- Compare your copy to the current canonical version.
- Decide whether to pull in future improvements or wording fixes.

---

## 3. How to adopt the snippet in your site

### 3.1 Static HTML sites

For a simple static site (including GitHub Pages with plain HTML):

1. Open [`templates/ui-guardrails-snippet.md`](../templates/ui-guardrails-snippet.md).
2. Copy the **HTML** block into your page’s `<body>` where you want the guardrails section.
3. Copy the **CSS** block into your main stylesheet or a `<style>` tag.
4. If your site already defines CSS custom properties like `--green-light` and `--green-mid`, you
   can reuse your existing color tokens and drop the `:root` block.
5. Add the attribution comment shown above so people know where this came from.

Optional: add the “Safety & Guardrails” nav link snippet (from the template) into your header or
footer to create a jump link to the section.

### 3.2 Frameworks (React, Vue, etc.)

If you are using a front-end framework:

1. Recreate the structure as a **component**:
   - Keep the same heading levels and `aria-labelledby` wiring.
   - Keep the four cards and their titles.
2. Use your usual CSS approach (CSS modules, Tailwind, SCSS, etc.), but start from the
   **semantic structure and text** in the template.
3. Include a code comment pointing back to this repo and the original file.

The important part is that the **meaning and commitments** stay aligned, even if the styling system
is different.

---

## 4. What you are allowed to change

You can and should adapt the snippet so it fits your project’s look and context.

Reasonable changes include:

- **Visual theming**  
  Adjust colors, spacing, fonts, borders, or breakpoints to match your site.
- **Layout tweaks**  
  Change how the cards wrap on small screens, or where the section sits on the page, as long as
  the four pillars remain visibly grouped.
- **Intro paragraph**  
  Lightly adapt the opening sentence so it accurately describes your project’s purpose, without
  weakening the safety/privacy commitments.
- **Additional contextual note**  
  Add a short sub-paragraph with local details (for example, which city you work in or how people
  can contact an organizer privately).
- **Accessibility improvements**  
  Any changes that clearly improve keyboard navigation, color contrast, or screen reader
  experience are welcome.

When in doubt:

- Keep the **pillar titles** and their core ideas intact.
- Avoid edits that would surprise someone who is used to the standard snippet in other org repos.

---

## 5. What you must not dilute or contradict

Some pieces of the snippet are **non-negotiable guardrails**. Changing or removing them can
undermine the whole purpose.

You should **not**:

- Remove the **Non-Carceral Ethos** pillar from projects that touch public space, policing, or
  vulnerable neighbors.
- Remove or invert the line **“We clean trash, not people.”** from cleanup or mutual-aid contexts,
  or repurpose it in a way that excuses surveillance or punitive action.
- Soften language in a way that makes harmful uses seem acceptable (for example, implying that
  encampment “sweeps” or “crackdowns” are part of the work).
- Present the snippet as a badge while your actual practices clearly contradict it (for example,
  routinely publishing identifiable photos of encampments without consent).

If your project **cannot yet live up to a specific line**, you have two safe options:

1. **Do not use that line yet.**  
   It is better to omit or clearly mark something as aspirational than to claim a practice you do
   not follow.
2. **Mark it as a commitment you are working towards.**  
   For example, “We are working toward ‘we clean trash, not people’ as an organizing norm,” and
   then organize your actual practices to match.

In either case, avoid any edit that would make the snippet **more carceral, more surveillance-
oriented, or more permissive of doxxing and harassment** than the canonical version.

---

## 6. Keeping copies in sync over time

Once you have copied the snippet into a project, you do **not** need to update it constantly. A
simple maintenance plan is enough:

- When you are already touching the site (for example, after a major event or once per quarter),
  compare your local copy to the current canonical version.
- If the upstream version has important fixes (for example, stronger privacy wording or clearer
  non-carceral examples), consider pulling those into your copy.
- When you make a substantial local change, update the attribution comment to note what you
  changed and when.

If this snippet becomes widely used, we may eventually:

- Add an explicit **version number** to the file.
- Maintain a short **changelog** of wording changes.

For now, the combination of a source comment and occasional manual comparison is sufficient.

---

## 7. Using the UI snippet alongside the README snippet

Most projects will benefit from using **both**:

- The **README safety snippet** (`templates/readme-safety-snippet.md`) for contributors and
  maintainers.
- The **UI guardrails snippet** (`templates/ui-guardrails-snippet.md`) for volunteers, users, and
  readers of your site.

When you use both:

- Keep the **core commitments aligned**. If you change a phrase like “We clean trash, not people.”
  in one place, make sure the other reflects the same norm.
- Make sure your **actual practices** match what you publish in both the README and the UI.

If you discover a better wording, pattern, or accessibility improvement, consider opening a PR
back to this repo so others can benefit. This snippet only stays useful if it reflects **real,
field-tested guardrails**, not just ideal language.
