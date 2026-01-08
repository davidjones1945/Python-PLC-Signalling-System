import uvicorn
from fastapi import FastAPI
from time import sleep
import arrow
from datetime import timedelta
import snap7

import S71200
import RiseEdge as RE
import FallEdge as FE

app = FastAPI()
client = snap7.client.Client()

plc = S71200.S71200('158.193.224.220')   #definícia IP adresy PLC

zapis = False   #premenné pre arbitráž dopytov do PLC
citanie = False

PrevStav = False    #premené pre SR obvod
outFF = False
odozvaESA = False

casovaPeciatkaESA = arrow.now() #časové pečiatky posledných príchodzích správ
casovaPeciatkaILTISdisp = arrow.now()
casovaPeciatkaILTISzbe = arrow.now()

RiseEdgeR = RE.RiseEdge()   #objekty detektora pre detekciu nábežnej hrany
RiseEdgeZH = RE.RiseEdge()
RiseEdgeZL = RE.RiseEdge()
RiseEdgeZR = RE.RiseEdge()
RiseEdgeH = RE.RiseEdge()
RiseEdgeL = RE.RiseEdge()
FallEdgeBP = FE.FallEdge()

dataTS = {  #slovník s dátami o traťových súhlasoch, odchodových cestách, predlháškach a odhláškach
    'smerRZ': False,
    'smerZH': False,
    'smerLZ': False,

    'ZUS_RZ': False,
    'ZUS_LZ': False,
    'ZTS_L': False,

    'volRZ': True,
    'volZH': True,
    'volLZ': False,

    'odchodR': False,   # zároveň predhláška zo stanice
    'odchodZR': False,
    'odchodZL': False,
    'odchodZH': False,
    'odchodH': False,  
    'odchodL': False, 

    'predhlLo': False,
    'predhlSo': False,
    'odhlLo': False,
    'odhlSo': False,

    'odhlZBE': True,
    'volnoZBE': False,
    'ziadZBP': False,
    'ZBP': False
}

dataRiadenie = {    #slovník s dátami o spôsobe riadenia zabzar
    'dialkoveRAD': True,
    'dialkoveZBE': True,
    'dialkoveHLO': True,

    'ziadostRAD': False,
    'ziadostZBE': False,
    'ziadostHLO': False,
}

dataCesta = {
    'pociatocne': 0,
    'koncove': 0,
    'typCesty': False, #True - posun, False - vlak
    'OD': False,
    'stavanie': False,
    'rusenie': False,
    'odosielatel': 'X'

}

dataNavest = {
    'ID': 0,
    'znak': 'Stoj',
    'odosielatel': 'X'
}

usekZL = False  #voľnosť úseku Lužianky - Zbehy

def FlipFlop(Set, Reset):   #metóda SR obvodu
    global PrevStav
    global outFF

    if (Set is False) and (Reset is False):
        outFF = PrevStav

    elif (Set is False) and (Reset is True):
        outFF = False

    elif (Set is True) and (Reset is False):
        outFF = True

    PrevStav = outFF

    return outFF

@app.put('/Cesta/{start}/{end}/{typ}/{od}/{stav}/{rus}/{meno}')   #metóda spracovávajúca časové pečiatky z dispečerskej aplikácie a staničnej aplikácie Zbehy
async def writeCesta(start: int, end: int, typ: bool, od: bool, stav: bool, rus: bool, meno: str):
    dataCesta['pociatocne'] = start
    dataCesta['koncove'] = end
    dataCesta['typCesty'] = typ
    dataCesta['OD'] = od
    dataCesta['stavanie'] = stav
    dataCesta['rusenie'] = rus
    dataCesta['odosielatel'] = meno

@app.put('/Navest/{ID}/{znak}/{meno}')   #metóda spracovávajúca časové pečiatky z dispečerskej aplikácie a staničnej aplikácie Zbehy
async def writeNavest(ID: int, znak: str, meno: str):
    dataNavest['ID'] = ID
    dataNavest['znak'] = znak
    dataNavest['odosielatel'] = meno

@app.put('/CasP/{index}')   #metóda spracovávajúca časové pečiatky z dispečerskej aplikácie a staničnej aplikácie Zbehy
async def writeCasPec(index: str):
    global casovaPeciatkaILTISdisp
    global casovaPeciatkaILTISzbe

    aktualnyCas = arrow.now()
    if index == 'disp':
        casovaPeciatkaILTISdisp = aktualnyCas
    elif index == 'zbe':
        casovaPeciatkaILTISzbe = aktualnyCas

