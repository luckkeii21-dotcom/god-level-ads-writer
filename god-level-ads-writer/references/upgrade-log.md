# Upgrade Log — Living Knowledge Base

This file tracks all updates, additions, and new learnings added to this skill over time.
Every entry should be dated, sourced, and tagged with testing status.

**Testing status tags:**
- `[THEORETICAL]` — Not yet tested in live campaigns
- `[TESTED]` — Tested with results noted
- `[PROVEN WINNER]` — Repeated positive results. Weight heavily in output.

---

## HOW TO ADD AN UPGRADE

When you learn something new — from a YouTube video, a course, a podcast, a winning ad, 
real campaign results, a new hook that's working, or a platform update — tell Claude:

> "Add this to the skill: [paste notes/transcript/learning]"
> or "I learned something new about [topic] — update the skill"
> or "This ad got [result] — add it"

Claude will:
1. Extract the key learnings
2. Identify which reference file to update (or create a new one)
3. Add the content with a date stamp and testing status tag
4. Update this log with what was added and where

---

## UPGRADE ENTRIES

---

### ENTRY 001
**Date:** 2025-04
**Source:** Deep research + Meta Ads Masternote (insider document)
**Added by:** Initial skill build (ad-scriptwriter v1)
**Status:** `[PROVEN WINNER]` — Core foundations, widely validated

**What was added:**
Initial knowledge base from the original ad-scriptwriter skill:
- Framework library: PAS, Hook-Story-Offer, BAB, AIDA, 4Ps, PASTOR, Indirect, Direct
- USA vs. India market differences (cultural, language, CTA, pricing, trust signals)
- Offer construction using Hormozi Grand Slam framework
- Industry playbooks: Med Spa, Dental, Wellness, Coaching, Dealerships, AI/Tech, Herbalife
- CTA and offer library with benchmarks
- Meta ad copy best practices
- Hook library: 18 types + 30+ industry examples
- Second-by-second 60s framework

**Files created:**
- `references/frameworks.md`
- `references/hooks.md`
- `references/industry-playbooks.md`
- `references/india-market.md`
- `references/offer-cta-library.md`

**Client context from v1:**
- Rizz Dial (AI sales automation)
- Phoenix Truxx (NJ truck dealership)
- EvrythingAI (AI marketing agency)
- Haven N Smile (Indian dental clinic)

---

### ENTRY 002
**Date:** 2026-04
**Source:** Human vs AI Writing research (linguistic studies + practitioner analysis)
**Added by:** God-level ads writer v1 rebuild
**Status:** `[PROVEN WINNER]` — Based on documented linguistic research

**What was added:**
Full anti-AI writing rules and Voice DNA framework based on:
- Linguistic studies comparing human vs. AI-generated text
- AI fingerprint research and detection guide analysis
- Practitioner analysis of Claude skill building for writing
- Voice DNA building methodology

**Key rules encoded:**
- Hard ban on em dashes in all output
- Hard ban on contrast-negation patterns ("not just X, it's Y")
- Hard ban on stock transitions and overused AI phrases
- Sentence rhythm variation requirements
- Specificity requirements (numbers, names, dates, places)
- Grammar standards (excellent throughout)
- Conversion Priority Rule for conflict resolution

**Files created/updated:**
- `references/writing-voice.md` (new)
- `SKILL.md` — Writing Constitution section added

---

### ENTRY 003
**Date:** 2026-04
**Source:** Format analysis + platform best practices
**Added by:** God-level ads writer v1 rebuild
**Status:** `[THEORETICAL]` — Format specs based on best practices, not yet fully campaign-tested

**What was added:**
Complete ad format library covering all major ad types:
- Short-form UGC
- Founder-led
- Testimonial
- Faceless/AI-generated
- Influencer-style
- Static image ad (single + carousel)
- Mini VSL (2–5 min)
- Full VSL (10–30 min)
- Platform-specific adaptations: Meta, TikTok, YouTube, LinkedIn

**Files created:**
- `references/ad-formats.md` (new)

---

### ENTRY 004
**Date:** 2026-04
**Source:** Architecture decision — skill rebuild
**Added by:** God-level ads writer v1 rebuild
**Status:** `[THEORETICAL]` — Multi-pass framework, to be validated against output quality

**What was added:**
Multi-pass processing framework in SKILL.md:
- Phase 1: Deep intake
- Phase 2: Strategic Plan (mandatory output before scripts)
- Phase 3: Ad type + format selection
- Phase 4: Write (with Writing Constitution applied)
- Phase 5: Self-critique + rewrite pass
- Phase 6: Delivery (minimum deliverables)

Conversion Priority Rule and Prioritization Rules framework added.

**Files updated:**
- `SKILL.md` — Complete rewrite

---

## QUICK REFERENCE: WHERE THINGS LIVE

