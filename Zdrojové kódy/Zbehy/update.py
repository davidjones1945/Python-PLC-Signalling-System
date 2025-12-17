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