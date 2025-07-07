class Vyhybka:
    def __init__(self, ID:int, IDsmer:int, nazovGUI:str, usek:str, enumIkon, dictIkon, app, spojka:bool = False, zavisla:int = -1, druhaVymena:int = -1):
        self.app = app  #inštancia spolupracujúcej triedy
        self.ID = ID    #ID výhybky
        self.IDsmer = IDsmer #ID pre načítanie smeru výhybky

        self.nazovGUI = nazovGUI    #názov výhybky v grafickom zobrazení
        self.usek = usek    #úsek, do ktorého výhybka patrí
        
        self.enumIkon = enumIkon    #prepojenie so symbolmi
        self.dictIkon = dictIkon

        self.jeVolny:bool = False     #informácia o voľnosti úseku
        self.vyber:bool = False  #informácia o výbere výhybky pre obsluhu

        self.smer:bool = True    #aktuálny smer výhybky (1-priamy, 0-odbočný)
        self.lastSmer:bool = True    #vnútorná pamäťová premenná predošlého smeru výhybky
        self.prest:bool = False  #aktuálne prestavovanie výhybky (1-áno, 0-nie)

        self.stavanie:str = ' '

        self.cesta:str = ' '

        self.zaver:bool = False  #výhybka je pod záverom jazdnej cesty

        self.spojka = spojka #výhybka je súčasťou koľajovej spojky
        self.druhaVymena = druhaVymena #ID druhej výmeny v koľajovej spojke

        self.prejazd:bool = False #informácia o prejazde vlaku cez výhybkový úsek

        self.zavisla = zavisla  #závislé symboly výhybiek v dispečerskej aplikácii

        # smer | prest || out
        #    1   |   0   || smer +
        #    0   |   0   || smer -
        #    1   |   1   || prestavovanie + > -
        #    0   |   1   || prestavovanie - > +
   
    def update(self, app):  #metóda pre aktualizáciu symbolu výhybky
        self.prestavenieEnd()
        self.rusenieCesty()        
        self.lastSmer = self.smer   #zápis aktuálneho smeru výhybky ako predošlého smeru

        if self.enumIkon != None:   #ak existuje priradený enum symbolov
            if self.jeVolny:    #ak je úsek výhybky voľný
                if self.smer:   #ak je výhybka prestavená v priamom smere
                    if self.vyber:  #ak je výhybka vybraná obsluhou
                        if self.cesta == 'Vlak': #self.vlak:  #počas vlakovej cesty 
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VLAK_P_V.value])

                        elif self.cesta == 'Posun': #self.posun:    #počas posunovej cesty
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_P_V.value])

                        elif self.cesta == 'OchrDr': #self.ochr: #počas ochrannej dráhy  
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.OCHRANA_P_V.value])

                        elif self.zaver:  #ak je pod záverom
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZAVER_P_V.value])

                        else:   #základný obraz vabranej výhybky
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PRIAMA_VYBER.value])

                    elif self.prest:    #ak sa výhybka prestavuje do odbočnej polohy
                        if self.stavanie == 'Vlak':   #ak sa stavia vlaková cesta 
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_VC_O_P.value])
                        
                        elif self.stavanie == 'Posun':    #ak sa stavia posunová cesta 
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_PC_O_P.value])
                            
                        elif self.stavanie == 'OchrDr':    #ak sa stavia posunová cesta 
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_OD_O_P.value])

                        else:   #základný obraz prestavujúcej sa výmeny
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PREST_M.value])

                    elif self.stavanie == 'Vlak': #ak je výhybka súčasťou vybranej vlakovej cesty
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_VC_P_P.value])

                    elif self.stavanie == 'Posun':    #ak je výhybka súčasťou vybranej posunovej cesty
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_PC_P_P.value])

                    elif self.zaver:  #ak je pod záverom
                        if self.cesta == 'OchrDr': #elf.ochr:   #pre ochrannú dráhu
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.OCHRANA_P.value])

                        elif self.cesta == 'Vlak': #self.vlak: #pre vlakovú cestu
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VLAK_P.value])

                        elif self.cesta == 'Posun': #self.posun:    #pre posunovú cestu
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_P.value])

                        else:   #kvôli bočnej ochrane
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZAVER_P.value])                      

                    else:   #základný obraz výhybky
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PRIAMA.value])

                else:   #ak je výhybka prestavená v odbočnom smere
                    if self.vyber:  #ak je výhybka vybraná obsluhou
                        if self.cesta == 'Vlak': #self.vlak:   #počas vlakovej cesty 
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VLAK_M_V.value])

                        elif self.cesta == 'Posun': #self.posun:    #počas posunovej cesty 
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_M_V.value])

                        elif self.cesta == 'OchrDr': #self.ochr: #počas ochrannej dráhy    
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.OCHRANA_M_V.value])

                        else:   #základný obraz vabranej výhybky
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ODB_VYBER.value])

                    elif self.prest:    #ak sa výhybka prestavuje do priamej polohy
                        if self.stavanie == 'Vlak':   #ak sa stavia vlaková cesta 
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_VC_P_M.value])

                        elif self.stavanie == 'Posun':    #ak sa stavia posunová cesta 
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_PC_P_M.value])

                        elif self.stavanie == 'OchrDr':    #ak sa stavia posunová cesta 
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_OD_P_M.value])

                        else:   #základný obraz prestavujúcej sa výmeny
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PREST_P.value])

                    elif self.stavanie == 'Vlak': #ak je výhybka súčasťou vybranej vlakovej cesty
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_VC_O_M.value])

                    elif self.stavanie == 'Posun':    #ak je výhybka súčasťou vybranej posunovej cesty
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.STAVANIE_PC_O_M.value])

                    elif self.zaver:  #ak je pod záverom
                        if self.cesta == 'OchrDr': #self.ochr:   #pre ochrannú dráhu
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.OCHRANA_M.value])

                        elif self.cesta == 'Vlak': #self.vlak: #pre vlakovú cestu
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.VLAK_M.value])

                        elif self.cesta == 'Posun': #self.posun:    #pre posunovú cestu
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.POSUN_M.value])

                    else:   #základný obraz výhybky
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ODB.value])

            else:  #ak je úsek výhybky obsadený             
                if self.smer:   #ak je výhybka prestavená  v priamom smere
                    if self.zaver:  #ak je pod záverom
                        if self.vyber:
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZAVER_P_OBS_V.value])
                        
                        else:
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZAVER_P_OBS.value])

                    elif self.vyber:    #ak je vybraná obsluhou
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PRIAMA_OBS_VYBER.value])

                    else:   #základný obraz výhybky
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PRIAMA_OBS.value])

                else:   #ak je výhybka prestavená  v odbočnom smere
                    if self.zaver:  #ak je pod záverom
                        if self.vyber:
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZAVER_M_OBS_V.value])

                        else:
                            getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZAVER_M_OBS.value])

                    elif self.vyber:     #ak je vybraná obsluhou
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ODB_OBS_VYBER.value])

                    else:   #základný obraz výhybky
                        getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ODB_OBS.value])

    def prestavenieEnd(self):   #metóda pre zobrazenie symbolu počas prestavovania výhybky
        if self.lastSmer != self.smer:  #ak je výmena v opačnej koncovej polohe
            self.prest = False  #ukonči prestavovanie

    def rusenieCesty(self): #metóda pre rušenie cesty jazdou vlaku
        if (self.cesta == 'Vlak' or self.cesta == 'Posun') and not self.jeVolny:  #ak je úsek výhybky súčasťou jazdnej cesty a je obsadený
            self.cesta = ' '
            # self.vlak = False   #zruš jazdnú cestu
            # self.posun = False
            self.prejazd = True

        if self.jeVolny and self.prejazd:
            self.zaver = False
            self.prejazd = False

            if self.spojka:
                for i in self.app.vlaknoUpdate.dictUseky.keys(): #vyberaj z úsekov
                    spojka = getattr(self.app.vlaknoUpdate.dictUseky[i], 'spojka', None)   #načítaj hodnotu atribútu 'spojka'
                    
                    if spojka is not  None: #ak hodnota existuje
                        if (self.ID != self.app.vlaknoUpdate.dictUseky[i].ID) and spojka and (self.ID != self.app.vlaknoUpdate.dictUseky[i].jeVolny):  #ak hodnota neukazuje na vlastný objekt
                            self.app.vlaknoUpdate.dictUseky[i].zaver = False   #zruš záver sploupracujúcej výhybky
                            self.app.vlaknoUpdate.dictUseky[i].update(self)         
            
        if self.jeVolny and self.cesta != 'Vlak' and self.cesta != 'Posun' and not self.prejazd:   #ak je výhybka voľná a bez jazdnej cesty
            if self.spojka: #ak je výhybka súčasťou koľajovej spojky
                for i in self.app.vlaknoUpdate.dictUseky.keys(): #vyberaj z úsekov
                    spojka = getattr(self.app.vlaknoUpdate.dictUseky[i], 'spojka', None)   #načítaj hodnotu atribútu 'spojka'
                    
                    if spojka is not  None: #ak hodnota existuje
                        if (self.ID != self.app.vlaknoUpdate.dictUseky[i].ID) and spojka:  #ak hodnota neukazuje na vlastný objekt
                            if (self.app.vlaknoUpdate.dictUseky[i].zaver) and not self.zaver:   #ak je záver druhej výhybky v koľajovej spojke aktívny
                                self.app.vlaknoUpdate.dictUseky[i].zaver = True   #aktivuj záver sploupracujúcej výhybky
                                self.app.vlaknoUpdate.dictUseky[i].update(self)         