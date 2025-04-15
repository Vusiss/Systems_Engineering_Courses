class MT:
    def __init__(self, zb_stnw, alfbt_wej, alfbt_tsm, fun_prz, stn_p, stn_ak, stn_od):
        self.zb_stnw = zb_stnw
        self.alfbt_wej = alfbt_wej
        self.alfbt_tsm = alfbt_tsm
        self.fun_prz = fun_prz
        self.stn_p = stn_p
        self.stn_ak = stn_ak
        self.stn_od = stn_od
        self.blank = '˽'

    def start(self, slowo):
        tasm = list(slowo) + [self.blank]
        glw_idx = 0
        stn = self.stn_p

        while stn != self.stn_ak and stn != self.stn_od:
            
            # Dodaje puste miejsce na koniec taśmy, gdy głowica jest na końcu
            if glw_idx >= len(tasm):
                tasm.append(self.blank)
            symbol = tasm[glw_idx]

            # Wyświetla aktualny stan taśmy
            lewa = ''.join(tasm[:glw_idx]) if glw_idx != 0 else ''
            prawa = ''.join(tasm[glw_idx:]) if glw_idx+1 < len(tasm) else ''
            print(f"{lewa}{stn}{prawa}")

            # Sprawdza, czy przejście istnieje
            if (stn, symbol) not in self.fun_prz:
                print(f"Brak przejścia dla ({stn}, {symbol}) – maszyna zatrzymana.")
                break

            nowy_stn, nowy_symbol, ruch = self.fun_prz[(stn, symbol)]
            tasm[glw_idx] = nowy_symbol
            stn = nowy_stn


            # Przesuwa głowicę
            if ruch == 'R':
                glw_idx += 1
                if glw_idx >= len(tasm):  # Dodaje puste miejsce na koniec taśmy, gdy głowica jest na końcu
                    tasm.append(self.blank)
            elif ruch == 'L':
                glw_idx -= 1
                if glw_idx < 0: # Gdy głowica ma wejśc przed taśmę, wraca na początek
                    glw_idx = 0

        lewa = ''.join(tasm[:glw_idx]) if glw_idx != 0 else ''
        prawa = ''.join(tasm[glw_idx:]) if glw_idx+1 < len(tasm) else ''
        print(f"{lewa}{stn}{prawa}")

        if stn == self.stn_ak:
            print("Słowo zostało zaakceptowane.")
        elif stn == self.stn_od:
            print("Słowo zostało odrzucone.")
        else:
            print("Maszyna zakończyła działanie w stanie nieakceptującym.")


zb_stnw = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'qr', 'qa']
alfbt_wej = ['a']  # alfabet wejściowy
alfbt_tsm = ['a', '˽','α','/']  # alfabet taśmy
fun_prz = {
    ('q0', 'a'): ('q1', 'α', 'R'),
    ('q0', '˽'): ('qr', '˽', 'L'),
    
    ('q1', 'a'): ('q2', 'a', 'L'),
    ('q1', '˽'): ('qa', '˽', 'L'),
    ('q1', '/'): ('q1', '/', 'R'),
    
    ('q2', '/'): ('q2', '/', 'L'),
    ('q2', 'α'): ('q3', 'α', 'L'),
    
    ('q3', '/'): ('q3', '/', 'R'),
    ('q3', 'a'): ('q4', 'a', 'R'),
    ('q3', 'α'): ('q4', 'α', 'R'),
    ('q3', '˽'): ('q6', '˽', 'L'),
    
    ('q4', 'a'): ('q5', '/', 'R'),
    ('q4', '/'): ('q4', '/', 'R'),
    ('q4', '˽'): ('qr', '˽', 'L'),
    
    ('q5', 'a'): ('q3', '/', 'R'),
    ('q5', '/'): ('q5', '/', 'R'),
    ('q5', '˽'): ('qr', '˽', 'L'),
    
    ('q6', 'a'): ('q6', 'a', 'L'),
    ('q6', '/'): ('q6', '/', 'L'),
    ('q6', 'α'): ('q1', 'α', 'R'),
    
    ('qr', 'a'): ('qr', 'a', 'R'),
    ('qr', '˽'): ('qr', '˽', 'R'),
    ('qr', 'α'): ('qr', 'α', 'R'),
    
    ('qa', 'a'): ('qa', 'a', 'R'),
    ('qa', '˽'): ('qa', '˽', 'R'),
    ('qa', 'α'): ('qa', 'α', 'R')
}
stn_p = 'q0'
stn_ak = 'qa'
stn_od = 'qr'
word = "aaa"

mt = MT(zb_stnw, alfbt_wej, alfbt_tsm, fun_prz, stn_p, stn_ak, stn_od)
mt.start(word)