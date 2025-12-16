from PySide6.QtCore import QThread, Signal,QTimer

class DlhyCasVlak(QThread): #dlhý časový súbor pre vlakovú cestu
    finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        while not self.isInterruptionRequested():
            self.sleep(1)   #nenkonečná slučka vlákna

    def start_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.stop_timer)
        self.timer.start(180000) #3 minúty

    def stop_timer(self):
        self.timer.stop()
        self.finished.emit()

class DlhyCasPosun(QThread): #dlhý časový súbor pre posunovú cestu
    finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        while not self.isInterruptionRequested():
            self.sleep(1)   #nenkonečná slučka vlákna

    def start_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.stop_timer)
        self.timer.start(60000) #1 minúta

    def stop_timer(self):
        self.timer.stop()
        self.finished.emit()

class CasOchrDr(QThread): #časový súbor pre ochrannú dráhu
    finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        while not self.isInterruptionRequested():
            self.sleep(1)   #nenkonečná slučka vlákna

    def start_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.stop_timer)
        self.timer.start(30000) #30 sekúnd
        
    def stop_timer(self):
        self.timer.stop()
        self.finished.emit()

class LifeSign(QThread): #LifeSign aplikácie
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance

    def run(self):
        while not self.isInterruptionRequested():
            self.app_instance.prikazDoPLC(adresat='cas')
            self.sleep(5)   #5 sekúnd

