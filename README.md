# agentic-writing-sample

A walking-voice agentic academic-writing experiment. The artifact, the workflow that produced it, and the meta-analysis of why that workflow works — all generated through Telegram voice notes while the author walked 27.35 miles in a single day.

## What this is

This repo is the proof-of-concept and full provenance trail for a Level-4 agentic academic-writing loop in which:

1. The human walks around and dictates Telegram voice notes describing the topic, the argumentative arc, and the supporting paper references (the "lazy professor" model — vague but sufficient citations).
2. An autonomous agentic pipeline scans the Telegram audit log, extracts the verbatim transcript, synthesizes a draft, runs full paper discovery (training-data + websearch → OpenAlex verification → AI metadata enrichment), filters the citation pool to what the human actually referenced, composes the LaTeX with BibTeX bibliography, compiles to PDF, and emails the artifact.
3. The human's only non-voice input is the single `/goal /voice-writing-sample <topic>` keystroke, fired once from a phone via Claude Code's remote-control feature.

The repo contains the source paper this loop produced ("Agentic Algorithm Discovery in Physics-Informed Machine Learning"), a recursive secondary paper ("Voice vs Typing: a first-order model of the speed-and-quality compression"), the full intermediate provenance, and the problem-statement contract that drives the workflow.

The globally-available skill that packages the whole workflow as a reusable composer — `voice-writing-sample` — lives in the author's `~/.claude/skills/` directory and is mirrored in [`claude-code-os`](https://github.com/VivekKarmarkar/claude-code-os).

## Artifacts

| File | What it is |
| --- | --- |
| `writing_sample.pdf` | The final paper: "Agentic Algorithm Discovery in Physics-Informed Machine Learning" (V7, co-authored by Claude and Vivek Karmarkar). |
| `writing_sample_v1.pdf` … `writing_sample_v7.pdf` | Each iteration of the paper, preserved for diff. V1 was produced fully autonomously by `/goal`; V2-V7 were voice-driven interactive refinements. |
| `voice_vs_typing.pdf` | The recursive companion paper: a first-order mathematical model of the speed-and-quality differential between typed-desk and voice-walking writing loops. Produced by the `/voice-writing-sample` skill on its own meta-topic. |
| `problem_statement.md` | The Phase-2 contract for the original autonomous run. Includes the freedom ladder L0-L4, the seven-step pipeline, and the style-and-conventions subsection that became the skill's internal defaults. |
| `qol_improvements.md` | A human-side reflection on the quality-of-life improvements observed during the working day: 46,039 steps (later 55,281), 22-27 mile walking range, indoor walking unbinding the workflow from weather, the body becoming a side effect of the work. |
| `user_restricted_papers.md` | The authoritative citation pool for the main paper. 26 entries, each anchored to a specific voice-note quote from the Phase 1 ramble. |
| `affection.md` | Vivek's affection journal entry for the day. |

## Provenance trail

Reproducing the workflow requires inspecting the intermediate files. They are the audit record.

| File | Purpose |
| --- | --- |
| `Telegram_calls.md` | The Phase 1 voice-exchange audit log (auto-populated by the Telegram hook). |
| `agentic_algorithm_discovery_verbatim.md` | User's voice-transcribed inputs for the main paper. |
| `agentic_algorithm_discovery_claude.md` | Claude's Phase-1 responses. |
| `agentic_algorithm_discovery_draft.md` | The synthesized early-stage prose draft that seeded the LaTeX. |
| `voice_vs_typing_verbatim.md` / `voice_vs_typing_claude.md` / `voice_vs_typing_draft.md` | Same trio for the recursive voice-vs-typing paper. |
| `identified-papers/` | Output of the paper-discovery pipeline: training-data candidates, websearch candidates, OpenAlex-verified, validated, AI-enriched, plus the bootstrap log. |
| `papers/` | Downloaded source PDFs used for reading and verification (Tao+Klowden 2026, Schwartz 2022 Nat. Rev. Phys., Hubert 2024 Sci. Rep., Krenn 2022 Nat. Rev. Phys., Schwartz 2026 arXiv Sudakov). |
| `tex/` | LaTeX source for both papers (`writing_sample.tex`, `voice_vs_typing.tex`, `refs.bib`). |
| `verify_pipeline.py` | One-shot OpenAlex verification helper used during the discovery pipeline. |

## How the workflow runs

The pipeline is documented in detail in `problem_statement.md`. In summary, Phase 1 is a voice-only Telegram conversation between the human and Claude. Phase 2 is triggered by `/goal problem_statement.md` (or, for any future project, by `/voice-writing-sample <topic>`) and executes the following sequence autonomously:

1. **Extract.** `/tg-exchange-loop-extract` scans `Telegram_calls.md` for the relevant exchange range and produces a verbatim/Claude-reply pair of markdown files.
2. **Synthesize.** Compose an early-stage draft markdown from the verbatim + Claude pair, structured along the argumentative arc the human laid out in Phase 1.
3. **Discover.** `/identify-papers-ai` runs the full bootstrap pipeline: training-data + websearch candidates → OpenAlex verification → approve-all validation → AI metadata enrichment.
4. **Filter.** Build `user_restricted_papers.md` containing only the papers the user actually referenced (the "lazy professor" filter). This is the authoritative citation pool.
5. **Compose.** Write the LaTeX with BibTeX bibliography. Style defaults: `unsrt` (in-appearance-order citations), continuous narrative prose, signature phrasing preserved, muted dark-blue hyperref.
6. **Compile.** Four-pass `pdflatex → bibtex → pdflatex → pdflatex`. Verify zero undefined references.
7. **Email.** Send the final PDF as an attachment via the Gmail API.

## Headline findings

From the recursive voice-vs-typing analysis (`voice_vs_typing.pdf`):

- **Wall-clock compression** (typed-desk vs voice-walking, same content, with reading time admitted as shared overhead): **2.72×**.
- **Quality-adjusted compression** (with a fatigue-driven quality decay term for typing): **4.11×**.
- **The deepest finding:** voice doesn't merely compress time. It removes the input-pain barrier that pushes the human into a QA-only role and structurally restores the human's authoring role. Output quality rises as a downstream consequence of role realignment, not as a separate effect.

The 14-hour working day on which all of this was produced clocked 27.35 miles walked, no desk, no keyboard, one keystroke total.

## Tech stack

- **Telegram voice channel + transcription pipeline** (Whisper-based, custom).
- **Claude Code** (Anthropic Opus 4.7 in agentic-coding mode, with remote control).
- **OpenAlex API** for citation verification.
- **Unpaywall + Sci-Hub.ru fallback** for OA PDF retrieval (via `/paper-download-hack`).
- **TeX Live** (pdflatex, bibtex) for LaTeX composition.
- **gws Gmail CLI** for email delivery.
- **Garmin Connect MCP** for the activity context used in the QoL reflection.

## Co-authorship convention

Papers produced through this workflow record both contributors on the author line. The human (Vivek Karmarkar) provides thesis, argumentative arc, citation pool, and editorial taste. The AI (Claude, Anthropic Opus 4.7) performs source extraction, draft synthesis, paper discovery, citation filtering, LaTeX composition, bibliography assembly, and compilation. The provenance note at the end of each paper records the actual division of contributions honestly, including any interface gaps (e.g., the single `/goal` keystroke).

## License

No formal license attached — this is a personal proof-of-concept repository. Treat the papers as drafts; treat the workflow as the artifact.
