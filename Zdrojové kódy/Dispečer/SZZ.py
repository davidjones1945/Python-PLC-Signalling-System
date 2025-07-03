import zaverTab

class SZZ:
    def __init__(self, app):
        self.app = app  #väzba na hlavný súbor app.py
        self.typCesty = ' ' #indikuje typ vybranej cesty
        self.rusenaCesta = ' ' #tu sa zapisuje názov aktuálne rušenej jazdnej cesty
        self.stavanaCesta = ' '    #tu sa zapisuje názov aktuálne stavanej jazdnej cesty
        self.ochrDraha = False #informácia o prítomnosti ochrannej dráhy
        self.vyberCesty = False
        self.obsad1TU = False   #informácia o obsadenom prvom TÚ pri odchodovej ceste
        self.spravnaPolohaVymen = False
        self.dictStavanieCesty = {  #dáta o stavanej jazdnej ceste
            'polohaVymen': False
            #'volnostUsekov': False,
            #'nekonfliktnaCesta': False    
        }

    def kontrolaJazdnejCesty(self, rozsah:str, server:bool):
        konfliktnaCesta = False
        volneUseky = True

        for i in self.app.vlaknoUpdate.dictUseky.keys():    #metóda na overenie podmienok postavenia jazdnej cesty
            for usek in zaverTab.dictVC[self.stavanaCesta][rozsah]:  #vyberaj zo úsekov stavanej cesty
                if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa našla zhoda
                    if (self.app.vlaknoUpdate.dictUseky[i].cesta != ' '):    #ak je niektorý z úsekov pod záverom
                        #self.dictStavanieCesty['nekonfliktnaCesta'] = False
                        konfliktnaCesta = True
                        if not server:
                            self.app.vypisHlasenia('Konfliktná jazdná cesta')

                    if self.app.vlaknoUpdate.dictUseky[i].jeVolny is False: #ak je niektorý z úsekov cesty obsadený 
                        #self.dictStavanieCesty['volnostUsekov'] = False
                        volneUseky = False
                        if not server:
                            if rozsah == 'Useky':
                                self.app.vypisHlasenia('Obsadené úseky v stavanej ceste')

                            elif rozsah == 'UsekyOD':
                                self.app.vypisHlasenia('Obsadené úseky v ochrannej dráhe stavanej cesty')

                    if konfliktnaCesta or not volneUseky: #ukonči stavanie
                        self.ochrDraha = False
                        self.stavanaCesta = ' '

                        self.app.zoznamNav[self.app.pociatocneNav].stavanieOd = False #zruš návestidlu príznak 'počiatočné'
                        self.app.zoznamNav[self.app.pociatocneNav].update(self)

                        return 0
        return 1

    def hladanieCestyVZavTab(self, OD:bool, Disp:bool, server:bool):    #metóda na prehľadanie záverovej tabuľky
        for id in zaverTab.dictVC.keys():   #hľadaj v záverovej tabuľke
            if (self.app.zoznamNav[self.app.pociatocneNav].nazov in zaverTab.dictVC[id]['start']) and (
            self.app.zoznamNav[self.app.koncoveNav].nazov in zaverTab.dictVC[id]['stop']): #ak sa našla správna kombinácia počiatočného a koncového návestidla
                if OD and 'UsekyOD' in zaverTab.dictVC[id].keys():
                    self.stavanaCesta = id #vyber cestu na stavanie
                    self.ochrDraha = OD
                    self.app.zoznamNav[self.app.koncoveNav].OD = True
                    
                    if Disp: #úprava pre dispečerskú aplikáciu
                        self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].OD = True

                elif not OD:
                    self.stavanaCesta = id #vyber cestu na stavanie

                #------------KONTROLA VYLÚČENÝCH CIEST A OBSADENOSTI ÚSEKOV STAVANEJ CESTY------------
                if self.stavanaCesta != ' ':   #cesta bola vybraná
                    #self.dictStavanieCesty['nekonfliktnaCesta'] = True   #ukazovatele pripravovanej cesty
                    #self.dictStavanieCesty['volnostUsekov'] = True  

                    if self.kontrolaJazdnejCesty(rozsah='Useky', server=server) == 0:
                        return 0    #stavanie cesty je ukončené
                    
                    if self.ochrDraha and self.kontrolaJazdnejCesty(rozsah='UsekyOD', server=server) == 0:                                    
                        return 0    #stavanie cesty je ukončené 
                    
                    return 1
        return 2

    def predbeznyZaverCesty(self, index:int, typ:str):
        self.app.vlaknoUpdate.dictUseky[index].stavanie = typ
        self.app.vlaknoUpdate.dictUseky[index].update(self)

        for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel 
            if (self.app.vlaknoUpdate.dictUseky[index].nazovGUI == self.app.zoznamNav[nav].usekPred) and (
            self.app.zoznamNav[nav].ID != self.app.koncoveNav) and (self.app.zoznamNav[nav].zavisle != self.app.zoznamNav[self.app.koncoveNav].ID):   
            #ak je návestidlo vo vnútri cesty a nie je definované ako koncové ani ako závislé návestidlo ku koncovému (Dispečer)
                self.app.zoznamNav[nav].cesta = typ  #zmeň jeho symbol 
                self.app.zoznamNav[nav].update(self)   

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
                                self.rozsvietNavest(navest=self.app.zoznamNav[nav].typAktCes, Disp=Disp, nav=nav, index=i, usek=usek)   #skontroluj závislosti pre automatickú zmenu návesti

                        else:   #ak hľadaný úsek neexistuje ukonči beh metódy
                            return 

    def rozsvietNavest(self, navest:str, Disp:bool, nav:int, index:int, usek:str):                                      
            if (self.app.vlaknoUpdate.dictUseky[index].jeVolny) or (usek == '0'):    #ak je úsek voľný
                if self.app.zoznamNav[nav].znak == navest:
                    return
                else:
                    self.app.zoznamNav[nav].znak = navest #rozsvietenie povoľujúcej návesti na návestidle 
                    if Disp: #úprava pre dispečerskú aplikáciu
                        self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].znak = navest
                    
                    self.app.prikazDoPLC(prikaz='/' + navest, id=self.app.zoznamNav[nav].ID, nazov=self.app.zoznamNav[nav].nazov)                                

            else:   #ak je úsek obsadený
                if self.app.zoznamNav[nav].znak == 'Stoj':
                    return
                else:
                    self.app.zoznamNav[nav].znak = 'Stoj' #rozsvietenie zakazujúcej návesti na návestidle
                    if Disp: #úprava pre dispečerskú aplikáciu
                        self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].znak = 'Stoj' 
                    self.app.prikazDoPLC(prikaz='/Stoj', id=self.app.zoznamNav[nav].ID, nazov=self.app.zoznamNav[nav].nazov)                                                                
    
    def stavanieCesty(self, OD:bool=False, Disp:bool=False, server:bool=False):    #metóda na kontrolu podmienok stavania vlakových ciest  
        if self.app.pociatocneNav != 0 and self.app.koncoveNav != 0:    #ak sú vybrané pociatočné a koncové návestidlá
            if self.hladanieCestyVZavTab(OD=OD, Disp=Disp, server=server) == 1: #nájdi cestu v záverovej tabuľke a over možnosť jej postavenia                  
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
                for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov
                    for vyhybka in zaverTab.dictVC[self.stavanaCesta].keys():  #vyberaj z výhybiek jazdnej cesty v záverovej tabuľke                        
                        if vyhybka == self.app.vlaknoUpdate.dictUseky[i].nazovGUI:    #ak sa názvy zhodujú                            
                            if self.app.vlaknoUpdate.dictUseky[i].smer == zaverTab.dictVC[self.stavanaCesta][vyhybka][0]: #skontroluj smer výhybky
                                self.spravnaPolohaVymen = True #ak je prestavená správne vytvor záver

                            else:   #ak nie je správne prestavená vydaj povel na prestavenie
                                self.app.vlaknoUpdate.dictUseky[i].prest = True
                                self.app.vlaknoUpdate.dictUseky[i].update(self)
                                
                                if Disp:    #úprava pre dispečerskú aplikáciu
                                    self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].prest = True
                                    self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].update(self)
                                    self.spravnaPolohaVymen = False

                                if not server:  #povel pre prestavenie fyzickej výmeny 
                                    self.prestavenieVyh(i,1)

        else:
            self.app.vypisHlasenia('Počiatočné alebo koncové návestidlo nie je definované')
                            
        #------------ZÁVER JAZDNEJ CESTY------------
        if self.stavanaCesta != ' ':   #ak sa aktuálne stavia nejaká jazdná cesta 
            if self.spravnaPolohaVymen:           
                #------------ZÁVER ÚSEKOV------------               
                for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov                     
                    for usek in zaverTab.dictVC[self.stavanaCesta]['Useky']:   #vyberaj z úsekov danej cesty                         
                        if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek: #ak sa názvy zhodujú, definuj úsek ako záverovaný
                            
                            self.app.vlaknoUpdate.dictUseky[i].stavanie = ' '                                    
                            self.app.vlaknoUpdate.dictUseky[i].cesta = self.typCesty                                                                                                        
                            self.app.vlaknoUpdate.dictUseky[i].update(self)

                            self.app.zoznamNav[self.app.koncoveNav].stavanieDo = False #úprava parametrov koncového mávestidla                      
                            self.app.zoznamNav[self.app.koncoveNav].koncove = True 
                            self.app.zoznamNav[self.app.koncoveNav].update(self)
                            
                            if Disp and self.app.zoznamNav[self.app.koncoveNav].zavisle != -1: #úprava pre dispečerskú aplikáciu                         
                                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].stavanieDo = False
                                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].koncove = True
                                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].update(self)

                    if self.ochrDraha: #ak má cesta definovanú ochrannú dráhu
                        for usek in zaverTab.dictVC[self.stavanaCesta]['UsekyOD']:   #vyberaj z úsekov danej cesty                         
                            if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek: #ak sa názvy zhodujú, definuj úsek ako záverovaný
                                self.app.vlaknoUpdate.dictUseky[i].stavanie = ' '                                    
                                self.app.vlaknoUpdate.dictUseky[i].cesta = 'OchrDr'                                 
                                self.app.vlaknoUpdate.dictUseky[i].update(self)

                    if self.typCesty == 'Posun':   #v prípade posunu na obsadenú koľaj sa vytvorí záver aj danej koľaje
                        for usek in zaverTab.dictVC[self.stavanaCesta]['dopUseky']: #vyber úsek zo záverovej tabuľky
                            if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa názvy zhodujú, vytvor záver jazdnej cesty
                                self.app.vlaknoUpdate.dictUseky[i].stavanie = ' '
                                self.app.vlaknoUpdate.dictUseky[i].cesta = 'Posun'
                                self.app.vlaknoUpdate.dictUseky[i].update(self)
                
                #------------DEFINITÍVNE ZÁVEROVANIE VÝHYBIEK------------ 
                for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov
                    if self.stavanaCesta in zaverTab.dictVC.keys():    #vyberaj pre aktuálne stavanú jazdnú cestu                      
                        for vyhybka in zaverTab.dictVC[self.stavanaCesta].keys():  #vyberaj z výhybiek jazdnej cesty v záverovej tabuľke                   
                            if vyhybka == self.app.vlaknoUpdate.dictUseky[i].nazovGUI:     #ak sa názvy výhybiek zhodujú   
                                if i in [12,13]:   #úprava pre koľajovú spojku
                                    self.app.vlaknoUpdate.dictUseky[12].zaver = True    #záver koľajovej spojky
                                    self.app.vlaknoUpdate.dictUseky[13].zaver = True   
                                    self.app.vlaknoUpdate.dictUseky[12].update(self)
                                    self.app.vlaknoUpdate.dictUseky[13].update(self)
                                
                                elif i in [40,41]:   #úprava pre koľajovú spojku
                                    self.app.vlaknoUpdate.dictUseky[40].zaver = True    #záver koľajovej spojky
                                    self.app.vlaknoUpdate.dictUseky[41].zaver = True   
                                    self.app.vlaknoUpdate.dictUseky[40].update(self)
                                    self.app.vlaknoUpdate.dictUseky[41].update(self)
                               
                                else:                                    
                                    self.app.vlaknoUpdate.dictUseky[i].zaver = True    #záver výhybky
                                    self.app.vlaknoUpdate.dictUseky[i].update(self)

                                    if self.app.vlaknoUpdate.dictUseky[i].zavisla != -1:   #úprava pre dipsečerskú aplikáciu
                                        self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].zaver = True
                                        self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[i].zavisla].update(self)

                #------------ROZSVIETENIE POVOĽUJÚCEJ NÁVESTI POČIATOČNÉHO NÁVESTIDLA------------ 
                for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov 
                    usek = zaverTab.dictVC[self.stavanaCesta].get('1TU', None)   #vyber úsek zo záverovej tabuľky                    
                    if usek is None:    #rozsvietenie návesti pre posunovú cestu 
                        self.app.zoznamNav[self.app.koncoveNav].zaverPC = True
                        self.app.zoznamNav[self.app.pociatocneNav].pociatocne = True
                        
                        if Disp: #and (self.app.zoznamNav[self.app.pociatocneNav].zavisle != -1) and (self.app.zoznamNav[self.app.koncoveNav].zavisle != -1): #úprava pre dispečerskú aplikáciu
                            self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].zaverPC = True
                            self.app.zoznamNav[self.app.zoznamNav[self.app.pociatocneNav].zavisle].pociatocne = True

                        if (self.app.vlaknoUpdate.dictUseky[i].jeVolny) or (usek == '0'): #ak je 1. úsek za odchdovou cestou voľný
                            self.app.zoznamNav[self.app.pociatocneNav].znak = 'Posun' #rozsvietenie povoľujúcej návesti na návestidle 
                            
                            if Disp and (self.app.zoznamNav[self.app.pociatocneNav].zavisle != -1): #úprava pre dispečerskú aplikáciu
                                self.app.zoznamNav[self.app.zoznamNav[self.app.pociatocneNav].zavisle].znak = 'Posun'                              
                            
                            if not server:
                                self.app.prikazDoPLC(prikaz='/Posun', id=self.app.zoznamNav[self.app.pociatocneNav].ID, nazov=self.app.zoznamNav[self.app.pociatocneNav].nazov)
                            break
                    
                    else:   #rozsvietenie návesti pre vlakovú cestu
                        if (self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek) or (usek == '0') and self.typCesty == 'Vlak':    #ak sa názvy zhodujú
                            self.app.zoznamNav[self.app.koncoveNav].zaverVC = True
                            self.app.zoznamNav[self.app.pociatocneNav].pociatocne = True
                            
                            if Disp: #úprava pre dispečerskú aplikáciu
                                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].zaverVC = True                           
                                self.app.zoznamNav[self.app.zoznamNav[self.app.pociatocneNav].zavisle].pociatocne = True

                            if (self.app.vlaknoUpdate.dictUseky[i].jeVolny) or (usek == '0'):
                                self.app.zoznamNav[self.app.pociatocneNav].znak = 'Volno' 
                                
                                if Disp: #úprava pre dispečerskú aplikáciu
                                    self.app.zoznamNav[self.app.zoznamNav[self.app.pociatocneNav].zavisle].znak = 'Volno'
                                
                                if not server:
                                    self.app.prikazDoPLC(prikaz='/Volno', id=self.app.zoznamNav[self.app.pociatocneNav].ID, nazov=self.app.zoznamNav[self.app.pociatocneNav].nazov)
                                break

                if self.ochrDraha:  #zápis ochrannej dráhy do PLC
                    if not server:
                        self.app.prikazDoPLC(prikaz='/True', nazov=self.stavanaCesta, OD=True)
                
                self.app.zoznamNav[self.app.pociatocneNav].update(self)
                self.app.zoznamNav[self.app.koncoveNav].update(self)
                
                if Disp and (self.app.zoznamNav[self.app.pociatocneNav].zavisle != -1) and (self.app.zoznamNav[self.app.koncoveNav].zavisle != -1): #úprava pre dispečerskú aplikáciu
                    self.app.zoznamNav[self.app.zoznamNav[self.app.pociatocneNav].zavisle].update(self)
                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].update(self)             

                self.stavanaCesta = ' '    #ukončenie stavania jazdnej cesty
                self.ochrDraha = False
                self.spravnaPolohaVymen = False #reset premennej

            if not server and self.typCesty == 'Vlak':
                self.app.prikazDoPLC(cesta=True, nazov='stavanie', prikaz=str(OD))

                if self.app.pociatocneNav in [4,5,47,48]:
                    self.app.prikazDoPLC(odchod=True, nazov='odchodR', prikaz='/True')
                
                elif self.app.pociatocneNav in [20,62]:
                    self.app.prikazDoPLC(odchod=True, nazov='odchodZR', prikaz='/True')

                elif self.app.pociatocneNav in [21,63] and self.app.koncoveNav in [14,60]:
                    self.app.prikazDoPLC(odchod=True, nazov='odchodZR', prikaz='/True')

                elif self.app.pociatocneNav in [21,63] and self.app.koncoveNav in [15,61]:
                    self.app.prikazDoPLC(odchod=True, nazov='odchodZL', prikaz='/True')

                elif self.app.pociatocneNav in [22,23,64,65]:
                    self.app.prikazDoPLC(odchod=True, nazov='odchodZH', prikaz='/True')
                    self.app.prikazDoPLC(prikaz='/True', nazov='ZBE', predhl=True)
                    for nav in [30,44,69]:
                        if nav in self.app.zoznamNav.keys():
                            self.app.prikazDoPLC(prikaz='/Volno', id=self.app.zoznamNav[nav].ID, nazov=self.app.zoznamNav[nav].nazov)
                            break 

                elif self.app.pociatocneNav in [38,39,72,73]:
                    self.app.prikazDoPLC(odchod=True, nazov='odchodH', prikaz='/True')
                    self.app.prikazDoPLC(prikaz='/True', nazov='HLO', predhl=True)
                    for nav in [31,45,70]:
                        if nav in self.app.zoznamNav.keys():
                            self.app.prikazDoPLC(prikaz='/Volno', id=self.app.zoznamNav[nav].ID, nazov=self.app.zoznamNav[nav].nazov)
                            break 

                self.app.pociatocneNav = 0
                self.app.koncoveNav = 0
                self.stavCesty = False  #ukonči stavanie

    def rusenieCesty(self, cas = False, Disp = False, server=False):    #metóda pre rušenie jazdnej cesty
        if not cas: #ak nie je metóda volaná po uplynutí čaového súboru 

            #------------HĽADANIE RUŠENEJ CESTY V ZÁVEROVEJ TABUĽKE------------
            for id in zaverTab.dictVC.keys():   #vyberaj zo záverovej tabuľky                
                if (self.app.zoznamNav[self.app.koncoveNav].nazov in zaverTab.dictVC[id]['stop']):   #ak nájdeš cestu s koncovým návestuidlom, ktoré obsluha vybrala                    
                    for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel                        
                        if (self.app.zoznamNav[nav].nazov in zaverTab.dictVC[id]['start'])  and (
                        (self.app.zoznamNav[nav].znak == 'Volno') or (self.app.zoznamNav[nav].znak == 'Posun')):
                        #ak nájdeš návestidlo s povoľujúcim znakom zapísané ako počiatočné návestidlo vybranej jazdnej cesty
                            if ((self.app.zoznamNav[self.app.koncoveNav].OD is True) and ('UsekyOD' in zaverTab.dictVC[id].keys())) or (self.app.zoznamNav[self.app.koncoveNav].OD is False):
                            #ak je za koncovým návestidlom cesty aktívna ochranná dráha a je v jazdnej ceste definovaná ALEBO nie
                                for usek in self.app.vlaknoUpdate.dictUseky.keys():    #vyberaj z úsekov
                                    for vyh in zaverTab.dictVC[id].keys():  #hľadaj výhybky jazdnej cesty v záverovej tabuľke 
                                        if self.app.vlaknoUpdate.dictUseky[usek].nazovGUI == vyh:  #ak ich nájdeš
                                            if  (zaverTab.dictVC[id][vyh][0]) == (self.app.vlaknoUpdate.dictUseky[usek].smer): #ak je polohy výmen správna pre danú cestu                                                                                           
                                                self.app.zoznamNav[nav].znak = 'Stoj' #zmeň znak na zakazujúci
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
                                                    
                                                    if not server:
                                                        self.app.prikazDoPLC(prikaz='/False', nazov=self.rusenaCesta, OD=True)

                                                if not server:
                                                    self.app.prikazDoPLC(prikaz='/Stoj', id=self.app.zoznamNav[nav].ID, nazov=self.app.zoznamNav[nav].nazov)
                                                break
                                    if self.rusenaCesta != ' ': #po úspešnom vyhľadaní rušenej cesty sa opúšťajú vyhľadávacie cykly
                                        break
                                if self.rusenaCesta != ' ':
                                    break   
                    if self.rusenaCesta != ' ':
                        break

            #------------KONTROLA VOĽNOSTI PRIBLIŽOVACIEHO ÚSEKU A SPUSTENIE RUŠENIA CESTY------------
            if self.rusenaCesta != ' ':
                for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov                    
                    if zaverTab.dictVC[self.rusenaCesta]['PU'] == self.app.vlaknoUpdate.dictUseky[i].nazovGUI:  #ak nájdeš približovací úsek
                        self.app.zoznamNav[self.app.koncoveNav].rusenie = True   #zobraz pri symbole koncového návestidla fialový index
                        if self.app.vlaknoUpdate.dictUseky[i].jeVolny: #ak je voľný
                            cas = True  #zruš cestu okamžite
                            self.app.zoznamNav[self.app.koncoveNav].zaverVC = False  #zruš jej záver
                            self.app.zoznamNav[self.app.koncoveNav].zaverPC = False 
                            
                            if Disp and self.app.zoznamNav[self.app.koncoveNav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].zaverVC = False  
                                self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].zaverPC = False  
                            
                            break

                        else:   #ak je obsadený
                            if self.app.zoznamNav[self.app.koncoveNav].zaverVC:  #ak sa jedná o vlakovú cestu
                                self.app.zoznamNav[self.app.koncoveNav].zaverVC = False  #zruš jej záver
                                
                                if Disp: #úprava pre dispečerskú aplikáciu
                                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].zaverVC = False
                                
                                self.app.workerThreadTimeVlak.pociatocneNav_timer()  #spusti časový súbor rušenia vlakovej cesty (3 min)
                                break

                            elif self.app.zoznamNav[self.app.koncoveNav].zaverPC:    #ak sa jedná o posunovú cestu
                                self.app.zoznamNav[self.app.koncoveNav].zaverPC = False  #zruš jej záver
                                
                                if Disp: #úprava pre dispečerskú aplikáciu
                                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].zaverPC = False
                                
                                self.app.workerThreadTimePosun.pociatocneNav_timer() #spusti časový súbor rušenia posunovej cesty (1 min)
                                break

                self.app.zoznamNav[self.app.koncoveNav].update(self) #aktualizuj symbol koncového návestidla
                if Disp and self.app.zoznamNav[self.app.koncoveNav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].update(self)

        #------------VYPRŠANIE ČASOVÝCH SÚBOROV RUŠENIA CESTY------------
        if cas: #ak je metóda volaná po uplynutí čaového súboru  
            if self.rusenaCesta != ' ':  
                for i in self.app.vlaknoUpdate.dictUseky.keys():   #vyberaj zo všetkých úsekov
                    #------------RUŠENIE ZÁVERU ÚSEKOV JAZDNEJ CESTY------------                
                    for usek in zaverTab.dictVC[self.rusenaCesta]['Useky']:  #vyberaj z úsekov 
                        if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa názvy úsekov zhodujú
                            self.app.vlaknoUpdate.dictUseky[i].vlak = False    #zruš záver daného úseku
                            self.app.vlaknoUpdate.dictUseky[i].posun = False                        
                            
                            if i in [12,13]:  #špeciálna úprava pre koľajovú spojku
                                if (i == 12 and ((
                                self.app.vlaknoUpdate.dictUseky[13].vlak is True) or (
                                self.app.vlaknoUpdate.dictUseky[13].posun is True) or (
                                self.app.vlaknoUpdate.dictUseky[13].ochr is True))) or (
                                i == 13 and ((
                                self.app.vlaknoUpdate.dictUseky[12].vlak is True) or (
                                self.app.vlaknoUpdate.dictUseky[12].posun is True) or (
                                self.app.vlaknoUpdate.dictUseky[12].ochr is True))
                                ):
                                    self.app.vlaknoUpdate.dictUseky[i].zaver = True
                                    
                                else:
                                    self.app.vlaknoUpdate.dictUseky[12].zaver = False
                                    self.app.vlaknoUpdate.dictUseky[13].zaver = False
                            
                            elif i in [40,41]:  #špeciálna úprava pre koľajovú spojku
                                if (i == 40 and ((
                                self.app.vlaknoUpdate.dictUseky[41].vlak is True) or (
                                self.app.vlaknoUpdate.dictUseky[41].posun is True) or (
                                self.app.vlaknoUpdate.dictUseky[41].ochr is True))) or (
                                i == 41 and ((
                                self.app.vlaknoUpdate.dictUseky[40].vlak is True) or (
                                self.app.vlaknoUpdate.dictUseky[40].posun is True) or (
                                self.app.vlaknoUpdate.dictUseky[40].ochr is True))
                                ):
                                    self.app.vlaknoUpdate.dictUseky[i].zaver = True
                                    
                                else:
                                    self.app.vlaknoUpdate.dictUseky[40].zaver = False
                                    self.app.vlaknoUpdate.dictUseky[41].zaver = False

                            else:
                                self.app.vlaknoUpdate.dictUseky[i].zaver = False

                            self.app.vlaknoUpdate.dictUseky[i].update(self)

                            for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel                            
                                if (self.app.vlaknoUpdate.dictUseky[i].nazovGUI == self.app.zoznamNav[nav].usekPred): #and (self.app.zoznamNav[nav].ID != self.app.koncoveNav) and (
                                    self.app.zoznamNav[nav].vlak = False  #uprav jeho symbol
                                    self.app.zoznamNav[nav].posun = False
                                    self.app.zoznamNav[nav].update(self)
                                    
                                    if Disp and self.app.zoznamNav[nav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                        self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].vlak = False  #uprav jeho symbol
                                        self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].posun = False
                                        self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].update(self)

                    for usek in zaverTab.dictVC[self.rusenaCesta]['dopUseky']: #vyber úsek zo záverovej tabuľky
                        if usek is not None:
                            if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa názvy úsekov zhodujú
                                self.app.vlaknoUpdate.dictUseky[i].posun = False   #zruš záver úseku

                                for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel                                
                                    if (self.app.vlaknoUpdate.dictUseky[i].nazovGUI == self.app.zoznamNav[nav].usekPred): #and (self.app.zoznamNav[nav].ID != self.app.koncoveNav) and (
                                        self.app.zoznamNav[nav].posun = False #uprav jeho symbol
                                        self.app.zoznamNav[nav].update(self)
                                        
                                        if Disp and self.app.zoznamNav[nav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                            self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].posun = False 
                                            self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].update(self)

                    if self.ochrDraha:  #ak sa ruší aj ochranná dráha
                        for usek in zaverTab.dictVC[self.rusenaCesta]['UsekyOD']:  #vyberaj z úsekov 
                            if self.app.vlaknoUpdate.dictUseky[i].nazovGUI == usek:    #ak sa názvy úsekov zhodujú
                                self.app.vlaknoUpdate.dictUseky[i].ochr = False    #zruš záver daného úseku
                                if i in [12,13]:  #špeciálna úprava pre koľajovú spojku
                                    
                                    if i == 12 and ((self.app.vlaknoUpdate.dictUseky[13].vlak is True) or (self.app.vlaknoUpdate.dictUseky[13].posun is True) or (
                                    self.app.vlaknoUpdate.dictUseky[13].ochr is True)):
                                        self.app.vlaknoUpdate.dictUseky[12].zaver = False
                                    
                                    elif i == 13 and ((self.app.vlaknoUpdate.dictUseky[12].vlak is True) or (self.app.vlaknoUpdate.dictUseky[12].posun is True) or (
                                    self.app.vlaknoUpdate.dictUseky[12].ochr is True)):
                                        self.app.vlaknoUpdate.dictUseky[13].zaver = False
                                    
                                    else:
                                        self.app.vlaknoUpdate.dictUseky[12].zaver = False
                                        self.app.vlaknoUpdate.dictUseky[13].zaver = False

                                elif i in [40,41]:  #špeciálna úprava pre koľajovú spojku
                                    if i == 40 and ((self.app.vlaknoUpdate.dictUseky[41].vlak is True) or (self.app.vlaknoUpdate.dictUseky[41].posun is True) or (
                                    self.app.vlaknoUpdate.dictUseky[41].ochr is True)):
                                        self.app.vlaknoUpdate.dictUseky[40].zaver = False
                                    
                                    elif i == 41 and ((self.app.vlaknoUpdate.dictUseky[40].vlak is True) or (self.app.vlaknoUpdate.dictUseky[40].posun is True) or (
                                    self.app.vlaknoUpdate.dictUseky[40].ochr is True)):
                                        self.app.vlaknoUpdate.dictUseky[41].zaver = False
                                    
                                    else:
                                        self.app.vlaknoUpdate.dictUseky[40].zaver = False
                                        self.app.vlaknoUpdate.dictUseky[41].zaver = False

                                else:
                                    self.app.vlaknoUpdate.dictUseky[i].zaver = False

                                self.app.vlaknoUpdate.dictUseky[i].update(self)

                                for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel                            
                                    if (self.app.vlaknoUpdate.dictUseky[i].nazovGUI == self.app.zoznamNav[nav].usekPred): #and (self.app.zoznamNav[nav].ID != self.app.koncoveNav) and (
                                        self.app.zoznamNav[nav].ochr = False  #uprav jeho symbol
                                        self.app.zoznamNav[nav].update(self)
                                        
                                        if Disp and self.app.zoznamNav[nav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                            self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].ochr = False                                        
                                            self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].update(self)

                self.app.zoznamNav[self.app.koncoveNav].rusenie = False  #ukončenie rušenia jazdnej cesty
                self.app.zoznamNav[self.app.koncoveNav].update(self)
                
                if Disp and self.app.zoznamNav[self.app.koncoveNav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].rusenie = False  
                    self.app.zoznamNav[self.app.zoznamNav[self.app.koncoveNav].zavisle].update(self)

                self.rusenaCesta = ' '
                if not server:
                    self.app.prikazDoPLC(cesta=True, nazov='rusenie')
                
                self.app.koncoveNav = 0
                self.ochrDraha = False

    def rusenieOD(self, Disp = False):
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
                                self.app.vlaknoUpdate.dictUseky[i].ochr = False    #zruš záver daného úseku
                                
                                if i in [12,13]:  #špeciálna úprava pre koľajovú spojku
                                    self.app.vlaknoUpdate.dictUseky[12].zaver = False
                                    self.app.vlaknoUpdate.dictUseky[13].zaver = False

                                elif i in [40,41]:  #špeciálna úprava pre koľajovú spojku
                                    self.app.vlaknoUpdate.dictUseky[40].zaver = False
                                    self.app.vlaknoUpdate.dictUseky[41].zaver = False

                                else:
                                    self.app.vlaknoUpdate.dictUseky[i].zaver = False
                                self.app.vlaknoUpdate.dictUseky[i].update(self)

                                for nav in self.app.zoznamNav.keys(): #vyberaj z návestidiel                            
                                    if (self.app.vlaknoUpdate.dictUseky[i].nazovGUI == self.app.zoznamNav[nav].usekPred) and (self.app.zoznamNav[nav].ID != self.app.koncoveNav) and (
                                    self.app.zoznamNav[nav].zavisle != self.app.koncoveNav):  #ak sa návestidlo nachádza v úseku jazdnej cesty a nie je koncové návestidlo                                
                                        self.app.zoznamNav[nav].ochr = False  #uprav jeho symbol
                                        self.app.zoznamNav[nav].update(self)
                                        
                                        if Disp and self.app.zoznamNav[nav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                            self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].ochr = False
                                            self.app.zoznamNav[self.app.zoznamNav[nav].zavisle].update(self)

                    self.app.prikazDoPLC(prikaz='/False', nazov=id, OD=True)

    def prestavenieVyh(self, vyhybka, index):  #metóda pre ručné prestavovanie výmen
            self.app.ui.combo_vyh.hide()
            
            if vyhybka in [12,13]:
                spojkaOK = False
                for id in [12,13]:
                    if (self.app.vlaknoUpdate.dictUseky[id].jeVolny) and ((self.app.vlaknoUpdate.dictUseky[id].vlak is False) and (
                    self.app.vlaknoUpdate.dictUseky[id].posun is False) and (self.app.vlaknoUpdate.dictUseky[id].ochr is False)):           
                        spojkaOK = True
                    
                    else:
                        break

                if spojkaOK:
                    if index == 1:  #ak bolo v menu vybraný príkaz na prestavenie začni prestavovať výmenu
                        self.app.vlaknoUpdate.dictUseky[12].prest = True 
                        self.app.vlaknoUpdate.dictUseky[13].prest = True
                        
                        if self.app.vlaknoUpdate.dictUseky[vyhybka].zavisla != -1: #úprava pre dispečerskú aplikáciu
                            self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[12].zavisla].prest = True 
                            self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[13].zavisla].prest = True
                        
                        self.app.clickObjekt(id=13, objekt='vyhybka')

                        if (self.app.vlaknoUpdate.dictUseky[12].smer) and (self.app.vlaknoUpdate.dictUseky[13].smer):
                            self.app.prikazDoPLC(prikaz='/True', nazov=self.app.vlaknoUpdate.dictUseky[vyhybka].nazovGUI, vyh=True)
                        
                        else:
                            self.app.prikazDoPLC(prikaz='/False', nazov=self.app.vlaknoUpdate.dictUseky[vyhybka].nazovGUI, vyh=True)

            elif vyhybka in [40,41]:
                spojkaOK = False
                for id in [40,41]:
                    if (self.app.vlaknoUpdate.dictUseky[id].jeVolny) and ((self.app.vlaknoUpdate.dictUseky[id].vlak is False) and (
                    self.app.vlaknoUpdate.dictUseky[id].posun is False) and (self.app.vlaknoUpdate.dictUseky[id].ochr is False)):           
                        spojkaOK = True
                    
                    else:
                        break

                if spojkaOK:
                    if index == 1:  #ak bolo v menu vybraný príkaz na prestavenie začni prestavovať výmenu
                        self.app.vlaknoUpdate.dictUseky[40].prest = True 
                        self.app.vlaknoUpdate.dictUseky[41].prest = True
                        
                        if self.app.vlaknoUpdate.dictUseky[vyhybka].zavisla != -1: #úprava pre dispečerskú aplikáciu
                            self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[40].zavisla].prest = True 
                            self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[41].zavisla].prest = True 
                        
                        self.app.clickObjekt(id=41, objekt='vyhybka')

                        if (self.app.vlaknoUpdate.dictUseky[40].smer) and (self.app.vlaknoUpdate.dictUseky[41].smer):
                            self.app.prikazDoPLC(prikaz='/True', nazov=self.app.vlaknoUpdate.dictUseky[vyhybka].nazovGUI, vyh=True)
                        
                        else:
                            self.app.prikazDoPLC(prikaz='/False', nazov=self.app.vlaknoUpdate.dictUseky[vyhybka].nazovGUI, vyh=True)

            else:
                if (self.app.vlaknoUpdate.dictUseky[vyhybka].jeVolny) and ((self.app.vlaknoUpdate.dictUseky[vyhybka].vlak is False) and (
                self.app.vlaknoUpdate.dictUseky[vyhybka].posun is False) and (self.app.vlaknoUpdate.dictUseky[vyhybka].ochr is False)):           
                    if index == 1:  #ak bolo v menu vybraný príkaz na prestavenie začni prestavovať výmenu
                        self.app.vlaknoUpdate.dictUseky[vyhybka].prest = True 
                        self.app.vlaknoUpdate.dictUseky[vyhybka].vyber = False
                        
                        if self.app.vlaknoUpdate.dictUseky[vyhybka].zavisla != -1: #úprava pre dispečerskú aplikáciu
                            self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[vyhybka].zavisla].prest = True 
                            self.app.vlaknoUpdate.dictUseky[self.app.vlaknoUpdate.dictUseky[vyhybka].zavisla].vyber = False 

                        if self.app.vlaknoUpdate.dictUseky[vyhybka].smer:
                            self.app.prikazDoPLC(prikaz='/True', nazov=self.app.vlaknoUpdate.dictUseky[vyhybka].nazovGUI, vyh=True)
                        
                        else:
                            self.app.prikazDoPLC(prikaz='/False', nazov=self.app.vlaknoUpdate.dictUseky[vyhybka].nazovGUI, vyh=True)

            self.app.ui.combo_vyh.setCurrentIndex(0)    #vynulovanie výberového menu pre ďalšie použitie