from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, Signal, QTimer
import sys
import requests
from time import sleep
import arrow

from ui_form import Ui_ILTIS
import ico
from vyhybka import Vyhybka
from navestidlo import Navestidlo
from usek import Usek
from SZZ import SZZ
from tratSuhlas import TratSuhlas
from priecestie import Priecestie
from riadenieObsluhy import RiadenieObsluhy

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or

class dataUpdate(QThread):
    dataUpdated = Signal(dict, dict)

    def __init__(self, app_instance):
        self.dictUseky ={   #slovník úsekov
            1: Usek(ID=0, nazovGUI='RAD_k1', enummIkon=ico.KolajSt1, dictIkon=ico.dictStanKolaj1, app=app_instance),
            2: Usek(ID=1, nazovGUI='RAD_k2', enummIkon=ico.KolajSt2, dictIkon=ico.dictStanKolaj2, app=app_instance),
            3: Vyhybka(ID=2, IDsmer=0, nazovGUI='RAD_V1', usek='RAD_v1' , enumIkon=ico.VyhP, dictIkon=ico.dictVyhP, app=app_instance),
            4: Usek(ID=3, nazovGUI='RAD_Sk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            5: Usek(ID=4, nazovGUI='RAD_ZBE_TU1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            6: Usek(ID=5, nazovGUI='RAD_ZBE_TU2_1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            7: Usek(ID=5, nazovGUI='RAD_ZBE_TU2_2', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance)
        }

        self.dictTS = { #slovník traťových súhlasov
            1: TratSuhlas(ID=1, nazovGUI='RAD_trat_suhlas_doZ', enumIkon=ico.TrSP, dictIkon=ico.dictTrSP, app=app_instance, typ='L'),
        }

        self.dictPriecestie = { #slovník priecestí
            1:Priecestie(ID=1, nazovGUI='RAD_ZBE_priec', enumIkon=ico.Priecestie, dictIkon=ico.dictPriecestie, app=app_instance)
        } 

        self.dictStanice = {    #slovník stníc
            1:RiadenieObsluhy(ID=1, nazovGUI='RAD_dialkove', enumIkon=ico.RiadenieRAD, dictIkon=ico.dictRiadenieRAD, app=app_instance),
        }

        super().__init__()
        self.app_instance = app_instance

    def run(self):  #základ vlákna
        while not self.isInterruptionRequested(): 
            
            adresa = self.app_instance.citajAdresu()
            URL = adresa + 'read'
            response = requests.get(URL)    #dopyt do PLC
            data = response.json()
            
            if data is not None:
                for index in self.dictUseky.keys():  #čítanie stavov koľajových úsekov
                    self.dictUseky[index].jeVolny = data['RAD;RAD-ZBE'][self.dictUseky[index].ID]

                for i in [3]:   #čítanie smeru výmen
                    self.dictUseky[i].smer = data['SmerVyh'][self.dictUseky[i].IDsmer]

                #čítanie stavov traťových súhlasov
                self.dictTS[1].smer = data['TS']['smerRZ'] 
                self.dictTS[1].ziadost = data['TS']['ZUS_RZ']                   
                self.dictTS[1].volnost = data['TS']['volRZ'] 
                MyOdchod = data['TS']['odchodR']
                SusOdchod = data['TS']['odchodZR']
                self.dictTS[1].odchod = (MyOdchod or SusOdchod)

                #čítanie stavov priecestí
                self.dictPriecestie[1].predzvananie = data['Priecestie'][4]
                self.dictPriecestie[1].otvorene = data['Priecestie'][2]
                self.dictPriecestie[1].zatvorene = data['Priecestie'][3]
                self.dictPriecestie[1].jeVolny = self.dictUseky[6].jeVolny

                #čítanie stavov riadenia staníc
                self.dictStanice[1].dialkove = data['Riadenie']['dialkoveRAD']
                self.dictStanice[1].ziadost = data['Riadenie']['ziadostRAD']
               
                if data['Cesta']['stavanie']:
                    if (data['Cesta']['pociatocne'] in self.app_instance.dictNav.keys() and data['Cesta']['koncove'] in self.app_instance.dictNav.keys()) and (
                    data['Cesta']['odosielatel'] != 'RAD'):
                        self.app_instance.Start = data['Cesta']['pociatocne']
                        self.app_instance.dictNav[self.app_instance.Start].pociatocne = True
                        self.app_instance.End = data['Cesta']['koncove']
                        self.app_instance.szz.typCesty = data['Cesta']['typCesty']
                        self.app_instance.szz.stavanieCesty(server=True)
                        self.app_instance.prikazDoPLC(cesta=True)
                
                if data['Cesta']['rusenie']:
                    if data['Cesta']['koncove'] in self.app_instance.dictNav.keys() and data['Cesta']['odosielatel'] != 'RAD':
                        self.app_instance.End = data['Cesta']['koncove']
                        self.app_instance.szz.rusenieCesty(server=True)
                        self.app_instance.prikazDoPLC(cesta=True)

                if data['Navest']['ID'] != 0 and data['Navest']['ID'] in self.app_instance.dictNav.keys() and data['Navest']['odosielatel'] != 'HLO':
                    self.app_instance.dictNav[data['Navest']['ID']].znak = data['Navest']['znak']
                    self.app_instance.dictNav[data['Navest']['ID']].update(self)
                    self.app_instance.prikazDoPLC(znak=True)

                self.dataUpdated.emit(self.dictUseky, self.dictTS)
            
            sleep(0.33)

class DlhyCasVlak(QThread): #dlhý časový súbor pre vlakovú cestu
    finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        while not self.isInterruptionRequested():
            self.sleep(1)   #nenkonečná slučka vlákna

    def start_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.stop_timer)
        self.timer.start(180000) #3 minúty

    def stop_timer(self):
        self.timer.stop()
        self.finished.emit()

class DlhyCasPosun(QThread): #dlhý časový súbor pre posunovú cestu
    finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        while not self.isInterruptionRequested():
            self.sleep(1)   #nenkonečná slučka vlákna

    def start_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.stop_timer)
        self.timer.start(60000) #1 minúta

    def stop_timer(self):
        self.timer.stop()
        self.finished.emit()

