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

    def u_turn(self, direction = "c"):
        self.rotate_face("u", direction)
        f_row = self.f_face[0]
        r_row = self.r_face[0]
        b_row = self.b_face[0]
        l_row = self.l_face[0]

        new_rows = (r_row, b_row, l_row, f_row) if direction == "c" else (l_row, f_row, r_row, b_row)
        self.f_face[0], self.r_face[0], self.b_face[0], self.l_face[0] = new_rows

        #if direction == "c":
        #    self.f_face[0], self.r_face[0], self.b_face[0], self.l_face[0] = (r_row, b_row, l_row, f_row)
        #else:
        #    self.f_face[0], self.r_face[0], self.b_face[0], self.l_face[0] = (l_row, f_row, r_row, b_row)



cube = Cube()
print(cube.f_face)
cube.u_turn("ac")
print(cube.f_face)
cube.u_turn("c")
print(cube.f_face)