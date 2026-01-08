dictVC = {
    #################### VLAKOVÉ CESTY ####################
    ##########ZHLAVIE S##########
    'ZBE_HLO_1v': {
        'start':  ['Z_S'],  #počiatočné návestidlo
        'stop':  ['Z_S1'],  #koncové návestidlo
        'ZBE_V3': [1], #smer výmeny (0 - do odbočky, 1 - do priama)
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                    'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2',
                    'ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD', 
                    'ZBE_k1L_k1'], #vylúčené jazdné cesty
        'Useky': ['ZBE_k1S', 'ZBE_V3', 'ZBE_k1'], #kontrolované úseky
        'dopUseky': [], 
        'PU': 'ZBE_HLO_TU1_1', #úsek pred počiatočným návestidlom
        '1TU': '0'   #prvý traťový úsek za odchodovou vlakovou cestou
    },

    'ZBE_HLO_1v_OD': {
        'start':  ['Z_S'],  
        'stop':  ['Z_S1'],  
        'ZBE_V1': [1], 
        'ZBE_V2': [1], 
        'ZBE_V3': [1], 
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                    'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2',
                    'ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_1o', 'ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v_OD', 
                    'ZBE_k1_k1L', 'ZBE_k1L_k1', 'ZBE_k2_k1L', 'ZBE_k1L_k2'],
        'Useky': ['ZBE_k1S', 'ZBE_V3', 'ZBE_k1'],
        'UsekyOD': ['ZBE_V1', 'ZBE_k1L'], #úseky tvoriace ochrannú dráhu
        'dopUseky': [], 
        'PU': 'ZBE_HLO_TU1_1',
        '1TU': '0'   
    },  

    'ZBE_HLO_1o': {
        'start':  ['Z_L1'],
        'stop':  ['Z_S_fik'],
        'ZBE_V3': [1],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                    'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2',
                    'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_k1S', 'ZBE_V3'],
        'dopUseky': [], 
        'PU': 'ZBE_k1',
        '1TU': 'ZBE_HLO_TU1_1'
    },      
    'ZBE_HLO_2v': {
        'start':  ['Z_S'],
        'stop':  ['Z_S2'],
        'ZBE_V3': [0],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                    'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2',
                    'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD',
                    'ZBE_k1L_k2', 'ZBE_k2BL_k2'],
        'Useky': ['ZBE_k1S', 'ZBE_V3', 'ZBE_k2'],
        'dopUseky': [], 
        'PU': 'ZBE_HLO_TU1_1',
        '1TU': '0'
    },       
    'ZBE_HLO_2o': {
        'start':  ['Z_L2'],
        'stop':  ['Z_S_fik'],
        'ZBE_V3': [0],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                    'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2',
                    'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_k1S', 'ZBE_V3'],
        'dopUseky': [], 
        'PU': 'ZBE_k2',
        '1TU': 'ZBE_HLO_TU1_1'
    },
    
    ########## ZHLAVIE L ##########
    'ZBE_RAD_1v': {
        'start':  ['Z_L'],
        'stop':  ['Z_L1'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_1o', 'ZBE_RAD_2o',
                    'ZBE_k1_k1L', 'ZBE_k1L_k1', 'ZBE_k2_k1L', 'ZBE_k1L_k2',
                    'ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 
                    'ZBE_k1S_k1'],
        'Useky': ['ZBE_k1L', 'ZBE_V1', 'ZBE_k1'],
        'dopUseky': [], 
        'PU': 'RAD_ZBE_TU4',
        '1TU': '0'
    },  

    'ZBE_RAD_1v_OD': {
        'start':  ['Z_L'],
        'stop':  ['Z_L1'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'ZBE_V3': [1],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_1o', 'ZBE_RAD_2o', 'ZBE_LUZ_2v_OD',
                   'ZBE_k1_k1L', 'ZBE_k1L_k1', 'ZBE_k2_k1L', 'ZBE_k1L_k2',
                   'ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2'],
        'Useky': ['ZBE_k1L', 'ZBE_V1', 'ZBE_k1'],
        'UsekyOD': ['ZBE_V3', 'ZBE_k1S'],
        'dopUseky': [], 
        'PU': 'RAD_ZBE_TU4',
        '1TU': '0'
    },

    'ZBE_RAD_1o': {
        'start':  ['Z_S1'],
        'stop':  ['Z_L_fik'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_1o', 'ZBE_RAD_2o',
                   'ZBE_k1_k1L', 'ZBE_k1L_k1', 'ZBE_k2_k1L', 'ZBE_k1L_k2',
                   'ZBE_HLO_1v_OD'],
        'Useky': ['ZBE_k1L', 'ZBE_V1'],
        'dopUseky': [], 
        'PU': 'ZBE_k1',
        '1TU': 'RAD_ZBE_TU4'
    },  
    'ZBE_RAD_2v': {
        'start':  ['Z_L'],
        'stop':  ['Z_L2'],
        'ZBE_V1': [0],
        'ZBE_V2': [0],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_1o', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD' 'ZBE_LUZ_2o',
                   'ZBE_k1_k1L', 'ZBE_k1L_k1', 'ZBE_k2_k1L', 'ZBE_k1L_k2', 'ZBE_k2_k2BL', 'ZBE_k2BL_k2',
                   'ZBE_HLO_1v_OD', 'ZBE_HLO_2v', 
                   'ZBE_k1_k1S', 'ZBE_k1S_k1',  'ZBE_k1S_k2'],
        'Useky': ['ZBE_k1L', 'ZBE_V1', 'ZBE_V2', 'ZBE_k2'],
        'dopUseky': [], 
        'PU': 'RAD_ZBE_TU4',
        '1TU': '0'
    },    
    'ZBE_RAD_2o': {
        'start':  ['Z_S2'],
        'stop':  ['Z_L_fik'],
        'ZBE_V1': [0],
        'ZBE_V2': [0],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_1o', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD' 'ZBE_LUZ_2o',
                   'ZBE_k1_k1L', 'ZBE_k1L_k1', 'ZBE_k2_k1L', 'ZBE_k1L_k2', 'ZBE_k2_k2BL', 'ZBE_k2BL_k2',
                   'ZBE_HLO_1v_OD'],
        'Useky': ['ZBE_k1L', 'ZBE_V1', 'ZBE_V2'],
        'dopUseky': [], 
        'PU': 'ZBE_k2',
        '1TU': 'RAD_ZBE_TU4'
    },
    'ZBE_LUZ_2v': {
        'start':  ['Z_BL'],
        'stop':  ['Z_L2'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD' 'ZBE_LUZ_2o',
                   'ZBE_k2_k1L', 'ZBE_k1L_k2', 'ZBE_k2_k2BL', 'ZBE_k2BL_k2',
                   'ZBE_HLO_2v', 
                   'ZBE_k1S_k2'],
        'Useky': ['ZBE_k2BL', 'ZBE_V2', 'ZBE_k2'],
        'dopUseky': [], 
        'PU': '0',
        '1TU': '0'
    },  
    'ZBE_LUZ_2v_OD': {
        'start':  ['Z_BL'],
        'stop':  ['Z_L2'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'ZBE_V3': [0],
        'Vyluky': ['ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD' 'ZBE_LUZ_2o',
                   'ZBE_k2_k1L', 'ZBE_k1L_k2', 'ZBE_k2_k2BL', 'ZBE_k2BL_k2',
                   'ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2'],
        'Useky': ['ZBE_k2BL', 'ZBE_V2', 'ZBE_k2'],
        'UsekyOD': ['ZBE_V3', 'ZBE_k1S'],
        'dopUseky': [], 
        'PU': '0',
        '1TU': '0'
    }, 
    'ZBE_LUZ_2o': {
        'start':  ['Z_S2'],
        'stop':  ['Z_BL_fik'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD', 'ZBE_LUZ_2o',
                   'ZBE_k2_k1L', 'ZBE_k1L_k2', 'ZBE_k2_k2BL', 'ZBE_k2BL_k2',
                   'ZBE_HLO_2v', 'ZBE_HLO_2o'],
        'Useky': ['ZBE_k2BL', 'ZBE_V2'],
        'dopUseky': [], 
        'PU': 'ZBE_k2',
        '1TU': 'ZBE_LUZ_TU1'
    },

    #################### POSUNOVÉ CESTY ####################
    ########## ZHLAVIE S ##########
    'ZBE_k1_k1S': {
        'start':  ['Z_L1'],
        'stop':  ['Z_Se3p'],
        'ZBE_V3': [1],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2',
                   'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_k1S', 'ZBE_V3'],
        'dopUseky': [], #doplnkové úseky (potrebné v prípade posunu na obsadenú staničnú koľaj)
        'PU': 'ZBE_k1'
    },   
    'ZBE_k1S_k1': {
        'start':  ['Z_Se3'],
        'stop':  ['Z_S1'],
        'ZBE_V3': [1],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2',
                   'ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_V3'],
        'dopUseky': ['ZBE_k1'],
        'PU': 'ZBE_k1S'
    },  
    'ZBE_k2_k1S': {
        'start':  ['Z_L2'],
        'stop':  ['Z_Se3p'],
        'ZBE_V3': [0],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2',
                   'ZBE_RAD_1v_OD', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_k1S', 'ZBE_V3'],
        'dopUseky': [],
        'PU': 'ZBE_k2'
    },
    'ZBE_k1S_k2': {
        'start':  ['Z_Se3'],
        'stop':  ['Z_S2'],
        'ZBE_V3': [0],
        'Vyluky': ['ZBE_HLO_1v', 'ZBE_HLO_1v_OD', 'ZBE_HLO_1o', 'ZBE_HLO_2v', 'ZBE_HLO_2o', 
                   'ZBE_k1_k1S', 'ZBE_k1S_k1', 'ZBE_k2_k1S', 'ZBE_k1S_k2',
                   'ZBE_RAD_1v_OD', 'ZBE_RAD_2v', 'ZBE_LUZ_2v_OD'],
        'Useky': ['ZBE_V3'],
        'dopUseky': ['ZBE_k2'],
        'PU': 'ZBE_k1S'
    },  

    ########## ZHLAVIE L ##########
    'ZBE_k1_k1L': {
        'start':  ['Z_S1'],
        'stop':  ['Z_Se1p'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_1o', 'ZBE_RAD_2v', 'ZBE_RAD_2o',
                   'ZBE_k1_k1L', 'ZBE_k1L_k1', 'ZBE_k2_k1L', 'ZBE_k1L_k2',
                   'ZBE_HLO_1v_OD'],
        'Useky': ['ZBE_k1L', 'ZBE_V1'],
        'dopUseky': [], 
        'PU': 'ZBE_k1'
    }, 
    'ZBE_k1L_k1': {
        'start':  ['Z_Se1'],
        'stop':  ['Z_L1'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_1o', 'ZBE_RAD_2v', 'ZBE_RAD_2o',
                   'ZBE_k1_k1L', 'ZBE_k1L_k1', 'ZBE_k2_k1L', 'ZBE_k1L_k2',
                   'ZBE_HLO_1v', 'ZBE_HLO_1v_OD'],
        'Useky': ['ZBE_V1'],
        'dopUseky': ['ZBE_k1'], 
        'PU': 'ZBE_k1L'
    },
    'ZBE_k2_k1L': {
        'start':  ['Z_S2'],
        'stop':  ['Z_Se1p'],
        'ZBE_V1': [0],
        'ZBE_V2': [0],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_1o', 'ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD', 'ZBE_LUZ_2o'
                   'ZBE_k1_k1L', 'ZBE_k1L_k1', 'ZBE_k2_k1L', 'ZBE_k1L_k2', 'ZBE_k2_k2BL', 'ZBE_k2BL_k2',
                   'ZBE_HLO_1v_OD'],
        'Useky': ['ZBE_k1L', 'ZBE_V1', 'ZBE_V2'],
        'dopUseky': [], 
        'PU': 'ZBE_k2'
    },
    'ZBE_k1L_k2': {
        'start':  ['Z_Se1'],
        'stop':  ['Z_L2'],
        'ZBE_V1': [0],
        'ZBE_V2': [0],
        'Vyluky': ['ZBE_RAD_1v', 'ZBE_RAD_1v_OD', 'ZBE_RAD_1o', 'ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD', 'ZBE_LUZ_2o'
                   'ZBE_k1_k1L', 'ZBE_k1L_k1', 'ZBE_k2_k1L', 'ZBE_k1L_k2', 'ZBE_k2_k2BL', 'ZBE_k2BL_k2',
                   'ZBE_HLO_1v_OD', 'ZBE_HLO_2v'],
        'Useky': ['ZBE_V1', 'ZBE_V2'],
        'dopUseky': ['ZBE_k2'], 
        'PU': 'ZBE_k1L'
    },   
    'ZBE_k2_k2BL': {
        'start':  ['Z_S2'],
        'stop':  ['Z_Se2p'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD', 'ZBE_LUZ_2o',
                   'ZBE_k2_k1L', 'ZBE_k1L_k2', 'ZBE_k2_k2BL', 'ZBE_k2BL_k2'],
        'Useky': ['ZBE_k2BL', 'ZBE_V2'],
        'dopUseky': [], 
        'PU': 'ZBE_k2'
    },
    'ZBE_k2BL_k2': {
        'start':  ['Z_Se2'],
        'stop':  ['Z_L2'],
        'ZBE_V1': [1],
        'ZBE_V2': [1],
        'Vyluky': ['ZBE_RAD_2v', 'ZBE_RAD_2o', 'ZBE_LUZ_2v', 'ZBE_LUZ_2v_OD', 'ZBE_LUZ_2o',
                   'ZBE_k2_k1L', 'ZBE_k1L_k2', 'ZBE_k2_k2BL', 'ZBE_k2BL_k2',
                   'ZBE_HLO_2v'],
        'Useky': ['ZBE_V2'],
        'dopUseky': ['ZBE_k2'], 
        'PU': 'ZBE_k2BL'
    },  
}
