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
from tratSuhlas import TratSuhlas
from SZZ import SZZ
from priecestie import Priecestie
from riadenieObsluhy import RiadenieObsluhy

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or

class dataUpdate(QThread):
    dataUpdated = Signal(dict, dict)

    odhlaskaLo = False
    odhlaskaSo = False
    predhlaskaZBE = False
    predhlaskaHLO = False

    def __init__(self, app_instance):
        self.dictUseky = {   #slovník úsekov
            8: Usek(ID=6, nazovGUI='RAD_ZBE_TU3', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),  
            9: Usek(ID=7, nazovGUI='RAD_ZBE_TU4', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),            
            10: Usek(ID=0, nazovGUI='ZBE_k1L', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            11: Usek(ID=1, nazovGUI='ZBE_k2BL', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            12: Vyhybka(ID=2, IDsmer=1, nazovGUI='ZBE_V1', usek='ZBE_v1', spojka=True, enumIkon=ico.SpojkaA, dictIkon=ico.dictSpojkaA, app=app_instance),
            13: Vyhybka(ID=3, IDsmer=1, nazovGUI='ZBE_V2', usek='ZBE_v2', spojka=True, enumIkon=ico.SpojkaB, dictIkon=ico.dictSpojkaB, app=app_instance),
            14: Usek(ID=4, nazovGUI='ZBE_k1', enummIkon=ico.KolajSt1, dictIkon=ico.dictStanKolaj1, app=app_instance),
            15: Usek(ID=5, nazovGUI='ZBE_k2', enummIkon=ico.KolajSt2, dictIkon=ico.dictStanKolaj2, app=app_instance),
            16: Vyhybka(ID=6, IDsmer=2, nazovGUI='ZBE_V3', usek='ZBE_v3', enumIkon=ico.VyhP, dictIkon=ico.dictVyhP, app=app_instance),
            17: Usek(ID=7, nazovGUI='ZBE_k1S', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),            
            18: Usek(ID=6, nazovGUI='ZBE_HLO_TU1_1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            19: Usek(ID=7, nazovGUI='ZBE_HLO_TU2_a', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            20: Usek(ID=7, nazovGUI='ZBE_HLO_TU2_b', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            21: Usek(ID=100, nazovGUI='LUZ_ZBE_TU1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance)
        }

        self.dictTS = { #slovník traťových súhlasov
            2: TratSuhlas(ID=2, nazovGUI='ZBE_trat_suhlas_doR', enumIkon=ico.TrSL, dictIkon=ico.dictTrSL, app=app_instance, typ='S'),
            3: TratSuhlas(ID=3, nazovGUI='ZBE_trat_suhlas_doH', enumIkon=ico.TrSP, dictIkon=ico.dictTrSP, app=app_instance, typ='L'),
            4: TratSuhlas(ID=4, nazovGUI='ZBE_trat_suhlas_doL', enumIkon=ico.TrSL, dictIkon=ico.dictTrSL, app=app_instance, typ='L')
        }

        self.dictPriecestie = { #slovník priecestí
            2:Priecestie(ID=2, nazovGUI='ZBE_HLO_priec', enumIkon=ico.Priecestie, dictIkon=ico.dictPriecestie, app=app_instance)
        } 

        self.dictStanice = {    #slovník stníc
            2:RiadenieObsluhy(ID=2, nazovGUI='ZBE_dialkove', enumIkon=ico.RiadenieZBE, dictIkon=ico.dictRiadenieZBE, app=app_instance),
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
                for index in self.dictUseky.keys(): #čítanie stavov koľajových úsekov             
                    if index in range(8,10):   
                        self.dictUseky[index].jeVolny = data['RAD;RAD-ZBE'][self.dictUseky[index].ID]

                    elif index in range(10,18):
                        self.dictUseky[index].jeVolny = data['ZBE'][self.dictUseky[index].ID]

                    elif index in range(18,21):
                        self.dictUseky[index].jeVolny = data['P1;P2;ZBE-HLO'][self.dictUseky[index].ID]

                    elif index in [21]:  #špeciálny prípad kedy sa dopytuje aj na LifeSigh ESA 44
                        if data['ZbeLuz'] is None:
                            self.dictUseky[index].odozva = False
                        else:
                            self.dictUseky[index].odozva = True
                            self.dictUseky[index].jeVolny = data['ZbeLuz']

                for i in [12,13,16]:    #čítanie smeru výmen
                    self.dictUseky[i].smer = data['SmerVyh'][self.dictUseky[i].IDsmer]

                #čítanie stavov traťových súhlasov
                self.dictTS[2].smer = data['TS']['smerRZ'] 
                self.dictTS[2].ziadost = data['TS']['ZUS_RZ']                   
                self.dictTS[2].volnost = data['TS']['volRZ']
                MyOdchod = data['TS']['odchodZR']
                SusOdchod = data['TS']['odchodR']
                self.dictTS[2].odchod = (MyOdchod or SusOdchod)  

                self.dictTS[3].smer = data['TS']['smerZH']                    
                self.dictTS[3].volnost = data['TS']['volZH']
                MyOdchod = data['TS']['odchodZH']
                HradloOdchod = data['TS']['predhlSo']
                self.dictTS[3].odchod = (MyOdchod or HradloOdchod) 

                self.dictTS[4].smer = data['TS']['smerLZ']  
                ZUS_ZBE = data['TS']['ZUS_LZ']
                ZTS_LUZ = data['TS']['ZTS_L']
                self.dictTS[4].ziadost = ZUS_ZBE or ZTS_LUZ                    
                self.dictTS[4].volnost = data['TS']['volLZ']
                self.dictTS[4].porBP = data['TS']['ziadZBP']
                MyOdchod = data['TS']['odchodZL']
                SusOdchod = data['TS']['odchodL']
                self.dictTS[4].odchod = (MyOdchod or SusOdchod) 

                #čítanie stavov priecestí
                self.dictPriecestie[2].predzvananie = data['Priecestie'][7]
                self.dictPriecestie[2].otvorene = data['Priecestie'][5]
                self.dictPriecestie[2].zatvorene = data['Priecestie'][6]
                self.dictPriecestie[2].jeVolny = self.dictUseky[19].jeVolny

                for index in self.dictStanice.keys():   #čítanie stavov riadenia staníc
                    self.dictStanice[2].dialkove = data['Riadenie']['dialkoveZBE']
                    self.dictStanice[2].ziadost = data['Riadenie']['ziadostZBE']

                self.odhlaskaLo = data['TS']['odhlLo']   #čítanie odhlášok z hradla Rišňovce  

                self.predhlaskaZBE = data['TS']['odchodZH'] #čítanie predhlášok zo staníc
                self.predhlaskaHLO = data['TS']['odchodH']  

                if data['Cesta']['stavanie']:
                    if (data['Cesta']['pociatocne'] in self.app_instance.dictNav.keys() and data['Cesta']['koncove'] in self.app_instance.dictNav.keys()) and (
                    data['Cesta']['odosielatel'] != 'ZBE'):
                        self.app_instance.Start = data['Cesta']['pociatocne']
                        self.app_instance.dictNav[self.app_instance.Start].pociatocne = True
                        self.app_instance.End = data['Cesta']['koncove']
                        self.app_instance.szz.typCesty = data['Cesta']['typCesty']
                        ochr = data['Cesta']['OD']
                        self.app_instance.szz.stavanieCesty(OD=ochr, server=True)
                        self.app_instance.prikazDoPLC(cesta=True)

                if data['Cesta']['rusenie']:
                    if data['Cesta']['koncove'] in self.app_instance.dictNav.keys() and data['Cesta']['odosielatel'] != 'ZBE':
                        self.app_instance.End = data['Cesta']['koncove']
                        self.app_instance.szz.rusenieCesty(server=True)
                        self.app_instance.prikazDoPLC(cesta=True)

                if data['Navest']['ID'] != 0 and data['Navest']['ID'] in self.app_instance.dictNav.keys() and data['Navest']['odosielatel'] != 'HLO':
                    self.app_instance.dictNav[data['Navest']['ID']].znak = data['Navest']['znak']
                    self.app_instance.dictNav[data['Navest']['ID']].update(self)
                    self.app_instance.prikazDoPLC(znak=True)

            self.dataUpdated.emit(self.dictUseky, self.dictTS)
        sleep(0.1)

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

class LifeSign(QThread): #LifeSign aplikácie
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance

    def run(self):
        while not self.isInterruptionRequested():
            self.app_instance.prikazDoPLC(cas=True)
            self.sleep(5)   #5 sekúnd

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
            12: Navestidlo(ID=12, nazov='Z_L', usekPred='RAD_ZBE_TU4', usekZa='ZBE_k1L', nazovGUI='ZBE_L', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self),
            13: Navestidlo(ID=13, nazov='Z_BL', usekPred='LUZ_ZBE_TU1', usekZa='ZBE_k2BL', nazovGUI='ZBE_BL', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self),
            14: Navestidlo(ID=14, nazov='Z_L_fik', usekPred='ZBE_k1L', nazovGUI='ZBE_fik_L', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            15: Navestidlo(ID=15, nazov='Z_BL_fik', usekPred='ZBE_k2BL', nazovGUI='ZBE_fik_BL', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            16: Navestidlo(ID=16, nazov='Z_Se1p', usekPred='ZBE_k1L', nazovGUI='ZBE_zr_zo_st_odR', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL, app=self),
            17: Navestidlo(ID=17, nazov='Z_Se2p', usekPred='ZBE_k2BL', nazovGUI='ZBE_zr_zo_st_odL', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL, app=self),
            18: Navestidlo(ID=18, nazov='Z_Se1', usekPred='ZBE_k1L', usekZa='ZBE_V1', nazovGUI='ZBE_zr_do_st_odR', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=self),
            19: Navestidlo(ID=19, nazov='Z_Se2', usekPred='ZBE_k2BL', usekZa='ZBE_V2', nazovGUI='ZBE_zr_do_st_odL', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=self),
            20: Navestidlo(ID=20, nazov='Z_S1', usekPred='ZBE_k1', usekZa='ZBE_V1', nazovGUI='ZBE_S1', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, app=self),
            21: Navestidlo(ID=21, nazov='Z_S2', usekPred='ZBE_k2', usekZa='ZBE_V2', nazovGUI='ZBE_S2', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, app=self),
            22: Navestidlo(ID=22, nazov='Z_L1', usekPred='ZBE_k1', usekZa='ZBE_V3', nazovGUI='ZBE_L1', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, app=self),
            23: Navestidlo(ID=23, nazov='Z_L2', usekPred='ZBE_k2', usekZa='ZBE_V3', nazovGUI='ZBE_L2', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, app=self),
            24: Navestidlo(ID=24, nazov='Z_Se3', usekPred='ZBE_k1S', usekZa='ZBE_V3', nazovGUI='ZBE_zr_do_st_odH', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL, app=self),
            25: Navestidlo(ID=25, nazov='Z_Se3p', usekPred='ZBE_k1S', nazovGUI='ZBE_zr_zo_st_odH', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=self),
            26: Navestidlo(ID=26, nazov='Z_S_fik', usekPred='ZBE_k1S', nazovGUI='ZBE_fik_S', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, app=self),
            27: Navestidlo(ID=27, nazov='Z_S', usekPred='ZBE_HLO_TU1_1', usekZa='ZBE_k1S', nazovGUI='ZBE_S', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self),
            28: Navestidlo(ID=28, nazov='Z_40', usekPred='RAD_ZBE_TU4', usekZa='RAD_ZBE_TU3', nazovGUI='RAD_ZBE_40', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self, oddielove=True, TZZ='AB3'),
            29: Navestidlo(ID=29, nazov='Z_39', usekPred='RAD_ZBE_TU3', usekZa='RAD_ZBE_TU4', nazovGUI='RAD_ZBE_39', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self, oddielove=True, TZZ='AB3'),
            30: Navestidlo(ID=30, nazov='Z_Lo', usekPred='ZBE_HLO_TU1_1', usekZa='ZBE_HLO_TU2_a', nazovGUI='ZBE_HLO_Lo', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self, oddielove=True, TZZ='AH'),
            31: Navestidlo(ID=31, nazov='Z_So', usekPred='ZBE_HLO_TU2_a', usekZa='ZBE_HLO_TU1_1', nazovGUI='ZBE_HLO_So', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self, oddielove=True, TZZ='AH'),
            32: Navestidlo(ID=32, nazov='Z_28_fik', usekPred='RAD_ZBE_TU3', nazovGUI='RAD_ZBE_fik_28', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            33: Navestidlo(ID=33, nazov='Z_BS_fik', usekPred='LUZ_ZBE_TU1', nazovGUI='LUZ_fik_BS', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            34: Navestidlo(ID=34, nazov='Z_HLO_L_fik', usekPred='ZBE_HLO_TU2_b', nazovGUI='HLO_fiktL', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, app=self)
            }       

        super().__init__(parent)
        self.ui = Ui_ILTIS()    #vytvorenie spojenia s triedami
        self.szz = SZZ(self)   

        self.ui.setupUi(self)

        self.workerThread = dataUpdate(self)   #prepojenie bočných vláken s hlavným vláknom
        self.workerThreadTimeVlak = DlhyCasVlak()
        self.workerThreadTimePosun = DlhyCasPosun()
        self.workerThreadTimeOD = CasOchrDr()
        self.workerThreadLifeSign = LifeSign(self)
        self.workerThreadDateTime = DateTime()
        self.workerThreadDateTime.start()

        self.workerThread.dataUpdated.connect(self.update)    #definícia prepojenia vláken a metód
        self.workerThread.dataUpdated.connect(lambda: self.szz.stavanieCesty(True))

        self.workerThreadDateTime.dataUpdated.connect(self.aktualizaciaCasu)

        self.workerThreadTimeVlak.finished.connect(lambda: self.szz.rusenieCesty(True))
        self.workerThreadTimePosun.finished.connect(lambda: self.szz.rusenieCesty(True))
        self.workerThreadTimeOD.finished.connect(lambda: self.szz.rusenieOD())

        self.workerThread.setParent(self)  #definovanie rosičovského objektu pre vlákna
        self.workerThreadLifeSign.setParent(self)

        self.dictNav[28].zhasnute = True

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
            self.workerThreadLifeSign.start()

            self.ui.ZBE_ASVC.setIcon(ico.icon_ASVC_vypnute)

    def ukonciPripojenie(self):  #metóda pre zastavenie vláken a ukončenie komunikácie
        self.workerThread.requestInterruption()    #po úspešnom spojení sa spúšťa beh vláken
        self.workerThreadTimeVlak.requestInterruption()
        self.workerThreadTimePosun.requestInterruption()
        self.workerThreadTimeOD.requestInterruption()  
        self.workerThreadDateTime.requestInterruption()  
        self.workerThreadLifeSign.requestInterruption()  

        self.ui.textChybaREST.show()
        self.ui.textChybaESA.show() 

    def aktualizaciaCasu(self, cas):    #metóda pre aktualizáciu času v GUI
        self.ui.DateTime.setText(cas)

    def update(self, ID=-1, clicked=False, objekt='update'): #metóda pre aktualizáciu symbolov objektov
        if objekt in ['update', 'useky']:   #aktualizácia úsekov
            for i in self.workerThread.dictUseky.keys():
                self.workerThread.dictUseky[i].update(self)
                
                if self.workerThread.dictUseky[21].odozva:
                    self.ui.textChybaESA.hide()
                
                else:
                    self.ui.textChybaESA.show()

        if objekt in ['update', 'navestidla']:  #aktualizácia návestidiel
            self.dictNav[28].zhasnute =  not self.workerThread.dictTS[2].smer  #otáčanie svietenia AB podľa TS
            self.dictNav[29].zhasnute =  self.workerThread.dictTS[2].smer
            
            self.dictNav[30].predhlaska = self.workerThread.predhlaskaZBE
            self.dictNav[31].predhlaska = self.workerThread.predhlaskaHLO

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

    def clickObjekt(self, id, objekt): #metóda spracovávajúca kliknutie na objekt
        if objekt == 'navestidlo':
            self.lastNav = id   #zápis posledného kliknutého návestidla                
            
            if not self.workerThread.dictStanice[2].dialkove:   #ak má precovisko aktívne riadenie 
                self.update(id, True, 'navestidla')            
                if id in [12, 13, 27]: #vchodové návestidlo
                    if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('vchodove')
                    
                    elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('vchodove_konc')
                    
                    else:
                        self.comboShowHide()

                elif id in [20, 21, 22, 23]:    #odchodové návestidlo
                    if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('odchodove')
                    
                    elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('odchodove_konc')
                    
                    else:
                        self.comboShowHide()

                elif id in [16, 17, 18, 19, 24, 25]:  #zriaďovacie návestidlo
                    if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('zriadovacie')
                    
                    elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('zriadovacie_konc')
                    
                    else:
                        self.comboShowHide()

                elif id in [14, 15, 26]:   #fiktívne návestidlo
                    if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                        self.comboShowHide('fiktivne')
                    
                    elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                        self.comboShowHide('fiktivne_konc')
                    
                    else:
                        self.comboShowHide()

                elif id in [31]:   #oddielové návestidlo
                    if self.dictNav[id].vybrane:
                        self.comboShowHide('oddielove')
                    
                    else:
                        self.comboShowHide()

            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko vzdialenej obsluhy')

        elif objekt == 'vyhybka':
            if not self.workerThread.dictStanice[2].dialkove:   #ak má precovisko aktívne riadenie 
                if id in self.workerThread.dictUseky:  #ak sa výhybka nachádza v zozname
                    self.lastVyh = id   #zapíš ju ako poslednú kliknutú
                    if id in [12, 13]:  #úprava pre výhybkovú spojku
                        self.workerThread.dictUseky[12].vyber = not self.workerThread.dictUseky[12].vyber
                        self.workerThread.dictUseky[13].vyber = not self.workerThread.dictUseky[13].vyber
                        self.workerThread.dictUseky[12].update(self)
                        self.workerThread.dictUseky[13].update(self)
                    
                    else:
                        self.workerThread.dictUseky[id].vyber = not self.workerThread.dictUseky[id].vyber
                        self.workerThread.dictUseky[id].update(self)

                    if self.workerThread.dictUseky[id].vyber:  #je výhybka vybraná obsluhou?
                        self.ui.combo_vyh.show()  #ak áno zobraz kontextové okno akcií
                    
                    else:
                        self.ui.combo_vyh.hide()  #ak nie skry kontextové okno
                    
            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko vzdialenej obsluhy')

        elif objekt == 'TS':
            if not self.workerThread.dictStanice[2].dialkove:   #ak má precovisko aktívne riadenie 
                self.lastTS = id
                self.workerThread.dictTS[id].vybrane = not self.workerThread.dictTS[id].vybrane 

                if id == 2 and self.workerThread.dictTS[2].vybrane:
                    self.comboShowHide('TS_RAD')
                
                elif id == 3 and self.workerThread.dictTS[3].vybrane:
                    self.comboShowHide('TS_HLO')
                
                elif id == 4 and self.workerThread.dictTS[4].vybrane:
                    self.comboShowHide('TS_LUZ')
                
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

    def akciaNavestidlo(self, index, ID):   #vyhodnotenie vybranej akcie z kontextového menu
        self.comboShowHide()    #po výbere skry menu

        if ((ID in [1,2]) and index == 1):  #výber vlakovej cesty
            self.vyberCestu('Vlak')

        elif ((ID == 2 and index == 2) or (ID == 3 and index == 1)) and (self.lastNav not in [16, 17, 25]):  #výber posunovej cesty
            if self.lastNav in [18,19,20,21,22,23,24]:
                self.vyberCestu('Posun')

            else:
                self.vypisHlasenia('Nie je možné postaviť posunovú cestu')

        elif (ID == 4 and index == 1) or (ID == 2 and index == 4) or (ID == 3 and index == 2):    #rušenie cesty
            self.End = self.lastNav
            self.lastNav = 0

            if ID ==4:  #predhlášky od jednotlivých staníc
                if self.End == 14:
                    self.prikazDoPLC(odchod=True, nazov='odchodZR', prikaz='/False')
                elif self.End == 15:
                    self.prikazDoPLC(odchod=True, nazov='odchodZL', prikaz='/False')
                elif self.End == 26:
                    self.prikazDoPLC(odchod=True, nazov='odchodZH', prikaz='/False')
                    self.prikazDoPLC(prikaz='/False', nazov='ZBE', predhl=True)
            
            if self.End == 26:
                self.dictNav[30].predhlaska = False

            self.dictNav[self.End].vybrane = False
            self.dictNav[self.End].update(self)
            self.szz.rusenieCesty()

        elif self.Start in [12, 13, 27] and ID == 10 and index == 1: #stavanie vchodovej bez ochrannej dráhy
            if not self.szz.typCesty:
                self.postavCestu()
            else:
                self.vypisHlasenia('Nekorektný typ jazndej cesty')

        elif (ID == 10) and (index == 2) and (not self.szz.typCesty): #stavanie vchodovej cesty s ochrannou dráhou
            if self.Start in [12,13,27]:
                self.postavCestu(True)

            else:
                self.vypisHlasenia('Jazdná cesta nemá definovanú ochrannú dráhu')
                self.ukonciStavanie()

        elif (self.Start in [20, 21, 22, 23]) and ((ID == 12) and (index == 1) and (not self.szz.typCesty)): #stavanie odchodovej cesty
            if self.Start == 20:
                if self.workerThread.dictTS[2].prijem:
                    self.postavCestu()
                else:
                    self.ukonciStavanie(TS=True)
                
            elif self.Start == 21:
                if self.lastNav == 14:
                    if self.workerThread.dictTS[2].prijem:
                        self.postavCestu()
                    else:
                        self.ukonciStavanie(TS=True)

                elif self.lastNav == 15:
                    if self.workerThread.dictTS[4].volnost: 
                        if self.workerThread.dictTS[4].prijem:
                            self.postavCestu()
                        else:
                            self.ukonciStavanie(TS=True)
                    else:
                        self.ukonciStavanie(volnost=True)

            elif self.Start in [22, 23]:
                if self.workerThread.odhlaskaLo:                    
                    if self.workerThread.dictTS[3].prijem:
                        self.postavCestu()
                    else:
                        self.ukonciStavanie(TS=True)
                else:
                    self.ukonciStavanie(odhl=True)

        elif (self.Start in [18, 19, 20, 21, 22, 23, 24]) and ((ID == 10) and (index == 3)) or ((ID == 11) and (index == 1) and self.szz.typCesty):    #stavanie posunovej cesty
            self.postavCestu()

        elif  ((ID == 1 and index == 2) or (ID == 2 and index == 3) or (ID == 5 and index == 1)): #Privolávacia návesť
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

        elif  ((ID == 1 and index == 5) or (ID == 2 and index == 6) or (ID == 3 and index == 4) or (ID == 5 and index == 3)) and (self.lastNav not in [15, 16, 25]): #Manuálne zadanie 'Stoj'
            self.dictNav[self.lastNav].vybrane = False

            if (self.dictNav[self.lastNav].pociatocne) or (self.dictNav[self.lastNav].TZZ == 'AH' and self.dictNav[self.lastNav].predhlaska):   #iba ak je návestidlo počiatočným návestidlom jazdnej cesty
                self.dictNav[self.lastNav].manual = True
                self.dictNav[self.lastNav].znak = 'Stoj'
                self.prikazDoPLC(prikaz='/Stoj', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)
                self.prikazDoPLC(prikaz='/Stoj', znak=True)
                self.dictNav[self.lastNav].update(self)
            else:
                self.vypisHlasenia('Nesprávne zadanie STOJ na návestidle')

        elif  ((ID == 1 and index == 4) or (ID == 2 and index == 5) or (ID == 3 and index == 3) or (ID == 5 and index == 2)) and (self.lastNav not in [15, 16, 25]): #Manuálne zadanie 'Volno'
            self.dictNav[self.lastNav].vybrane = False

            if (self.dictNav[self.lastNav].pociatocne) or (self.dictNav[self.lastNav].TZZ == 'AH' and self.dictNav[self.lastNav].predhlaska):   #iba ak je návestidlo počiatočným návestidlom jazdnej cesty
                self.dictNav[self.lastNav].manual = True
                if (ID in [1,5]) or (ID == 2 and not self.dictNav[self.lastNav].typAktCes):
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
        self.ui.combo_oddielove.setCurrentIndex(0)   

        self.ui.combo_ciel_zr.setCurrentIndex(0)
        self.ui.combo_ciel_ko.setCurrentIndex(0)
        self.ui.combo_ciel_fi.setCurrentIndex(0)

    def akciaTS(self, index, id):   #metóda pre prácu s traťovým súhlasom
        if ((index == 1) and (id == 5) and (self.workerThread.dictTS[id].prijem is True)): 
            self.prikazDoPLC('UTS/' + str(id))
        
        self.comboShowHide()
        self.ui.combo_TS_HLO.setCurrentIndex(0)

        if (index == 1) and (id in [2,4]):   #žiadosť o TS
            if (not self.workerThread.dictTS[id].prijem) and (not self.workerThread.dictTS[id].odchod):
                if self.workerThread.dictTS[id].volnost: 
                    self.prikazDoPLC('ZUS/' + str(id) + '/True')
                else:
                    self.vypisHlasenia('Obsadený medzistaničný úsek')
            else:
                self.vypisHlasenia('Traťový súhlas je prijatý')

        elif (index == 2) and (id in [2,4]):   #zrušenie žiadosti o TS
            self.prikazDoPLC('ZUS/' + str(id) + '/False')        

        elif (((index == 3) and (id == 2) and (self.workerThread.dictTS[2].ziadost is True)) or
        ((index == 3) and (id == 4) and (self.workerThread.dictTS[4].ziadost is True)) or (
        (index == 1) and (id == 3) and (self.workerThread.dictTS[3].prijem is True))):   #udelenie TS
            self.prikazDoPLC('UTS/' + str(id))

        elif (index == 4) and (id == 4):    #zrušenie blokovej podmienky
            self.prikazDoPLC('ZBP/' + str(self.lastTS))

        elif index != 0:
            self.vypisHlasenia('Neudelený traťový súhlas')

        self.comboShowHide()
        self.ui.combo_TS_RAD.setCurrentIndex(0)
        self.ui.combo_TS_HLO.setCurrentIndex(0)
        self.ui.combo_TS_LUZ.setCurrentIndex(0)  

    def akciaStanica(self, index):  #metóda pre spracovanie signálov riadenia
        if index == 1: #žiadosť o prevzatie riadenia
            if self.workerThread.dictStanice[self.lastStanica].dialkove:
                if self.workerThread.dictStanice[self.lastStanica].ziadost: #ak už je aktívna žiadosť
                    self.prikazDoPLC(prikaz='/False', nazov=self.workerThread.dictStanice[self.lastStanica].nazovGUI, ziadRiad=True)    #zruš ju

                else:   #ak nie je žiadosť aktívna
                    self.prikazDoPLC(prikaz='/True', nazov=self.workerThread.dictStanice[self.lastStanica].nazovGUI, ziadRiad=True) #aktivuj ju

            else:
                self.vypisHlasenia('Obsluha stanice prevedená na pracovisko lokálnej obsluhy')
        
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

    def ukonciStavanie(self, TS=False, odhl=False, volnost=False):   #metóda slúži na ukončenie stavania VC v prípade zlého TS alebo obsadeného medzist. úseku
        self.dictNav[self.Start].stavanieOd = False
        self.dictNav[self.Start].update(self)
        self.szz.vyberCesty = False
        self.Start = 0
        self.End = 0
        
        if odhl:
            self.vypisHlasenia('Chýbajúca odhláška za posledným vlakom')
        elif TS:
            self.vypisHlasenia('Neudelený traťový súhlas')
        elif volnost:
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
                        URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/' + str(self.szz.typCesty) + '/True/True/False/DISP'

                    else:
                        URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/' + str(self.szz.typCesty) + '/False/True/False/DISP'

                elif nazov == 'rusenie':
                    URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/False/False/False/True/DISP'
                    
                else:
                    URL = adresa + 'Cesta/0/0/False/False/False/False/DISP'

            elif znak:
                if self.lastNav > 45:
                    nav = self.dictNav[self.lastNav].zavisle
                else:
                    nav = self.lastNav

                if prikaz != '_':
                    URL = adresa + 'Navest/' + str(nav) + prikaz + '/DISP'

                else:
                    URL = adresa + 'Navest/0/Stoj/DISP'

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

    widget.ui.combo_vyh.currentIndexChanged.connect(lambda: widget.szz.prestavenieVyh(widget.lastVyh, widget.ui.combo_vyh.currentIndex()))    #prestavenie výmeny    

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