@app.put('/ziadostZBP/{value}')   #metóda spracovávajúca žiadosti o blokovej podmienke od ESA-44
async def writeZBP(value: bool):
    global dataTS

    dataTS['ziadZBP'] = value

@app.get('/hlasenieESA')    #metóda spätného hlásenia pre ESA 44
async def writeESA():
    global dataTS
    global casovaPeciatkaILTISdisp
    global casovaPeciatkaILTISzbe

    aktualnyCas = arrow.now()
    if ((aktualnyCas - casovaPeciatkaILTISdisp) <= timedelta(seconds=15)) or (
        (aktualnyCas - casovaPeciatkaILTISzbe) <= timedelta(seconds=15)):   #ak je posledná správa od ILTIS-N s platným časom
        casPeciatka = True
    
    else:
        casPeciatka = False

    hlasenie = {
        'smerTS': dataTS['smerLZ'],
        'ZTS': dataTS['ZUS_LZ'],
        'ZBP': dataTS['ZBP'],
        'zaverOdch': dataTS['odchodZL'],
        'volnoZBE': dataTS['volnoZBE'],
        'odhlaska': dataTS['odhlZBE'],
        'casPeciatka' : casPeciatka
    }

    return {'hlasenie': hlasenie}

@app.put('/volnost/{value}') #metóda pre ESA 44 na zápis obsadenosti medzstaničného úseku
async def writeVolnost(value: bool):
    global usekZL
    global casovaPeciatkaESA

    usekZL = value
    casovaPeciatkaESA = arrow.now()

@app.put('/ZUS/{index}/{value}')    #metóda pre zápis žiadsti o traťový súhlas
async def writeZUS(index: int, value: bool):
    global dataTS

    if index in [1,2,6,7]:
        dataTS['ZUS_RZ'] = value

    elif index in [4,9]:
        dataTS['ZUS_LZ'] = value

    elif index == 11:
        dataTS['ZTS_L'] = value

@app.put('/ZBP/{index}')    #metóda pre zápis príznaku rušenia blokovej podmienky
async def writeZUS(index: int):
    global dataTS

    if index in [4,9]:
        dataTS['ZBP'] = True

@app.put('/UTS/{index}')    #metóda pre zmenu smeru traťového súhlasu
async def writeUTS(index: int):
    global plc
    global zapis
    global citanie
    global dataTS

    while zapis or citanie:
        sleep(0.1)

    if (not zapis) and (not citanie):
        zapis = True
        if index in [1,2,6,7]:
            dataTS['ZUS_RZ'] = False
            dataTS['smerRZ'] = not dataTS['smerRZ']
            address = 'MX7.0'
            value = dataTS['smerRZ']

        elif index in [3,5,8,10]:
            dataTS['smerZH'] = not dataTS['smerZH']
            address = 'MX7.1'
            value = dataTS['smerZH']

        elif index in [4,9]:
            dataTS['ZTS_L'] = False
            dataTS['smerLZ'] = not dataTS['smerLZ']
            address = None
            value = dataTS['smerLZ']

        elif index == 11:
            dataTS['ZUS_LZ'] = False
            dataTS['smerLZ'] = not dataTS['smerLZ']
            value = dataTS['smerLZ']

        while True: #arbitrážny cyklus
            zapis = True
            try:
                if address is not None:
                    plc.writeMem(address, value)
            except RuntimeError:
                zapis = False
                sleep(0.1)
            else:
                break
        zapis = False

@app.put('/ziadRiad/{index}/{value}')   #metóda spracovávajúca žiadosti o zmenu ovládania medzi aplikáciami
async def writeZiadRiad(index: str, value: bool):
    global dataRiadenie

    if index in ['RAD_dialkove', 'DISP_RAD_dialkove']:
        dataRiadenie['ziadostRAD'] = value
    
    elif index in ['ZBE_dialkove', 'DISP_ZBE_dialkove']:
        dataRiadenie['ziadostZBE'] = value
    
    elif index in ['HLO_dialkove', 'DISP_HLO_dialkove']:
        dataRiadenie['ziadostHLO'] = value

