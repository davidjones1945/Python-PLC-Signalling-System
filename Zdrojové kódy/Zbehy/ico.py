from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
import enum

icon_ASVC_vypnute = QIcon()

class NavZriadL(enum.Enum):
    STOJ = 'icon_zr_stojL' #posun zakázaný
    STOJ_V = 'icon_zr_stojL_v'  #posun zakázaný, výber návestidla
    STOJ_OBS = 'icon_zr_stojL_obs'  #posun zakázaný, obsadený úsek pred
    STOJ_OBS_V = 'icon_zr_stojL_obs_v'    #posun zakázaný, výber návestidla, obsadený úsek pred
    STOJ_STAVANIE_START = 'icon_zr_stojL'   #posun zakázaný, výber posunovej cesty
    STOJ_STAVANIE_START_OBS = 'icon_zr_stojL_obs'   #posun zakázaný, výber posunovej cesty
    STOJ_VC = 'icon_zr_stojL_vc'    #posun zakázaný, úsek pred návestidlom vo vlakovej ceste
    STOJ_PC = 'icon_zr_stojL_pc'    #posun zakázaný, úsek pred návestidlov v posunovej ceste
    STOJ_OD = 'icon_zr_stojL_od'    #posun zakázaný, úsek pred návestidlov v ochrannej dráhe
    STOJ_ZAVER_STAVANIE = 'icon_zr_stojL_zaver_stavanie' #posun zakázaný, žltý index cesty
    STOJ_ZAVER_PC = 'icon_zr_stojL_zaver_pc' #posun zakázaný, biely index cesty
    STOJ_ZAVER_PC_VYB = 'icon_zr_stojL_zaver_pc_v' #posun zakázaný, biely index cesty, výber návestidla
    RUSENIE = 'icon_zr_stojL_rusenie_cesty' #posun zakázaný, fialový index cesty
    POSUN = 'icon_zr_posunL' #posun
    POSUN_V = 'icon_zr_posunL_v' #posun, výber návestidla   
    POSUN_OBS = 'icon_zr_posunL_obs' #posun, obsadený úsek pred návestidlom
    POSUN_V_OBS = 'icon_zr_posunL_v_obs' #posun, obsadený úsek pred návestidlom, výber návestidla  

class NavZriadP(enum.Enum):
    STOJ = 'icon_zr_stojP'
    STOJ_V = 'icon_zr_stojP_v'
    STOJ_OBS = 'icon_zr_stojP_obs'
    STOJ_OBS_V = 'icon_zr_stojP_obs_v'
    STOJ_STAVANIE_START = 'icon_zr_stojP'
    STOJ_STAVANIE_START_OBS = 'icon_zr_stojP_obs'
    STOJ_VC = 'icon_zr_stojP_vc'
    STOJ_PC = 'icon_zr_stojP_pc'
    STOJ_OD = 'icon_zr_stojP_od'   
    STOJ_ZAVER_STAVANIE = 'icon_zr_stojP_zaver_stavanie'
    STOJ_ZAVER_PC = 'icon_zr_stojP_zaver_pc'
    STOJ_ZAVER_PC_VYB = 'icon_zr_stojP_zaver_pc_v'
    RUSENIE = 'icon_zr_stojP_rusenie_cesty'
    POSUN = 'icon_zr_posunP'
    POSUN_V = 'icon_zr_posunP_v' 
    POSUN_OBS = 'icon_zr_posunP_obs' 
    POSUN_V_OBS = 'icon_zr_posunP_v_obs'

dictZriadovacieL = {
    'icon_zr_stojL': QIcon(),
    'icon_zr_stojL_v': QIcon(),
    'icon_zr_stojL_obs': QIcon(),
    'icon_zr_stojL_obs_v': QIcon(),
    'icon_zr_stojL_vc': QIcon(),
    'icon_zr_stojL_zaver_stavanie': QIcon(),
    'icon_zr_stojL_zaver_pc': QIcon(),
    'icon_zr_stojL_zaver_pc_v': QIcon(),
    'icon_zr_stojL_pc': QIcon(),
    'icon_zr_stojL_od': QIcon(),
    'icon_zr_stojL_rusenie_cesty': QIcon(),
    'icon_zr_posunL': QIcon(),
    'icon_zr_posunL_v': QIcon(),
    'icon_zr_posunL_obs': QIcon(),
    'icon_zr_posunL_v_obs': QIcon()
}

dictZriadovacieP = {
    'icon_zr_stojP': QIcon(),
    'icon_zr_stojP_v': QIcon(),
    'icon_zr_stojP_obs': QIcon(),
    'icon_zr_stojP_obs_v': QIcon(),
    'icon_zr_stojP_vc': QIcon(),
    'icon_zr_stojP_zaver_stavanie': QIcon(),
    'icon_zr_stojP_zaver_pc': QIcon(),
    'icon_zr_stojP_zaver_pc_v': QIcon(),
    'icon_zr_stojP_pc': QIcon(),
    'icon_zr_stojP_od': QIcon(),
    'icon_zr_stojP_rusenie_cesty': QIcon(),
    'icon_zr_posunP': QIcon(),
    'icon_zr_posunP_v': QIcon(),
    'icon_zr_posunP_obs': QIcon(),
    'icon_zr_posunP_v_obs': QIcon()
}

#-------------------------------------------
#-------------------------------------------

class NavVchodL(enum.Enum):
    STOJ = 'icon_hl_stojL'  #stoj
    STOJ_V = 'icon_hl_stojL_v' #stoj, vybrané návestidlo
    STOJ_PN = 'icon_hl_stojL_PN'    #stoj, privolávacia návesť
    STOJ_V_PN = 'icon_hl_stojL_v_PN'    #stoj, výber návestidla, privolávacia návesť
    STOJ_OBS = 'icon_hl_stojL_obs' #stoj, obsadený úsek
    STOJ_OBS_V = 'icon_hl_stojL_v_obs'  #stoj, obsadený úsek, vybrané návestidlo
    STOJ_OBS_PN = 'icon_hl_stojL_obs_PN'    #stoj, obssadený úsek pred návestidlom, privolávacia návesť
    STOJ_OBS_V_PN = 'icon_hl_stojL_v_obs_PN'    #stoj, obsadený úsek pred návestidlom, výber návestidla, privolávacia návesť
    STOJ_MRTVE = 'icon_hl_stojL_mrtve' #stoj, mŕtvy úsek 
    STOJ_MRTVE_V = 'icon_hl_stojL_v_mrtve'  #stoj, mŕtvy úsek, vybrané návestidlo
    STOJ_MRTVE_PN = 'icon_hl_stojL_mrtve_PN'    #stoj, omŕtvy úsek pred návestidlom, privolávacia návesť
    STOJ_MRTVE_V_PN = 'icon_hl_stojL_v_mrtve_PN'    #stoj, mŕtvy úsek pred návestidlom, výber návestidla, privolávacia návesť 
    STOJ_STAVANIE_START = 'icon_hl_cestaL'  #stoj, zelený kruh výberu cesty
    STOJ_STAVANIE_START_OBS = 'icon_hl_cestaL_obs' #stoj, obsadený úsek, zelený kruh výberu cesty
    STOJ_STAVANIE_START_MRTVE = 'icon_hl_cestaL_mrtve' #stoj, mŕtvy úsek, zelený kruh výberu cesty
    STOJ_VC = 'icon_hl_stojL_vlak' #stoj, úsek pred návestidlom vo vlakovej ceste
    VOLNO = 'icon_hl_volnoL' #voľno
    VOLNO_V = 'icon_hl_volnoL_v' #voľno, výber návestidla
    VOLNO_OBS = 'icon_hl_volnoL_obs' #voľno, obsadený úsek pred návestidlom
    VOLNO_OBS_V = 'icon_hl_volnoL_v_obs' #voľno, obsadený úsek pred návestidlom, výber návestidla 
    VOLNO_MRTVE = 'icon_hl_volnoL_mrtve' #voľno, mŕtvy úsek pred návestidlom
    VOLNO_MRTVE_V = 'icon_hl_volnoL_v_mrtve' #voľno, mŕtvy úsek pred návestidlom, výber návestidla 
    ZHASNUTE = 'icon_hl_zhasnuteL'  #zhasnuté návestidlo
    ZHASNUTE_OBS = 'icon_hl_zhasnuteL_obs'  #zhasnuté návestidlo, obsadený úsek pred návestidlom
    RUSENIE = 'icon_hl_stojL_rusenie_cesty'
    STOJ_ZAVER_STAVANIE = 'icon_hl_zaverL_stavanie'
    STOJ_ZAVER_VC = 'icon_hl_stojL_zaver_vc'
    STOJ_ZAVER_VC_VYB = 'icon_hl_zaverL_vc_v'
    VOLNO_STAVANIE_START = 'icon_hl_cestaL_vlak'  #stoj, výber cesty, zelený index cesty
    STAV_STAVANIE_START = 'icon_hl_cestaL_stavanie'  #stoj, výber cesty, žltý index cesty
    RUS_STAVANIE_START = 'icon_hl_cestaL_rusenie'  #stoj, výber cesty, fialový index cesty    
    VOLNO_ZAVER_VC = 'icon_hl_zaverL_vc_volno'  #voľno, zelený index cesty 
    VOLNO_ZAVER_VC_VYB = 'icon_hl_zaverL_vc_v_volno'    #voľno, zelený index cesty, výber návestidla
    VOLNO_ZAVER_STAVANIE = 'icon_hl_zaverL_stavanie_volno'  #voľno, žltý index cesty      
    VOLNO_RUSENIE = 'icon_hl_volnoL_rusenie_cesty' #voľno, fialový index cesty     
    PN_ZAVER_VC = 'icon_hl_zaverL_vc_PNav'  #privolávacia návesť, zelený index cesty 
    PN_ZAVER_VC_VYB = 'icon_hl_zaverL_vc_v_PNav'    #privolávacia návesť, zelený index cesty, výber návestidla
    PN_ZAVER_STAVANIE = 'icon_hl_zaverL_stavanie_PNav'  #privolávacia návesť, žltý index cesty      
    PN_RUSENIE = 'icon_hl_PNavL_rusenie_cesty' #privolávacia návesť, fialový index cesty
    STOJ_ZAVER_PC = 'icon_hl_zaverL_pc'     #stoj, biely index cesty
    STOJ_ZAVER_PC_VYB = 'icon_hl_zaverL_pc_v'   #stoj, biely index cesty, výber návestidla
    STOJ_PC = 'icon_hl_stojL_posun' #stoj , úsek pred návestidlom v posunovej ceste
    STOJ_PC_VYB = 'icon_hl_stojL_posun_v' #stoj , úsek pred návestidlom v posunovej ceste, výber návestidla
    VOLNO_ZAVER_PC =  'icon_hl_zaverL_pc_volno' #voľno, biely index cesty
    VOLNO_ZAVER_PC_VYB = 'icon_hl_zaverL_pc_v_volno'    #voľno, biely index cesty, výber návestidla
    POSUN = 'icon_hl_posunL' #posun
    POSUN_V = 'icon_hl_posunL_v' #posun, výber návestidla   
    POSUN_OBS = 'icon_hl_posunL_obs' #posun, obsadený úsek pred návestidlom
    POSUN_V_OBS = 'icon_hl_posunL_v_obs' #posun, obsadený úsek pred návestidlom, výber návestidla  
    POSUN_MRTVE = 'icon_hl_posunL_mrtve' #posun, mŕtvy úsek pred návestidlom
    POSUN_V_MRTVE = 'icon_hl_posunL_v_mrtve' #posun, mŕtvy úsek pred návestidlom, výber návestidla  
    POSUN_ZAVER_VC = 'icon_hl_zaverL_vc_posun'  #posun, zelený index cesty 
    POSUN_ZAVER_VC_VYB = 'icon_hl_zaverL_vc_v_posun'    #posun, zelený index cesty, výber návestidla
    POSUN_ZAVER_PC =  'icon_hl_zaverL_pc_posun' #posun, biely index cesty
    POSUN_ZAVER_PC_VYB = 'icon_hl_zaverL_pc_v_posun'    #posun, biely index cesty, výber návestidla
    POSUN_ZAVER_STAVANIE = 'icon_hl_zaverL_stavanie_posun'  #posun, žltý index cesty      
    POSUN_RUSENIE = 'icon_hl_posunL_rusenie_cesty' #posun, fialový index cesty 
    PN_ZAVER_PC =  'icon_hl_zaverL_pc_PNav' #privolávacia návesť, biely index cesty
    PN_ZAVER_PC_VYB = 'icon_hl_zaverL_pc_v_PNav'    #privolávacia návesť, biely index cesty, výber návestidla
    
class NavVchodP(enum.Enum):
    STOJ = 'icon_hl_stojP' 
    STOJ_V = 'icon_hl_stojP_v' 
    STOJ_PN = 'icon_hl_stojP_PN'   
    STOJ_V_PN = 'icon_hl_stojP_v_PN'   
    STOJ_OBS = 'icon_hl_stojP_obs'
    STOJ_OBS_V = 'icon_hl_stojP_v_obs' 
    STOJ_OBS_PN = 'icon_hl_stojP_obs_PN'    
    STOJ_OBS_V_PN = 'icon_hl_stojP_v_obs_PN' 
    STOJ_MRTVE = 'icon_hl_stojP_mrtve'
    STOJ_MRTVE_V = 'icon_hl_stojP_v_mrtve' 
    STOJ_MRTVE_PN = 'icon_hl_stojP_mrtve_PN'    
    STOJ_MRTVE_V_PN = 'icon_hl_stojP_v_mrtve_PN' 
    STOJ_STAVANIE_START = 'icon_hl_cestaP'  
    STOJ_STAVANIE_START_OBS = 'icon_hl_cestaP_obs'
    STOJ_STAVANIE_START_MRTVE = 'icon_hl_cestaP_mrtve'
    STOJ_VC = 'icon_hl_stojP_vlak'    
    VOLNO = 'icon_hl_volnoP'
    VOLNO_V = 'icon_hl_volnoP_v'
    VOLNO_OBS = 'icon_hl_volnoP_obs'
    VOLNO_OBS_V = 'icon_hl_volnoP_v_obs' 
    VOLNO_MRTVE = 'icon_hl_volnoP_mrtve' 
    VOLNO_MRTVE_V = 'icon_hl_volnoP_v_mrtve'
    ZHASNUTE = 'icon_hl_zhasnuteP'  
    ZHASNUTE_OBS = 'icon_hl_zhasnuteP_obs'
    RUSENIE = 'icon_hl_stojP_rusenie_cesty'
    STOJ_ZAVER_STAVANIE = 'icon_hl_zaverP_stavanie'
    STOJ_ZAVER_VC = 'icon_hl_stojP_zaver_vc'
    STOJ_ZAVER_VC_VYB = 'icon_hl_zaverP_vc_v'
    VOLNO_STAVANIE_START = 'icon_hl_cestaP_vlak'  
    STAV_STAVANIE_START = 'icon_hl_cestaP_stavanie'  
    RUS_STAVANIE_START = 'icon_hl_cestaP_rusenie'    
    VOLNO_ZAVER_VC = 'icon_hl_zaverP_vc_volno' 
    VOLNO_ZAVER_VC_VYB = 'icon_hl_zaverP_vc_v_volno'    
    VOLNO_ZAVER_STAVANIE = 'icon_hl_zaverP_stavanie_volno'      
    VOLNO_RUSENIE = 'icon_hl_volnoP_rusenie_cesty'   
    PN_ZAVER_VC = 'icon_hl_zaverP_vc_PNav'  
    PN_ZAVER_VC_VYB = 'icon_hl_zaverP_vc_v_PNav'    
    PN_ZAVER_STAVANIE = 'icon_hl_zaverP_stavanie_PNav'     
    PN_RUSENIE = 'icon_hl_PNavP_rusenie_cesty' 
    STOJ_ZAVER_PC = 'icon_hl_zaverP_pc'    
    STOJ_ZAVER_PC_VYB = 'icon_hl_zaverP_pc_v' 
    STOJ_PC = 'icon_hl_stojP_posun'
    STOJ_PC_VYB = 'icon_hl_stojP_posun_v'
    VOLNO_ZAVER_PC =  'icon_hl_zaverP_pc_volno'
    VOLNO_ZAVER_PC_VYB = 'icon_hl_zaverP_pc_v_volno'
    POSUN = 'icon_hl_posunP'
    POSUN_V = 'icon_hl_posunP_v' 
    POSUN_OBS = 'icon_hl_posunP_obs'
    POSUN_V_OBS = 'icon_hl_posunP_v_obs'
    POSUN_MRTVE = 'icon_hl_posunP_mrtve' 
    POSUN_V_MRTVE = 'icon_hl_posunP_v_mrtve'   
    POSUN_ZAVER_VC = 'icon_hl_zaverP_vc_posun' 
    POSUN_ZAVER_VC_VYB = 'icon_hl_zaverP_vc_v_posun'
    POSUN_ZAVER_PC =  'icon_hl_zaverP_pc_posun'
    POSUN_ZAVER_PC_VYB = 'icon_hl_zaverP_pc_v_posun'
    POSUN_ZAVER_STAVANIE = 'icon_hl_zaverP_stavanie_posun'      
    POSUN_RUSENIE = 'icon_hl_posunP_rusenie_cesty'
    PN_ZAVER_PC =  'icon_hl_zaverP_pc_PNav'
    PN_ZAVER_PC_VYB = 'icon_hl_zaverP_pc_v_PNav'

