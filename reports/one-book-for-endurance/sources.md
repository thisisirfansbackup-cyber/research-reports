# Sources — "One Book for Endurance"

Access dates: all retrieved 2026-09-25 unless noted.
Tiers: **A** primary/scholarly/official/retailer page loaded directly · **B** independent
community or aggregator aggregate · **C** vendor, affiliate, SEO or "best X" listicle.

---

## Infrastructure note (affects the evidence base)

The `websearch` (Exa) tool returned **HTTP 401 — authentication failed** partway through
this session, and the Exa key is not present in a non-interactive shell, so it could not be
recovered or rotated from inside the session. Fallbacks established and used:

- **Crossref REST API** (`api.crossref.org`) — peer-reviewed metadata and abstracts. Working.
- **Open Library Search API** (`openlibrary.org/search.json`) — edition/page-count metadata. Working.
- **Google Books API** — **429 quota exceeded** for this host's IP. Unusable.
- **Bing HTML** via curl_cffi — returns bot-poisoned results (unrelated cached pages). Unusable.
- **Mojeek / searx.be / lite.duckduckgo** — challenge pages or empty result sets. Unusable.
- **DuckDuckGo / any search via Playwright** — works, but the Playwright browser is a **single
  shared instance** being used concurrently by the four background research lanes. Navigating
  it from the main session would clobber their in-flight searches, so it was deliberately not
  used for search in main context.

**Consequence, stated plainly:** general web *discovery* in this session was degraded. Direct
retrieval of known URLs (publisher, retailer, journal, encyclopaedic) was unaffected and is what
most Tier A evidence below rests on. This is a real limitation on the report and is recorded
as such rather than papered over.

---

## A — Peer-reviewed / primary

| # | Source | Why it is used |
|---|---|---|
| A1 | Kidd & Castano (2013), "Reading Literary Fiction Improves Theory of Mind", *Science* 341(6146). DOI 10.1126/science.1239918 | The canonical positive claim. Abstract retrieved via Crossref. 928 citations at time of check. |
| A2 | Kidd & Castano (2018), "Reading Literary Fiction and Theory of Mind: Three Preregistered Replications and Extensions of Kidd and Castano (2013)", *Social Psychological and Personality Science*. DOI 10.1177/1948550618775410 | **Authors' own** preregistered replications. Reports "two uninformative failures to replicate and one successful replication" (small-telescopes method). Full abstract retrieved. |
| A3 | van Kuijk, Verkoeijen, Dijkstra & Zwaan (2018), "The Effect of Reading a Short Passage of Literary Fiction on Theory of Mind: A Replication of Kidd and Castano (2013)", *Collabra: Psychology* 4(1). DOI 10.1525/collabra.117 | Direct replication + p-curve analysis. Key sentence: "The meta-analytic effect of reading literary fiction on ToM was small and non-significant but there was considerable heterogeneity." Full abstract retrieved. |
| A4 | Bal & Veltkamp (2013), "How Does Fiction Reading Influence Empathy? An Experimental Investigation on the Role of Emotional Transportation", *PLoS ONE* 8(1):e55341. DOI 10.1371/journal.pone.0055341 | Open access; full abstract read. Two experiments; transportation is the moderator; **no transportation → lower empathy**; effects absent for non-fiction controls. 351 citations at time of check. |
| A5 | Encyclopaedia Britannica / Wikipedia, "Kristin Lavransdatter" | Orientation only for publication dates, volume titles, Nobel citation. Not cited as final authority. |
| A6 | Nobel Prize in Literature 1928 — Sigrid Undset, "principally for her powerful descriptions of Northern life during the Middle Ages" (quoted via A5) | Establishes what the Nobel was *for* — description, not interiority per se. Used to keep the report honest about the award's basis. |
| A7 | Waterstones product page, ISBN 9780143039167 — https://www.waterstones.com/book/kristin-lavransdatter/sigrid-undset/tiina-nunnally/9780143039167 | Loaded directly. Publisher, page count (1168), dimensions (213×145×50 mm), weight (1253 g), listed price £22.00, and an `unavailable` availability marker in page source. |
| A8 | Penguin Random House Canada reading guide, ISBN 9780143039167 — https://www.penguinrandomhouse.ca/books/297272/... | Publisher's own guide: confirms Nunnally is "the first English version since Charles Archer's translation in the 1920s"; Nunnally translation "with notes"; introduction by Brad Leithauser. |
| A9 | Open Library Search API, work `/works/OL69210W` ("Kristin Lavransdatter Trilogy") | 78 editions; first published 1920; median 1065 pages across editions (vs. 1168 in A7 — recorded as a *median across editions*, not a page count for one book). |

