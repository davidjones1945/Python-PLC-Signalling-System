class RiseEdge: #trieda detektora nábežnej hrany signálu
    def __init__(self):
        self.previous = True

    def detect(self, val):
        edge = val and not (self.previous)
        self.previous = val

        return edge