@app.put('/udelRiad/{index}')   #metóda spracovávajúca pokyny pre zmenu ovládania medzi aplikáciami
async def writeUdelRiad(index: str):
    global dataRiadenie

    if index in ['RAD_dialkove', 'DISP_RAD_dialkove']:
        dataRiadenie['ziadostRAD'] = False
        dataRiadenie['dialkoveRAD'] = not dataRiadenie['dialkoveRAD']
    
    elif index in ['ZBE_dialkove', 'DISP_ZBE_dialkove']:
        dataRiadenie['ziadostZBE'] = False
        dataRiadenie['dialkoveZBE'] = not dataRiadenie['dialkoveZBE']
    
    elif index in ['HLO_dialkove', 'DISP_HLO_dialkove']:
        dataRiadenie['ziadostHLO'] = False
        dataRiadenie['dialkoveHLO'] = not dataRiadenie['dialkoveHLO']

@app.put('/odchod/{index}/{value}')  #metóda pre zápis aktívnych odchodových ciest
async def writeOdchod(index: str, value: bool):
    global dataTS

    dataTS[index] = value

@app.put('/predhl/{index}/{value}') #metóda pre zápis preshlášok pre AH
async def writePredhl(index: str, value: bool):
    global plc
    global zapis
    global citanie

    while zapis and citanie:
        sleep(0.1)

    if not (zapis and citanie):
        if index == 'ZBE':
            address = 'MX29.0'

        elif index == 'HLO':
            address = 'MX29.1'

        while True: #arbitrážny cyklus
            zapis = True
            try:
                plc.writeMem(address, value)

            except RuntimeError:
                zapis = False
                sleep(0.1)

            else:
                break

        zapis = False

@app.get('/read')   #metóda spätného hlásenia pre ILTIS-N
async def read():
    global plc
    global zapis
    global citanie
    global dataTS
    global dataRiadenie
    global usekZL
    global casovaPeciatkaESA

    while zapis and citanie:
        sleep(0.1)

    if not (zapis and citanie):
        citanie = True
        bin_array_I1_usek = []
        bin_array_I2_usek = []
        bin_array_I3_usek = []
        bin_array_I4_usek = []
        bin_array_M5_smerVyh = []
        bin_array_M7_volnost = []
        bin_array_M1_priecestie = []
        bin_array_M29_PreOdh = []

        while True: #arbitrážny cyklus
            citanie = True
            try:
                byteI1usek = plc.getMem('IB2', True)
                byteI2usek = plc.getMem('IB3', True)
                byteI3usek = plc.getMem('IB4', True)
                byteI4usek = plc.getMem('IB5', True)
                byteM5smerVyh = plc.getMem('MB5', True)
                byteM7volnost = plc.getMem('MB7', True)
                byteM1priecestie = plc.getMem('MB1', True)
                byteM29PreOdh = plc.getMem('MB29', True)

            except RuntimeError:
                citanie = False
                sleep(0.1)

            else:
                break

        for byte in byteI1usek: #spracovanie správy z PLC do bytearray
            for i in range(8):  
                bin_array_I1_usek.append((byte >> i) & 1)

        for byte in byteI2usek:
            for i in range(8):  
                bin_array_I2_usek.append((byte >> i) & 1)

        for byte in byteI3usek:
            for i in range(8):  
                bin_array_I3_usek.append((byte >> i) & 1)

        for byte in byteI4usek:
            for i in range(8):  
                bin_array_I4_usek.append((byte >> i) & 1)

        for byte in byteM5smerVyh:
            for i in range(8):  
                bin_array_M5_smerVyh.append((byte >> i) & 1)

        for byte in byteM7volnost:
            for i in range(8):  
                bin_array_M7_volnost.append((byte >> i) & 1)

        for byte in byteM1priecestie:
            for i in range(8):  
                bin_array_M1_priecestie.append((byte >> i) & 1)

        for byte in byteM29PreOdh:
            for i in range(8):  
                bin_array_M29_PreOdh.append((byte >> i) & 1)

        if RiseEdgeR.detect(bool(bin_array_M7_volnost[3])): #rušenie prízaku odchodovej cesty po uovoľnení medzistaničného úseku
            dataTS['odchodR'] = False

        if RiseEdgeZR.detect(bool(bin_array_M7_volnost[3])):
            dataTS['odchodZR'] = False

        if RiseEdgeZH.detect(bool(bin_array_M7_volnost[4])):
            dataTS['odchodZH'] = False

        if RiseEdgeZL.detect(usekZL):
            dataTS['odchodZL'] = False

        if RiseEdgeH.detect(bool(bin_array_M7_volnost[4])):
            dataTS['odchodH'] = False

        if RiseEdgeL.detect(usekZL):
            dataTS['odchodL'] = False

        if FallEdgeBP.detect(dataTS['ziadZBP']):
            dataTS['ZBP']=False

        dataTS['volRZ'] = FlipFlop(Set=bool(bool(bin_array_M7_volnost[3]) and not (dataTS['odchodR'] or dataTS['odchodZR'])),   #SR obvod pre správnu indikáciu voľnosti trate
                                   Reset=(dataTS['odchodR'] or dataTS['odchodZR']or not (bool(bin_array_M7_volnost[3]))))
        
        dataTS['volZH'] = FlipFlop(Set=bool(bool(bin_array_M7_volnost[4]) and dataTS['odhlLo']),
                                   Reset=(dataTS['odchodZH'] or dataTS['odchodH'] or not (bool(bin_array_M7_volnost[4]))))

        dataTS['volLZ'] = FlipFlop(Set= usekZL and (not dataTS['odchodL']) and (not dataTS['odchodZL']),
                                   Reset=(dataTS['odchodL'] or dataTS['odchodZL'] or not usekZL))

        dataTS['predhlLo'] = bin_array_M29_PreOdh[2]    #načítanie predhlášok a odhlášok z AH Rišňovce
        dataTS['predhlSo'] = bin_array_M29_PreOdh[3]
        dataTS['odhlLo'] = bin_array_M29_PreOdh[6]
        dataTS['odhlSo'] = bin_array_M29_PreOdh[7]

        aktualnyCas = arrow.now()   #porovnanie časovej platnosti poslednej správy z ESA 44
        if (aktualnyCas - casovaPeciatkaESA) <= timedelta(seconds=15):
            muZbeLuz = usekZL
        else:
            muZbeLuz = None

        citanie = False
        # return{'RAD;RAD-ZBE': [1,1,1,1,1,1,1,1], 'ZBE': [1,1,1,1,1,1,1,1], 'P1;P2;ZBE-HLO': [1,1,1,1,1,1,1,1], 'HLO': [1,1,1,1,1,1,1,1], 'ZbeLuz': muZbeLuz,
        #     'SmerVyh': [1,1,1,1,1,1,1,1], 'Priecestie': [0,0,1,0,0,1,0,0],
        #     'TS': dataTS, 'Riadenie': dataRiadenie, 'Cesta': dataCesta, 'Navest': dataNavest}

        return {'RAD;RAD-ZBE': bin_array_I1_usek,  'ZBE': bin_array_I2_usek, 'P1;P2;ZBE-HLO': bin_array_I3_usek, 'HLO': bin_array_I4_usek, 'ZbeLuz': muZbeLuz,
            'SmerVyh': bin_array_M5_smerVyh, 'Priecestie': bin_array_M1_priecestie,
            'TS': dataTS, 'Riadenie': dataRiadenie, 'Cesta': dataCesta, 'Navest': dataNavest}

