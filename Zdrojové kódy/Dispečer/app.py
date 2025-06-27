from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, Signal, QTimer
import sys
import requests
from time import sleep
import arrow

from ui_form import Ui_ILTIS
import ico
from zoznamNavestidiel import ZoznamNavestidiel
from vyhybka import Vyhybka
from navestidlo import Navestidlo
from usek import Usek
from SZZ import SZZ
from tratSuhlas import TratSuhlas
from priecestie import Priecestie
from riadenieObsluhy import RiadenieObsluhy

from datum import Datum
from casSubory import DlhyCasPosun, DlhyCasVlak, CasOchrDr, LifeSign

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

class App(QMainWindow): #hlavná triedy vizualizácie
    def __init__(self, parent=None):              
        super().__init__(parent)
        self.ui = Ui_ILTIS()    #vytvorenie spojenia s triedami
        self.szz = SZZ(self)   

        self.ui.setupUi(self)

        self.workerThread = dataUpdate(self)   #prepojenie bočných vláken s hlavným vláknom
        self.workerThreadDlhyCasVlak = DlhyCasVlak()
        self.workerThreadDlhyCasPosun = DlhyCasPosun()
        self.workerThreadCasOchrDrahy = CasOchrDr()
        self.workerThreadLifeSign = LifeSign(self)
        self.workerThreadDatum = Datum()
        self.workerThreadDatum.start()

        self.workerThread.dataUpdated.connect(self.update) #definícia prepojenia vláken a metód
        self.workerThread.dataUpdated.connect(lambda: self.szz.stavanieCesty(True, Disp=True))

        self.workerThreadDatum.dataUpdated.connect(self.aktualizaciaCasu)
        
        self.workerThreadDlhyCasVlak.finished.connect(lambda: self.szz.rusenieCesty(True))
        self.workerThreadDlhyCasPosun.finished.connect(lambda: self.szz.rusenieCesty(True))
        self.workerThreadCasOchrDrahy.finished.connect(lambda: self.szz.rusenieOD(Disp=True))

        self.workerThread.setParent(self)  #definovanie rodičovského objektu pre vlákna
        self.workerThreadLifeSign.setParent(self)

        self.posledneNav = 0  #posledné kliknuté návestidlo
        self.pociatocneNav = 0    #počiatočné návestidlo jazdnej cesty
        self.koncoveNav = 0    #koncové návestidlo jazdnej cesty

        self.poslednaVyh = 'X'  #posledná kliknutá výhybka
        self.poslednePriec = 'X'  #posledné kliknuté priecestie 
        self.poslednaStn = 'X' #posledná kliknutá stanica
        self.poslednyTS = 'X'   #posledný kliknutý traťový súhlas
        self.predposlednyTS = 'X' #predposledný kliknutý traťový súhlas

        self.zoznamNavOBJ = ZoznamNavestidiel(parent = self)    #objekt zoznamu návestidiel
        self.zoznamNav = self.zoznamNavOBJ.zoznamNav

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
            self.workerThreadDlhyCasVlak.start()
            self.workerThreadDlhyCasPosun.start()
            self.workerThreadCasOchrDrahy.start()
            self.workerThreadLifeSign.start()

            self.ui.RAD_ASVC.setIcon(ico.icon_ASVC_vypnute)
            self.ui.DISP_RAD_ASVC.setIcon(ico.icon_ASVC_vypnute)
            self.ui.ZBE_ASVC.setIcon(ico.icon_ASVC_vypnute)
            self.ui.DISP_ZBE_ASVC.setIcon(ico.icon_ASVC_vypnute)
            self.ui.HLO_ASVC.setIcon(ico.icon_ASVC_vypnute)
            self.ui.DISP_HLO_ASVC.setIcon(ico.icon_ASVC_vypnute)

    def ukonciPripojenie(self): #metóda pre zastavenie vláken a ukončenie komunikácie
        self.workerThread.requestInterruption()    
        self.workerThreadDlhyCasVlak.requestInterruption()
        self.workerThreadDlhyCasPosun.requestInterruption()
        self.workerThreadCasOchrDrahy.requestInterruption()  
        self.workerThreadLifeSign.requestInterruption()  
        self.workerThreadDatum.requestInterruption()  

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
            self.zoznamNav[8].zhasnute =  self.workerThread.dictTS[1].smer  #otáčanie svietenia AB podľa TS
            self.zoznamNav[9].zhasnute =  not self.workerThread.dictTS[1].smer  #AB18 + AB19
            self.zoznamNav[52].zhasnute =  self.workerThread.dictTS[1].smer  
            self.zoznamNav[53].zhasnute =  not self.workerThread.dictTS[1].smer

            self.zoznamNav[28].zhasnute =  not self.workerThread.dictTS[2].smer  #AB28 + AB29
            self.zoznamNav[29].zhasnute =  self.workerThread.dictTS[2].smer
            self.zoznamNav[55].zhasnute =  not self.workerThread.dictTS[2].smer  
            self.zoznamNav[54].zhasnute =  self.workerThread.dictTS[2].smer
            

            self.zoznamNav[57].zhasnute =  self.workerThread.dictTS[2].smer  #AB39 + AB40
            self.zoznamNav[56].zhasnute =  not self.workerThread.dictTS[2].smer

            for nav in [30,44,69]:
                self.zoznamNav[nav].predhlaska = self.workerThread.predhlaskaZBE

            for nav in [31,45,70]:
                self.zoznamNav[nav].predhlaska = self.workerThread.predhlaskaHLO

            if clicked and ID in self.zoznamNav:  #ak bolo návestidlo kliknuté obsluhou
                self.zoznamNav[ID].vybrane = not self.zoznamNav[ID].vybrane 
                for i in self.zoznamNav.keys():
                    if i != ID:
                        self.zoznamNav[i].vybrane = False               

            for ID in self.zoznamNav.keys():  #vyberaj z návestidiel
                for i in self.workerThread.dictUseky.keys():   #vyberaj z úsekov
                    if self.zoznamNav[ID].usekPred == self.workerThread.dictUseky[i].nazovGUI:   #ak sa nájde úsek previazaný s návestidlom
                        self.zoznamNav[ID].jeVolnyPred = self.workerThread.dictUseky[i].jeVolny  #aktualizuj symbol návestidla podľa obsadenia úseku

                    if self.zoznamNav[ID].usekPred == self.workerThread.dictUseky[i].nazovGUI:   #ak sa nájde úsek previazaný s návestidlom
                        self.zoznamNav[ID].usekOdozva = self.workerThread.dictUseky[i].odozva  #aktualizuj symbol návestidla podľa LIfeSign úseku

                    if self.zoznamNav[ID].usekZa == self.workerThread.dictUseky[i].nazovGUI:   #ak sa nájde úsek previazaný s návestidlom
                        self.zoznamNav[ID].jeVolnyZa = self.workerThread.dictUseky[i].jeVolny  #aktualizuj symbol návestidla podľa obsadenia úseku

                self.zoznamNav[ID].update(self)

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
        if objekt == 'navestidlo': # ak bolo vybrané návestidlo
            self.posledneNav = id   #zápis posledného kliknutého návestidla  

            if ((self.posledneNav in range(1, 11) or self.posledneNav in range(46, 55)) and self.workerThread.dictStanice[1].dialkove) or (
            (self.posledneNav in range(12, 34) or self.posledneNav in range(56, 69)) and self.workerThread.dictStanice[2].dialkove) or (
            (self.posledneNav in range(35, 45) or self.posledneNav in range(70, 77)) and self.workerThread.dictStanice[3].dialkove):
                
                self.update(self.posledneNav, True, objekt='navestidla') #aktualizuj symbol návestidla

                if self.zoznamNav[self.posledneNav].vybrane and not self.szz.vyberCesty:    
                    self.comboShowHide(self.zoznamNav[self.posledneNav].comboBox)   #otvor comboBox pre počiatok stavenia vlakovej cesty
                elif self.zoznamNav[self.posledneNav].vybrane and self.szz.vyberCesty:
                    self.comboShowHide((self.zoznamNav[self.posledneNav].comboBox + '_konc'))   #otvor comboBox pre unokčenie stavenia vlakovej cesty
                else:
                    self.comboShowHide()    #skry comboBox

            else:
                self.vypisHlasenia('Obsluha stanice prevedená na lokálne pracovisko') #ak nie je aktívne ovládanie, vypíš hlásenie

        elif objekt == 'vyhybka':
            if id in self.workerThread.dictUseky:  #ak sa výhybka nachádza v zozname
                self.poslednaVyh = id   #zapíš ju ako poslednú kliknutú
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
            self.poslednePriec = id
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
            self.poslednyTS = id 
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
            self.poslednaStn = id
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
            self.prikazDoPLC(priec=True, nazov=self.workerThread.dictPriecestie[self.poslednePriec].nazovGUI, prikaz='/True')            

        elif index == 2:  #otvorenie priecestia
            self.prikazDoPLC(priec=True, nazov=self.workerThread.dictPriecestie[self.poslednePriec].nazovGUI, prikaz='/False')
        
        else:
            self.workerThread.dictPriecestie[self.poslednePriec].vyber = False
            self.workerThread.dictPriecestie[self.poslednePriec].update(self)

        self.ui.combo_priec.setCurrentIndex(0) #resetuj index vybranej akcie z kontextového menu  

    def akciaNavestidlo(self, index, ID):   #vyhodnotenie vybranej akcie z kontextového menu
        self.comboShowHide()    #po výbere skry menu

        if ((ID in [1,2]) and index == 1) and (self.posledneNav not in [10,11,42,43,50,51,76,77]):  #výber vlakovej cesty
            self.vyberCestu('Vlak')

        elif (ID == 2 and index == 2) or (ID == 3 and index == 1):  #výber posunovej cesty
            if self.posledneNav in [1,4,5,18,19,20,21,22,23,24,35,38,39]:
                self.vyberCestu('Posun')

            else:
                self.vypisHlasenia('Nie je možné postaviť posunovú cestu')

        elif (ID == 1 and index == 3) or (ID == 4 and index == 1) or (ID == 2 and index == 4) or (ID == 3 and index == 2):    #rušenie cesty
            self.koncoveNav = self.posledneNav
            self.posledneNav = 0

            if ID == 4: #predhlášky od jednotlivých staníc
                if self.koncoveNav in [6,49]:
                    self.prikazDoPLC(odchod=True, nazov='odchodR', prikaz='/False')
                if self.koncoveNav in [14,60]:
                    self.prikazDoPLC(odchod=True, nazov='odchodZR', prikaz='/False')
                elif self.koncoveNav in [15,61]:
                    self.prikazDoPLC(odchod=True, nazov='odchodZL', prikaz='/False')
                elif self.koncoveNav in [26,66]:
                    self.prikazDoPLC(odchod=True, nazov='odchodZH', prikaz='/False')
                    self.prikazDoPLC(prikaz='/False', nazov='ZBE', predhl=True)
                elif self.koncoveNav in [40,74]:
                    self.prikazDoPLC(odchod=True, nazov='odchodH', prikaz='/False')
                    self.prikazDoPLC(prikaz='/False', nazov='HLO', predhl=True)

            if self.koncoveNav in [26,66]:
                for nav in [30,44,69]:
                    self.zoznamNav[nav].predhlaska = False

            elif self.koncoveNav in [40,74]:
                for nav in [31,45,70]:
                    self.zoznamNav[nav].predhlaska = False

            self.zoznamNav[self.koncoveNav].vybrane = False
            self.zoznamNav[self.koncoveNav].update(self)
            self.szz.rusenieCesty(Disp=True)

        elif self.pociatocneNav in [3,12,13,27,37,46,58,59,67,68,71] and ID in [10,12,13] and index == 1: #stavanie vchodovej bez ochrannej dráhy
            if not self.szz.typCesty:
                self.postavCestu()
            else:
                self.vypisHlasenia('Nekorektný typ jazdnej cesty')

        elif ((ID in [10,12,13]) and (index == 2) and (not self.szz.typCesty)): #stavanie vchodovej cesty s ochrannou dráhou
            if self.pociatocneNav in [12,13,27,58,59,67]:
                self.postavCestu(True)

            else:
                self.vypisHlasenia('Jazdná cesta nemá definovanú ochrannú dráhu')
                self.ukonciStavanie()
            
        elif (self.pociatocneNav in [4,5,20,21,22,23,38,39,47,48,62,63,64,65,72,73]) and ((ID in [10,12]) and (index == 1) and (not self.szz.typCesty)): #stavanie odchodovej cesty
            if self.pociatocneNav in [4,5,47,48]:
                if self.workerThread.dictTS[1].prijem:
                    self.postavCestu()
                else:
                    self.ukonciStavanie(TS=True)

            elif self.pociatocneNav in [20,62]:
                if self.workerThread.dictTS[2].prijem:
                    self.postavCestu()
                else:
                    self.ukonciStavanie(TS=True)
                
            elif self.pociatocneNav in [21,63]:
                if self.posledneNav in [14,60]:                    
                    if self.workerThread.dictTS[2].prijem:
                        self.postavCestu()
                    else:
                        self.ukonciStavanie(TS=True)

                elif self.posledneNav in [15,61]:                    
                    if self.workerThread.dictTS[4].volnost: 
                        if self.workerThread.dictTS[4].prijem:
                            self.postavCestu()
                        else:
                            self.ukonciStavanie(TS=True)
                    else:
                        self.ukonciStavanie(volnost=True)

            elif self.pociatocneNav in [22,23,64,65]:
                if self.workerThread.odhlaskaLo:                    
                    if self.workerThread.dictTS[3].prijem:
                        self.postavCestu()
                    else:
                        self.ukonciStavanie(TS=True)
                else:
                    self.ukonciStavanie(odhl=True)

            elif self.pociatocneNav in [38,39,72,73]:
                if self.workerThread.odhlaskaSo:
                    if self.workerThread.dictTS[5].prijem:
                        self.postavCestu()
                    else:
                        self.ukonciStavanie(TS=True)
                else:
                    self.ukonciStavanie(odhl=True)

        elif (ID == 10 and index == 3) or (ID == 11 and index == 1):    #stavanie posunovej cesty
            self.postavCestu()

        elif ((ID == 1 and index == 2) or (ID == 2 and index == 3) or (ID == 5 and index == 1)) and (self.posledneNav not in [10,11,42,43,50,51,76,77]): #Privolávacia návesť
            self.zoznamNav[self.posledneNav].vybrane = False
            
            if self.zoznamNav[self.posledneNav].znak == 'Stoj':
                self.zoznamNav[self.posledneNav].znak = 'PN'
                self.prikazDoPLC(prikaz='/PN', id=self.zoznamNav[self.posledneNav].ID, nazov=self.zoznamNav[self.posledneNav].nazov)  
                self.prikazDoPLC(prikaz='/PN', znak=True)
                self.zoznamNav[self.posledneNav].update(self)
                
                if self.zoznamNav[self.posledneNav].zavisle != -1:
                    self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].znak = 'PN'
                    self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].update(self)

            elif self.zoznamNav[self.posledneNav].znak == 'PN':
                self.zoznamNav[self.posledneNav].znak = 'Stoj'
                self.prikazDoPLC(prikaz='/Stoj', id=self.zoznamNav[self.posledneNav].ID, nazov=self.zoznamNav[self.posledneNav].nazov)
                self.prikazDoPLC(prikaz='/Stoj', znak=True)
                self.zoznamNav[self.posledneNav].update(self) 

                if self.zoznamNav[self.posledneNav].zavisle != -1:
                    self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].znak = 'Stoj'
                    self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].update(self)           

        elif ((ID == 1 and index == 5) or (ID == 2 and index == 6) or (ID == 3 and index == 4) or (ID == 5 and index == 3)) and (self.posledneNav not in [10,11,42,43,50,51,76,77]): #Manuálne zadanie 'Stoj'
            self.zoznamNav[self.posledneNav].vybrane = False

            if (self.zoznamNav[self.posledneNav].pociatocne) or (self.zoznamNav[self.posledneNav].TZZ == 'AH' and self.zoznamNav[self.posledneNav].predhlaska):   #iba ak je návestidlo počiatočným návestidlom jazdnej cesty
                self.zoznamNav[self.posledneNav].manual = True
                self.zoznamNav[self.posledneNav].znak = 'Stoj'
                self.prikazDoPLC(prikaz='/Stoj', id=self.zoznamNav[self.posledneNav].ID, nazov=self.zoznamNav[self.posledneNav].nazov)
                self.prikazDoPLC(prikaz='/Stoj', znak=True)
                self.zoznamNav[self.posledneNav].update(self)

                if self.zoznamNav[self.posledneNav].zavisle != -1:
                    self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].znak = 'Stoj'
                    self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].update(self)

            else:
                self.vypisHlasenia('Nesprávne zadanie STOJ na návestidle')

        elif ((ID == 1 and index == 4) or (ID == 2 and index == 5) or (ID == 3 and index == 3) or (ID == 5 and index == 2)) and (self.posledneNav not in [10,11,42,43,50,51,76,77]): #Manuálne zadanie 'Volno'
            self.zoznamNav[self.posledneNav].vybrane = False

            if (self.zoznamNav[self.posledneNav].pociatocne) or (self.zoznamNav[self.posledneNav].TZZ == 'AH' and self.zoznamNav[self.posledneNav].predhlaska):   #iba ak je návestidlo počiatočným návestidlom jazdnej cesty
                self.zoznamNav[self.posledneNav].manual = True
                if (ID in [1,5]) or (ID == 2 and not self.zoznamNav[self.posledneNav].typAktCes):
                    self.zoznamNav[self.posledneNav].znak = 'Volno'
                    self.prikazDoPLC(prikaz='/Volno', id=self.zoznamNav[self.posledneNav].ID, nazov=self.zoznamNav[self.posledneNav].nazov)
                    self.prikazDoPLC(prikaz='/Volno', znak=True)

                    if self.zoznamNav[self.posledneNav].zavisle != -1:
                        self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].znak = 'Volno'
                        self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].update(self)

                elif (ID == 3) or (ID == 2 and self.zoznamNav[self.posledneNav].typAktCes):
                    self.zoznamNav[self.posledneNav].znak = 'Posun'
                    self.prikazDoPLC(prikaz='/Posun', id=self.zoznamNav[self.posledneNav].ID, nazov=self.zoznamNav[self.posledneNav].nazov)
                    self.prikazDoPLC(prikaz='/Posun', znak=True)

                    if self.zoznamNav[self.posledneNav].zavisle != -1:
                        self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].znak = 'Posun'
                        self.zoznamNav[self.zoznamNav[self.posledneNav].zavisle].update(self)

                self.zoznamNav[self.posledneNav].update(self)

            else:
                self.vypisHlasenia('Nesprávne zadanie VOĽNO na návestidle')
        
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
        self.ui.combo_ciel_hl.setCurrentIndex(0)

    def akciaTS(self, index, id):   #metóda pre prácu s traťovým súhlasom 
        if (index == 1) and (id == 2):   #žiadosť o TS
            if not self.workerThread.dictTS[self.poslednyTS].prijem:
                if self.workerThread.dictTS[self.poslednyTS].volnost: 
                    self.prikazDoPLC('ZUS/' + str(self.poslednyTS) + '/True')
                else:
                    self.vypisHlasenia('Obsadený medzistaničný úsek')
            else:
                self.vypisHlasenia('Traťový súhlas je prijatý')

        elif (index == 2) and (id == 2):   #zrušenie žiadosti o TS
            self.prikazDoPLC('ZUS/' + str(self.poslednyTS) + '/False')        

        elif ((index == 1 and id == 1) or (index == 3 and id ==2))  and (self.workerThread.dictTS[self.poslednyTS].prijem is True):   #udelenie TS
            self.prikazDoPLC('UTS/' + str(self.poslednyTS))
          
        elif (index == 4) and (id == 2):    #zrušenie blokovej podmienky
            self.prikazDoPLC('ZBP/' + str(self.poslednyTS))

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

        self.pociatocneNav = self.posledneNav   #vybrané návestidlo označí za počiatočné

        self.zoznamNav[self.pociatocneNav].stavanieOd = True
        self.zoznamNav[self.pociatocneNav].typAktCes = self.szz.typCesty #zapíše počiatočnému návestidlu typ cesty
        self.zoznamNav[self.pociatocneNav].vybrane = False
        self.zoznamNav[self.pociatocneNav].update(self)

    def postavCestu(self, Ochr=False):  #metóda, ktorá vydá príkaz pre postavenie vybranej cesty algoritmom SZZ
        self.szz.vyberCesty = False
        self.koncoveNav = self.posledneNav
        self.posledneNav = 0

        self.zoznamNav[self.koncoveNav].vybrane = False
        self.zoznamNav[self.koncoveNav].update(self)

        self.szz.stavanieCesty(OD=Ochr, Disp=True)

    def ukonciStavanie(self, TS=False, odhl=False, volnost=False):   #metóda slúži na ukončenie stavania VC v prípade zlého TS alebo obsadeného medzist. úseku
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
                        URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/' + str(self.szz.typCesty) + '/True/True/False/DISP'

                    else:
                        URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/' + str(self.szz.typCesty) + '/False/True/False/DISP'

                elif nazov == 'rusenie':
                    URL = adresa + 'Cesta/' + str(start) + '/' + str(end) + '/False/False/False/True/DISP'
                    
                else:
                    URL = adresa + 'Cesta/0/0/False/False/False/False/DISP'

            elif znak:
                if self.posledneNav > 45:
                    nav = self.zoznamNav[self.posledneNav].zavisle
                else:
                    nav = self.posledneNav

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