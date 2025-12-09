import qrcode
from PIL import Image
from datetime import datetime
import sys
import os

def make_qr_with_logo(data, logo_path="logo.png", out_prefix="qr_logo"):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    except Exception as e:
        print("Failed to create QR:", e)
        return None

    # Try to load and paste logo; if fails, continue without logo
    if logo_path and os.path.isfile(logo_path):
        try:
            logo = Image.open(logo_path)
            # Ensure image is RGBA for mask handling
            if logo.mode not in ("RGBA", "LA"):
                logo = logo.convert("RGBA")
            qr_width, qr_height = img_qr.size
            # Keep logo <= 20% of QR width (safe)
            logo_size = qr_width // 5
            logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS)
            pos = ((qr_width - logo.size[0]) // 2, (qr_height - logo.size[1]) // 2)
            img_qr.paste(logo, pos, mask=logo)
        except Exception as e:
            print("Warning: could not use logo (continuing without it). Error:", e)

    filename = f"{out_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    img_qr.save(filename)
    return filename

if __name__ == "__main__":
    data = input("Enter text or URL for QR: ").strip()
    if not data:
        print("No data entered. Exiting.")
        sys.exit(1)

    out = make_qr_with_logo(data)
    if out:
        print("Saved:", out)
    else:
        print("QR generation failed.")