dictVchodoveL = {
    'icon_hl_stojL': QIcon(),
    'icon_hl_stojL_v': QIcon(),
    'icon_hl_stojL_PN': QIcon(),
    'icon_hl_stojL_v_PN': QIcon(),
    'icon_hl_stojL_obs': QIcon(),
    'icon_hl_stojL_v_obs': QIcon(),
    'icon_hl_stojL_obs_PN': QIcon(),
    'icon_hl_stojL_v_obs_PN': QIcon(),
    'icon_hl_stojL_mrtve': QIcon(), 
    'icon_hl_stojL_v_mrtve': QIcon(), 
    'icon_hl_stojL_mrtve_PN': QIcon(), 
    'icon_hl_stojL_v_mrtve_PN': QIcon(), 
    'icon_hl_stojL_vlak': QIcon(),
    'icon_hl_cestaL': QIcon(),
    'icon_hl_cestaL_obs': QIcon(),
    'icon_hl_cestaL_mrtve': QIcon(),
    'icon_hl_volnoL': QIcon(), 
    'icon_hl_volnoL_v': QIcon(),
    'icon_hl_volnoL_obs': QIcon(),
    'icon_hl_volnoL_v_obs': QIcon(),
    'icon_hl_volnoL_mrtve': QIcon(), 
    'icon_hl_volnoL_v_mrtve': QIcon(), 
    'icon_hl_zhasnuteL': QIcon(),     
    'icon_hl_zhasnuteL_obs': QIcon(),
    'icon_hl_stojL_rusenie_cesty': QIcon(),
    'icon_hl_zaverL_stavanie': QIcon(),
    'icon_hl_stojL_zaver_vc': QIcon(),
    'icon_hl_zaverL_vc_v': QIcon(),
    'icon_hl_cestaL_vlak': QIcon(),  
    'icon_hl_cestaL_stavanie': QIcon(),  
    'icon_hl_cestaL_rusenie': QIcon(),    
    'icon_hl_zaverL_vc_volno': QIcon(), 
    'icon_hl_zaverL_vc_v_volno': QIcon(),    
    'icon_hl_zaverL_stavanie_volno': QIcon(),      
    'icon_hl_volnoL_rusenie_cesty': QIcon(),   
    'icon_hl_zaverL_vc_PNav': QIcon(),  
    'icon_hl_zaverL_vc_v_PNav': QIcon(),    
    'icon_hl_zaverL_stavanie_PNav': QIcon(),     
    'icon_hl_PNavL_rusenie_cesty': QIcon(),
    'icon_hl_zaverL_pc': QIcon(),
    'icon_hl_zaverL_pc_v': QIcon(),
    'icon_hl_stojL_posun': QIcon(),
    'icon_hl_zaverL_pc_volno': QIcon(),
    'icon_hl_zaverL_pc_v_volno': QIcon(),
    'icon_hl_posunL': QIcon(),
    'icon_hl_posunL_v': QIcon(),
    'icon_hl_posunL_obs': QIcon(),
    'icon_hl_posunL_v_obs': QIcon(), 
    'icon_hl_posunL_mrtve': QIcon(), 
    'icon_hl_posunL_v_mrtve': QIcon(), 
    'icon_hl_zaverL_vc_posun': QIcon(), 
    'icon_hl_zaverL_vc_v_posun': QIcon(),
    'icon_hl_zaverL_pc_posun': QIcon(),
    'icon_hl_zaverL_pc_v_posun': QIcon(),
    'icon_hl_zaverL_stavanie_posun': QIcon(),  
    'icon_hl_posunL_rusenie_cesty': QIcon(),
    'icon_hl_zaverL_pc_PNav': QIcon(),
    'icon_hl_zaverL_pc_v_PNav': QIcon(),
    'icon_hl_stojL_posun_v': QIcon()
}

dictVchodoveP = {
    'icon_hl_stojP': QIcon(),
    'icon_hl_stojP_v': QIcon(),
    'icon_hl_stojP_PN': QIcon(),
    'icon_hl_stojP_v_PN': QIcon(),
    'icon_hl_stojP_obs': QIcon(),
    'icon_hl_stojP_v_obs': QIcon(),
    'icon_hl_stojP_obs_PN': QIcon(),
    'icon_hl_stojP_v_obs_PN': QIcon(),
    'icon_hl_stojP_mrtve': QIcon(), 
    'icon_hl_stojP_v_mrtve': QIcon(), 
    'icon_hl_stojP_mrtve_PN': QIcon(), 
    'icon_hl_stojP_v_mrtve_PN': QIcon(),
    'icon_hl_stojP_vlak': QIcon(),
    'icon_hl_cestaP': QIcon(),
    'icon_hl_cestaP_obs': QIcon(),
    'icon_hl_cestaP_mrtve': QIcon(),
    'icon_hl_volnoP': QIcon(), 
    'icon_hl_volnoP_v': QIcon(),
    'icon_hl_volnoP_obs': QIcon(),
    'icon_hl_volnoP_v_obs': QIcon(),
    'icon_hl_volnoP_mrtve': QIcon(), 
    'icon_hl_volnoP_v_mrtve': QIcon(),
    'icon_hl_zhasnuteP': QIcon(),     
    'icon_hl_zhasnuteP_obs': QIcon(),
    'icon_hl_stojP_rusenie_cesty': QIcon(),
    'icon_hl_zaverP_stavanie': QIcon(),
    'icon_hl_stojP_zaver_vc': QIcon(),
    'icon_hl_zaverP_vc_v': QIcon(),
    'icon_hl_cestaP_vlak': QIcon(),  
    'icon_hl_cestaP_stavanie': QIcon(),  
    'icon_hl_cestaP_rusenie': QIcon(),    
    'icon_hl_zaverP_vc_volno': QIcon(), 
    'icon_hl_zaverP_vc_v_volno': QIcon(),    
    'icon_hl_zaverP_stavanie_volno': QIcon(),      
    'icon_hl_volnoP_rusenie_cesty': QIcon(),   
    'icon_hl_zaverP_vc_PNav': QIcon(),  
    'icon_hl_zaverP_vc_v_PNav': QIcon(),    
    'icon_hl_zaverP_stavanie_PNav': QIcon(),     
    'icon_hl_PNavP_rusenie_cesty': QIcon(),
    'icon_hl_zaverP_pc': QIcon(),
    'icon_hl_zaverP_pc_v': QIcon(),
    'icon_hl_stojP_posun': QIcon(),
    'icon_hl_zaverP_pc_volno': QIcon(),
    'icon_hl_zaverP_pc_v_volno': QIcon(),
    'icon_hl_posunP': QIcon(),
    'icon_hl_posunP_v': QIcon(),
    'icon_hl_posunP_obs': QIcon(),
    'icon_hl_posunP_v_obs': QIcon(), 
    'icon_hl_posunP_mrtve': QIcon(), 
    'icon_hl_posunP_v_mrtve': QIcon(),  
    'icon_hl_zaverP_vc_posun': QIcon(), 
    'icon_hl_zaverP_vc_v_posun': QIcon(),
    'icon_hl_zaverP_pc_posun': QIcon(),
    'icon_hl_zaverP_pc_v_posun': QIcon(),
    'icon_hl_zaverP_stavanie_posun': QIcon(),  
    'icon_hl_posunP_rusenie_cesty': QIcon(),
    'icon_hl_zaverP_pc_PNav': QIcon(),
    'icon_hl_zaverP_pc_v_PNav': QIcon(),
    'icon_hl_stojP_posun_v': QIcon() 
}

#-------------------------------------------
#-------------------------------------------
    
class NavOdchodP(enum.Enum):
    STOJ = 'icon_ko_stojP'  #stoj
    STOJ_V = 'icon_ko_stojP_v'  #stoj, výber návestidla
    STOJ_PN = 'icon_ko_stojP_PN'    #stoj, privolávacia návesť
    STOJ_V_PN = 'icon_ko_stojP_v_PN'    #stoj, výber návestidla, privolávacia návesť
    STOJ_OBS = 'icon_ko_stojP_obs'  #stoj, obssadený úsek pred návestidlom
    STOJ_OBS_V = 'icon_ko_stojP_v_obs'  #stoj, obsadený úsek pred návestidlom, výber návestidla
    STOJ_OBS_PN = 'icon_ko_stojP_obs_PN'    #stoj, obssadený úsek pred návestidlom, privolávacia návesť
    STOJ_OBS_V_PN = 'icon_ko_stojP_v_obs_PN'    #stoj, obsadený úsek pred návestidlom, výber návestidla, privolávacia návesť
    STOJ_STAVANIE_START = 'icon_ko_cestaP'  #stoj, výber cesty
    STOJ_STAVANIE_START_OBS = 'icon_ko_cestaP_obs'  #stoj, obsadený úsek pred návestidlom, výber cesty 
    VOLNO_STAVANIE_START = 'icon_ko_cestaP_vlak'  #stoj, výber cesty, zelený index cesty
    POSUN_STAVANIE_START = 'icon_ko_cestaP_posun'  #stoj, výber cesty, biely index cesty
    STAV_STAVANIE_START = 'icon_ko_cestaP_stavanie'  #stoj, výber cesty, žltý index cesty
    RUS_STAVANIE_START = 'icon_ko_cestaP_rusenie'  #stoj, výber cesty, fialový index cesty    
    STOJ_ZAVER_STAVANIE = 'icon_ko_zaverP_stavanie'     #stoj, žltý index cesty
    STOJ_ZAVER_VC = 'icon_ko_zaverP_vc'     #stoj, zelený index cesty
    STOJ_ZAVER_VC_VYB = 'icon_ko_zaverP_vc_v'  #stoj, zelený index cesty, výber návestidla
    STOJ_ZAVER_PC = 'icon_ko_zaverP_pc'     #stoj, biely index cesty
    STOJ_ZAVER_PC_VYB = 'icon_ko_zaverP_pc_v'   #stoj, biely index cesty, výber návestidla
    STOJ_VC = 'icon_ko_stojP_vlak'  #stoj, úsek pred návestidlom vo vlakovej ceste
    STOJ_PC = 'icon_ko_stojP_posun' #stoj , úsek pred návestidlom v posunovej ceste
    RUSENIE = 'icon_ko_stojP_rusenie_cesty' #stoj, fialový index cesty
    VOLNO = 'icon_ko_volnoP' #voľno
    VOLNO_V = 'icon_ko_volnoP_v' #voľno, výber návestidla
    VOLNO_OBS = 'icon_ko_volnoP_obs' #voľno, obsadený úsek pred návestidlom
    VOLNO_OBS_V = 'icon_ko_volnoP_v_obs' #voľno, obsadený úsek pred návestidlom, výber návestidla    
    VOLNO_ZAVER_VC = 'icon_ko_zaverP_vc_volno'  #voľno, zelený index cesty 
    VOLNO_ZAVER_VC_VYB = 'icon_ko_zaverP_vc_v_volno'    #voľno, zelený index cesty, výber návestidla
    VOLNO_ZAVER_PC =  'icon_ko_zaverP_pc_volno' #voľno, biely index cesty
    VOLNO_ZAVER_PC_VYB = 'icon_ko_zaverP_pc_v_volno'    #voľno, biely index cesty, výber návestidla
    VOLNO_ZAVER_STAVANIE = 'icon_ko_zaverP_stavanie_volno'  #voľno, žltý index cesty      
    VOLNO_RUSENIE = 'icon_ko_volnoP_rusenie_cesty' #voľno, fialový index cesty     
    POSUN = 'icon_ko_posunP' #posun
    POSUN_V = 'icon_ko_posunP_v' #posun, výber návestidla   
    POSUN_OBS = 'icon_ko_posunP_obs' #posun, obsadený úsek pred návestidlom
    POSUN_V_OBS = 'icon_ko_posunP_v_obs' #posun, obsadený úsek pred návestidlom, výber návestidla 
    POSUN_ZAVER_VC = 'icon_ko_zaverP_vc_posun'  #posun, zelený index cesty 
    POSUN_ZAVER_VC_VYB = 'icon_ko_zaverP_vc_v_posun'    #posun, zelený index cesty, výber návestidla
    POSUN_ZAVER_PC =  'icon_ko_zaverP_pc_posun' #posun, biely index cesty
    POSUN_ZAVER_PC_VYB = 'icon_ko_zaverP_pc_v_posun'    #posun, biely index cesty, výber návestidla
    POSUN_ZAVER_STAVANIE = 'icon_ko_zaverP_stavanie_posun'  #posun, žltý index cesty      
    POSUN_RUSENIE = 'icon_ko_posunP_rusenie_cesty' #posun, fialový index cesty 
    PN_ZAVER_VC = 'icon_ko_zaverP_vc_PNav'  #privolávacia návesť, zelený index cesty 
    PN_ZAVER_VC_VYB = 'icon_ko_zaverP_vc_v_PNav'    #privolávacia návesť, zelený index cesty, výber návestidla
    PN_ZAVER_PC =  'icon_ko_zaverP_pc_PNav' #privolávacia návesť, biely index cesty
    PN_ZAVER_PC_VYB = 'icon_ko_zaverP_pc_v_PNav'    #privolávacia návesť, biely index cesty, výber návestidla
    PN_ZAVER_STAVANIE = 'icon_ko_zaverP_stavanie_PNav'  #privolávacia návesť, žltý index cesty      
    PN_RUSENIE = 'icon_ko_PNavP_rusenie_cesty' #privolávacia návesť, fialový index cesty    

