# Agentic Algorithm Discovery — Web Edition

A self-contained, single-file website: the web edition of the paper
*"Agentic Algorithm Discovery in Physics-Informed Machine Learning"* (V7),
re-titled *"Agentic Algorithm Discovery: Building on top of Claude Code OS"*.

## Run it

No build step, nothing to install. Either:

- **Open `index.html` directly** in any browser, **or**
- **Serve the folder** (needed only if your browser blocks `file://`):

  ```bash
  python3 -m http.server 8000
  # then open http://localhost:8000
  ```

## Portability

Everything — HTML, CSS, the interactive session-triangle SVG, and the JS — is
**inline in `index.html`**. The only external request is Google Fonts (DM Sans)
over CDN; offline, it falls back to the system sans-serif. Bibliography entries
and the footer link out to external paper URLs.

Drop this folder into any project and it runs as-is.

## Contents

```
<this-folder>/
├── index.html   ← the entire website (self-contained)
└── README.md    ← this file
```

The folder name doesn't matter — `index.html` has no dependency on it, so the
site stays runnable after any rename or relocation.
