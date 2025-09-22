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
            new_face = list(zip(*getattr(self, f"{face}_face")[::-1]))
            for row_number, row in enumerate(new_face):
                new_face[row_number] = list(row)
            # setattr(self, f"{face}_face", list(zip(*getattr(self, f"{face}_face")[::-1])))
            setattr(self, f"{face}_face", new_face)

        elif direction == "ac":
            new_face = list(zip(*getattr(self, f"{face}_face")))[::-1]
            for row_number, row in enumerate(new_face):
                new_face[row_number] = list(row)
            #setattr(self, f"{face}_face", list(zip(*getattr(self, f"{face}_face")))[::-1])
        else:
            new_face = []
        setattr(self, f"{face}_face", new_face)

    def f_turn(self, direction = "c"):
        self.rotate_face("f", direction)
        u_row = self.u_face[2].copy()
        print(u_row)
        r_col = [self.r_face[i][0] for i in range(3)]
        print(r_col)
        d_row = self.d_face[0].copy()
        print(d_row)
        l_col = [self.l_face[i][2] for i in range(3)]
        print(l_col)

        if direction == "c":
            for i in range(3):
                self.u_face[2][i] = l_col[2-i]
                self.r_face[i][0] = u_row[i]
                self.d_face[0][i] = r_col[2-i]
                self.l_face[i][2] = d_row[i]
        elif direction == "ac":
            for i in range(3):
                self.u_face[2][i] = r_col[i]
                self.r_face[i][0] = d_row[2-i]
                self.d_face[0][i] = l_col[i]
                self.l_face[i][2] = u_row[2-i]

        print(self.u_face)
        print(self.r_face)
        print(self.d_face)
        print(self.l_face)

    def b_turn(self, direction = "c"):
        self.rotate_face("b", direction)
        u_row = self.u_face[0]
        r_col = [self.r_face[i][2] for i in range(3)]
        d_row = self.d_face[2]
        l_col = [self.l_face[i][0] for i in range(3)]

        if direction == "c":
            for i in range(3):
                self.u_face[0][i] = r_col[i]
                self.r_face[i][2] = d_row[2-i]
                self.d_face[2][i] = l_col[i]
                self.l_face[i][0] = u_row[2-i]
        elif direction == "ac":
            for i in range(3):
                self.u_face[0][i] = l_col[2-i]
                self.r_face[i][2] = u_row[i]
                self.d_face[2][i] = r_col[2-i]
                self.l_face[i][0] = d_row[i]

    def u_turn(self, direction = "c"):
        self.rotate_face("u", direction)
        f_row = self.f_face[0]
        r_row = self.r_face[0]
        b_row = self.b_face[0]
        l_row = self.l_face[0]

        new_rows = (r_row, b_row, l_row, f_row) if direction == "c" else (l_row, f_row, r_row, b_row)
        self.f_face[0], self.r_face[0], self.b_face[0], self.l_face[0] = new_rows

    def d_turn(self, direction = "c"):
        self.rotate_face("d", direction)
        f_row = self.f_face[2]
        r_row = self.r_face[2]
        b_row = self.b_face[2]
        l_row = self.l_face[2]

        new_rows = (l_row, f_row, r_row, b_row) if direction == "c" else (r_row, b_row, l_row, f_row)
        self.f_face[0], self.r_face[0], self.b_face[0], self.l_face[0] = new_rows

    def r_turn(self, direction = "c"):
        self.rotate_face("r", direction)
        f_col = [self.f_face[i][2] for i in range(3)]
        u_col = [self.u_face[i][2] for i in range(3)]
        b_col = [self.b_face[i][0] for i in range(2,-1,-1)]
        d_col = [self.d_face[i][2] for i in range(3)]

        if direction == "c":
            for i in range(3):
                self.f_face[i][2] = d_col[i]
                self.u_face[i][2] = f_col[i]
                self.b_face[i][0] = u_col[2-i]
                self.d_face[i][2] = b_col[i]
        elif direction == "ac":
            for i in range(3):
                self.f_face[i][2] = u_col[i]
                self.u_face[i][2] = b_col[i]
                self.b_face[i][0] = d_col[2-i]
                self.d_face[i][2] = f_col[i]

    def l_turn(self, direction = "c"):
        self.rotate_face("l", direction)
        f_col = [self.f_face[i][0] for i in range(3)]
        u_col = [self.u_face[i][0] for i in range(3)]
        b_col = [self.b_face[i][2] for i in range(2, -1, -1)]
        d_col = [self.d_face[i][0] for i in range(3)]

        if direction == "c":
            for i in range(3):
                self.f_face[i][0] = u_col[i]
                self.u_face[i][0] = b_col[i]
                self.b_face[i][2] = d_col[2-i]
                self.d_face[i][0] = f_col[i]
        elif direction == "ac":
            for i in range(3):
                self.f_face[i][0] = d_col[i]
                self.u_face[i][0] = f_col[i]
                self.b_face[i][2] = u_col[2 - i]
                self.d_face[i][0] = b_col[i]




#cube = Cube()
#print(cube.f_face)
#cube.u_turn("ac")
#print(cube.f_face)
#cube.u_turn("c")
#print(cube.f_face)
#
#cube.r_turn()
#print(cube.f_face)
#cube.r_turn("ac")
#cube.r_turn("ac")
#print(cube.f_face)

#when rotating face, for tuple in 2d list, tuple = list(tuple)