#class Face:
#    def __init__(self, colour, surrounding_faces, numbers_to_be_moved):
#        self.tiles = [f"{colour}{i}" for i in range(8)]
#        self.surrounding_faces = surrounding_faces
#        self.numbers_to_be_moved = numbers_to_be_moved
#
#    def clockwise_spin(self):
#        self.tiles = self.tiles[6:8] + self.tiles[0:6]
#
#    def anticlockwise_spin(self):
#        self.tiles = self.tiles[2:8] + self.tiles[0:2]
#
#class Cube:
#    def __init__(self):
#        self.faces = {
#            "w": Face("w", ("b", "r", "g", "o"), ((2,1,0), (2,1,0), (2,1,0), (2,1,0))),
#            "o": Face("o", ("w", "g", "y", "b"), ((0,7,6), (0,7,6), (0,7,6), (4,3,2))),
#            "g": Face("g", ("w", "r", "y", "o"), ((6,5,4), (0,7,6), (2,1,0), (4,3,2))),
#            "r": Face("r", ("w", "b", "y", "g"), ((4,3,2), (0,7,6), (4,3,2), (4,3,2))),
#            "b": Face("b", ("w", "o", "y", "r"), ((2,1,0), (0,7,6), (6,5,4), (4,3,2))),
#            "y": Face("y", ("g", "r", "b", "o"), ((6,5,4), (6,5,4), (6,5,4), (6,5,4)))
#        }
#
#    def turn_side(self, colour_of_side_turning):
#        self.faces[colour_of_side_turning].clockwise_spin()
#        face_copies = [self.faces[colour_of_side_turning].numbers_to_be_moved[0]]
#        for i in range(3):
#            face_copies.append(self.faces[colour_of_side_turning].surrounding_faces[i+1][self.faces[colour_of_side_turning[]]])


class Cube:
    def __init__(self):
        self.f_face, self.b_face, self.u_face, self.d_face, self.r_face, self.l_face = [],[],[],[],[],[]

        colours = ("G", "B", "W", "Y", "R", "O")
        for side_number, side in enumerate(("f", "b", "u", "d", "r" ,"l")):
            setattr(self, f"{side}_face", [[colours[side_number] for _ in range(3)] for _ in range(3)])

        # testing purposes
        #for side in ("f", "b", "u", "d", "r" ,"l"):
        #    setattr(self, f"{side}_face", [[0,1,2], [3,4,5], [6,7,8]])

    def rotate_face(self, face, direction):
        if direction == "c":
            setattr(self, f"{face}_face", list(zip(*getattr(self, f"{face}_face")[::-1])))
        elif direction == "ac":
            setattr(self, f"{face}_face", list(zip(*getattr(self, f"{face}_face")))[::-1])

    def u_turn(self):



cube = Cube()
print(cube.f_face)
cube.rotate_face("f", "ac")
print(cube.f_face)
cube.rotate_face("f", "ac")
print(cube.f_face)
