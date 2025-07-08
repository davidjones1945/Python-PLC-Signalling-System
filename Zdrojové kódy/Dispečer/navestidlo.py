class Navestidlo:
    def __init__(self, ID:int, nazov:str, nazovGUI:str, enumIkon, dictIkon, app, usekPred:str = 'X', zavisle:int = -1,  usekZa:str = 'X', oddielove:bool = False, TZZ:str = ' ', comboBox:str = ' '):
        self.app = app  #inštancia spolupracujúcej triedy
        self.ID = ID    #ID návestidla

        self.nazov = nazov  #názov návestidla
        self.nazovGUI = nazovGUI    #názov návestidla v GUI

        self.enumIkon = enumIkon    #prepojenie so symbolmi
        self.dictIkon = dictIkon    

        self.usekPred = usekPred    #úsek pred návestidlom (nitné kvôli správnemu symbolu)
        self.usekZa = usekZa #definícia prvého úseku za návestidlom
        self.jeVolnyPred:bool = False    #voľnosť úseku pred návestidlom
        self.jeVolnyZa:bool = False #voľnosť úseku za návestidlom
        self.usekOdozva:bool = False  #úsek pred návestidlom je mŕtvy

        self.vybrane:bool = False    #výber návestidla obsluhou

        self.stavanieOd:bool = False #aktívne stavanie cesty od návestidla
        self.stavanieDo:bool = False #aktívne stavenie cesty k nívestidlu        

        self.zaverVC:bool = False    #je vykonaný źáver vlakovej cesty
        self.zaverPC:bool = False    #je vykonaný źáver posunovej cesty

        self.cesta:str = ' '    #typ cesty postavenej v úseku s návestidlom

        self.rusenie:bool = False    #je aktívne rušenie cesty

        self.znak:str = 'Stoj'  #aktuálny typ návestného znaku

        self.pociatocne:bool = False #návestidlo je počiatočným návestidlom postavenej jazdnej cesty
        self.typAktCes:str = ' ' #typ cesty počiatočného návestidla (0-vlaková, 1-posunová)
        self.manual:bool = False #manuálne ovládanie návesti na počiatočnom návestidle

        self.OD:bool = False #za návestidlom pokračuje ochranná dráha
        self.koncove:bool = False

        self.TZZ = TZZ  #typ TZZ
        self.oddielove = oddielove  #definícia oddielového návestidla
        self.zhasnute:bool = False #väzba TS na AB3

        self.predhlaska:bool = False #príjem predhlášky na návestidlo

        self.zavisle = zavisle  #definícia závislých symbolov jedného návestidla v dispečerskej aplikácii

        self.comboBox = comboBox #dafinícia priradeného comboBox-u k návestidlu

    def update(self, app):  #metóda pre aktualizáciu symbolu návestidla
        if not self.oddielove:  #ak nie je oddielové
            self.rusenieCesty()
            self.zmenaNavesti()
            if self.usekOdozva: #ak je z úseku pred návestidlom aktívna odozva
                if self.jeVolnyPred:    #ak je úsek pred návestidlom voľný
                    if self.vybrane:    #ak je návestidlo vybrané obsluhou
                        if self.cesta == 'Posun': #self.posun:  #počas posunu
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_PC_VYB.value])

                        elif self.zaverVC:    #počas záveru vlakovej cesty
                            if self.znak == 'Stoj': #ak je aktuálny typ návestného znaku 'Stoj'
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_ZAVER_VC_VYB.value])
                        
                            elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_ZAVER_VC_VYB.value])

                            elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_ZAVER_VC_VYB.value])

                            elif self.znak == 'PN': #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PN_ZAVER_VC_VYB.value])
                        
                        elif self.zaverPC:  #počas záveru posunovej cesty
                            if self.znak == 'Stoj': #ak je aktuálny typ návestného znaku 'Stoj'
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_ZAVER_PC_VYB.value])
                        
                            elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_ZAVER_PC_VYB.value])

                            elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_ZAVER_PC_VYB.value])

                            elif self.znak == 'PN': #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PN_ZAVER_PC_VYB.value])
                        
                        elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_V.value])                        

                        elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_V.value])

                        elif self.znak == 'PN':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_V_PN.value])

                        else:   #základný obraz návestidla vybraného obsluhou
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_V.value])                            

                    elif self.stavanieOd:   #ak je návestidlo vybrané ako počiatočné návestidlo jazdnej cety
                        if self.zaverVC:    #ak je návestidlo koncovým bodom inej vlakovej cesty
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_STAVANIE_START.value])
                        
                        elif self.zaverPC:  #ak je návestidlo koncovým bodom inej posunovej cesty
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_STAVANIE_START.value])
                        
                        elif self.stavanieDo:   #ak je návestidlo vybrané ako koncové návestidlo inej jazdnej cety
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAV_STAVANIE_START.value])
                        
                        elif self.rusenie:  #ak prebieha rušenie inej jazdnej cesty
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.RUS_STAVANIE_START.value])

                        else:   #základný obraz počiatočného návestidla
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_STAVANIE_START.value])

                    elif self.cesta == 'Vlak': #self.vlak: #ak je úsek pred návestidlom súčasťou vlakovej cesty
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_VC.value])

                    elif self.cesta == 'Posun': #self.posun:   #ak je úsek pred návestidlom súčasťou posunovej cesty
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_PC.value])

                    elif self.cesta == 'OchrDr': #self.ochr:   #ak je úsek pred návestidlom súčasťou posunovej cesty
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_OD.value])

                    elif self.stavanieDo:   #ak je návestidlo vybrané ako koncové návestidlo jazdnej cety
                        if self.znak == 'Stoj': #ak je aktuálny typ návestného znaku 'Stoj'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_ZAVER_STAVANIE.value])
                        
                        elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_ZAVER_STAVANIE.value])
                        
                        elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_ZAVER_STAVANIE.value])

                        elif self.znak == 'PN': #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PN_ZAVER_STAVANIE.value])

                    elif self.zaverVC:  #ak je návestidlo koncovým bodom vlakovej cesty
                        if self.znak == 'Stoj': #ak je aktuálny typ návestného znaku 'Stoj'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_ZAVER_VC.value])
                        
                        elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_ZAVER_VC.value])
                        
                        elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_ZAVER_VC.value])

                        elif self.znak == 'PN': #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PN_ZAVER_VC.value])

                    elif self.zaverPC:  #ak je návestidlo koncovým bodom posunovej cesty
                        if self.znak == 'Stoj': #ak je aktuálny typ návestného znaku 'Stoj'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_ZAVER_PC.value])
                        
                        elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_ZAVER_PC.value])

                        elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_ZAVER_PC.value])

                        elif self.znak == 'PN': #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PN_ZAVER_PC.value])

                    elif self.rusenie:  #ak prebieha rušenie jazdnej cesty
                        if self.znak == 'Stoj': #ak je aktuálny typ návestného znaku 'Stoj'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.RUSENIE.value])
                        
                        elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_RUSENIE.value])

                        elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_RUSENIE.value])

                        elif self.znak == 'PN': #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PN_RUSENIE.value])

                    elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO.value])

                    elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN.value])

                    elif self.znak == 'PN':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_PN.value])

                    else:   #základný obraz návestidla
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ.value])

                else:   #ak je úsek pred návestidlom obsadený

                    if self.vybrane:    #ak je návestidlo vybrané obsluhou
                        if self.zaverPC:    #ak je vytvorený záver posunovej cesty
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_ZAVER_PC_VYB.value])

                        elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_OBS_V.value])

                        elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_V_OBS.value])
                            
                        elif self.znak == 'PN':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_OBS_V_PN.value])

                        else:   #základný obraz návestidla vybraného obsluhou
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_OBS_V.value])

                    elif self.stavanieOd:   #ak je návestidlo vybrané ako počiatočné návestidlo jazdnej cety
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_STAVANIE_START_OBS.value])

                    elif self.zaverPC:  #ak je návestidlo koncovým bodom posunovej cesty
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_ZAVER_PC.value])

                    elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_OBS.value])

                    elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_OBS.value])

                    elif self.znak == 'PN':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_OBS_PN.value])

                    else:   #základný obraz návestidla
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_OBS.value])
            
            else:   #úsek pred návestidlom je mŕtvy
                if self.vybrane:    #ak je návestidlo vybrané obsluhou
                    if self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_MRTVE_V.value])

                    elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_V_MRTVE.value])

                    elif self.znak == 'PN':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_MRTVE_V_PN.value])

                    elif self.znak == 'Stoj':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_MRTVE_V.value])

                elif self.stavanieOd:   #ak je návestidlo vybrané ako počiatočné návestidlo jazdnej cety
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_STAVANIE_START_MRTVE.value])

                elif self.znak == 'Vlak':  #ak je aktuálny typ návestného znaku 'Voľno'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_MRTVE.value])

                elif self.znak == 'Posun':  #ak je aktuálny typ návestného znaku 'Posun dovolený'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_MRTVE.value])

                elif self.znak == 'PN':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_MRTVE_PN.value])

                elif self.znak == 'Stoj':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_MRTVE.value])
    
        else:   #oddielové návestidlo
            if self.TZZ == 'AB3':   #autobloku
                if self.jeVolnyPred:    #ak je úsek pred návestidlom voľný
                    if self.zhasnute:   #ak je návestidlo zhasnuté
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZHASNUTE.value])

                    elif self.jeVolnyZa:    #ak je úsek za návestidlom voľný
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO.value])

                    else:   #základný obraz návestidla
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ.value])

                else:   #ak je úsek pred návestidlom obsadený
                    if self.zhasnute:   #ak je návestidlo zhasnuté
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZHASNUTE_OBS.value])
                    
                    elif self.jeVolnyZa:      #ak je úsek za návestidlom voľný
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_OBS.value])

                    else:   #základný obraz návestidla
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_OBS.value])
            
            elif self.TZZ == 'AH':  #automatického hradla
                self.ruseniePredhlasky()
                if self.jeVolnyPred:    #ak je úsek pred návestidlom voľný
                    if self.vybrane:    #ak je návestidlo vybrané obsluhou
                        if self.predhlaska and self.jeVolnyZa:    #ak je úsek za návestidlom voľný
                            if self.manual:
                                if self.znak == 'Vlak':
                                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_V.value])
                        
                                elif self.znak == 'Stoj':
                                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_V.value])

                            else:
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_V.value])
                            
                        elif self.znak == 'PN':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_V_PN.value])

                        else:   #základný obraz návestidla vybraného obsluhou
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_V.value])

                    elif self.predhlaska and self.jeVolnyZa:      #ak je úsek za návestidlom voľný
                        if self.manual:
                            if self.znak == 'Vlak':
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO.value])
                        
                            elif self.znak == 'Stoj':
                                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ.value])
                        
                        else:
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO.value])
                    
                    elif self.znak == 'PN':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_PN.value])

                    else:   #základný obraz návestidla
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ.value])

                else:   #ak je úsek pred návestidlom obsadený
                    if self.vybrane:    #ak je návestidlo vybrané obsluhou
                        if self.predhlaska and self.jeVolnyZa:    #ak je úsek za návestidlom voľný
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_OBS_V.value])
                            
                        elif self.znak == 'PN':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_OBS_V_PN.value])

                        else:   #základný obraz návestidla vybraného obsluhou
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_OBS_V.value])

                    elif self.predhlaska and self.jeVolnyZa:      #ak je úsek za návestidlom voľný
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VOLNO_OBS.value])

                    elif self.znak == 'PN':  #ak je aktuálny typ návestného znaku 'Privolávacia návesť'
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_OBS_PN.value])

                    else:   #základný obraz návestidla
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STOJ_OBS.value])

    def rusenieCesty(self): #metóda volaná pri rušení jazdnej cesty
        if (self.cesta == 'Vlak' or self.cesta == 'Posun' or self.zaverVC or self.zaverPC) and not self.jeVolnyPred:    #ak je úsek pred návestidlom obsadený a návestidlo má príznak vlakovej cesty alebo jej záveru
            self.cesta = ' '
            self.zaverVC = False
            self.zaverPC = False
            if self.OD: #ak je za návestidlom ochranná dráha
                self.app.vlaknoCasOchrDrahy.start_timer()    #spusti časový súbor rušenia ochrannej dráhy (30 s)
            else:
                self.stavanieDo = False

    def zmenaNavesti(self): #metóda zobrazí zakazujúci návestný znak po prejazde vlaku za návestidlo
        if ((self.znak == 'Vlak') and (not self.jeVolnyZa)) or (
        (self.znak == 'Posun') and (not self.jeVolnyZa) and self.jeVolnyPred):
            self.znak = 'Stoj'
            self.pociatocne = False
            self.manual = False
            self.app.prikazDoPLC(adresat='navestidlo', prikaz='/Stoj', id=self.ID, nazov=self.nazov)

    def ruseniePredhlasky(self):    #metóda pre rušenie predhlášky pri prejatzde vlaku okolo hradla na trati
        if (not self.jeVolnyPred) and (not self.jeVolnyZa):
            self.predhlaska = False