import pyqrcode
import png  # For saving as PNG
from pyqrcode import QRCode

# Data to encode
data = "https://youtu.be/TMY1g8pAktk?list=RDTMY1g8pAktk"

# Create QR Code
qr = pyqrcode.create(data)

# Save as PNG
qr.png("qrcode.png", scale=8)

# Optionally, save as SVG
qr.svg("qrcode.svg", scale=8)

print("QR Code created successfully!")