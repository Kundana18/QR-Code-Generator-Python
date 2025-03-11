import qrcode
myqr =  qrcode.make("https://github.com/")
myqr1 = qrcode.make("https://github.com/Kundana18/QRCode-Generator-Python")
myqr.save("myqr.png", scale = 8)
myqr1.save("myqr1.png", scale = 6)






