#zadanie 1

import time

def przetworz_daty(data_od, data_do):
    dataWTimeOd = time.strptime(data_od, "%Y-%m-%d")
    dataWTimeDo = time.strptime(data_do, "%Y-%m-%d")

    roznicaDni = int((time.mktime(dataWTimeDo) - time.mktime(dataWTimeOd)) / (24 * 3600))

    dniTyg = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]

    dzienTygodniaOd = time.localtime(time.mktime(dataWTimeOd)).tm_wday
    dzienTygodniaDo = time.localtime(time.mktime(dataWTimeDo)).tm_wday
    dzienTygodniaOd = dniTyg[dzienTygodniaOd]
    dzienTygodniaDo = dniTyg[dzienTygodniaDo]
    
    print(f"Dzień tygodnia dla {data_od} to {dzienTygodniaOd}, a dla {data_do} to {dzienTygodniaDo}.")
    print(f"Między {data_od} a {data_do} upłynęło {roznicaDni} dni.")
    

data_od = "2023-10-02"
data_do = "2023-11-08"

przetworz_daty(data_od,data_do)

# Zadanie 2

import segno
from PIL import Image

code = segno.make("Warto programować")
code.save("WartoProgramować.pdf", kind='pdf',dark="red", light="yellow")
code.save("WartoProgramować.png",scale=5,dark="purple", light="grey")
qr = Image.open("WartoProgramować.png")
imgObrot = qr.rotate(60,expand=True)
imgObrot.save("ObróconeWartoProgramować.png")