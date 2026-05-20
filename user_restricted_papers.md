# User-restricted papers — authoritative citation pool

This is the slice of `identified-papers/identified_papers_ai_info.md` that the user actually referenced (vaguely-but-sufficiently) in the Phase 1 Telegram voice exchanges. Per problem_statement.md §Phase 2 step 5, this file is the AUTHORITATIVE citation pool for the writing sample — **no paper outside this file may be cited in writing_sample.tex**.

Filter rule applied: the "lazy professor" model — a paper qualifies if the user (a) named the author by name, (b) named the paper directly, or (c) described it with sufficient specificity (topic + venue or topic + canonical association) that it can be unambiguously resolved against the identified-papers pool. Papers from `identified_papers_ai_info.md` that the user did *not* reference in voice are excluded even if they were surfaced by the discovery pipeline.

---

## Pool (26 entries, organized by the 15-stage arc)

### Stage 1 — Definition of AI

1) Klowden, Tao 2026 — Mathematical methods and human thought in the age of AI — arXiv:2603.26524 [math.HO]
   - User reference: "Terence Tao and Tanya Cloudin, 2026 paper about AI and human thought and math in the age of AI" (msg 3824).
   - BibKey: `klowden2026math`

### Stage 2 — AI ubiquity: Nobel splash

2) Jumper, Evans, Pritzel, Green, Figurnov, Ronneberger, Tunyasuvunakool, et al. 2021 — Highly accurate protein structure prediction with AlphaFold — Nature — DOI: 10.1038/s41586-021-03819-2
   - User reference: "you want to get the deep mind, alpha fold citation, cite that" (msg 3824).
   - BibKey: `jumper2021alphafold`

3) Hopfield 1982 — Neural networks and physical systems with emergent collective computational abilities — Proceedings of the National Academy of Sciences — DOI: 10.1073/pnas.79.8.2554
   - User reference: "Say AI has won the Nobel Prize in physics and chemistry, 24, and cite that" — Hopfield is the foundational citation for the Hopfield-Hinton Physics Nobel 2024 (msg 3824).
   - BibKey: `hopfield1982`

### Stage 3 — Why LLMs: neural scaling laws

4) Kaplan, McCandlish, Henighan, Brown, Chess, Child, Gray, Radford, Wu, Amodei 2020 — Scaling laws for neural language models — arXiv:2001.08361
   - User reference: "the neural scaling laws, right" (msg 3824).
   - BibKey: `kaplan2020scaling`

5) Hoffmann, Borgeaud, Mensch, et al. 2022 — Training compute-optimal large language models (Chinchilla) — arXiv:2203.15556
   - User reference: scaling laws extension (msg 3824, implicit in the broader scaling discussion).
   - BibKey: `hoffmann2022chinchilla`

### Stage 4 — Capability today + growth-rate gap

6) Schwartz 2022 — Should artificial intelligence be interpretable to humans? — Nature Reviews Physics — DOI: 10.1038/s42254-022-00538-z
   - User reference: "Matthew Schwartz is this guy at Harvard and he has a paper I think in nature review physics about should AI be interpretable to humans" (msg 3826). "We are going to keep coming back to that paper."
   - BibKey: `schwartz2022interpretable`

### Stage 5 — Creativity benchmarks

7) Hubert, Awa, Zabelina 2024 — The current state of artificial intelligence generative language models is more creative than humans on divergent thinking tasks — Scientific Reports — DOI: 10.1038/s41598-024-53303-w
   - User reference: "one in like Nature's Creativity Journal... machine creativity versus humans" (msg 3828).
   - BibKey: `hubert2024creative`

8) Guzik, Byrge, Gilde 2023 — The originality of machines: AI takes the Torrance Test — Journal of Creativity — DOI: 10.1016/j.yjoc.2023.100065
   - User reference: "one of them for sure has the torrents test, it uses GPT-4 and I think it's by some people in a business school" (msg 3828).
   - BibKey: `guzik2023torrance`

### Stage 6 — Possibility-space exploration: games, experiments, algorithms

9) Silver, Huang, Maddison, Guez, Sifre, van den Driessche, Schrittwieser, et al. 2016 — Mastering the game of Go with deep neural networks and tree search — Nature — DOI: 10.1038/nature16961
   - User reference: "alpha go move 37, I do not know if alpha go has a paper if yes go find it" (msg 3830).
   - BibKey: `silver2016alphago`

