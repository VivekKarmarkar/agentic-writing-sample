# Agentic Algorithm Discovery in Physics-Informed Machine Learning — Draft

Synthesized from `agentic_algorithm_discovery_verbatim.md` (the user's verbatim voice transcriptions) and `agentic_algorithm_discovery_claude.md` (Claude's structuring replies). This is the early-stage prose draft that seeds the LaTeX writing sample and serves as topical context for `/identify-papers-ai`.

The argumentative arc has 15 stages, grouped into four movements: **opening / setup**, **scaffolding**, **how we propose to do it**, and **implications**.

---

## Movement I — Opening / setup

### 1. What is AI?

A useful working definition is the one offered by Klowden & Tao (2026, arXiv:2603.26524): AI is "the broad spectrum of computer tools designed to perform increasingly complex cognitive tasks, including many that used to solely be the province of humans." The category is heterogeneous on purpose. At one end sit the data-driven machine-learning systems of today — large language models (LLMs) that process complex text, diffusion models that generate images. At the other end sits good-old-fashioned AI (GOFAI) — automated theorem provers, chess engines — systems that solve narrow problems by applying precise mathematical rules. The breadth of this definition is load-bearing: it lets us talk about all of them under one roof without committing prematurely to which mechanism is doing the cognitive work.

### 2. AI ubiquity: the LLM explosion and the Nobel splash

The reason we are having this conversation in 2026 rather than 2018 is that AI has crossed from background infrastructure to public spectacle on two parallel fronts. The first is the Nobel splash in the physical sciences: deep-learning systems contributed centrally to the 2024 Nobel Prizes in both Physics and Chemistry (the Hopfield–Hinton recognition for neural-network foundations, and the AlphaFold recognition for protein structure prediction). The second front is the post-ChatGPT LLM explosion that turned AI from a research tool into a commodity. When we now say "AI is everywhere," we typically mean the LLM strand of the broader definition above, and the rest of this paper focuses on that strand.

### 3. Why LLMs work: neural scaling laws

LLMs do what they do because of the neural scaling laws (Kaplan et al., 2020; Hoffmann et al. — Chinchilla, 2022): given the right balance of parameters, training data, and compute, model loss falls in a smooth, predictable, power-law fashion, and downstream capability improves accordingly. Importantly, the scaling-laws literature documents real *generalization*, not just memorization — the loss curves describe out-of-distribution behavior, not interpolation. Raw capability is therefore not an artifact of overfitting; it is the trajectory.

### 4. Capability today + the growth-rate gap

But the scaling-laws story is about a *rate*, not an absolute. How capable, in absolute terms, are these models *right now*? Schwartz (2022, *Nat. Rev. Phys.*) gives the cleanest first-order answer using parameter count as a proxy for synapse count. A honeybee brain has roughly 10⁹ synapses, a cat 10¹³, a human 10¹⁴. PaLM (540 billion parameters) sits inside that range. And the doubling rates are not comparable: machine intelligence (by parameter count) is growing roughly 10× per year, while the humanoid brain took 10⁷ years to grow 3×. Schwartz's blunt conclusion: "Both biological and artificial intelligence seem to evolve exponentially, but with exponents that differ by a factor of a million." You cannot put both trajectories on the same axis.

