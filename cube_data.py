class Face:
    def __init__(self, colour):
        self.tiles = [f"{colour}{i}" for i in range(8)]

    def clockwise_spin(self):
        self.tiles = self.tiles[6:8] + self.tiles[0:6]

    def anticlockwise_spin(self):
        self.tiles = self.tiles[2:8] + self.tiles[0:2]

class Cube:
    def __init__(self):
        for colour in ("white", "orange", "green", "red", "blue", "yellow"):
            setattr(self, colour, Face(colour[0]))

        self.white = Face("w")
        self.orange = Face("o")
        self.green = Face("g")
        self.red = Face("r")
        self.blue = Face("b")
        self.yellow = Face("y")

    def r(self):
        self.red.clockwise_spin()
        other_edges = (self.white.tiles[2:5], self.blue.tiles[6:8] + [self.blue.tiles[0]], )