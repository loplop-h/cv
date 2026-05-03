# max-cv build targets
# Requires: Python 3.12+, Chrome installed, qrcode[pil] package

PYTHON ?= python

.PHONY: all build qr clean help

all: qr build

build:
	$(PYTHON) generate_pdf.py

qr:
	$(PYTHON) generate_qr.py

clean:
	rm -f .stamped-*.html
	rm -f cv-max-huisman-*.pdf

help:
	@echo "make build  - rebuild both PDFs from HTML (injects build stamp from git)"
	@echo "make qr     - regenerate qr-github.png"
	@echo "make all    - qr + build"
	@echo "make clean  - remove built artifacts and temp files"
