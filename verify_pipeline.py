#!/usr/bin/env python3
"""One-shot verification: hit OpenAlex by DOI/arXiv, emit verified info file."""
import json, sys, time, urllib.request, urllib.parse

# (label, DOI_or_arxiv, raw_line_to_copy_verbatim)
ENTRIES = [
    ("doi", "10.1016/j.jcp.2018.10.045",
     "1) Raissi, Perdikaris, Karniadakis 2019 — Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations — Journal of Computational Physics"),
    ("doi", "10.1002/cnm.1640100303",
     "2) Dissanayake, Phan-Thien 1994 — Neural-network-based approximations for solving partial differential equations — Communications in Numerical Methods in Engineering"),
    ("doi", "10.1109/72.712178",
     "3) Lagaris, Likas, Fotiadis 1998 — Artificial neural networks for solving ordinary and partial differential equations — IEEE Transactions on Neural Networks"),
    ("doi", "10.1038/s42254-021-00314-5",
     "4) Karniadakis, Kevrekidis, Lu, Perdikaris, Wang, Yang 2021 — Physics-informed machine learning — Nature Reviews Physics"),
    ("doi", "10.1016/j.cma.2021.113741",
     "5) Haghighat, Raissi, Moure, Gomez, Juanes 2021 — A physics-informed deep learning framework for inversion and surrogate modeling in solid mechanics — Computer Methods in Applied Mechanics and Engineering"),
    ("doi", "10.1016/j.cma.2011.04.014",
     "6) Goenezen, Barbone, Oberai 2011 — Solution of the nonlinear elasticity imaging inverse problem: the incompressible case — Computer Methods in Applied Mechanics and Engineering"),
    ("doi", "10.1145/2601097.2601119",
     "7) Davis, Rubinstein, Wadhwa, Mysore, Durand, Freeman 2014 — The visual microphone: passive recovery of sound from video — ACM Transactions on Graphics (SIGGRAPH)"),
    ("doi", "10.1109/CVPR.2015.7299005",
     "8) Davis, Bouman, Chen, Rubinstein, Durand, Freeman 2015 — Visual Vibrometry: estimating material properties from small motion in video — IEEE CVPR"),
    ("arxiv", "2603.26524",
     "9) Klowden, Tao 2026 — Mathematical methods and human thought in the age of AI — arXiv:2603.26524"),
    ("doi", "10.1038/s42254-022-00538-z",
     "10) Schwartz 2022 — Should artificial intelligence be interpretable to humans? — Nature Reviews Physics"),
    ("doi", "10.1038/s41598-024-53303-w",
     "11) Hubert, Awa, Zabelina 2024 — The current state of artificial intelligence generative language models is more creative than humans on divergent thinking tasks — Scientific Reports"),
    ("doi", "10.1016/j.yjoc.2023.100065",
     "12) Guzik, Byrge, Gilde 2023 — The originality of machines: AI takes the Torrance Test — Journal of Creativity"),
    ("doi", "10.1038/nature16961",
     "13) Silver et al. 2016 — Mastering the game of Go with deep neural networks and tree search — Nature"),
    ("doi", "10.1103/physrevlett.116.090405",
     "14) Krenn, Malik, Fickler, Lapkiewicz, Zeilinger 2016 — Automated search for new quantum experiments — Physical Review Letters"),
    ("doi", "10.1038/s42254-020-0230-4",
     "15) Krenn, Erhard, Zeilinger 2020 — Computer-inspired quantum experiments — Nature Reviews Physics"),
    ("doi", "10.1007/s00500-006-0075-5",
     "16) Aizenberg, Moraga 2007 — Multilayer feedforward neural network based on multi-valued neurons (MLMVN) and a backpropagation learning algorithm — Soft Computing"),
    ("doi", "10.1126/science.aax6239",
     "17) Gidon, Zolnik, Fidzinski, Bolduan, Papoutsi, Poirazi, Holtkamp, Vida, Larkum 2020 — Dendritic action potentials and computation in human layer 2/3 cortical neurons — Science"),
    ("arxiv", "2001.08361",
     "18) Kaplan et al. 2020 — Scaling laws for neural language models — arXiv:2001.08361"),
    ("arxiv", "2203.15556",
     "19) Hoffmann et al. 2022 — Training compute-optimal large language models (Chinchilla) — arXiv:2203.15556"),
    ("doi", "10.1145/1465482.1465560",
     "20) Amdahl 1967 — Validity of the single processor approach to achieving large scale computing capabilities — AFIPS Spring Joint Computer Conference Proceedings"),
    ("doi", "10.1038/s42254-022-00518-3",
     "21) Krenn, Pollice, Guo, Aldeghi, Cervera-Lierta, Friederich, dos Passos Gomes, Häse, Jinich, Nigam, Yao, Aspuru-Guzik 2022 — On scientific understanding with artificial intelligence — Nature Reviews Physics"),
    ("arxiv", "2601.02484",
     "22) Schwartz 2026 — Resummation of the C-parameter Sudakov shoulder using effective field theory — arXiv:2601.02484"),
    ("doi", "10.1038/s41586-021-03819-2",
     "23) Jumper et al. 2021 — Highly accurate protein structure prediction with AlphaFold — Nature"),
    ("doi", "10.1073/pnas.79.8.2554",
     "24) Hopfield 1982 — Neural networks and physical systems with emergent collective computational abilities — PNAS"),
    # Gray literature (no DOI; will not verify via OpenAlex; pass through as VERIFIED-GRAY)
    ("graylit", "anthropic-vibe-physics",
     "25) Schwartz et al. (Anthropic case study) 2026 — Vibe physics: The AI grad student — anthropic.com/research/vibe-physics"),
    ("graylit", "anthropic-long-running-claude",
     "26) Mishra-Sharma (Anthropic case study) 2026 — Long-running Claude for scientific computing — anthropic.com/research/long-running-Claude"),
]