@app.put('/write/vyhybka/{meno}/{smer}')    #metóda pre ovládanie prestavovania výmen
async def writeVyhybka(meno: str, smer: bool):
    global plc
    global zapis
    global citanie

    ack = True
    while zapis and citanie:
        sleep(0.1)

    if not (zapis and citanie):
        if meno in ['RAD_V1', 'DISP_RAD_V1']:
            if smer:
                address = 'MX4.1'
            else:
                address = 'MX4.0'

        elif meno in ['ZBE_V1', 'ZBE_V2', 'DISP_ZBE_V1', 'DISP_ZBE_V2']:
            if smer:
                address = 'MX4.3'
            else:
                address = 'MX4.2'

        elif meno in ['ZBE_V3', 'DISP_ZBE_V3']:
            if smer:
                address = 'MX4.5'
            else:
                address = 'MX4.4'

        elif meno in ['HLO_V1', 'DISP_HLO_V1']:
            if smer:
                address = 'MX4.7'
            else:
                address = 'MX4.6'

        else:
            ack = False
            print('ERR - zapis vyhybky')

        while ack:  #arbitrážny cyklus
            zapis = True
            try:
                plc.writeMem(address, True)

            except RuntimeError:
                zapis = False
                sleep(0.1)

            else:
                break

        zapis = False

