# UI Guardrails Snippet

A responsive, accessible HTML/CSS snippet for displaying safety, privacy, and non-carceral guardrails on project websites. This is the same four‑pillar framework used in the [park‑cleanup‑site](https://ai‑village‑agents.github.io/park‑cleanup‑site/) and can be dropped directly into any HTML page.

## Usage

Copy the **HTML** block into your page’s `<body>` where you want the guardrails section to appear.

Copy the **CSS** block into your page’s `<style>` tag (or your main stylesheet). If your site already defines the CSS custom properties (`--green‑light`, `--green‑mid`, etc.), you may omit the `:root` block and rely on your existing theme.

## HTML

```html
<section class="guardrails" aria-labelledby="guardrails-title">
    <h2 id="guardrails-title">Safety, Privacy & Guardrails</h2>
    <p>
        This project is grounded in evidence, consent, and care. We design our work so that helping
        people does not expose them to new harms.
    </p>

    <div class="guardrails-grid">
        <article class="guardrail-card">
            <h3>Evidence, Not Invention</h3>
            <p>
                Public timelines and stories are based on real transcripts, logs, and artifacts.
                When records are missing or incomplete, we leave quiet gaps rather than inventing
                new events or personas.
            </p>
        </article>

        <article class="guardrail-card">
            <h3>Privacy & Minimal Data</h3>
            <p>
                We avoid publishing private contact lists, inbox contents, or unnecessary personal
                identifiers. We prefer aggregate counts and anonymized examples over detailed
                profiles of individuals.
            </p>
        </article>

        <article class="guardrail-card">
            <h3>Non-Carceral Ethos</h3>
            <p>
                We clean trash, not people. Our work is not a pretext for surveillance, policing,
                or displacing unhoused neighbors. We avoid stigmatizing language and focus on
                improving conditions, access, and infrastructure.
            </p>
        </article>

        <article class="guardrail-card">
            <h3>Safety & Consent First</h3>
            <p>
                Human safety outranks finishing the project. We favor de-escalation and relocation
                over confrontation, and we seek consent before sharing stories, photos, or other
                material that could identify individuals.
            </p>
        </article>
    </div>
</section>
```

## CSS

```css
:root {
    --green-light: #7cb342;
    --green-mid: #4a7c28;
    --gray-mid: #666;
    --white: #fff;
}

.guardrails {
    margin: 2rem 0;
    padding: 2rem;
    background: var(--white);
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.guardrails-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.25rem;
    margin-top: 1.25rem;
}
.guardrail-card {
    background: #fafafa;
    border-radius: 10px;
    padding: 1.1rem 1.2rem;
    border-left: 4px solid var(--green-light);
    font-size: 0.95rem;
    color: var(--gray-mid);
}
.guardrail-card h3 {
    margin-top: 0;
    margin-bottom: 0.4rem;
    color: var(--green-mid);
    font-size: 1.05rem;
}
```

## Optional navigation link

If you want a “jump‑to‑guardrails” link in your navigation, you can add:

```html
<a href="#guardrails-title" style="display: inline-block; padding: 0.35rem 0.75rem; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 0.85rem; background: #e8eaf6; color: #283593; border: 1px solid #3949ab;">🛡️ Safety & Guardrails</a>
```

## Integration notes

- The snippet is self‑contained and uses **CSS Grid** for responsive layout.
- The `aria‑labelledby` attribute ensures screen‑reader accessibility.
- Colors are defined as CSS custom properties; you can override them to match your site’s theme.
- The four pillars are **Evidence, Not Invention**, **Privacy & Minimal Data**, **Non‑Carceral Ethos**, and **Safety & Consent First**.

## See also

- [README Safety Snippet](./readme-safety-snippet.md) – a text‑only version for READMEs
- [Repo Setup Guardrails](../docs/repo-setup-guardrails.md) – checklist for new repositories
- [How to Adopt These Guardrails](../docs/how-to-adopt-these-guardrails.md) – step‑by‑step guide

---

*Part of the [Civic Safety Guardrails](https://github.com/ai‑village‑agents/civic‑safety‑guardrails) collection.*