class NavOdchodL(enum.Enum):
    STOJ = 'icon_ko_stojL'
    STOJ_V = 'icon_ko_stojL_v'
    STOJ_PN = 'icon_ko_stojL_PN'
    STOJ_V_PN = 'icon_ko_stojL_v_PN'
    STOJ_OBS = 'icon_ko_stojL_obs'
    STOJ_OBS_V = 'icon_ko_stojL_v_obs'
    STOJ_OBS_PN = 'icon_ko_stojl_obs_PN'
    STOJ_OBS_V_PN = 'icon_ko_stojl_v_obs_PN'
    STOJ_STAVANIE_START = 'icon_ko_cestaL'
    STOJ_STAVANIE_START_OBS = 'icon_ko_cestaL_obs'
    VOLNO_STAVANIE_START = 'icon_ko_cestaL_vlak'  
    POSUN_STAVANIE_START = 'icon_ko_cestaL_posun'  
    STAV_STAVANIE_START = 'icon_ko_cestaL_stavanie'  
    RUS_STAVANIE_START = 'icon_ko_cestaL_rusenie' 
    STOJ_ZAVER_STAVANIE = 'icon_ko_zaverL_stavanie'
    STOJ_ZAVER_VC_VYB = 'icon_ko_zaverL_vc_v'
    STOJ_ZAVER_PC = 'icon_ko_zaverL_pc'
    STOJ_ZAVER_PC_VYB = 'icon_ko_zaverL_pc_v'
    STOJ_ZAVER_VC = 'icon_ko_zaverL_vc'
    STOJ_VC = 'icon_ko_stojL_vlak'
    STOJ_PC = 'icon_ko_stojL_posun'
    RUSENIE = 'icon_ko_stojL_rusenie_cesty'
    VOLNO = 'icon_ko_volnoL'
    VOLNO_V = 'icon_ko_volnoL_v' 
    VOLNO_OBS = 'icon_ko_volnoL_obs' 
    VOLNO_OBS_V = 'icon_ko_volnoL_v_obs'  
    VOLNO_ZAVER_VC = 'icon_ko_zaverL_vc_volno' 
    VOLNO_ZAVER_VC_VYB = 'icon_ko_zaverL_vc_v_volno'    
    VOLNO_ZAVER_PC =  'icon_ko_zaverL_pc_volno' 
    VOLNO_ZAVER_PC_VYB = 'icon_ko_zaverL_pc_v_volno'   
    VOLNO_ZAVER_STAVANIE = 'icon_ko_zaverL_stavanie_volno'  
    VOLNO_RUSENIE = 'icon_ko_volnoL_rusenie_cesty'  
    POSUN = 'icon_ko_posunL' 
    POSUN_V = 'icon_ko_posunL_v' 
    POSUN_OBS = 'icon_ko_posunL_obs'
    POSUN_V_OBS = 'icon_ko_posunL_v_obs'
    POSUN_ZAVER_VC = 'icon_ko_zaverL_vc_posun' 
    POSUN_ZAVER_VC_VYB = 'icon_ko_zaverL_vc_v_posun'    
    POSUN_ZAVER_PC =  'icon_ko_zaverL_pc_posun' 
    POSUN_ZAVER_PC_VYB = 'icon_ko_zaverL_pc_v_posun'   
    POSUN_ZAVER_STAVANIE = 'icon_ko_zaverL_stavanie_posun'  
    POSUN_RUSENIE = 'icon_ko_posunL_rusenie_cesty' 
    PN_ZAVER_VC = 'icon_ko_zaverL_vc_PNav' 
    PN_ZAVER_VC_VYB = 'icon_ko_zaverL_vc_v_PNav'   
    PN_ZAVER_PC =  'icon_ko_zaverL_pc_PNav' 
    PN_ZAVER_PC_VYB = 'icon_ko_zaverL_pc_v_PNav'   
    PN_ZAVER_STAVANIE = 'icon_ko_zaverL_stavanie_PNav'   
    PN_RUSENIE = 'icon_ko_PNavL_rusenie_cesty'    

dictOdchodoveP = {
    'icon_ko_stojP': QIcon(),
    'icon_ko_stojP_v': QIcon(),
    'icon_ko_stojP_PN': QIcon(),
    'icon_ko_stojP_v_PN': QIcon(),
    'icon_ko_stojP_obs': QIcon(),
    'icon_ko_stojP_v_obs': QIcon(),
    'icon_ko_stojP_obs_PN': QIcon(),
    'icon_ko_stojP_v_obs_PN': QIcon(),
    'icon_ko_cestaP': QIcon(),
    'icon_ko_cestaP_obs': QIcon(),
    'icon_ko_cestaP_vlak': QIcon(),  
    'icon_ko_cestaP_posun' : QIcon(), 
    'icon_ko_cestaP_stavanie': QIcon(),  
    'icon_ko_cestaP_rusenie': QIcon(),
    'icon_ko_stojP_vlak': QIcon(),
    'icon_ko_zaverP_stavanie': QIcon(),
    'icon_ko_zaverP_vc': QIcon(),
    'icon_ko_stojP_rusenie_cesty': QIcon(),
    'icon_ko_zaverP_vc_v': QIcon(),
    'icon_ko_zaverP_pc': QIcon(),
    'icon_ko_zaverP_pc_v': QIcon(),
    'icon_ko_stojP_posun': QIcon(),
    'icon_ko_volnoP': QIcon(),
    'icon_ko_volnoP_v': QIcon(),
    'icon_ko_volnoP_obs': QIcon(),
    'icon_ko_volnoP_v_obs': QIcon(),
    'icon_ko_zaverP_vc_volno': QIcon(),  
    'icon_ko_zaverP_vc_v_volno': QIcon(),   
    'icon_ko_zaverP_pc_volno': QIcon(), 
    'icon_ko_zaverP_pc_v_volno': QIcon(),  
    'icon_ko_zaverP_stavanie_volno': QIcon(),    
    'icon_ko_volnoP_rusenie_cesty': QIcon(),  
    'icon_ko_posunP': QIcon(),
    'icon_ko_posunP_v': QIcon(),
    'icon_ko_posunP_obs': QIcon(),
    'icon_ko_posunP_v_obs': QIcon(),
    'icon_ko_zaverP_vc_posun': QIcon(),  
    'icon_ko_zaverP_vc_v_posun': QIcon(),   
    'icon_ko_zaverP_pc_posun': QIcon(), 
    'icon_ko_zaverP_pc_v_posun': QIcon(),  
    'icon_ko_zaverP_stavanie_posun': QIcon(),    
    'icon_ko_posunP_rusenie_cesty': QIcon(),
    'icon_ko_zaverP_vc_PNav': QIcon(),  
    'icon_ko_zaverP_vc_v_PNav': QIcon(),   
    'icon_ko_zaverP_pc_PNav': QIcon(), 
    'icon_ko_zaverP_pc_v_PNav': QIcon(),  
    'icon_ko_zaverP_stavanie_PNav': QIcon(),    
    'icon_ko_PNavP_rusenie_cesty': QIcon()   
}

dictOdchodoveL = {
    'icon_ko_stojL': QIcon(),
    'icon_ko_stojL_v': QIcon(),
    'icon_ko_stojL_PN': QIcon(),
    'icon_ko_stojL_v_PN': QIcon(),
    'icon_ko_stojL_obs': QIcon(),
    'icon_ko_stojL_v_obs': QIcon(),
    'icon_ko_stojL_obs_PN': QIcon(),
    'icon_ko_stojL_v_obs_PN': QIcon(),
    'icon_ko_cestaL': QIcon(),
    'icon_ko_cestaL_obs': QIcon(),
    'icon_ko_cestaL_vlak': QIcon(),  
    'icon_ko_cestaL_posun' : QIcon(), 
    'icon_ko_cestaL_stavanie': QIcon(),  
    'icon_ko_cestaL_rusenie': QIcon(),
    'icon_ko_stojL_vlak': QIcon(),
    'icon_ko_zaverL_stavanie': QIcon(),
    'icon_ko_zaverL_vc': QIcon(),
    'icon_ko_stojL_rusenie_cesty': QIcon(),
    'icon_ko_zaverL_vc_v': QIcon(),
    'icon_ko_zaverL_pc': QIcon(),
    'icon_ko_zaverL_pc_v': QIcon(),
    'icon_ko_stojL_posun': QIcon(),
    'icon_ko_volnoL': QIcon(),
    'icon_ko_volnoL_v': QIcon(),
    'icon_ko_volnoL_obs': QIcon(),
    'icon_ko_volnoL_v_obs': QIcon(),
    'icon_ko_zaverL_vc_volno': QIcon(),  
    'icon_ko_zaverL_vc_v_volno': QIcon(),   
    'icon_ko_zaverL_pc_volno': QIcon(), 
    'icon_ko_zaverL_pc_v_volno': QIcon(),  
    'icon_ko_zaverL_stavanie_volno': QIcon(),    
    'icon_ko_volnoL_rusenie_cesty': QIcon(),   
    'icon_ko_posunL': QIcon(),
    'icon_ko_posunL_v': QIcon(), 
    'icon_ko_posunL_obs': QIcon(),
    'icon_ko_posunL_v_obs': QIcon(),
    'icon_ko_zaverL_vc_posun': QIcon(),  
    'icon_ko_zaverL_vc_v_posun': QIcon(),   
    'icon_ko_zaverL_pc_posun': QIcon(), 
    'icon_ko_zaverL_pc_v_posun': QIcon(),  
    'icon_ko_zaverL_stavanie_posun': QIcon(),    
    'icon_ko_posunL_rusenie_cesty': QIcon(),
    'icon_ko_zaverL_vc_PNav': QIcon(),  
    'icon_ko_zaverL_vc_v_PNav': QIcon(),   
    'icon_ko_zaverL_pc_PNav': QIcon(), 
    'icon_ko_zaverL_pc_v_PNav': QIcon(),  
    'icon_ko_zaverL_stavanie_PNav': QIcon(),    
    'icon_ko_PNavL_rusenie_cesty': QIcon() 
}

#-------------------------------------------
#-------------------------------------------

class FiktL(enum.Enum):
    STOJ = 'icon_fiktL' #základný obraz
    STOJ_V = 'icon_fiktL_v' #výber návestidla
    STOJ_OBS = 'icon_fiktL_obs' #obsadený úsek pred návestidlom
    STOJ_MRTVE = 'icon_fiktL_mrtve' #mŕtvy úsek pred návestidlom
    STOJ_OBS_V = 'icon_fiktL_v_obs' #obsadený úsek pred návestidlom, výber návestidla
    STOJ_ZAVER_STAVANIE = 'icon_fiktL_zaver_stavanie' #žltý index cesty
    STOJ_ZAVER_VC = 'icon_fiktL_zaver_vc'   #zelený index  cesty
    STOJ_ZAVER_VC_VYB = 'icon_fiktL_zaver_vc_v' #zelený index cesty, výber návestidla
    STOJ_VC = 'icon_fiktL_vlak' #úsek pred návestilom súčasťou vlakovej cesty
    STOJ_PC = 'icon_fiktL_posun'    #úsek pred návestidlom súčasťou posunovej cesty
    STOJ_OD = 'icon_fiktL_ochr'    #úsek pred návestidlom súčasťou ochrannej dráhy
    RUSENIE = 'icon_fiktL_rusenie_cesty'    #fialový index cesty

class FiktP(enum.Enum):
    STOJ = 'icon_fiktP'
    STOJ_V = 'icon_fiktP_v'
    STOJ_OBS = 'icon_fiktP_obs'
    STOJ_MRTVE = 'icon_fiktP_mrtve'
    STOJ_OBS_V = 'icon_fiktP_v_obs'
    STOJ_ZAVER_STAVANIE = 'icon_fiktP_zaver_stavanie'
    STOJ_ZAVER_VC = 'icon_fiktP_zaver_vc'
    STOJ_ZAVER_VC_VYB = 'icon_fiktP_zaver_vc_v'
    STOJ_VC = 'icon_fiktP_vlak'
    STOJ_PC = 'icon_fiktP_posun'
    STOJ_OD = 'icon_fiktP_ochr'
    RUSENIE = 'icon_fiktP_rusenie_cesty'

dictFiktP = {
    'icon_fiktP': QIcon(),
    'icon_fiktP_v': QIcon(),
    'icon_fiktP_obs': QIcon(),
    'icon_fiktP_mrtve': QIcon(),
    'icon_fiktP_v_obs': QIcon(),
    'icon_fiktP_vlak': QIcon(),
    'icon_fiktP_zaver_stavanie': QIcon(),
    'icon_fiktP_zaver_vc': QIcon(),
    'icon_fiktP_rusenie_cesty': QIcon(),
    'icon_fiktP_zaver_vc_v': QIcon(),
    'icon_fiktP_posun': QIcon(),
    'icon_fiktP_ochr': QIcon()
}

dictFiktL = {
    'icon_fiktL': QIcon(),
    'icon_fiktL_v': QIcon(),
    'icon_fiktL_obs': QIcon(),
    'icon_fiktL_mrtve': QIcon(),
    'icon_fiktL_v_obs': QIcon(),
    'icon_fiktL_vlak': QIcon(),
    'icon_fiktL_zaver_stavanie': QIcon(),
    'icon_fiktL_zaver_vc': QIcon(),
    'icon_fiktL_rusenie_cesty': QIcon(),
    'icon_fiktL_zaver_vc_v': QIcon(),
    'icon_fiktL_posun': QIcon(),
    'icon_fiktL_ochr': QIcon()
}

#-------------------------------------------
#-------------------------------------------

class Kolaj(enum.Enum):
    VOLNA = 'icon_kol_volna'    #voľná
    OBSAD = 'icon_kol_obsad'    #obsadená
    STAVANIE_VC = 'icon_kol_vlak'   #stavanie vlakovej cesty
    STAVANIE_PC = 'icon_kol_posun'   #stavenie posunovej cesty
    STAVANIE_OD = 'icon_kol_ochr'   #stavanie ochrannej dráhy
    VLAK = 'icon_kol_vlak'  #vlaková cesta v úseku
    POSUN = 'icon_kol_posun'    #posunová cesta v úseku
    OCHR = 'icon_kol_ochr'  #ochranná dríha v úseku
    MRTVA = 'icon_kol_mrtva' #fialová smrť

class Kolaj45(enum.Enum):
    VOLNA = 'icon_kol45_volna' 
    OBSAD = 'icon_kol45_obsad'
    MRTVA = 'icon_kol45_mrtva'

class KolajSt1(enum.Enum):
    VOLNA = 'icon_st1_volna'
    OBSAD = 'icon_st1_obsad'
    STAVANIE_VC = 'icon_st1_vlak'
    STAVANIE_PC ='icon_st1_posun'
    VLAK = 'icon_st1_vlak'
    POSUN = 'icon_st1_posun'
    MRTVA = 'icon_st1_mrtva'

class KolajSt2(enum.Enum):
    VOLNA = 'icon_st2_volna'
    OBSAD = 'icon_st2_obsad'
    STAVANIE_VC = 'icon_st2_vlak'
    STAVANIE_PC ='icon_st2_posun'
    VLAK = 'icon_st2_vlak'
    POSUN = 'icon_st2_posun'
    MRTVA = 'icon_st2_mrtva'

dictKolaj = {
    'icon_kol_volna': QIcon(),
    'icon_kol_obsad': QIcon(),
    'icon_kol_ochr': QIcon(),
    'icon_kol_vlak': QIcon(),
    'icon_kol_posun': QIcon(),
    'icon_kol_mrtva': QIcon()
}

dictKolaj45 = {
    'icon_kol45_volna': QIcon(),
    'icon_kol45_obsad': QIcon(),
    'icon_kol45_mrtva': QIcon()
}

dictStanKolaj1 = {
    'icon_st1_volna': QIcon(),
    'icon_st1_obsad': QIcon(),
    'icon_st1_vlak': QIcon(),
    'icon_st1_posun': QIcon(),
    'icon_st1_mrtva': QIcon()
}

