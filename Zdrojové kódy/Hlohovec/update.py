from PySide6.QtCore import QThread, Signal
from time import sleep
import requests

from vyhybka import Vyhybka
from usek import Usek
from tratSuhlas import TratSuhlas
from priecestie import Priecestie
from riadenieObsluhy import RiadenieObsluhy
import ico

class dataUpdate(QThread):
    dataUpdated = Signal(dict, dict)

    odhlaskaSo = False
    predhlaskaZBE = False
    predhlaskaHLO = False

    def __init__(self, app_instance):
        self.dictUseky ={   #slovník úsekov
            22: Usek(ID=6, nazovGUI='ZBE_HLO_TU1_1', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            23: Usek(ID=7, nazovGUI='ZBE_HLO_TU2_a', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            24: Usek(ID=7, nazovGUI='ZBE_HLO_TU2_b', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            25: Usek(ID=0, nazovGUI='HLO_Sk', enummIkon=ico.Kolaj, dictIkon=ico.dictKolaj, app=app_instance),
            26: Vyhybka(ID=1, IDsmer=3, nazovGUI='HLO_V1', usek='HLO_v1' , enumIkon=ico.VyhL, dictIkon=ico.dictVyhL, app=app_instance),
            27: Usek(ID=2, nazovGUI='HLO_k1', enummIkon=ico.KolajSt1, dictIkon=ico.dictStanKolaj1, app=app_instance),
            28: Usek(ID=3, nazovGUI='HLO_k2', enummIkon=ico.KolajSt2, dictIkon=ico.dictStanKolaj2, app=app_instance)
        }

        self.dictTS = { #slovník traťových súhlasov
            5: TratSuhlas(ID=5, nazovGUI='HLO_trat_suhlas_doZ', enumIkon=ico.TrSL, dictIkon=ico.dictTrSL, app=app_instance, typ='S'),
        }

        self.dictPriecestie = { #slovník priecestí
            2:Priecestie(ID=2, nazovGUI='H_ZBE_HLO_priec', enumIkon=ico.Priecestie, dictIkon=ico.dictPriecestie, app=app_instance)
        } 

        self.dictStanice = {    #slovník stníc
            3:RiadenieObsluhy(ID=3, nazovGUI='HLO_dialkove', enumIkon=ico.RiadenieHLO, dictIkon=ico.dictRiadenieHLO, app=app_instance),
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
                    for index in range(22,25):
                        self.dictUseky[index].jeVolny = data['P1;P2;ZBE-HLO'][self.dictUseky[index].ID]

                    for index in range(25,29):
                        self.dictUseky[index].jeVolny = data['HLO'][self.dictUseky[index].ID]

                for i in [26]:  #čítanie smeru výmen
                    self.dictUseky[i].smer = data['SmerVyh'][self.dictUseky[i].IDsmer]    #informácia o aktuálnom smere výmeny

                #čítanie stavov traťových súhlasov
                self.dictTS[5].smer = data['TS']['smerZH'] 
                self.dictTS[5].volnost = data['TS']['volZH'] 
                MyOdchod = data['TS']['odchodH']
                HradloOdchod = data['TS']['predhlLo']
                self.dictTS[5].odchod = (MyOdchod or HradloOdchod) 

                #čítanie stavov priecestí
                self.dictPriecestie[2].predzvananie = data['Priecestie'][7]
                self.dictPriecestie[2].otvorene = data['Priecestie'][5]
                self.dictPriecestie[2].zatvorene = data['Priecestie'][6]
                self.dictPriecestie[2].jeVolny = self.dictUseky[23].jeVolny  

                for index in self.dictStanice.keys():   #čítanie stavov riadenia staníc
                    self.dictStanice[3].dialkove = data['Riadenie']['dialkoveHLO']
                    self.dictStanice[3].ziadost = data['Riadenie']['ziadostHLO']

                self.odhlaskaSo = data['TS']['odhlSo']   #čítanie odhlášok z hradla Rišňovce 

                self.predhlaskaZBE = data['TS']['odchodZH'] #čítanie predhlášok zo susedných staníc
                self.predhlaskaHLO = data['TS']['odchodH'] 

                if data['Cesta']['stavanie']:
                    if (data['Cesta']['pociatocne'] in self.app_instance.dictNav.keys() and data['Cesta']['koncove'] in self.app_instance.dictNav.keys()) and (
                    data['Cesta']['odosielatel'] != 'HLO'):
                        self.app_instance.Start = data['Cesta']['pociatocne']
                        self.app_instance.dictNav[self.app_instance.Start].pociatocne = True
                        self.app_instance.End = data['Cesta']['koncove']
                        self.app_instance.szz.typCesty = data['Cesta']['typCesty']
                        self.app_instance.szz.stavanieCesty(server=True)
                        self.app_instance.prikazDoPLC(cesta=True)

                if data['Cesta']['rusenie']:
                    if data['Cesta']['koncove'] in self.app_instance.dictNav.keys() and data['Cesta']['odosielatel'] != 'HLO':
                        self.app_instance.End = data['Cesta']['koncove']
                        self.app_instance.szz.rusenieCesty(server=True)
                        self.app_instance.prikazDoPLC(cesta=True)

                if data['Navest']['ID'] != 0 and data['Navest']['ID'] in self.app_instance.dictNav.keys() and data['Navest']['odosielatel'] != 'HLO':
                    self.app_instance.dictNav[data['Navest']['ID']].znak = data['Navest']['znak']
                    self.app_instance.dictNav[data['Navest']['ID']].update(self)
                    self.app_instance.prikazDoPLC(znak=True)

                self.dataUpdated.emit(self.dictUseky, self.dictTS)
            sleep(0.1)