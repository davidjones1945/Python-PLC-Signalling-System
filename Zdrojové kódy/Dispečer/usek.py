class Usek:
    def __init__(self, ID:int, nazovGUI:str, enummIkon, dictIkon, app):
        self.app = app  #inštancia spolupracujúcej triedy
        self.ID = ID    #ID úseku

        self.nazovGUI = nazovGUI    #názov úseku v GUI

        self.enumIkon = enummIkon   #prepojenie so symbolmi
        self.dictIkon = dictIkon

        self.jeVolny:bool = False    #informácia o voľnosti úseku

        self.stavanie:str = ' ' #typ cesty v úseku
        self.cesta:str = ' '    #typ stavanej cesty v úseku

        self.vyberVlak:bool = False  #úsek je vybraný pre stavanie vlakovej cesty

        self.zaver:bool = False  #úsek je pod záverom jazdnej cesty

        self.odozva:bool = True  #odozva koľajového obvodu

    def update(self):  #metóda pre aktualizáciu symbolu úseku
        self.rusenieCesty()

        if self.odozva: #ak je prijatá informácia o stave úseku
            if self.jeVolny:    #ak je úsek voľný
                if self.stavanie == 'Vlak': #self.stavanieVlak:   #ak je úsek vybratý pre vlakovú cestu
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_VC.value])

                elif self.stavanie == 'Posun': #self.stavaniePosun:    #ak je úsek vybratý pre posunovú cestu
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_PC.value])

                elif self.stavanie == 'OchrDr': #self.stavanieOchr:    #ak je úsek vybratý pre ochrannú
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_OD.value])

                elif self.cesta == 'Vlak': #self.vlak: #ak je úsek vo vlakovej ceste
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VLAK.value])

                elif self.cesta == 'Posun': #self.posun:    #ak je úsek v posunovej ceste
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN.value])

                elif self.cesta == 'OchrDr': #self.ochr:    #ak je úsek v ovhrannej dráhe
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
        if (self.cesta == 'Vlak' or self.cesta == 'Posun') and not self.jeVolny:
            self.cesta = ' '