import zaverTab

class SZZ:
    def __init__(self, app:object):
        self.app = app  #väzba na hlavný súbor app.py
        self.typCesty:str = ' ' #indikuje typ vybranej cesty
        self.rusenaCesta:str = ' ' #tu sa zapisuje názov aktuálne rušenej jazdnej cesty
        self.stavanaCesta:str = ' '    #tu sa zapisuje názov aktuálne stavanej jazdnej cesty
        self.ochrDraha:bool = False #informácia o prítomnosti ochrannej dráhy
        self.vyberCesty:bool = False
        self.obsad1TU:bool = False   #informácia o obsadenom prvom TÚ pri odchodovej ceste
        self.spravnaPolohaVymen:bool = False
        self.server:bool = False #vyvolanie algoritmov cez REST

    def stavanieCesty(self, OD:bool=False, Disp:bool=False, server:bool=False):    #metóda na kontrolu podmienok stavania vlakových ciest  
        self.server = server
        self.ochrDraha = OD

        if self.app.pociatocneNav != 0 and self.app.koncoveNav != 0:    #ak sú vybrané pociatočné a koncové návestidlá
            if self.hladanieCestyVZavTab(Disp=Disp) == 0: #nájdi cestu v záverovej tabuľke a over možnosť jej postavenia                  
                for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov 
                    
                    for usek in zaverTab.dictVC[self.stavanaCesta]['Useky']:   #vyberaj z úsekov danej cesty 
                        if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa názvy zhodujú, vyhraď úsek pre jazdnú cestu                                
                    
                            self.predbeznyZaverCesty(i, self.typCesty)                            

                    if self.ochrDraha:  #ak existuje ochranná dráha
                        for usek in zaverTab.dictVC[self.stavanaCesta]['UsekyOD']:   #vyberaj z úsekov danej cesty 
                            if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa názvy zhodujú, vyhraď úsek pre ochrannú dráhu  
                                self.predbeznyZaverCesty(i, 'OchrDr')                                                      

                    if self.typCesty == 'Posun':   #v prípade posunu na obsadenú koľaj sa vytvorí záver aj tejto koľaje
                        for usek in zaverTab.dictVC[self.stavanaCesta]['dopUseky']: #vyber úsek zo záverovej tabuľky
                            if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa názvy zhodujú, vytvor záver jazdnej cesty
                                self.predbeznyZaverCesty(i, self.typCesty)

                self.app.zoznamNav[self.app.pociatocneNav].stavanieOd = False #zhasni symbol stavania cesty na počiatočnom návestidle
                self.app.zoznamNav[self.app.pociatocneNav].update(self)
                
                self.app.zoznamNav[self.app.koncoveNav].stavanieDo = True    #zobraz žltý index stavania cesty pri koncovom návestidle
                self.app.zoznamNav[self.app.koncoveNav].update(self)
                
                if Disp and self.app.zoznamNav[self.app.koncoveNav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].stavanieDo = True
                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].update(self)

                #------------KONTROLA SMERU VÝMEN------------
                self.spravnaPolohaVymen = True
                for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov
                    for vyhybka in zaverTab.dictVC[self.stavanaCesta].keys():  #vyberaj z výhybiek jazdnej cesty v záverovej tabuľke                        
                        if vyhybka == self.app.vlaknoUpdate.dictUseky[i].nazovGUI:    #ak sa názvy zhodujú                            
                            if self.app.vlaknoUpdate.dictUseky[i].smer == zaverTab.dictVC[self.stavanaCesta][vyhybka][0]: #skontroluj smer výhybky
                                break                             

                            else:   #ak nie je správne prestavená vydaj povel na prestavenie
                                self.spravnaPolohaVymen = False
                                self.app.vlaknoUpdate.dictUseky[i].prest = True
                                self.app.vlaknoUpdate.dictUseky[i].update(self)
                                
                                if Disp:    #úprava pre dispečerskú aplikáciu
                                    self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].prest = True
                                    self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].update(self)
                                    
                                if not self.server:  #povel pre prestavenie fyzickej výmeny 
                                    self.prestavenieVyh(vyhybka=i, i=1, auto=True)

                if self.spravnaPolohaVymen:
                    self.dokoncenieStavaniaCesty(Disp=Disp)

            else:
                self.app.vypisHlasenia('Nesprávny výber jazdnej cesty')
                return -1

        else:
            self.app.vypisHlasenia('Počiatočné alebo koncové návestidlo nie je definované')
            return -1
        
    def hladanieCestyVZavTab(self, Disp:bool):    #metóda na prehľadanie záverovej tabuľky
        for id in zaverTab.dictVC.keys():   #hľadaj v záverovej tabuľke
            if (self.app.zoznamNav[self.app.pociatocneNav].nazov in zaverTab.dictVC[id]['start']) and (
            self.app.zoznamNav[self.app.koncoveNav].nazov in zaverTab.dictVC[id]['stop']): #ak sa našla správna kombinácia počiatočného a koncového návestidla
                if self.ochrDraha and 'UsekyOD' in zaverTab.dictVC[id].keys():
                    self.stavanaCesta = id #vyber cestu na stavanie
                    self.app.zoznamNav[self.app.koncoveNav].OD = True
                    
                    if Disp: #úprava pre dispečerskú aplikáciu
                        self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].OD = True

                elif not self.ochrDraha:
                    self.stavanaCesta = id #vyber cestu na stavanie

                #------------KONTROLA VYLÚČENÝCH CIEST A OBSADENOSTI ÚSEKOV STAVANEJ CESTY------------
                if self.stavanaCesta != ' ':   #cesta bola vybraná

                    if self.kontrolaJazdnejCesty(rozsah='Useky') == -1:
                        return -1    #stavanie cesty je ukončené
                    
                    if self.ochrDraha and self.kontrolaJazdnejCesty(rozsah='UsekyOD') == -1:                                    
                        return -1    #stavanie cesty je ukončené 
                    
                    return 0
        return -1

    def kontrolaJazdnejCesty(self, rozsah:str):
        konfliktnaCesta = False
        volneUseky = True

        for i in self.app.vlaknoUpdate.dictUseky.keys():    #metóda na overenie podmienok postavenia jazdnej cesty
            for usek in zaverTab.dictVC[self.stavanaCesta][rozsah]:  #vyberaj zo úsekov stavanej cesty
                if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa našla zhoda
                    if (self.app.vlaknoUpdate.dictUseky[i].cesta != ' '):    #ak je niektorý z úsekov pod záverom
                        #self.dictStavanieCesty['nekonfliktnaCesta'] = False
                        konfliktnaCesta = True
                        if not self.server:
                            self.app.vypisHlasenia('Konfliktná jazdná cesta')

                    if self.app.vlaknoUpdate.dictUseky[i].jeVolny is False: #ak je niektorý z úsekov cesty obsadený 
                        #self.dictStavanieCesty['volnostUsekov'] = False
                        volneUseky = False
                        if not self.server:
                            if rozsah == 'Useky':
                                self.app.vypisHlasenia('Obsadené úseky v stavanej ceste')

                            elif rozsah == 'UsekyOD':
                                self.app.vypisHlasenia('Obsadené úseky v ochrannej dráhe stavanej cesty')

                    if konfliktnaCesta or not volneUseky: #ukonči stavanie
                        self.ochrDraha = False
                        self.stavanaCesta = ' '

                        self.app.zoznamNav[self.app.pociatocneNav].stavanieOd = False #zruš návestidlu príznak 'počiatočné'
                        self.app.zoznamNav[self.app.pociatocneNav].update(self)

                        return -1
        return 0

    def predbeznyZaverCesty(self, i:int, typ:str):
        self.app.vlaknoUpdate.dictUseky[i].stavanie = typ
        self.app.vlaknoUpdate.dictUseky[i].update(self)

        for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel 
            if (self.app.vlaknoUpdate.dictUseky[i].nazovGUI == self.app.zoznamNav[nav].usekPred) and (
            self.app.zoznamNav[nav].ID != self.app.koncoveNav) and (self.app.zoznamNav[nav].zavisle != self.app.zoznamNav[self.app.koncoveNav].ID):   
            #ak je návestidlo vo vnútri cesty a nie je definované ako koncové ani ako závislé návestidlo ku koncovému (Dispečer)
                self.app.zoznamNav[nav].cesta = typ  #zmeň jeho symbol 
                self.app.zoznamNav[nav].update(self)    

    def dokoncenieStavaniaCesty(self, Disp:bool):
        #------------ZÁVER JAZDNEJ CESTY------------
        if self.stavanaCesta != ' ':   #ak sa aktuálne stavia nejaká jazdná cesta            
            #------------ZÁVER BEZVÝHYBKOVÝCH ÚSEKOV------------               
            for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov
                self.zaverUsekov(i=i, zoznam='Useky', typZaveru=self.typCesty, Disp=Disp)  #vytvor záver jazdnej cesty                     

                if self.ochrDraha: #ak má cesta definovanú ochrannú dráhu
                    self.zaverUsekov(i=i, zoznam='UsekyOD', typZaveru='OchrDr', Disp=Disp) #vytvor záver úsekov ochrannej dráhy   

                if self.typCesty == 'Posun':   #v prípade posunu na obsadenú koľaj sa vytvorí záver cieľovej koľaje
                    self.zaverUsekov(i=i, zoznam='dopUseky', typZaveru=self.typCesty, Disp=Disp)
            
            #------------ZÁVER VÝHYBKOVÝCH ÚSEKOV------------ 
            for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov
                if self.stavanaCesta in zaverTab.dictVC.keys():    #vyberaj pre aktuálne stavanú jazdnú cestu                      
                    for vyhybka in zaverTab.dictVC[self.stavanaCesta].keys():  #vyberaj z výhybiek jazdnej cesty v záverovej tabuľke                   
                        if vyhybka == self.app.vlaknoUpdate.dictUseky[i].nazovGUI:     #ak sa názvy výhybiek zhodujú 
                            self.app.vlaknoUpdate.dictUseky[i].zaver = True    #záver výhybky
                            self.app.vlaknoUpdate.dictUseky[i].update(self)

                            if self.app.vlaknoUpdate.dictUseky[i].druhaVymena != -1:   #úprava pre spojku
                                self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].druhaVymena].zaver = True    #záver výhybky
                                self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].druhaVymena].update(self)

                            if self.app.vlaknoUpdate.dictUseky[i].zavisla != -1:   #úprava pre dipsečerskú aplikáciu
                                self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].zaver = True
                                self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].update(self)

            #------------ROZSVIETENIE POVOĽUJÚCEJ NÁVESTI POČIATOČNÉHO NÁVESTIDLA------------ 
            for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov 
                usek = zaverTab.dictVC[self.stavanaCesta].get('1TU', None)   #vyber úsek zo záverovej tabuľky                    
                if usek is None:    #rozsvietenie návesti pre posunovú cestu 

                    self.rozsvietPovolujucuNavest(Disp=Disp, usek=usek, i=i, navest='Posun')
                    break
                
                elif (self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek) or (usek == '0') and self.typCesty == 'Vlak': #rozsvietenie návesti pre vlakovú cestu
                    self.rozsvietPovolujucuNavest(Disp=Disp, usek=usek, i=i, navest='Vlak')
                    break

            if self.ochrDraha:  #zápis ochrannej dráhy do PLC
                if not self.server:
                    self.app.prikazDoPLC(adresat='ochranna_draha/', prikaz='true', nazov=self.stavanaCesta)
            
            self.app.zoznamNav[self.app.pociatocneNav].update(self)
            self.app.zoznamNav[self.app.koncoveNav].update(self)
            
            if Disp and (self.app.zoznamNav[self.app.pociatocneNav].zavisle != -1) and (self.app.zoznamNav[self.app.koncoveNav].zavisle != -1): #úprava pre dispečerskú aplikáciu
                self.app.zoznamNav[self.app.zoznamNav[self.app.pociatocneNav].zavisle].update(self)
                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].update(self)             

        if not self.server and self.typCesty == 'Vlak':  #zápis príznaku odchodovej cesty pre traťový súhlas a voľnosť trate
            self.app.prikazDoPLC(adresat='cesta', nazov='stavanie', prikaz=str(self.ochrDraha))

            if self.app.pociatocneNav in [4,5,47,48]:
                self.app.prikazDoPLC(adresat='odchod/', nazov='odchodR', prikaz='true')
            
            elif self.app.pociatocneNav in [20,62]:
                self.app.prikazDoPLC(adresat='odchod/', nazov='odchodZR', prikaz='true')

            elif self.app.pociatocneNav in [21,63]:
                if self.app.koncoveNav in [14,60]:
                    self.app.prikazDoPLC(adresat='odchod/', nazov='odchodZR', prikaz='true')

                elif self.app.koncoveNav in [15,61]:
                    self.app.prikazDoPLC(adresat='odchod/', nazov='odchodZL', prikaz='true')

            elif self.app.pociatocneNav in [22,23,64,65]:
                self.app.prikazDoPLC(adresat='odchod/', nazov='odchodZH', prikaz='true')
                self.app.prikazDoPLC(adresat='predhl/', prikaz='true', nazov='ZBE')  #v prípade AH odoslanie predhlášky na hradlo
                for nav in [30,44,69]:
                    if nav in self.app.zoznamNav.keys():
                        self.app.prikazDoPLC(adresat='navestidlo', prikaz='Volno', nazov=self.app.zoznamNav[nav].nazov)
                        break 

            elif self.app.pociatocneNav in [38,39,72,73]:
                self.app.prikazDoPLC(adresat='odchod/', nazov='odchodH', prikaz='true')
                self.app.prikazDoPLC(adresat='predhl/', prikaz='true', nazov='HLO')
                for nav in [31,45,70]:
                    if nav in self.app.zoznamNav.keys():
                        self.app.prikazDoPLC(adresat='navestidlo', prikaz='Volno', id=self.app.zoznamNav[nav].ID, nazov=self.app.zoznamNav[nav].nazov)
                        break 

        self.app.pociatocneNav = 0
        self.app.koncoveNav = 0
        self.stavanaCesta = ' '    
        self.ochrDraha = False
        self.spravnaPolohaVymen = False #reset premennej
        self.server = False
        self.stavCesty = False  #ukonči stavanie

    def zaverUsekov(self, i:int, zoznam:str, typZaveru:str, Disp:bool=False):
        for usek in zaverTab.dictVC[self.stavanaCesta][zoznam]:   #vyberaj z úsekov danej cesty                         
            if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek: #ak sa názvy zhodujú, definuj úsek ako záverovaný
                
                self.app.vlaknoUpdate.dictUseky[i].stavanie = ' '                                    
                self.app.vlaknoUpdate.dictUseky[i].cesta = typZaveru                                                                                                        
                self.app.vlaknoUpdate.dictUseky[i].update(self)

                if zoznam == 'Useky':
                    self.app.zoznamNav[self.app.koncoveNav].stavanieDo = False #úprava parametrov koncového mávestidla                      
                    self.app.zoznamNav[self.app.koncoveNav].koncove = True 
                    self.app.zoznamNav[self.app.koncoveNav].update(self)
                    
                    if Disp and self.app.zoznamNav[self.app.koncoveNav].zavisle != -1: #úprava pre dispečerskú aplikáciu                         
                        self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].stavanieDo = False
                        self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].koncove = True
                        self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].update(self)

    def rozsvietPovolujucuNavest(self, Disp:bool, usek:str, i:int, navest:str):
        self.app.zoznamNav[self.app.koncoveNav].zaver = navest
        self.app.zoznamNav[self.app.pociatocneNav].pociatocne = True
        
        if Disp:
            if self.app.zoznamNav[self.app.koncoveNav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                if navest == 'Posun':
                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].cesta = navest
                
                else:
                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].zaver = navest

            if self.app.zoznamNav[self.app.pociatocneNav].zavisle != -1:
                self.app.zoznamNav[self.app.zoznamNav[self.app.pociatocneNav].zavisle].pociatocne = True

        if (self.app.vlaknoUpdate.dictUseky[i].jeVolny) or (usek == '0'): #ak je 1. úsek za odchdovou cestou voľný
            self.app.zoznamNav[self.app.pociatocneNav].znak = navest #rozsvietenie povoľujúcej návesti na návestidle 
            
            if Disp and (self.app.zoznamNav[self.app.pociatocneNav].zavisle != -1): #úprava pre dispečerskú aplikáciu
                self.app.zoznamNav[self.app.zoznamNav[self.app.pociatocneNav].zavisle].znak = navest                              
            
            if not self.server:
                self.app.prikazDoPLC(adresat='navestidlo', prikaz=navest, nazov=self.app.zoznamNav[self.app.pociatocneNav].nazov)

    def aktualizaciaNavesti(self, navest:str, Disp:bool, nav:int, i:int, usek:str):                                      
            if (self.app.vlaknoUpdate.dictUseky[i].jeVolny) or (usek == '0'):    #ak je úsek voľný
                if self.app.zoznamNav[nav].znak == navest:
                    return
                else:
                    self.app.zoznamNav[nav].znak = navest #rozsvietenie povoľujúcej návesti na návestidle 
                    if Disp: #úprava pre dispečerskú aplikáciu
                        self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].znak = navest
                    
                    self.app.prikazDoPLC(adresat='navestidlo', prikaz=navest, nazov=self.app.zoznamNav[nav].nazov)                                

            else:   #ak je úsek obsadený
                if self.app.zoznamNav[nav].znak == 'Stoj':
                    return
                else:
                    self.app.zoznamNav[nav].znak = 'Stoj' #rozsvietenie zakazujúcej návesti na návestidle
                    if Disp: #úprava pre dispečerskú aplikáciu
                        self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].znak = 'Stoj' 
                    self.app.prikazDoPLC(adresat='navestidlo', prikaz='Stoj', nazov=self.app.zoznamNav[nav].nazov)                                                                
    
    def update(self, Disp:bool=False):     
        #------------AKTUALIZÁCIA VÝMEN-----------------
        if self.stavanaCesta in zaverTab.dictVC.keys():    #vyberaj pre aktuálne stavanú jazdnú cestu 
            self.spravnaPolohaVymen = True

            for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov
                for vyhybka in zaverTab.dictVC[self.stavanaCesta].keys():  #vyberaj z výhybiek jazdnej cesty v záverovej tabuľke                   
                    if vyhybka == self.app.vlaknoUpdate.dictUseky[i].nazovGUI:     #ak sa názvy výhybiek zhodujú                         
                        if self.app.vlaknoUpdate.dictUseky[i].smer == zaverTab.dictVC[self.stavanaCesta][vyhybka][0]: #ak je prestavená správne 
                            self.app.vlaknoUpdate.dictUseky[i].prest = False   #ukonči prestavovanie
                            
                            if self.app.vlaknoUpdate.dictUseky[i].zavisla != -1:   #úprava pre dipsečerskú aplikáciu
                                self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].prest = False

                            if vyhybka in zaverTab.dictVC[self.stavanaCesta]['Useky']: #ak je výhybka súčasťou jazdnej cesty
                                self.app.vlaknoUpdate.dictUseky[i].cesta = self.typCesty

                            elif self.ochrDraha and vyhybka in zaverTab.dictVC[self.stavanaCesta]['UsekyOD']: #ak je výhybka súčasťou ochrannej dráhy
                                self.app.vlaknoUpdate.dictUseky[i].cesta = 'OchrDr'                                    

                            self.app.vlaknoUpdate.dictUseky[i].update(self)
                        
                        else:  #ak je aspoň jedna výmena v zlej polohe
                            self.spravnaPolohaVymen = False  #pokračuj v prestavovaní  

            if self.spravnaPolohaVymen:
                self.dokoncenieStavaniaCesty(Disp=Disp)

        #------------AKTUALIZÁCIA ODCHODOVÉHO NÁVESTIDLA------------ 
        usek = None
        
        for c in zaverTab.dictVC.keys():    #vyberaj zo všetkých ciest                
            for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel                    
                if (self.app.zoznamNav[nav].nazov in zaverTab.dictVC[c]['start']) and (       #ak je počiatočné návestidlo niektorej jazdnej cesty,
                self.app.zoznamNav[nav].pociatocne) and (not self.app.zoznamNav[nav].manual):    #má príznak "pociatocne" a nie je v manuálnom režime                        
                    for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov    
                        usek = zaverTab.dictVC[c].get('1TU', None)  #vyber 1TÚ za stanicou zo záverovej tabuľky 
                        if usek is None:    #ak hľadaný úsek neexistuje ukonči beh metódy
                            return
                                                 
                        if usek is not None: #ak je úsek nájdený                                
                            if ((self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek) or (usek == '0')): #ak sa názvy úsekov zhodujú alebo nie je definovaný
                                self.aktualizaciaNavesti(navest=self.app.zoznamNav[nav].typAktCes, Disp=Disp, nav=nav, i=i, usek=usek)   #skontroluj závislosti pre automatickú zmenu návesti

                        # else:   #ak hľadaný úsek neexistuje ukonči beh metódy
                        #     return
                        
    def rusenieCesty(self, cas:bool=False, Disp:bool=False, server:bool=False):    #metóda pre rušenie jazdnej cesty
        self.server = server
        self.hladanieRusenejcestyVZaverTab(Disp=Disp)    #nájdi rušenú cestu v záverovej tabuľke

        #------------KONTROLA VOĽNOSTI PRIBLIŽOVACIEHO ÚSEKU A SPUSTENIE RUŠENIA CESTY------------
        if self.rusenaCesta != ' ':
            for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov                    
                if zaverTab.dictVC[self.rusenaCesta]['PU'] == self.app.vlaknoUpdate.dictUseky[i].nazovGUI:  #ak nájdeš približovací úsek
                    self.app.zoznamNav[self.app.koncoveNav].rusenie = True   #zobraz pri symbole koncového návestidla fialový index

                    if Disp and self.app.zoznamNav[self.app.koncoveNav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                            self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].rusenie = True 

                    if self.app.vlaknoUpdate.dictUseky[i].jeVolny: #ak je voľný
                        self.app.zoznamNav[self.app.koncoveNav].zaver = 'X'  #zruš príznak záveru na koncovom návestidle
                        
                        if Disp and self.app.zoznamNav[self.app.koncoveNav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                            self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].zaver = 'X'   
                        
                        self.uplynutieCasSuboru(Disp=Disp)

                        break

                    else:   #ak je obsadený
                        if self.app.zoznamNav[self.app.koncoveNav].zaver == 'Vlak':  #ak sa jedná o vlakovú cestu
                            self.app.zoznamNav[self.app.koncoveNav].zaver = 'X'  #zruš jej záver
                            
                            if Disp: #úprava pre dispečerskú aplikáciu
                                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].zaver = 'X'
                            
                            self.app.vlaknoDlhyCasVlak.start_timer()  #spusti časový súbor rušenia vlakovej cesty (3 min)
                            break

                        elif self.app.zoznamNav[self.app.koncoveNav].zaver == 'Posun':    #ak sa jedná o posunovú cestu
                            self.app.zoznamNav[self.app.koncoveNav].zaver = 'X'  #zruš jej záver
                            
                            if Disp: #úprava pre dispečerskú aplikáciu
                                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].zaver = 'X'
                            
                            self.app.vlaknoDlhyCasPosun.start_timer() #spusti časový súbor rušenia posunovej cesty (1 min)
                            break

    def uplynutieCasSuboru(self, Disp:bool): 
        if self.rusenaCesta != ' ':  
            for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov
                #------------RUŠENIE ZÁVERU ÚSEKOV JAZDNEJ CESTY------------ 
                self.rusenieZaveruUsekov(i=i, zoznam='Useky', Disp=Disp)               

                self.rusenieZaveruUsekov(i=i, zoznam='dopUseky', Disp=Disp)

                if self.ochrDraha:  #ak sa ruší aj ochranná dráha
                    self.rusenieOD(Disp=Disp)

            self.app.zoznamNav[self.app.koncoveNav].rusenie = False  #ukončenie rušenia jazdnej cesty
            self.app.zoznamNav[self.app.koncoveNav].update(self)
            
            if Disp and self.app.zoznamNav[self.app.koncoveNav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].rusenie = False  
                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].update(self)

            self.rusenaCesta = ' '
            if not self.server:
                self.app.prikazDoPLC(adresat='cesta', nazov='rusenie')
            
            self.app.koncoveNav = 0
            self.server = False
            self.ochrDraha = False

    def hladanieRusenejcestyVZaverTab(self, Disp:bool):
        for id in zaverTab.dictVC.keys():   #vyberaj zo záverovej tabuľky                
            if (self.app.zoznamNav[self.app.koncoveNav].nazov in zaverTab.dictVC[id]['stop']):   #ak nájdeš cestu s koncovým návestuidlom, ktoré obsluha vybrala                    
                for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel                        
                    if (self.app.zoznamNav[nav].nazov in zaverTab.dictVC[id]['start'])  and (
                    self.app.zoznamNav[nav].znak == 'Vlak' or self.app.zoznamNav[nav].znak == 'Posun' or (
                    self.app.zoznamNav[nav].znak == 'Stoj' and self.app.zoznamNav[nav].manual)):
                    #ak nájdeš návestidlo s povoľujúcim znakom alebo so Stoj v manuáln om režime zapísané ako počiatočné návestidlo vybranej jazdnej cesty
                        if (self.app.zoznamNav[self.app.koncoveNav].OD is True and 'UsekyOD' in zaverTab.dictVC[id].keys()) or (self.app.zoznamNav[self.app.koncoveNav].OD is False):
                        #ak je za koncovým návestidlom cesty aktívna ochranná dráha a je v jazdnej ceste definovaná ALEBO nie
                            for usek in self.app.vlaknoUpdate.dictUseky.keys():    #vyberaj z úsekov
                                for vyh in zaverTab.dictVC[id].keys():  #hľadaj výhybky jazdnej cesty v záverovej tabuľke 
                                    if self.app.vlaknoUpdate.dictUseky[usek].nazovGUI == vyh:  #ak ich nájdeš
                                        if  (zaverTab.dictVC[id][vyh][0]) == (self.app.vlaknoUpdate.dictUseky[usek].smer): #ak je polohy výmen správna pre danú cestu                                                                                           
                                            self.app.zoznamNav[nav].znak = 'Stoj' #zmeň návesť počiatočného návestidla na Stoj
                                            self.app.zoznamNav[nav].pociatocne = False
                                            self.app.zoznamNav[nav].manual = False
                                            self.app.zoznamNav[nav].update(self)
                                            
                                            if Disp and (self.app.zoznamNav[nav].zavisle != -1): #úprava pre dispečerskú aplikáciu
                                                self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].znak = 'Stoj' 
                                                self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].pociatocne = False
                                                self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].manual = False
                                                self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].update(self)

                                            self.rusenaCesta = id   #zapíš aktuálne vybranú cestu ako rušenú
                                            
                                            if self.app.zoznamNav[self.app.koncoveNav].OD:   #ak cesta obsahuje ochrannú dráhu
                                                self.ochrDraha = True
                                                self.app.zoznamNav[self.app.koncoveNav].OD = False
                                                
                                                if Disp: #úprava pre dispečerskú aplikáciu
                                                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].OD = False
                                                
                                                if not self.server:
                                                    self.app.prikazDoPLC(adresat='ochrannad_draha/', prikaz='false', nazov=self.rusenaCesta)

                                            if not self.server:
                                                self.app.prikazDoPLC(adresat='navestidlo', prikaz='Stoj', nazov=self.app.zoznamNav[nav].nazov)
                                                
                                            break
                                
                                if self.rusenaCesta != ' ': #po úspešnom vyhľadaní rušenej cesty sa opúšťa metóda
                                    return

    def rusenieZaveruUsekov(self, i:int, zoznam:str, Disp:bool):
        for usek in zaverTab.dictVC[self.rusenaCesta][zoznam]:  #vyberaj z úsekov 
            if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa názvy úsekov zhodujú
                self.app.vlaknoUpdate.dictUseky[i].cesta = ' '    #zruš záver daného úseku                       
                self.app.vlaknoUpdate.dictUseky[i].zaver = False

                if zoznam == 'Useky':
                    if hasattr(self.app.vlaknoUpdate.dictUseky[i], 'druhaVymena') and self.app.vlaknoUpdate.dictUseky[i].druhaVymena != -1: #úprava pre výhybkovú spojku
                        if self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].druhaVymena].cesta != ' ':
                            self.app.vlaknoUpdate.dictUseky[i].zaver = True
                        
                        else:
                            self.app.vlaknoUpdate.dictUseky[i].zaver = False
                            self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].druhaVymena].zaver = False

                self.app.vlaknoUpdate.dictUseky[i].update(self)

                for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel                            
                    if (self.app.vlaknoUpdate.dictUseky[i].nazovGUI == self.app.zoznamNav[nav].usekPred):
                        self.app.zoznamNav[nav].cesta = ' '  #uprav jeho symbol
                        self.app.zoznamNav[nav].update(self)
                        
                        if Disp and self.app.zoznamNav[nav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                            self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].cesta = ' '  #uprav jeho symbol
                            self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].update(self)
    
    def rusenieOD(self, Disp:bool=False):
        for id in zaverTab.dictVC.keys():   #vyberaj zo záverovej tabuľky             
            for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel    
                if (self.app.zoznamNav[nav].koncove is True) and (self.app.zoznamNav[nav].nazov in zaverTab.dictVC[id]['stop']) and (
                'UsekyOD' in zaverTab.dictVC[id].keys()):
                #ak je návestidlo definované ako koncové a je nájdené v jazdnej ceste s ochrannou dráhou                  

                    #------------RUŠENIE OCHRANNEJ DRÁHY JAZDNEJ CESTY------------
                    self.app.zoznamNav[nav].koncove = False
                    if Disp and self.app.zoznamNav[nav].zavisle != -1:
                        self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].koncove = False

                    for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov 
                        for usek in zaverTab.dictVC[id]['UsekyOD']:  #vyberaj z úsekov 
                            if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa názvy úsekov zhodujú
                                self.app.vlaknoUpdate.dictUseky[i].cesta = ' '    #zruš záver daného úseku
                                self.app.vlaknoUpdate.dictUseky[i].zaver = False
                                self.app.vlaknoUpdate.dictUseky[i].update(self)
                                
                                if hasattr(self.app.vlaknoUpdate.dictUseky[i], 'druhaVymena') and self.app.vlaknoUpdate.dictUseky[i].druhaVymena != -1:   #úprava pre spojku
                                    self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].druhaVymena].zaver = False    #záver výhybky
                                    self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].druhaVymena].update(self)

                                if hasattr(self.app.vlaknoUpdate.dictUseky[i], 'zavisla') and self.app.vlaknoUpdate.dictUseky[i].zavisla != -1:   #úprava pre dipsečerskú aplikáciu
                                    self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].zaver = False
                                    self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].update(self)

                                for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel                            
                                    if (self.app.vlaknoUpdate.dictUseky[i].nazovGUI == self.app.zoznamNav[nav].usekPred) and (self.app.zoznamNav[nav].ID != self.app.koncoveNav) and (
                                    self.app.zoznamNav[nav].zavisle != self.app.koncoveNav):  #ak sa návestidlo nachádza v úseku jazdnej cesty a nie je koncové návestidlo                                
                                        self.app.zoznamNav[nav].cesta = ' '  #uprav jeho symbol
                                        self.app.zoznamNav[nav].update(self)
                                        
                                        if Disp and self.app.zoznamNav[nav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                            self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].cesta = ' '
                                            self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].update(self)

                    self.app.prikazDoPLC(adresat='ochranna_draha/', prikaz='false', nazov=id)

    def prestavenieVyh(self, vyhybka:int, i:int, auto:bool=False):  #metóda pre ručné prestavovanie výmen
            self.app.ui.combo_vyh.hide()
            
            if self.app.vlaknoUpdate.dictUseky[vyhybka].jeVolny and self.app.vlaknoUpdate.dictUseky[vyhybka].cesta == ' ' and i == 1:          
                self.app.vlaknoUpdate.dictUseky[vyhybka].prest = True 
                self.app.vlaknoUpdate.dictUseky[vyhybka].vyber = False
                
                if auto: 
                    if self.app.vlaknoUpdate.dictUseky[vyhybka].druhaVymena != -1:   #úprava pre spojku
                        self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[vyhybka].druhaVymena].prest = True 
                        self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[vyhybka].druhaVymena].vyber = False

                        if self.app.vlaknoUpdate.dictUseky[vyhybka].zavisla != -1: #úprava pre dispečerskú aplikáciu
                            self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[vyhybka].druhaVymena].zavisla].prest = True 
                            self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[vyhybka].druhaVymena].zavisla].vyber = False

                if self.app.vlaknoUpdate.dictUseky[vyhybka].zavisla != -1: #úprava pre dispečerskú aplikáciu
                    self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[vyhybka].zavisla].prest = True 
                    self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[vyhybka].zavisla].vyber = False 

                if self.app.vlaknoUpdate.dictUseky[vyhybka].smer:
                    self.app.prikazDoPLC(adresat='vymena', prikaz='true', nazov=self.app.vlaknoUpdate.dictUseky[vyhybka].nazovGUI)
                
                else:
                    self.app.prikazDoPLC(adresat='vymena', prikaz='false', nazov=self.app.vlaknoUpdate.dictUseky[vyhybka].nazovGUI)

            self.app.ui.combo_vyh.setCurrentIndex(0)    #vynulovanie výberového menu pre ďalšie použitie