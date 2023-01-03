import qrcode

img = qrcode.make("I am coming for you!")
img.save("QR.png")
