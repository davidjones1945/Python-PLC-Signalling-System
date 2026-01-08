dictVC = {
    #################### VLAKOVÉ CESTY ####################
    ###################### RADOSINA #######################
    'RAD_1v': {
        'start':  ['R_S', 'DR_S'],  #počiatočné návestidlo
        'stop':  ['R_k1_fik', 'DR_k1_fik'],  #koncové návestidlo
        'RAD_V1': [1], #smer výmeny (0 - do odbočky, 1 - do priama)
        'DISP_RAD_V1': [1],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'], #vylúčené jazdné cesty
        'Useky': ['RAD_Sk', 'RAD_V1', 'RAD_k1',
                  'DISP_RAD_Sk', 'DISP_RAD_V1', 'DISP_RAD_k1'], #kontrolované úseky
        'dopUseky': [], #doplnkové úseky (potrebné v prípade posunu na obsadenú staničnú koľaj)
        'PU': 'RAD_ZBE_TU1', #úsek pred počiatočným návestidlom
        '1TU': '0'   #prvý traťový úsek za odchodovou vlakovou cestou
    },
    'RAD_1o': {
        'start':  ['R_L1', 'DR_L1'],
        'stop':  ['R_S_fik', 'DR_S_fik'],
        'RAD_V1': [1],
        'DISP_RAD_V1': [1],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_Sk', 'RAD_V1',
                  'DISP_RAD_Sk', 'DISP_RAD_V1'],
        'dopUseky': [],
        'PU': 'RAD_k1',
        '1TU': 'RAD_ZBE_TU1'
    },
    'RAD_2v': {
        'start':  ['R_S', 'DR_S'],
        'stop':  ['R_k2_fik', 'DR_k2_fik'],
        'RAD_V1': [0],
        'DISP_RAD_V1': [0],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_Sk', 'RAD_V1', 'RAD_k2',
                  'DISP_RAD_Sk', 'DISP_RAD_V1', 'DISP_RAD_k2'],
        'dopUseky': [],
        'PU': 'RAD_ZBE_TU1',
        '1TU': '0'
    },
    'RAD_2o': {
        'start':  ['R_L2', 'DR_L2'],
        'stop':  ['R_S_fik', 'DR_S_fik'],
        'RAD_V1': [0],
        'DISP_RAD_V1': [0],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_Sk', 'RAD_V1',
                  'DISP_RAD_Sk', 'DISP_RAD_V1'],
        'dopUseky': [],
        'PU': 'RAD_k2',
        '1TU': 'RAD_ZBE_TU1'
    },

    #################### ZBEHY ####################
    ##########ZHLAVIE S##########
    'ZBE_HLO_1v': {
        'start':  ['Z_S', 'DZ_S'],  
        'stop':  ['Z_S1', 'DZ_S1'], 
        'ZBE_V3': [1],
        'DISP_ZBE_V3': [1], 
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                    'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2',
                    'ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD', 
                    'ZBE_Lk_k1'], 
        'Useky': ['ZBE_Sk', 'ZBE_V3', 'ZBE_k1',
                  'DISP_ZBE_Sk', 'DISP_ZBE_V3', 'DISP_ZBE_k1'], 
        'dopUseky': [],
        'PU': 'ZBE_HLO_TU1_1', 
        '1TU': '0'   
    },

    'ZBE_HLO_1v_OD': {
        'start':  ['Z_S', 'DZ_S'],  
        'stop':  ['Z_S1', 'DZ_S1'],  
        'ZBE_V1': [1], 
        'ZBE_V2': [1], 
        'ZBE_V3': [1], 
        'DISP_ZBE_V1': [1], 
        'DISP_ZBE_V2': [1], 
        'DISP_ZBE_V3': [1], 
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                    'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2',
                    'ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_1o', 'ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v_OD', 
                    'ZBE_k1_Lk', 'ZBE_Lk_k1', 'ZBE_k2_Lk', 'ZBE_Lk_k2'],
        'Useky': ['ZBE_Sk', 'ZBE_V3', 'ZBE_k1',
                  'DISP_ZBE_Sk', 'DISP_ZBE_V3', 'DISP_ZBE_k1'],
        'UsekyOD': ['ZBE_V1', 'ZBE_Lk',
                    'DISP_ZBE_V1', 'DISP_ZBE_Lk'], #úseky tvoriace ochrannú dráhu
        'dopUseky': [],
        'PU': 'ZBE_HLO_TU1_1',
        '1TU': '0'   
    },  

    'ZBE_HLO_1o': {
        'start':  ['Z_L1', 'DZ_L1'],
        'stop':  ['Z_S_fik', 'DZ_S_fik'],
        'ZBE_V3': [1],
        'DISP_ZBE_V3': [1],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                    'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2',
                    'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_Sk', 'ZBE_V3',
                  'DISP_ZBE_Sk', 'DISP_ZBE_V3'],
        'dopUseky': [],
        'PU': 'ZBE_k1',
        '1TU': 'ZBE_HLO_TU1_1'
    },      
    'ZBE_HLO_2v': {
        'start':  ['Z_S', 'DZ_S'],
        'stop':  ['Z_S2', 'DZ_S2'],
        'ZBE_V3': [0],
        'DISP_ZBE_V3': [0],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                    'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2',
                    'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD',
                    'ZBE_Lk_k2', 'ZBE_BLk_k2'],
        'Useky': ['ZBE_Sk', 'ZBE_V3', 'ZBE_k2',
                  'DISP_ZBE_Sk', 'DISP_ZBE_V3', 'DISP_ZBE_k2'],
        'dopUseky': [],
        'PU': 'ZBE_HLO_TU1_1',
        '1TU': '0'
    },       
    'ZBE_HLO_2o': {
        'start':  ['Z_L2', 'DZ_L2'],
        'stop':  ['Z_S_fik', 'DZ_S_fik'],
        'ZBE_V3': [0],
        'DISP_ZBE_V3': [0],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                    'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2',
                    'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_Sk', 'ZBE_V3',
                  'DISP_ZBE_Sk', 'DISP_ZBE_V3'],
        'dopUseky': [],
        'PU': 'ZBE_k2',
        '1TU': 'ZBE_HLO_TU1_1'
    },
    
    ########## ZHLAVIE L ##########
    'ZBE_RAD_1v': {
        'start':  ['Z_L', 'DZ_L'],
        'stop':  ['Z_L1', 'DZ_L1'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'DISP_ZBE_V1': [1],
        'DISP_ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_1o', 'ZBE_RAD_2o',
                    'ZBE_k1_Lk', 'ZBE_Lk_k1', 'ZBE_k2_Lk', 'ZBE_Lk_k2',
                    'ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 
                    'ZBE_Sk_k1'],
        'Useky': ['ZBE_Lk', 'ZBE_V1', 'ZBE_k1',
                  'DISP_ZBE_Lk', 'DISP_ZBE_V1', 'DISP_ZBE_k1'],
        'dopUseky': [],
        'PU': 'RAD_ZBE_TU4',
        '1TU': '0'
    },  

    'ZBE_RAD_1v_OD': {
        'start':  ['Z_L', 'DZ_L'],
        'stop':  ['Z_L1', 'DZ_L1'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'ZBE_V3': [1],
        'DISP_ZBE_V1': [1],
        'DISP_ZBE_V2': [1],
        'DISP_ZBE_V3': [1],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_1o', 'ZBE_RAD_2o', 'ZBE_LUZ_2v_OD',
                   'ZBE_k1_Lk', 'ZBE_Lk_k1', 'ZBE_k2_Lk', 'ZBE_Lk_k2',
                   'ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2'],
        'Useky': ['ZBE_Lk', 'ZBE_V1', 'ZBE_k1',
                  'DISP_ZBE_Lk', 'DISP_ZBE_V1', 'DISP_ZBE_k1'],
        'UsekyOD': ['ZBE_V3', 'ZBE_Sk',
                    'DISP_ZBE_V3', 'DISP_ZBE_Sk'],
        'dopUseky': [],
        'PU': 'RAD_ZBE_TU4',
        '1TU': '0'
    },

    'ZBE_RAD_1o': {
        'start':  ['Z_S1', 'DZ_S1'],
        'stop':  ['Z_L_fik', 'DZ_L_fik'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'DISP_ZBE_V1': [1],
        'DISP_ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_1o', 'ZBE_RAD_2o',
                   'ZBE_k1_Lk', 'ZBE_Lk_k1', 'ZBE_k2_Lk', 'ZBE_Lk_k2',
                   'ZBE_HLO_1v_OD'],
        'Useky': ['ZBE_Lk', 'ZBE_V1',
                  'DISP_ZBE_Lk', 'DISP_ZBE_V1'],
        'dopUseky': [],
        'PU': 'ZBE_k1',
        '1TU': 'RAD_ZBE_TU4'
    },  
    'ZBE_RAD_2v': {
        'start':  ['Z_L', 'DZ_L'],
        'stop':  ['Z_L2', 'DZ_L2'],
        'ZBE_V1': [0],
        'ZBE_V2': [0],
        'DISP_ZBE_V1': [0],
        'DISP_ZBE_V2': [0],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_1o', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD' 'ZBE_LUZ_2o',
                   'ZBE_k1_Lk', 'ZBE_Lk_k1', 'ZBE_k2_Lk', 'ZBE_Lk_k2', 'ZBE_k2_BLk', 'ZBE_BLk_k2',
                   'ZBE_HLO_1v_OD', 'ZBE_HLO_2v', 
                   'ZBE_k1_Sk', 'ZBE_Sk_k1',  'ZBE_Sk_k2'],
        'Useky': ['ZBE_Lk', 'ZBE_V1', 'ZBE_V2', 'ZBE_k2',
                  'DISP_ZBE_Lk', 'DISP_ZBE_V1', 'DISP_ZBE_V2', 'DISP_ZBE_k2'],
        'dopUseky': [],
        'PU': 'RAD_ZBE_TU4',
        '1TU': '0'
    },    
    'ZBE_RAD_2o': {
        'start':  ['Z_S2', 'DZ_S2'],
        'stop':  ['Z_L_fik', 'DZ_L_fik'],
        'ZBE_V1': [0],
        'ZBE_V2': [0],
        'DISP_ZBE_V1': [0],
        'DISP_ZBE_V2': [0],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_1o', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD' 'ZBE_LUZ_2o',
                   'ZBE_k1_Lk', 'ZBE_Lk_k1', 'ZBE_k2_Lk', 'ZBE_Lk_k2', 'ZBE_k2_BLk', 'ZBE_BLk_k2',
                   'ZBE_HLO_1v_OD'],
        'Useky': ['ZBE_Lk', 'ZBE_V1', 'ZBE_V2',
                  'DISP_ZBE_Lk', 'DISP_ZBE_V1', 'DISP_ZBE_V2'],
        'dopUseky': [],
        'PU': 'ZBE_k2',
        '1TU': 'RAD_ZBE_TU4'
    },
    'ZBE_LUZ_2v': {
        'start':  ['Z_BL', 'DZ_BL'],
        'stop':  ['Z_L2', 'DZ_L2'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'DISP_ZBE_V1': [1],
        'DISP_ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD' 'ZBE_LUZ_2o',
                   'ZBE_k2_Lk', 'ZBE_Lk_k2', 'ZBE_k2_BLk', 'ZBE_BLk_k2',
                   'ZBE_HLO_2v', 
                   'ZBE_Sk_k2'],
        'Useky': ['ZBE_BLk', 'ZBE_V2', 'ZBE_k2', 
                  'DISP_ZBE_BLk', 'DISP_ZBE_V2', 'DISP_ZBE_k2'],
        'dopUseky': [],
        'PU': 'ZBE_LUZ_TU1',
        '1TU': '0'
    },  
    'ZBE_LUZ_2v_OD': {
        'start':  ['Z_BL', 'DZ_BL'],
        'stop':  ['Z_L2', 'DZ_L2'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'ZBE_V3': [0],
        'DISP_ZBE_V1': [1],
        'DISP_ZBE_V2': [1],
        'DISP_ZBE_V3': [0],
        'Vyluky': ['ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD' 'ZBE_LUZ_2o',
                   'ZBE_k2_Lk', 'ZBE_Lk_k2', 'ZBE_k2_BLk', 'ZBE_BLk_k2',
                   'ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2'],
        'Useky': ['ZBE_BLk', 'ZBE_V2', 'ZBE_k2',
                  'DISP_ZBE_BLk', 'DISP_ZBE_V2', 'DISP_ZBE_k2'],
        'UsekyOD': ['ZBE_V3', 'ZBE_Sk',
                    'DISP_ZBE_V3', 'DISP_ZBE_Sk'],
        'dopUseky': [],
        'PU': 'ZBE_LUZ_TU1',
        '1TU': '0'
    }, 
    'ZBE_LUZ_2o': {
        'start':  ['Z_S2', 'DZ_S2'],
        'stop':  ['Z_BL_fik', 'DZ_BL_fik'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'DISP_ZBE_V1': [1],
        'DISP_ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD', 'ZBE_LUZ_2o',
                   'ZBE_k2_Lk', 'ZBE_Lk_k2', 'ZBE_k2_BLk', 'ZBE_BLk_k2',
                   'ZBE_HLO_2v', 'ZBE_HLO_2o'],
        'Useky': ['ZBE_BLk', 'ZBE_V2',
                  'DISP_ZBE_BLk', 'DISP_ZBE_V2'],
        'dopUseky': [],
        'PU': 'ZBE_k2',
        '1TU': 'ZBE_LUZ_TU1'
    },

    #################### HLOHOVEC ####################
    'HLO_1v': {
        'start':  ['H_L','DH_L'],  
        'stop':  ['H_k1_fik', 'DH_k1_fik'],  
        'HLO_V1': [1],
        'DISP_HLO_V1': [1],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'], 
        'Useky': ['HLO_Sk', 'HLO_V1', 'HLO_k1',
                  'DISP_HLO_Sk', 'DISP_HLO_V1', 'DISP_HLO_k1'],
        'dopUseky': [],
        'PU': 'ZBE_HLO_TU2_b', 
        '1TU': '0'  
    },
    'HLO_1o': {
        'start':  ['H_S1', 'DH_S1'],
        'stop':  ['H_L_fik', 'DH_L_fik'],
        'HLO_V1': [1],
        'DISP_HLO_V1': [1],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_Sk', 'HLO_V1',
                  'DISP_HLO_Sk', 'DISP_HLO_V1'],
        'dopUseky': [],
        'PU': 'HLO_k1',
        '1TU': 'ZBE_HLO_TU2_b'
    },
    'HLO_2v': {
        'start':  ['H_L', 'DH_L'],
        'stop':  ['H_k2_fik', 'DH_k2_fik'],
        'HLO_V1': [0],
        'DISP_HLO_V1': [0],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_Sk', 'HLO_V1', 'HLO_k2',
                  'DISP_HLO_Sk', 'DISP_HLO_V1', 'DISP_HLO_k2'],
        'dopUseky': [],
        'PU': 'ZBE_HLO_TU2_b',
        '1TU': '0'
    },
    'HLO_2o': {
        'start':  ['H_S2', 'DH_S2'],
        'stop':  ['H_L_fik', 'DH_L_fik'],
        'HLO_V1': [0],
        'DISP_HLO_V1': [0],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_Sk', 'HLO_V1',
                  'DISP_HLO_Sk', 'DISP_HLO_V1'],
        'dopUseky': [],
        'PU': 'HLO_k2',
        '1TU': 'ZBE_HLO_TU2_b'
    },

    #################### POSUNOVÉ CESTY ####################
    #################### RADOSINA ####################
    'RAD_k1_Sk': {
        'start':  ['R_L1'],
        'stop':  ['R_Se1p'],
        'RAD_V1': [1],
        'DISP_RAD_V1': [1],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_Sk', 'RAD_V1',
                  'DISP_RAD_Sk', 'DISP_RAD_V1'],
        'dopUseky': [], 
        'PU': 'RAD_k1'
    },
    'RAD_Sk_k1': {
        'start':  ['R_Se1'],
        'stop':  ['R_k1_fik'],
        'RAD_V1': [1],
        'DISP_RAD_V1': [1],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_V1',
                  'DISP_RAD_V1'],
        'dopUseky': ['RAD_k1',
                     'DISP_RAD_k1'],
        'PU': 'RAD_Sk'
    },
    'RAD_k2_Sk': {
        'start':  ['R_L2'],
        'stop':  ['R_Se1p'],
        'RAD_V1': [0],
        'DISP_RAD_V1': [0],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_V1', 'RAD_Sk',
                  'DISP_RAD_V1', 'DISP_RAD_Sk'],
        'dopUseky': [],
        'PU': 'RAD_k2'
    },
    'RAD_Sk_k2': {
        'start':  ['R_Se1'],
        'stop':  ['R_k2_fik'],
        'RAD_V1': [0],
        'DISP_RAD_V1': [0],
        'Vyluky': ['RAD_1v', 'RAD_1o', 'RAD_2v', 'RAD_2o', 'RAD_k1_Sk', 'RAD_Sk_k1', 'RAD_k2_Sk', 'RAD_Sk_k2'],
        'Useky': ['RAD_V1',
                  'DISP_RAD_V1'],
        'dopUseky': ['RAD_k2',
                     'DISP_RAD_k2'],
        'PU': 'RAD_Sk'
    },

    #################### ZBEHY ####################
    ########## ZHLAVIE S ##########
    'ZBE_k1_Sk': {
        'start':  ['Z_L1'],
        'stop':  ['Z_Se3p'],
        'ZBE_V3': [1],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2',
                   'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_Sk', 'ZBE_V3',
                  'DISP_ZBE_Sk', 'DISP_ZBE_V3'],
        'dopUseky': [], 
        'PU': 'ZBE_k1'
    },   
    'ZBE_Sk_k1': {
        'start':  ['Z_Se3'],
        'stop':  ['Z_S1'],
        'ZBE_V3': [1],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2',
                   'ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_V3',
                  'DISP_ZBE_V3'],
        'dopUseky': ['ZBE_k1',
                     'DISP_ZBE_k1'],
        'PU': 'ZBE_Sk'
    },  
    'ZBE_k2_Sk': {
        'start':  ['Z_L2'],
        'stop':  ['Z_Se3p'],
        'ZBE_V3': [0],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2',
                   'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_Sk', 'ZBE_V3',
                  'DISP_ZBE_Sk', 'DISP_ZBE_V3'],
        'dopUseky': [],
        'PU': 'ZBE_k2'
    },
    'ZBE_Sk_k2': {
        'start':  ['Z_Se3'],
        'stop':  ['Z_S2'],
        'ZBE_V3': [0],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_Sk', 'ZBE_Sk_k1', 'ZBE_k2_Sk', 'ZBE_Sk_k2',
                   'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_V3',
                  'DISP_ZBE_V3'],
        'dopUseky': ['ZBE_k2',
                     'DISP_ZBE_k2'],
        'PU': 'ZBE_Sk'
    },  

    ########## ZHLAVIE L ##########
    'ZBE_k1_Lk': {
        'start':  ['Z_S1'],
        'stop':  ['Z_Se1p'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_1o', 'ZBE_RAD_2v', 'ZBE_RAD_2o',
                   'ZBE_k1_Lk', 'ZBE_Lk_k1', 'ZBE_k2_Lk', 'ZBE_Lk_k2',
                   'ZBE_HLO_1v_OD'],
        'Useky': ['ZBE_Lk', 'ZBE_V1',
                  'DISP_ZBE_Lk', 'DISP_ZBE_V1'],
        'dopUseky': [], 
        'PU': 'ZBE_k1'
    }, 
    'ZBE_Lk_k1': {
        'start':  ['Z_Se1'],
        'stop':  ['Z_L1'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_1o', 'ZBE_RAD_2v', 'ZBE_RAD_2o',
                   'ZBE_k1_Lk', 'ZBE_Lk_k1', 'ZBE_k2_Lk', 'ZBE_Lk_k2',
                   'ZBE_HLO_1v', 'ZBE_HLO_1v_OD'],
        'Useky': ['ZBE_V1',
                  'DISP_ZBE_V1'],
        'dopUseky': ['ZBE_k1',
                     'DISP_ZBE_k1'], 
        'PU': 'ZBE_Lk'
    },
    'ZBE_k2_Lk': {
        'start':  ['Z_S2'],
        'stop':  ['Z_Se1p'],
        'ZBE_V1': [0],
        'ZBE_V2': [0],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_1o', 'ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD', 'ZBE_LUZ_2o'
                   'ZBE_k1_Lk', 'ZBE_Lk_k1', 'ZBE_k2_Lk', 'ZBE_Lk_k2', 'ZBE_k2_BLk', 'ZBE_BLk_k2',
                   'ZBE_HLO_1v_OD'],
        'Useky': ['ZBE_Lk', 'ZBE_V1', 'ZBE_V2',
                  'DISP_ZBE_Lk', 'DISP_ZBE_V1', 'DISP_ZBE_V2'],
        'dopUseky': [], 
        'PU': 'ZBE_k2'
    },
    'ZBE_Lk_k2': {
        'start':  ['Z_Se1'],
        'stop':  ['Z_L2'],
        'ZBE_V1': [0],
        'ZBE_V2': [0],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_1o', 'ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD', 'ZBE_LUZ_2o'
                   'ZBE_k1_Lk', 'ZBE_Lk_k1', 'ZBE_k2_Lk', 'ZBE_Lk_k2', 'ZBE_k2_BLk', 'ZBE_BLk_k2',
                   'ZBE_HLO_1v_OD', 'ZBE_HLO_2v'],
        'Useky': ['ZBE_V1', 'ZBE_V2',
                  'DISP_ZBE_V1', 'DISP_ZBE_V2'],
        'dopUseky': ['ZBE_k2',
                     'DISP_ZBE_k2'], 
        'PU': 'ZBE_Lk'
    },   
    'ZBE_k2_BLk': {
        'start':  ['Z_S2'],
        'stop':  ['Z_Se2p'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD', 'ZBE_LUZ_2o',
                   'ZBE_k2_Lk', 'ZBE_Lk_k2', 'ZBE_k2_BLk', 'ZBE_BLk_k2'],
        'Useky': ['ZBE_BLk', 'ZBE_V2',
                  'DISP_ZBE_BLk', 'DISP_ZBE_V2'],
        'dopUseky': [], 
        'PU': 'ZBE_k2'
    },
    'ZBE_BLk_k2': {
        'start':  ['Z_Se2'],
        'stop':  ['Z_L2'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD', 'ZBE_LUZ_2o',
                   'ZBE_k2_Lk', 'ZBE_Lk_k2', 'ZBE_k2_BLk', 'ZBE_BLk_k2',
                   'ZBE_HLO_2v'],
        'Useky': ['ZBE_V2',
                  'DISP_ZBE_V2'],
        'dopUseky': ['ZBE_k2',
                     'DISP_ZBE_k2'], 
        'PU': 'ZBE_BLk'
    },

    #################### HLOHOVEC ####################
    'HLO_k1_Sk': {
        'start':  ['H_S1'],
        'stop':  ['H_Se1p'],
        'HLO_V1': [1],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_Sk', 'HLO_V1',
                  'DISP_HLO_Sk', 'DISP_HLO_V1'],
        'dopUseky': [], 
        'PU': 'HLO_k1'
    },
    'HLO_Sk_k1': {
        'start':  ['H_Se1'],
        'stop':  ['H_k1_fik'],
        'HLO_V1': [1],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_V1',
                  'DISP_HLO_V1'],
        'dopUseky': ['HLO_k1',
                     'DISP_HLO_k1'],
        'PU': 'HLO_Sk'
    },
    'HLO_k2_Sk': {
        'start':  ['H_S2'],
        'stop':  ['H_Se1p'],
        'HLO_V1': [0],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_V1', 'HLO_Sk',
                  'DISP_HLO_V1', 'DISP_HLO_Sk'],
        'dopUseky': [],
        'PU': 'HLO_k2'
    },
    'HLO_Sk_k2': {
        'start':  ['H_Se1'],
        'stop':  ['H_k2_fik'],
        'HLO_V1': [0],
        'Vyluky': ['HLO_1v', 'HLO_1o', 'HLO_2v', 'HLO_2o', 'HLO_k1_Sk', 'HLO_Sk_k1', 'HLO_k2_Sk', 'HLO_Sk_k2'],
        'Useky': ['HLO_V1',
                  'DISP_HLO_V1'],
        'dopUseky': ['HLO_k2',
                     'DISP_HLO_k2'],
        'PU': 'HLO_Sk'
    }
}