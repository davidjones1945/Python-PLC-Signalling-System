class FallEdge: #trieda detektora nábežnej hrany signálu
    def __init__(self):
        self.previous = False

    def detect(self, val):
        edge = (not val) and self.previous
        self.previous = val

        return edge