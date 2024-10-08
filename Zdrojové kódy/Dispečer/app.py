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

    odhlaskaLo = False
    odhlaskaSo = False
    predhlaskaZBE = False
    predhlaskaHLO = False

    def __init__(self, app_instance):
        self.dictUseky ={   #slovník úsekov
            #------------------------------------------LOKALNE-----------------------------------------------------------------------------
            1: Usek(ID=0, nazovGUI='RAD_k1', enummIkon=ico.KolajSt1, dictIkon=ico.dictStanKolaj1, app=app_instance),
            2: Usek(ID=1, nazovGUI='RAD_k2', enummIkon=ico.KolajSt2, dictIkon=ico.dictStanKolaj2, app=app_instance),
            3: Vyhybka(ID=2, IDsmer=0, nazovGUI='RAD_V1', usek='RAD_v1' , enumIkon=ico.VyhP, dictIkon=ico.dictVyhP, zavisla=31, app=app_instance),
            4: Usek(ID=3, nazovGUI='RAD_Sk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            5: Usek(ID=4, nazovGUI='RAD_ZBE_TU1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            6: Usek(ID=5, nazovGUI='RAD_ZBE_TU2_1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            7: Usek(ID=5, nazovGUI='RAD_ZBE_TU2_2', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            8: Usek(ID=6, nazovGUI='RAD_ZBE_TU3', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),  
            9: Usek(ID=7, nazovGUI='RAD_ZBE_TU4', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),            
            10: Usek(ID=0, nazovGUI='ZBE_Lk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            11: Usek(ID=1, nazovGUI='ZBE_BLk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            12: Vyhybka(ID=2, IDsmer=1, nazovGUI='ZBE_V1', usek='ZBE_v1', spojka=True, enumIkon=ico.SpojkaA, dictIkon=ico.dictSpojkaA, zavisla=40, app=app_instance),
            13: Vyhybka(ID=3, IDsmer=1, nazovGUI='ZBE_V2', usek='ZBE_v2', spojka=True, enumIkon=ico.SpojkaB, dictIkon=ico.dictSpojkaB, zavisla=41, app=app_instance),
            14: Usek(ID=4, nazovGUI='ZBE_k1', enummIkon=ico.KolajSt1, dictIkon=ico.dictStanKolaj1, app=app_instance),
            15: Usek(ID=5, nazovGUI='ZBE_k2', enummIkon=ico.KolajSt2, dictIkon=ico.dictStanKolaj2, app=app_instance),
            16: Vyhybka(ID=6, IDsmer=2, nazovGUI='ZBE_V3', usek='ZBE_v3', enumIkon=ico.VyhP, dictIkon=ico.dictVyhP, zavisla=44, app=app_instance),
            17: Usek(ID=7, nazovGUI='ZBE_Sk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),            
            18: Usek(ID=6, nazovGUI='ZBE_HLO_TU1_1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            19: Usek(ID=7, nazovGUI='ZBE_HLO_TU2_a', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            20: Usek(ID=7, nazovGUI='ZBE_HLO_TU2_b', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            21: Usek(ID=100, nazovGUI='LUZ_ZBE_TU1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            22: Usek(ID=6, nazovGUI='H_ZBE_HLO_TU1_1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            23: Usek(ID=7, nazovGUI='H_ZBE_HLO_TU2_a', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            24: Usek(ID=7, nazovGUI='H_ZBE_HLO_TU2_b', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            25: Usek(ID=0, nazovGUI='HLO_Sk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            26: Vyhybka(ID=1, IDsmer=3, nazovGUI='HLO_V1', usek='HLO_v1' , enumIkon=ico.VyhL, dictIkon=ico.dictVyhL, zavisla=54, app=app_instance),
            27: Usek(ID=2, nazovGUI='HLO_k1', enummIkon=ico.KolajSt1, dictIkon=ico.dictStanKolaj1, app=app_instance),
            28: Usek(ID=3, nazovGUI='HLO_k2', enummIkon=ico.KolajSt2, dictIkon=ico.dictStanKolaj2, app=app_instance),
            #------------------------------------------DISPECER-----------------------------------------------------------------------------
            29: Usek(ID=0, nazovGUI='DISP_RAD_k1', enummIkon=ico.KolajSt1, dictIkon=ico.dictStanKolaj1, app=app_instance),
            30: Usek(ID=1, nazovGUI='DISP_RAD_k2', enummIkon=ico.KolajSt2, dictIkon=ico.dictStanKolaj2, app=app_instance),
            31: Vyhybka(ID=2, IDsmer=0, nazovGUI='DISP_RAD_V1', usek='DISP_RAD_v1' , enumIkon=ico.VyhP, dictIkon=ico.dictVyhP, zavisla=3, app=app_instance),
            32: Usek(ID=3, nazovGUI='DISP_RAD_Sk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            33: Usek(ID=4, nazovGUI='DISP_RAD_ZBE_TU1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            34: Usek(ID=5, nazovGUI='DISP_RAD_ZBE_TU2a', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            35: Usek(ID=5, nazovGUI='DISP_RAD_ZBE_TU2b', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            36: Usek(ID=6, nazovGUI='DISP_RAD_ZBE_TU3', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),  
            37: Usek(ID=7, nazovGUI='DISP_RAD_ZBE_TU4', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),            
            38: Usek(ID=0, nazovGUI='DISP_ZBE_Lk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            39: Usek(ID=1, nazovGUI='DISP_ZBE_BLk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            40: Vyhybka(ID=2, IDsmer=1, nazovGUI='DISP_ZBE_V1', usek='DISP_ZBE_v1', spojka=True, enumIkon=ico.SpojkaA, dictIkon=ico.dictSpojkaA, zavisla=12, app=app_instance),
            41: Vyhybka(ID=3, IDsmer=1, nazovGUI='DISP_ZBE_V2', usek='DISP_ZBE_v2', spojka=True, enumIkon=ico.SpojkaB, dictIkon=ico.dictSpojkaB, zavisla=13, app=app_instance),
            42: Usek(ID=4, nazovGUI='DISP_ZBE_k1', enummIkon=ico.KolajSt1, dictIkon=ico.dictStanKolaj1, app=app_instance),
            43: Usek(ID=5, nazovGUI='DISP_ZBE_k2', enummIkon=ico.KolajSt2, dictIkon=ico.dictStanKolaj2, app=app_instance),
            44: Vyhybka(ID=6, IDsmer=2, nazovGUI='DISP_ZBE_V3', usek='DISP_ZBE_v3', enumIkon=ico.VyhP, dictIkon=ico.dictVyhP, zavisla=16, app=app_instance),
            45: Usek(ID=7, nazovGUI='DISP_ZBE_Sk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),            
            46: Usek(ID=6, nazovGUI='DISP_ZBE_HLO_TU1_1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            47: Usek(ID=6, nazovGUI='DISP_ZBE_HLO_TU1_2', enummIkon=ico.Kolaj45, dictIkon=ico.dictKolaj45, app=app_instance),
            48: Usek(ID=6, nazovGUI='DISP_ZBE_HLO_TU1_3', enummIkon=ico.Kolaj45, dictIkon=ico.dictKolaj45, app=app_instance),
            49: Usek(ID=6, nazovGUI='DISP_ZBE_HLO_TU1_4', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            50: Usek(ID=7, nazovGUI='DISP_ZBE_HLO_TU2_a', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            51: Usek(ID=7, nazovGUI='DISP_ZBE_HLO_TU2_b', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            52: Usek(ID=101, nazovGUI='DISP_LUZ_ZBE_TU1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            53: Usek(ID=0, nazovGUI='DISP_HLO_Sk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            54: Vyhybka(ID=1, IDsmer=3, nazovGUI='DISP_HLO_V1', usek='DISP_HLO_v1' , enumIkon=ico.VyhL, dictIkon=ico.dictVyhL, zavisla=26, app=app_instance),
            55: Usek(ID=2, nazovGUI='DISP_HLO_k1', enummIkon=ico.KolajSt1, dictIkon=ico.dictStanKolaj1, app=app_instance),
            56: Usek(ID=3, nazovGUI='DISP_HLO_k2', enummIkon=ico.KolajSt2, dictIkon=ico.dictStanKolaj2, app=app_instance),
        }

        self.dictTS = { #slovník traťových súhlasov
            1: TratSuhlas(ID=1, nazovGUI='RAD_trat_suhlas_doZ', enumIkon=ico.TrSP, dictIkon=ico.dictTrSP, app=app_instance, typ='L'),
            2: TratSuhlas(ID=2, nazovGUI='ZBE_trat_suhlas_doR', enumIkon=ico.TrSL, dictIkon=ico.dictTrSL, app=app_instance, typ='S'),
            3: TratSuhlas(ID=3, nazovGUI='ZBE_trat_suhlas_doH', enumIkon=ico.TrSP, dictIkon=ico.dictTrSP, app=app_instance, typ='L'),
            4: TratSuhlas(ID=4, nazovGUI='ZBE_trat_suhlas_doL', enumIkon=ico.TrSL, dictIkon=ico.dictTrSL, app=app_instance, typ='L'),
            5: TratSuhlas(ID=5, nazovGUI='HLO_trat_suhlas_doZ', enumIkon=ico.TrSL, dictIkon=ico.dictTrSL, app=app_instance, typ='S'),
            6: TratSuhlas(ID=1, nazovGUI='DISP_RAD_trat_suhlas_doZ', enumIkon=ico.TrSP, dictIkon=ico.dictTrSP, app=app_instance, typ='L'),
            7: TratSuhlas(ID=2, nazovGUI='DISP_ZBE_trat_suhlas_doR', enumIkon=ico.TrSL, dictIkon=ico.dictTrSL, app=app_instance, typ='S'),
            8: TratSuhlas(ID=3, nazovGUI='DISP_ZBE_trat_suhlas_doH', enumIkon=ico.TrSP, dictIkon=ico.dictTrSP, app=app_instance, typ='L'),
            9: TratSuhlas(ID=4, nazovGUI='DISP_ZBE_trat_suhlas_doL', enumIkon=ico.TrSL, dictIkon=ico.dictTrSL, app=app_instance, typ='L'),
            10: TratSuhlas(ID=5, nazovGUI='DISP_HLO_trat_suhlas_doZ', enumIkon=ico.TrSL, dictIkon=ico.dictTrSL, app=app_instance, typ='S')
        }

        self.dictPriecestie = { #slovník priecestí
            1:Priecestie(ID=1, nazovGUI='RAD_ZBE_priec', enumIkon=ico.Priecestie, dictIkon=ico.dictPriecestie, app=app_instance),
            2:Priecestie(ID=2, nazovGUI='H_ZBE_HLO_priec', enumIkon=ico.Priecestie, dictIkon=ico.dictPriecestie, app=app_instance),
            3:Priecestie(ID=3, nazovGUI='DISP_RAD_ZBE_priec', enumIkon=ico.Priecestie, dictIkon=ico.dictPriecestie, app=app_instance),
            4:Priecestie(ID=4, nazovGUI='DISP_ZBE_HLO_priec', enumIkon=ico.Priecestie, dictIkon=ico.dictPriecestie, app=app_instance),
            5:Priecestie(ID=5, nazovGUI='ZBE_HLO_priec', enumIkon=ico.Priecestie, dictIkon=ico.dictPriecestie, app=app_instance),
        } 

        self.dictStanice = {    #slovník stníc
            1:RiadenieObsluhy(ID=1, nazovGUI='RAD_dialkove', enumIkon=ico.RiadenieRAD, dictIkon=ico.dictRiadenieRAD, app=app_instance),
            2:RiadenieObsluhy(ID=2, nazovGUI='ZBE_dialkove', enumIkon=ico.RiadenieZBE, dictIkon=ico.dictRiadenieZBE, app=app_instance),
            3:RiadenieObsluhy(ID=3, nazovGUI='HLO_dialkove', enumIkon=ico.RiadenieHLO, dictIkon=ico.dictRiadenieHLO, app=app_instance),
            4:RiadenieObsluhy(ID=4, nazovGUI='DISP_RAD_dialkove', enumIkon=ico.RiadenieRAD, dictIkon=ico.dictRiadenieRAD, app=app_instance),
            5:RiadenieObsluhy(ID=5, nazovGUI='DISP_ZBE_dialkove', enumIkon=ico.RiadenieZBE, dictIkon=ico.dictRiadenieZBE, app=app_instance),
            6:RiadenieObsluhy(ID=6, nazovGUI='DISP_HLO_dialkove', enumIkon=ico.RiadenieHLO, dictIkon=ico.dictRiadenieHLO, app=app_instance),
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
                    if index in list(range(1,10)) + list(range(29,38)):
                        self.dictUseky[index].jeVolny = data['RAD;RAD-ZBE'][self.dictUseky[index].ID]

                    elif index in list(range(10,18)) + list(range(38,46)):
                        self.dictUseky[index].jeVolny = data['ZBE'][self.dictUseky[index].ID]

                    elif index in list(range(18,21)) + list(range(22,25)) + list(range(46,52)):
                        self.dictUseky[index].jeVolny = data['P1;P2;ZBE-HLO'][self.dictUseky[index].ID]

                    elif index in list(range(25,29)) + list(range(53,57)):
                        self.dictUseky[index].jeVolny = data['HLO'][self.dictUseky[index].ID]

                    elif index in [21,52]:  #špeciálny prípad kedy sa dopytuje aj na LifeSigh ESA 44
                        if data['ZbeLuz'] is None:
                            self.dictUseky[index].odozva = False
                        else:
                            self.dictUseky[index].odozva = True
                            self.dictUseky[index].jeVolny = data['ZbeLuz']

                    if index in [3,31]: #čítanie smeru výmen
                        self.dictUseky[index].smer = data['SmerVyh'][self.dictUseky[index].IDsmer]
                    
                    elif index in [12,13,16,40,41,44]:
                        self.dictUseky[index].smer = data['SmerVyh'][self.dictUseky[index].IDsmer]
                    
                    elif index in [26,54]:
                        self.dictUseky[index].smer = data['SmerVyh'][self.dictUseky[index].IDsmer]

                for index in self.dictTS.keys():    #čítanie stavov traťových súhlasov
                    if index in [1,6]:
                        self.dictTS[index].smer = data['TS']['smerRZ'] 
                        self.dictTS[index].ziadost = data['TS']['ZUS_RZ']                   
                        self.dictTS[index].volnost = data['TS']['volRZ']  

                    elif index in [2,7]:
                        self.dictTS[index].smer = data['TS']['smerRZ'] 
                        self.dictTS[index].ziadost = data['TS']['ZUS_RZ']                   
                        self.dictTS[index].volnost = data['TS']['volRZ']

                    elif index in [3,8]:
                        self.dictTS[index].smer = data['TS']['smerZH']                    
                        self.dictTS[index].volnost = data['TS']['volZH']
                        MyOdchod = data['TS']['odchodZH']
                        HradloOdchod = data['TS']['predhlSo']
                        self.dictTS[index].odchod = MyOdchod or HradloOdchod

                    elif index in [4,9]:
                        self.dictTS[index].smer = data['TS']['smerLZ']  
                        ZUS_ZBE = data['TS']['ZUS_LZ']
                        ZTS_LUZ = data['TS']['ZTS_L']
                        self.dictTS[index].ziadost = ZUS_ZBE or ZTS_LUZ                  
                        self.dictTS[index].volnost = data['TS']['volLZ']
                        self.dictTS[index].porBP = data['TS']['ziadZBP']
                        MyOdchod = data['TS']['odchodZL']
                        SusOdchod = data['TS']['odchodL']
                        self.dictTS[index].odchod = MyOdchod or SusOdchod

                    elif index in [5,10]:
                        self.dictTS[index].smer = data['TS']['smerZH'] 
                        self.dictTS[index].volnost = data['TS']['volZH']
                        MyOdchod = data['TS']['odchodH']
                        HradloOdchod = data['TS']['predhlLo']
                        self.dictTS[index].odchod = MyOdchod or HradloOdchod

                for index in self.dictPriecestie.keys():    #čítanie stavov priecestí
                    if index in [1,3]:
                        self.dictPriecestie[index].predzvananie = data['Priecestie'][4]
                        self.dictPriecestie[index].otvorene = data['Priecestie'][2]
                        self.dictPriecestie[index].zatvorene = data['Priecestie'][3]
                        self.dictPriecestie[index].jeVolny = self.dictUseky[6].jeVolny

                    elif index in [2,4,5]:
                        self.dictPriecestie[index].predzvananie = data['Priecestie'][7]
                        self.dictPriecestie[index].otvorene = data['Priecestie'][5]
                        self.dictPriecestie[index].zatvorene = data['Priecestie'][6]
                        self.dictPriecestie[index].jeVolny = self.dictUseky[23].jeVolny 

                for index in self.dictStanice.keys():   #čítanie stavov riadenia staníc
                    if index in [1,4]:
                        self.dictStanice[index].dialkove = data['Riadenie']['dialkoveRAD']
                        self.dictStanice[index].ziadost = data['Riadenie']['ziadostRAD']

                    elif index in [2,5]:
                        self.dictStanice[index].dialkove = data['Riadenie']['dialkoveZBE']
                        self.dictStanice[index].ziadost = data['Riadenie']['ziadostZBE']

                    elif index in [3,6]:
                        self.dictStanice[index].dialkove = data['Riadenie']['dialkoveHLO']
                        self.dictStanice[index].ziadost = data['Riadenie']['ziadostHLO']

                self.odhlaskaLo = data['TS']['odhlLo']  #čítanie dát z hradla Rišňovce
                self.odhlaskaSo = data['TS']['odhlSo'] 

                self.predhlaskaZBE = data['TS']['odchodZH'] #čítanie predhlášok zo staníc
                self.predhlaskaHLO = data['TS']['odchodH']

                if data['Cesta']['stavanie']:
                    if (data['Cesta']['pociatocne'] in self.app_instance.dictNav.keys() and data['Cesta']['koncove'] in self.app_instance.dictNav.keys()) and (
                    data['Cesta']['odosielatel'] != 'DISP'):
                        self.app_instance.Start = data['Cesta']['pociatocne']
                        self.app_instance.dictNav[self.app_instance.Start].pociatocne = True
                        self.app_instance.End = data['Cesta']['koncove']
                        self.app_instance.szz.typCesty = data['Cesta']['typCesty']
                        ochr = data['Cesta']['OD']
                        self.app_instance.szz.stavanieCesty(Disp=True, OD=ochr, server=True)
                        self.app_instance.prikazDoPLC(cesta=True)

                if data['Cesta']['rusenie']:
                    if data['Cesta']['koncove'] in self.app_instance.dictNav.keys() and data['Cesta']['odosielatel'] != 'DISP':
                        self.app_instance.End = data['Cesta']['koncove']
                        self.app_instance.szz.rusenieCesty(Disp=True, server=True)
                        self.app_instance.prikazDoPLC(cesta=True)

                if data['Navest']['ID'] != 0 and data['Navest']['ID'] in self.app_instance.dictNav.keys() and data['Navest']['odosielatel'] != 'DISP':
                    self.app_instance.dictNav[data['Navest']['ID']].znak = data['Navest']['znak']
                    self.app_instance.dictNav[data['Navest']['ID']].manual = True
                    self.app_instance.dictNav[data['Navest']['ID']].update(self)

                    if self.app_instance.dictNav[data['Navest']['ID']].zavisle != -1:
                        self.app_instance.dictNav[self.app_instance.dictNav[data['Navest']['ID']].zavisle].znak = data['Navest']['znak']
                        self.app_instance.dictNav[self.app_instance.dictNav[data['Navest']['ID']].zavisle].manual = True
                        self.app_instance.dictNav[self.app_instance.dictNav[data['Navest']['ID']].zavisle].update(self)

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
            #------------------------------------------RADOSINA-----------------------------------------------------------------------------
            1: Navestidlo(ID=1, nazov='R_Se1', usekPred='RAD_Sk', usekZa='RAD_V1', nazovGUI='RAD_zr_do_st_odZ', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL,app=self),
            2: Navestidlo(ID=2, nazov='R_Se1p', usekPred='RAD_Sk', nazovGUI='RAD_zr_zo_st_odZ', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=self),
            3: Navestidlo(ID=3, nazov='R_S', usekPred='RAD_ZBE_TU1', usekZa='RAD_Sk', nazovGUI='RAD_S', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=46, app=self),
            4: Navestidlo(ID=4, nazov='R_L1', usekPred='RAD_k1', usekZa='RAD_V1', nazovGUI='RAD_L1', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, zavisle=47, app=self),
            5: Navestidlo(ID=5, nazov='R_L2', usekPred='RAD_k2', usekZa='RAD_V1', nazovGUI='RAD_L2', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, zavisle=48, app=self),
            6: Navestidlo(ID=6, nazov='R_S_fik', usekPred='RAD_Sk', nazovGUI='RAD_fik_S', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, zavisle=49, app=self),
            7: Navestidlo(ID=7, nazov='R_29_fik', usekPred='RAD_ZBE_TU2_2', nazovGUI='RAD_fik_29', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, app=self),
            8: Navestidlo(ID=8, nazov='R_19', usekPred='RAD_ZBE_TU1', usekZa='RAD_ZBE_TU2_1', nazovGUI='RAD_ZBE_19', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self, oddielove=True, TZZ='AB3'),
            9: Navestidlo(ID=9, nazov='R_18', usekPred='RAD_ZBE_TU2_1', usekZa='RAD_ZBE_TU1', nazovGUI='RAD_ZBE_18', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self, oddielove=True, TZZ='AB3'),
            10: Navestidlo(ID=10, nazov='R_k1_fik', usekPred='RAD_k1', nazovGUI='RAD_k1_fik', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, zavisle=50, app=self),
            11: Navestidlo(ID=11, nazov='R_k2_fik', usekPred='RAD_k2', nazovGUI='RAD_k2_fik', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, zavisle=51, app=self),
            #------------------------------------------ZBEHY-----------------------------------------------------------------------------
            12: Navestidlo(ID=12, nazov='Z_L', usekPred='RAD_ZBE_TU4', usekZa='ZBE_Lk', nazovGUI='ZBE_L', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=58, app=self),
            13: Navestidlo(ID=13, nazov='Z_BL', usekPred='LUZ_ZBE_TU1', usekZa='ZBE_BLk', nazovGUI='ZBE_BL', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=59, app=self),
            14: Navestidlo(ID=14, nazov='Z_L_fik', usekPred='ZBE_Lk', nazovGUI='ZBE_fik_L', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, zavisle=60, app=self),
            15: Navestidlo(ID=15, nazov='Z_BL_fik', usekPred='ZBE_BLk', nazovGUI='ZBE_fik_BL', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, zavisle=61, app=self),
            16: Navestidlo(ID=16, nazov='Z_Se1p', usekPred='ZBE_Lk', nazovGUI='ZBE_zr_zo_st_odR', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL, app=self),
            17: Navestidlo(ID=17, nazov='Z_Se2p', usekPred='ZBE_BLk', nazovGUI='ZBE_zr_zo_st_odL', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL, app=self),
            18: Navestidlo(ID=18, nazov='Z_Se1', usekPred='ZBE_Lk', usekZa='ZBE_V1', nazovGUI='ZBE_zr_do_st_odR', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=self),
            19: Navestidlo(ID=19, nazov='Z_Se2', usekPred='ZBE_BLk', usekZa='ZBE_V2', nazovGUI='ZBE_zr_do_st_odL', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=self),
            20: Navestidlo(ID=20, nazov='Z_S1', usekPred='ZBE_k1', usekZa='ZBE_V1', nazovGUI='ZBE_S1', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, zavisle=62, app=self),
            21: Navestidlo(ID=21, nazov='Z_S2', usekPred='ZBE_k2', usekZa='ZBE_V2', nazovGUI='ZBE_S2', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, zavisle=63, app=self),
            22: Navestidlo(ID=22, nazov='Z_L1', usekPred='ZBE_k1', usekZa='ZBE_V3', nazovGUI='ZBE_L1', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, zavisle=64, app=self),
            23: Navestidlo(ID=23, nazov='Z_L2', usekPred='ZBE_k2', usekZa='ZBE_V3', nazovGUI='ZBE_L2', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, zavisle=65, app=self),
            24: Navestidlo(ID=24, nazov='Z_Se3', usekPred='ZBE_Sk', usekZa='ZBE_V3', nazovGUI='ZBE_zr_do_st_odH', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL, app=self),
            25: Navestidlo(ID=25, nazov='Z_Se3p', usekPred='ZBE_Sk', nazovGUI='ZBE_zr_zo_st_odH', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=self),
            26: Navestidlo(ID=26, nazov='Z_S_fik', usekPred='ZBE_Sk', nazovGUI='ZBE_fik_S', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, zavisle=66, app=self),
            27: Navestidlo(ID=27, nazov='Z_S', usekPred='ZBE_HLO_TU1_1', usekZa='ZBE_Sk', nazovGUI='ZBE_S', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=67, app=self),
            28: Navestidlo(ID=28, nazov='Z_RAD_ZBE_40', usekPred='RAD_ZBE_TU4', usekZa='RAD_ZBE_TU3', nazovGUI='RAD_ZBE_40', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self, oddielove=True, TZZ='AB3'),
            29: Navestidlo(ID=29, nazov='Z_RAD_ZBE_39', usekPred='RAD_ZBE_TU3', usekZa='RAD_ZBE_TU4', nazovGUI='RAD_ZBE_39', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self, oddielove=True, TZZ='AB3'),
            30: Navestidlo(ID=30, nazov='Z_Lo', usekPred='ZBE_HLO_TU1_1', usekZa='ZBE_HLO_TU2_a', nazovGUI='ZBE_HLO_Lo', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=69, app=self, oddielove=True, TZZ='AH'),
            31: Navestidlo(ID=31, nazov='Z_So', usekPred='ZBE_HLO_TU2_a', usekZa='ZBE_HLO_TU1_1', nazovGUI='ZBE_HLO_So', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=70, app=self, oddielove=True, TZZ='AH'),
            32: Navestidlo(ID=32, nazov='Z_28_fik', usekPred='RAD_ZBE_TU3', nazovGUI='RAD_ZBE_fik_28', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            33: Navestidlo(ID=33, nazov='Z_BS_fik', usekPred='LUZ_ZBE_TU1', nazovGUI='LUZ_fik_BS', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            34: Navestidlo(ID=34, nazov='Z_HLO_L_fik', usekPred='ZBE_HLO_TU2_b', nazovGUI='Z_HLO_fikL', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, app=self),
            #------------------------------------------HLOHOVEC-----------------------------------------------------------------------------
            35: Navestidlo(ID=35, nazov='H_Se1', usekPred='HLO_Sk', usekZa='HLO_V1', nazovGUI='HLO_zr_do_st_odZ', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=self),
            36: Navestidlo(ID=36, nazov='H_Se1p', usekPred='HLO_Sk', nazovGUI='HLO_zr_zo_st_odZ', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL, app=self),
            37: Navestidlo(ID=37, nazov='H_L', usekPred='ZBE_HLO_TU2_b', usekZa='HLO_Sk', nazovGUI='HLO_L', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=71, app=self),
            38: Navestidlo(ID=38, nazov='H_S1', usekPred='HLO_k1', usekZa='HLO_V1', nazovGUI='HLO_S1', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, zavisle=72, app=self),
            39: Navestidlo(ID=39, nazov='H_S2', usekPred='HLO_k2', usekZa='HLO_V1', nazovGUI='HLO_S2', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, zavisle=73, app=self),
            40: Navestidlo(ID=40, nazov='H_L_fik', usekPred='HLO_Sk', nazovGUI='HLO_fik_L', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, zavisle=74, app=self),
            41: Navestidlo(ID=41, nazov='H_ZBE_L_fik', usekPred='ZBE_HLO_TU1_1', nazovGUI='H_ZBE_fik_S', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            42: Navestidlo(ID=42, nazov='H_k1_fik', usekPred='HLO_k1', nazovGUI='HLO_k1_fik', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, zavisle=76, app=self),
            43: Navestidlo(ID=43, nazov='H_k2_fik', usekPred='HLO_k2', nazovGUI='HLO_k2_fik', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, zavisle=77, app=self),
            44: Navestidlo(ID=44, nazov='H_Lo', usekPred='H_ZBE_HLO_TU1_1', usekZa='H_ZBE_HLO_TU2_a', nazovGUI='H_ZBE_HLO_Lo', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=69, app=self, oddielove=True, TZZ='AH'),
            45: Navestidlo(ID=45, nazov='H_So', usekPred='H_ZBE_HLO_TU2_a', usekZa='H_ZBE_HLO_TU1_1', nazovGUI='H_ZBE_HLO_So', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=70, app=self, oddielove=True, TZZ='AH'),
            #------------------------------------------DISPECER-----------------------------------------------------------------------------
            #------------------------------------------RADOSINA-----------------------------------------------------------------------------
            46: Navestidlo(ID=46, nazov='DR_S', usekPred='DISP_RAD_ZBE_TU1', usekZa='DISP_RAD_Sk', nazovGUI='DISP_RAD_S', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=3, app=self),
            47: Navestidlo(ID=47, nazov='DR_L1', usekPred='DISP_RAD_k1', usekZa='DISP_RAD_V1', nazovGUI='DISP_RAD_L1', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=4, app=self),
            48: Navestidlo(ID=48, nazov='DR_L2', usekPred='DISP_RAD_k2', usekZa='DISP_RAD_V1', nazovGUI='DISP_RAD_L2', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=5, app=self),
            49: Navestidlo(ID=49, nazov='DR_S_fik', usekPred='DISP_RAD_Sk', nazovGUI='DISP_RAD_fik_S', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, zavisle=6, app=self),
            50: Navestidlo(ID=50, nazov='DR_k1_fik', usekPred='DISP_RAD_k1', nazovGUI='DISP_RAD_k1_fik', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=10, app=self),
            51: Navestidlo(ID=51, nazov='DR_k2_fik', usekPred='DISP_RAD_k2', nazovGUI='DISP_RAD_k2_fik', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=11, app=self),
            52: Navestidlo(ID=52, nazov='DR_19', usekPred='DISP_RAD_ZBE_TU1', usekZa='DISP_RAD_ZBE_TU2a', nazovGUI='DISP_RAD_ZBE_19', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self, oddielove=True, TZZ='AB3'),
            53: Navestidlo(ID=53, nazov='DR_18', usekPred='DISP_RAD_ZBE_TU2a', usekZa='DISP_RAD_ZBE_TU1', nazovGUI='DISP_RAD_ZBE_18', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self, oddielove=True, TZZ='AB3'),
            54: Navestidlo(ID=54, nazov='DR_29', usekPred='DISP_RAD_ZBE_TU2b', usekZa='DISP_RAD_ZBE_TU3', nazovGUI='DISP_RAD_ZBE_29', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self, oddielove=True, TZZ='AB3'),
            55: Navestidlo(ID=55, nazov='DR_28', usekPred='DISP_RAD_ZBE_TU3', usekZa='DISP_RAD_ZBE_TU2b', nazovGUI='DISP_RAD_ZBE_28', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self, oddielove=True, TZZ='AB3'),
            #------------------------------------------ZBEHY-----------------------------------------------------------------------------
            56: Navestidlo(ID=56, nazov='DZ_RAD_ZBE_40', usekPred='DISP_RAD_ZBE_TU4', usekZa='DISP_RAD_ZBE_TU3', nazovGUI='DISP_RAD_ZBE_40', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self, oddielove=True, TZZ='AB3'),
            57: Navestidlo(ID=57, nazov='DZ_RAD_ZBE_39', usekPred='DISP_RAD_ZBE_TU3', usekZa='DISP_RAD_ZBE_TU4', nazovGUI='DISP_RAD_ZBE_39', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self, oddielove=True, TZZ='AB3'),
            58: Navestidlo(ID=58, nazov='DZ_L', usekPred='DISP_RAD_ZBE_TU4', usekZa='DISP_ZBE_Lk', nazovGUI='DISP_ZBE_L', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=12, app=self),
            59: Navestidlo(ID=59, nazov='DZ_BL', usekPred='DISP_LUZ_ZBE_TU1', usekZa='DISP_ZBE_BLk', nazovGUI='DISP_ZBE_BL', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=13, app=self),
            60: Navestidlo(ID=60, nazov='DZ_L_fik', usekPred='DISP_ZBE_Lk', nazovGUI='DISP_ZBE_fik_L', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, zavisle=14, app=self),
            61: Navestidlo(ID=61, nazov='DZ_BL_fik', usekPred='DISP_ZBE_BLk', nazovGUI='DISP_ZBE_fik_BL', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, zavisle=15, app=self),
            62: Navestidlo(ID=62, nazov='DZ_S1', usekPred='DISP_ZBE_k1', usekZa='DISP_ZBE_V1', nazovGUI='DISP_ZBE_S1', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=20, app=self),
            63: Navestidlo(ID=63, nazov='DZ_S2', usekPred='DISP_ZBE_k2', usekZa='DISP_ZBE_V2', nazovGUI='DISP_ZBE_S2', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=21, app=self),
            64: Navestidlo(ID=64, nazov='DZ_L1', usekPred='DISP_ZBE_k1', usekZa='DISP_ZBE_V3', nazovGUI='DISP_ZBE_L1', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=22, app=self),
            65: Navestidlo(ID=65, nazov='DZ_L2', usekPred='DISP_ZBE_k2', usekZa='DISP_ZBE_V3', nazovGUI='DISP_ZBE_L2', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=23, app=self),
            66: Navestidlo(ID=66, nazov='DZ_S_fik', usekPred='DISP_ZBE_Sk', nazovGUI='DISP_ZBE_fik_S', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, zavisle=26, app=self),
            67: Navestidlo(ID=67, nazov='DZ_S', usekPred='DISP_ZBE_HLO_TU1_1', usekZa='ZBE_Sk', nazovGUI='DISP_ZBE_S', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=27, app=self),
            68: Navestidlo(ID=68, nazov='DZ_BS_fik', usekPred='DISP_LUZ_ZBE_TU1', nazovGUI='DISP_LUZ_fik_BS', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            69: Navestidlo(ID=69, nazov='DH_Lo', usekPred='DISP_ZBE_HLO_TU1_4', usekZa='DISP_ZBE_HLO_TU2_a', nazovGUI='DISP_ZBE_HLO_Lo', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=30, app=self, oddielove=True, TZZ='AH'),
            #------------------------------------------HLOHOVEC-----------------------------------------------------------------------------
            70: Navestidlo(ID=70, nazov='DH_So', usekPred='DISP_ZBE_HLO_TU2_a', usekZa='DISP_ZBE_HLO_TU1_4', nazovGUI='DISP_ZBE_HLO_So', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=45, app=self, oddielove=True, TZZ='AH'),
            71: Navestidlo(ID=71, nazov='DH_L', usekPred='DISP_ZBE_HLO_TU2_b', usekZa='DISP_HLO_Sk', nazovGUI='DISP_HLO_L', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=37, app=self),
            72: Navestidlo(ID=72, nazov='DH_S1', usekPred='DISP_HLO_k1', usekZa='DISP_HLO_V1', nazovGUI='DISP_HLO_S1', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=38, app=self),
            73: Navestidlo(ID=73, nazov='DH_S2', usekPred='DISP_HLO_k2', usekZa='DISP_HLO_V1', nazovGUI='DISP_HLO_S2', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=39, app=self),
            74: Navestidlo(ID=74, nazov='DH_L_fik', usekPred='DISP_HLO_Sk', nazovGUI='DISP_HLO_fik_L', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, zavisle=40, app=self),
            75: Navestidlo(ID=75, nazov='DH_ZBE_S_fik', usekPred='DISP_ZBE_HLO_TU1_1', nazovGUI='H_ZBE_fik_S', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            76: Navestidlo(ID=76, nazov='DH_k1_fik', usekPred='DISP_HLO_k1', nazovGUI='DISP_HLO_k1_fik', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=42, app=self),
            77: Navestidlo(ID=77, nazov='DH_k2_fik', usekPred='DISP_HLO_k2', nazovGUI='DISP_HLO_k2_fik', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, zavisle=43, app=self),
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

        self.workerThread.dataUpdated.connect(self.update) #definícia prepojenia vláken a metód
        self.workerThread.dataUpdated.connect(lambda: self.szz.stavanieCesty(True, Disp=True))

        self.workerThreadDateTime.dataUpdated.connect(self.aktualizaciaCasu)
        
        self.workerThreadTimeVlak.finished.connect(lambda: self.szz.rusenieCesty(True))
        self.workerThreadTimePosun.finished.connect(lambda: self.szz.rusenieCesty(True))
        self.workerThreadTimeOD.finished.connect(lambda: self.szz.rusenieOD(Disp=True))

        self.workerThread.setParent(self)  #definovanie rosičovského objektu pre vlákna
        self.workerThreadLifeSign.setParent(self)

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

            self.ui.RAD_ASVC.setIcon(ico.icon_ASVC_vypnute)
            self.ui.DISP_RAD_ASVC.setIcon(ico.icon_ASVC_vypnute)
            self.ui.ZBE_ASVC.setIcon(ico.icon_ASVC_vypnute)
            self.ui.DISP_ZBE_ASVC.setIcon(ico.icon_ASVC_vypnute)
            self.ui.HLO_ASVC.setIcon(ico.icon_ASVC_vypnute)
            self.ui.DISP_HLO_ASVC.setIcon(ico.icon_ASVC_vypnute)

    def ukonciPripojenie(self): #metóda pre zastavenie vláken a ukončenie komunikácie
        self.workerThread.requestInterruption()    
        self.workerThreadTimeVlak.requestInterruption()
        self.workerThreadTimePosun.requestInterruption()
        self.workerThreadTimeOD.requestInterruption()  
        self.workerThreadLifeSign.requestInterruption()  
        self.workerThreadDateTime.requestInterruption()  

        self.ui.textChybaREST.show()
        self.ui.textChybaESA.show()  

    def aktualizaciaCasu(self, cas):    #metóda pre aktualizáciu času v GUI
        self.ui.DateTime.setText(cas)

    def update(self, ID = -1, clicked=False, objekt='update'): #metóda pre aktualizáciu symbolov objektov
        if objekt in ['update', 'useky']:   #aktualizácia úsekov
            for i in self.workerThread.dictUseky.keys():
                self.workerThread.dictUseky[i].update(self)
                
                if self.workerThread.dictUseky[21].odozva:
                    self.ui.textChybaESA.hide()
                
                else:
                    self.ui.textChybaESA.show()

        if objekt in ['update', 'navestidla']:  #aktualizácia návestidiel
            self.dictNav[8].zhasnute =  self.workerThread.dictTS[1].smer  #otáčanie svietenia AB podľa TS
            self.dictNav[9].zhasnute =  not self.workerThread.dictTS[1].smer
            self.dictNav[52].zhasnute =  self.workerThread.dictTS[1].smer  
            self.dictNav[53].zhasnute =  not self.workerThread.dictTS[1].smer

            self.dictNav[55].zhasnute =  not self.workerThread.dictTS[2].smer  
            self.dictNav[54].zhasnute =  self.workerThread.dictTS[2].smer

            self.dictNav[28].zhasnute =  not self.workerThread.dictTS[2].smer  
            self.dictNav[29].zhasnute =  self.workerThread.dictTS[2].smer
            self.dictNav[57].zhasnute =  self.workerThread.dictTS[2].smer  
            self.dictNav[56].zhasnute =  not self.workerThread.dictTS[2].smer

            for nav in [30,44,69]:
                self.dictNav[nav].predhlaska = self.workerThread.predhlaskaZBE

            for nav in [31,45,70]:
                self.dictNav[nav].predhlaska = self.workerThread.predhlaskaHLO

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
            if (id in [3,46,47,48,50,51] and self.workerThread.dictStanice[1].dialkove) or (    #ak má precovisko aktívne riadenie   
            id in [12,13,27,58,59,62,63,64,65,67] and self.workerThread.dictStanice[2].dialkove) or (
            id in [37,71,72,73,76,77] and self.workerThread.dictStanice[3].dialkove):  #vchodové návestidlo
                self.update(id, True, objekt='navestidla') #aktualizuj symbol návestidla
                if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                    self.comboShowHide('vchodove')
                elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                    self.comboShowHide('vchodove_konc')
                else:
                    self.comboShowHide()

            elif (id in [4,5,10,11] and self.workerThread.dictStanice[1].dialkove) or ( #ak má precovisko aktívne riadenie 
            id in [20,21,22,23]  and self.workerThread.dictStanice[2].dialkove) or (
            id in [38,39,42,43] and self.workerThread.dictStanice[3].dialkove):    #odchodové návestidlo
                self.update(id, True, objekt='navestidla') #aktualizuj symbol návestidla
                if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                    self.comboShowHide('odchodove')
                elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                    self.comboShowHide('odchodove_konc')
                else:
                    self.comboShowHide()

            elif (id in [1,2] and self.workerThread.dictStanice[1].dialkove) or (   #ak má precovisko aktívne riadenie 
            id in [16,17,18,19,24,25] and self.workerThread.dictStanice[2].dialkove) or (
            id in[35,36] and self.workerThread.dictStanice[3].dialkove):  #zriaďovacie návestidlo
                self.update(id, True, objekt='navestidla') #aktualizuj symbol návestidla
                if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                    self.comboShowHide('zriadovacie')
                elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                    self.comboShowHide('zriadovacie_konc')
                else:
                    self.comboShowHide()

            elif (id in [6,49] and self.workerThread.dictStanice[1].dialkove) or (  #ak má precovisko aktívne riadenie 
            id in [14,15,26,60,61,66] and self.workerThread.dictStanice[2].dialkove) or (
            id in [40,74] and self.workerThread.dictStanice[3].dialkove):   #fiktívne návestidlo
                self.update(id, True, objekt='navestidla') #aktualizuj symbol návestidla
                if self.dictNav[id].vybrane and not self.szz.vyberCesty:
                    self.comboShowHide('fiktivne')
                elif self.dictNav[id].vybrane and self.szz.vyberCesty:
                    self.comboShowHide('fiktivne_konc')
                else:
                    self.comboShowHide()

            elif (id in [31,69] and self.workerThread.dictStanice[2].dialkove) or ( #ak má precovisko aktívne riadenie 
            id in [44,70] and self.workerThread.dictStanice[3].dialkove):   #oddielové návestidlo
                self.update(id, True, objekt='navestidla') #aktualizuj symbol návestidla
                if self.dictNav[id].vybrane:
                    self.comboShowHide('oddielove')
                else:
                    self.comboShowHide()
            
            else:
                self.vypisHlasenia('Obsluha stanice prevedená na lokálne pracovisko')

        elif objekt == 'vyhybka':
            if id in self.workerThread.dictUseky:  #ak sa výhybka nachádza v zozname
                self.lastVyh = id   #zapíš ju ako poslednú kliknutú
                if (id in [3,31] and self.workerThread.dictStanice[1].dialkove) or (
                id in [12,13,16,40,41,44] and self.workerThread.dictStanice[2].dialkove) or (
                id in [26,54] and self.workerThread.dictStanice[3].dialkove):   #ak má precovisko aktívne riadenie 
                    if id in [12, 13]:  #úprava pre výhybkovú spojku
                        self.workerThread.dictUseky[12].vyber = not self.workerThread.dictUseky[12].vyber
                        self.workerThread.dictUseky[13].vyber = not self.workerThread.dictUseky[13].vyber
                        self.workerThread.dictUseky[12].update(self)
                        self.workerThread.dictUseky[13].update(self)
                    
                    elif id in [40, 41]:  #úprava pre výhybkovú spojku
                        self.workerThread.dictUseky[40].vyber = not self.workerThread.dictUseky[40].vyber
                        self.workerThread.dictUseky[41].vyber = not self.workerThread.dictUseky[41].vyber
                        self.workerThread.dictUseky[40].update(self)
                        self.workerThread.dictUseky[41].update(self)

                    else:
                        self.workerThread.dictUseky[id].vyber = not self.workerThread.dictUseky[id].vyber
                        self.workerThread.dictUseky[id].update(self)

                    if self.workerThread.dictUseky[id].vyber:  #je výhybka vybraná obsluhou?
                        self.comboShowHide('vyhybka')  #ak áno zobraz kontextové okno akcií
                    else:
                        self.comboShowHide()  #ak nie skry kontextové okno

                else:
                    self.vypisHlasenia('Obsluha stanice prevedená na lokálne pracovisko')

        elif objekt == 'priecestie':
            self.lastPri = id
            if (id in [1,3] and self.workerThread.dictStanice[1].dialkove) or (
            id in [2,4,5] and self.workerThread.dictStanice[3].dialkove):   #ak má precovisko aktívne riadenie 
                self.update(id, True, objekt='priecestie')

                if self.workerThread.dictPriecestie[id].vyber:
                    self.comboShowHide('priecestie')
                else:
                    self.comboShowHide()
            
            else:
                self.vypisHlasenia('Obsluha stanice prevedená na lokálne pracovisko')

        elif objekt == 'TS':
            self.lastTS = id 
            if (id in [1,6] and self.workerThread.dictStanice[1].dialkove) or (
            id in [2,3,4,7,8,9] and self.workerThread.dictStanice[2].dialkove) or (
            id in [5,10] and self.workerThread.dictStanice[3].dialkove):    #ak má precovisko aktívne riadenie 
                if (id in [4,9]) or (id in [1,2,6,7] and (not self.workerThread.dictStanice[1].dialkove or not self.workerThread.dictStanice[2].dialkove)):
                    self.workerThread.dictTS[id].vybrane = not self.workerThread.dictTS[id].vybrane 
                    if self.workerThread.dictTS[id].vybrane:
                        self.comboShowHide('TS_ESA')
                    else:
                        self.comboShowHide()
                elif (id in [3,5,8,10]) or (id in [1,2,6,7] and (self.workerThread.dictStanice[1].dialkove or self.workerThread.dictStanice[2].dialkove)):
                    self.workerThread.dictTS[id].vybrane = not self.workerThread.dictTS[id].vybrane 
                    if self.workerThread.dictTS[id].vybrane:
                        self.comboShowHide('TS_DISP')
                    else:
                        self.comboShowHide()
            else:
                self.vypisHlasenia('Obsluha stanice prevedená na lokálne pracovisko')

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
            self.ui.combo_ciel_hl.hide()
        elif nazov == 'vchodove_konc':    #zobrazí menu pre výber typu cesty pre odchodové návestidlo
            self.ui.combo_ciel_ko.hide()
            self.ui.combo_ciel_fi.hide()   
            self.ui.combo_ciel_zr.hide()
            self.ui.combo_ciel_hl.show()
        elif nazov == 'zriadovacie_konc':    #zobrazí menu pre výber typu cesty pre zriaďovacie návestidlo
            self.ui.combo_ciel_zr.show()
            self.ui.combo_ciel_fi.hide()   
            self.ui.combo_ciel_ko.hide()
            self.ui.combo_ciel_hl.hide()
        elif nazov == 'fiktivne_konc':    #zobrazí menu pre výber typu cesty pre fiktívne návestidlo
            self.ui.combo_ciel_fi.show()    
            self.ui.combo_ciel_ko.hide()
            self.ui.combo_ciel_zr.hide()
            self.ui.combo_ciel_hl.hide()

        elif nazov == 'vyhybka':    #zobrazí menu pre výhybku
            self.ui.combo_vyh.show()

        elif nazov == 'TS_ESA': #zobrazí menu pre traťový súhlas typ 1
            self.ui.combo_TS_ESA.show()
            self.ui.combo_TS_DISP.hide()
            
        elif nazov == 'TS_DISP':    #zobrazí menu pre traťový súhlas typ 2
            self.ui.combo_TS_ESA.hide()
            self.ui.combo_TS_DISP.show()

        elif nazov == 'priecestie': #zobrazí menu pre priecestie
            self.ui.combo_priec.show()

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
            self.ui.combo_ciel_hl.hide()
            self.ui.combo_vyh.hide()
            self.ui.combo_TS_ESA.hide()
            self.ui.combo_TS_DISP.hide()
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

        if ((ID in [1,2]) and index == 1) and (self.lastNav not in [10,11,42,43,50,51,76,77]):  #výber vlakovej cesty
            self.vyberCestu('Vlak')

        elif (ID == 2 and index == 2) or (ID == 3 and index == 1):  #výber posunovej cesty
            if self.lastNav in [1,4,5,18,19,20,21,22,23,24,35,38,39]:
                self.vyberCestu('Posun')

            else:
                self.vypisHlasenia('Nie je možné postaviť posunovú cestu')

        elif (ID == 1 and index == 3) or (ID == 4 and index == 1) or (ID == 2 and index == 4) or (ID == 3 and index == 2):    #rušenie cesty
            self.End = self.lastNav
            self.lastNav = 0

            if ID == 4: #predhlášky od jednotlivých staníc
                if self.End in [6,49]:
                    self.prikazDoPLC(odchod=True, nazov='odchodR', prikaz='/False')
                if self.End in [14,60]:
                    self.prikazDoPLC(odchod=True, nazov='odchodZR', prikaz='/False')
                elif self.End in [15,61]:
                    self.prikazDoPLC(odchod=True, nazov='odchodZL', prikaz='/False')
                elif self.End in [26,66]:
                    self.prikazDoPLC(odchod=True, nazov='odchodZH', prikaz='/False')
                    self.prikazDoPLC(prikaz='/False', nazov='ZBE', predhl=True)
                elif self.End in [40,74]:
                    self.prikazDoPLC(odchod=True, nazov='odchodH', prikaz='/False')
                    self.prikazDoPLC(prikaz='/False', nazov='HLO', predhl=True)

            if self.End in [26,66]:
                for nav in [30,44,69]:
                    self.dictNav[nav].predhlaska = False

            elif self.End in [40,74]:
                for nav in [31,45,70]:
                    self.dictNav[nav].predhlaska = False

            self.dictNav[self.End].vybrane = False
            self.dictNav[self.End].update(self)
            self.szz.rusenieCesty(Disp=True)

        elif self.Start in [3,12,13,27,37,46,58,59,67,68,71] and ID in [10,12,13] and index == 1: #stavanie vchodovej bez ochrannej dráhy
            if not self.szz.typCesty:
                self.postavCestu()
            else:
                self.vypisHlasenia('Nekorektný typ jazdnej cesty')

        elif ((ID in [10,12,13]) and (index == 2) and (not self.szz.typCesty)): #stavanie vchodovej cesty s ochrannou dráhou
            if self.Start in [12,13,27,58,59,67]:
                self.postavCestu(True)

            else:
                self.vypisHlasenia('Jazdná cesta nemá definovanú ochrannú dráhu')
                self.ukonciStavanie()
            
        elif (self.Start in [4,5,20,21,22,23,38,39,47,48,62,63,64,65,72,73]) and ((ID in [10,12]) and (index == 1) and (not self.szz.typCesty)): #stavanie odchodovej cesty
            if self.Start in [4,5,47,48]:
                if self.workerThread.dictTS[1].prijem:
                    self.postavCestu()
                else:
                    self.ukonciStavanie(TS=True)

            elif self.Start in [20,62]:
                if self.workerThread.dictTS[2].prijem:
                    self.postavCestu()
                else:
                    self.ukonciStavanie(TS=True)
                
            elif self.Start in [21,63]:
                if self.lastNav in [14,60]:                    
                    if self.workerThread.dictTS[2].prijem:
                        self.postavCestu()
                    else:
                        self.ukonciStavanie(TS=True)

                elif self.lastNav in [15,61]:                    
                    if self.workerThread.dictTS[4].volnost: 
                        if self.workerThread.dictTS[4].prijem:
                            self.postavCestu()
                        else:
                            self.ukonciStavanie(TS=True)
                    else:
                        self.ukonciStavanie(volnost=True)

            elif self.Start in [22,23,64,65]:
                if self.workerThread.odhlaskaLo:                    
                    if self.workerThread.dictTS[3].prijem:
                        self.postavCestu()
                    else:
                        self.ukonciStavanie(TS=True)
                else:
                    self.ukonciStavanie(odhl=True)

            elif self.Start in [38,39,72,73]:
                if self.workerThread.odhlaskaSo:
                    if self.workerThread.dictTS[5].prijem:
                        self.postavCestu()
                    else:
                        self.ukonciStavanie(TS=True)
                else:
                    self.ukonciStavanie(odhl=True)

        elif (ID == 10 and index == 3) or (ID == 11 and index == 1):    #stavanie posunovej cesty
            self.postavCestu()

        elif ((ID == 1 and index == 2) or (ID == 2 and index == 3) or (ID == 5 and index == 1)) and (self.lastNav not in [10,11,42,43,50,51,76,77]): #Privolávacia návesť
            self.dictNav[self.lastNav].vybrane = False
            
            if self.dictNav[self.lastNav].znak == 'Stoj':
                self.dictNav[self.lastNav].znak = 'PN'
                self.prikazDoPLC(prikaz='/PN', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)  
                self.prikazDoPLC(prikaz='/PN', znak=True)
                self.dictNav[self.lastNav].update(self)
                
                if self.dictNav[self.lastNav].zavisle != -1:
                    self.dictNav[self.dictNav[self.lastNav].zavisle].znak = 'PN'
                    self.dictNav[self.dictNav[self.lastNav].zavisle].update(self)

            elif self.dictNav[self.lastNav].znak == 'PN':
                self.dictNav[self.lastNav].znak = 'Stoj'
                self.prikazDoPLC(prikaz='/Stoj', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)
                self.prikazDoPLC(prikaz='/Stoj', znak=True)
                self.dictNav[self.lastNav].update(self) 

                if self.dictNav[self.lastNav].zavisle != -1:
                    self.dictNav[self.dictNav[self.lastNav].zavisle].znak = 'Stoj'
                    self.dictNav[self.dictNav[self.lastNav].zavisle].update(self)           

        elif ((ID == 1 and index == 5) or (ID == 2 and index == 6) or (ID == 3 and index == 4) or (ID == 5 and index == 3)) and (self.lastNav not in [10,11,42,43,50,51,76,77]): #Manuálne zadanie 'Stoj'
            self.dictNav[self.lastNav].vybrane = False

            if (self.dictNav[self.lastNav].pociatocne) or (self.dictNav[self.lastNav].TZZ == 'AH' and self.dictNav[self.lastNav].predhlaska):   #iba ak je návestidlo počiatočným návestidlom jazdnej cesty
                self.dictNav[self.lastNav].manual = True
                self.dictNav[self.lastNav].znak = 'Stoj'
                self.prikazDoPLC(prikaz='/Stoj', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)
                self.prikazDoPLC(prikaz='/Stoj', znak=True)
                self.dictNav[self.lastNav].update(self)

                if self.dictNav[self.lastNav].zavisle != -1:
                    self.dictNav[self.dictNav[self.lastNav].zavisle].znak = 'Stoj'
                    self.dictNav[self.dictNav[self.lastNav].zavisle].update(self)

            else:
                self.vypisHlasenia('Nesprávne zadanie STOJ na návestidle')

        elif ((ID == 1 and index == 4) or (ID == 2 and index == 5) or (ID == 3 and index == 3) or (ID == 5 and index == 2)) and (self.lastNav not in [10,11,42,43,50,51,76,77]): #Manuálne zadanie 'Volno'
            self.dictNav[self.lastNav].vybrane = False

            if (self.dictNav[self.lastNav].pociatocne) or (self.dictNav[self.lastNav].TZZ == 'AH' and self.dictNav[self.lastNav].predhlaska):   #iba ak je návestidlo počiatočným návestidlom jazdnej cesty
                self.dictNav[self.lastNav].manual = True
                if (ID in [1,5]) or (ID == 2 and not self.dictNav[self.lastNav].typAktCes):
                    self.dictNav[self.lastNav].znak = 'Volno'
                    self.prikazDoPLC(prikaz='/Volno', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)
                    self.prikazDoPLC(prikaz='/Volno', znak=True)

                    if self.dictNav[self.lastNav].zavisle != -1:
                        self.dictNav[self.dictNav[self.lastNav].zavisle].znak = 'Volno'
                        self.dictNav[self.dictNav[self.lastNav].zavisle].update(self)

                elif (ID == 3) or (ID == 2 and self.dictNav[self.lastNav].typAktCes):
                    self.dictNav[self.lastNav].znak = 'Posun'
                    self.prikazDoPLC(prikaz='/Posun', id=self.dictNav[self.lastNav].ID, nazov=self.dictNav[self.lastNav].nazov)
                    self.prikazDoPLC(prikaz='/Posun', znak=True)

                    if self.dictNav[self.lastNav].zavisle != -1:
                        self.dictNav[self.dictNav[self.lastNav].zavisle].znak = 'Posun'
                        self.dictNav[self.dictNav[self.lastNav].zavisle].update(self)

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
        self.ui.combo_ciel_hl.setCurrentIndex(0)

    def akciaTS(self, index, id):   #metóda pre prácu s traťovým súhlasom 
        if (index == 1) and (id == 2):   #žiadosť o TS
            if not self.workerThread.dictTS[self.lastTS].prijem:
                if self.workerThread.dictTS[self.lastTS].volnost: 
                    self.prikazDoPLC('ZUS/' + str(self.lastTS) + '/True')
                else:
                    self.vypisHlasenia('Obsadený medzistaničný úsek')
            else:
                self.vypisHlasenia('Traťový súhlas je prijatý')

        elif (index == 2) and (id == 2):   #zrušenie žiadosti o TS
            self.prikazDoPLC('ZUS/' + str(self.lastTS) + '/False')        

        elif ((index == 1 and id == 1) or (index == 3 and id ==2))  and (self.workerThread.dictTS[self.lastTS].prijem is True):   #udelenie TS
            self.prikazDoPLC('UTS/' + str(self.lastTS))
          
        elif (index == 4) and (id == 2):    #zrušenie blokovej podmienky
            self.prikazDoPLC('ZBP/' + str(self.lastTS))

        elif index != 0:
            self.vypisHlasenia('Neudelený traťový súhlas')

        self.comboShowHide()
        self.ui.combo_TS_ESA.setCurrentIndex(0)
        self.ui.combo_TS_DISP.setCurrentIndex(0) 

    def akciaStanica(self, index):  #metóda pre spracovanie signálov riadenia
        if index == 1: #žiadosť o prevzatie riadenia
            if not self.workerThread.dictStanice[self.lastStanica].dialkove:
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

        self.szz.stavanieCesty(OD=Ochr, Disp=True)

    def ukonciStavanie(self, TS=False, odhl=False, volnost=False):   #metóda slúži na ukončenie stavania VC v prípade zlého TS alebo obsadeného medzist. úseku
        self.dictNav[self.Start].stavanieOd = False
        self.dictNav[self.Start].update(self)
        self.szz.vyberCesty = False
        self.Start = 0
        self.End = 0

        if odhl:
            self.vypisHlasenia('Chýbajúca odhláška za vlakom')
        elif TS:
            self.vypisHlasenia('Neudelený traťový súhlas')
        elif volnost:
            self.vypisHlasenia('Obsadený medzistaničný úsek')

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
                
    def lupa(self, index):  #metóda pre prácu s podrobnými obrazmi staníc
        if index == 1:
            self.ui.RadosinaLupa.setVisible(True)
            self.ui.ZbehyLupa.setVisible(False)
            self.ui.HlohovecLupa.setVisible(False)

        elif index == 2:
            self.ui.RadosinaLupa.setVisible(False)
            self.ui.ZbehyLupa.setVisible(True)
            self.ui.HlohovecLupa.setVisible(False)

        elif index == 3:
            self.ui.RadosinaLupa.setVisible(False)
            self.ui.ZbehyLupa.setVisible(False)
            self.ui.HlohovecLupa.setVisible(True)

        elif index == 4:
            self.ui.RadosinaLupa.setVisible(False)
            self.ui.ZbehyLupa.setVisible(False)
            self.ui.HlohovecLupa.setVisible(False)

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
    widget.ui.combo_ciel_hl.hide()
    widget.ui.combo_vyh.hide()
    widget.ui.combo_TS_ESA.hide()
    widget.ui.combo_TS_DISP.hide()
    widget.ui.combo_priec.hide()
    widget.ui.combo_Riadenie.hide()

    widget.ui.RadosinaLupa.setVisible(False)  #po spustení skryje podrobné zobrazenia staníc
    widget.ui.ZbehyLupa.setVisible(False)
    widget.ui.HlohovecLupa.setVisible(False)
    widget.ui.groupREST.setVisible(False)
    widget.ui.groupPrehlad.setVisible(False)

    #prepojenia s metódou vyhodnotenia akcie z kontextového menu
    widget.ui.combo_hlavne.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_hlavne.currentIndex(), 1)) #počiatok jazdnej cesty   
    widget.ui.combo_kombi.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_kombi.currentIndex(), 2))
    widget.ui.combo_zriad.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_zriad.currentIndex(), 3))
    widget.ui.combo_fikt.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_fikt.currentIndex(), 4))
    widget.ui.combo_oddielove.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_oddielove.currentIndex(), 5))

    widget.ui.combo_ciel_ko.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_ciel_ko.currentIndex(), 10)) #koniec jazdnej cesty
    widget.ui.combo_ciel_zr.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_ciel_zr.currentIndex(), 11))
    widget.ui.combo_ciel_fi.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_ciel_fi.currentIndex(), 12))
    widget.ui.combo_ciel_hl.currentIndexChanged.connect(lambda: widget.akciaNavestidlo(widget.ui.combo_ciel_hl.currentIndex(), 13))

    widget.ui.combo_priec.currentIndexChanged.connect(lambda: widget.akciaPriecestie(widget.ui.combo_priec.currentIndex())) #priecestie

    widget.ui.combo_Riadenie.currentIndexChanged.connect(lambda: widget.akciaStanica(widget.ui.combo_Riadenie.currentIndex()))  #riadenie stanice

    widget.ui.combo_TS_DISP.currentIndexChanged.connect(lambda: widget.akciaTS(widget.ui.combo_TS_DISP.currentIndex(), 1))  #traťový súhlas
    widget.ui.combo_TS_ESA.currentIndexChanged.connect(lambda: widget.akciaTS(widget.ui.combo_TS_ESA.currentIndex(), 2))

    widget.ui.combo_vyh.currentIndexChanged.connect(lambda: widget.szz.prestavenieVyh(widget.lastVyh ,widget.ui.combo_vyh.currentIndex()))  #prestavenie výmeny    

    widget.ui.actionLupa_Radosina.triggered.connect(lambda: widget.lupa(1)) #práca s podrobnými obrazmi staníc
    widget.ui.actionLupa_Zbehy.triggered.connect(lambda: widget.lupa(2))
    widget.ui.actionLupa_Hlohovec.triggered.connect(lambda: widget.lupa(3))
    widget.ui.actionPreh_ad.triggered.connect(lambda: widget.lupa(4))

    widget.ui.actionZavrie.triggered.connect(widget.quit) #terminácia aplikácie

    widget.ui.actionVlastnosti.triggered.connect(lambda: widget.popUp(okno='REST'))   #práca s oknom REST API
    widget.ui.ButtonClose.clicked.connect(lambda: widget.popUp(okno='REST'))

    widget.ui.actionInfo.triggered.connect(lambda: widget.popUp(okno='Prehlad'))
    widget.ui.ButtonClose_1.clicked.connect(lambda: widget.popUp(okno='Prehlad'))

    #prepojenia s metódou na zobrazenie kontextového menu pre zvolený element
    #---------------NÁVESTIDLÁ-------------------------------------------
    widget.ui.RAD_zr_do_st_odZ.clicked.connect(lambda: widget.clickObjekt(1, 'navestidlo')) 
    widget.ui.RAD_zr_zo_st_odZ.clicked.connect(lambda: widget.clickObjekt(2, 'navestidlo'))
    widget.ui.RAD_S.clicked.connect(lambda: widget.clickObjekt(3, 'navestidlo'))
    widget.ui.RAD_L1.clicked.connect(lambda: widget.clickObjekt(4, 'navestidlo'))
    widget.ui.RAD_L2.clicked.connect(lambda: widget.clickObjekt(5, 'navestidlo'))    
    widget.ui.RAD_fik_S.clicked.connect(lambda: widget.clickObjekt(6, 'navestidlo'))
    widget.ui.RAD_k1_fik.clicked.connect(lambda: widget.clickObjekt(10, 'navestidlo'))
    widget.ui.RAD_k2_fik.clicked.connect(lambda: widget.clickObjekt(11, 'navestidlo'))
    #--------------------------------------------------------------------
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
    widget.ui.HLO_zr_do_st_odZ.clicked.connect(lambda: widget.clickObjekt(35, 'navestidlo')) 
    widget.ui.HLO_zr_zo_st_odZ.clicked.connect(lambda: widget.clickObjekt(36, 'navestidlo'))
    widget.ui.HLO_L.clicked.connect(lambda: widget.clickObjekt(37, 'navestidlo'))
    widget.ui.HLO_S1.clicked.connect(lambda: widget.clickObjekt(38, 'navestidlo'))
    widget.ui.HLO_S2.clicked.connect(lambda: widget.clickObjekt(39, 'navestidlo'))     
    widget.ui.HLO_fik_L.clicked.connect(lambda: widget.clickObjekt(40, 'navestidlo'))
    widget.ui.HLO_k1_fik.clicked.connect(lambda: widget.clickObjekt(42, 'navestidlo'))
    widget.ui.HLO_k2_fik.clicked.connect(lambda: widget.clickObjekt(43, 'navestidlo'))
    widget.ui.H_ZBE_HLO_Lo.clicked.connect(lambda: widget.clickObjekt(44, 'navestidlo'))
    #----------------------------DISPEČER--------------------------------
    widget.ui.DISP_RAD_S.clicked.connect(lambda: widget.clickObjekt(46, 'navestidlo'))
    widget.ui.DISP_RAD_L1.clicked.connect(lambda: widget.clickObjekt(47, 'navestidlo'))
    widget.ui.DISP_RAD_L2.clicked.connect(lambda: widget.clickObjekt(48, 'navestidlo'))    
    widget.ui.DISP_RAD_fik_S.clicked.connect(lambda: widget.clickObjekt(49, 'navestidlo'))
    widget.ui.DISP_RAD_k1_fik.clicked.connect(lambda: widget.clickObjekt(50, 'navestidlo'))
    widget.ui.DISP_RAD_k2_fik.clicked.connect(lambda: widget.clickObjekt(51, 'navestidlo'))
    #--------------------------------------------------------------------
    widget.ui.DISP_ZBE_L.clicked.connect(lambda: widget.clickObjekt(58, 'navestidlo')) 
    widget.ui.DISP_ZBE_BL.clicked.connect(lambda: widget.clickObjekt(59, 'navestidlo'))
    widget.ui.DISP_ZBE_fik_L.clicked.connect(lambda: widget.clickObjekt(60, 'navestidlo'))
    widget.ui.DISP_ZBE_fik_BL.clicked.connect(lambda: widget.clickObjekt(61, 'navestidlo'))
    widget.ui.DISP_ZBE_S1.clicked.connect(lambda: widget.clickObjekt(62, 'navestidlo'))
    widget.ui.DISP_ZBE_S2.clicked.connect(lambda: widget.clickObjekt(63, 'navestidlo'))
    widget.ui.DISP_ZBE_L1.clicked.connect(lambda: widget.clickObjekt(64, 'navestidlo'))
    widget.ui.DISP_ZBE_L2.clicked.connect(lambda: widget.clickObjekt(65, 'navestidlo'))
    widget.ui.DISP_ZBE_fik_S.clicked.connect(lambda: widget.clickObjekt(66, 'navestidlo'))
    widget.ui.DISP_ZBE_S.clicked.connect(lambda: widget.clickObjekt(67, 'navestidlo'))
    #--------------------------------------------------------------------
    widget.ui.DISP_ZBE_HLO_Lo.clicked.connect(lambda: widget.clickObjekt(69, 'navestidlo'))
    widget.ui.DISP_ZBE_HLO_So.clicked.connect(lambda: widget.clickObjekt(70, 'navestidlo'))
    widget.ui.DISP_HLO_L.clicked.connect(lambda: widget.clickObjekt(71, 'navestidlo'))
    widget.ui.DISP_HLO_S1.clicked.connect(lambda: widget.clickObjekt(72, 'navestidlo'))
    widget.ui.DISP_HLO_S2.clicked.connect(lambda: widget.clickObjekt(73, 'navestidlo'))     
    widget.ui.DISP_HLO_fik_L.clicked.connect(lambda: widget.clickObjekt(74, 'navestidlo'))
    widget.ui.DISP_HLO_k1_fik.clicked.connect(lambda: widget.clickObjekt(76, 'navestidlo'))
    widget.ui.DISP_HLO_k2_fik.clicked.connect(lambda: widget.clickObjekt(77, 'navestidlo'))
    #--------------------------------------------------------------------
    #-------------VÝHYBKY------------------------------------------------
    widget.ui.RAD_V1.clicked.connect(lambda: widget.clickObjekt(3, 'vyhybka'))
    widget.ui.ZBE_V1.clicked.connect(lambda: widget.clickObjekt(12, 'vyhybka'))
    widget.ui.ZBE_V2.clicked.connect(lambda: widget.clickObjekt(13, 'vyhybka'))
    widget.ui.ZBE_V3.clicked.connect(lambda: widget.clickObjekt(16, 'vyhybka'))
    widget.ui.HLO_V1.clicked.connect(lambda: widget.clickObjekt(26, 'vyhybka'))
    #----------------------------DISPEČER--------------------------------
    widget.ui.DISP_RAD_V1.clicked.connect(lambda: widget.clickObjekt(31, 'vyhybka'))
    widget.ui.DISP_ZBE_V1.clicked.connect(lambda: widget.clickObjekt(40, 'vyhybka'))
    widget.ui.DISP_ZBE_V2.clicked.connect(lambda: widget.clickObjekt(41, 'vyhybka'))
    widget.ui.DISP_ZBE_V3.clicked.connect(lambda: widget.clickObjekt(44, 'vyhybka'))
    widget.ui.DISP_HLO_V1.clicked.connect(lambda: widget.clickObjekt(54, 'vyhybka'))
    #--------------------------------------------------------------------
    #-------------TRAŤOVÝ SÚHLAS-----------------------------------------
    widget.ui.RAD_trat_suhlas_doZ.clicked.connect(lambda: widget.clickObjekt(1, 'TS'))
    widget.ui.ZBE_trat_suhlas_doR.clicked.connect(lambda: widget.clickObjekt(2, 'TS'))
    widget.ui.ZBE_trat_suhlas_doH.clicked.connect(lambda: widget.clickObjekt(3, 'TS'))
    widget.ui.ZBE_trat_suhlas_doL.clicked.connect(lambda: widget.clickObjekt(4, 'TS'))
    widget.ui.HLO_trat_suhlas_doZ.clicked.connect(lambda: widget.clickObjekt(5, 'TS'))
    #----------------------------DISPEČER--------------------------------
    widget.ui.DISP_RAD_trat_suhlas_doZ.clicked.connect(lambda: widget.clickObjekt(6, 'TS'))
    widget.ui.DISP_ZBE_trat_suhlas_doR.clicked.connect(lambda: widget.clickObjekt(7, 'TS'))
    widget.ui.DISP_ZBE_trat_suhlas_doH.clicked.connect(lambda: widget.clickObjekt(8, 'TS'))
    widget.ui.DISP_ZBE_trat_suhlas_doL.clicked.connect(lambda: widget.clickObjekt(9, 'TS'))
    widget.ui.DISP_HLO_trat_suhlas_doZ.clicked.connect(lambda: widget.clickObjekt(10, 'TS'))
    #--------------------------------------------------------------------
    #-------------PRIECESTIE---------------------------------------------
    widget.ui.RAD_ZBE_priec.clicked.connect(lambda: widget.clickObjekt(1, 'priecestie'))
    widget.ui.H_ZBE_HLO_priec.clicked.connect(lambda: widget.clickObjekt(2, 'priecestie'))
    widget.ui.DISP_RAD_ZBE_priec.clicked.connect(lambda: widget.clickObjekt(3, 'priecestie'))
    widget.ui.DISP_ZBE_HLO_priec.clicked.connect(lambda: widget.clickObjekt(4, 'priecestie'))
    #--------------------------------------------------------------------
    #-------------RIADENIE STANICE---------------------------------------
    widget.ui.RAD_dialkove.clicked.connect(lambda: widget.clickObjekt(1, 'stanica'))
    widget.ui.ZBE_dialkove.clicked.connect(lambda: widget.clickObjekt(2, 'stanica'))
    widget.ui.HLO_dialkove.clicked.connect(lambda: widget.clickObjekt(3, 'stanica'))
    widget.ui.DISP_RAD_dialkove.clicked.connect(lambda: widget.clickObjekt(4, 'stanica'))
    widget.ui.DISP_ZBE_dialkove.clicked.connect(lambda: widget.clickObjekt(5, 'stanica'))
    widget.ui.DISP_HLO_dialkove.clicked.connect(lambda: widget.clickObjekt(6, 'stanica'))

    widget.ui.ButtonConnect.clicked.connect(widget.zahajPripojenie)  #prepojenie s metódou pre testovanie spojenia s PLC
    widget.ui.ButtonDisconnect.clicked.connect(widget.ukonciPripojenie)  #vyvolá ukončenie komunikácie

    app.exec()