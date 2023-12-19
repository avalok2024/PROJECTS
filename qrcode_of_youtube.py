import qrcode
from PIL import Image
qr = qrcode.QRCode(version=10.5, error_correction=qrcode.constants.ERROR_CORRECT_H, border=4, box_size=10)
qr.add_data("https://www.youtube.com/")
qr.make(fit=True)
image = qr.make_image(fill_color= "red", back_color= "white")
image.save("youtube.png")

