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