dictStanKolaj2 = {
    'icon_st2_volna': QIcon(),
    'icon_st2_obsad': QIcon(),
    'icon_st2_vlak': QIcon(),
    'icon_st2_posun': QIcon(),
    'icon_st2_mrtva': QIcon()
}

#-------------------------------------------
#-------------------------------------------

class VyhP(enum.Enum):
    PRIAMA = 'icon_vyhP_priama' #voľná, priama
    PRIAMA_OBS = 'icon_vyhP_priama_obs' #obsadená, priama
    ODB = 'icon_vyhP_odb' #voľná, odbočka
    ODB_OBS = 'icon_vyhP_odb_obs' #obsadená, odbočka
    PRIAMA_VYBER = 'icon_vyhP_priama_vyber' #voľná, priama, výber výhybky
    PRIAMA_OBS_VYBER = 'icon_vyhP_priama_obs_v' #obsadená, priama, výber vhybky
    ODB_VYBER = 'icon_vyhP_odb_vyber' #voľná, odbočka, výber výhybky
    ODB_OBS_VYBER = 'icon_vyhP_odb_obs_v' #obsadená, odbočka, výber výhybky
    PREST_P = 'icon_vyhP_prest_P' #prestavovanie do priama
    PREST_M = 'icon_vyhP_prest_M' #prestavenie do odbočky
    STAVANIE_VC_P_P = 'icon_vyhP_vlakP' #priama, stavanie priamej vlakovej cesty
    STAVANIE_VC_P_M = 'icon_vyhP_vc_pri_M' #odbočka, stavanie priamej vlakovej cesty
    STAVANIE_VC_O_P = 'icon_vyhP_vc_odb_P' #priama, stavanie vyber odbočnej vlakovej cesty
    STAVANIE_VC_O_M = 'icon_vyhP_vlakM' #odbocka, stavanie vyber odbočnej vlakovejcesty
    STAVANIE_PC_P_P = 'icon_vyhP_posP' #priama, stavanie priamej posunovej cesty
    STAVANIE_PC_P_M = 'icon_vyhP_pc_pri_M' #odbočka, stavanie priamej posunovej cesty
    STAVANIE_PC_O_P = 'icon_vyhP_pc_odb_P' #priama, stavanie vyber odbočnej posunovej cesty
    STAVANIE_PC_O_M = 'icon_vyhP_posM' #odbočka, stavanie vyber odbočnej posunovej cesty
    STAVANIE_OD_P_P = 'icon_vyhP_ochrP' #priama, stavanie priamej ochrannej dráhy
    STAVANIE_OD_P_M = 'icon_vyhP_od_pri_M' #odbočka, stavanie priamej ochrannej dráhy
    STAVANIE_OD_O_P = 'icon_vyhP_od_odb_P' #priama, stavanie vyber odbočnej ochrannej dráhy
    STAVANIE_OD_O_M = 'icon_vyhP_ochrM' #odbočka, stavanie vyber odbočnej ochrannej dráhy
    VLAK_P = 'icon_vyhP_vlakP' #voľná, záver, priama vlaková cesta
    VLAK_M = 'icon_vyhP_vlakM' #voľná, záver, odbočna vlaková cesta
    VLAK_P_V = 'icon_vyhP_vlakP_v'  #voľná, záver, priama vlaková cesta, výber výhybky
    VLAK_M_V = 'icon_vyhP_vlakM_v'  #voľná, záver, odbočná vlaková cesta, výber výhybky
    POSUN_P = 'icon_vyhP_posP' #voľná, záver, priamy posun
    POSUN_M = 'icon_vyhP_posM' #voľná, záver, posun odbočkou
    POSUN_P_V = 'icon_vyhP_posP_v'  #voľná, záver, priamy posun, výber výhybky
    POSUN_M_V = 'icon_vyhP_posM_v'  #voľná, záver, posun odbočkou, výber výhybky
    OCHRANA_P = 'icon_vyhP_ochrP' #voľná, záver, ochranná dráha priama
    OCHRANA_M = 'icon_vyhP_ochrM' #voľná, záver, ochranná dráha do odbočky
    OCHRANA_P_V = 'icon_vyhP_ochrP_v' #voľná, záver, ochranná dráha priama, výber výhybky
    OCHRANA_M_V = 'icon_vyhP_ochrM_v' #voľná, záver, ochranná dráha do odbočky, výber výhybky
    ZAVER_P_OBS = 'icon_vyhP_zaver_pri_obs' #obsadená, záver, priama
    ZAVER_M_OBS = 'icon_vyhP_zaver_odb_obs' #obsadená, záver, odbočka
    ZAVER_P_OBS_V = 'icon_vyhP_zaver_pri_obs_v' #obsadená, záver, priama, výber výhybky
    ZAVER_M_OBS_V = 'icon_vyhP_zaver_odb_obs_v' #obsadená, záver, odbočka, výber výhybky
    ZAVER_P = 'icon_vyhP_priama'
    ZAVER_P_V = 'icon_vyhP_priama_vyber'

class VyhL(enum.Enum):
    PRIAMA = 'icon_vyhL_priama' 
    PRIAMA_OBS = 'icon_vyhL_priama_obs' 
    ODB = 'icon_vyhL_odb' 
    ODB_OBS = 'icon_vyhL_odb_obs' 
    PRIAMA_VYBER = 'icon_vyhL_priama_vyber' 
    PRIAMA_OBS_VYBER = 'icon_vyhL_priama_obs_v' 
    ODB_VYBER = 'icon_vyhL_odb_vyber'
    ODB_OBS_VYBER = 'icon_vyhL_odb_obs_v' 
    PREST_P = 'icon_vyhL_prest_P'
    PREST_M = 'icon_vyhL_prest_M'
    STAVANIE_VC_P_P = 'icon_vyhL_vlakP' 
    STAVANIE_VC_P_M = 'icon_vyhL_vc_pri_M' 
    STAVANIE_VC_O_P = 'icon_vyhL_vc_odb_P'
    STAVANIE_VC_O_M = 'icon_vyhL_vlakM' 
    STAVANIE_PC_P_P = 'icon_vyhL_posP' 
    STAVANIE_PC_P_M = 'icon_vyhL_pc_pri_M' 
    STAVANIE_PC_O_P = 'icon_vyhL_pc_odb_P' 
    STAVANIE_PC_O_M = 'icon_vyhL_posM' 
    STAVANIE_OD_P_P = 'icon_vyhL_ochrP'
    STAVANIE_OD_P_M = 'icon_vyhL_od_pri_M' 
    STAVANIE_OD_O_P = 'icon_vyhL_od_odb_P'
    STAVANIE_OD_O_M = 'icon_vyhL_ochrM' 
    VLAK_P = 'icon_vyhL_vlakP' 
    VLAK_M = 'icon_vyhL_vlakM' 
    VLAK_P_V = 'icon_vyhL_vlakP_v' 
    VLAK_M_V = 'icon_vyhL_vlakM_v' 
    POSUN_P = 'icon_vyhL_posP' 
    POSUN_M = 'icon_vyhL_posM' 
    POSUN_P_V = 'icon_vyhL_posP_v'  
    POSUN_M_V = 'icon_vyhL_posM_v' 
    OCHRANA_P = 'icon_vyhL_ochrP' 
    OCHRANA_M = 'icon_vyhL_ochrM' 
    OCHRANA_P_V = 'icon_vyhL_ochrP_v'
    OCHRANA_M_V = 'icon_vyhL_ochrM_v'
    ZAVER_P_OBS = 'icon_vyhL_zaver_pri_obs'
    ZAVER_M_OBS = 'icon_vyhL_zaver_odb_obs'
    ZAVER_P_OBS_V = 'icon_vyhL_zaver_pri_obs_v'
    ZAVER_M_OBS_V = 'icon_vyhL_zaver_odb_obs_v' 
    ZAVER_P = 'icon_vyhL_priama'
    ZAVER_P_V = 'icon_vyhL_priama_vyber'

class SpojkaA(enum.Enum):
    PRIAMA = 'icon_spojkaA_priama' #voľná, priama
    PRIAMA_OBS = 'icon_spojkaA_priama_obs' #obsadená, priama
    ODB = 'icon_spojkaA_odb' #voľná, odbočka
    ODB_OBS = 'icon_spojkaA_odb_obs' #obsadená, odbočka
    PRIAMA_VYBER = 'icon_spojkaA_priama_vyber' #voľná, priama, výber výhybky
    PRIAMA_OBS_VYBER = 'icon_spojkaA_priama_obs_v' #obsadená, priama, výber vhybky
    ODB_VYBER = 'icon_spojkaA_odb_vyber' #voľná, odbočka, výber výhybky
    ODB_OBS_VYBER = 'icon_spojkaA_odb_obs_v' #obsadená, odbočka, výber výhybky
    PREST_P = 'icon_spojkaA_prest_P' #prestavovanie do priama
    PREST_M = 'icon_spojkaA_prest_M' #prestavenie do odbočky
    STAVANIE_VC_P_P = 'icon_spojkaA_vlakP' #priama, stavanie priamej vlakovej cesty
    STAVANIE_VC_P_M = 'icon_spojkaA_vc_pri_M' #odbočka, stavanie priamej vlakovej cesty
    STAVANIE_VC_O_P = 'icon_spojkaA_vc_odb_P' #priama, stavanie vyber odbočnej vlakovej cesty
    STAVANIE_VC_O_M = 'icon_spojkaA_vlakM' #odbocka, stavanie vyber odbočnej vlakovejcesty
    STAVANIE_PC_P_P = 'icon_spojkaA_posP' #priama, stavanie priamej posunovej cesty
    STAVANIE_PC_P_M = 'icon_spojkaA_pc_pri_M' #odbočka, stavanie priamej posunovej cesty
    STAVANIE_PC_O_P = 'icon_spojkaA_pc_odb_P' #priama, stavanie vyber odbočnej posunovej cesty
    STAVANIE_PC_O_M = 'icon_spojkaA_posM' #odbočka, stavanie vyber odbočnej posunovej cesty
    STAVANIE_OD_P_P = 'icon_spojkaA_ochrP' #priama, stavanie priamej ochrannej dráhy
    STAVANIE_OD_P_M = 'icon_spojkaA_od_pri_M' #odbočka, stavanie priamej ochrannej dráhy
    VLAK_P = 'icon_spojkaA_vlakP' #voľná, záver, priama vlaková cesta
    VLAK_M = 'icon_spojkaA_vlakM' #voľná, záver, odbočna vlaková cesta
    VLAK_P_V = 'icon_spojkaA_vlakP_v'  #voľná, záver, priama vlaková cesta, výber výhybky
    VLAK_M_V = 'icon_spojkaA_vlakM_v'  #voľná, záver, odbočná vlaková cesta, výber výhybky
    POSUN_P = 'icon_spojkaA_posP' #voľná, záver, priamy posun
    POSUN_M = 'icon_spojkaA_posM' #voľná, záver, posun odbočkou
    POSUN_P_V = 'icon_spojkaA_posP_v'  #voľná, záver, priamy posun, výber výhybky
    POSUN_M_V = 'icon_spojkaA_posM_v'  #voľná, záver, posun odbočkou, výber výhybky
    OCHRANA_P = 'icon_spojkaA_ochrP' #voľná, záver, ochranná dráha priama
    OCHRANA_P_V = 'icon_spojkaA_ochrP_v' #voľná, záver, ochranná dráha priama, výber výhybky
    ZAVER_P_OBS = 'icon_spojkaA_zaver_pri_obs' #obsadená, záver, priama
    ZAVER_M_OBS = 'icon_spojkaA_zaver_odb_obs' #obsadená, záver, odbočka
    ZAVER_P_OBS_V = 'icon_spojkaA_zaver_pri_obs_v' #obsadená, záver, priama, výber výhybky
    ZAVER_M_OBS_V = 'icon_spojkaA_zaver_odb_obs_v' #obsadená, záver, odbočka, výber výhybky
    ZAVER_P = 'icon_spojkaA_zaver_pri' #voľná, záver, priama
    ZAVER_P_V = 'icon_spojkaA_zaver_pri_v' #voľná, záver, priama, výber výhybky

class SpojkaB(enum.Enum):
    PRIAMA = 'icon_spojkaB_priama' 
    PRIAMA_OBS = 'icon_spojkaB_priama_obs' 
    ODB = 'icon_spojkaB_odb' 
    ODB_OBS = 'icon_spojkaB_odb_obs' 
    PRIAMA_VYBER = 'icon_spojkaB_priama_vyber' 
    PRIAMA_OBS_VYBER = 'icon_spojkaB_priama_obs_v' 
    ODB_VYBER = 'icon_spojkaB_odb_vyber'
    ODB_OBS_VYBER = 'icon_spojkaB_odb_obs_v' 
    PREST_P = 'icon_spojkaB_prest_P' 
    PREST_M = 'icon_spojkaB_prest_M'
    STAVANIE_VC_P_P = 'icon_spojkaB_vlakP' 
    STAVANIE_VC_P_M = 'icon_spojkaB_vc_pri_M' 
    STAVANIE_VC_O_P = 'icon_spojkaB_vc_odb_P' 
    STAVANIE_VC_O_M = 'icon_spojkaB_vlakM'
    STAVANIE_PC_P_P = 'icon_spojkaB_posP'
    STAVANIE_PC_P_M = 'icon_spojkaB_pc_pri_M' 
    STAVANIE_PC_O_P = 'icon_spojkaB_pc_odb_P'
    STAVANIE_PC_O_M = 'icon_spojkaB_posM' 
    STAVANIE_OD_P_P = 'icon_spojkaB_ochrP' 
    STAVANIE_OD_P_M = 'icon_spojkaB_od_pri_M' 
    VLAK_P = 'icon_spojkaB_vlakP' 
    VLAK_M = 'icon_spojkaB_vlakM' 
    VLAK_P_V = 'icon_spojkaB_vlakP_v'  
    VLAK_M_V = 'icon_spojkaB_vlakM_v'  
    POSUN_P = 'icon_spojkaB_posP' 
    POSUN_M = 'icon_spojkaB_posM' 
    POSUN_P_V = 'icon_spojkaB_posP_v'  
    POSUN_M_V = 'icon_spojkaB_posM_v' 
    OCHRANA_P = 'icon_spojkaB_ochrP'
    OCHRANA_P_V = 'icon_spojkaB_ochrP_v'
    ZAVER_P_OBS = 'icon_spojkaB_zaver_pri_obs'
    ZAVER_M_OBS = 'icon_spojkaB_zaver_odb_obs'
    ZAVER_P_OBS_V = 'icon_spojkaB_zaver_pri_obs_v'
    ZAVER_M_OBS_V = 'icon_spojkaB_zaver_odb_obs_v' 
    ZAVER_P = 'icon_spojkaB_zaver_pri'
    ZAVER_P_V = 'icon_spojkaB_zaver_pri_v'

dictVyhP = {
    'icon_vyhP_priama': QIcon(),
    'icon_vyhP_priama_obs': QIcon(),
    'icon_vyhP_odb': QIcon (),
    'icon_vyhP_odb_obs': QIcon(),
    'icon_vyhP_priama_vyber': QIcon(),
    'icon_vyhP_priama_obs_v': QIcon(),
    'icon_vyhP_odb_vyber': QIcon(),
    'icon_vyhP_odb_obs_v': QIcon(),    
    'icon_vyhP_prest_P': QIcon(),
    'icon_vyhP_prest_M': QIcon(),    
    'icon_vyhP_vc_pri_M': QIcon(),
    'icon_vyhP_vc_odb_P': QIcon(),      
    'icon_vyhP_pc_pri_M': QIcon(),
    'icon_vyhP_pc_odb_P': QIcon(),
    'icon_vyhP_od_pri_M': QIcon(),
    'icon_vyhP_od_odb_P': QIcon(),
    'icon_vyhP_vlakP': QIcon(),
    'icon_vyhP_vlakM': QIcon(),
    'icon_vyhP_vlakP_v': QIcon(),
    'icon_vyhP_vlakM_v': QIcon(),
    'icon_vyhP_posP': QIcon(),
    'icon_vyhP_posM': QIcon(),
    'icon_vyhP_posP_v': QIcon(),
    'icon_vyhP_posM_v': QIcon(),
    'icon_vyhP_ochrP': QIcon(),
    'icon_vyhP_ochrM': QIcon(),
    'icon_vyhP_ochrP_v': QIcon(),
    'icon_vyhP_ochrM_v': QIcon(),    
    'icon_vyhP_zaver_pri_obs': QIcon(),
    'icon_vyhP_zaver_odb_obs': QIcon(),
    'icon_vyhP_zaver_pri_obs_v': QIcon(),
    'icon_vyhP_zaver_odb_obs_v': QIcon()     
}