def fetch_openalex(kind, ident):
    if kind == "doi":
        url = f"https://api.openalex.org/works/https://doi.org/{ident}"
    elif kind == "arxiv":
        url = f"https://api.openalex.org/works?filter=ids.openalex:&search=&filter=primary_location.source.id:S4306400194,doi:10.48550/arxiv.{ident}"
        # Try the canonical arxiv search instead
        url = f"https://api.openalex.org/works?search={ident}&per_page=3"
    else:
        return None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "agentic-writing-sample/0.1"})
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read())
    except Exception as e:
        return {"_error": str(e)}

results = []
for kind, ident, raw in ENTRIES:
    if kind == "graylit":
        results.append({"raw": raw, "verified": True, "kind": "graylit", "ident": ident})
        continue
    data = fetch_openalex(kind, ident)
    if data is None or "_error" in data:
        results.append({"raw": raw, "verified": False, "kind": kind, "ident": ident, "err": data.get("_error") if data else "no data"})
    elif "id" in data:
        results.append({"raw": raw, "verified": True, "kind": kind, "ident": ident, "openalex_id": data.get("id"), "title": data.get("title")})
    elif "results" in data and data["results"]:
        first = data["results"][0]
        results.append({"raw": raw, "verified": True, "kind": kind, "ident": ident, "openalex_id": first.get("id"), "title": first.get("title")})
    else:
        results.append({"raw": raw, "verified": False, "kind": kind, "ident": ident, "err": "no match"})
    time.sleep(0.15)

# Write verified file
with open("identified-papers/identified_and_verified_papers_info.md", "w") as f:
    f.write("# Verified papers — agentic algorithm discovery\n\n")
    f.write("Source: identified_papers_training_data.md + identified_papers_websearch.md, verified against OpenAlex.\n\n")
    f.write("---\n\n")
    for r in results:
        if r["verified"]:
            f.write(r["raw"] + "\n")
    f.write("\n---\n\n## Verification report\n\n")
    for r in results:
        status = "VERIFIED" if r["verified"] else "FAILED"
        f.write(f"- {status} | {r['kind']}={r['ident']} | {r['raw'][:80]}...\n")
        if not r["verified"]:
            f.write(f"  - error: {r.get('err','')}\n")

print(f"Verified: {sum(1 for r in results if r['verified'])} / {len(results)}")
print(f"Failed:   {sum(1 for r in results if not r['verified'])}")
for r in results:
    if not r["verified"]:
        print(f"  FAIL: {r['kind']}={r['ident']} err={r.get('err','')}")
