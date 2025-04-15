import segno
from PIL import Image


qr = segno.make_qr("Warto programować")
qr.save("WartoProgramować.png",scale = 5)

img = Image.open("WartoProgramować.png")

imgObrot = img.rotate(60, expand=True)

imgObrot.show()
imgObrot.save("ObróconeWarto Programować.png")