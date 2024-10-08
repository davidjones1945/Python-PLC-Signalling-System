class TratSuhlas:
    def __init__(self, ID, nazovGUI, enumIkon, dictIkon, app, typ):
        self.app = app #inštancia spolupracujúcej triedy
        self.ID =ID #ID traťového súhlasu

        self.nazovGUI = nazovGUI    #názov prvku v GUI

        self.enumIkon = enumIkon    #prepojenie so symbolmi
        self.dictIkon = dictIkon

        self.typ = typ  #smer súhlasu (L - lichý, S - sudý)

        self.smer = False   #smer udeleného TS
        self.volnost = False #vošnosť medzistaničného úseku
        self.ziadost = False    #žiadosť o TS

        self.prijem = False #príjem TS

        self.odchod=False   #aktívna odchodová cesta do úseku

        self.vybrane = False    #výber objektu užívateľom

        self.porBP = False #došlo k poruche blokovej podmienky

    def update(self, app):
        self.setPrijem()

        if self.enumIkon != None:   #ak existuje priradený enum symbolov
                if not self.odchod and self.volnost:    #ak je medzistaničný úsek voľný
                    if self.prijem: #ak je TS prijatý
                        if self.ziadost:    #ak prebieha žiadosť o TS
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PRIJEM_ZIADOST.value])

                        elif self.porBP:  #ak došlo k poruche blokovej podmienky
                             getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PRIJEM_VOLNOST_PORUCHA_BP.value])
                        
                        else:   #základný obraz TS
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PRIJEM_VOLNOST.value])

                    else:   #ak je TS udelený
                        if self.ziadost:    #ak prebieha žiadosť o TS
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.UDELENIE_ZIADOST.value])
                        
                        elif self.porBP:  #ak došlo k poruche blokovej podmienky
                             getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.UDELENIE_VOLNOST_PORUCHA_BP.value])

                        else:    #základný obraz TS
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.UDELENIE_VOLNOST.value])

                else:   #ak je medzistaničný úsek obsadený
                    if self.prijem: #ak je TS prijatý
                        if self.porBP:  #ak došlo k poruche blokovej podmienky
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PRIJEM_PORUCHA_BP.value])

                        else:
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PRIJEM.value])
                    
                    else:   #ak je TS udelený
                        if self.porBP:  #ak došlo k poruche blokovej podmienky
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.UDELENIE_PORUCHA_BP.value])

                        else:
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.UDELENIE.value])

    def setPrijem(self):    #metóda na výpočet príjmu traťového súhlasu
        #príjem TS závisí hlavne od smeru objektu TS vo vizualizácii
        if self.typ == 'S': 
            if self.smer:
                self.prijem = True
            else:
                self.prijem = False

        elif self.typ == 'L':
            if self.smer:
                self.prijem = False
            else:
                self.prijem = True