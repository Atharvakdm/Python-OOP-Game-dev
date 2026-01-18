import qrcode
#download qrcode by pip install qrcode[pil]
img = qrcode.make(input("Enter URL: "))
img.save("qrcode.png")
