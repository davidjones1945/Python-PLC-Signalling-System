class Priecestie:
    def __init__(self, ID:int, nazovGUI:str, enumIkon, dictIkon, app):
        self.app = app  #inštancia spolupracujúcej triedy
        self.ID = ID    #ID úseku s priecestím

        self.nazovGUI = nazovGUI    #názov priecestia v GUI

        self.enumIkon = enumIkon    #prepojenie so symbolmi
        self.dictIkon = dictIkon

        self.predzvananie:bool = False   #plynie predzváňací čas priecestia
        self.otvorene:bool = False   #otvorené priecestie
        self.zatvorene:bool = False  #zatvorené priecestie

        self.jeVolny:bool = False    #informácia o obsadenosti úseku s priecestím

        self.vyber:bool = False  #informácia o výbere priecestia užívateľom

    def update(self):
        if self.jeVolny: #ak je úsek voľný    
            if self.otvorene: #ak je priecestie otvorené
                if self.vyber:  #ak je vybrané užívateľom
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.OTVORENE_VYBER.value])

                else:   #základný obraz otvoreného priecestia
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.OTVORENE.value])

            elif self.zatvorene:    #ak je priecestie zatvorené
                if self.vyber:  #ak je vybrané užívateľom
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZATVORENE_VYBER.value])

                else:   #základný obraz zatvoreného priecestia
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZATVORENE.value])

            elif self.predzvananie: #ak plynie predzváňací čas
                getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.PREDZVANANIE.value])

        else:   #ak je úsek obsadený   
            if self.zatvorene:  #ak je priecestie zatvorené
                if self.vyber:  #ak je vybrané užívateľom
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZATVORENE_VYBER_OBS.value])

                else:   #základný obraz zatvoreného priecestia
                    getattr(self.app.ui, self.nazovGUI).setIcon(self.dictIkon[self.enumIkon.ZATVORENE_OBS.value])
    