import qrcode
from datetime import datetime

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    img.save(filename)

    return filename


if __name__ == "__main__":
    text = input("Enter text or URL for QR: ").strip()

    if text:
        file = generate_qr(text)
        print(f"QR Generated Successfully: {file}")
    else:
        print("No input provided!")

