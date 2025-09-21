class Face:
    def __init__(self, colour, surrounding_faces, numbers_to_be_moved):
        self.tiles = [f"{colour}{i}" for i in range(8)]
        self.surrounding_faces = surrounding_faces
        self.numbers_to_be_moved = numbers_to_be_moved

    def clockwise_spin(self):
        self.tiles = self.tiles[6:8] + self.tiles[0:6]

    def anticlockwise_spin(self):
        self.tiles = self.tiles[2:8] + self.tiles[0:2]

class Cube:
    def __init__(self):
        for colour in ("white", "orange", "green", "red", "blue", "yellow"):
            setattr(self, colour, Face(colour[0]))

        self.faces = {
            "w": Face("w", ("b", "r", "g", "o"), ((2,1,0), (2,1,0), (2,1,0), (2,1,0))),
            "o": Face("o", ("w", "g", "y", "b"), ((0,7,6), (0,7,6), ())),
            "g": Face("g"),
            "r": Face("r"),
            "b": Face("b"),
            "y": Face("y")
        }

    def r(self):
        self.red.clockwise_spin()
        other_edges = (self.white.tiles[2:5], self.blue.tiles[6:8] + [self.blue.tiles[0]], )