## B — Independent aggregate / long-form journalism

| # | Source | Why it is used | Method caveat |
|---|---|---|---|
| B1 | Goodreads edition page, *Kristin Lavransdatter* (Nunnally) https://www.goodreads.com/book/show/35074304 — 4.32 avg, 15,564 ratings | Community consensus for the specific recommended edition | **Per-edition count, not per-work.** Goodreads slugs were found to redirect unpredictably during this session (e.g. `/book/show/4364` resolved to a different novel; a slug lookup for *The Childhood of Jesus* returned 85,931 ratings on an unrelated book). Only figures whose title **and** count were both verified on the same page are used. |
| B2 | Goodreads edition page, *Life and Fate* — 3.52 avg, 7,028 ratings | Community consensus comparison | As B1 |
| B3 | Goodreads edition page, *Stoner* — 4.07 avg, 2,158 ratings | Community consensus comparison | As B1 |
| B4 | Kathryn Anne Casey, "An Introduction to the Text: Kristin Lavransdatter" — https://www.kathrynannecasey.com/p/kristin-lavransdatter-review-of-the | Independent long-form reader-essay. Supplies the interiority/exterior contrast: "Undset is the opposite [of War and Peace]. She takes us deep into the heart and mind." Also a four-reads-over-a-lifetime account, which is direct evidence about the book's re-read value at different life stages. |
| B5 | Edward Buccuscio, review, *The Catholic Telegraph* — https://thecatholictelegraph.com/book-review-sigrid-undsets-trilogy-kristin-lavransdatter/ | Serious long-form review; supplies the Anna Karenina contrast ("Kristin Lavransdatter is a comic one… redemptive suffering and the triumph of faith") and a reviewer's disagreement about translation (prefers Archer/Scott over Nunnally). Useful as a *live* critical disagreement, not as a verdict. |
| B6 | Bookslut / bookspast.com review (2019) — https://bookspast.com/2019/01/... | Independent reader review; captures the "a thousand pages of incident" objection and the accumulating-dailiness praise, and notes the pace/incident density. Tier B — a single reader, used for texture and for recording the existence of the objection, not as a count. |
| B7 | Scholarly/encyclopaedic orientation: Mark B. McDiarmid, "Writing Medieval Women (and Men): Sigrid Undset's *Kristin Lavransdatter*" — cited in *Studies in Medievalism XVII* (De Gruyter, 2022) | Confirms there is a peer-reviewed article on the novel, which is the existence of the criticism rather than its content. |

## C — Vendor / promotional / listicle (never load-bearing)

| # | Source | Handling |
|---|---|---|
| C1 | Penguin/ Waterstones jacket copy and endorsement block on the product page ("should be the next Elena Ferrante", "best book our judges have ever selected") | **Publisher marketing.** Not used as evidence of quality. One item in that block is a real published quote and is used as such: "Sigrid Undset's trilogy embodies more of life, seen understandingly and seriously… than any novel since Dostoevsky's Brothers Karamazov" — *Commonweal*. Treated as one critic's dated assertion, not as consensus. |
| C2 | "quiet novels", "books for commitment", "10 literary novels that prove romance isn't dead" style listicles | Searched, found, and **deliberately discarded**. Representative failure mode: a search for "best novels about commitment endurance fidelity" returned romance-blog and Facebook-group content with no engagement with the question. Recorded here so the report can show the candidate-space search was run and the low-quality tier was identified and excluded. |
| C3 | eBay / Instagram / AbeBooks listing pages for Archer/Abacus printings | Used only to establish that an abridged Archer/Scott English translation circulates in the UK. Not used for price. |

