"""Generate QR code linking to GitHub for CV embedding."""

from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_M
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

OUT = Path(__file__).parent / "qr-github.png"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_M,
    box_size=10,
    border=2,
)
qr.add_data("https://github.com/loplop-h")
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(radius_ratio=1.0),
    fill_color=(15, 28, 48),
    back_color=(255, 255, 255),
)
img.save(OUT)
print(f"Wrote {OUT}  ({OUT.stat().st_size // 1024} KB)")
