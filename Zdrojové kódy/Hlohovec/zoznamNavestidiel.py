from navestidlo import Navestidlo
import ico

class ZoznamNavestidiel:
    def __init__(self, parent):
        self.zoznamNav:dict[int:object] = {    #slovník návestidiel
            35: Navestidlo(ID=35, nazov='H_Se1', usekPred='HLO_Sk', usekZa='HLO_V1', nazovGUI='HLO_zr_do_st_odZ', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=self),
            36: Navestidlo(ID=36, nazov='H_Se1p', usekPred='HLO_Sk', nazovGUI='HLO_zr_zo_st_odZ', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL, app=self),
            37: Navestidlo(ID=37, nazov='H_L', usekPred='ZBE_HLO_TU2_b', usekZa='HLO_Sk', nazovGUI='HLO_L', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self),
            38: Navestidlo(ID=38, nazov='H_S1', usekPred='HLO_k1', usekZa='HLO_V1', nazovGUI='HLO_S1', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, app=self),
            39: Navestidlo(ID=39, nazov='H_S2', usekPred='HLO_k2', usekZa='HLO_V1', nazovGUI='HLO_S2', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, app=self),
            40: Navestidlo(ID=40, nazov='H_L_fik', usekPred='HLO_Sk', nazovGUI='HLO_fik_L', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            41: Navestidlo(ID=41, nazov='H_ZBE_L_fik', usekPred='ZBE_HLO_TU1_1', nazovGUI='ZBE_fik_S', enumIkon=ico.FiktL, dictIkon=ico.dictFiktL, app=self),
            42: Navestidlo(ID=42, nazov='H_k1_fik', usekPred='HLO_k1', nazovGUI='HLO_1k_fik', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, app=self),
            43: Navestidlo(ID=43, nazov='H_k2_fik', usekPred='HLO_k2', nazovGUI='HLO_2k_fik', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, app=self),
            44: Navestidlo(ID=44, nazov='H_Lo', usekPred='ZBE_HLO_TU1_1', usekZa='ZBE_HLO_TU2_a', nazovGUI='ZBE_HLO_Lo', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=self, oddielove=True, TZZ='AH'),
            45: Navestidlo(ID=45, nazov='H_So', usekPred='ZBE_HLO_TU2_a', usekZa='ZBE_HLO_TU1_1', nazovGUI='ZBE_HLO_So', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=self, oddielove=True, TZZ='AH')
            }             