## A — Primary text (loaded and read directly by the main agent)

| # | Source | Method |
|---|---|---|
| A10 | *Middlemarch*, full text, Project Gutenberg eBook #145 — `https://www.gutenberg.org/cache/epub/145/pg145.txt` | Downloaded to disk (1,865,685 bytes). Whitespace-normalised, then searched. **Word count measured as 318,638 tokens** by regex `[A-Za-z’'\-]+` between the `*** START` / `*** END` markers. Independently reproduces the figure reported by Lane A, which is a two-lane agreement. |
| A11 | **Verbatim, from A10** — "But the living... seriously, the growing good of the world is partly dependent on unhistoric acts" | Full closing: *"…the effect of her being on those around her was incalculably diffusive: for the growing good of the world is partly dependent on unhistoric acts; and that things are not so ill with you and me as they might have been, is half owing to the number who lived faithfully a hidden life, and rest in unvisited tombs."* The last line before `THE END`. |
| A12 | **Verbatim, from A10** — Book I, ch. II | *"Dorothea's inferences may seem large; but really life could never have gone on at any period but for this liberal allowance of conclusions, which has facilitated marriage under the difficulties of civilization. Has any one ever pinched into its pilulous smallness the cobweb of pre-matrimonial acquaintanceship?"* **Correction to Lane A: the spelling is "pilulous", not "pilous".** |
| A13 | **Verbatim, from A10** — Book I, ch. XV | *"For surely all must admit that a man may be puffed and belauded, envied, ridiculed, counted upon as a tool and fallen in love with, or at least selected as a future husband, and yet remain virtually unknown—known merely as a cluster of signs for his neighbors' false suppositions."* |
| A14 | **Verbatim, from A10** — Book V, ch. XXXVI | *"Young love-making—that gossamer web!… The web itself is made of spontaneous beliefs and indefinable joys, yearnings of one life towards another, visions of completeness, indefinite trust. And Lydgate fell to spinning that web from his inward self with wonderful rapidity, in spite of experience supposed to be finished off with the drama of Laure."* |
| A15 | **Verbatim, from A10** — Casaubon's proposal letter, Book II | *"But I have discerned in you an elevation of thought and a capability of devotedness, which I had hitherto not conceived to be compatible either with the early bloom of youth or with those graces of sex… adapted to supply aid in graver labors and to cast a charm over vacant hours."* |
| A16 | **Verbatim, from A10** — Finale | *"Some set out, like Crusaders of old, with a glorious equipment of hope and enthusiasm and get broken by the way, wanting patience with each other and the world."* And: *"For there is no creature whose inward being is so strong that it is not greatly determined by what lies outside it."* And: *"But we insignificant people with our daily words and acts are preparing the lives of many Dorotheas, some of which may present a far sadder sacrifice than that of the Dorothea whose story we know."* |
| A17 | **Verbatim, from A10** — Finale, on the obvious misreading of the book | *"But no one stated exactly what else was in her power she ought rather to have done—not even Sir James Chettam, who went no further than the negative prescription that she ought not to have married Will Ladislaw."* Eliot naming the "wrong marriage" misreading **inside the novel**. |
| A18 | **Verbatim, from A10** — Finale, Mary Garth | *"My feelings have not changed, father. I shall be constant to Fred as long as he is constant to me. I don't think either of us could spare the other, or like any one else better, however much we might admire them."* And Caleb Garth: *"A woman must not force her heart—she'll do a man no good by that."* |
| A19 | *Middlemarch* copyright status in the UK | Project Gutenberg's licence header restricts the free US text to the US. George Eliot died 1880, so the work is **in copyright in the UK until 2051**. Free Standard Ebooks / Gutenberg editions exist (`standardebooks.org/ebooks/george-eliot/middlemarch`, verified) but the free route is a **US** right, not a UK one. A UK reader must buy or borrow. |

