from navestidlo import Navestidlo
import ico

class ZoznamNavestidiel:
    def __init__(self, parent):
        self.zoznamNav:dict[int:object] = {    #slovník návestidiel
            1: Navestidlo(ID=1, nazov='R_Se1', usekPred='RAD_Sk', usekZa='RAD_V1', nazovGUI='RAD_zr_do_st_odZ', enumIkon=ico.NavZriadL, dictIkon=ico.dictZriadovacieL,app=parent, comboBox='zriadovacie'),
            2: Navestidlo(ID=2, nazov='R_Se1p', usekPred='RAD_Sk', nazovGUI='RAD_zr_zo_st_odZ', enumIkon=ico.NavZriadP, dictIkon=ico.dictZriadovacieP, app=parent, comboBox='zriadovacie'),
            3: Navestidlo(ID=3, nazov='R_S', usekPred='RAD_ZBE_TU1', usekZa='RAD_Sk', nazovGUI='RAD_S', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, zavisle=46, app=parent, comboBox='vchodove'),
            4: Navestidlo(ID=4, nazov='R_L1', usekPred='RAD_k1', usekZa='RAD_V1', nazovGUI='RAD_L1', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, zavisle=47, app=parent, comboBox='odchodove'),
            5: Navestidlo(ID=5, nazov='R_L2', usekPred='RAD_k2', usekZa='RAD_V1', nazovGUI='RAD_L2', enumIkon=ico.NavOdchodP, dictIkon=ico.dictOdchodoveP, zavisle=48, app=parent, comboBox='odchodove'),
            6: Navestidlo(ID=6, nazov='R_S_fik', usekPred='RAD_Sk', nazovGUI='RAD_fik_S', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, zavisle=49, app=parent, comboBox='fiktivne'),
            7: Navestidlo(ID=7, nazov='R_29_fik', usekPred='RAD_ZBE_TU2_2', nazovGUI='RAD_fik_29', enumIkon=ico.FiktP, dictIkon=ico.dictFiktP, app=parent, comboBox='fiktivne'),
            8: Navestidlo(ID=8, nazov='R_19', usekPred='RAD_ZBE_TU1', usekZa='RAD_ZBE_TU2_1', nazovGUI='RAD_ZBE_19', enumIkon=ico.NavVchodP, dictIkon=ico.dictVchodoveP, app=parent, oddielove=True, TZZ='AB3'),
            9: Navestidlo(ID=9, nazov='R_18', usekPred='RAD_ZBE_TU2_1', usekZa='RAD_ZBE_TU1', nazovGUI='RAD_ZBE_18', enumIkon=ico.NavVchodL, dictIkon=ico.dictVchodoveL, app=parent, oddielove=True, TZZ='AB3'),
            10: Navestidlo(ID=10, nazov='R_k1_fik', usekPred='RAD_k1', nazovGUI='RAD_k1_fik', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, zavisle=50, app=parent, comboBox='odchodove'),
            11: Navestidlo(ID=11, nazov='R_k2_fik', usekPred='RAD_k2', nazovGUI='RAD_k2_fik', enumIkon=ico.NavOdchodL, dictIkon=ico.dictOdchodoveL, zavisle=51, app=parent, comboBox='odchodove'),
        }