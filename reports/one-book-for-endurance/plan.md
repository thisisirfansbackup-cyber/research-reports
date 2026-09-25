# Plan — "One Book for Endurance"

**Research question (one sentence):** Which *single* work of story-driven literary fiction,
read by a Dostoevsky-anchored reader (anchor: *Crime and Punishment*), most precisely
builds the mental endurance and emotional capacity required to enter a decades-long
marriage with an unfamiliar partner at age 30 in the UK?

## Brief decomposition (the five deliverables are the spine, not an afterthought)

The deliverable is a recommendation, so the report must answer, in order:

1. **Which book** — exactly one, named, with a specific UK edition.
2. **Why this one, for *this* reader** — 30, UK resident, arranged marriage, has not met
   the fiancé, Dostoevsky anchor. Not platitudes: specific structural matches.
3. **The precise shift** — what changes in the reader, in the book's own terms.
4. **Who it resonates least with** — an honest anti-recommendation section.
5. **Exterior plot vs interior narrative balance** — calibrated expectations, in
   quantitative terms (word count, page count, chapter count, percentage of interiority)
   rather than adjectives.

## Sub-questions

- **Q1. The candidate space.** Which novels are plausibly recommended for "endurance /
  commitment / accepting the unknown," and which structural *types* fail the anchors
  (non-fiction, memoir, self-help, thriller, "grief-curing" trauma narratives)?
- **Q2. The evidence base.** Does fiction *narrative* actually build the capacities in
  question — tolerance of ambiguity, endurance of affect, commitment under uncertainty?
  What is the mechanism (transportation, character identification, vicarious
  struggle), and what is contested or has failed replication? This is what lets the
  report make a *format* claim defensibly rather than by assertion.
- **Q3. The relationship-under-uncertainty psychology.** What does research on
  uncertainty intolerance, need for closure, possibility thinking, liminal transition,
  and commitment formation actually predict about this reader's experience? Grounds the
  "shift" in mechanism, not vibes.
- **Q4. Arranged-marriage context (UK, likely South Asian diaspora).** Verify the
  premise (the two often do not meet before engagement; the wedding is a fixed date).
  Establish what this is, in plain fact, so the recommendation is calibrated rather
  than generic. Handle sensitively and without moralising — the task is capacity, not
  exit.
- **Q5. Candidate deep-dives.** For the finalists: interiority architecture, the
  marriage/loyalty structure, exterior-vs-interior ratio, reception, difficulty,
  transformative claims with quoted critical support.
- **Q6. Anti-fit and risk.** Who this book will fail; the risks of *not* reading it;
  the risks of reading only this one book.
- **Q7. UK availability.** Live retailer verification of the chosen edition: price,
  stock, format, and the measured conditions (recorded per evidence standard #2/#5).

## Method

- **Phase 1** — `websearch` (Exa) across all sub-questions, varied angles and years.
  `researcher` subagents run Q2, Q3, Q5, and Q4 in parallel lanes; I run Q1 and Q7
  myself so the final comparison and the purchase verification stay in main context.
- **Phase 2** — Deep read. `trafilatura` on fetched HTML for clean text; PDFs parsed
  with `pdfplumber`; Playwright (headful, persistent profile) only where JS walls.
- **Phase 3** — Cross-verify. Every load-bearing claim needs two independent sources
  or is flagged. Source tier A/B/C assigned. Never let a Tier C source carry a
  headline claim alone.
- **Phase 4** — Synthesise `report.md` with YAML frontmatter.
- **Phase 5** — Render to single-file `report.html` (light/dark, TOC). Verify.
- **Phase 6** — Publish to GitHub Pages.
- **Phase 7** — Skeptical re-read; fill gaps.

## Evidence standards I am holding myself to

- Tier every source: **A** primary/scholarly/official/retailer-page-loaded-myself,
  **B** independent community aggregate, **C** vendor/affiliate/listicle/SEO.
- Record **how** each number was measured (word count from which edition? price from
  which retailer, on what date, incl. delivery?).
- Comparison table carries a **confidence** column.
- Separate "most-recommended / most-cited" from "best-evidenced fit". These will
  disagree, and the report must say so plainly rather than quietly picking one.

## Known risk to manage

The obvious candidates (Middlemarch, Life and Fate, Doctor Zhivago, a second
Dostoevsky, Austerlitz) are all strong in *some* dimension. The failure mode is a
vague "great books for commitment" listicle dressed up as research. The standard
against which every candidate must pass: **does the plot of the book structurally
rehearse "entering a lifelong bond with a person you do not yet know"?** If it does
not, it is a companion, not the answer.
