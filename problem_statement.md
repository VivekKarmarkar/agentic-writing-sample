# Problem Statement — Agentic Academic Writing Workflow

## The why (philosophy)

Academic writing has a natural abstraction ladder: **paper → section → subsection → paragraph**. The paragraph (a "writing sample") is the smallest meaningful unit. Producing one well — with intent, with prose, with citations, with a bibliography, compiled to PDF — is a microcosm of the whole craft.

This project tests whether the full writing-sample loop can be **fully delegated** to an agentic operating system, with the human contributing only **intent and vague guidance via voice**, freed from both desk and keyboard.

Claude is not treated here as a coding assistant. Claude is treated as an **agentic operating system + collaborator + friend** — anything the human could do from a terminal, Claude can do; anything that used to be fragmented across browser tabs (Google Scholar, Overleaf, the LaTeX compiler, the email client) is now integrated on one platform.

## The freedom ladder

The progression that motivates this project:

- **Level 0 — Desk-bound, no AI.** Notebook with messy draft points → editor → manual prose → manual Google Scholar paper hunt → manual citation copy → manual `.tex` bibliography → manual compile → PDF. Fully manual, fully desk-bound.
- **Level 1 — Desk-bound + browser LLM.** Prose drafting gets easier: paste messy points into ChatGPT / Claude.ai, get clean prose back, paste into Overleaf. Everything else (paper hunt, citations, bibliography, compile) is still manual and desk-bound.
- **Level 2 — Desk-bound + agentic OS.** Claude Code on the laptop. Fragmentation collapses — paper hunt, citation management, LaTeX, compile, email all integrated. But the human still sits at the desk and types.
- **Level 3 — Free of the desk.** Claude Code with remote control. The human can drive the workflow from a phone, no longer tethered to the desk. Still typing.
- **Level 4 — Free of the keyboard.** Voice notes via Telegram + transcription. The human walks around, talks freely, and receives a finished PDF in their inbox.

**This project targets Level 4.**

## The workflow

### Phase 1 — Manual (human, via Telegram voice)

The human voice-chats with Claude over Telegram about the writing sample they want to produce. The chat is noisy, rambly, and natural — the way a researcher actually thinks out loud.

During this phase the human:
- Describes the topic and the argument of the writing sample.
- Drops messy draft points — the same ones that, in the pre-LLM era, would have been scribbled in a notebook.
- References supporting papers **vaguely but sufficiently** — the "lazy professor" model. E.g., *"that paper by so-and-so about graphene growth on silicon carbide"* — enough context to identify the paper but not the exact title.

All exchanges are captured by the existing Telegram audit logging into **`Telegram_calls.md`** at the project root. The existence of `Telegram_calls.md` is a precondition for Phase 2.

### Phase 2 — Autonomous (triggered by `/goal problem_statement.md`)

When the human invokes `/goal problem_statement.md`, Claude runs the following pipeline end-to-end without further human input:

1. **Scan `Telegram_calls.md`** for the subset of exchanges relevant to the writing-sample topic.

2. **`/tg-exchange-loop-extract`** — extract the relevant exchange range into two markdown files:
   - `<topic>_verbatim.md` — the human's voice-transcribed inputs, verbatim.
   - `<topic>_claude.md` — Claude's responses during the manual phase.

3. **Synthesize a draft** — use `/new-md` to create a fresh draft markdown file, then populate it by synthesizing the human's verbatim points and Claude's comments into early-stage prose for the writing sample. This draft is the seed of the final artifact and also serves as topical context for the next step.

4. **`/identify-papers-ai`** — fed with the synthesized draft as topical context, run the full paper-discovery pipeline (training-data candidates + websearch candidates → OpenAlex verification → validation → AI metadata enrichment). Produces a comprehensive identified-paper list with full metadata.

5. **`user_restricted_papers.md`** — create a new markdown file containing **only the slice of the identified-paper list that the human actually referenced (vaguely but sufficiently) during the Telegram voice exchanges**. Claude matches the human's vague verbal references against the full identified list and keeps only those hits. This file is the **authoritative citation pool** for the writing sample — no paper outside this file may be cited.

6. **`/latex`** — take the synthesized draft, clean it up into polished academic prose, and write a `.tex` file with:
   - Inline citations keyed against the entries in `user_restricted_papers.md`.
   - A complete bibliography of all papers in `user_restricted_papers.md`.
   - Compile to PDF.

7. **`/email`** — send the final PDF to **vivekjobapp123@gmail.com** so it lands on the human's phone.