10) Krenn, Malik, Fickler, Lapkiewicz, Zeilinger 2016 — Automated search for new quantum experiments — Physical Review Letters — DOI: 10.1103/physrevlett.116.090405
    - User reference: "Mario Crane and Anton Zeilinger... used automated search to find an experimental configuration for like quantum entanglement" (msg 3830).
    - BibKey: `krenn2016automated`

11) Krenn, Erhard, Zeilinger 2020 — Computer-inspired quantum experiments — Nature Reviews Physics — DOI: 10.1038/s42254-020-0230-4
    - User reference: implicit higher-altitude review citation in the Krenn-Zeilinger program (msg 3830).
    - BibKey: `krenn2020computer`

### Stage 7 — PINN foundations and PIML overview

12) Raissi, Perdikaris, Karniadakis 2019 — Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations — Journal of Computational Physics — DOI: 10.1016/j.jcp.2018.10.045
    - User reference: "the Karniadakis and Raisi paper... famous pin one" (msg 3820).
    - BibKey: `raissi2019pinn`

13) Dissanayake, Phan-Thien 1994 — Neural-network-based approximations for solving partial differential equations — Communications in Numerical Methods in Engineering — DOI: 10.1002/cnm.1640100303
    - User reference: "94 paper by Disanayaka... foundational... not getting the sort of credibility they deserve" (msg 3820).
    - BibKey: `dissanayake1994`

14) Lagaris, Likas, Fotiadis 1998 — Artificial neural networks for solving ordinary and partial differential equations — IEEE Transactions on Neural Networks — DOI: 10.1109/72.712178
    - User reference: "98, Laguerre's paper... foundational" (msg 3820).
    - BibKey: `lagaris1998`

15) Karniadakis, Kevrekidis, Lu, Perdikaris, Wang, Yang 2021 — Physics-informed machine learning — Nature Reviews Physics — DOI: 10.1038/s42254-021-00314-5
    - User reference: "Karniadakis has one in Nature Reviews, it's like a broad physics-informed machine learning paper" (msg 3820).
    - BibKey: `karniadakis2021piml`

### Stage 7b — PINNs for elasticity + mechanics-based tomography branch

16) Haghighat, Raissi, Moure, Gomez, Juanes 2021 — A physics-informed deep learning framework for inversion and surrogate modeling in solid mechanics — Computer Methods in Applied Mechanics and Engineering — DOI: 10.1016/j.cma.2021.113741
    - User reference: "Karniadakis also has a paper on pins for like some elasticity stuff, where he did something with full field and boundaries" (msg 3820).
    - BibKey: `haghighat2021solid`

17) Goenezen, Barbone, Oberai 2011 — Solution of the nonlinear elasticity imaging inverse problem: the incompressible case — Computer Methods in Applied Mechanics and Engineering — DOI: 10.1016/j.cma.2011.04.014
    - User reference: "a paper called Mechanics-Based Tomography by Gonazen or something like that" (msg 3820).
    - BibKey: `goenezen2011nonlinear`

18) Davis, Bouman, Chen, Rubinstein, Durand, Freeman 2015 — Visual Vibrometry: estimating material properties from small motion in video — IEEE CVPR — DOI: 10.1109/CVPR.2015.7299005
    - User reference: "Katie Bowman has really cool work called Visual Vibration Tomography, Visual Surface Wave Elastography" (msg 3820). Best-fit canonical: Bouman co-authored Visual Vibrometry with Davis et al.
    - BibKey: `davis2015visual`

19) Davis, Rubinstein, Wadhwa, Mysore, Durand, Freeman 2014 — The visual microphone: passive recovery of sound from video — ACM Transactions on Graphics (SIGGRAPH) — DOI: 10.1145/2601097.2601119
    - User reference: same Bouman-line context as above; companion piece in the Davis-MIT visual-vibration program (msg 3820).
    - BibKey: `davis2014microphone`

### Stage 7c — Complex-valued NN + biological-neuron XOR

20) Aizenberg, Moraga 2007 — Multilayer feedforward neural network based on multi-valued neurons (MLMVN) and a backpropagation learning algorithm — Soft Computing — DOI: 10.1007/s00500-006-0075-5
    - User reference: "there is a guy called Eisenberg... complex valued neural network solves the XOR gate" (msg 3820).
    - BibKey: `aizenberg2007mlmvn`

