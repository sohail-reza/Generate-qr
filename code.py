import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = input("Enter the web address for which you require the qr code: ")
# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("myqr1.svg","myqr.png", scale=8)