| Topic | File |
|-------|------|
| Script structures and frameworks | `references/frameworks.md` |
| Hook types, examples, data | `references/hooks.md` |
| Industry-specific angles, offers, CTAs | `references/industry-playbooks.md` |
| India market (Hinglish, WhatsApp, culture) | `references/india-market.md` |
| Turkey market (Turkish language, Meta + Turkish ad law, health rules) | `references/turkey-market.md` |
| Offer construction, CTAs, urgency, risk reversal | `references/offer-cta-library.md` |
| All ad format specifications | `references/ad-formats.md` |
| Anti-AI writing rules, Voice DNA, human writing | `references/writing-voice.md` |
| Client-specific context | `references/clients/[client-name].md` |
| Online Ticaret Üniversitesi / Digiens Akademi | `references/clients/online-ticaret-universitesi.md` |
| Cialdini persuasion principles | `references/frameworks.md` Section 12 |
| New industry added after initial build | `references/[industry-name].md` |

---

---

### ENTRY 005
**Date:** 2026-04
**Source:** Meta Andromeda era deep research report (2025–2026 benchmarks, Gemini debrief)
**Added by:** User — Resource batch 1
**Status:** `[PROVEN WINNER]` for structural/architectural rules | `[TESTED]` for benchmarks

**What was added:**

1. **Creative Hierarchy** — Concept vs. Angle vs. Hook vs. Body vs. CTA taxonomy integrated
   into SKILL.md core principles and Strategic Plan template (steps 4 and 5)

2. **Visual Swings Rule** — Meta Lattice Entity ID clustering: ads with similar opening
   3 seconds are treated as one concept by the algorithm, raising CPMs and limiting learning.
   Each concept must have a visually distinct opening.

3. **Campaign architecture** — Full testing and scaling framework:
   - Wednesday launch cadence
   - ABO for testing (5–8 creatives per batch), CBO/Advantage+ for scaling
   - 50 conversions/week to exit learning phase
   - 8–12 new variants per month target
   - "Scale concepts not ads" principle

4. **Performance benchmarks 2025** — CPL $27.66 (+26% YoY), CTR 2.59%, thumb-stop >25%,
   static CTR >1.5%. Track Cost Per Opportunity and Lead-to-SQL, not just CPL.

5. **Us vs. Them framework** — Mid-funnel differentiation format added to frameworks.md
   (Section 10). For solution-aware audiences comparing options.

6. **Lead magnet intelligence** — Utility tools (calculators, specific checklists, quizzes)
   outperform generic PDFs. Added to offer-cta-library.md Section 1a.

7. **"Creative is the targeting"** principle formally integrated into SKILL.md core section.

**Files created/updated:**
- `SKILL.md` — Creative Hierarchy section, Visual Swings Rule, Strategic Plan steps 4+5 updated
- `references/campaign-architecture.md` (new file)
- `references/frameworks.md` — Section 10 (Us vs. Them) added
- `references/offer-cta-library.md` — Section 1a (Lead Magnet Intelligence) added

**Conflicts with existing knowledge:** None. All additions are complementary.

---

### ENTRY 006
**Date:** 2026-11
**Source:** Turkish advertising regulation research (Reklam Kurulu, Ticaret Bakanlığı, Sağlık
Bakanlığı, Resmî Gazete), Meta advertising standards, Turkish linguistics and spoken-language analysis
**Added by:** User request: permanent Turkey Mode
**Status:** `[THEORETICAL]` for language/hook/offer guidance (test in live campaigns) |
regulatory notes verified against sources as of 2026-11 (re-check before publishing)

**What was added:**
1. **Turkey Mode (Türkiye Modu)** with auto-activation when the user writes in Turkish or the
   market is Turkey. Full process runs in Turkish.
2. **Turkish language structure:** agglutination, Turkish timing/word-count table
   (30s ≈ 55–62 words), SOV word order and pre-verb emphasis, inverted sentences in hooks,
   Turkish characters and İ/I capitalization, apostrophes, number/currency format, common
   spelling errors (de/da, ki, mi).
3. **Spoken Turkish patterns:** sen/siz decision table, natural openers, filler dosage, register
   by generation, hitap words (hocam, abi/abla, kanka), idioms, regional guidance.
4. **Turkish anti-AI ban list:** contrast-negation equivalents, translated openers, corporate
   brochure language, book suffixes (-mektedir), translationese, with rewrite examples.
5. **Turkish hook library** across the 18 hook types.
6. **Meta in Turkey:** personal-attributes traps in Turkish, banned/restricted categories
   (alcohol, tobacco, illegal betting, fortune-telling, crypto, financial), Click-to-WhatsApp,
   DM ads, lead quality, KVKK in lead forms, no targeted ads to minors.