class CasOchrDr(QThread): #časový súbor pre ochrannú dráhu
    finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        while not self.isInterruptionRequested():
            self.sleep(1)   #nenkonečná slučka vlákna

    def start_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.stop_timer)
        self.timer.start(30000) #30 sekúnd
    def stop_timer(self):
        self.timer.stop()
        self.finished.emit()

class DateTime(QThread): #Čas a dátum pre aplikáciu
    dataUpdated = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while not self.isInterruptionRequested():
            cas = arrow.now().format('  DD.MM.YY HH:mm:ss')
            self.sleep(1)   #1 sekunda
            self.dataUpdated.emit(cas)

class App(QMainWindow): #hlavná triedy vizualizácie 
    def __init__(self, parent=None):
        self.lastNav = 0  #posledné kliknuté návestidlo
        self.Start = 0    #počiatočné návestidlo jazdnej cesty
        self.End = 0    #koncové návestidlo jazdnej cesty
        self.lastVyh = 'X'  #posledná kliknutá výhybka   
        self.lastPri = 'X'  #posledné kliknuté priecestie
        self.lastStanica = 'X' #posledná kliknutá stanica
        self.lastTS = 'X'   #posledný kliknutý traťový súhlas
        self.secondLastTS = 'X' #predposledný kliknutý traťový súhlas

        self.dictNav = {    #slovník návestidiel
            1: Navestidlo(ID=1, nazov='R_Se1', usekPred='RAD_Sk', usekZa='RAD_V1', nazovGUI='RAD_zr_do_st_odZ', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL, app=self),
            2: Navestidlo(ID=2, nazov='R_Se1p', usekPred='RAD_Sk', nazovGUI='RAD_zr_zo_st_odZ', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=self),
            3: Navestidlo(ID=3, nazov='R_S', usekPred='RAD_ZBE_TU1', usekZa='RAD_Sk', nazovGUI='RAD_S', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self),
            4: Navestidlo(ID=4, nazov='R_L1', usekPred='RAD_k1', usekZa='RAD_V1', nazovGUI='RAD_L1', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, app=self),
            5: Navestidlo(ID=5, nazov='R_L2', usekPred='RAD_k2', usekZa='RAD_V1', nazovGUI='RAD_L2', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, app=self),
            6: Navestidlo(ID=6, nazov='R_S_fik', usekPred='RAD_Sk', nazovGUI='RAD_fik_S', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, app=self),
            7: Navestidlo(ID=7, nazov='R_29_fik', usekPred='RAD_ZBE_TU2_2', nazovGUI='RAD_fik_29', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, app=self),
            8: Navestidlo(ID=8, nazov='R_19', usekPred='RAD_ZBE_TU1', usekZa='RAD_ZBE_TU2_1', nazovGUI='RAD_ZBE_19', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self, oddielove=True, TZZ='AB3'),
            9: Navestidlo(ID=9, nazov='R_18', usekPred='RAD_ZBE_TU2_1', usekZa='RAD_ZBE_TU1', nazovGUI='RAD_ZBE_18', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self, oddielove=True, TZZ='AB3'),
            10: Navestidlo(ID=10, nazov='R_k1_fik', usekPred='RAD_k1', nazovGUI='RAD_1k_fik', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, app=self),
            11: Navestidlo(ID=11, nazov='R_k2_fik', usekPred='RAD_k2', nazovGUI='RAD_2k_fik', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, app=self)
            }      

        super().__init__(parent)
        self.ui = Ui_ILTIS()    #vytvorenie spojenia s triedami
        self.szz = SZZ(self)   

        self.ui.setupUi(self)

        self.workerThread = dataUpdate(self)   #prepojenie bočných vláken s hlavným vláknom
        self.workerThreadTimeVlak = DlhyCasVlak()
        self.workerThreadTimePosun = DlhyCasPosun()
        self.workerThreadTimeOD = CasOchrDr()
        self.workerThreadDateTime = DateTime()
        self.workerThreadDateTime.start()

        self.workerThread.dataUpdated.connect(self.update)    #definícia prepojenia vláken a metód
        self.workerThread.dataUpdated.connect(lambda: self.szz.stavanieCesty(True))
        
        self.workerThreadDateTime.dataUpdated.connect(self.aktualizaciaCasu)

        self.workerThreadTimeVlak.finished.connect(lambda: self.szz.rusenieCesty(True))
        self.workerThreadTimePosun.finished.connect(lambda: self.szz.rusenieCesty(True))        
        self.workerThreadTimeOD.finished.connect(lambda: self.szz.rusenieOD())

        self.workerThread.setParent(self)  #definovanie rosičovského objektu pre vlákna

        self.dictNav[9].zhasnute = True

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

            self.workerThread.start()    #po úspešnom spojení sa spúšťa beh vláken
            self.workerThreadTimeVlak.start()
            self.workerThreadTimePosun.start()
            self.workerThreadTimeOD.start()

            self.ui.RAD_ASVC.setIcon(ico.icon_ASVC_vypnute)

    def ukonciPripojenie(self):  #metóda pre zastavenie vláken a ukončenie komunikácie
        self.workerThread.requestInterruption()   
        self.workerThreadTimeVlak.requestInterruption()
        self.workerThreadTimePosun.requestInterruption()
        self.workerThreadTimeOD.requestInterruption() 
        self.workerThreadDateTime.requestInterruption() 

        self.ui.textChybaREST.show()     

    def aktualizaciaCasu(self, cas): #metóda pre aktualizáciu času v GUI
        self.ui.DateTime.setText(cas)

    def update(self, ID=-1, clicked=False, objekt='update'):    #metóda pre aktualizáciu symbolov objektov
        if objekt in ['update', 'useky']:   #aktualizácia úsekov
            for i in self.workerThread.dictUseky.keys():
                self.workerThread.dictUseky[i].update(self)

        if objekt in ['update', 'navestidla']:  #aktualizácia návestidiel
            self.dictNav[8].zhasnute =  self.workerThread.dictTS[1].smer  #otáčanie svietenia AB podľa TS
            self.dictNav[9].zhasnute =  not self.workerThread.dictTS[1].smer

            if clicked and ID in self.dictNav:  #ak bolo návestidlo kliknuté obsluhou
                self.dictNav[ID].vybrane = not self.dictNav[ID].vybrane 
                for i in self.dictNav.keys():
                    if i != ID:
                        self.dictNav[i].vybrane = False               

            for ID in self.dictNav.keys():  #vyberaj z návestidiel
                for i in self.workerThread.dictUseky.keys():   #vyberaj z úsekov
                    if self.dictNav[ID].usekPred == self.workerThread.dictUseky[i].nazovGUI:   #ak sa nájde úsek previazaný s návestidlom
                        self.dictNav[ID].jeVolnyPred = self.workerThread.dictUseky[i].jeVolny  #aktualizuj symbol návestidla podľa obsadenia úseku
                    
                    if self.dictNav[ID].usekPred == self.workerThread.dictUseky[i].nazovGUI:   #ak sa nájde úsek previazaný s návestidlom
                        self.dictNav[ID].usekOdozva = self.workerThread.dictUseky[i].odozva  #aktualizuj symbol návestidla podľa LIfeSign úseku

                    if self.dictNav[ID].usekZa == self.workerThread.dictUseky[i].nazovGUI:   #ak sa nájde úsek previazaný s návestidlom
                        self.dictNav[ID].jeVolnyZa = self.workerThread.dictUseky[i].jeVolny  #aktualizuj symbol návestidla podľa obsadenia úseku

                self.dictNav[ID].update(self)

        if objekt in ['update', 'priecestie']:  #aktualizácia priecestí
            if clicked and ID in self.workerThread.dictPriecestie:  
                self.workerThread.dictPriecestie[ID].vyber = not self.workerThread.dictPriecestie[ID].vyber
                for i in self.workerThread.dictPriecestie.keys():
                    if i != ID:
                        self.workerThread.dictPriecestie[i].vyber = False

            for i in self.workerThread.dictPriecestie.keys():
                self.workerThread.dictPriecestie[i].update(self)  

        if objekt in ['update', 'TS']:  #aktualizácia traťového súhlasu
            for i in self.workerThread.dictTS.keys():
                self.workerThread.dictTS[i].update(self)
                self.ziadostAktivna = self.workerThread.dictTS[i].ziadost

        if objekt in ['update', 'Stanice']: #aktualizácia raidenia stanice
            if clicked and ID in self.workerThread.dictStanice:  
                self.workerThread.dictStanice[ID].vyber = not self.workerThread.dictStanice[ID].vyber
            for i in self.workerThread.dictStanice.keys():
                self.workerThread.dictStanice[i].update(self)

    def clickObjekt(self, id, objekt):  #metóda spracovávajúca kliknutie na objekt
        if objekt == 'navestidlo':
            self.lastNav = id   #zápis posledného kliknutého návestidla                
            
            if not self.workerThread.dictStanice[1].dialkove:   #ak má precovisko aktívne riadenie 
                self.update(id, True, 'navestidla')
                if id in [3]: #vchodové návestidlo
                    if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('vchodove')
                    
                    elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('vchodove_konc')
                    
                    else:
                        self.comboShowHide()

                elif id in [4, 5, 10, 11]:    #odchodové návestidlo
                    if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('odchodove')
                    
                    elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('odchodove_konc')
                    
                    else:
                        self.comboShowHide()

                elif id in [1, 2]:  #zriaďovacie návestidlo
                    if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('zriadovacie')
                    
                    elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('zriadovacie_konc')
                    
                    else:
                        self.comboShowHide()

                elif id in [6]:   #fiktívne návestidlo
                    if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('fiktivne')
                    
                    elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('fiktivne_konc')
                    
                    else:
                        self.comboShowHide()

            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko vzdialenej obsluhy')

        elif objekt == 'vyhybka':
            if not self.workerThread.dictStanice[1].dialkove:   #ak má precovisko aktívne riadenie 
                if id in self.workerThread.dictUseky:  #ak sa výhybka nachádza v zozname
                    self.lastVyh = id   #zapíš ju ako poslednú kliknutú
                    self.workerThread.dictUseky[id].vyber = not self.workerThread.dictUseky[id].vyber
                    self.workerThread.dictUseky[id].update(self)

                    if self.workerThread.dictUseky[id].vyber:  #je výhybka vybraná obsluhou?
                        self.ui.combo_vyh.show()  #ak áno zobraz kontextové okno akcií
                    
                    else:
                        self.ui.combo_vyh.hide()  #ak nie skry kontextové okno
            
            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko vzdialenej obsluhy')

        elif objekt == 'priecestie':
            self.lastPri = id
            if not self.workerThread.dictStanice[1].dialkove:   #ak má precovisko aktívne riadenie 
                self.update(id, clicked=True, objekt='priecestie')

                if self.workerThread.dictPriecestie[id].vyber:
                    self.comboShowHide('priecestie')
                
                else:
                    self.comboShowHide()

            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko vzdialenej obsluhy')

        elif objekt == 'TS':
            if not self.workerThread.dictStanice[1].dialkove:   #ak má precovisko aktívne riadenie 
                self.lastTS = id
                self.workerThread.dictTS[id].vybrane = not self.workerThread.dictTS[id].vybrane 
                if self.workerThread.dictTS[id].vybrane:
                    self.comboShowHide('TS_ZBE')
                
                else:
                    self.comboShowHide() 

            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko vzdialenej obsluhy')

        elif objekt == 'stanica':
            self.lastStanica = id
            self.update(id, True, 'Stanice')
            if self.workerThread.dictStanice[id].vyber:
                self.comboShowHide('stanica')
            
            else:
                self.comboShowHide()

    def comboShowHide(self, nazov = ' '):   #metóda pre zobrazovanie výberových ponúk pre návestidlá
        if nazov == 'vchodove': #zobrazí menu pre vchodové návestidlo
            self.ui.combo_hlavne.show()
            self.ui.combo_fikt.hide()
            self.ui.combo_kombi.hide()
            self.ui.combo_zriad.hide()    
        elif nazov == 'odchodove':  #zobrazí menu pre odchodové návestidlo
            self.ui.combo_kombi.show()
            self.ui.combo_fikt.hide()
            self.ui.combo_hlavne.hide()
            self.ui.combo_zriad.hide() 
        elif nazov == 'zriadovacie':    #zobrazí menu pre zriaďovacie návestidlo
            self.ui.combo_zriad.show() 
            self.ui.combo_fikt.hide()
            self.ui.combo_hlavne.hide()
            self.ui.combo_kombi.hide() 
        elif nazov == 'fiktivne':   #zobrazí menu pre fiktívne návestidlo
            self.ui.combo_fikt.show()
            self.ui.combo_hlavne.hide()
            self.ui.combo_kombi.hide()
            self.ui.combo_zriad.hide()    

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

        elif nazov == 'TS_ZBE': #zobrazí menu pre traťový súhlas
            self.ui.combo_TS_ZBE.show()

        elif nazov == 'priecestie': #zobrazí menu pre priecestie
            self.ui.combo_priec.show()

        elif nazov == 'stanica':    #zobrazí menu pre riadenie stanice
            self.ui.combo_Riadenie.show()

        else:   #skryje všetky menu
            self.ui.combo_fikt.hide()
            self.ui.combo_hlavne.hide()
            self.ui.combo_kombi.hide()
            self.ui.combo_zriad.hide()    
            self.ui.combo_ciel_fi.hide()   
            self.ui.combo_ciel_ko.hide()
            self.ui.combo_ciel_zr.hide()
            self.ui.combo_vyh.hide()
            self.ui.combo_TS_ZBE.hide()
            self.ui.combo_priec.hide()
            self.ui.combo_Riadenie.hide()

    def akciaPriecestie(self, index):   #vyhodnotenie vybranej akcie z kontextového menu
        self.comboShowHide()    #po výbere skry menu

        if index == 1:  #zatvorenie priecetia
            self.prikazDoPLC(priec=True, nazov=self.workerThread.dictPriecestie[self.lastPri].nazovGUI, prikaz='/True')            

        elif index == 2:  #otvorenie priecestia
            self.prikazDoPLC(priec=True, nazov=self.workerThread.dictPriecestie[self.lastPri].nazovGUI, prikaz='/False')
        
        else:
            self.workerThread.dictPriecestie[self.lastPri].vyber = False
            self.workerThread.dictPriecestie[self.lastPri].update(self)

        self.ui.combo_priec.setCurrentIndex(0) #resetuj index vybranej akcie z kontextového menu

    def akciaNavestidlo(self, index, ID):   #vyhodnotenie vybranej akcie z kontextového menu
        self.comboShowHide()    #po výbere skry menu

        if ((ID in [1,2]) and index == 1) and (self.lastNav not in [10,11]):  #výber vlakovej cesty
            self.vyberCestu('Vlak')

        elif ((ID == 2 and index == 2) or (ID == 3 and index == 1)) and (self.lastNav not in [10,11]):  #výber posunovej cesty
            if self.lastNav in [1,4,5]:
                self.vyberCestu('Posun')

            else:
                self.vypisHlasenia('Nie je možné postaviť posunovú cestu')

        elif (ID == 4 and index == 1) or (ID == 2 and index == 4) or (ID == 3 and index == 2):    #rušenie cesty
            self.End = self.lastNav
            self.lastNav = 0

            if ID == 4:
                self.prikazDoPLC(odchod=True, nazov='odchodR', prikaz='/False')

            self.dictNav[self.End].vybrane = False
            self.dictNav[self.End].update(self)
            self.szz.rusenieCesty()

        elif self.Start == self.dictNav[3].ID and ID in [10,12] and index == 1: #stavanie vchodovej bez ochrannej dráhy
            if not self.szz.typCesty:
                self.postavCestu()
            else:
                self.vypisHlasenia('Nekorektný typ jazdnej cesty')

        elif (self.Start == self.dictNav[3].ID) and ((ID in [10,12]) and (index == 2) and (not self.szz.typCesty)): #stavanie vchodovej cesty s ochrannou dráhou
           self.vypisHlasenia('Nie je možné postaviť cestu s ochrannou drájou')
           self.ukonciStavanie()

        elif (self.Start in [self.dictNav[4].ID, self.dictNav[5].ID]) and ((ID in [10,12]) and (index == 1) and (not self.szz.typCesty)): #stavanie odchodovej cesty
            if self.workerThread.dictTS[1].prijem:
                self.postavCestu()
            else:
                self.ukonciStavanie(TS=True)

        elif (self.Start in [1] and ID == 10 and index == 3) or (ID == 11 and index ==1):    #stavanie posunovej cesty
                self.postavCestu()

        elif ((ID == 1 and index == 2) or (ID == 2 and index == 3)) and (self.lastNav not in [9,10]): #Privolávacia návesť
            self.dictNav[self.lastNav].vybrane = False
            
            if self.dictNav[self.lastNav].znak == 'Stoj':
                self.dictNav[self.lastNav].znak = 'PN'
                self.prikazDoPLC(prikaz='/PN', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)
                self.prikazDoPLC(prikaz='/PN', znak=True)
                self.dictNav[self.lastNav].update(self)

            elif self.dictNav[self.lastNav].znak == 'PN':
                self.dictNav[self.lastNav].znak = 'Stoj'
                self.prikazDoPLC(prikaz='/Stoj', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)
                self.prikazDoPLC(prikaz='/Stoj', znak=True)
                self.dictNav[self.lastNav].update(self)            

        elif ((ID == 1 and index == 5) or (ID == 2 and index == 6) or (ID == 3 and index == 4)) and (self.lastNav not in [10,11]): #Manuálne zadanie 'Stoj'
            self.dictNav[self.lastNav].vybrane = False

            if self.dictNav[self.lastNav].pociatocne:   #iba ak je návestidlo počiatočným návestidlom jazdnej cesty
                self.dictNav[self.lastNav].manual = True
                self.dictNav[self.lastNav].znak = 'Stoj'
                self.prikazDoPLC(prikaz='/Stoj', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)
                self.prikazDoPLC(prikaz='/Stoj', znak=True)
                self.dictNav[self.lastNav].update(self)

            else:
                self.vypisHlasenia('Nesprávne zadanie STOJ na návestidle')

        elif ((ID == 1 and index == 4) or (ID == 2 and index == 5) or (ID == 3 and index == 3)) and (self.lastNav not in [10,11]): #Manuálne zadanie 'Volno'
            self.dictNav[self.lastNav].vybrane = False

            if self.dictNav[self.lastNav].pociatocne:   #iba ak je návestidlo počiatočným návestidlom jazdnej cesty
                self.dictNav[self.lastNav].manual = True
                if (ID == 1) or (ID == 2 and not self.dictNav[self.lastNav].typAktCes):
                    self.dictNav[self.lastNav].znak = 'Volno'
                    self.prikazDoPLC(prikaz='/Volno', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)
                    self.prikazDoPLC(prikaz='/Volno', znak=True)
                
                elif (ID == 3) or (ID == 2 and self.dictNav[self.lastNav].typAktCes):
                    self.dictNav[self.lastNav].znak = 'Posun'
                    self.prikazDoPLC(prikaz='/Posun', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)
                    self.prikazDoPLC(prikaz='/Posun', znak=True)
                
                self.dictNav[self.lastNav].update(self)
            
            else:
                self.vypisHlasenia('Nesprávne zadanie VOĽNO na návestidle')
        
        else:
            if self.lastNav != 0:
                self.dictNav[self.lastNav].vybrane = False
                self.dictNav[self.lastNav].update(self)

            if self.End != 0:
                self.dictNav[self.End].vybrane = False
                self.dictNav[self.End].update(self)

        self.ui.combo_hlavne.setCurrentIndex(0) #resetuj index vybranej akcie z kontextového menu
        self.ui.combo_kombi.setCurrentIndex(0)
        self.ui.combo_zriad.setCurrentIndex(0)
        self.ui.combo_fikt.setCurrentIndex(0)    

        self.ui.combo_ciel_zr.setCurrentIndex(0)
        self.ui.combo_ciel_ko.setCurrentIndex(0)
        self.ui.combo_ciel_fi.setCurrentIndex(0)

    def akciaTS(self, index):   #metóda pre prácu s traťovým súhlasom
        if (index == 1):   #žiadosť o TS    
            if  (not self.workerThread.dictTS[1].prijem) and (not self.workerThread.dictTS[1].odchod):
                if self.workerThread.dictTS[1].volnost: 
                    self.prikazDoPLC('ZUS/1/True')
                else:
                    self.vypisHlasenia('Obsadený medzistaničný úsek')
            else:
                self.vypisHlasenia('Traťový súhlas je prijatý')

        elif (index == 2):   #zrušenie žiadosti o TS
            self.prikazDoPLC('ZUS/1/False')        
            self.ziadostAktivna = False

        elif (index == 3) and (self.workerThread.dictTS[1].ziadost is True):   #udelenie TS
            self.prikazDoPLC('UTS/1')
        
        self.comboShowHide()
        self.ui.combo_TS_ZBE.setCurrentIndex(0)

    def akciaStanica(self, index):  #metóda pre spracovanie signálov riadenia
        if index == 1: #žiadosť o prevzatie riadenia
            if self.workerThread.dictStanice[self.lastStanica].dialkove:
                if self.workerThread.dictStanice[self.lastStanica].ziadost: #ak už je aktívna žiadosť
                    self.prikazDoPLC(prikaz='/True', nazov=self.workerThread.dictStanice[self.lastStanica].nazovGUI, ziadRiad=False)    #zruš ju

                else:   #ak nie je žiadosť aktívna
                    self.prikazDoPLC(prikaz='/True', nazov=self.workerThread.dictStanice[self.lastStanica].nazovGUI, ziadRiad=True) #aktivuj ju

            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko vzdialenej obsluhy')
        
        elif index == 2: #potvrdenie žiadosti o prevzatie riadenia
            if self.workerThread.dictStanice[self.lastStanica].ziadost:
                self.prikazDoPLC(nazov=self.workerThread.dictStanice[self.lastStanica].nazovGUI, udelRiad=True)     

            else:
                self.vypisHlasenia('Žiadosť nebola prijatá')       

        self.comboShowHide()
        widget.ui.combo_Riadenie.setCurrentIndex(0)

    def vyberCestu(self, typ):  #metóda pre zápis potrebných hodnôt pre výber jazdnej cesty
        if typ == 'Vlak':   #zapíše správny typ cesty
            self.szz.typCesty = False
        elif typ == 'Posun':
            self.szz.typCesty = True

        self.szz.vyberCesty = True #definuje aktívny výber vlakovej cesty

        self.Start = self.lastNav   #vybrané návestidlo označí za počiatočné

        self.dictNav[self.Start].stavanieOd = True
        self.dictNav[self.Start].typAktCes = self.szz.typCesty #zapíše počiatočnému návestidlu typ cesty
        self.dictNav[self.Start].vybrane = False
        self.dictNav[self.Start].update(self)

    def postavCestu(self, Ochr=False):  #metóda, ktorá vydá príkaz pre postavenie vybranej cesty algoritmom SZZ
        self.szz.vyberCesty = False
        self.End = self.lastNav
        self.lastNav = 0

        self.dictNav[self.End].vybrane = False
        self.dictNav[self.End].update(self)

        return self.szz.stavanieCesty(OD=Ochr)
    
    def ukonciStavanie(self, TS=False, odhl=False):   #metóda slúži na ukončenie stavania VC v prípade zlého TS alebo obsadeného medzist. úseku
        self.dictNav[self.Start].stavanieOd = False
        self.dictNav[self.Start].update(self)
        self.szz.vyberCesty = False
        self.Start = 0
        self.End = 0
        
        if odhl:
            self.vypisHlasenia('Chýbajúca odhláška za posledným vlakom')
        elif TS:
            self.vypisHlasenia('Neudelený traťový súhlas')
        elif TS:
            self.vypisHlasenia('Obsadený medzstaničný úsek')

    def prikazDoPLC(self, prikaz='_', id=0, nazov='_', OD=False, vyh=False, odchod=False, priec=False, predhl=False, ziadRiad=False, udelRiad=False, cesta=False, cas=False, znak=False):  #metóda pre odosielanie dát do PLC
        adresa = self.citajAdresu()
        if id == 0:
            if OD:  #príkaz do PLC pre ochrannú dráhu
                URL = adresa + 'write/OchrDr/' + nazov + prikaz
            
            elif vyh: #prestavenie výhybky
                URL = adresa + 'write/vyhybka/' + nazov + prikaz
            
            elif odchod:
                URL = adresa + 'odchod/' + nazov + prikaz
            
            elif priec:
                URL = adresa + 'write/priecestie/' + nazov + prikaz
            
            elif predhl:
                URL = adresa + 'predhl/' + nazov + prikaz
            
            elif ziadRiad:
                URL = adresa + 'ziadRiad/' + nazov + prikaz
            
            elif udelRiad:
                URL = adresa + 'udelRiad/' + nazov
            
            elif cesta:
                if self.Start > 45:
                    start = self.dictNav[self.Start].zavisle
                else:
                    start = self.Start

                if self.End > 45:
                    end = self.dictNav[self.End].zavisle
                else:
                    end = self.End

                if nazov == 'stavanie':
                    if prikaz == 'True':
                        URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/' + str(self.szz.typCesty) + '/True/True/False/RAD'

                    else:
                        URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/' + str(self.szz.typCesty) + '/False/True/False/RAD'

                elif nazov == 'rusenie':
                    URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/False/False/False/True/RAD'
                    
                else:
                    URL = adresa + 'Cesta/0/0/False/False/False/False/RAD'

            elif znak:
                if self.lastNav > 45:
                    nav = self.dictNav[self.lastNav].zavisle
                else:
                    nav = self.lastNav

                if prikaz != '_':
                    URL = adresa + 'Navest/' + str(nav) + prikaz + '/RAD'

                else:
                    URL = adresa + 'Navest/0/Stoj/RAD'

            elif cas:
                URL = adresa + 'CasP/disp'

            else:   #Traťový súhlas
                URL = adresa + prikaz
        else:   #príkaz od objektu Navestidlo na zmenu návesti
            URL = 'write/navestidlo/'
            if id in range(1,11) or id in range(46,55):
                URL = URL + 'RAD/'
            
            elif id in range(12,34) or id in range(56,68):
                URL = URL + 'ZBE/'
            
            elif id in range(35,45) or id in range(69,77):
                URL = URL + 'HLO/'
        
            URL = adresa + URL + nazov + prikaz

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
    widget.ui.combo_ciel_ko.hide()
    widget.ui.combo_ciel_zr.hide()
    widget.ui.combo_ciel_fi.hide()
    widget.ui.combo_vyh.hide()
    widget.ui.combo_TS_ZBE.hide()
    widget.ui.combo_priec.hide()
    widget.ui.combo_Riadenie.hide()

    widget.ui.groupREST.setVisible(False)
    widget.ui.groupPrehlad.setVisible(False)

    #prepojenia s metódou vyhodnotenia akcie z kontextového menu
    widget.ui.combo_hlavne.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_hlavne.currentIndex(), 1))    #počiatok jazdnej cesty   
    widget.ui.combo_kombi.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_kombi.currentIndex(), 2))
    widget.ui.combo_zriad.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_zriad.currentIndex(), 3))
    widget.ui.combo_fikt.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_fikt.currentIndex(), 4))

    widget.ui.combo_ciel_ko.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_ciel_ko.currentIndex(), 10)) #koniec jazdnej cesty 
    widget.ui.combo_ciel_zr.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_ciel_zr.currentIndex(), 11))
    widget.ui.combo_ciel_fi.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_ciel_fi.currentIndex(), 12))

    widget.ui.combo_TS_ZBE.currentIndexChanged.connect(lambda: widget.akciaTS(widget.ui.combo_TS_ZBE.currentIndex()))   #traťový súhlas

    widget.ui.combo_priec.currentIndexChanged.connect(lambda: widget.akciaPriecestie(widget.ui.combo_priec.currentIndex())) #priecestie

    widget.ui.combo_Riadenie.currentIndexChanged.connect(lambda: widget.akciaStanica(widget.ui.combo_Riadenie.currentIndex()))   #riadenie stanice

    widget.ui.combo_vyh.currentIndexChanged.connect(lambda: widget.szz.prestavenieVyh(widget.lastVyh ,widget.ui.combo_vyh.currentIndex()))  #prestavenie výmeny  

    widget.ui.actionVlastnosti.triggered.connect(lambda: widget.popUp(okno='REST'))   #práca s oknom REST API
    widget.ui.ButtonClose.clicked.connect(lambda: widget.popUp(okno='REST'))

    widget.ui.actionInfo.triggered.connect(lambda: widget.popUp(okno='Prehlad'))
    widget.ui.ButtonClose_1.clicked.connect(lambda: widget.popUp(okno='Prehlad'))

    widget.ui.actionZavrie.triggered.connect(lambda: widget.quit()) #terminácia aplikácie
    
    #prepojenia s metódou na zobrazenie kontextového menu pre zvolený element
    #---------------NÁVESTIDLÁ-------------------------------------------    
    widget.ui.RAD_zr_do_st_odZ.clicked.connect(lambda: widget.clickObjekt(1, 'navestidlo')) 
    widget.ui.RAD_zr_zo_st_odZ.clicked.connect(lambda: widget.clickObjekt(2, 'navestidlo'))
    widget.ui.RAD_S.clicked.connect(lambda: widget.clickObjekt(3, 'navestidlo'))
    widget.ui.RAD_L1.clicked.connect(lambda: widget.clickObjekt(4, 'navestidlo'))
    widget.ui.RAD_L2.clicked.connect(lambda: widget.clickObjekt(5, 'navestidlo'))    
    widget.ui.RAD_fik_S.clicked.connect(lambda: widget.clickObjekt(6, 'navestidlo'))
    widget.ui.RAD_1k_fik.clicked.connect(lambda: widget.clickObjekt(10, 'navestidlo'))
    widget.ui.RAD_2k_fik.clicked.connect(lambda: widget.clickObjekt(11, 'navestidlo'))
    #--------------------------------------------------------------------
    #-------------VÝHYBKY------------------------------------------------
    widget.ui.RAD_V1.clicked.connect(lambda: widget.clickObjekt(3, 'vyhybka'))
    #--------------------------------------------------------------------
    #-------------TRAŤOVÝ SÚHLAS-----------------------------------------
    widget.ui.RAD_trat_suhlas_doZ.clicked.connect(lambda: widget.clickObjekt(1, 'TS'))
    #--------------------------------------------------------------------
    #-------------PRIECESTIE---------------------------------------------
    widget.ui.RAD_ZBE_priec.clicked.connect(lambda: widget.clickObjekt(1, 'priecestie'))
    #--------------------------------------------------------------------
    #-------------RIADENIE STANICE---------------------------------------   
    widget.ui.RAD_dialkove.clicked.connect(lambda: widget.clickObjekt(1, 'stanica'))

    widget.ui.ButtonConnect.clicked.connect(lambda: widget.zahajPripojenie())  #prepojenie s metódou pre testovanie spojenia s PLC
    widget.ui.ButtonDisconnect.clicked.connect(lambda: widget.ukonciPripojenie())  #vyvolá ukončenie komunikácie

    app.exec()