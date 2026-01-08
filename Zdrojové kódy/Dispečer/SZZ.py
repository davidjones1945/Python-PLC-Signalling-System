import zaverTab

class SZZ:
    def __init__(self, app):
        self.app = app  #väzba na hlavný súbor app.py
        self.typCesty = False #indikuje typ vybranej cesty (0 - vlaková, 1 - posunová)
        self.rusenaCesta = ' ' #tu sa zapisuje názov aktuálne rušenej jazdnej cesty
        self.cesta = ' '    #tu sa zapisuje názov aktuálne stavanej jazdnej cesty
        self.ochrDraha = False #informácia o prítomnosti ochrannej dráhy
        self.vyberCesty = False
        self.obsad1TU = False   #informácia o obsadenom prvom TÚ pri odchodovej ceste
        self.dictStavanieCesty = {
            'vymeny': False,
            'volnost': False,
            'stavanie': False
        }

    def stavanieCesty(self, update = False, OD = False, Disp = False, server=False):    #metóda na kontrolu podmienok stavania vlakových ciest  
        if (not update) and (self.app.Start != 0 and self.app.End != 0) and self.app.Start != self.app.End:  #ak nie je metóda volaná iba pre aktualizáciu stavu
            #------------PREHĽADÁVANIE ZÁVEROVEJ TABUĽKY------------
            for id in zaverTab.dictVC.keys():   #hľadaj v záverovej tabuľke
                if (self.app.dictNav[self.app.Start].nazov in zaverTab.dictVC[id]['start']) and (
                self.app.dictNav[self.app.End].nazov in zaverTab.dictVC[id]['stop']) and (
                self.app.dictNav[self.app.Start].znak != 'PN'): #ak sa našla správna kombinácia počiatočného a koncového návestidla a na počiatočnom nie je priv. náv.
                    if OD and 'UsekyOD' in zaverTab.dictVC[id].keys():
                        self.cesta = id #vyber cestu na stavanie
                        self.ochrDraha = OD
                        self.app.dictNav[self.app.End].OD = True
                        if Disp: #úprava pre dispečerskú aplikáciu
                            self.app.dictNav[self.app.dictNav[self.app.End].zavisle].OD = True

                    elif not OD:
                        self.cesta = id #vyber cestu na stavanie

                    if self.cesta != ' ':   #cesta bola vybraná
                        self.dictStavanieCesty['stavanie'] = True
                        self.dictStavanieCesty['volnost'] = True

                        #------------KONTROLA VYLÚČENÝCH CIEST------------
                        ochrDr = zaverTab.dictVC[self.cesta].get('UsekyOD', None)   #zisti či má cesta definovanú ochrannú dráhu

                        for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov
                            for usek in zaverTab.dictVC[self.cesta]['Useky']:  
                                if (self.app.workerThread.dictUseky[i].nazovGUI == usek) and (
                                (self.app.workerThread.dictUseky[i].vlak is True) or (self.app.workerThread.dictUseky[i].posun is True) or (
                                self.app.workerThread.dictUseky[i].ochr is True)):    #ak je niektorý z nich pod záverom pre inú cestu ukonči stavanie
                                    self.dictStavanieCesty['stavanie'] = False
                                    self.ochrDraha = False
                                    self.cesta = ' '

                                    self.app.dictNav[self.app.Start].stavanieOd = False #zruš návestidlu príznak 'počiatočné'
                                    self.app.dictNav[self.app.Start].update(self)

                                    if not server:
                                        self.app.vypisHlasenia('Konfliktná jazdná cesta')
                                    break

                            if not self.dictStavanieCesty['stavanie']:
                                break   #stavanie cesty je ukončené

                            if ochrDr is not None: #vybraná cesta obsahuje ochrannú dráhu
                                for usek in zaverTab.dictVC[self.cesta]['UsekyOD']:  
                                    if (self.app.workerThread.dictUseky[i].nazovGUI == usek) and (
                                    (self.app.workerThread.dictUseky[i].vlak is True) or (self.app.workerThread.dictUseky[i].posun is True) or (
                                    self.app.workerThread.dictUseky[i].ochr is True)):    #ak je niektorý z nich pod záverom pre inú cestu ukonči stavanie
                                        self.dictStavanieCesty['stavanie'] = False
                                        self.ochrDraha = False
                                        self.cesta = ' '

                                        self.app.dictNav[self.app.Start].stavanieOd = False #zruš návestidlu príznak 'počiatočné'
                                        self.app.dictNav[self.app.Start].update(self)

                                        if not server:
                                            self.app.vypisHlasenia('Konfliktná jazdná cesta')
                                        break

                                if not self.dictStavanieCesty['stavanie']:
                                    break   #stavanie cesty je ukončené
                        
                        if not self.dictStavanieCesty['stavanie']:
                            break   #stavanie cesty je ukončené

                        #------------KONTROLA OBSADENOSTI ÚSEKOV STAVANEJ CESTY------------                        
                        for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov                         
                                for usek in zaverTab.dictVC[self.cesta]['Useky']:   #vyberaj z úsekov danej cesty 
                                    if (self.app.workerThread.dictUseky[i].nazovGUI == usek) and (
                                    self.app.workerThread.dictUseky[i].jeVolny is False):  #ak je niektorý z nich obsadený ukonči stavanie
                                        self.dictStavanieCesty['volnost'] = False
                                        self.ochrDraha = False
                                        self.cesta = ' '

                                        self.app.dictNav[self.app.Start].stavanieOd = False #zruš návestidlu príznak 'počiatočné'
                                        self.app.dictNav[self.app.Start].update(self)

                                        if not server:
                                            self.app.vypisHlasenia('Úsek(y) jazdnej cesty sú obsadené')
                                        break
                                
                                if not self.dictStavanieCesty['volnost']:
                                    break   #stavanie cesty je ukončené
                                
                                if ochrDr is not None: #ak vybraná cesta obsahuje ochrannú dráhu
                                    for usek in zaverTab.dictVC[self.cesta]['UsekyOD']:   #vyberaj z úsekov ochrannej dráhy
                                        if (self.app.workerThread.dictUseky[i].nazovGUI == usek) and (
                                        self.app.workerThread.dictUseky[i].jeVolny is False):  #ak je niektorý z nich obsadený ukonči stavanie
                                            self.dictStavanieCesty['volnost'] = False
                                            self.ochrDraha = False
                                            self.cesta = ' '

                                            self.app.dictNav[self.app.Start].stavanieOd = False #zruš návestidlu príznak 'počiatočné'
                                            self.app.dictNav[self.app.Start].update(self)

                                            if not server:
                                                self.app.vypisHlasenia('Úsek(y) jazdnej cesty sú obsadené')
                                            break

                                if  self.dictStavanieCesty['volnost'] is False:
                                    break #stavanie cesty je ukončené                       
                        
                        if self.dictStavanieCesty['volnost']  is False:
                            break   #stavanie cesty je ukončené
                        
                        #------------KONTROLA OBSADENOSTI 1.TÚ PRI ODCHODOVEJ CESTE------------
                        if '1TU' in zaverTab.dictVC[self.cesta].keys(): #cesta obsahuje v definícii 1. traťový oddiel
                            usek = zaverTab.dictVC[self.cesta]['1TU']
                            if usek != '0':   #1. traťový oddiel je definovaný (ide o odchodovú cestu)
                                for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov
                                    if (self.app.workerThread.dictUseky[i].nazovGUI == usek) and (
                                    self.app.workerThread.dictUseky[i].jeVolny == False):    #ak bol úsek nájdený a je obsadený
                                        self.dictStavanieCesty['stavanie'] = False
                                        self.dictStavanieCesty['volnost'] = False
                                        self.obsad1TU = True
                                        break

                                if (self.dictStavanieCesty['stavanie'] is False) and (self.dictStavanieCesty['volnost'] is False):
                                    self.cesta = ' '
                                    break #prerušenie stavania cesty

                    if (self.dictStavanieCesty['stavanie'] is True) and (self.dictStavanieCesty['volnost'] is True):
                        break   #cesta je vyhodnotená ako vhodná pre postavenie

                
            if self.cesta == ' ' and not self.dictStavanieCesty['stavanie'] and  not self.dictStavanieCesty['volnost']:
                if not server:
                    if self.obsad1TU:
                        self.app.vypisHlasenia('1TÚ za stanicou je obsadený')
                        self.obsad1TU = False
                    else:
                        self.app.vypisHlasenia('Cesta nenájdená v databáze')
                self.app.ukonciStavanie()

            #------------ZAČIATOK STAVANIA JAZDNEJ CESTY------------
            if (self.dictStavanieCesty['stavanie'] is True) and (self.dictStavanieCesty['volnost'] is True):
                #------------PREDBEŽNÉ ZÁVEROVANIE ÚSEKOV------------
                for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov 
                    for usek in zaverTab.dictVC[self.cesta]['Useky']:   #vyberaj z úsekov danej cesty 
                        if self.app.workerThread.dictUseky[i].nazovGUI == usek:    #ak sa názvy zhodujú, vyhraď úsek pre jazdnú cestu                                
                            
                            if self.typCesty:   #posunová cesta
                                self.app.workerThread.dictUseky[i].stavaniePosun = True
                                self.app.workerThread.dictUseky[i].update(self)

                                for nav in self.app.dictNav.keys(): #vyberaj z návestidiel 
                                    if (self.app.workerThread.dictUseky[i].nazovGUI == self.app.dictNav[nav].usekPred) and (
                                    self.app.dictNav[nav].ID != self.app.End) and (self.app.dictNav[nav].zavisle != self.app.dictNav[self.app.End].ID):   
                                    #ak je návestidlo vo vnútri cesty a nie je definované ako koncové ani ako závislé návestidlo ku koncovému (Dispečer)
                                        self.app.dictNav[nav].posun = True  #zmeň jeho symbol 
                                        self.app.dictNav[nav].update(self)                                
                            
                            else:   #vlaková cesta
                                self.app.workerThread.dictUseky[i].stavanieVlak = True
                                self.app.workerThread.dictUseky[i].update(self)
                            
                                for nav in self.app.dictNav.keys():  #vyberaj z nvestidiel
                                    if (self.app.workerThread.dictUseky[i].nazovGUI == self.app.dictNav[nav].usekPred) and (
                                    self.app.dictNav[nav].ID != self.app.End) and (self.app.dictNav[nav].zavisle != self.app.dictNav[self.app.End].ID):  
                                    #ak je návestidlo vo vnútri cesty a nie je definované ako koncové ani ako závislé návestidlo ku koncovému (Dispečer)                                        
                                        self.app.dictNav[nav].vlak = True   #zmeň jeho symbol
                                        self.app.dictNav[nav].update(self)

                    if self.ochrDraha:  #ak existuje ochranná dráha
                        for usek in zaverTab.dictVC[self.cesta]['UsekyOD']:   #vyberaj z úsekov danej cesty 
                            if self.app.workerThread.dictUseky[i].nazovGUI == usek:    #ak sa názvy zhodujú, vyhraď úsek pre ochrannú dráhu                                                        
                                self.app.workerThread.dictUseky[i].stavanieOchr= True
                                self.app.workerThread.dictUseky[i].update(self)
                                
                                for nav in self.app.dictNav.keys():  #vyberaj z nvestidiel
                                    if (self.app.workerThread.dictUseky[i].nazovGUI == self.app.dictNav[nav].usekPred) and (
                                    self.app.dictNav[nav].ID != self.app.End) and (self.app.dictNav[nav].zavisle != self.app.dictNav[self.app.End].ID):  
                                    #ak je návestidlo vo vnútri cesty a nie je definované ako koncové ani ako závislé návestidlo ku koncovému (Dispečer)                                        
                                        self.app.dictNav[nav].ochr = True  #zmeň jeho symbol
                                        self.app.dictNav[nav].update(self)

                    if self.typCesty:   #v prípade posunu na obsadenú koľaj sa vytvorí záver aj tejto koľaje
                        for usek in zaverTab.dictVC[self.cesta]['dopUseky']: #vyber úsek zo záverovej tabuľky
                            if self.app.workerThread.dictUseky[i].nazovGUI == usek:    #ak sa názvy zhodujú, vytvor záver jazdnej cesty
                                self.app.workerThread.dictUseky[i].stavaniePosun = True
                                self.app.workerThread.dictUseky[i].update(self)

                                for nav in self.app.dictNav.keys(): #vyberaj z nvestidiel
                                    if (self.app.workerThread.dictUseky[i].nazovGUI == self.app.dictNav[nav].usekPred) and (
                                    self.app.dictNav[nav].ID != self.app.End):  #ak sa návestidlo nachádza v jazdnej ceste a nie je koncové návestidlo 
                                        self.app.dictNav[nav].posun = True  #zmeň jeho symbol
                                        self.app.dictNav[nav].update(self)

                self.app.dictNav[self.app.Start].stavanieOd = False #zhasni symbol stavania cesty na počiatočnom návestidle
                self.app.dictNav[self.app.Start].update(self)
                
                self.app.dictNav[self.app.End].stavanieDo = True    #zobraz žltý index stavania cesty pri koncovom návestidle
                self.app.dictNav[self.app.End].update(self)
                
                if Disp and self.app.dictNav[self.app.End].zavisle != -1: #úprava pre dispečerskú aplikáciu
                    self.app.dictNav[self.app.dictNav[self.app.End].zavisle].stavanieDo = True
                    self.app.dictNav[self.app.dictNav[self.app.End].zavisle].update(self)

                #------------KONTROLA SMERU VÝMEN------------
                for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov
                    for vyhybka in zaverTab.dictVC[self.cesta].keys():  #vyberaj z výhybiek jazdnej cesty v záverovej tabuľke                        
                        if vyhybka == self.app.workerThread.dictUseky[i].nazovGUI:    #ak sa názvy zhodujú                            
                            if self.app.workerThread.dictUseky[i].smer == zaverTab.dictVC[self.cesta][vyhybka][0]: #skontroluj smer výhybky
                                self.dictStavanieCesty['vymeny'] = True #ak je prestavená správne vytvor záver

                            else:   #ak nie je správne prestavená vydaj povel na prestavenie
                                self.app.workerThread.dictUseky[i].prest = True
                                self.app.workerThread.dictUseky[i].update(self)
                                
                                if Disp:    #úprava pre dispečerskú aplikáciu
                                    self.app.workerThread.dictUseky[self.app.workerThread.dictUseky[i].zavisla].prest = True
                                    self.app.workerThread.dictUseky[self.app.workerThread.dictUseky[i].zavisla].update(self)
                                    self.dictStavanieCesty['vymeny'] = False

                                if not server:
                                    self.prestavenieVyh(i,1)

        #--------UPDATE ZOBRAZENIA POČAS STAVANIA CESTY--------
        if update:  #ak je metóda volaná iba pre aktualizáciu stavu výhybiek a odchodového návestidla
            usek = None
            #------------AKTUALIZÁCIA VÝHYBIEK------------
            if self.cesta in zaverTab.dictVC.keys():    #vyberaj pre aktuálne stavanú jazdnú cestu 
                self.dictStavanieCesty['vymeny'] = True

                for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov
                    for vyhybka in zaverTab.dictVC[self.cesta].keys():  #vyberaj z výhybiek jazdnej cesty v záverovej tabuľke                   
                        if vyhybka == self.app.workerThread.dictUseky[i].nazovGUI:     #ak sa názvy výhybiek zhodujú                         
                            if self.app.workerThread.dictUseky[i].smer == zaverTab.dictVC[self.cesta][vyhybka][0]: #ak je prestavená správne 
                                self.app.workerThread.dictUseky[i].prest = False   #ukonči prestavovanie
                                self.app.workerThread.dictUseky[i].zaver = True    #vytvor záver výhybky
                                
                                if self.app.workerThread.dictUseky[i].zavisla != -1:   #úprava pre dipsečerskú aplikáciu
                                    self.app.workerThread.dictUseky[self.app.workerThread.dictUseky[i].zavisla].prest = False
                                    self.app.workerThread.dictUseky[self.app.workerThread.dictUseky[i].zavisla].zaver = True

                                if vyhybka in zaverTab.dictVC[self.cesta]['Useky']: #ak je výhybka súčasťou jazdnej dráhy
                                    if self.typCesty:   #pre posunovú cestu
                                        self.app.workerThread.dictUseky[i].posun = True
                                    else:   #pre vlakovú cestu
                                        self.app.workerThread.dictUseky[i].vlak = True

                                elif self.ochrDraha and (vyhybka in zaverTab.dictVC[self.cesta]['UsekyOD']): #ak je výhybka súčasťou ochrannej dráhy
                                    self.app.workerThread.dictUseky[i].ochr = True                                    

                                self.app.workerThread.dictUseky[i].update(self)
                            
                            else:  #ak je aspoň jedna výmena v zlej polohe
                                self.dictStavanieCesty['vymeny'] = False  #pokračuj v prestavovaní  

            #------------AKTUALIZÁCIA ODCHODOVÉHO NÁVESTIDLA------------ 
            for c in zaverTab.dictVC.keys():    #vyberaj zo všetkých ciest                
                for nav in self.app.dictNav.keys(): #vyberaj z návestidiel                    
                    if (self.app.dictNav[nav].nazov in zaverTab.dictVC[c]['start']) and (       #ak je počiatočné návestidlo niektorej jazdnej cesty,
                    self.app.dictNav[nav].pociatocne) and (not self.app.dictNav[nav].manual):    #má príznak "pociatocne" a nie je v manuálnom režime                        
                        for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov    
                            usek = zaverTab.dictVC[c].get('1TU', None)  #vyber 1TÚ za stanicou zo záverovej tabuľky                          
                            if usek is not None: #ak je úsek nájdený                                
                                if ((self.app.workerThread.dictUseky[i].nazovGUI == usek) or (usek == '0')): #ak sa názvy úsekov zhodujú alebo nie je definovaný
                                    
                                    if self.app.dictNav[nav].typAktCes:   #rozsvietenie návesti pre posunovú cestu                                         
                                        if (self.app.workerThread.dictUseky[i].jeVolny) or (usek == '0'):    #ak je úsek voľný
                                            if self.app.dictNav[nav].znak == 'Posun':
                                                break
                                            
                                            else:
                                                self.app.dictNav[nav].znak = 'Posun' #rozsvietenie povoľujúcej návesti na návestidle 
                                                if Disp: #úprava pre dispečerskú aplikáciu
                                                    self.app.dictNav[self.app.dictNav[nav].zavisle].znak = 'Posun'
                                                
                                                self.app.prikazDoPLC(prikaz='/Posun', id=self.app.dictNav[nav].ID, nazov=self.app.dictNav[nav].nazov)                                

                                        else:   #ak je úsek obsadený
                                            if self.app.dictNav[nav].znak == 'Stoj':
                                                break
                                            
                                            else:
                                                self.app.dictNav[nav].znak = 'Stoj' #rozsvietenie zakazujúcej návesti na návestidle
                                                if Disp: #úprava pre dispečerskú aplikáciu
                                                    self.app.dictNav[self.app.dictNav[nav].zavisle].znak = 'Stoj' 
                                                self.app.prikazDoPLC(prikaz='/Stoj', id=self.app.dictNav[nav].ID, nazov=self.app.dictNav[nav].nazov)                                

                                        break

                                    else:    #rozsvietenie návesti pre vlakovú cestu
                                        if (self.app.workerThread.dictUseky[i].jeVolny) or (usek == '0'):    #ak je úsek voľný
                                            if self.app.dictNav[nav].znak == 'Volno':
                                                break
                                            
                                            else:
                                                self.app.dictNav[nav].znak = 'Volno' 
                                                if Disp: #úprava pre dispečerskú aplikáciu
                                                    self.app.dictNav[self.app.dictNav[nav].zavisle].znak = 'Volno'
                                                self.app.prikazDoPLC(prikaz='/Volno', id=self.app.dictNav[nav].ID, nazov=self.app.dictNav[nav].nazov)

                                        else:   #ak je úsek obsadený
                                            if self.app.dictNav[nav].znak == 'Stoj':
                                                break
                                            
                                            else:
                                                self.app.dictNav[nav].znak = 'Stoj' #rozsvietenie zakazujúcej návesti na návestidle
                                                if Disp: #úprava pre dispečerskú aplikáciu
                                                    self.app.dictNav[self.app.dictNav[nav].zavisle].znak = 'Stoj'
                                                self.app.prikazDoPLC(prikaz='/Stoj', id=self.app.dictNav[nav].ID, nazov=self.app.dictNav[nav].nazov)                                 
                                        break
                            else:   #ak hľadaný úsek neexistuje
                                break
                    if usek is None: #ak hľadaný úsek neexistuje
                        break
                if usek is None: #ak hľadaný úsek neexistuje
                        break
                            
        #------------ZÁVER JAZDNEJ CESTY------------
        if self.cesta != ' ':   #ak sa aktuálne stavia nejaká jazdná cesta            
            if (self.dictStavanieCesty['stavanie'] is True) and (self.dictStavanieCesty['volnost'] is True) and (self.dictStavanieCesty['vymeny'] is True): #ak je postavená 
                #------------DEFINITÍVNE ZÁVEROVANIE ÚSEKOV------------               
                for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov                     
                    for usek in zaverTab.dictVC[self.cesta]['Useky']:   #vyberaj z úsekov danej cesty                         
                        if self.app.workerThread.dictUseky[i].nazovGUI == usek: #ak sa názvy zhodujú, definuj úsek ako záverovaný
                            
                            if self.typCesty:   #posunová cesta
                                self.app.workerThread.dictUseky[i].stavaniePosun = False                                    
                                self.app.workerThread.dictUseky[i].posun = True                                                                       

                            else:   #vlaková cesta
                                self.app.workerThread.dictUseky[i].stavanieVlak = False                                    
                                self.app.workerThread.dictUseky[i].vlak = True                                    

                            self.app.workerThread.dictUseky[i].update(self)

                            self.app.dictNav[self.app.End].stavanieDo = False #úprava parametrov koncového mávestidla                      
                            self.app.dictNav[self.app.End].koncove = True 
                            self.app.dictNav[self.app.End].update(self)
                            
                            if Disp and self.app.dictNav[self.app.End].zavisle != -1: #úprava pre dispečerskú aplikáciu                         
                                self.app.dictNav[self.app.dictNav[self.app.End].zavisle].stavanieDo = False
                                self.app.dictNav[self.app.dictNav[self.app.End].zavisle].koncove = True
                                self.app.dictNav[self.app.dictNav[self.app.End].zavisle].update(self)

                    if self.ochrDraha: #ak má cesta definovanú ochrannú dráhu
                        for usek in zaverTab.dictVC[self.cesta]['UsekyOD']:   #vyberaj z úsekov danej cesty                         
                            if self.app.workerThread.dictUseky[i].nazovGUI == usek: #ak sa názvy zhodujú, definuj úsek ako záverovaný
                                self.app.workerThread.dictUseky[i].stavanieOchr = False                                    
                                self.app.workerThread.dictUseky[i].ochr = True                                 
                                self.app.workerThread.dictUseky[i].update(self)

                    if self.typCesty:   #v prípade posunu na obsadenú koľaj sa vytvorí záver aj danej koľaje
                        for usek in zaverTab.dictVC[self.cesta]['dopUseky']: #vyber úsek zo záverovej tabuľky
                            if self.app.workerThread.dictUseky[i].nazovGUI == usek:    #ak sa názvy zhodujú, vytvor záver jazdnej cesty
                                self.app.workerThread.dictUseky[i].stavaniePosun = False
                                self.app.workerThread.dictUseky[i].posun = True
                                self.app.workerThread.dictUseky[i].update(self)

                #------------ROZSVIETENIE POVOĽUJÚCEJ NÁVESTI POČIATOČNÉHO NÁVESTIDLA------------ 
                for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov 
                    usek = zaverTab.dictVC[self.cesta].get('1TU', None)   #vyber úsek zo záverovej tabuľky                    
                    if usek is None:    #rozsvietenie návesti pre posunovú cestu 
                        self.app.dictNav[self.app.End].zaverPC = True
                        self.app.dictNav[self.app.Start].pociatocne = True
                        
                        if Disp and (self.app.dictNav[self.app.Start].zavisle != -1) and (self.app.dictNav[self.app.End].zavisle != -1): #úprava pre dispečerskú aplikáciu
                            self.app.dictNav[self.app.dictNav[self.app.End].zavisle].zaverPC = True
                            self.app.dictNav[self.app.dictNav[self.app.Start].zavisle].pociatocne = True

                        if (self.app.workerThread.dictUseky[i].jeVolny) or (usek == '0'): #ak je 1. úsek za odchdovou cestou voľný
                            self.app.dictNav[self.app.Start].znak = 'Posun' #rozsvietenie povoľujúcej návesti na návestidle 
                            
                            if Disp and (self.app.dictNav[self.app.Start].zavisle != -1): #úprava pre dispečerskú aplikáciu
                                self.app.dictNav[self.app.dictNav[self.app.Start].zavisle].znak = 'Posun'                              
                            
                            
                            if not server:
                                self.app.prikazDoPLC(prikaz='/Posun', id=self.app.dictNav[self.app.Start].ID, nazov=self.app.dictNav[self.app.Start].nazov)
                            break
                    
                    else:   #rozsvietenie návesti pre vlakovú cestu
                        if (self.app.workerThread.dictUseky[i].nazovGUI == usek) or (usek == '0') and not self.typCesty:    #ak sa názvy zhodujú
                            self.app.dictNav[self.app.End].zaverVC = True
                            self.app.dictNav[self.app.Start].pociatocne = True
                            
                            if Disp: #úprava pre dispečerskú aplikáciu
                                self.app.dictNav[self.app.dictNav[self.app.End].zavisle].zaverVC = True                           
                                self.app.dictNav[self.app.dictNav[self.app.Start].zavisle].pociatocne = True

                            if (self.app.workerThread.dictUseky[i].jeVolny) or (usek == '0'):
                                self.app.dictNav[self.app.Start].znak = 'Volno' 
                                
                                if Disp: #úprava pre dispečerskú aplikáciu
                                    self.app.dictNav[self.app.dictNav[self.app.Start].zavisle].znak = 'Volno'
                                
                                
                                if not server:
                                    self.app.prikazDoPLC(prikaz='/Volno', id=self.app.dictNav[self.app.Start].ID, nazov=self.app.dictNav[self.app.Start].nazov)
                                break

                if self.ochrDraha:  #zápis ochrannej dráhy do PLC
                    if not server:
                        self.app.prikazDoPLC(prikaz='/True', nazov=self.cesta, OD=True)
                
                self.app.dictNav[self.app.Start].update(self)
                self.app.dictNav[self.app.End].update(self)
                
                if Disp and (self.app.dictNav[self.app.Start].zavisle != -1) and (self.app.dictNav[self.app.End].zavisle != -1): #úprava pre dispečerskú aplikáciu
                    self.app.dictNav[self.app.dictNav[self.app.Start].zavisle].update(self)
                    self.app.dictNav[self.app.dictNav[self.app.End].zavisle].update(self)             

                #------------DEFINITÍVNE ZÁVEROVANIE VÝHYBIEK------------ 
                for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov
                    if self.cesta in zaverTab.dictVC.keys():    #vyberaj pre aktuálne stavanú jazdnú cestu                      
                        for vyhybka in zaverTab.dictVC[self.cesta].keys():  #vyberaj z výhybiek jazdnej cesty v záverovej tabuľke                   
                            if vyhybka == self.app.workerThread.dictUseky[i].nazovGUI:     #ak sa názvy výhybiek zhodujú   
                                if i in [12,13]:   #úprava pre koľajovú spojku
                                    self.app.workerThread.dictUseky[12].zaver = True    #záver koľajovej spojky
                                    self.app.workerThread.dictUseky[13].zaver = True   
                                    self.app.workerThread.dictUseky[12].update(self)
                                    self.app.workerThread.dictUseky[13].update(self)
                                
                                elif i in [40,41]:   #úprava pre koľajovú spojku
                                    self.app.workerThread.dictUseky[40].zaver = True    #záver koľajovej spojky
                                    self.app.workerThread.dictUseky[41].zaver = True   
                                    self.app.workerThread.dictUseky[40].update(self)
                                    self.app.workerThread.dictUseky[41].update(self)
                               
                                else:                                    
                                    self.app.workerThread.dictUseky[i].zaver = True    #záver výhybky
                                    self.app.workerThread.dictUseky[i].update(self)

                self.cesta = ' '    #ukončenie stavania jazdnej cesty
                self.ochrDraha = False

                self.dictStavanieCesty['stavanie'] = False  #vynulovanie parametrov stavania jazdnej cesty
                self.dictStavanieCesty['volnost'] = False
                self.dictStavanieCesty['vymeny'] = False

            #if not update:  #ak nie je metóda volaná iba pre aktualizáciu stavu 
                if not server:
                    self.app.prikazDoPLC(cesta=True, nazov='stavanie', prikaz=str(OD))

                    if self.app.Start in [4,5,47,48] and not self.typCesty:
                        self.app.prikazDoPLC(odchod=True, nazov='odchodR', prikaz='/True')
                    
                    elif self.app.Start in [20,62] and not self.typCesty:
                        self.app.prikazDoPLC(odchod=True, nazov='odchodZR', prikaz='/True')

                    elif self.app.Start in [21,63] and self.app.End in [14,60] and not self.typCesty:
                        self.app.prikazDoPLC(odchod=True, nazov='odchodZR', prikaz='/True')

                    elif self.app.Start in [21,63] and self.app.End in [15,61] and not self.typCesty:
                        self.app.prikazDoPLC(odchod=True, nazov='odchodZL', prikaz='/True')

                    elif self.app.Start in [22,23,64,65] and not self.typCesty:
                        self.app.prikazDoPLC(odchod=True, nazov='odchodZH', prikaz='/True')
                        self.app.prikazDoPLC(prikaz='/True', nazov='ZBE', predhl=True)
                        for nav in [30,44,69]:
                            if nav in self.app.dictNav.keys():
                                self.app.prikazDoPLC(prikaz='/Volno', id=self.app.dictNav[nav].ID, nazov=self.app.dictNav[nav].nazov)
                                break 

                    elif self.app.Start in [38,39,72,73] and not self.typCesty:
                        self.app.prikazDoPLC(odchod=True, nazov='odchodH', prikaz='/True')
                        self.app.prikazDoPLC(prikaz='/True', nazov='HLO', predhl=True)
                        for nav in [31,45,70]:
                            if nav in self.app.dictNav.keys():
                                self.app.prikazDoPLC(prikaz='/Volno', id=self.app.dictNav[nav].ID, nazov=self.app.dictNav[nav].nazov)
                                break 

                self.app.Start = 0
                self.app.End = 0
                self.stavCesty = False  #ukonči stavanie

    def rusenieCesty(self, cas = False, Disp = False, server=False):    #metóda pre rušenie jazdnej cesty
        if not cas: #ak nie je metóda volaná po uplynutí čaového súboru 

            #------------HĽADANIE RUŠENEJ CESTY V ZÁVEROVEJ TABUĽKE------------
            for id in zaverTab.dictVC.keys():   #vyberaj zo záverovej tabuľky                
                if (self.app.dictNav[self.app.End].nazov in zaverTab.dictVC[id]['stop']):   #ak nájdeš cestu s koncovým návestuidlom, ktoré obsluha vybrala                    
                    for nav in self.app.dictNav.keys(): #vyberaj z návestidiel                        
                        if (self.app.dictNav[nav].nazov in zaverTab.dictVC[id]['start'])  and (
                        (self.app.dictNav[nav].znak == 'Volno') or (self.app.dictNav[nav].znak == 'Posun')):
                        #ak nájdeš návestidlo s povoľujúcim znakom zapísané ako počiatočné návestidlo vybranej jazdnej cesty
                            if ((self.app.dictNav[self.app.End].OD is True) and ('UsekyOD' in zaverTab.dictVC[id].keys())) or (self.app.dictNav[self.app.End].OD is False):
                            #ak je za koncovým návestidlom cesty aktívna ochranná dráha a je v jazdnej ceste definovaná ALEBO nie
                                for usek in self.app.workerThread.dictUseky.keys():    #vyberaj z úsekov
                                    for vyh in zaverTab.dictVC[id].keys():  #hľadaj výhybky jazdnej cesty v záverovej tabuľke 
                                        if self.app.workerThread.dictUseky[usek].nazovGUI == vyh:  #ak ich nájdeš
                                            if  (zaverTab.dictVC[id][vyh][0]) == (self.app.workerThread.dictUseky[usek].smer): #ak je polohy výmen správna pre danú cestu                                                                                           
                                                self.app.dictNav[nav].znak = 'Stoj' #zmeň znak na zakazujúci
                                                self.app.dictNav[nav].pociatocne = False
                                                self.app.dictNav[nav].manual = False
                                                self.app.dictNav[nav].update(self)
                                                
                                                if Disp and (self.app.dictNav[nav].zavisle != -1): #úprava pre dispečerskú aplikáciu
                                                    self.app.dictNav[self.app.dictNav[nav].zavisle].znak = 'Stoj' 
                                                    self.app.dictNav[self.app.dictNav[nav].zavisle].pociatocne = False
                                                    self.app.dictNav[self.app.dictNav[nav].zavisle].manual = False
                                                    self.app.dictNav[self.app.dictNav[nav].zavisle].update(self)

                                                self.rusenaCesta = id   #zapíš aktuálne vybranú cestu ako rušenú
                                                
                                                if self.app.dictNav[self.app.End].OD:   #ak cesta obsahuje ochrannú dráhu
                                                    self.ochrDraha = True
                                                    self.app.dictNav[self.app.End].OD = False
                                                    
                                                    if Disp: #úprava pre dispečerskú aplikáciu
                                                        self.app.dictNav[self.app.dictNav[self.app.End].zavisle].OD = False
                                                    
                                                    if not server:
                                                        self.app.prikazDoPLC(prikaz='/False', nazov=self.rusenaCesta, OD=True)

                                                if not server:
                                                    self.app.prikazDoPLC(prikaz='/Stoj', id=self.app.dictNav[nav].ID, nazov=self.app.dictNav[nav].nazov)
                                                break
                                    if self.rusenaCesta != ' ': #po úspešnom vyhľadaní rušenej cesty sa opúšťajú vyhľadávacie cykly
                                        break
                                if self.rusenaCesta != ' ':
                                    break   
                    if self.rusenaCesta != ' ':
                        break

            #------------KONTROLA VOĽNOSTI PRIBLIŽOVACIEHO ÚSEKU A SPUSTENIE RUŠENIA CESTY------------
            if self.rusenaCesta != ' ':
                for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov                    
                    if zaverTab.dictVC[self.rusenaCesta]['PU'] == self.app.workerThread.dictUseky[i].nazovGUI:  #ak nájdeš približovací úsek
                        self.app.dictNav[self.app.End].rusenie = True   #zobraz pri symbole koncového návestidla fialový index
                        if self.app.workerThread.dictUseky[i].jeVolny: #ak je voľný
                            cas = True  #zruš cestu okamžite
                            self.app.dictNav[self.app.End].zaverVC = False  #zruš jej záver
                            self.app.dictNav[self.app.End].zaverPC = False 
                            
                            if Disp and self.app.dictNav[self.app.End].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                self.app.dictNav[self.app.dictNav[self.app.End].zavisle].zaverVC = False  
                                self.app.dictNav[self.app.dictNav[self.app.End].zavisle].zaverPC = False  
                            
                            break

                        else:   #ak je obsadený
                            if self.app.dictNav[self.app.End].zaverVC:  #ak sa jedná o vlakovú cestu
                                self.app.dictNav[self.app.End].zaverVC = False  #zruš jej záver
                                
                                if Disp: #úprava pre dispečerskú aplikáciu
                                    self.app.dictNav[self.app.dictNav[self.app.End].zavisle].zaverVC = False
                                
                                self.app.workerThreadTimeVlak.start_timer()  #spusti časový súbor rušenia vlakovej cesty (3 min)
                                break

                            elif self.app.dictNav[self.app.End].zaverPC:    #ak sa jedná o posunovú cestu
                                self.app.dictNav[self.app.End].zaverPC = False  #zruš jej záver
                                
                                if Disp: #úprava pre dispečerskú aplikáciu
                                    self.app.dictNav[self.app.dictNav[self.app.End].zavisle].zaverPC = False
                                
                                self.app.workerThreadTimePosun.start_timer() #spusti časový súbor rušenia posunovej cesty (1 min)
                                break

                self.app.dictNav[self.app.End].update(self) #aktualizuj symbol koncového návestidla
                if Disp and self.app.dictNav[self.app.End].zavisle != -1: #úprava pre dispečerskú aplikáciu
                    self.app.dictNav[self.app.dictNav[self.app.End].zavisle].update(self)

        #------------VYPRŠANIE ČASOVÝCH SÚBOROV RUŠENIA CESTY------------
        if cas: #ak je metóda volaná po uplynutí čaového súboru  
            if self.rusenaCesta != ' ':  
                for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov
                    #------------RUŠENIE ZÁVERU ÚSEKOV JAZDNEJ CESTY------------                
                    for usek in zaverTab.dictVC[self.rusenaCesta]['Useky']:  #vyberaj z úsekov 
                        if self.app.workerThread.dictUseky[i].nazovGUI == usek:    #ak sa názvy úsekov zhodujú
                            self.app.workerThread.dictUseky[i].vlak = False    #zruš záver daného úseku
                            self.app.workerThread.dictUseky[i].posun = False                        
                            
                            if i in [12,13]:  #špeciálna úprava pre koľajovú spojku
                                if (i == 12 and ((
                                self.app.workerThread.dictUseky[13].vlak is True) or (
                                self.app.workerThread.dictUseky[13].posun is True) or (
                                self.app.workerThread.dictUseky[13].ochr is True))) or (
                                i == 13 and ((
                                self.app.workerThread.dictUseky[12].vlak is True) or (
                                self.app.workerThread.dictUseky[12].posun is True) or (
                                self.app.workerThread.dictUseky[12].ochr is True))
                                ):
                                    self.app.workerThread.dictUseky[i].zaver = True
                                    
                                else:
                                    self.app.workerThread.dictUseky[12].zaver = False
                                    self.app.workerThread.dictUseky[13].zaver = False
                            
                            elif i in [40,41]:  #špeciálna úprava pre koľajovú spojku
                                if (i == 40 and ((
                                self.app.workerThread.dictUseky[41].vlak is True) or (
                                self.app.workerThread.dictUseky[41].posun is True) or (
                                self.app.workerThread.dictUseky[41].ochr is True))) or (
                                i == 41 and ((
                                self.app.workerThread.dictUseky[40].vlak is True) or (
                                self.app.workerThread.dictUseky[40].posun is True) or (
                                self.app.workerThread.dictUseky[40].ochr is True))
                                ):
                                    self.app.workerThread.dictUseky[i].zaver = True
                                    
                                else:
                                    self.app.workerThread.dictUseky[40].zaver = False
                                    self.app.workerThread.dictUseky[41].zaver = False

                            else:
                                self.app.workerThread.dictUseky[i].zaver = False

                            self.app.workerThread.dictUseky[i].update(self)

                            for nav in self.app.dictNav.keys(): #vyberaj z návestidiel                            
                                if (self.app.workerThread.dictUseky[i].nazovGUI == self.app.dictNav[nav].usekPred): #and (self.app.dictNav[nav].ID != self.app.End) and (
                                    self.app.dictNav[nav].vlak = False  #uprav jeho symbol
                                    self.app.dictNav[nav].posun = False
                                    self.app.dictNav[nav].update(self)
                                    
                                    if Disp and self.app.dictNav[nav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                        self.app.dictNav[self.app.dictNav[nav].zavisle].vlak = False  #uprav jeho symbol
                                        self.app.dictNav[self.app.dictNav[nav].zavisle].posun = False
                                        self.app.dictNav[self.app.dictNav[nav].zavisle].update(self)

                    for usek in zaverTab.dictVC[self.rusenaCesta]['dopUseky']: #vyber úsek zo záverovej tabuľky
                        if usek is not None:
                            if self.app.workerThread.dictUseky[i].nazovGUI == usek:    #ak sa názvy úsekov zhodujú
                                self.app.workerThread.dictUseky[i].posun = False   #zruš záver úseku

                                for nav in self.app.dictNav.keys(): #vyberaj z návestidiel                                
                                    if (self.app.workerThread.dictUseky[i].nazovGUI == self.app.dictNav[nav].usekPred): #and (self.app.dictNav[nav].ID != self.app.End) and (
                                        self.app.dictNav[nav].posun = False #uprav jeho symbol
                                        self.app.dictNav[nav].update(self)
                                        
                                        if Disp and self.app.dictNav[nav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                            self.app.dictNav[self.app.dictNav[nav].zavisle].posun = False 
                                            self.app.dictNav[self.app.dictNav[nav].zavisle].update(self)

                    if self.ochrDraha:  #ak sa ruší aj ochranná dráha
                        for usek in zaverTab.dictVC[self.rusenaCesta]['UsekyOD']:  #vyberaj z úsekov 
                            if self.app.workerThread.dictUseky[i].nazovGUI == usek:    #ak sa názvy úsekov zhodujú
                                self.app.workerThread.dictUseky[i].ochr = False    #zruš záver daného úseku
                                if i in [12,13]:  #špeciálna úprava pre koľajovú spojku
                                    
                                    if i == 12 and ((self.app.workerThread.dictUseky[13].vlak is True) or (self.app.workerThread.dictUseky[13].posun is True) or (
                                    self.app.workerThread.dictUseky[13].ochr is True)):
                                        self.app.workerThread.dictUseky[12].zaver = False
                                    
                                    elif i == 13 and ((self.app.workerThread.dictUseky[12].vlak is True) or (self.app.workerThread.dictUseky[12].posun is True) or (
                                    self.app.workerThread.dictUseky[12].ochr is True)):
                                        self.app.workerThread.dictUseky[13].zaver = False
                                    
                                    else:
                                        self.app.workerThread.dictUseky[12].zaver = False
                                        self.app.workerThread.dictUseky[13].zaver = False

                                elif i in [40,41]:  #špeciálna úprava pre koľajovú spojku
                                    if i == 40 and ((self.app.workerThread.dictUseky[41].vlak is True) or (self.app.workerThread.dictUseky[41].posun is True) or (
                                    self.app.workerThread.dictUseky[41].ochr is True)):
                                        self.app.workerThread.dictUseky[40].zaver = False
                                    
                                    elif i == 41 and ((self.app.workerThread.dictUseky[40].vlak is True) or (self.app.workerThread.dictUseky[40].posun is True) or (
                                    self.app.workerThread.dictUseky[40].ochr is True)):
                                        self.app.workerThread.dictUseky[41].zaver = False
                                    
                                    else:
                                        self.app.workerThread.dictUseky[40].zaver = False
                                        self.app.workerThread.dictUseky[41].zaver = False

                                else:
                                    self.app.workerThread.dictUseky[i].zaver = False

                                self.app.workerThread.dictUseky[i].update(self)

                                for nav in self.app.dictNav.keys(): #vyberaj z návestidiel                            
                                    if (self.app.workerThread.dictUseky[i].nazovGUI == self.app.dictNav[nav].usekPred): #and (self.app.dictNav[nav].ID != self.app.End) and (
                                        self.app.dictNav[nav].ochr = False  #uprav jeho symbol
                                        self.app.dictNav[nav].update(self)
                                        
                                        if Disp and self.app.dictNav[nav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                            self.app.dictNav[self.app.dictNav[nav].zavisle].ochr = False                                        
                                            self.app.dictNav[self.app.dictNav[nav].zavisle].update(self)

                self.app.dictNav[self.app.End].rusenie = False  #ukončenie rušenia jazdnej cesty
                self.app.dictNav[self.app.End].update(self)
                
                if Disp and self.app.dictNav[self.app.End].zavisle != -1: #úprava pre dispečerskú aplikáciu
                    self.app.dictNav[self.app.dictNav[self.app.End].zavisle].rusenie = False  
                    self.app.dictNav[self.app.dictNav[self.app.End].zavisle].update(self)

                self.rusenaCesta = ' '
                if not server:
                    self.app.prikazDoPLC(cesta=True, nazov='rusenie')
                
                self.app.End = 0
                self.ochrDraha = False

    def rusenieOD(self, Disp = False):
        for id in zaverTab.dictVC.keys():   #vyberaj zo záverovej tabuľky             
            for nav in self.app.dictNav.keys(): #vyberaj z návestidiel    
                if (self.app.dictNav[nav].koncove is True) and (self.app.dictNav[nav].nazov in zaverTab.dictVC[id]['stop']) and (
                'UsekyOD' in zaverTab.dictVC[id].keys()):
                #ak je návestidlo definované ako koncové a je nájdené v jazdnej ceste s ochrannou dráhou                  

                    #------------RUŠENIE OCHRANNEJ DRÁHY JAZDNEJ CESTY------------
                    self.app.dictNav[nav].koncove = False
                    if Disp and self.app.dictNav[nav].zavisle != -1:
                        self.app.dictNav[self.app.dictNav[nav].zavisle].koncove = False

                    for i in self.app.workerThread.dictUseky.keys():   #vyberaj zo všetkých úsekov 
                        for usek in zaverTab.dictVC[id]['UsekyOD']:  #vyberaj z úsekov 
                            if self.app.workerThread.dictUseky[i].nazovGUI == usek:    #ak sa názvy úsekov zhodujú
                                self.app.workerThread.dictUseky[i].ochr = False    #zruš záver daného úseku
                                
                                if i in [12,13]:  #špeciálna úprava pre koľajovú spojku
                                    self.app.workerThread.dictUseky[12].zaver = False
                                    self.app.workerThread.dictUseky[13].zaver = False

                                elif i in [40,41]:  #špeciálna úprava pre koľajovú spojku
                                    self.app.workerThread.dictUseky[40].zaver = False
                                    self.app.workerThread.dictUseky[41].zaver = False

                                else:
                                    self.app.workerThread.dictUseky[i].zaver = False
                                self.app.workerThread.dictUseky[i].update(self)

                                for nav in self.app.dictNav.keys(): #vyberaj z návestidiel                            
                                    if (self.app.workerThread.dictUseky[i].nazovGUI == self.app.dictNav[nav].usekPred) and (self.app.dictNav[nav].ID != self.app.End) and (
                                    self.app.dictNav[nav].zavisle != self.app.End):  #ak sa návestidlo nachádza v úseku jazdnej cesty a nie je koncové návestidlo                                
                                        self.app.dictNav[nav].ochr = False  #uprav jeho symbol
                                        self.app.dictNav[nav].update(self)
                                        
                                        if Disp and self.app.dictNav[nav].zavisle != -1: #úprava pre dispečerskú aplikáciu
                                            self.app.dictNav[self.app.dictNav[nav].zavisle].ochr = False
                                            self.app.dictNav[self.app.dictNav[nav].zavisle].update(self)

                    self.app.prikazDoPLC(prikaz='/False', nazov=id, OD=True)

    def prestavenieVyh(self, vyhybka, index):  #metóda pre ručné prestavovanie výmen
            self.app.ui.combo_vyh.hide()
            
            if vyhybka in [12,13]:
                spojkaOK = False
                for id in [12,13]:
                    if (self.app.workerThread.dictUseky[id].jeVolny) and ((self.app.workerThread.dictUseky[id].vlak is False) and (
                    self.app.workerThread.dictUseky[id].posun is False) and (self.app.workerThread.dictUseky[id].ochr is False)):           
                        spojkaOK = True
                    
                    else:
                        break

                if spojkaOK:
                    if index == 1:  #ak bolo v menu vybraný príkaz na prestavenie začni prestavovať výmenu
                        self.app.workerThread.dictUseky[12].prest = True 
                        self.app.workerThread.dictUseky[13].prest = True
                        
                        if self.app.workerThread.dictUseky[vyhybka].zavisla != -1: #úprava pre dispečerskú aplikáciu
                            self.app.workerThread.dictUseky[self.app.workerThread.dictUseky[12].zavisla].prest = True 
                            self.app.workerThread.dictUseky[self.app.workerThread.dictUseky[13].zavisla].prest = True
                        
                        self.app.clickObjekt(id=13, objekt='vyhybka')

                        if (self.app.workerThread.dictUseky[12].smer) and (self.app.workerThread.dictUseky[13].smer):
                            self.app.prikazDoPLC(prikaz='/True', nazov=self.app.workerThread.dictUseky[vyhybka].nazovGUI, vyh=True)
                        
                        else:
                            self.app.prikazDoPLC(prikaz='/False', nazov=self.app.workerThread.dictUseky[vyhybka].nazovGUI, vyh=True)

            elif vyhybka in [40,41]:
                spojkaOK = False
                for id in [40,41]:
                    if (self.app.workerThread.dictUseky[id].jeVolny) and ((self.app.workerThread.dictUseky[id].vlak is False) and (
                    self.app.workerThread.dictUseky[id].posun is False) and (self.app.workerThread.dictUseky[id].ochr is False)):           
                        spojkaOK = True
                    
                    else:
                        break

                if spojkaOK:
                    if index == 1:  #ak bolo v menu vybraný príkaz na prestavenie začni prestavovať výmenu
                        self.app.workerThread.dictUseky[40].prest = True 
                        self.app.workerThread.dictUseky[41].prest = True
                        
                        if self.app.workerThread.dictUseky[vyhybka].zavisla != -1: #úprava pre dispečerskú aplikáciu
                            self.app.workerThread.dictUseky[self.app.workerThread.dictUseky[40].zavisla].prest = True 
                            self.app.workerThread.dictUseky[self.app.workerThread.dictUseky[41].zavisla].prest = True 
                        
                        self.app.clickObjekt(id=41, objekt='vyhybka')

                        if (self.app.workerThread.dictUseky[40].smer) and (self.app.workerThread.dictUseky[41].smer):
                            self.app.prikazDoPLC(prikaz='/True', nazov=self.app.workerThread.dictUseky[vyhybka].nazovGUI, vyh=True)
                        
                        else:
                            self.app.prikazDoPLC(prikaz='/False', nazov=self.app.workerThread.dictUseky[vyhybka].nazovGUI, vyh=True)

            else:
                if (self.app.workerThread.dictUseky[vyhybka].jeVolny) and ((self.app.workerThread.dictUseky[vyhybka].vlak is False) and (
                self.app.workerThread.dictUseky[vyhybka].posun is False) and (self.app.workerThread.dictUseky[vyhybka].ochr is False)):           
                    if index == 1:  #ak bolo v menu vybraný príkaz na prestavenie začni prestavovať výmenu
                        self.app.workerThread.dictUseky[vyhybka].prest = True 
                        self.app.workerThread.dictUseky[vyhybka].vyber = False
                        
                        if self.app.workerThread.dictUseky[vyhybka].zavisla != -1: #úprava pre dispečerskú aplikáciu
                            self.app.workerThread.dictUseky[self.app.workerThread.dictUseky[vyhybka].zavisla].prest = True 
                            self.app.workerThread.dictUseky[self.app.workerThread.dictUseky[vyhybka].zavisla].vyber = False 

                        if self.app.workerThread.dictUseky[vyhybka].smer:
                            self.app.prikazDoPLC(prikaz='/True', nazov=self.app.workerThread.dictUseky[vyhybka].nazovGUI, vyh=True)
                        
                        else:
                            self.app.prikazDoPLC(prikaz='/False', nazov=self.app.workerThread.dictUseky[vyhybka].nazovGUI, vyh=True)

            self.app.ui.combo_vyh.setCurrentIndex(0)    #vynulovanie výberového menu pre ďalšie použitie