7. **Turkish ad law:** covert advertising ban, "reklam"/"tanıtım" influencer label (2026),
   AI-character disclosure and AI clones of real people ban (2026), substantiated claims,
   environmental claims (2026), discount reference price (10 days per 2026 amendment, previously
   30), "ücretsiz", taksit, verified reviews only (2026), comparative ads, KVKK/İYS, 14-day
   withdrawal right, sensitive topics and 10 Kasım.
8. **Health sector override:** 12 Nov 2025 health promotion regulation (no domestic paid ads,
   prices, discounts, testimonials, comparisons; before/after conditions; health tourism only
   via separate foreign-facing accounts in non-Turkish languages, Turkey excluded from targeting).
9. **Turkish offers, CTAs, WhatsApp greeting template, urgency do/don't, Turkish ad calendar,
   sector adaptations, US vs Turkey comparison, three full Turkish examples, Turkey checklist.**

**Files created/updated:**
- `references/turkey-market.md` (new file)
- `SKILL.md`: Turkish trigger keywords, market question, auto-detect rule, Turkish ban pointer,
  Turkish timing note, Turkey Mode Check, Turkey delivery rules, Turkey Mode block, reference table
- `references/industry-playbooks.md`: Turkey warning on Med Spa and Dental sections

**Conflicts with existing knowledge:** US health-sector offers in `industry-playbooks.md` and
`offer-cta-library.md` conflict with Turkish law. Resolved: in Turkey Mode, `turkey-market.md`
wins (legal compliance is a precondition for conversion; a rejected or fined ad converts nothing).

---

### ENTRY 007
**Date:** 2026-11
**Source:** User (Online Ticaret Üniversitesi team practice) + Robert Cialdini, "Influence" / "Pre-Suasion"
**Added by:** User request
**Status:** `[TESTED]` multi-CTA architecture (client team practice) | `[THEORETICAL]` recruitment format

**What was added:**
1. **Client file** `references/clients/online-ticaret-universitesi.md`: launch, education and
   hiring ads; multi-CTA architecture (early CTA by second 20, mid CTA for 60s+, final CTA;
   same single action every time); mandatory Cialdini labeling; launch ad patterns.
2. **Cialdini's principles** (6 + Unity) as `frameworks.md` Section 12, with Turkish examples
   and truthfulness rules for scarcity and social proof.
3. **Recruitment / hiring ad format** as `ad-formats.md` Format 9.
4. **SKILL.md:** client-file auto-read rule, client and hiring triggers, CTA rule 8 and Phase 5
   check updated to allow repeated same-action CTAs, Cialdini Map in the Strategic Plan,
   recruitment row in the format table, reference table rows.

**Conflicts with existing knowledge:** SKILL.md rule 8 / Phase 5 said the CTA is stated exactly
once. Resolved: the rule is "one action"; repeating that same action at set timestamps is allowed
when a client file requires it (the Full VSL spec already repeated the CTA 2-3 times).

---

### ENTRY 008
**Date:** 2026-11
**Source:** User feedback on the first DGNS Akademi hiring ad
**Added by:** User
**Status:** `[TESTED]` (user-approved rule)

**What changed:**
- Hiring ads for this client: Hook → Body → one CTA only. Light production. No multi-CTA.
- Describe the ideal candidate in a few "sen" sentences from the 3-4 most important
  requirements instead of listing all requirements; full list goes to the caption.
- No internal operational numbers (e.g. "6 videos a day"); pace in general terms.
- State the attractors clearly: fully remote, USD-based salary; CV by e-mail (in description).
- Brand spelling corrected: Digiens Akademi (also written DGNS), Fatih Çoban's team.

**Files updated:** `references/clients/online-ticaret-universitesi.md` (Sections 1, 2, 5, 6),
`references/ad-formats.md` (Format 9), `SKILL.md` (triggers, client table).

**Conflicts:** Overrides the multi-CTA architecture for hiring ads only; launch/education ads keep it.

---

## KNOWN GAPS TO FILL (Future Upgrades)

- [ ] Real winning ad examples with performance data — to be added as they come in
- [ ] Real estate agent advertising
- [ ] Home services (HVAC, plumbing, roofing)
- [ ] Instagram Reels-specific adaptations
- [ ] YouTube pre-roll — 5-second skip window optimization details
- [ ] TikTok Shop creator scripts
- [ ] Retargeting sequence strategy (Day 1, Day 3, Day 7 scripts)
- [ ] SMS follow-up copy post-lead-capture
- [ ] Client campaign results — add as they come in
- [ ] Winning ad swipe file — real ads with results attached
- [ ] VSL conversion benchmarks by industry and price point
- [ ] Turkey Mode: real Turkish campaign results (CPL/CTR benchmarks in TL) to move guidance from THEORETICAL to TESTED
