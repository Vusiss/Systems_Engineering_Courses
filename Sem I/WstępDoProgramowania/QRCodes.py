# Zadanie 2

import segno
from PIL import Image

code = segno.make("Warto programować")
code.save("WartoProgramować.pdf", kind='pdf',dark="red", light="yellow")
code.save("WartoProgramować.png",scale=5,dark="purple", light="grey")
qr = Image.open("WartoProgramować.png")
imgObrot = qr.rotate(60,expand=True)
imgObrot.save("ObróconeWartoProgramować.png")