dictVyhL = {
    'icon_vyhL_priama': QIcon(),
    'icon_vyhL_priama_obs': QIcon(),
    'icon_vyhL_odb': QIcon (),
    'icon_vyhL_odb_obs': QIcon(),
    'icon_vyhL_priama_vyber': QIcon(),
    'icon_vyhL_priama_obs_v': QIcon(),
    'icon_vyhL_odb_vyber': QIcon(),
    'icon_vyhL_odb_obs_v': QIcon(),    
    'icon_vyhL_prest_P': QIcon(),
    'icon_vyhL_prest_M': QIcon(),    
    'icon_vyhL_vc_pri_M': QIcon(),
    'icon_vyhL_vc_odb_P': QIcon(),      
    'icon_vyhL_pc_pri_M': QIcon(),
    'icon_vyhL_pc_odb_P': QIcon(),
    'icon_vyhL_od_pri_M': QIcon(),
    'icon_vyhL_od_odb_P': QIcon(),
    'icon_vyhL_vlakP': QIcon(),
    'icon_vyhL_vlakM': QIcon(),
    'icon_vyhL_vlakP_v': QIcon(),
    'icon_vyhL_vlakM_v': QIcon(),
    'icon_vyhL_posP': QIcon(),
    'icon_vyhL_posM': QIcon(),
    'icon_vyhL_posP_v': QIcon(),
    'icon_vyhL_posM_v': QIcon(),
    'icon_vyhL_ochrP': QIcon(),
    'icon_vyhL_ochrM': QIcon(),
    'icon_vyhL_ochrP_v': QIcon(),
    'icon_vyhL_ochrM_v': QIcon(),    
    'icon_vyhL_zaver_pri_obs': QIcon(),
    'icon_vyhL_zaver_odb_obs': QIcon(),
    'icon_vyhL_zaver_pri_obs_v': QIcon(),
    'icon_vyhL_zaver_odb_obs_v': QIcon()  
}

dictSpojkaA = {
    'icon_spojkaA_priama': QIcon(),
    'icon_spojkaA_priama_obs': QIcon(),
    'icon_spojkaA_odb': QIcon (),
    'icon_spojkaA_odb_obs': QIcon(),
    'icon_spojkaA_priama_vyber': QIcon(),
    'icon_spojkaA_priama_obs_v': QIcon(),
    'icon_spojkaA_odb_vyber': QIcon(),
    'icon_spojkaA_odb_obs_v': QIcon(),
    'icon_spojkaA_prest_P': QIcon(),
    'icon_spojkaA_prest_M': QIcon(),
    'icon_spojkaA_vc_pri_M': QIcon(),
    'icon_spojkaA_vc_odb_P': QIcon(),
    'icon_spojkaA_pc_pri_M': QIcon(),
    'icon_spojkaA_pc_odb_P': QIcon(),
    'icon_spojkaA_od_pri_M': QIcon(),
    'icon_spojkaA_vlakP': QIcon(),
    'icon_spojkaA_vlakM': QIcon(),
    'icon_spojkaA_vlakP_v': QIcon(),
    'icon_spojkaA_vlakM_v': QIcon(),
    'icon_spojkaA_posP': QIcon(),
    'icon_spojkaA_posM': QIcon(),
    'icon_spojkaA_posP_v': QIcon(),
    'icon_spojkaA_posM_v': QIcon(),
    'icon_spojkaA_ochrP': QIcon(),
    'icon_spojkaA_ochrP_v': QIcon(),    
    'icon_spojkaA_zaver_pri_obs': QIcon(),
    'icon_spojkaA_zaver_odb_obs': QIcon(),
    'icon_spojkaA_zaver_pri_obs_v': QIcon(),
    'icon_spojkaA_zaver_odb_obs_v': QIcon(),
    'icon_spojkaA_zaver_pri': QIcon(),
    'icon_spojkaA_zaver_pri_v': QIcon()
}

dictSpojkaB = {
    'icon_spojkaB_priama': QIcon(),
    'icon_spojkaB_priama_obs': QIcon(),
    'icon_spojkaB_odb': QIcon (),
    'icon_spojkaB_odb_obs': QIcon(),
    'icon_spojkaB_priama_vyber': QIcon(),
    'icon_spojkaB_priama_obs_v': QIcon(),
    'icon_spojkaB_odb_vyber': QIcon(),
    'icon_spojkaB_odb_obs_v': QIcon(),
    'icon_spojkaB_prest_P': QIcon(),
    'icon_spojkaB_prest_M': QIcon(),
    'icon_spojkaB_vc_pri_M': QIcon(),
    'icon_spojkaB_vc_odb_P': QIcon(),
    'icon_spojkaB_pc_pri_M': QIcon(),
    'icon_spojkaB_pc_odb_P': QIcon(),
    'icon_spojkaB_od_pri_M': QIcon(),
    'icon_spojkaB_vlakP': QIcon(),
    'icon_spojkaB_vlakM': QIcon(),
    'icon_spojkaB_vlakP_v': QIcon(),
    'icon_spojkaB_vlakM_v': QIcon(),
    'icon_spojkaB_posP': QIcon(),
    'icon_spojkaB_posM': QIcon(),
    'icon_spojkaB_posP_v': QIcon(),
    'icon_spojkaB_posM_v': QIcon(),
    'icon_spojkaB_ochrP': QIcon(),
    'icon_spojkaB_ochrP_v': QIcon(),    
    'icon_spojkaB_zaver_pri_obs': QIcon(),
    'icon_spojkaB_zaver_odb_obs': QIcon(),
    'icon_spojkaB_zaver_pri_obs_v': QIcon(),
    'icon_spojkaB_zaver_odb_obs_v': QIcon(),
    'icon_spojkaB_zaver_pri': QIcon(),
    'icon_spojkaB_zaver_pri_v': QIcon()
}

#-------------------------------------------
#-------------------------------------------

class TrSP(enum.Enum):
    PRIJEM = 'icon_TS_prijemP'  #príjem TS, obsadený medzistaničný úsek
    PRIJEM_VOLNOST = 'icon_TS_prijemP_volnost'  #príjem TS, voľný medzistaničný úsek
    PRIJEM_ZIADOST = 'icon_TS_prijemP_ziadost'  #príjem TS, voľný medzistaničný úsek, žiadosť o TS
    UDELENIE = 'icon_TS_udelenieP'  #udelenie TS, obsadený medzistaničný úsek
    UDELENIE_VOLNOST = 'icon_TS_udelenieP_volnost'  #udelenie TS, voľný medzistaničný úsek
    UDELENIE_ZIADOST = 'icon_TS_udelenieP_ziadost'  #udelenie TS, voľný medzistaničný úsek, žiadosť o TS

class TrSL(enum.Enum):
    PRIJEM = 'icon_TS_prijemL'  
    PRIJEM_VOLNOST = 'icon_TS_prijemL_volnost'  
    PRIJEM_ZIADOST = 'icon_TS_prijemL_ziadost'
    UDELENIE = 'icon_TS_udelenieL'  
    UDELENIE_VOLNOST = 'icon_TS_udelenieL_volnost'  
    UDELENIE_ZIADOST = 'icon_TS_udelenieL_ziadost'
    PRIJEM_PORUCHA_BP = 'icon_TS_prijemL_porBP'  #príjem TS, obsadený medzistaničný úsek, porucha blokovej podmienky
    PRIJEM_VOLNOST_PORUCHA_BP = 'icon_TS_prijemL_volnost_porBP'  #príjem TS, voľný medzistaničný úsek, porucha blokovej podmienky
    UDELENIE_PORUCHA_BP = 'icon_TS_udelenieL_porBP'  #udelenie TS, obsadený medzistaničný úsek, porucha blokovej podmienky
    UDELENIE_VOLNOST_PORUCHA_BP = 'icon_TS_udelenieL_volnost_porBP'  #udelenie TS, voľný medzistaničný úsek, porucha blokovej podmienky

dictTrSP = {
    'icon_TS_prijemP': QIcon(),
    'icon_TS_prijemP_volnost': QIcon(),
    'icon_TS_prijemP_ziadost': QIcon(),
    'icon_TS_udelenieP': QIcon(),
    'icon_TS_udelenieP_volnost': QIcon(),
    'icon_TS_udelenieP_ziadost': QIcon(),
}

dictTrSL = {
    'icon_TS_prijemL': QIcon(),
    'icon_TS_prijemL_volnost': QIcon(),
    'icon_TS_prijemL_ziadost': QIcon(),
    'icon_TS_udelenieL': QIcon(),
    'icon_TS_udelenieL_volnost': QIcon(),
    'icon_TS_udelenieL_ziadost': QIcon(),
    'icon_TS_prijemL_porBP': QIcon(),
    'icon_TS_prijemL_volnost_porBP': QIcon(),
    'icon_TS_udelenieL_porBP': QIcon(),
    'icon_TS_udelenieL_volnost_porBP': QIcon()
}

#-------------------------------------------
#-------------------------------------------

class Priecestie(enum.Enum):
    OTVORENE = 'icon_priec_otvorene'    #priecestie otvorené
    OTVORENE_VYBER = 'icon_priec_otvorene_v' #priecestie otvorené, výber priecestia
    PREDZVANANIE = 'icon_priec_predzv' #priecestie vo výstrahe (plynie predzváňací čas)
    ZATVORENE = 'icon_priec_zatvorene'  #priecestie zatvorené
    ZATVORENE_VYBER = 'icon_priec_zatvorene_v'    #priecestie zatvorené, výber priecestia
    ZATVORENE_OBS = 'icon_priec_zatvorene_o'  #priecestie zatvorené, obsadený úsek
    ZATVORENE_VYBER_OBS = 'icon_priec_zatvorene_v_o'    #priecestie zatvorené, výber priecestia, obsadený úsek

dictPriecestie = {
    'icon_priec_otvorene': QIcon(),   
    'icon_priec_otvorene_v': QIcon(), 
    'icon_priec_predzv': QIcon(), 
    'icon_priec_zatvorene': QIcon(), 
    'icon_priec_zatvorene_v': QIcon(),
    'icon_priec_zatvorene_o': QIcon(),
    'icon_priec_zatvorene_v_o': QIcon()
}

#-------------------------------------------
#-------------------------------------------

class RiadenieRAD(enum.Enum):
    DIALKOVE = 'icon_riadRAD_dialkove' #riadenie z dispečerského pracoviska
    DIALKOVE_ZIADOST = 'icon_riadRAD_dialkove_ziadost' #riadenie z dispečerského pracoviska, žiadosť na miestne ovládanie
    MIESTNE = 'icon_riadRAD_misetne'   #riadenie z lokálneho pracoviska
    MIESTNE_ZIADOST = 'icon_riadRAD_miestne_ziadost'   #riadenie z lokálneho pracoviska, žiadosť na diaľkové ovládanie

class RiadenieZBE(enum.Enum):
    DIALKOVE = 'icon_riadZBE_dialkove'
    DIALKOVE_ZIADOST = 'icon_riadZBE_dialkove_ziadost' 
    MIESTNE = 'icon_riadZBE_misetne' 
    MIESTNE_ZIADOST = 'icon_riadZBE_miestne_ziadost' 

class RiadenieHLO(enum.Enum):
    DIALKOVE = 'icon_riadHLO_dialkove'
    DIALKOVE_ZIADOST = 'icon_riadHLO_dialkove_ziadost' 
    MIESTNE = 'icon_riadHLO_misetne' 
    MIESTNE_ZIADOST = 'icon_riadHLO_miestne_ziadost'  

dictRiadenieRAD = {
    'icon_riadRAD_dialkove': QIcon(),
    'icon_riadRAD_dialkove_ziadost': QIcon(),
    'icon_riadRAD_misetne': QIcon(),  
    'icon_riadRAD_miestne_ziadost': QIcon()
}

dictRiadenieZBE = {
    'icon_riadZBE_dialkove': QIcon(),
    'icon_riadZBE_dialkove_ziadost': QIcon(),
    'icon_riadZBE_misetne': QIcon(),  
    'icon_riadZBE_miestne_ziadost': QIcon()
}

dictRiadenieHLO = {
    'icon_riadHLO_dialkove': QIcon(),
    'icon_riadHLO_dialkove_ziadost': QIcon(),
    'icon_riadHLO_misetne': QIcon(),  
    'icon_riadHLO_miestne_ziadost': QIcon()
}

#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------

def create():
    kolaje()

    vyhybky()

    hlavneNavestidla()
    zriadNavestidla()
    fiktNavestidla()

    priecestie()

    tratSuhlas()
    riadenie()

    ostatneElementy()    

