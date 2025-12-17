from navestidlo import Navestidlo
import ico

class ZoznamNavestidiel:
    def __init__(self, parent):
        self.zoznamNav:dict[int:object] = {    #slovník návestidiel
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