import copy

class Okienko:
    
    def __init__(self, typ : str, czas_obsługi = 0):
        self.typ = typ
        self.czas_obsługi = czas_obsługi
        if self.typ == "D": self.typ = "E"
        
    def status(self) -> list:
        return [self.typ, self.czas_obsługi]
        
class Urząd:
    
    def __init__(self,  liczba_okien : list):
        self.liczba_okien = liczba_okien
        self.okienka = []
        typ = 0
        for l in self.liczba_okien:
            for i in range(l):
                self.okienka.append(Okienko(str(chr(65 + typ))).status())
            typ+=1
        self.obsłueni_klienci = [0 for i in range(len(self.okienka))]
    
    def przyjęcie_klienta(self,typ_problemu,złozoność):
        try:
            self.wolne_okno = self.okienka.index([typ_problemu,0])
            self.okienka[self.wolne_okno][1] = złozoność
            self.obsłueni_klienci[self.wolne_okno] += 1
        except:
            try:
                self.wolne_okno = self.okienka.index(["E",0])
                self.okienka[self.wolne_okno][1] = złozoność
                self.obsłueni_klienci[self.wolne_okno] += 1
            except:
                return False
        return True
        
    def mijanie_czasu(self):
        for i in range(len(self.okienka)):
            if self.okienka[i][1] > 0:
                self.okienka[i][1] -= 1
        
    
    def okna(self):
        return self.okienka
    
    def obsłuzeni(self):
        return self.obsłueni_klienci
   
   
def Czas_na_wykonanie_zadań(urząd : Urząd, klienci : list):
    
    CZAS = 0
    układ = copy.deepcopy(urząd.okna())
    urząd.przyjęcie_klienta("A",1)
    klienci_kopia = copy.deepcopy(klienci)

    while urząd.okna() != układ:
        urząd.mijanie_czasu()
        obsługiwani = []
        for klient in klienci_kopia:
            if urząd.przyjęcie_klienta(*klient): 
                obsługiwani.append(klient)
            if len(obsługiwani) == 10: break
        for klient in obsługiwani:
            klienci_kopia.remove(klient)
        CZAS += 1

    urząd.obsłuzeni()[0] -= 1
    
    return CZAS, urząd.obsłuzeni()

