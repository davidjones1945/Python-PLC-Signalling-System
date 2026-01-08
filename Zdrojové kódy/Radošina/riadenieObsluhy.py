class RiadenieObsluhy:
    def __init__(self, ID, nazovGUI, enumIkon, dictIkon, app):
        self.app = app #inštancia spolupracujúcej triedy
        self.ID = ID #ID stanice

        self.nazovGUI = nazovGUI #názov objektu riadenia v GUI

        self.enumIkon = enumIkon #prepojenie so symbolmi
        self.dictIkon = dictIkon

        self.ziadost = False #žiadosť o prebranie kontroly
        self.dialkove = True    #aktuálne udelený súhlas na riadenie (True - diaľkové, False - lokálne)

        self.vyber = False #informácia o výbere priecestia užívateľom

    def update(self, app):
        if self.dialkove: #diaľkové ovládanie stanice
            if self.ziadost: #ak je aktívna žiadosť o lokálnu obsluhu
                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.DIALKOVE_ZIADOST.value])
            
            else:   #základný obraz
                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.DIALKOVE.value])
        
        else:   #lokálne ovládanie stanice
            if self.ziadost:  #ak je aktívna žiadosť o lokálnu obsluhu
                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.MIESTNE_ZIADOST.value])
            
            else: #základný obraz
                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.MIESTNE.value])