@app.put('/write/navestidlo/{stanica}/{meno}/{znak}')   #metóda pre zmenu návestného znaku na návestidlách
async def writeNavestidlo(stanica: str, meno: str, znak: str):
    global plc
    global zapis
    global citanie

    volnoESA = False

    while zapis and citanie:
        sleep(0.1)

    if not (zapis and citanie):
        if znak == 'Stoj':
            value = 0

        elif znak == 'Volno':
            value = 1
            volnoESA = True

        elif znak == 'Posun':
            value = 2

        elif znak == 'PN':
            value = 3
            volnoESA = True

        else:
            value = 0

        if stanica == 'RAD':            
            if meno in ['R_L1', 'DR_L1']:
                address = 'MB8'

            elif meno in ['R_L2', 'DR_L2']:
                address = 'MB9'

            elif meno in ['R_S', 'DR_S']:
                address = 'MB10'

            elif meno in ['R_Se1', 'DR_Se1']:
                address = 'MB11'

            else:
                print('ERR - zapis navestidla RAD')

        elif stanica == 'ZBE':
            if meno in ['Z_L', 'DZ_L']:
                address = 'MB12'

            elif meno in ['Z_BL', 'DZ_BL']:
                dataTS['volnoZBE'] = volnoESA
                address = 'MB13'

            elif meno in ['Z_S', 'DZ_S']:
                address = 'MB14'

            elif meno in ['Z_L1', 'DZ_L1']:
                address = 'MB15'

            elif meno in ['Z_L2', 'DZ_L2']:
                address = 'MB16'

            elif meno in ['Z_S1', 'DZ_S1']:
                address = 'MB17'

            elif meno in ['Z_S2', 'DZ_S2']:
                address = 'MB18'

            elif meno in ['Z_Se1', 'DZ_Se1']:
                address = 'MB19'

            elif meno in ['Z_Se2', 'DZ_Se2']:
                address = 'MB20'

            elif meno in ['Z_Se3', 'DZ_Se3']:
                address = 'MB21'

            elif meno in ['Z_Lo', 'DZ_Lo']:
                address = 'MB27'

            elif meno in ['Z_So', 'DZ_So']:
                address = 'MB28'

            else:
                print('ERR - zapis navestidla ZBE')

        elif stanica == 'HLO':
            if meno in ['H_L', 'DH_L']:
                address = 'MB22'

            elif meno in ['H_S1', 'DH_S1']:
                address = 'MB23'

            elif meno in ['H_S2', 'DH_S2']:
                address = 'MB24'

            elif meno in ['H_Se1', 'DH_Se1']:
                address = 'MB25'

            elif meno in ['H_Lo', 'DH_Lo']:
                address = 'MB27'

            elif meno in ['H_So', 'DH_So']:
                address = 'MB28'

            else:
                print('ERR - zapis navestidla HLO')

        while True: #arbitrážny cyklus
            zapis = True
            try:
                plc.writeMem(address, value)               
            except RuntimeError:
                zapis = False
                sleep(0.1)
            
            else:
                break

        zapis = False

@app.put('/write/OchrDr/{meno}/{value}')    #metóda re zápis stavaných ochranných dráh vlakových ciest
async def writeOchrDr(meno: str, value: bool):
    global plc
    global zapis
    global citanie

    while zapis and citanie:
        sleep(0.1)

    if not (zapis and citanie):
        if meno == 'ZBE_RAD_1v_OD':
            address = 'MX6.0'

        elif meno == 'ZBE_HLO_1v_OD':
            address = 'MX6.1'

        elif meno == 'ZBE_LUZ_2v_OD':
            address = 'MX6.2'

        else:
            print('ERR - zapis ochrannej drahy')

        while True: #arbitrážny cyklus
            zapis = True
            try:
                plc.writeMem(address, value)
            
            except RuntimeError:
                zapis = False
                sleep(0.1)
            
            else:
                break

        zapis = False

@app.put('/write/priecestie/{meno}/{value}')    #metóda pre manálne ovládanie priecestí
async def writePriecestie(meno: str, value: bool):
    global plc
    global zapis
    global citanie

    while zapis and citanie:
        sleep(0.1)

    if not (zapis and citanie):
        if meno in ['RAD_ZBE_priec', 'DISP_RAD_ZBE_priec']:
            address = 'MX3.2'

        elif meno in ['H_ZBE_HLO_priec', 'DISP_ZBE_HLO_priec']:
            address = 'MX3.3'

        else:
            print('ERR - zapis priecestia')

        while True: #arbitrážny cyklus
            zapis = True
            try:
                plc.writeMem(address, value)
            
            except RuntimeError:
                zapis = False
                sleep(0.1)
            
            else:
                break

        zapis = False

@app.get('/test')   #metóda pre zahájenie komunikácie REST API s aplikáciou 
async def test():
    return {'OK': True}

if __name__ == '__main__':  #spustenie rozhrania na lokálnej IP adrese zariadenia
    uvicorn.run(app, host='0.0.0.0', port=8041)