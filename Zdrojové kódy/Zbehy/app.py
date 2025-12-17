from PySide6.QtWidgets import QApplication, QMainWindow
import sys
import requests
import arrow

import ico
from ui_form import Ui_ILTIS
from zoznamNavestidiel import ZoznamNavestidiel
from SZZ import SZZ
from update import DataUpdate
from datum import Datum
from casSubory import DlhyCasPosun, DlhyCasVlak, CasOchrDr, LifeSign

# Important: You need to run the following command to generate the ui_form.py file: pyside6-uic form.ui -o ui_form.py

class App(QMainWindow): #hlavná triedy vizualizácie
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ILTIS()    #vytvorenie spojenia s triedami
        self.szz = SZZ(self) 

        self.vlaknoUpdate = DataUpdate(self)   #prepojenie bočných vláken s hlavným vláknom
        self.vlaknoDlhyCasVlak = DlhyCasVlak()
        self.vlaknoDlhyCasPosun = DlhyCasPosun()
        self.vlaknoCasOchrDrahy = CasOchrDr()
        self.vlaknoLifeSign = LifeSign(self)
        self.vlaknoDatum = Datum()

        self.zoznamNavOBJ = ZoznamNavestidiel(parent = self)    #objekt zoznamu návestidiel
        self.zoznamNav = self.zoznamNavOBJ.zoznamNav

        self.vlaknoUpdate.setParent(self)  #definovanie rodičovského objektu pre vlákna
        self.vlaknoLifeSign.setParent(self)

        self.ui.setupUi(self)

        self.vlaknoDatum.pociatocneNav()

        self.vlaknoUpdate.dataUpdated.connect(self.update) #definícia prepojenia vláken a metód
        self.vlaknoUpdate.dataUpdated.connect(lambda: self.szz.update(Disp=True))

        self.vlaknoDatum.dataUpdated.connect(self.aktualizaciaCasu)
        
        self.vlaknoDlhyCasVlak.finished.connect(lambda: self.szz.uplynutieCasSuboru(Disp=True))
        self.vlaknoDlhyCasPosun.finished.connect(lambda: self.szz.uplynutieCasSuboru(Disp=True))
        self.vlaknoCasOchrDrahy.finished.connect(lambda: self.szz.rusenieOD(Disp=True)) 

        self.posledneNav:int = 0  #posledné kliknuté návestidlo
        self.pociatocneNav:int = 0    #počiatočné návestidlo jazdnej cesty
        self.koncoveNav:int = 0    #koncové návestidlo jazdnej cesty

        self.poslednaVyh:str = 'X'  #posledná kliknutá výhybka
        self.poslednePriec:str = 'X'  #posledné kliknuté priecestie 
        self.poslednaStn:str = 'X' #posledná kliknutá stanica
        self.poslednyTS:str = 'X'   #posledný kliknutý traťový súhlas
        self.predposlednyTS:str = 'X' #predposledný kliknutý traťový súhlas

        self.zoznamNav[28].zhasnute = True

    def popUp(self, okno): #zobrazenie a skrytie kontextového okna s RAST API adresou
        if okno == 'REST':
            self.ui.groupREST.setVisible(not(self.ui.groupREST.isVisible()))

        elif okno == 'Prehlad':
            self.ui.groupPrehlad.setVisible(not(self.ui.groupPrehlad.isVisible()))

    def citajAdresu(self): #načítanie adresy zadanej užívateľom
        adresa = self.ui.Line_IP.text()
        URL = "http://{}/".format(adresa)
        return(URL)

    def zahajPripojenie(self):  #metóda pre testovanie pripojenia k PLC
        IP = self.citajAdresu()
        URL = IP + 'test'

        try:
            response = requests.get(URL)    
            resp = response.json()
        except (requests.exceptions.ConnectionError):
            print('zla IP adresa')
            return -1

        if resp['OK']:
            self.ui.textChybaREST.hide()
            self.ui.groupREST.hide()

            self.vlaknoUpdate.start()    #po úspešnom spojení sa spúšťa beh vláken
            self.vlaknoDlhyCasVlak.start()
            self.vlaknoDlhyCasPosun.start()
            self.vlaknoCasOchrDrahy.start()
            self.vlaknoLifeSign.start()

            self.ui.ZBE_ASVC.setIcon(ico.icon_ASVC_vypnute)

    def ukonciPripojenie(self):  #metóda pre zastavenie vláken a ukončenie komunikácie
        self.vlaknoUpdate.requestInterruption()    
        self.vlaknoDlhyCasVlak.requestInterruption()
        self.vlaknoDlhyCasPosun.requestInterruption()
        self.vlaknoCasOchrDrahy.requestInterruption()  
        self.vlaknoLifeSign.requestInterruption()  
        self.vlaknoDatum.requestInterruption()   

        self.ui.textChybaREST.show()
        self.ui.textChybaESA.show() 

    def aktualizaciaCasu(self, cas):    #metóda pre aktualizáciu času v GUI
        self.ui.DateTime.setText(cas)

    def update(self, ID:int=-1, clicked:bool=False, objekt:str='update'): #metóda pre aktualizáciu symbolov objektov
        if objekt in ['update', 'useky']:   #aktualizácia úsekov
            for i in self.vlaknoUpdate.dictUseky.keys():
                self.vlaknoUpdate.dictUseky[i].update(self)
                
                if self.vlaknoUpdate.dictUseky[21].odozva:
                    self.ui.textChybaESA.hide()
                
                else:
                    self.ui.textChybaESA.show()

        if objekt in ['update', 'navestidla']:  #aktualizácia návestidiel
            self.zoznamNav[28].zhasnute =  not self.vlaknoUpdate.dictTS[2].smer  #otáčanie svietenia AB podľa TS
            self.zoznamNav[29].zhasnute =  self.vlaknoUpdate.dictTS[2].smer
            
            self.zoznamNav[30].predhlaska = self.vlaknoUpdate.predhlaskaZBE
            self.zoznamNav[31].predhlaska = self.vlaknoUpdate.predhlaskaHLO

            if clicked and ID in self.zoznamNav:  #ak bolo návestidlo kliknuté obsluhou
                self.zoznamNav[ID].vybrane = not self.zoznamNav[ID].vybrane 
                for i in self.zoznamNav.keys():
                    if i != ID:
                        self.zoznamNav[i].vybrane = False               

            for ID in self.zoznamNav.keys():  #vyberaj z návestidiel
                for i in self.vlaknoUpdate.dictUseky.keys():   #vyberaj z úsekov
                    if self.zoznamNav[ID].usekPred == self.vlaknoUpdate.dictUseky[i].nazovGUI:   #ak sa nájde úsek previazaný s návestidlom
                        self.zoznamNav[ID].jeVolnyPred = self.vlaknoUpdate.dictUseky[i].jeVolny  #aktualizuj symbol návestidla podľa obsadenia úseku

                    if self.zoznamNav[ID].usekPred == self.vlaknoUpdate.dictUseky[i].nazovGUI:   #ak sa nájde úsek previazaný s návestidlom
                        self.zoznamNav[ID].usekOdozva = self.vlaknoUpdate.dictUseky[i].odozva  #aktualizuj symbol návestidla podľa LIfeSign úseku
                        
                    if self.zoznamNav[ID].usekZa == self.vlaknoUpdate.dictUseky[i].nazovGUI:   #ak sa nájde úsek previazaný s návestidlom
                        self.zoznamNav[ID].jeVolnyZa = self.vlaknoUpdate.dictUseky[i].jeVolny  #aktualizuj symbol návestidla podľa obsadenia úseku

                self.zoznamNav[ID].update(self)

        if objekt in ['update', 'priecestie']:  #aktualizácia priecestí
            for i in self.vlaknoUpdate.dictPriecestie.keys():
                self.vlaknoUpdate.dictPriecestie[i].update(self)

        if objekt in ['update', 'TS']:  #aktualizácia traťového súhlasu
            for i in self.vlaknoUpdate.dictTS.keys():
                self.vlaknoUpdate.dictTS[i].update(self)
                self.ziadostAktivna = self.vlaknoUpdate.dictTS[i].ziadost

        if objekt in ['update', 'Stanice']: #aktualizácia raidenia stanice
            if clicked and ID in self.vlaknoUpdate.dictStanice:  
                self.vlaknoUpdate.dictStanice[ID].vyber = not self.vlaknoUpdate.dictStanice[ID].vyber
            for i in self.vlaknoUpdate.dictStanice.keys():
                self.vlaknoUpdate.dictStanice[i].update(self)

    def clickObjekt(self, id:int, objekt:str): #metóda spracovávajúca kliknutie na objekt
        if objekt == 'navestidlo':
            self.posledneNav = id   #zápis posledného kliknutého návestidla                
            
            if not self.vlaknoUpdate.dictStanice[2].dialkove:   #ak má precovisko aktívne riadenie 
                self.update(id, True, 'navestidla')            
                if self.zoznamNav[id].nazov in ['Z_L', 'Z_BL', 'Z_S']: #vchodové návestidlo
                    if self.zoznamNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('vchodove')
                    
                    elif self.zoznamNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('vchodove_konc')
                    
                    else:
                        self.comboShowHide()

                elif self.zoznamNav[id].nazov in ['Z_S1','Z_S2','Z_L1','Z_L2']:    #odchodové návestidlo
                    if self.zoznamNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('odchodove')
                    
                    elif self.zoznamNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('odchodove_konc')
                    
                    else:
                        self.comboShowHide()

                elif self.zoznamNav[id].nazov in ['Z_Se1p','Z_Se2p','Z_Se1','Z_Se2','Z_Se3','Z_Se3p']:  #zriaďovacie návestidlo
                    if self.zoznamNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('zriadovacie')
                    
                    elif self.zoznamNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('zriadovacie_konc')
                    
                    else:
                        self.comboShowHide()

                elif self.zoznamNav[id].nazov in ['Z_L_fik', 'Z_BL_fik', 'Z_S_fik']:   #fiktívne návestidlo
                    if self.zoznamNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('fiktivne')
                    
                    elif self.zoznamNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('fiktivne_konc')
                    
                    else:
                        self.comboShowHide()

                elif self.zoznamNav[id].nazov in ['Z_So']:   #oddielové návestidlo
                    if self.zoznamNav[id].vybrane:
                        self.comboShowHide('oddielove')
                    
                    else:
                        self.comboShowHide()

            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko vzdialenej obsluhy')

        elif objekt == 'vyhybka':
            if not self.vlaknoUpdate.dictStanice[2].dialkove:   #ak má precovisko aktívne riadenie 
                if id in self.vlaknoUpdate.dictUseky:  #ak sa výhybka nachádza v zozname
                    self.poslednaVyh = id   #zapíš ju ako poslednú kliknutú
                    if id in [12, 13]:  #úprava pre výhybkovú spojku
                        self.vlaknoUpdate.dictUseky[12].vyber = not self.vlaknoUpdate.dictUseky[12].vyber
                        self.vlaknoUpdate.dictUseky[13].vyber = not self.vlaknoUpdate.dictUseky[13].vyber
                        self.vlaknoUpdate.dictUseky[12].update(self)
                        self.vlaknoUpdate.dictUseky[13].update(self)
                    
                    else:
                        self.vlaknoUpdate.dictUseky[id].vyber = not self.vlaknoUpdate.dictUseky[id].vyber
                        self.vlaknoUpdate.dictUseky[id].update(self)

                    if self.vlaknoUpdate.dictUseky[id].vyber:  #je výhybka vybraná obsluhou?
                        self.ui.combo_vyh.show()  #ak áno zobraz kontextové okno akcií
                    
                    else:
                        self.ui.combo_vyh.hide()  #ak nie skry kontextové okno
                    
            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko vzdialenej obsluhy')

        elif objekt == 'TS':
            if not self.vla.dictStanice[2].dialkove:   #ak má precovisko aktívne riadenie 
                self.poslednyTS = id
                self.vla.dictTS[id].vybrane = not self.vla.dictTS[id].vybrane 

                if id == 2 and self.vla.dictTS[2].vybrane:
                    self.comboShowHide('TS_RAD')
                
                elif id == 3 and self.vla.dictTS[3].vybrane:
                    self.comboShowHide('TS_HLO')
                
                elif id == 4 and self.vla.dictTS[4].vybrane:
                    self.comboShowHide('TS_LUZ')
                
            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko vzdialenej obsluhy')

        elif objekt == 'stanica':
            self.poslednaStn = id
            self.update(id, True, 'Stanice')
            if self.vla.dictStanice[id].vyber:
                self.comboShowHide('stanica')
            
            else:
                self.comboShowHide()

    def comboShowHide(self, nazov:str=' '):   #metóda pre zobrazovanie výberových ponúk pre návestidlá
        if nazov == 'vchodove': #zobrazí menu pre vchodové návestidlo
            self.ui.combo_hlavne.show()
            self.ui.combo_fikt.hide()
            self.ui.combo_kombi.hide()
            self.ui.combo_zriad.hide() 
            self.ui.combo_oddielove.hide()   
        elif nazov == 'odchodove':  #zobrazí menu pre odchodové návestidlo
            self.ui.combo_kombi.show()
            self.ui.combo_fikt.hide()
            self.ui.combo_hlavne.hide()
            self.ui.combo_zriad.hide() 
            self.ui.combo_oddielove.hide()
        elif nazov == 'zriadovacie':    #zobrazí menu pre zriaďovacie návestidlo
            self.ui.combo_zriad.show() 
            self.ui.combo_fikt.hide()
            self.ui.combo_hlavne.hide()
            self.ui.combo_kombi.hide() 
            self.ui.combo_oddielove.hide()
        elif nazov == 'fiktivne':   #zobrazí menu pre fiktívne návestidlo
            self.ui.combo_fikt.show()
            self.ui.combo_hlavne.hide()
            self.ui.combo_kombi.hide()
            self.ui.combo_zriad.hide()  
            self.ui.combo_oddielove.hide()
        elif nazov == 'oddielove':   #zobrazí menu pre fiktívne návestidlo
            self.ui.combo_fikt.hide()
            self.ui.combo_hlavne.hide()
            self.ui.combo_kombi.hide()
            self.ui.combo_zriad.hide()
            self.ui.combo_oddielove.show()  

        elif nazov == 'odchodove_konc':    #zobrazí menu pre výber typu cesty pre odchodové návestidlo
            self.ui.combo_ciel_ko.show()
            self.ui.combo_ciel_fi.hide()   
            self.ui.combo_ciel_zr.hide()
        elif nazov == 'zriadovacie_konc':    #zobrazí menu pre výber typu cesty pre zriaďovacie návestidlo
            self.ui.combo_ciel_zr.show()
            self.ui.combo_ciel_fi.hide()   
            self.ui.combo_ciel_ko.hide()
        elif nazov == 'fiktivne_konc':    #zobrazí menu pre výber typu cesty pre fiktívne návestidlo
            self.ui.combo_ciel_fi.show()    
            self.ui.combo_ciel_ko.hide()
            self.ui.combo_ciel_zr.hide()

        elif nazov == 'vyhybka':    #zobrazí menu pre výhybku
            self.ui.combo_vyh.show()

        elif nazov == 'TS_RAD': #zobrazí menu pre traťový súhlas
            self.ui.combo_TS_HLO.hide()
            self.ui.combo_TS_RAD.show()
            self.ui.combo_TS_LUZ.hide()
        elif nazov == 'TS_HLO': #zobrazí menu pre traťový súhlas
            self.ui.combo_TS_HLO.show()
            self.ui.combo_TS_RAD.hide()
            self.ui.combo_TS_LUZ.hide()
        elif nazov == 'TS_LUZ': #zobrazí menu pre traťový súhlas
            self.ui.combo_TS_HLO.hide()
            self.ui.combo_TS_RAD.hide()
            self.ui.combo_TS_LUZ.show()

        elif nazov == 'stanica':    #zobrazí menu pre riadenie stanice
            self.ui.combo_Riadenie.show()

        else:   #skryje všetky menu
            self.ui.combo_fikt.hide()
            self.ui.combo_hlavne.hide()
            self.ui.combo_kombi.hide()
            self.ui.combo_zriad.hide() 
            self.ui.combo_oddielove.hide()   
            self.ui.combo_ciel_fi.hide()   
            self.ui.combo_ciel_ko.hide()
            self.ui.combo_ciel_zr.hide()
            self.ui.combo_vyh.hide()
            self.ui.combo_TS_HLO.hide()
            self.ui.combo_TS_RAD.hide()
            self.ui.combo_TS_LUZ.hide()
            self.ui.combo_Riadenie.hide()

    def akciaNavestidlo(self, index:int, typ:str):   #vyhodnotenie vybranej akcie z kontextového menu
        self.comboShowHide()    #po výbere skry menu

        #----------------------------výber typu vlakovej cesty------------------------------------------------------------------
        if ((typ in ['hlavne', 'kombi']) and index == 1):   #výber vlakovej cesty 
            if self.zoznamNav[self.posledneNav].znak != 'PN':
                self.vyberCestu('Vlak')
            
            else:
                self.vypisHlasenia('Nemožno stavať od aktívnej privolávecej návesti')

        elif (typ == 'kombi' and index == 2) or (typ == 'zriad' and index == 1):  #výber posunovej cesty
            if self.zoznamNav[self.posledneNav].nazov in ['Z_Se1','Z_Se2','Z_Se3','Z_S1','Z_S2','Z_L1','Z_L2']:
                if self.zoznamNav[self.posledneNav].znak != 'PN':
                    self.vyberCestu('Posun')
                
                else:
                    self.vypisHlasenia('Nemožno stavať od aktívnej privolávecej návesti')

            else:
                self.vypisHlasenia('Nie je možné postaviť posunovú cestu')

        #---------------------------stavanie jazdnej cesty------------------------------------------------------------------------
        elif typ in ['ciel_kombi','ciel_hlavne'] and index == 1 and self.szz.typCesty == 'Vlak': #stavanie vchodovej bez OD
            if self.zoznamNav[self.pociatocneNav].nazov in ['Z_L','Z_BL','Z_S']: #vybrané správne návestidlo   
                self.postavCestu()

        elif typ in ['ciel_kombi','ciel_hlavne'] and index == 2 and self.szz.typCesty == 'Vlak': #stavanie vchodovej cesty s OD
            if self.zoznamNav[self.pociatocneNav].nazov in ['Z_L','Z_BL','Z_S']: #vybrané správne návestidlo
                self.postavCestu(Ochr = True)

            else:
                self.vypisHlasenia('Jazdná cesta nemá definovanú ochrannú dráhu')
                self.ukonciStavanie()

        elif typ in ['ciel_kombi','ciel_fikt'] and index == 1 and self.szz.typCesty == 'Vlak': #stavanie odchodovej cesty
            if self.zoznamNav[self.pociatocneNav].nazov in ['Z_S1','Z_S2','Z_L1','Z_L2']: #kontrola počiatočného návestidla ZBE
                if self.zoznamNav[self.pociatocneNav].nazov in ['Z_S1'] and self.vlaknoUpdate.dictTS[2].prijem: #kontrola TS
                    self.postavCestu()
                    
                elif self.zoznamNav[self.pociatocneNav].nazov in ['Z_S2']:
                    if self.zoznamNav[self.posledneNav].nazov in ['Z_L_fik'] and self.vlaknoUpdate.dictTS[2].prijem:

                        self.postavCestu()

                    elif self.zoznamNav[self.posledneNav].nazov in ['Z_BL_fik'] and self.vlaknoUpdate.dictTS[4].prijem:
                        if self.vlaknoUpdate.dictTS[4].volnost:

                            self.postavCestu()
                        
                        else:
                            self.ukonciStavanie(volnost=True)

                elif self.zoznamNav[self.pociatocneNav].nazov in ['Z_L1', 'Z_L2']:
                    if self.vlaknoUpdate.odhlaskaLo:                    
                        if self.vlaknoUpdate.dictTS[3].prijem:
                            self.postavCestu()
                        
                        else:
                            self.ukonciStavanie(TS=True)
                    
                    else:
                        self.ukonciStavanie(odhl=True)

                else:
                    self.ukonciStavanie(TS=True)

            else:
                self.vypisHlasenia('Nesprávny výber')

        elif self.szz.typCesty == 'Posun':   #je vybraná posunová cesta pre stavanie
            if (typ == 'ciel_kombi' and index == 3) or (typ == 'ciel_zriad' and index == 1):    
                self.postavCestu()

        #---------------------------rušenie vlakovej cesty------------------------------------------------------------------------
        elif (typ == 'hlavne' and index == 3) or (typ == 'kombi' and index == 4) or (typ == 'zriad' and index == 2) or (typ == 'fikt' and index == 1):    #rušenie cesty
            self.koncoveNav = self.posledneNav
            self.posledneNav = 0

            if typ == 'fikt': #zrušenie predhlášky v prípade rušenia odchodovej cesty
                if self.zoznamNav[self.koncoveNav].nazov in ['Z_L_fik']:
                    self.prikazDoPLC(adresat='odchod/', nazov='odchodZR', prikaz='/False')

                elif self.zoznamNav[self.koncoveNav].nazov in ['Z_BL_fik']:
                    self.prikazDoPLC(adresat='odchod/', nazov='odchodZL', prikaz='/False')

                elif self.zoznamNav[self.koncoveNav].nazov in ['Z_S_fik']:
                    self.prikazDoPLC(adresat='odchod/', nazov='odchodZH', prikaz='/False')
                    self.prikazDoPLC(adresat='predhl/', prikaz='/False', nazov='ZBE')
                    self.zoznamNav[30].predhlaska = False  #zmazanie predhlášky na návestidle AH Lo
                                        
            self.zoznamNav[self.koncoveNav].vybrane = False
            self.zoznamNav[self.koncoveNav].update(self)
            self.szz.rusenieCesty(Disp=True)

        #---------------------------aktivácia privolávacej návesti------------------------------------------------------------------------         
        elif (typ == 'hlavne' and index == 2) or (typ == 'kombi' and index == 3) or (typ == 'oddiel' and index == 1):
            if self.zoznamNav[self.posledneNav].nazov not in ['R_k1_fik','R_k2_fik','DR_k1_fik','DR_k2_fik',
                                                          'H_k1_fik','H_k2_fik','DH_k1_fik','DH_k2_fik']: #kontrola správneho návestidla    
                self.zoznamNav[self.posledneNav].vybrane = False
                
                if self.zoznamNav[self.posledneNav].znak == 'Stoj' and self.zoznamNav[self.posledneNav].znak != 'PN': #rozsvietenie privolávacej návesti
                    self.zmenaNavZnaku(navest = 'PN')

                elif self.zoznamNav[self.posledneNav].znak == 'PN': #zhasnutie privolávacej návesti
                    self.zmenaNavZnaku(navest = 'Stoj')
                                
                elif self.zoznamNav[self.posledneNav].znak != 'Stoj' and self.zoznamNav[self.posledneNav].znak != 'PN':
                    self.vypisHlasenia('Nie je možné rozsvietiť privolávaciu návesť')

            else:
                self.vypisHlasenia('Nesprávny výber návestidla')

        #---------------------------manuálne rozsvietenie Stoj------------------------------------------------------------------------
        elif (typ == 'hlavne' and index == 5) or (typ == 'kombi' and index == 6) or (typ == 'zriad' and index == 4) or (typ == 'oddiel' and index == 3):
            if self.zoznamNav[self.posledneNav].nazov not in ['R_k1_fik','R_k2_fik','DR_k1_fik','DR_k2_fik',
                                                              'H_k1_fik','H_k2_fik','DH_k1_fik','DH_k2_fik']: 
                self.zoznamNav[self.posledneNav].vybrane = False

                if (self.zoznamNav[self.posledneNav].pociatocne) or ( #iba ak je návestidlo počiatočným návestidlom jazdnej cesty
                self.zoznamNav[self.posledneNav].TZZ == 'AH' and self.zoznamNav[self.posledneNav].predhlaska):  #alebo návestidlo AH s prijatou predhláškou 
                    self.zoznamNav[self.posledneNav].manual = True
                    self.zmenaNavZnaku(navest = 'Stoj')

                else:
                    self.vypisHlasenia('Nesprávne zadanie STOJ na návestidle')

        #---------------------------manuálne rozsvietenie Voľno------------------------------------------------------------------------
        elif (typ == 'hlavne' and index == 4) or (typ == 'kombi' and index == 5) or (typ == 'zriad' and index == 3) or (typ == 'oddiel' and index == 2):
            if  self.zoznamNav[self.posledneNav].nazov not in ['R_k1_fik','R_k2_fik','DR_k1_fik','DR_k2_fik',
                                                              'H_k1_fik','H_k2_fik','DH_k1_fik','DH_k2_fik']:                                           
                if self.zoznamNav[self.posledneNav].znak != 'PN':
                    self.zoznamNav[self.posledneNav].vybrane = False

                    if (self.zoznamNav[self.posledneNav].pociatocne) or (   #iba ak je návestidlo počiatočným návestidlom jazdnej cesty
                        self.zoznamNav[self.posledneNav].TZZ == 'AH' and self.zoznamNav[self.posledneNav].predhlaska):   #alebo návestidlo AH s prijatou predhláškou 
                        self.zoznamNav[self.posledneNav].manual = True
                    
                        if (typ in ['hlavne','oddiel']) or (typ == 'kombi' and not self.zoznamNav[self.posledneNav].typAktCes):
                            self.zmenaNavZnaku(navest = 'Vlak')

                        elif (typ == 'zriad') or (typ == 'kombi' and self.zoznamNav[self.posledneNav].typAktCes):
                            self.zmenaNavZnaku(navest = 'Posun')

                    else:
                        self.vypisHlasenia('Nesprávne zadanie VOĽNO na návestidle')

                else:
                    self.vypisHlasenia('Návestidlo má aktívnu privoláviacu návesť')
        
        else:
            if self.posledneNav != 0:
                self.zoznamNav[self.posledneNav].vybrane = False
                self.zoznamNav[self.posledneNav].update(self)

            if self.koncoveNav != 0:
                self.zoznamNav[self.koncoveNav].vybrane = False
                self.zoznamNav[self.koncoveNav].update(self)

        self.ui.combo_hlavne.setCurrentIndex(0) #resetuj index vybranej akcie z kontextového menu
        self.ui.combo_kombi.setCurrentIndex(0)
        self.ui.combo_zriad.setCurrentIndex(0)
        self.ui.combo_fikt.setCurrentIndex(0) 
        self.ui.combo_oddielove.setCurrentIndex(0)   

        self.ui.combo_ciel_zr.setCurrentIndex(0)
        self.ui.combo_ciel_ko.setCurrentIndex(0)
        self.ui.combo_ciel_fi.setCurrentIndex(0)

    def zmenaNavZnaku(self, navest:str=' '):    #zmena návestného znaku na návestidle
        self.zoznamNav[self.posledneNav].znak = navest
        prikaz = '/' + navest
        self.prikazDoPLC(adresat='navestidlo', prikaz=prikaz, id=self.zoznamNav[self.posledneNav].typ, nazov=self.zoznamNav[self.posledneNav].nazov)  
        self.prikazDoPLC(adresat='navestidlo', prikaz=prikaz, znak=True)
        self.zoznamNav[self.posledneNav].update(self)
    
        if self.zoznamNav[self.posledneNav].zavisle != -1:  #úprava pre dispečerskú alikáciu
                        self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].znak = navest
                        self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].update(self)

    def akciaTS(self, index:int, typ:str):   #metóda pre prácu s traťovým súhlasom
        if (index == 1) and (typ == 'disp'):
            if self.vlaknoUpdate.dictTS[typ].prijem is True: 
                self.prikazDoPLC(adresat='TS', prikaz='UTS/' + str(self.poslednyTS))
        
        self.comboShowHide()
        self.ui.combo_TS_HLO.setCurrentIndex(0)

        if (index == 1) and (typ == 'esa'):   #žiadosť o TS
            if not self.vlaknoUpdate.dictTS[typ].prijem:    #kontrola udelenia TS
                if self.vlaknoUpdate.dictTS[typ].volnost:   #kontrola voľnosti úseku
                    self.prikazDoPLC(adresat='TS', prikaz='ZUS/' + str(self.poslednyTS) + '/True')

                else:
                    self.vypisHlasenia('Obsadený medzistaničný úsek')

            else:
                self.vypisHlasenia('Traťový súhlas je prijatý')

        elif (index == 2) and (typ == 'esa'):   #zrušenie žiadosti o TS
            self.prikazDoPLC(adresat='TS', prikaz='ZUS/' + str(self.poslednyTS) + '/False')      
            self.ziadostAktivna = False

        elif (index == 1 and typ == 'disp') or (index == 3 and typ =='esa'):  #udelenie TS
            if self.vlaknoUpdate.dictTS[self.poslednyTS].prijem is True:   #kontrola príjmu TS
                self.prikazDoPLC(adresat='TS', prikaz='UTS/' + str(self.poslednyTS))

        elif (index == 4) and (typ == 'esa'):    #zrušenie blokovej podmienky
            self.prikazDoPLC(adresat='TS', prikaz='ZBP/' + str(self.poslednyTS))

        elif index != 0:
            self.vypisHlasenia('Neudelený traťový súhlas')

        self.comboShowHide()
        self.ui.combo_TS_RAD.setCurrentIndex(0)
        self.ui.combo_TS_HLO.setCurrentIndex(0)
        self.ui.combo_TS_LUZ.setCurrentIndex(0)  

    def akciaStanica(self, index:int):  #metóda pre spracovanie signálov riadenia
        if index == 1: #žiadosť o prevzatie riadenia
            if self.vlaknoUpdate.dictStanice[self.poslednaStn].dialkove:
                if self.vlaknoUpdate.dictStanice[self.poslednaStn].ziadost: #ak už je aktívna žiadosť
                    self.prikazDoPLC(adresat='ziadRiad/', prikaz='/True', nazov=self.vlaknoUpdate.dictStanice[self.poslednaStn].nazovGUI)    #zruš ju

                else:   #ak nie je žiadosť aktívna
                    self.prikazDoPLC(adresat='ziadRiad/', prikaz='/True', nazov=self.vlaknoUpdate.dictStanice[self.poslednaStn].nazovGUI) #aktivuj ju

            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko lokálnej obsluhy')
        
        elif index == 2: #potvrdenie žiadosti o prevzatie riadenia
            if self.vlaknoUpdate.dictStanice[self.poslednaStn].ziadost:
                self.prikazDoPLC(adresat='udelRiad/', prikaz='/False', nazov=self.vlaknoUpdate.dictStanice[self.poslednaStn].nazovGUI)   

            else:
                self.vypisHlasenia('Žiadosť nebola prijatá')       

        self.comboShowHide()
        widget.ui.combo_Riadenie.setCurrentIndex(0)

    def vyberCestu(self, typ:str):  #metóda pre zápis potrebných hodnôt pre výber jazdnej cesty
        self.szz.typCesty = typ #zapíše správny typ cesty
        self.szz.vyberCesty = True #definuje aktívny výber vlakovej cesty
        self.pociatocneNav = self.posledneNav   #vybrané návestidlo označí za počiatočné

        self.zoznamNav[self.pociatocneNav].stavanieOd = True
        self.zoznamNav[self.pociatocneNav].typAktCes = self.szz.typCesty #zapíše počiatočnému návestidlu typ cesty
        self.zoznamNav[self.pociatocneNav].vybrane = False
        self.zoznamNav[self.pociatocneNav].update(self)

    def postavCestu(self, Ochr:bool=False):  #metóda, ktorá vydá príkaz pre postavenie vybranej cesty algoritmom SZZ
        self.szz.vyberCesty = False
        self.koncoveNav = self.posledneNav
        self.posledneNav = 0

        self.zoznamNav[self.koncoveNav].vybrane = False
        self.zoznamNav[self.koncoveNav].update(self)

        self.szz.stavanieCesty(OD = Ochr, Disp = True)

    def ukonciStavanie(self, TS:bool=False, odhl:bool=False, volnost:bool=False):   #metóda slúži na ukončenie stavania VC v prípade zlého TS alebo obsadeného medzist. úseku
        self.zoznamNav[self.pociatocneNav].stavanieOd = False
        self.zoznamNav[self.pociatocneNav].update(self)
        self.szz.vyberCesty = False
        self.pociatocneNav = 0
        self.koncoveNav = 0

        if odhl:
            self.vypisHlasenia('Chýbajúca odhláška za vlakom')
        
        elif TS:
            self.vypisHlasenia('Neudelený traťový súhlas')
        
        elif volnost:
            self.vypisHlasenia('Obsadený medzistaničný úsek')

    def prikazDoPLC(self, prikaz:str=' ', id:int=0, nazov:str=' ', adresat:str=' ', auto:bool=False):  #metóda pre odosielanie dát do PLC
        adresa = self.citajAdresu()
        if adresat == 'cas':    #odosielanie času do aplikácie
            URL = adresa + 'CasP/disp'
        
        elif adresat == 'navestidlo':   #pzmena návestného znaku
            URL = 'write/navestidlo/'
            if id in range(1,11) or id in range(46,55):
                URL = URL + 'RAD/'
            
            elif id in range(12,34) or id in range(56,68):
                URL = URL + 'ZBE/'
            
            elif id in range(35,45) or id in range(69,77):
                URL = URL + 'HLO/'
        
            URL = adresa + URL + nazov + prikaz
        
        elif adresat == 'cesta': #prenos info o stavaní / rušení jazdnej cesty medzi plikáciami ILTIS-N
            if self.pociatocneNav > 45:
                start = self.zoznamNav[self.pociatocneNav].zavisle
            
            else:
                start = self.pociatocneNav

            if self.koncoveNav > 45:
                end = self.zoznamNav[self.koncoveNav].zavisle
            
            else:
                end = self.koncoveNav

            if nazov == 'stavanie':
                if prikaz == 'True':
                    URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/' + self.szz.typCesty + '/True/True/False/DISP'

                else:
                    URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/' + self.szz.typCesty + '/False/True/False/DISP'

            elif nazov == 'rusenie':
                URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/X/False/False/True/DISP'
                
            else:
                URL = adresa + 'Cesta/0/0/False/False/False/False/DISP'
        
        elif adresat == 'znak':  #prenos návestného znaku medzi plikáciami ILTIS-N
            if self.posledneNav > 45:
                nav = self.zoznamNav[self.posledneNav].zavisle
            else:
                nav = self.posledneNav

            if prikaz != '_':
                URL = adresa + 'Navest/' + str(nav) + prikaz + '/DISP'

            else:
                URL = adresa + 'Navest/0/Stoj/DISP'

        elif adresat == 'vymena': #prestavenie výhybky
            URL = adresa + 'write/vyhybka/' + nazov + prikaz + auto           
        
        elif adresat == 'TS':   #Traťový súhlas
            URL = adresa + prikaz

        elif adresat in ['write/OchrDr/', 'odchod/', 'predhl/', 'ziadRiad/', 'write/priecestie/']:   #odosielanie info o ochrannej dráhe, odchodových cestách, predhláškach a diaľkovom riadení
            URL = adresa + adresat + nazov + prikaz
        
        requests.put(URL)
        
    def vypisHlasenia(self, hlasenie):  #metóda pre výpis varovného hlásenia pri zlej obsluhe
        cas = arrow.now().format('HH:mm:ss')
        self.ui.textHlasenia.append(hlasenie + ' - ' + cas)

    def quit(self): #metóda pre zatvorenie aplikácie
        self.ukonciPripojenie()
        app.quit()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = App()
    widget.show()
    widget.showFullScreen()

    ico.create()    #zavolá metódu pre tvorbu všetkých potrebných ikon

    widget.ui.combo_hlavne.hide()   #po spustení skryje kontextové menu prvkov
    widget.ui.combo_kombi.hide()
    widget.ui.combo_zriad.hide()
    widget.ui.combo_fikt.hide()
    widget.ui.combo_oddielove.hide()
    widget.ui.combo_ciel_ko.hide()
    widget.ui.combo_ciel_zr.hide()
    widget.ui.combo_ciel_fi.hide()
    widget.ui.combo_vyh.hide()
    widget.ui.combo_TS_HLO.hide()
    widget.ui.combo_TS_RAD.hide()
    widget.ui.combo_TS_LUZ.hide()
    widget.ui.combo_Riadenie.hide()

    widget.ui.groupREST.setVisible(False)
    widget.ui.groupPrehlad.setVisible(False)

    #prepojenia s metódou vyhodnotenia akcie z kontextového menu
    widget.ui.combo_hlavne.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_hlavne.currentIndex(), 1))    #počiatok jazdnej cesty  
    widget.ui.combo_kombi.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_kombi.currentIndex(), 2))
    widget.ui.combo_zriad.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_zriad.currentIndex(), 3))
    widget.ui.combo_fikt.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_fikt.currentIndex(), 4))
    widget.ui.combo_oddielove.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_oddielove.currentIndex(), 5))
    
    widget.ui.combo_ciel_ko.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_ciel_ko.currentIndex(), 10)) #koniec jazdnej cesty 
    widget.ui.combo_ciel_zr.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_ciel_zr.currentIndex(), 11))
    widget.ui.combo_ciel_fi.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_ciel_fi.currentIndex(), 12))

    widget.ui.combo_TS_RAD.currentIndexChanged.connect(lambda: widget.akciaTS(widget.ui.combo_TS_RAD.currentIndex(), 2))    #traťový súhlas
    widget.ui.combo_TS_HLO.currentIndexChanged.connect(lambda: widget.akciaTS(widget.ui.combo_TS_HLO.currentIndex(), 3))
    widget.ui.combo_TS_LUZ.currentIndexChanged.connect(lambda: widget.akciaTS(widget.ui.combo_TS_LUZ.currentIndex(), 4))
  
    widget.ui.combo_Riadenie.currentIndexChanged.connect(lambda: widget.akciaStanica(widget.ui.combo_Riadenie.currentIndex()))   #riadenie stanice

    widget.ui.combo_vyh.currentIndexChanged.connect(lambda: widget.szz.prestavenieVyh(widget.poslednaVyh, widget.ui.combo_vyh.currentIndex()))    #prestavenie výmeny    

    widget.ui.actionVlastnosti.triggered.connect(lambda: widget.popUp(okno='REST'))   #práca s oknom REST API
    widget.ui.ButtonClose.clicked.connect(lambda: widget.popUp(okno='REST'))

    widget.ui.actionInfo.triggered.connect(lambda: widget.popUp(okno='Prehlad'))
    widget.ui.ButtonClose_1.clicked.connect(lambda: widget.popUp(okno='Prehlad'))

    widget.ui.actionZavrie.triggered.connect(lambda: widget.quit()) #terminácia aplikácie

    #prepojenia s metódou na zobrazenie kontextového menu pre zvolený element
    #---------------NÁVESTIDLÁ-------------------------------------------   
    widget.ui.ZBE_L.clicked.connect(lambda: widget.clickObjekt(12, 'navestidlo')) 
    widget.ui.ZBE_BL.clicked.connect(lambda: widget.clickObjekt(13, 'navestidlo'))
    widget.ui.ZBE_fik_L.clicked.connect(lambda: widget.clickObjekt(14, 'navestidlo'))
    widget.ui.ZBE_fik_BL.clicked.connect(lambda: widget.clickObjekt(15, 'navestidlo'))
    widget.ui.ZBE_zr_zo_st_odR.clicked.connect(lambda: widget.clickObjekt(16, 'navestidlo'))    
    widget.ui.ZBE_zr_zo_st_odL.clicked.connect(lambda: widget.clickObjekt(17, 'navestidlo'))
    widget.ui.ZBE_zr_do_st_odR.clicked.connect(lambda: widget.clickObjekt(18, 'navestidlo'))
    widget.ui.ZBE_zr_do_st_odL.clicked.connect(lambda: widget.clickObjekt(19, 'navestidlo'))
    widget.ui.ZBE_S1.clicked.connect(lambda: widget.clickObjekt(20, 'navestidlo'))
    widget.ui.ZBE_S2.clicked.connect(lambda: widget.clickObjekt(21, 'navestidlo'))
    widget.ui.ZBE_L1.clicked.connect(lambda: widget.clickObjekt(22, 'navestidlo'))
    widget.ui.ZBE_L2.clicked.connect(lambda: widget.clickObjekt(23, 'navestidlo'))
    widget.ui.ZBE_zr_do_st_odH.clicked.connect(lambda: widget.clickObjekt(24, 'navestidlo'))
    widget.ui.ZBE_zr_zo_st_odH.clicked.connect(lambda: widget.clickObjekt(25, 'navestidlo'))
    widget.ui.ZBE_fik_S.clicked.connect(lambda: widget.clickObjekt(26, 'navestidlo'))
    widget.ui.ZBE_S.clicked.connect(lambda: widget.clickObjekt(27, 'navestidlo'))
    widget.ui.ZBE_HLO_So.clicked.connect(lambda: widget.clickObjekt(31, 'navestidlo'))
    #--------------------------------------------------------------------
    #-------------VÝHYBKY------------------------------------------------
    widget.ui.ZBE_V1.clicked.connect(lambda: widget.clickObjekt(12,'vyhybka'))
    widget.ui.ZBE_V2.clicked.connect(lambda: widget.clickObjekt(13,'vyhybka'))
    widget.ui.ZBE_V3.clicked.connect(lambda: widget.clickObjekt(16,'vyhybka'))
    #--------------------------------------------------------------------
    #-------------TRAŤOVÝ SÚHLAS-----------------------------------------
    widget.ui.ZBE_trat_suhlas_doR.clicked.connect(lambda: widget.clickObjekt(2, 'TS'))
    widget.ui.ZBE_trat_suhlas_doH.clicked.connect(lambda: widget.clickObjekt(3, 'TS'))
    widget.ui.ZBE_trat_suhlas_doL.clicked.connect(lambda: widget.clickObjekt(4, 'TS'))
    #--------------------------------------------------------------------
    #-------------RIADENIE STANICE---------------------------------------   
    widget.ui.ZBE_dialkove.clicked.connect(lambda: widget.clickObjekt(2, 'stanica'))

    widget.ui.ButtonConnect.clicked.connect(lambda: widget.zahajPripojenie())  #prepojenie s metódou pre testovanie spojenia s PLC
    widget.ui.ButtonDisconnect.clicked.connect(lambda: widget.ukonciPripojenie())  #vyvolá ukončenie komunikácie

    app.exec()