def kolaje():
    dictKolaj['icon_kol_volna'].addFile(u"img/Kolaj/Kol_volna.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictKolaj['icon_kol_obsad'].addFile(u"img/Kolaj/Kol_obsad.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictKolaj['icon_kol_vlak'].addFile(u"img/Kolaj/Kol_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictKolaj['icon_kol_posun'].addFile(u"img/Kolaj/Kol_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictKolaj['icon_kol_ochr'].addFile(u"img/Kolaj/Kol_ochr.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictKolaj['icon_kol_mrtva'].addFile(u"img/Kolaj/Kol_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictKolaj45['icon_kol45_volna'].addFile(u"img/Kolaj/Spojka_volna.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictKolaj45['icon_kol45_obsad'].addFile(u"img/Kolaj/Spojka_obsad.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictKolaj45['icon_kol45_mrtva'].addFile(u"img/Kolaj/Spojka_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictStanKolaj1['icon_st1_volna'].addFile(u"img/Kolaj/Kol_st1_volna.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictStanKolaj1['icon_st1_obsad'].addFile(u"img/Kolaj/Kol_st1_obsad.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictStanKolaj1['icon_st1_vlak'].addFile(u"img/Kolaj/Kol_st1_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictStanKolaj1['icon_st1_posun'].addFile(u"img/Kolaj/Kol_st1_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictStanKolaj1['icon_st1_mrtva'].addFile(u"img/Kolaj/Kol_st1_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictStanKolaj2['icon_st2_volna'].addFile(u"img/Kolaj/Kol_st2_volna.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictStanKolaj2['icon_st2_obsad'].addFile(u"img/Kolaj/Kol_st2_obsad.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictStanKolaj2['icon_st2_vlak'].addFile(u"img/Kolaj/Kol_st2_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictStanKolaj2['icon_st2_posun'].addFile(u"img/Kolaj/Kol_st2_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictStanKolaj2['icon_st2_mrtva'].addFile(u"img/Kolaj/Kol_st2_basic.bmp", QSize(), QIcon.Normal, QIcon.Off)

def vyhybky():
    #-------------------------------------------------Výhybka pravá------------------------------------------------------------
    dictVyhP['icon_vyhP_priama'].addFile(u"img/Vyhybka/VyhPH_priama.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_priama_obs'].addFile(u"img/Vyhybka/VyhPH_priama_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_odb'].addFile(u"img/Vyhybka/VyhPH_odb.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_odb_obs'].addFile(u"img/Vyhybka/VyhPH_odb_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVyhP['icon_vyhP_priama_vyber'].addFile(u"img/Vyhybka/VyhPH_priama_vyber.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_odb_vyber'].addFile(u"img/Vyhybka/VyhPH_odb_vyber.bmp", QSize(), QIcon.Normal, QIcon.Off)
    
    dictVyhP['icon_vyhP_prest_P'].addFile(u"img/Vyhybka/VyhPH_odb_prest.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_prest_M'].addFile(u"img/Vyhybka/VyhPH_priama_prest.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVyhP['icon_vyhP_vc_pri_M'].addFile(u"img/Vyhybka/VyhPH_odb_vlakPRI.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_vc_odb_P'].addFile(u"img/Vyhybka/VyhPH_priama_vlakODB.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_pc_pri_M'].addFile(u"img/Vyhybka/VyhPH_odb_posunPRI.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_pc_odb_P'].addFile(u"img/Vyhybka/VyhPH_priama_posunODB.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_od_pri_M'].addFile(u"img/Vyhybka/VyhPH_odb_ochrPRI.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_od_odb_P'].addFile(u"img/Vyhybka/VyhPH_priama_ochrODB.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVyhP['icon_vyhP_vlakP'].addFile(u"img/Vyhybka/VyhPH_priama_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_vlakM'].addFile(u"img/Vyhybka/VyhPH_odb_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)  
    dictVyhP['icon_vyhP_vlakP_v'].addFile(u"img/Vyhybka/VyhPH_priama_vlak_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_vlakM_v'].addFile(u"img/Vyhybka/VyhPH_odb_vlak_v.bmp", QSize(), QIcon.Normal, QIcon.Off)    
  
    dictVyhP['icon_vyhP_posP'].addFile(u"img/Vyhybka/VyhPH_priama_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_posM'].addFile(u"img/Vyhybka/VyhPH_odb_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictVyhP['icon_vyhP_posP_v'].addFile(u"img/Vyhybka/VyhPH_priama_posun_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_posM_v'].addFile(u"img/Vyhybka/VyhPH_odb_posun_v.bmp", QSize(), QIcon.Normal, QIcon.Off)    

    dictVyhP['icon_vyhP_ochrP'].addFile(u"img/Vyhybka/VyhPH_priama_ochr.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_ochrM'].addFile(u"img/Vyhybka/VyhPH_odb_ochr.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_ochrP_v'].addFile(u"img/Vyhybka/VyhPH_priama_ochr_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_ochrM_v'].addFile(u"img/Vyhybka/VyhPH_odb_ochr_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVyhP['icon_vyhP_zaver_pri_obs'].addFile(u"img/Vyhybka/VyhPH_priama_obsad.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_zaver_odb_obs'].addFile(u"img/Vyhybka/VyhPH_odb_obsad.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_zaver_pri_obs_v'].addFile(u"img/Vyhybka/VyhPH_priama_obs_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_zaver_odb_obs_v'].addFile(u"img/Vyhybka/VyhPH_odb_obs_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_priama_obs_v'].addFile(u"img/Vyhybka/VyhPH_priama_vyber_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhP['icon_vyhP_odb_obs_v'].addFile(u"img/Vyhybka/VyhPH_odb_vyber_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)

    #-------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------Výhybka ľavá------------------------------------------------------------
    dictVyhL['icon_vyhL_priama'].addFile(u"img/Vyhybka/VyhLH_priama.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_priama_obs'].addFile(u"img/Vyhybka/VyhLH_priama_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_odb'].addFile(u"img/Vyhybka/VyhLH_odb.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_odb_obs'].addFile(u"img/Vyhybka/VyhLH_odb_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVyhL['icon_vyhL_priama_vyber'].addFile(u"img/Vyhybka/VyhLH_priama_vyber.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_odb_vyber'].addFile(u"img/Vyhybka/VyhLH_odb_vyber.bmp", QSize(), QIcon.Normal, QIcon.Off)
    
    dictVyhL['icon_vyhL_prest_P'].addFile(u"img/Vyhybka/VyhLH_odb_prest.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_prest_M'].addFile(u"img/Vyhybka/VyhLH_priama_prest.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVyhL['icon_vyhL_vc_pri_M'].addFile(u"img/Vyhybka/VyhLH_odb_vlakPRI.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_vc_odb_P'].addFile(u"img/Vyhybka/VyhLH_priama_vlakODB.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_pc_pri_M'].addFile(u"img/Vyhybka/VyhLH_odb_posunPRI.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_pc_odb_P'].addFile(u"img/Vyhybka/VyhLH_priama_posunODB.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_od_pri_M'].addFile(u"img/Vyhybka/VyhLH_odb_ochrPRI.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_od_odb_P'].addFile(u"img/Vyhybka/VyhLH_priama_ochrODB.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVyhL['icon_vyhL_vlakP'].addFile(u"img/Vyhybka/VyhLH_priama_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_vlakM'].addFile(u"img/Vyhybka/VyhLH_odb_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)  
    dictVyhL['icon_vyhL_vlakP_v'].addFile(u"img/Vyhybka/VyhLH_priama_vlak_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_vlakM_v'].addFile(u"img/Vyhybka/VyhLH_odb_vlak_v.bmp", QSize(), QIcon.Normal, QIcon.Off)    
  
    dictVyhL['icon_vyhL_posP'].addFile(u"img/Vyhybka/VyhLH_priama_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_posM'].addFile(u"img/Vyhybka/VyhLH_odb_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictVyhL['icon_vyhL_posP_v'].addFile(u"img/Vyhybka/VyhLH_priama_posun_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_posM_v'].addFile(u"img/Vyhybka/VyhLH_odb_posun_v.bmp", QSize(), QIcon.Normal, QIcon.Off)    

    dictVyhL['icon_vyhL_ochrP'].addFile(u"img/Vyhybka/VyhLH_priama_ochr.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_ochrM'].addFile(u"img/Vyhybka/VyhLH_odb_ochr.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_ochrP_v'].addFile(u"img/Vyhybka/VyhLH_priama_ochr_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_ochrM_v'].addFile(u"img/Vyhybka/VyhLH_odb_ochr_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVyhL['icon_vyhL_zaver_pri_obs'].addFile(u"img/Vyhybka/VyhLH_priama_obsad.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_zaver_odb_obs'].addFile(u"img/Vyhybka/VyhLH_odb_obsad.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_zaver_pri_obs_v'].addFile(u"img/Vyhybka/VyhLH_priama_obs_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_zaver_odb_obs_v'].addFile(u"img/Vyhybka/VyhLH_odb_obs_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_priama_obs_v'].addFile(u"img/Vyhybka/VyhLH_priama_vyber_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVyhL['icon_vyhL_odb_obs_v'].addFile(u"img/Vyhybka/VyhLH_odb_vyber_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)

    #------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------Koľajová spojka A------------------------------------------------------------
    dictSpojkaA['icon_spojkaA_priama'].addFile(u"img/VyhSpojka/Spojka_volna_pri_A.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_priama_obs'].addFile(u"img/VyhSpojka/Spojka_obsad_PRI_A_BZ.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_odb'].addFile(u"img/VyhSpojka/Spojka_volna_ODB_A.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_odb_obs'].addFile(u"img/VyhSpojka/Spojka_obsad_ODB_A_BZ.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictSpojkaA['icon_spojkaA_priama_vyber'].addFile(u"img/VyhSpojka/Spojka_volna_PRI_A_vyber.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_odb_vyber'].addFile(u"img/VyhSpojka/Spojka_volna_ODB_A_vyber.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_zaver_odb_obs_v'].addFile(u"img/VyhSpojka/Spojka_obsad_ODB_A_BZ_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_priama_obs_v'].addFile(u"img/VyhSpojka/Spojka_obsad_PRI_A_BZ_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictSpojkaA['icon_spojkaA_prest_P'].addFile(u"img/VyhSpojka/Spojka_volna_ODB_prest_A.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_prest_M'].addFile(u"img/VyhSpojka/Spojka_volna_PRI_prest_A.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictSpojkaA['icon_spojkaA_vc_pri_M'].addFile(u"img/VyhSpojka/Spojka_ODB_vlakPRI_A.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_vc_odb_P'].addFile(u"img/VyhSpojka/Spojka_PRI_vlakODB_A.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_pc_pri_M'].addFile(u"img/VyhSpojka/Spojka_ODB_posunPRI_A.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_pc_odb_P'].addFile(u"img/VyhSpojka/Spojka_PRI_posunODB_A.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_od_pri_M'].addFile(u"img/VyhSpojka/Spojka_ODB_ochrPRI_A.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictSpojkaA['icon_spojkaA_vlakP'].addFile(u"img/VyhSpojka/Spojka_vlak_PRI_A.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_vlakM'].addFile(u"img/VyhSpojka/Spojka_vlak_ODB_A.bmp", QSize(), QIcon.Normal, QIcon.Off)  
    dictSpojkaA['icon_spojkaA_vlakP_v'].addFile(u"img/VyhSpojka/Spojka_vlak_PRI_A_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_vlakM_v'].addFile(u"img/VyhSpojka/Spojka_vlak_ODB_A_v.bmp", QSize(), QIcon.Normal, QIcon.Off)    
  
    dictSpojkaA['icon_spojkaA_posP'].addFile(u"img/VyhSpojka/Spojka_posun_PRI_A.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_posM'].addFile(u"img/VyhSpojka/Spojka_posun_ODB_A.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictSpojkaA['icon_spojkaA_posP_v'].addFile(u"img/VyhSpojka/Spojka_posun_PRI_A_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_posM_v'].addFile(u"img/VyhSpojka/Spojka_posun_ODB_A_v.bmp", QSize(), QIcon.Normal, QIcon.Off)    

    dictSpojkaA['icon_spojkaA_ochrP'].addFile(u"img/VyhSpojka/Spojka_ochr_PRI_A.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_ochrP_v'].addFile(u"img/VyhSpojka/Spojka_ochr_PRI_A_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictSpojkaA['icon_spojkaA_zaver_pri_obs'].addFile(u"img/VyhSpojka/Spojka_obsad_PRI_A_Z.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_zaver_odb_obs'].addFile(u"img/VyhSpojka/Spojka_obsad_ODB_A_Z.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_zaver_pri_obs_v'].addFile(u"img/VyhSpojka/Spojka_obsad_PRI_A_Z_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_odb_obs_v'].addFile(u"img/VyhSpojka/Spojka_obsad_ODB_A_Z_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_zaver_pri'].addFile(u"img/VyhSpojka/Spojka_volna_PRI_A_Z.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaA['icon_spojkaA_zaver_pri_v'].addFile(u"img/VyhSpojka/Spojka_volna_PRI_A_Z_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

    #------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------Koľajová spojka B------------------------------------------------------------
    dictSpojkaB['icon_spojkaB_priama'].addFile(u"img/VyhSpojka/Spojka_volna_pri_B.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_priama_obs'].addFile(u"img/VyhSpojka/Spojka_obsad_PRI_B_BZ.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_odb'].addFile(u"img/VyhSpojka/Spojka_volna_ODB_B.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_odb_obs'].addFile(u"img/VyhSpojka/Spojka_obsad_ODB_B_BZ.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictSpojkaB['icon_spojkaB_priama_vyber'].addFile(u"img/VyhSpojka/Spojka_volna_PRI_B_vyber.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_odb_vyber'].addFile(u"img/VyhSpojka/Spojka_volna_ODB_B_vyber.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_priama_obs_v'].addFile(u"img/VyhSpojka/Spojka_obsad_PRI_B_BZ_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_odb_obs_v'].addFile(u"img/VyhSpojka/Spojka_obsad_ODB_B_BZ_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictSpojkaB['icon_spojkaB_prest_P'].addFile(u"img/VyhSpojka/Spojka_volna_ODB_prest_B.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_prest_M'].addFile(u"img/VyhSpojka/Spojka_volna_PRI_prest_B.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictSpojkaB['icon_spojkaB_vc_pri_M'].addFile(u"img/VyhSpojka/Spojka_ODB_vlakPRI_B.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_vc_odb_P'].addFile(u"img/VyhSpojka/Spojka_PRI_vlakODB_B.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_pc_pri_M'].addFile(u"img/VyhSpojka/Spojka_ODB_posunPRI_B.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_pc_odb_P'].addFile(u"img/VyhSpojka/Spojka_PRI_posunODB_B.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_od_pri_M'].addFile(u"img/VyhSpojka/Spojka_ODB_ochrPRI_B.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictSpojkaB['icon_spojkaB_vlakP'].addFile(u"img/VyhSpojka/Spojka_vlak_PRI_B.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_vlakM'].addFile(u"img/VyhSpojka/Spojka_vlak_ODB_B.bmp", QSize(), QIcon.Normal, QIcon.Off)  
    dictSpojkaB['icon_spojkaB_vlakP_v'].addFile(u"img/VyhSpojka/Spojka_vlak_PRI_B_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_vlakM_v'].addFile(u"img/VyhSpojka/Spojka_vlak_ODB_B_v.bmp", QSize(), QIcon.Normal, QIcon.Off)    
  
    dictSpojkaB['icon_spojkaB_posP'].addFile(u"img/VyhSpojka/Spojka_posun_PRI_B.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_posM'].addFile(u"img/VyhSpojka/Spojka_posun_ODB_B.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictSpojkaB['icon_spojkaB_posP_v'].addFile(u"img/VyhSpojka/Spojka_posun_PRI_B_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_posM_v'].addFile(u"img/VyhSpojka/Spojka_posun_ODB_B_v.bmp", QSize(), QIcon.Normal, QIcon.Off)    

    dictSpojkaB['icon_spojkaB_ochrP'].addFile(u"img/VyhSpojka/Spojka_ochr_PRI_B.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_ochrP_v'].addFile(u"img/VyhSpojka/Spojka_ochr_PRI_B_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictSpojkaB['icon_spojkaB_zaver_pri_obs'].addFile(u"img/VyhSpojka/Spojka_obsad_PRI_B_Z.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_zaver_odb_obs'].addFile(u"img/VyhSpojka/Spojka_obsad_ODB_B_Z.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_zaver_pri_obs_v'].addFile(u"img/VyhSpojka/Spojka_obsad_PRI_B_Z_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_zaver_odb_obs_v'].addFile(u"img/VyhSpojka/Spojka_obsad_ODB_B_Z_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_zaver_pri'].addFile(u"img/VyhSpojka/Spojka_volna_PRI_B_Z.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictSpojkaB['icon_spojkaB_zaver_pri_v'].addFile(u"img/VyhSpojka/Spojka_volna_PRI_B_Z_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

def hlavneNavestidla():
    #-------------------------------------------------Vchodové ľavé návestidlo------------------------------------------------------------
    dictVchodoveL['icon_hl_stojL'].addFile(u"img/HlavneNav/Hl_stojL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_stojL_v'].addFile(u"img/HlavneNav/Hl_stoj_vL.bmp", QSize(), QIcon.Normal, QIcon.Off) 
    dictVchodoveL['icon_hl_stojL_PN'].addFile(u"img/HlavneNav/Hl_stojL_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_stojL_v_PN'].addFile(u"img/HlavneNav/Hl_stoj_vL_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_stojL_obs'].addFile(u"img/HlavneNav/Hl_stojL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictVchodoveL['icon_hl_stojL_v_obs'].addFile(u"img/HlavneNav/Hl_stoj_vL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_stojL_obs_PN'].addFile(u"img/HlavneNav/Hl_stojL_obs_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictVchodoveL['icon_hl_stojL_v_obs_PN'].addFile(u"img/HlavneNav/Hl_stoj_vL_obs_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_stojL_mrtve'].addFile(u"img/HlavneNav/Hl_stojL_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictVchodoveL['icon_hl_stojL_v_mrtve'].addFile(u"img/HlavneNav/Hl_stoj_vL_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_stojL_mrtve_PN'].addFile(u"img/HlavneNav/Hl_stojL_PN_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictVchodoveL['icon_hl_stojL_v_mrtve_PN'].addFile(u"img/HlavneNav/Hl_stoj_vL_mrtve_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_stojL_vlak'].addFile(u"img/HlavneNav/Hl_stojL_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_stojL_rusenie_cesty'].addFile(u"img/HlavneNav/Hl_stojL_zaver_rusenie.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_stavanie'].addFile(u"img/HlavneNav/Hl_stojL_zaver_stavanie.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_stojL_zaver_vc'].addFile(u"img/HlavneNav/Hl_stojL_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_vc_v'].addFile(u"img/HlavneNav/Hl_stoj_vL_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_cestaL'].addFile(u"img/HlavneNav/Hl_vyberL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_cestaL_obs'].addFile(u"img/HlavneNav/Hl_vyberL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_cestaL_mrtve'].addFile(u"img/HlavneNav/Hl_vyberL_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_volnoL'].addFile(u"img/HlavneNav/Hl_volnoL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_volnoL_v'].addFile(u"img/HlavneNav/Hl_volno_vL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_volnoL_obs'].addFile(u"img/HlavneNav/Hl_volno_obsL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_volnoL_v_obs'].addFile(u"img/HlavneNav/Hl_volno_vL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_volnoL_mrtve'].addFile(u"img/HlavneNav/Hl_volno_mrtveL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_volnoL_v_mrtve'].addFile(u"img/HlavneNav/Hl_volno_vL_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_zhasnuteL'].addFile(u"img/HlavneNav/Hl_zhasL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zhasnuteL_obs'].addFile(u"img/HlavneNav/Hl_zhasL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_cestaL_vlak'].addFile(u"img/HlavneNav/Hl_vyberL_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_cestaL_stavanie'].addFile(u"img/HlavneNav/Hl_vyberL_zaver_stavanie_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_cestaL_rusenie'].addFile(u"img/HlavneNav/Hl_vyberL_zaver_rusenie.bmp", QSize(), QIcon.Normal, QIcon.Off)   

    dictVchodoveL['icon_hl_zaverL_vc_volno'].addFile(u"img/HlavneNav/Hl_volnoL_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_vc_v_volno'].addFile(u"img/HlavneNav/Hl_volno_vL_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_zaverL_stavanie_volno'].addFile(u"img/HlavneNav/Hl_volnoL_zaver_stavanie.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_volnoL_rusenie_cesty'].addFile(u"img/HlavneNav/Hl_volno_vL_zaver_rusenie.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_zaverL_vc_PNav'].addFile(u"img/HlavneNav/Hl_stojL_zaver_vc_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_vc_v_PNav'].addFile(u"img/HlavneNav/Hl_stoj_vL_zaver_vc_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_stavanie_PNav'].addFile(u"img/HlavneNav/Hl_stojL_zaver_stavanie_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_PNavL_rusenie_cesty'].addFile(u"img/HlavneNav/Hl_stojL_zaver_rusenie_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_zaverL_pc'].addFile(u"img/HlavneNav/Hl_stojL_zaver_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_pc_v'].addFile(u"img/HlavneNav/Hl_stoj_vL_zaver_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_stojL_posun'].addFile(u"img/HlavneNav/Hl_stojL_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_stojL_posun_v'].addFile(u"img/HlavneNav/Hl_stoj_vL_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_pc_volno'].addFile(u"img/HlavneNav/Hl_volnoL_zaver_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_pc_v_volno'].addFile(u"img/HlavneNav/Hl_volno_vL_zaver_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_posunL'].addFile(u"img/HlavneNav/Hl_posunL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_posunL_v'].addFile(u"img/HlavneNav/Hl_posun_vL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_posunL_obs'].addFile(u"img/HlavneNav/Hl_posunL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_posunL_v_obs'].addFile(u"img/HlavneNav/Hl_posun_vL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_posunL_mrtve'].addFile(u"img/HlavneNav/Hl_posunL_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_posunL_v_mrtve'].addFile(u"img/HlavneNav/Hl_posun_vL_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_posunL_rusenie_cesty'].addFile(u"img/HlavneNav/Hl_posunL_zaver_rusenie.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveL['icon_hl_zaverL_vc_posun'].addFile(u"img/HlavneNav/Hl_posunL_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_vc_v_posun'].addFile(u"img/HlavneNav/Hl_posun_vL_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_pc_posun'].addFile(u"img/HlavneNav/Hl_posunL_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_pc_v_posun'].addFile(u"img/HlavneNav/Hl_posun_vL_zaver_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_pc_PNav'].addFile(u"img/HlavneNav/Hl_stojL_zaver_pc_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_pc_v_PNav'].addFile(u"img/HlavneNav/Hl_stoj_vL_zaver_pc_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_zaverL_stavanie_posun'].addFile(u"img/HlavneNav/Hl_posunL_zaver_stavanie.bmp", QSize(), QIcon.Normal, QIcon.Off)

    #-------------------------------------------------Vchodové pravé návestidlo------------------------------------------------------------
    dictVchodoveP['icon_hl_stojP'].addFile(u"img/HlavneNav/Hl_stojP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_stojP_v'].addFile(u"img/HlavneNav/Hl_stoj_vP.bmp", QSize(), QIcon.Normal, QIcon.Off) 
    dictVchodoveP['icon_hl_stojP_PN'].addFile(u"img/HlavneNav/Hl_stojP_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_stojP_v_PN'].addFile(u"img/HlavneNav/Hl_stoj_vP_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_stojP_obs'].addFile(u"img/HlavneNav/Hl_stojP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictVchodoveP['icon_hl_stojP_v_obs'].addFile(u"img/HlavneNav/Hl_stoj_vP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_stojP_obs_PN'].addFile(u"img/HlavneNav/Hl_stojP_obs_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictVchodoveP['icon_hl_stojP_v_obs_PN'].addFile(u"img/HlavneNav/Hl_stoj_vP_obs_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_stojP_mrtve'].addFile(u"img/HlavneNav/Hl_stojP_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictVchodoveP['icon_hl_stojP_v_mrtve'].addFile(u"img/HlavneNav/Hl_stoj_vP_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_stojP_mrtve_PN'].addFile(u"img/HlavneNav/Hl_stojP_PN_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictVchodoveP['icon_hl_stojP_v_mrtve_PN'].addFile(u"img/HlavneNav/Hl_stoj_vP_mrtve_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_stojP_vlak'].addFile(u"img/HlavneNav/Hl_stojP_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_stojP_rusenie_cesty'].addFile(u"img/HlavneNav/Hl_stojP_zaver_rusenie.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_stavanie'].addFile(u"img/HlavneNav/Hl_stojP_zaver_stavanie.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_stojP_zaver_vc'].addFile(u"img/HlavneNav/Hl_stojP_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_vc_v'].addFile(u"img/HlavneNav/Hl_stoj_vP_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_cestaP'].addFile(u"img/HlavneNav/Hl_vyberP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_cestaP_obs'].addFile(u"img/HlavneNav/Hl_vyberP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_cestaP_mrtve'].addFile(u"img/HlavneNav/Hl_vyberP_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_volnoP'].addFile(u"img/HlavneNav/Hl_volnoP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_volnoP_v'].addFile(u"img/HlavneNav/Hl_volno_vP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_volnoP_obs'].addFile(u"img/HlavneNav/Hl_volno_obsP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_volnoP_v_obs'].addFile(u"img/HlavneNav/Hl_volno_vP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_volnoP_mrtve'].addFile(u"img/HlavneNav/Hl_volno_mrtveP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_volnoP_v_mrtve'].addFile(u"img/HlavneNav/Hl_volno_vP_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_zhasnuteP'].addFile(u"img/HlavneNav/Hl_zhasP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zhasnuteP_obs'].addFile(u"img/HlavneNav/Hl_zhasP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_cestaP_vlak'].addFile(u"img/HlavneNav/Hl_vyberP_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_cestaP_stavanie'].addFile(u"img/HlavneNav/Hl_vyberP_zaver_stavanie_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_cestaP_rusenie'].addFile(u"img/HlavneNav/Hl_vyberP_zaver_rusenie.bmp", QSize(), QIcon.Normal, QIcon.Off)   

    dictVchodoveP['icon_hl_zaverP_vc_volno'].addFile(u"img/HlavneNav/Hl_volnoP_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_vc_v_volno'].addFile(u"img/HlavneNav/Hl_volno_vP_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_stavanie_volno'].addFile(u"img/HlavneNav/Hl_volnoP_zaver_stavanie.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_volnoP_rusenie_cesty'].addFile(u"img/HlavneNav/Hl_volno_vP_zaver_rusenie.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_vc_PNav'].addFile(u"img/HlavneNav/Hl_stojP_zaver_vc_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_vc_v_PNav'].addFile(u"img/HlavneNav/Hl_stoj_vP_zaver_vc_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_stavanie_PNav'].addFile(u"img/HlavneNav/Hl_stojP_zaver_stavanie_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_PNavP_rusenie_cesty'].addFile(u"img/HlavneNav/Hl_stojP_zaver_rusenie_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_zaverP_pc'].addFile(u"img/HlavneNav/Hl_stojP_zaver_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_pc_v'].addFile(u"img/HlavneNav/Hl_stoj_vP_zaver_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_stojP_posun'].addFile(u"img/HlavneNav/Hl_stojP_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_stojP_posun_v'].addFile(u"img/HlavneNav/Hl_stoj_vP_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_zaverP_pc_volno'].addFile(u"img/HlavneNav/Hl_volnoP_zaver_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_pc_v_volno'].addFile(u"img/HlavneNav/Hl_volno_vP_zaver_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_posunP'].addFile(u"img/HlavneNav/Hl_posunP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_posunP_v'].addFile(u"img/HlavneNav/Hl_posun_vP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_posunP_obs'].addFile(u"img/HlavneNav/Hl_posunP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_posunP_v_obs'].addFile(u"img/HlavneNav/Hl_posun_vP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_posunL_mrtve'].addFile(u"img/HlavneNav/Hl_posunL_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveL['icon_hl_posunL_v_mrtve'].addFile(u"img/HlavneNav/Hl_posun_vL_mrtve.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_vc_posun'].addFile(u"img/HlavneNav/Hl_posunP_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_posunP_rusenie_cesty'].addFile(u"img/HlavneNav/Hl_posunP_zaver_rusenie.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictVchodoveP['icon_hl_zaverP_vc_v_posun'].addFile(u"img/HlavneNav/Hl_posun_vP_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_pc_posun'].addFile(u"img/HlavneNav/Hl_posunP_zaver_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_pc_v_posun'].addFile(u"img/HlavneNav/Hl_posun_vP_zaver_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_stavanie_posun'].addFile(u"img/HlavneNav/Hl_posunP_zaver_stavanie.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_pc_PNav'].addFile(u"img/HlavneNav/Hl_stojP_zaver_pc_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictVchodoveP['icon_hl_zaverP_pc_v_PNav'].addFile(u"img/HlavneNav/Hl_stoj_vP_zaver_pc_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    #-------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------Odchodové pravé návestidlo-----------------------------------------------------------

    dictOdchodoveP['icon_ko_stojP_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_obsP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_stojP'].addFile(u"img/HlavneKombinovaneNav/Kom_stojP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_stojP_PN'].addFile(u"img/HlavneKombinovaneNav/Kom_stojP_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_stojP_v_PN'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_vP_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_stojP_v'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_vP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_stojP_v_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_vP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_stojP_obs_PN'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_obsP_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_stojP_v_obs_PN'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_vP_obs_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_cestaP'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_cestaP_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_cestaP_vlak'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberP_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_cestaP_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberP_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_cestaP_stavanie'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberP_stav.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_cestaP_rusenie'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberP_zrus.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_stojP_vlak'].addFile(u"img/HlavneKombinovaneNav/Kom_stojP_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_stojP_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_stojP_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_zaverP_stavanie'].addFile(u"img/HlavneKombinovaneNav/Kom_stavP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_stavanie_volno'].addFile(u"img/HlavneKombinovaneNav/Kom_stavP_volno.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_stavanie_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_stavP_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_stavanie_PNav'].addFile(u"img/HlavneKombinovaneNav/Kom_stavP_PNav.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_zaverP_vc'].addFile(u"img/HlavneKombinovaneNav/Kom_stojP_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_pc'].addFile(u"img/HlavneKombinovaneNav/Kom_posunP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_vc_v'].addFile(u"img/HlavneKombinovaneNav/Kom_vlak_vP.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictOdchodoveP['icon_ko_zaverP_pc_v'].addFile(u"img/HlavneKombinovaneNav/Kom_posun_vP.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_zaverP_vc_volno'].addFile(u"img/HlavneKombinovaneNav/Kom_volnoP_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_vc_v_volno'].addFile(u"img/HlavneKombinovaneNav/Kom_vlak_vP_volno.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_pc_volno'].addFile(u"img/HlavneKombinovaneNav/Kom_volnoP_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_pc_v_volno'].addFile(u"img/HlavneKombinovaneNav/Kom_posun_vP_volno.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_zaverP_vc_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_posunP_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_vc_v_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_vlak_vP_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_pc_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_posunP_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_pc_v_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_posun_vP_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_zaverP_vc_PNav'].addFile(u"img/HlavneKombinovaneNav/Kom_PNavP_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_vc_v_PNav'].addFile(u"img/HlavneKombinovaneNav/Kom_vlak_vP_PNav.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_pc_PNav'].addFile(u"img/HlavneKombinovaneNav/Kom_PNavP_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_zaverP_pc_v_PNav'].addFile(u"img/HlavneKombinovaneNav/Kom_posun_vP_PNav.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_stojP_rusenie_cesty'].addFile(u"img/HlavneKombinovaneNav/Kom_zrusP.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictOdchodoveP['icon_ko_volnoP_rusenie_cesty'].addFile(u"img/HlavneKombinovaneNav/Kom_zrusP_volno.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_posunP_rusenie_cesty'].addFile(u"img/HlavneKombinovaneNav/Kom_zrusP_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_PNavP_rusenie_cesty'].addFile(u"img/HlavneKombinovaneNav/Kom_zrusP_PNav.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_volnoP'].addFile(u"img/HlavneKombinovaneNav/Kom_volnoP.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictOdchodoveP['icon_ko_volnoP_v'].addFile(u"img/HlavneKombinovaneNav/Kom_volno_vP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_volnoP_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_volno_obsP.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictOdchodoveP['icon_ko_volnoP_v_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_volno_obsP_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveP['icon_ko_posunP'].addFile(u"img/HlavneKombinovaneNav/Kom_posP.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictOdchodoveP['icon_ko_posunP_v'].addFile(u"img/HlavneKombinovaneNav/Kom_pos_vP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveP['icon_ko_posunP_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_pos_obsP.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictOdchodoveP['icon_ko_posunP_v_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_pos_obsP_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
 
    #-------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------Odchodové ľavé návestidlo------------------------------------------------------------

    dictOdchodoveL['icon_ko_stojL_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_obsL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_stojL'].addFile(u"img/HlavneKombinovaneNav/Kom_stojL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_stojL_PN'].addFile(u"img/HlavneKombinovaneNav/Kom_stojL_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_stojL_v_PN'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_vL_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveL['icon_ko_stojL_v'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_vL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_stojL_v_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_vL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_stojL_obs_PN'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_obsL_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_stojL_v_obs_PN'].addFile(u"img/HlavneKombinovaneNav/Kom_stoj_vL_obs_PN.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveL['icon_ko_cestaL'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_cestaL_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_cestaL_vlak'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberL_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_cestaL_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberL_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_cestaL_stavanie'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberL_stav.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_cestaL_rusenie'].addFile(u"img/HlavneKombinovaneNav/Kom_vyberL_zrus.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveL['icon_ko_stojL_vlak'].addFile(u"img/HlavneKombinovaneNav/Kom_stojL_vc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_stojL_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_stojL_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)    

    dictOdchodoveL['icon_ko_zaverL_stavanie'].addFile(u"img/HlavneKombinovaneNav/Kom_stavL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_stavanie_volno'].addFile(u"img/HlavneKombinovaneNav/Kom_stavL_volno.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_stavanie_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_stavL_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_stavanie_PNav'].addFile(u"img/HlavneKombinovaneNav/Kom_stavL_PNav.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveL['icon_ko_zaverL_vc'].addFile(u"img/HlavneKombinovaneNav/Kom_stojL_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_pc'].addFile(u"img/HlavneKombinovaneNav/Kom_posunL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_vc_v'].addFile(u"img/HlavneKombinovaneNav/Kom_vlak_vL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_pc_v'].addFile(u"img/HlavneKombinovaneNav/Kom_posun_vL.bmp", QSize(), QIcon.Normal, QIcon.Off)    

    dictOdchodoveL['icon_ko_zaverL_vc_volno'].addFile(u"img/HlavneKombinovaneNav/Kom_volnoL_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_vc_v_volno'].addFile(u"img/HlavneKombinovaneNav/Kom_vlak_vL_volno.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_pc_volno'].addFile(u"img/HlavneKombinovaneNav/Kom_volnoL_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_pc_v_volno'].addFile(u"img/HlavneKombinovaneNav/Kom_posun_vL_volno.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveL['icon_ko_zaverL_vc_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_posunL_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_vc_v_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_vlak_vL_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_pc_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_posunL_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_pc_v_posun'].addFile(u"img/HlavneKombinovaneNav/Kom_posun_vL_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveL['icon_ko_zaverL_vc_PNav'].addFile(u"img/HlavneKombinovaneNav/Kom_PNavL_vlak.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_vc_v_PNav'].addFile(u"img/HlavneKombinovaneNav/Kom_vlak_vL_PNav.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_pc_PNav'].addFile(u"img/HlavneKombinovaneNav/Kom_PNavL_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_zaverL_pc_v_PNav'].addFile(u"img/HlavneKombinovaneNav/Kom_posun_vL_PNav.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveL['icon_ko_stojL_rusenie_cesty'].addFile(u"img/HlavneKombinovaneNav/Kom_zrusL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_volnoL_rusenie_cesty'].addFile(u"img/HlavneKombinovaneNav/Kom_zrusL_volno.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_posunL_rusenie_cesty'].addFile(u"img/HlavneKombinovaneNav/Kom_zrusL_posun.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_PNavL_rusenie_cesty'].addFile(u"img/HlavneKombinovaneNav/Kom_zrusL_PNav.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveL['icon_ko_volnoL'].addFile(u"img/HlavneKombinovaneNav/Kom_volnoL.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictOdchodoveL['icon_ko_volnoL_v'].addFile(u"img/HlavneKombinovaneNav/Kom_volno_vL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_volnoL_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_volno_obsL.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictOdchodoveL['icon_ko_volnoL_v_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_volno_obsL_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictOdchodoveL['icon_ko_posunL'].addFile(u"img/HlavneKombinovaneNav/Kom_posL.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictOdchodoveL['icon_ko_posunL_v'].addFile(u"img/HlavneKombinovaneNav/Kom_pos_vL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictOdchodoveL['icon_ko_posunL_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_pos_obsL.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictOdchodoveL['icon_ko_posunL_v_obs'].addFile(u"img/HlavneKombinovaneNav/Kom_pos_obsL_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

def zriadNavestidla():
    #------------------------------------------------Zriaďovacie ľavé návestidlo-----------------------------------------------------------

    dictZriadovacieL['icon_zr_stojL_obs'].addFile(u"img/Zriad/Zriad_obsadL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieL['icon_zr_stojL'].addFile(u"img/Zriad/Zriad_stojL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieL['icon_zr_stojL_obs_v'].addFile(u"img/Zriad/Zriad_vyberL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieL['icon_zr_stojL_v'].addFile(u"img/Zriad/Zriad_vyberL.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictZriadovacieL['icon_zr_stojL_zaver_pc'].addFile(u"img/Zriad/Zriad_posunL.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictZriadovacieL['icon_zr_stojL_zaver_stavanie'].addFile(u"img/Zriad/Zriad_stavL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieL['icon_zr_stojL_rusenie_cesty'].addFile(u"img/Zriad/Zriad_rusenieL.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictZriadovacieL['icon_zr_stojL_zaver_pc_v'].addFile(u"img/Zriad/Zriad_posunL_vyb.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictZriadovacieL['icon_zr_stojL_pc'].addFile(u"img/Zriad/Zriad_stojL_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieL['icon_zr_stojL_vc'].addFile(u"img/Zriad/Zriad_vlakL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieL['icon_zr_stojL_od'].addFile(u"img/Zriad/Zriad_ochrL.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictZriadovacieL['icon_zr_posunL'].addFile(u"img/Zriad/Zriad_posL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieL['icon_zr_posunL_v'].addFile(u"img/Zriad/Zriad_posL_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieL['icon_zr_posunL_obs'].addFile(u"img/Zriad/Zriad_posL_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieL['icon_zr_posunL_v_obs'].addFile(u"img/Zriad/Zriad_posL_obs_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

    #---------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------Zriaďovacie pravé návestidlo-----------------------------------------------------------

    dictZriadovacieP['icon_zr_stojP_obs'].addFile(u"img/Zriad/Zriad_obsadP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieP['icon_zr_stojP'].addFile(u"img/Zriad/Zriad_stojP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieP['icon_zr_stojP_obs_v'].addFile(u"img/Zriad/Zriad_vyberP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieP['icon_zr_stojP_v'].addFile(u"img/Zriad/Zriad_vyberP.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictZriadovacieP['icon_zr_stojP_zaver_pc'].addFile(u"img/Zriad/Zriad_posunP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieP['icon_zr_stojP_zaver_stavanie'].addFile(u"img/Zriad/Zriad_stavP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieP['icon_zr_stojP_rusenie_cesty'].addFile(u"img/Zriad/Zriad_rusenieP.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictZriadovacieP['icon_zr_stojP_zaver_pc_v'].addFile(u"img/Zriad/Zriad_posunP_vyb.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictZriadovacieP['icon_zr_stojP_pc'].addFile(u"img/Zriad/Zriad_stojP_pc.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictZriadovacieP['icon_zr_stojP_vc'].addFile(u"img/Zriad/Zriad_vlakP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieP['icon_zr_stojP_od'].addFile(u"img/Zriad/Zriad_ochrP.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictZriadovacieP['icon_zr_posunP'].addFile(u"img/Zriad/Zriad_posP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieP['icon_zr_posunP_v'].addFile(u"img/Zriad/Zriad_posP_v.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieP['icon_zr_posunP_obs'].addFile(u"img/Zriad/Zriad_posP_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictZriadovacieP['icon_zr_posunP_v_obs'].addFile(u"img/Zriad/Zriad_posP_obs_v.bmp", QSize(), QIcon.Normal, QIcon.Off)

def fiktNavestidla():
    #------------------------------------------------Fiktívne ľavé návestidlo-----------------------------------------------------------

    dictFiktL['icon_fiktL'].addFile(u"img/Fiktivne/Fikt_volnoL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktL['icon_fiktL_obs'].addFile(u"img/Fiktivne/Fikt_obsL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktL['icon_fiktL_mrtve'].addFile(u"img/Fiktivne/Fikt_mrtveL.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictFiktL['icon_fiktL_v'].addFile(u"img/Fiktivne/Fikt_volnoL_vyb.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktL['icon_fiktL_v_obs'].addFile(u"img/Fiktivne/Fikt_obsL_vyb.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictFiktL['icon_fiktL_vlak'].addFile(u"img/Fiktivne/Fikt_vlakL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktL['icon_fiktL_posun'].addFile(u"img/Fiktivne/Fikt_posunL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktL['icon_fiktL_ochr'].addFile(u"img/Fiktivne/Fikt_ochrL.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictFiktL['icon_fiktL_zaver_stavanie'].addFile(u"img/Fiktivne/Fikt_stavL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktL['icon_fiktL_zaver_vc'].addFile(u"img/Fiktivne/Fikt_vcL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktL['icon_fiktL_rusenie_cesty'].addFile(u"img/Fiktivne/Fikt_zrusL.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictFiktL['icon_fiktL_zaver_vc_v'].addFile(u"img/Fiktivne/Fikt_vlakL_vyb.bmp", QSize(), QIcon.Normal, QIcon.Off)
    
    #------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------Fiktívne pravé návestidlo-----------------------------------------------------------

    dictFiktP['icon_fiktP'].addFile(u"img/Fiktivne/Fikt_volnoP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktP['icon_fiktP_obs'].addFile(u"img/Fiktivne/Fikt_obsP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktP['icon_fiktP_mrtve'].addFile(u"img/Fiktivne/Fikt_mrtveP.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictFiktP['icon_fiktP_v'].addFile(u"img/Fiktivne/Fikt_volnoP_vyb.bmp", QSize(), QIcon.Normal, QIcon.Off)    
    dictFiktP['icon_fiktP_v_obs'].addFile(u"img/Fiktivne/Fikt_obsL_vyb.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictFiktP['icon_fiktP_vlak'].addFile(u"img/Fiktivne/Fikt_vlakP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktP['icon_fiktP_posun'].addFile(u"img/Fiktivne/Fikt_posunP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktP['icon_fiktP_ochr'].addFile(u"img/Fiktivne/Fikt_ochrP.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictFiktP['icon_fiktP_zaver_stavanie'].addFile(u"img/Fiktivne/Fikt_stavP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktP['icon_fiktP_zaver_vc'].addFile(u"img/Fiktivne/Fikt_vcP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictFiktP['icon_fiktP_rusenie_cesty'].addFile(u"img/Fiktivne/Fikt_zrusP.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictFiktP['icon_fiktP_zaver_vc_v'].addFile(u"img/Fiktivne/Fikt_vlakP_vyb.bmp", QSize(), QIcon.Normal, QIcon.Off)   

def priecestie():
    dictPriecestie['icon_priec_otvorene'].addFile(u"img/Priecestie/Priec_otvorene.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictPriecestie['icon_priec_otvorene_v'].addFile(u"img/Priecestie/Priec_otvorene_vyber.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictPriecestie['icon_priec_predzv'].addFile(u"img/Priecestie/Priec_predzvananie.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictPriecestie['icon_priec_zatvorene'].addFile(u"img/Priecestie/Priec_zatvorene.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictPriecestie['icon_priec_zatvorene_v'].addFile(u"img/Priecestie/Priec_zatvorene_vyber.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictPriecestie['icon_priec_zatvorene_o'].addFile(u"img/Priecestie/Priec_zatvorene_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictPriecestie['icon_priec_zatvorene_v_o'].addFile(u"img/Priecestie/Priec_zatvorene_vyber_obs.bmp", QSize(), QIcon.Normal, QIcon.Off)

def tratSuhlas():
    dictTrSP['icon_TS_prijemP'].addFile(u"img/TS/TS_prijemP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSP['icon_TS_prijemP_volnost'].addFile(u"img/TS/TS_prijemP_volnost.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSP['icon_TS_prijemP_ziadost'].addFile(u"img/TS/TS_prijemP_ziada.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSP['icon_TS_udelenieP'].addFile(u"img/TS/TS_udelenieP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSP['icon_TS_udelenieP_volnost'].addFile(u"img/TS/TS_udelenieP_volnost.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSP['icon_TS_udelenieP_ziadost'].addFile(u"img/TS/TS_udelenieP_ziada.bmp", QSize(), QIcon.Normal, QIcon.Off)
    
    dictTrSL['icon_TS_prijemL'].addFile(u"img/TS/TS_prijemL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSL['icon_TS_prijemL_volnost'].addFile(u"img/TS/TS_prijemL_volnost.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSL['icon_TS_prijemL_ziadost'].addFile(u"img/TS/TS_prijemL_ziada.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSL['icon_TS_udelenieL'].addFile(u"img/TS/TS_udelenieL.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSL['icon_TS_udelenieL_volnost'].addFile(u"img/TS/TS_udelenieL_volnost.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSL['icon_TS_udelenieL_ziadost'].addFile(u"img/TS/TS_udelenieL_ziada.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSL['icon_TS_prijemL_porBP'].addFile(u"img/TS/TS_prijemL_poruchaBP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSL['icon_TS_prijemL_volnost_porBP'].addFile(u"img/TS/TS_prijemL_volnost_poruchaBP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSL['icon_TS_udelenieL_porBP'].addFile(u"img/TS/TS_udelenieL_poruchaBP.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictTrSL['icon_TS_udelenieL_volnost_porBP'].addFile(u"img/TS/TS_udelenieL_volnost_poruchaBP.bmp", QSize(), QIcon.Normal, QIcon.Off)

def riadenie():
    dictRiadenieRAD['icon_riadRAD_dialkove'].addFile(u"img/Stanice/RAD_dialkove.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictRiadenieRAD['icon_riadRAD_dialkove_ziadost'].addFile(u"img/Stanice/RAD_ziad_miestne.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictRiadenieRAD['icon_riadRAD_misetne'].addFile(u"img/Stanice/RAD_miestne.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictRiadenieRAD['icon_riadRAD_miestne_ziadost'].addFile(u"img/Stanice/RAD_ziad_dialkove.bmp", QSize(), QIcon.Normal, QIcon.Off)

    dictRiadenieZBE['icon_riadZBE_dialkove'].addFile(u"img/Stanice/ZBE_dialkove.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictRiadenieZBE['icon_riadZBE_dialkove_ziadost'].addFile(u"img/Stanice/ZBE_ziad_miestne.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictRiadenieZBE['icon_riadZBE_misetne'].addFile(u"img/Stanice/ZBE_miestne.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictRiadenieZBE['icon_riadZBE_miestne_ziadost'].addFile(u"img/Stanice/ZBE_ziad_dialkove.bmp", QSize(), QIcon.Normal, QIcon.Off)
    
    dictRiadenieHLO['icon_riadHLO_dialkove'].addFile(u"img/Stanice/HLO_dialkove.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictRiadenieHLO['icon_riadHLO_dialkove_ziadost'].addFile(u"img/Stanice/HLO_ziad_miestne.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictRiadenieHLO['icon_riadHLO_misetne'].addFile(u"img/Stanice/HLO_miestne.bmp", QSize(), QIcon.Normal, QIcon.Off)
    dictRiadenieHLO['icon_riadHLO_miestne_ziadost'].addFile(u"img/Stanice/HLO_ziad_dialkove.bmp", QSize(), QIcon.Normal, QIcon.Off)

def ostatneElementy():
    icon_ASVC_vypnute.addFile(u"img/Stanice/ASVC_vypnute.bmp", QSize(), QIcon.Normal, QIcon.Off)   