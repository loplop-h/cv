# max-cv

Source for **Max Ernst Huisman Gutiérrez**'s curriculum vitae.

→ [cv-max-huisman-v3.pdf](./cv-max-huisman-v3.pdf) (canonical, one page A4, editorial layout)
→ [cv-max-huisman-v2.pdf](./cv-max-huisman-v2.pdf) (single-column ATS-strict fallback)

About me: [github.com/loplop-h](https://github.com/loplop-h) · [linkedin.com/in/maxernst-huisman](https://linkedin.com/in/maxernst-huisman) · [loplop.xyz](https://loplop.xyz)

---

## What this repo is

Most CVs are opaque artifacts — a recruiter receives a PDF and that is the entire surface. This repo is the **source of truth** behind the artifact:

- **[`cv-max-huisman-v3.html`](./cv-max-huisman-v3.html)** — the canonical CV, two-column editorial layout, written as raw HTML + CSS. ~1100 lines.
- **[`generate_pdf.py`](./generate_pdf.py)** — headless-Chrome renderer that produces a deterministic A4 PDF from the HTML. Forces paper size, embeds fonts, preserves background graphics, and injects a build stamp (date + git short SHA) into the footer at render time.
- **[`generate_qr.py`](./generate_qr.py)** — regenerator for the embedded QR code that links to my GitHub profile.
- **[`Makefile`](./Makefile)** — convenience targets for `make build`, `make qr`, `make all`.

The HTML keeps `{{BUILD_DATE}}` and `{{BUILD_SHA}}` placeholders in version control. The renderer replaces them before producing the PDF, then deletes the temp file. The committed HTML stays clean; the rendered PDF is always traceable to a commit.

---

## Build

Requirements:
- Python 3.12+
- Chrome installed at the standard path (`C:\Program Files\Google\Chrome\Application\chrome.exe` on Windows)
- `qrcode[pil]` Python package (`pip install qrcode[pil]`)

```bash
make all       # regenerate QR + both PDFs
make build     # only PDFs (uses existing qr-github.png)
make qr        # only QR
make clean     # remove built artifacts and temp files
```

Or run scripts directly:

```bash
python generate_qr.py
python generate_pdf.py
```

The renderer starts a local HTTP server on port 8765 so the QR PNG and Google Fonts both load correctly during print.

---

## Visual design notes

- **Two-column grid** (35% / 65%) using CSS Grid with `minmax(0, fr)` to prevent gap overflow
- **Stat strip** with one anchor metric in coral (16pt 800) — the others muted as supporting
- **Coral metric underlines** (`linear-gradient(transparent 60%, ...)`) on quantified facts inline
- **FEATURED project** treatment: 3px coral left border + ~5% coral background tint
- **Code block** with terminal styling, slate background, JetBrains Mono, coral left border
- **QR code** auto-pushed to bottom of left column via `margin-top: auto` on flex sidebar
- **Recent ships timeline** with status dots; live entry marked by a coral pulse-ring dot
- **Inter** for body and headers, **JetBrains Mono** for code, metadata, and timeline labels
- **Build stamp** in muted monospace at the bottom right — date + commit SHA + repo URL

The CV fits 1 page A4 with all 17 hyperlinks preserved as PDF link annotations.

---

## Why open-source the CV

Because if you're hiring me, you're hiring my judgment about how to ship things. The CV itself is something I shipped — read the source the same way you'd read any other repo of mine.

Fork the layout if you want it for your own CV. MIT licensed.

---

## Build stamp

Every render embeds the date and current `git rev-parse --short HEAD` into the footer. If the file says `built 2026-05-03 · main@4f8a2c1`, that's a verifiable claim against this repo's history.

---

## License

[MIT](./LICENSE)