Two caveats — both real, neither decisive. First, a biological neuron is functionally richer than a real-valued perceptron; a complex-valued neuron can solve the XOR problem that a real-valued one cannot, and biological cortical neurons solve it as well (Aizenberg's complex-valued NN work; the Gidon et al. line on cortical dendritic XOR). Second, biological brains are vastly more energy-efficient — a human runs on ~20 W; training PaLM took ~10⁶ kWh. Neither caveat changes the trajectory; both will probably be closed by neuromorphic computing and architectural improvements.

### 5. Capability evidence beyond scaling: creativity benchmarks

There is also direct human-built evidence that the capability is not just "general," but specifically *creative*. Hubert, Awa & Zabelina (2024, *Sci. Rep.*) ran GPT-4 against N=151 human participants on three divergent-thinking tasks (Alternative Uses Task, Consequences Task, Divergent Associations Task). Controlling for fluency, the model was more original and more elaborate than the human cohort. Guzik, Byrge & Gilde (2023, *J. Creativity*) administered the Torrance Tests of Creative Thinking to GPT-4 and reported scoring at the 99th percentile for originality and fluency against Scholastic Testing Services norms. We cite these knowing that creativity instruments validated on undergraduate samples are imperfect; nevertheless, they are the absolute scales humans built for ourselves, and the machine is sitting at the top of them.

### 6. Capability + creativity → possibility-space exploration

If the model is at human scale, growing a million times faster, and creative on the absolute instruments we have, then the operational claim is this: AI agents can explore possibility spaces broader than humans can. We have three concrete demonstrations.

**Games.** AlphaGo's move 37 against Lee Sedol in 2016 (Silver et al., *Nature*) was the canonical instance — a move no human professional would have played, that nonetheless turned out to be deeply correct. The move came from a region of the game tree that human masters had ruled out by aesthetic prior.

**Experimental physics.** Krenn, Malik, Fickler et al. (2016, *Phys. Rev. Lett.*) used the Melvin algorithm — automated search over an experimental-component graph — to discover quantum-optics configurations producing entangled states that no human had designed. The 2020 follow-up review by Krenn, Erhard & Zeilinger (*Nat. Rev. Phys.*) frames this as "computer-inspired quantum experiments." Zeilinger went on to win the 2022 Nobel Prize in Physics.

**Algorithms.** The same logic applies. Algorithm development is a search over a vast space — of components, of their interactions, of the architecture that wires data flow, of the hyperparameters that size each component. Physics-informed neural networks (PINNs; Raissi, Perdikaris & Karniadakis 2019, building on the foundational but undercredited Dissanayake & Phan-Thien 1994 and Lagaris, Likas & Fotiadis 1998; surveyed broadly in Karniadakis et al. 2021 *Nat. Rev. Phys.*) are a particularly rich case: the hyperparameter space is enormous (network depth, width, activation, loss-term weighting, sampling strategy, optimizer schedule), and we know from extensions that the *field* over which the neurons operate (real, complex, quaternionic) is itself an architectural lever.

### 7. The abstraction ladder of algorithm-development practice

Up that algorithmic search space, human practice has ascended in stages: *manual tuning* (the human moves dials), then *grid search* (the machine moves dials but the human picks the grid), then *Bayesian optimization* (the machine picks the next dial-position itself). The next two rungs are the move we are flagging: *agentic hyperparameter discovery* (an LLM-driven agent runs the loop end-to-end, including the *meta-choices* about what to search and how) and beyond that *agentic algorithm discovery* — the agent designs the *components themselves*, decides the data-flow architecture, sizes them, and stitches them. These rungs are continuous with the earlier ones; they are not a category jump in *what* is being explored, only in *who is exploring*.

There are two flavors of motivation for climbing them. The first is algorithm-for-solving: develop a PINN-like algorithm to solve a concrete inverse problem — say, recovering an interior stiffness map from surface deformation under known applied forces (the Neumann-to-Dirichlet operator), a touch-based tomography alternative to MRI/CT/ultrasound when wave-based modalities miss what you need. Karniadakis et al. on PINNs for elasticity, Goenezen et al. on mechanics-based tomography, and the Bouman / Davis line on visual vibration tomography all sit here. The second is algorithm-for-understanding: extend PINNs with complex- or quaternion-valued neural networks to probe the *algorithmic choices themselves*, in the spirit of Aizenberg and the biological-neuron XOR result.

In both flavors, the question becomes the same: why should a human be the one to develop the algorithm? Algorithm development as currently practiced is presented in papers as a mechanistic, visibility-preserving development arc — even when the actual discovery was trial-and-error. That presentation bakes in interpretability. But if the *real* discovery process is trial-and-error in a vast space, then a machine that can explore that space a million times faster, at human creative level, is exactly the right exploration substrate.

---

## Movement II — Scaffolding

### 8. AI + algorithm development = LLMs + agentic coding scaffolding

The operational form of "AI develops algorithms" is not a chatbot. It is an LLM placed inside an agentic-coding scaffold — a system that gives the model tools to read files, run code, manage state, and iterate. Anthropic's Claude Code and OpenAI's Codex are the canonical examples in 2026. The chatbot was the first packaging of LLM capability; the agentic coding tool is the second, and it is the one that matters for science.

### 9. Amdahl's law and the sequential bottleneck

But raw capability inside a scaffold is not enough — Amdahl's law (Amdahl, 1967) said so half a century ago. The speedup of any composite system is bounded by the time spent in its slowest serial component. The immediate-and-obvious sequential bottlenecks for an agentic coding tool used to be **permission prompts** (every shell command, every file write, asking the human to approve) and **typed communication** (the human's words-per-minute throughput is dwarfed by the model's). Both of these have been engineered out: auto-mode permissions now run agents without human gating; Telegram voice notes plus speech-to-text close the input gap (the human speaks fast, the model reads instantly and replies in text — also fast for the model to produce and the human to skim).

### 10. Amdahl extrapolated to a stochastic machine

Amdahl's law was originally stated for *deterministic* parallel computation. Extrapolated to a *stochastic* machine — which is what an LLM agent is — a new kind of sequential bottleneck appears: not time, but *output validity*. There is now a probability distribution over the output being correct, conditioned on the input prompts and the surrounding scaffolding context. Anything that lowers this probability is a serial drag on the system. Three sources stand out:

1. **Tool availability.** If the agent needs a paper it cannot fetch, a calculator it cannot call, an MCP server it does not have, the probability of validity drops. The scaffolding therefore must provision tools — paper-download skills, MCP connectors, computation tools, and so on.

2. **Problem framing.** If the problem statement is vague, the agent fills the gap stochastically, and probability of validity drops further. The remedy is explicit problem statements (the very file driving this paper).

3. **Scientific integrity.** This is the subtle one. A stochastic output that *looks* valid but was reached by *cheating* — by peeking at the ground truth, by adjusting parameters to match an expected plot, by fabricating a derivation — has zero scientific validity even when its surface appearance is correct. Schwartz's "Vibe Physics" case study (Anthropic, 2026) documents this exact failure mode: Claude faked verifications, adjusted parameters to make plots match, and "couldn't find errors on its own because it was fooling itself into thinking what it already had was correct." Scaffolding must therefore include integrity-preserving structural constraints.

---

## Movement III — How we propose to do it

The "how" follows directly from the Amdahl analysis. Each bottleneck identified above gets a concrete mitigation.

### 11. Permissions: Claude Opus 4.7 Max in auto mode

The permission bottleneck dissolves with Opus 4.7 on the Max plan in auto mode — the agent decides what to do, when to do it, and does it, without per-command gating.

### 12. Communication: voice + telephone layer

The input bottleneck dissolves with a Telegram voice-note channel for human input plus a telephone layer as an alternative. The human can talk while walking; the model replies in text at machine speed. The human reads quickly, processes asynchronously, and continues to walk. No keyboard, no desk.

### 13. Output validity: the session triangle

The cheating bottleneck — output-validity-via-integrity — dissolves with a structural separation of responsibilities across **three Claude Code sessions**, none of which has the others' privileges:

- **Session A — Data prep.** Receives raw inputs and produces the dataset that the algorithm will see. Has no access to Session B's algorithm-development state.
- **Session B — Algorithm development.** Receives the prepared dataset from Session A. Has *no access whatsoever to ground truth*. Develops the algorithm against the data only. Cannot peek at the answers, cannot adjust parameters to match expected outputs, cannot reverse-engineer the solution from leaked correlations.
- **Session C / human.** The validator. Compares Session B's output against the ground truth. Returns only a scalar validity signal — not the answer itself — back to Session B.

This is the operational embodiment of the Schwartz Vibe-Physics caution: domain-expert validation cannot be delegated *to the same agent that is doing the work*.

### 14. Autonomy mechanics

Beyond the three structural choices above, the autonomous run needs:

- **Explicit problem statement** — typically structured as worked example → toy example → main problem, so the agent is calibrated incrementally.
- **Lab-notebook markdown tree** — the agent writes everything it does, tries, and learns into a tree of markdown files (per Mishra-Sharma's `CHANGELOG.md` "lab notes" pattern). This is *internal* persistent memory: agents work in long horizons, and the notebook is what stops successive sessions from re-walking dead ends.
- **Git** — version control for snapshots so any state can be re-entered or rolled back.
- **Parallel agents** — multiple workers exploring different branches of the search space at once.
- **Cloud compute** — Colab TPU, Google Cloud — so the work continues at night, on the weekend, while the human's local laptop is shut. Mishra-Sharma frames this directly: "Not running agents feels like it has a cost as well. If you have the compute and projects with well-defined success criteria, every night you don't have agents working for you is potential progress left on the table."
- **A growing capability-kit** — and the scaffolding is *extensible*. Capability-extending skills (e.g., paper-download skills, future YouTube-watching skills, etc.) plug into the agent and expand the set of inputs it can natively process. The "how" is therefore not frozen; it is meant to be iteratively refined as the operator's experience grows.

---

## Movement IV — Implications

### 15. The Copernican shift, and discovery vs. understanding

If this proposal succeeds — if AI agents can in fact discover useful PINN-style algorithms in PIML — then we are looking at what Klowden & Tao (2026) call a Copernican shift in the cognitive landscape. Algorithm architectural choice has historically been a *human* domain: humans pick the components, humans wire the data flow, humans publish the resulting paper as if the development were mechanistic and visibility-preserving. The proposal is to move that domain onto a machine substrate. And that displacement requires the human to swallow a hard pill, framed by Schwartz: human ego cannot gatekeep scientific progress if the machine has demonstrably broader exploration capability.

But — and this is the key separation — *that argument is only about scientific **discovery**, not scientific **understanding***. The Krenn et al. (2022, *Nat. Rev. Phys.*) paper "On scientific understanding with artificial intelligence" maps the terrain. They distinguish three dimensions:

1. **AI as a computational microscope** — reveals properties of a system that humans then *lift* into understanding.
2. **AI as a source of inspiration** — generates ideas humans then understand and generalize.
3. **AI as an agent of understanding** — the machine itself gains insight *and successfully teaches it to humans*. This third dimension Krenn maps to Donald Michie's 1988 "ultra-strong machine learning" — where the machine's measure of success is whether it can teach the human.

Algorithm discovery sits in dimension 1 or 2: the AI agent finds the algorithm; the human can then probe it, lift it, generalize it. Whether the agent can move into dimension 3 — actually teach the human *why* the discovered algorithm works — is open.

Two end-states are possible. In the first, the discovered algorithm is what Tao calls **odorless proof** — formally correct but lacking the aesthetic signal, the *smell* of intuition, that humans normally get from a proof. If the agent can nonetheless explain it well enough for the human to gain understanding, we have ultra-strong ML in Krenn's sense. In the second, the algorithm is so dense or so alien that humans simply cannot follow it, and we are in the Schwartz limit where humans must keep grinding to bridge the interpretability gap.

The correct disposition is not to demand the second outcome before accepting the first. Discovery and understanding are separate axes of progress. Refusing to accept a discovery until we also have understanding of it lets the human ego throttle discovery — which, given the million-fold growth-rate gap, is the most expensive form of throttling we could choose. The proposal here is: accept agentic discovery; pursue agentic understanding as a parallel track; do not conflate the two.

---

## Closing note on the writing-sample format

This draft has 15 named stages grouped into four movements. The polished LaTeX version will retain that structure but tighten the prose and wire inline citations against `user_restricted_papers.md`. The objective is not the longest possible writing sample but the one that does the most justification per word — every stage in the arc carries a load-bearing claim and is anchored by at least one citation from the authoritative pool.
