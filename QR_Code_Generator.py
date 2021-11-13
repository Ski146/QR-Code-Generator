import pyqrcode
import png
from pyqrcode import QRCode
# String which represents the QR code
s = input("enter the url:")
# Generate QR code
url = pyqrcode.create(s)
url.show('myqr.png')
url.png('myqr.png', scale=6)