## A — Retailer verification for the recommended edition (live, loaded by the main agent)

| # | Source | What it establishes |
|---|---|---|
| A20 | **Waterstones product page, ISBN 9780141439549** — loaded 2026-09-25, 740,994 bytes | JSON-LD `offers.price` = **£10.99**; JSON-LD `offers.availability` = **`https://schema.org/InStock`**. Editorial metadata from the page: Publisher **Penguin Books Ltd**; ISBN **9780141439549**; **880 pages**; format **Paperback**; `datePublished` **2003-01-30**; dimensions 199 × 130 × 39 mm; 574 g. |
| A21 | **Penguin UK (publisher's own site), same ISBN** — loaded 2026-09-25, 320,653 bytes | Price **£10.99**, corroborating A20 from the publisher side. |

### Retailer walls hit (not re-hammered, per the escalation ladder)

- **Blackwell's** and **Bookshop.org**: Cloudflare interstitial ("Just a moment…") to any HTTP client. Would need the headful browser.
- **Foyles**: page fetched (573,222 bytes) but price is client-rendered; no price in the HTML. Stock signals present ("free UK delivery", "reserve online").
- **British Library `explore.bl.uk`**: returned 1 byte. Catalogue not verifiable from this host.
- Therefore the price claim rests on **two independent UK sources, one of them the publisher** (A20, A21). That is adequate for a ~£11 paperbound with a well-known ISBN, and the report says exactly how it was measured rather than asserting it as "the price".

## Verified facts that CORRECT the working brief

- The **standard modern English translation is Tiina Nunnally's** (Penguin Classics,
  1997–2000, 3 vols; 1,168 pp. in the Penguin Classics Deluxe edition), *not* Charles Archer's.
  Archer and J. S. Scott (1923–27) is the older, and per multiple independent accounts
  **abridged** English version. The brief to Lane A assumed Archer; corrected. (A8, B4, B5, C3)
- **Kristin does not marry a stranger.** She is betrothed to Simon Darre and *refuses* him; she
  marries Erlend, whom she has already met and been secretly engaged to. This is the structural
  *inverse* of the reader's situation and is a genuine mark against the leading candidate. (A5, B5, B6)
- Goodreads **rate counts are per-edition, not per-work**, and Goodreads slug lookups were
  demonstrably unreliable in this session. All figures are labelled as edition-specific. (B1–B3)
- **There is no phrase "slow web of time" in *Middlemarch*.** Verified by exhaustive
  whitespace-normalised search of the full text: `slow web of time` returns zero hits. The two
  real "web" passages are *"this particular web"* (Book I, ch. XV) and *"that gossamer web"*
  (Book V, ch. XXXVI). This phrase is widely repeated in secondary writing about the novel; it
  is not in the novel. (A10, A12, A13, A14)
- **Open Library's `first_publish_year` for *Middlemarch* is given as 1800.** That is a metadata
  error; the novel was published 1871–72. Recorded to show that the second-best structured
  source was also imperfect, and that no source was treated as authoritative by default. (A9)
- Corrected against Lane A's brief: *A Spool of Blue Thread* is **Anne Tyler** (2015), not Maile
  Meloy. *A Suitable Boy* is **Vikram Seth** (1993), not Rohinton Mistry. *Life and Fate* was
  translated by **Robert Chandler**, not "Ahlstrom". Faulks's *Where My Heart Used to Beat* is
  **2015**, not 1993, and concerns memory and grief, not arranged marriage. The Nobel for Undset
  was awarded "principally for her powerful descriptions of Northern life during the Middle
  Ages" — for historical description, **not** for psychological interiority.