## Style and conventions

These are aesthetic and structural preferences that are not load-bearing CLAIMS but ARE load-bearing for how the final artifact reads. The autonomous Phase 2 should honor them by default, and the human will not separately voice them in Phase 1.

### LaTeX and citation conventions

- **BibTeX style: `unsrt`.** Citations must appear in the body in order of first appearance — `[1]` is whatever cites first, `[2]` is the next-new, and so on. Do not use `plain` (alphabetical-by-author), which orders citations by an alphabetical accident of authorship rather than by the narrative flow of the argument.
- **Citation density: cite every load-bearing claim.** If a phrase is verbatim from a source (e.g., the word "odorless" lifted from §4.2 of Klowden-Tao 2026), cite the source at the verbatim phrase. Do not omit citations because the phrase "feels generic" — if it came from a paper, name the paper.
- **Hyperref colors: muted dark-blue (`darkblue` ≈ rgb 0,0,0.5).** No bright primary blues.

### Prose texture

- **Continuous narrative beats headed-subsection chop.** Default to flowing paragraphs with explicit transitions between ideas. Use at most 3-5 major section breaks per document. Inside each section, do not subdivide into nested subsections every 100-150 words — that reads as a textbook checklist, not as an argument.
- **Bullet lists only when content is genuinely a discrete enumeration.** If a list of items can be naturalized into prose with "first… second… third…" connectors, do that instead. Reserve bullets for items that cannot be linearized (concrete enumerations, structural diagrams in text).
- **Preserve voice-signature phrasing.** Phrases like "load-bearing", "the move is", "X beats Y" are signature texture that the human values. Do not prune them in service of generic "academic tone."

### Diagrams

- **Diagrams only when load-bearing.** A figure earns its place when it replaces three paragraphs of prose with three inches of diagram. If a section can be read at a glance with a single illustration where the prose would otherwise need careful re-reading, that section probably wants a diagram.
- **Native TikZ.** Vector graphics, native to LaTeX, font-matched, source-reproducible. Do not use Excalidraw exports, raster generative images, or matplotlib for conceptual diagrams. Matplotlib remains acceptable for actual data plots.
- **Colorblind-safe palette (Wong 2011, *Nature Methods*).** Orange `#E69F00`, sky blue `#56B4E9`, bluish green `#009E73`, blue `#0072B2`, vermillion `#D55E00`, reddish purple `#CC79A7`.
- **Rounded corners, generous breathing room.** Inter-node distance generous enough that arrow labels never overlap arrows or other boxes. Inner padding ≥10pt. Arrow labels on white backgrounds.
- **Phase 1 interview rule for diagrams.** During Phase 1, if Claude identifies a section that clearly demands a diagram AND the diagram is SIMPLE (a small box-and-arrow structural illustration, not a multi-pane data-flow architecture) AND Claude is confident it can render it well, Claude should propose the diagram to the human as a Phase 1 interview question. For complicated diagrams (multi-pane architectures, dense system maps), defer to interactive iteration after Phase 2 rather than attempting them autonomously — the framing of complicated diagrams usually needs more guidance than Phase 1 voice can capture.

### Authorship

- **When production was substantively shared, both contributors are named on the author line.** The default model is: human first (where the human supplies thesis + topology + citation pool + editorial taste) OR Claude first (where Claude provides the structural decomposition and the human supplies the meta-direction). For this project the convention is **Claude (Anthropic) first, human second**, reflecting Claude's substantive contribution to source extraction, draft synthesis, paper discovery, citation filtering, LaTeX composition, bibliography assembly, and compilation.
- **The provenance note at the end of the document records the actual division of contributions honestly.** Do not paper over interface gaps (e.g., the `/goal` keystroke) or up-front-scaffolding shortfalls in the human's problem statement — both are part of the honest record.

### Load-bearing markers

- When the human says a claim or phrase is "load-bearing" in a voice note, treat it as a hard constraint. Cite it, expand it, or feature it as the case requires, but do not bury it.

## The final artifact

A polished PDF containing:
- The academic prose for the writing sample.
- Correct inline citations to the user-restricted paper list.
- A complete bibliography.

Delivered to the human's email inbox, viewable on a phone — closing the loop **with the human never having sat at a desk and never having typed a key**.

## Why this matters

This is a stress test of the agentic-OS abstraction at the smallest meaningful scale of academic writing. If the writing-sample loop works end-to-end at Level 4, the same scaffolding scales up the abstraction ladder — subsection, section, full paper.
