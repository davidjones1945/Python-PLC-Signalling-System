from PySide6.QtCore import QThread, Signal
from time import sleep
import requests

from vyhybka import Vyhybka
from usek import Usek
from tratSuhlas import TratSuhlas
from priecestie import Priecestie
from riadenieObsluhy import RiadenieObsluhy
import ico

class DataUpdate(QThread):
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
            12: Vyhybka(ID=2, IDsmer=1, nazovGUI='ZBE_V1', usek='ZBE_v1', spojka=True, enumIkon=ico.SpojkaA, dictIkon=ico.dictSpojkaA, zavisla=40, druhaVymena=13, app=app_instance),
            13: Vyhybka(ID=3, IDsmer=1, nazovGUI='ZBE_V2', usek='ZBE_v2', spojka=True, enumIkon=ico.SpojkaB, dictIkon=ico.dictSpojkaB, zavisla=41, druhaVymena=12, app=app_instance),
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
            40: Vyhybka(ID=2, IDsmer=1, nazovGUI='DISP_ZBE_V1', usek='DISP_ZBE_v1', spojka=True, enumIkon=ico.SpojkaA, dictIkon=ico.dictSpojkaA, zavisla=12, druhaVymena=41, app=app_instance),
            41: Vyhybka(ID=3, IDsmer=1, nazovGUI='DISP_ZBE_V2', usek='DISP_ZBE_v2', spojka=True, enumIkon=ico.SpojkaB, dictIkon=ico.dictSpojkaB, zavisla=13, druhaVymena=40, app=app_instance),
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

                self.predhlaskaZBE = data['TS']['odchodZH'] #čítanie predhlášok zo staníc Hlohovec a Zbehy
                self.predhlaskaHLO = data['TS']['odchodH']

                if data['Cesta']['stavanie']:   #prenos dát o stavaní vlakovej cesty medzi výpravcom a dispečerom
                    if (data['Cesta']['pociatocne'] in self.app_instance.zoznamNav.keys() and data['Cesta']['koncove'] in self.app_instance.zoznamNav.keys()) and (
                    data['Cesta']['odosielatel'] != 'DISP'):
                        self.app_instance.pociatocneNav = data['Cesta']['pociatocne']
                        self.app_instance.zoznamNav[self.app_instance.pociatocneNav].pociatocne = True
                        self.app_instance.koncoveNav = data['Cesta']['koncove']
                        self.app_instance.szz.typCesty = data['Cesta']['typCesty']
                        ochr = data['Cesta']['OD']
                        self.app_instance.szz.stavanieCesty(Disp=True, OD=ochr, server=True)
                        self.app_instance.prikazDoPLC(cesta=True)

                if data['Cesta']['rusenie']:
                    if data['Cesta']['koncove'] in self.app_instance.zoznamNav.keys() and data['Cesta']['odosielatel'] != 'DISP':
                        self.app_instance.koncoveNav = data['Cesta']['koncove']
                        self.app_instance.szz.rusenieCesty(Disp=True, server=True)
                        self.app_instance.prikazDoPLC(cesta=True)

                if data['Navest']['ID'] != 0 and data['Navest']['ID'] in self.app_instance.zoznamNav.keys() and data['Navest']['odosielatel'] != 'DISP':
                    self.app_instance.zoznamNav[data['Navest']['ID']].znak = data['Navest']['znak']
                    self.app_instance.zoznamNav[data['Navest']['ID']].manual = True
                    self.app_instance.zoznamNav[data['Navest']['ID']].update(self)

                    if self.app_instance.zoznamNav[data['Navest']['ID']].zavisle != -1:
                        self.app_instance.zoznamNav[self.app_instance.zoznamNav[data['Navest']['ID']].zavisle].znak = data['Navest']['znak']
                        self.app_instance.zoznamNav[self.app_instance.zoznamNav[data['Navest']['ID']].zavisle].manual = True
                        self.app_instance.zoznamNav[self.app_instance.zoznamNav[data['Navest']['ID']].zavisle].update(self)

                    self.app_instance.prikazDoPLC(znak=True)

                self.dataUpdated.emit(self.dictUseky, self.dictTS)
            sleep(0.1)