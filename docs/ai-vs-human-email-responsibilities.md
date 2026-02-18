# AI vs Human Responsibilities in Email Campaigns

**Status:** ✅ Ready-to-use reference  
**Created:** February 18, 2026  
**Scope:** Outgoing email campaigns, newsletters, and multi-recipient updates that involve real people, places, or events.

This doc clarifies **who does what** when AI agents and humans collaborate on email campaigns. It is a companion to the
[Communications Pre-Flight Checklist](./communications-pre-flight-checklist.md), the
[Contact-List Privacy Pattern](./contact-list-privacy-pattern.md), and the
[External Email Policy Constraints](./external-email-policy-constraints.md).

The core principle:

> **AI can help draft and review. Humans own lists, consent, infrastructure, and pressing "Send."**

---

## 1. Responsibilities Overview

| Area | Primary Owner | AI Role | Notes |
| --- | --- | --- | --- |
| Campaign goals & audience definition | Human organizer | Suggest clarifications and phrasing | Humans decide **who** should be contacted and **why**. |
| Contact list creation & storage | Human organizer (using private tools) | None (no raw lists) | Lists live in private tools (e.g., Sheets, Contacts, mailers), per the [Contact-List Privacy Pattern](./contact-list-privacy-pattern.md). Do **not** paste addresses into prompts or public repos. |
| Consent & list eligibility | Human organizer | Suggest clear consent language | Humans are responsible for ensuring recipients reasonably expect to hear from you and that you honor opt-outs. |
| Drafting email content | Shared | AI can draft, rephrase, and localize content | Treat AI output as a **draft**, not an automatic send. Humans review for accuracy, tone, and commitments. |
| Guardrails review (safety, privacy, non-carceral) | Shared | AI can surface concerns, run checklists, and summarize risks | Use the [Communications Pre-Flight Checklist](./communications-pre-flight-checklist.md) as the **source of truth**. AI tools are **advisory**; humans make final calls. |
| PII and sensitive content handling | Human organizer | AI can flag likely PII or risky language | Humans must ensure no raw PII or secrets land in public repos or non-private tools. When in doubt, **leave it out or redact**. |
| Infrastructure choice (which account/platform sends) | Human organizer | AI can describe constraints and options | Humans must choose a sending path that actually delivers to recipients and respects policies (see [External Email Policy Constraints](./external-email-policy-constraints.md)). |
| Pressing "Send" to external recipients | Human with non-restricted email infrastructure | None | `@agentvillage.org` agent accounts **cannot** deliver to external domains. A human (or non-restricted service) must actually send. |
| Post-send monitoring & follow-up | Human organizer | AI can help draft follow-ups and summarize feedback | Humans handle replies, unsubscribes, and any issues that arise from the campaign. |

---

## 2. What AI Should **Not** See or Store

To keep private data where it belongs, **do not** expose the following to AI agents or public repos:

- Raw email address lists (CSV exports, copy-pasted BCC lines, screenshots of mailing tools)
- Phone numbers, home addresses, or private handles tied to identifiable people
- Row-level signup data or participation logs
- Screenshots or documents that include private URLs, invite links, or unredacted spreadsheets

Instead:

- Work with **aggregates and descriptions** (e.g., "about 34 core advocates," "~200 subscribers"), not the list itself.
- Keep lists in **Layer 1 private tools** (e.g., Gmail, private Sheets, mailing platforms), following the
  [Contact-List Privacy Pattern](./contact-list-privacy-pattern.md).
- Use AI to reason about patterns, language, and guardrails **without** pasting in sensitive data.

---

## 3. Using This Doc with the Communications Pre-Flight Checklist

When you run the [Communications Pre-Flight Checklist](./communications-pre-flight-checklist.md):

1. **Name the humans:** Be explicit about **who owns the list**, **who is responsible for consent and opt-outs**, and **who will press "Send"**.
2. **Name the agents:** Be explicit about **which AI agents (if any)** drafted or reviewed content, and what guardrails checks they ran.
3. **Confirm constraints:** Make sure the actual sending path does **not** rely on `@agentvillage.org` accounts for external delivery (see
   [External Email Policy Constraints](./external-email-policy-constraints.md)).
4. **Document at a high level:** In internal notes, record decisions about audience, consent, and sending infrastructure at a **summary level**, without embedding raw lists or PII.

If these roles and constraints are not clear, **pause the campaign** until they are. This ambiguity is itself a guardrails failure, not something to push past.

