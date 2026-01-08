class Usek:
    def __init__(self, ID, nazovGUI, enummIkon, dictIkon, app):
        self.app = app  #inštancia spolupracujúcej triedy
        self.ID = ID    #ID úseku

        self.nazovGUI = nazovGUI    #názov úseku v GUI

        self.enumIkon = enummIkon   #prepojenie so symbolmi
        self.dictIkon = dictIkon

        self.jeVolny = False    #informácia o voľnosti úseku

        self.stavanieVlak = False   #prebieha stavanie vlakovej cesty
        self.stavaniePosun = False  #prebieha stavanie posunovej cesty
        self.stavanieOchr = False  #prebieha stavanie ochrannej dráhy

        self.vyberVlak = False  #úsek je vybraný pre stavanie vlakovej cesty
        self.vyberPosun = False #úsek je vybraný pre stavanie posunovej cesty

        self.vlak = False   #v úseku je postavená vlaková cesta
        self.posun = False  # v úseku je postavená posunová cesta
        self.ochr = False   #v úseku je postavená ochrnná dráha

        self.zaver = False  #úsek je pod záverom jazdnej cesty

        self.odozva = True  #odozva koľajového obvodu

    def update(self, app):  #metóda pre aktualizáciu symbolu úseku
        self.rusenieCesty()

        if self.odozva: #ak je prijatá informácia o stave úseku
            if self.jeVolny:    #ak je úsek voľný
                if self.stavanieVlak:   #ak je úsek vybratý pre vlakovú cestu
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_VC.value])

                elif self.stavaniePosun:    #ak je úsek vybratý pre posunovú cestu
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_PC.value])

                elif self.stavanieOchr:    #ak je úsek vybratý pre ochrannú
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_OD.value])

                elif self.vlak: #ak je úsek vo vlakovej ceste
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VLAK.value])

                elif self.posun:    #ak je úsek v posunovej ceste
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN.value])

                elif self.ochr:    #ak je úsek v ovhrannej dráhe
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.OCHR.value])

                elif self.vyberVlak:    #ak prebieha výber vlakovej cesty
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VYBER_VC.value])

                else:   #základné zobrazenie úseku
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNA.value])

            else:    #ak je úsek obsadený
                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.OBSAD.value])

        else: #informácia o úseku neexistuje
            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.MRTVA.value])

    def rusenieCesty(self): #metóda volaná pri rušení cesty jazdou vlaku
        if (self.vlak or self.posun) and not self.jeVolny:
            self.vlak = False
            self.posun = False