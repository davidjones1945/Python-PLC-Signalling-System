dictVC = {
    #################### VLAKOVÉ CESTY ####################
    'RAD_1v': {
        'start':  ['R_S'],  #počiatočné návestidlo
        'stop':  ['R_k1_fik'],  #koncové návestidlo
        'RAD_V1': [1], #smer výmeny (0 - do odbočky, 1 - do priama)
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'], #vylúčené jazdné cesty
        'Useky': ['RAD_Sk', 'RAD_V1', 'RAD_k1'], #kontrolované úseky
        'dopUseky': [],
        'PU': 'RAD_ZBE_TU1', #úsek pred počiatočným návestidlom
        '1TU': '0'   #prvý traťový úsek za odchodovou vlakovou cestou
    },
    'RAD_1o': {
        'start':  ['R_L1'],
        'stop':  ['R_S_fik'],
        'RAD_V1': [1],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_Sk', 'RAD_V1'],
        'dopUseky': [],
        'PU': 'RAD_k1',
        '1TU': 'RAD_ZBE_TU1'
    },
    'RAD_2v': {
        'start':  ['R_S'],
        'stop':  ['R_k2_fik'],
        'RAD_V1': [0],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_Sk', 'RAD_V1', 'RAD_k2'],
        'dopUseky': [],
        'PU': 'RAD_ZBE_TU1',
        '1TU': '0'
    },
    'RAD_2o': {
        'start':  ['R_L2'],
        'stop':  ['R_S_fik'],
        'RAD_V1': [0],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_Sk', 'RAD_V1'],
        'dopUseky': [],
        'PU': 'RAD_k2',
        '1TU': 'RAD_ZBE_TU1'
    },

    #################### POSUNOVÉ CESTY ####################
    'RAD_k1_Sk': {
        'start':  ['R_L1'],
        'stop':  ['R_Se1p'],
        'RAD_V1': [1],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_Sk', 'RAD_V1'],
        'dopUseky': [], #doplnkové úseky (potrebné v prípade posunu na obsadenú staničnú koľaj)
        'PU': 'RAD_k1'
    },
    'RAD_Sk_k1': {
        'start':  ['R_Se1'],
        'stop':  ['R_k1_fik'],
        'RAD_V1': [1],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_V1'],
        'dopUseky': ['RAD_k1'],
        'PU': 'RAD_Sk'
    },
    'RAD_k2_Sk': {
        'start':  ['R_L2'],
        'stop':  ['R_Se1p'],
        'RAD_V1': [0],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_V1', 'RAD_Sk'],
        'dopUseky': [],
        'PU': 'RAD_k2'
    },
    'RAD_Sk_k2': {
        'start':  ['R_Se1'],
        'stop':  ['R_k2_fik'],
        'RAD_V1': [0],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_V1'],
        'dopUseky': ['RAD_k2'],
        'PU': 'RAD_Sk'
    }
}
