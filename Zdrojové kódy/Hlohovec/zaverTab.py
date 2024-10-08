dictVC = {
    #################### VLAKOVÉ CESTY ####################
    'HLO_1v': {
        'start':  ['H_L'],  #počiatočné návestidlo
        'stop':  ['H_k1_fik'],  #koncové návestidlo
        'HLO_V1': [1], #smer výmeny (0 - do odbočky, 1 - do priama)
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'], #vylúčené jazdné cesty
        'Useky': ['HLO_Sk', 'HLO_V1', 'HLO_k1'], #kontrolované úseky
        'dopUseky': [],
        'PU': 'ZBE_HLO_TU2_b', #úsek pred počiatočným návestidlom
        '1TU': '0'   #prvý traťový úsek za odchodovou vlakovou cestou
    },
    'HLO_1o': {
        'start':  ['H_S1'],
        'stop':  ['H_L_fik'],
        'HLO_V1': [1],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_Sk', 'HLO_V1'],
        'dopUseky': [],
        'PU': 'HLO_k1',
        '1TU': 'ZBE_HLO_TU2_b'
    },
    'HLO_2v': {
        'start':  ['H_L'],
        'stop':  ['H_k2_fik'],
        'HLO_V1': [0],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_Sk', 'HLO_V1', 'HLO_k2'],
        'dopUseky': [],
        'PU': 'ZBE_HLO_TU2_b',
        '1TU': '0'
    },
    'HLO_2o': {
        'start':  ['H_S2'],
        'stop':  ['H_L_fik'],
        'HLO_V1': [0],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_Sk', 'HLO_V1'],
        'dopUseky': [],
        'PU': 'HLO_k2',
        '1TU': 'ZBE_HLO_TU2_b'
    },

    #################### POSUNOVÉ CESTY ####################
    'HLO_k1_Sk': {
        'start':  ['H_S1'],
        'stop':  ['H_Se1p'],
        'HLO_V1': [1],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_Sk', 'HLO_V1'],
        'dopUseky': [], #doplnkové úseky (potrebné v prípade posunu na obsadenú staničnú koľaj)
        'PU': 'HLO_k1'
    },
    'HLO_Sk_k1': {
        'start':  ['H_Se1'],
        'stop':  ['H_k1_fik'],
        'HLO_V1': [1],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_V1'],
        'dopUseky': ['HLO_k1'],
        'PU': 'HLO_Sk'
    },
    'HLO_k2_Sk': {
        'start':  ['H_S2'],
        'stop':  ['H_Se1p'],
        'HLO_V1': [0],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_V1', 'HLO_Sk'],
        'dopUseky': [],
        'PU': 'HLO_k2'
    },
    'HLO_Sk_k2': {
        'start':  ['H_Se1'],
        'stop':  ['H_k2_fik'],
        'HLO_V1': [0],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_V1'],
        'dopUseky': ['HLO_k2'],
        'PU': 'HLO_Sk'
    }
}