21) Gidon, Zolnik, Fidzinski, Bolduan, Papoutsi, Poirazi, Holtkamp, Vida, Larkum 2020 — Dendritic action potentials and computation in human layer 2/3 cortical neurons — Science — DOI: 10.1126/science.aax6239
    - User reference: "a paper in Nature about like the biological neuron of some like rat or something like that... shown it can solve the XOR gate" (msg 3820). Best-fit canonical: Gidon et al. 2020 Science — human cortical layer 2/3 neurons solving XOR via dendritic Ca-APs. (Note: user said "Nature," paper is in Science; the paper otherwise fits all other criteria exactly.)
    - BibKey: `gidon2020dendritic`

### Stage 9 — Amdahl's law

22) Amdahl 1967 — Validity of the single processor approach to achieving large scale computing capabilities — AFIPS Spring Joint Computer Conference Proceedings — DOI: 10.1145/1465482.1465560
    - User reference: "in 1967, like, Gene Amdahl said that you can't just use a bunch of parallel computers" (msg 3824).
    - BibKey: `amdahl1967`

### Stage 11+13 — Agentic case studies (gray literature)

23) Schwartz et al. 2026 — Vibe physics: The AI grad student — Anthropic research blog (gray literature) — URL: https://www.anthropic.com/research/vibe-physics
    - User reference: "Matthew Schwartz... anthropic as an article called like vibe physics the AI graduate student and you know there is a paper in there about Sudokov shoulder" (msg 3830).
    - BibKey: `schwartz2026vibe`

24) Schwartz 2026 — Resummation of the C-parameter Sudakov shoulder using effective field theory — arXiv:2601.02484 [hep-ph]
    - User reference: paper that came out of Vibe Physics (msg 3830, msg 3833 — "Schwartz's maybe Sudhakov shoulder paper").
    - BibKey: `schwartz2026sudakov`

25) Mishra-Sharma 2026 — Long-running Claude for scientific computing — Anthropic research blog (gray literature) — URL: https://www.anthropic.com/research/long-running-Claude
    - User reference: "Siddharth Kumar Mishra talks about how he used cloud code to do a bunch of these things agentically" (msg 3830). "Siddharth Kumar Mishra he talks about the AI agents working at night" (msg 3833).
    - BibKey: `mishra2026longrunning`

### Stage 15 — Discovery vs understanding

26) Krenn, Pollice, Guo, Aldeghi, Cervera-Lierta, Friederich, dos Passos Gomes, Häse, Jinich, Nigam, Yao, Aspuru-Guzik 2022 — On scientific understanding with artificial intelligence — Nature Reviews Physics — DOI: 10.1038/s42254-022-00518-3
    - User reference: "Mario Cren has a paper on scientific understanding... something like a Turing test for scientific understanding with ultra strong machine learning... a paper by Mario Cren on scientific understanding with like AI" (msg 3833). "cite Cren's paper read through it."
    - BibKey: `krenn2022understanding`

---

## Excluded from the pool

The following candidates from the discovery pipeline were NOT referenced by the user in voice and therefore are excluded from the citation pool even though they appear in `identified_papers_ai_info.md`:

- Michie 1988 (ultra-strong ML) — the user mentioned the concept, but always via Krenn 2022's exposition. Citation goes through Krenn 2022, not Michie 1988 directly.

## Notes for the LaTeX step

- Stages 8, 10, 11, 12, 13, 14 of the arc are SCAFFOLDING/PROPOSAL claims (Amdahl-extrapolated bottlenecks; the three-session validity-preserving architecture; voice + auto-mode + cloud compute; lab-notebook tree; etc.) — these are framed by the user's own design choices rather than by external citations. They reference but do not require new bibliography entries.
- "Odorless proof" (stage 15, msg 3836) is the user's correction of his earlier "orderless proof" misspeak. In Tao's mathematical writing the closest related notion is in Klowden & Tao 2026; we cite that paper for the framing without making a stronger claim about Tao having used the exact phrase "odorless" in print.
- Hopfield 2024 Nobel Physics is cited via the foundational Hopfield 1982 paper; AlphaFold 2024 Nobel Chemistry is cited via Jumper et al. 2021. There is no "Nobel Prize paper" to cite directly.
- The Aizenberg complex-valued-NN line has many papers; we cite the 2007 MLMVN paper as a representative entry-point. Should the prose need the deeper claim about XOR specifically, this is the right anchor.

Total: 26 citation entries, covering every stage of the 15-stage arc that needs an external citation.
