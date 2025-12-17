from PySide6.QtCore import QThread, Signal
import arrow

class Datum(QThread): #Čas a dátum pre aplikáciu
    dataUpdated = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while not self.isInterruptionRequested():
            cas = arrow.now().format('  DD.MM.YY HH:mm:ss')
            self.sleep(1)   #1 sekunda
            self.dataUpdated.emit(cas)