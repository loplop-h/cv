"""Generate pixel-perfect PDF from CV HTML using headless Chrome.

Injects a build stamp (date + git short SHA) into placeholders before rendering,
then restores the source HTML so the placeholders stay in version control.

Why headless Chrome (not Chrome's native print dialog):
  - Background graphics ON (coral accents, code block, slate bars all render)
  - Fonts embedded (Inter + JetBrains Mono in the PDF itself)
  - No automatic headers/footers
  - @page CSS margins respected
  - Deterministic output (same on any machine)
  - A4 paper explicitly forced (default would be Letter)

Run after editing the HTML:
    make build
    # or directly:
    python generate_pdf.py
"""

from __future__ import annotations

import re
import shutil
import subprocess
import time
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

SERVER_URL = "http://localhost:8765"
SERVER_PORT = 8765

JOBS: list[tuple[str, str]] = [
    ("cv-max-huisman-v3.html", "cv-max-huisman-v3.pdf"),
    ("cv-max-huisman-v2.html", "cv-max-huisman-v2.pdf"),
]


def get_build_stamp() -> tuple[str, str]:
    """Return (date, short_sha) for the build stamp."""
    today = date.today().isoformat()
    try:
        sha = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        sha = "unstamped"
    return today, sha


def render_html_with_stamp(src: Path, build_date: str, build_sha: str) -> Path:
    """Replace {{BUILD_*}} placeholders, write to a temp HTML, return its path."""
    text = src.read_text(encoding="utf-8")
    text = text.replace("{{BUILD_DATE}}", build_date)
    text = text.replace("{{BUILD_SHA}}", build_sha)
    out = ROOT / f".stamped-{src.name}"
    out.write_text(text, encoding="utf-8")
    return out


def ensure_server_running() -> subprocess.Popen | None:
    """Start a local HTTP server if not already running. Return process handle."""
    try:
        urllib.request.urlopen(f"{SERVER_URL}/", timeout=1)
        return None
    except Exception:
        pass
    proc = subprocess.Popen(
        ["python", "-m", "http.server", str(SERVER_PORT)],
        cwd=str(ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    for _ in range(30):
        time.sleep(0.2)
        try:
            urllib.request.urlopen(f"{SERVER_URL}/", timeout=1)
            return proc
        except Exception:
            continue
    raise RuntimeError("Local HTTP server did not start in time")


def render_pdf(html_name: str, pdf_name: str, build_date: str, build_sha: str) -> None:
    src = ROOT / html_name
    dst = ROOT / pdf_name
    if not src.exists():
        print(f"  ! skip {html_name} (not found)")
        return

    stamped = render_html_with_stamp(src, build_date, build_sha)
    A4_W_IN = "8.27"
    A4_H_IN = "11.69"
    cmd = [
        str(CHROME),
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--no-margins",
        f"--paper-width={A4_W_IN}",
        f"--paper-height={A4_H_IN}",
        "--virtual-time-budget=15000",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={dst}",
        f"{SERVER_URL}/{stamped.name}",
    ]
    print(f"  rendering {html_name} -> {pdf_name}  ({build_date} · {build_sha})")
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        stamped.unlink()
    except OSError:
        pass
    if dst.exists():
        kb = dst.stat().st_size // 1024
        print(f"    -> {dst}  ({kb} KB)")
    else:
        raise RuntimeError(f"PDF not produced for {html_name}")


def main() -> None:
    if not CHROME.exists():
        raise SystemExit(f"Chrome not found at {CHROME}")

    build_date, build_sha = get_build_stamp()
    server = ensure_server_running()
    try:
        for html, pdf in JOBS:
            render_pdf(html, pdf, build_date, build_sha)
    finally:
        if server is not None:
            server.terminate()
            try:
                server.wait(timeout=3)
            except subprocess.TimeoutExpired:
                server.kill()
    print(f"\nDone. PDFs saved next to this script.\nBuild stamp: {build_date} · {build_sha}")


if __name__ == "__main__":
    main()
