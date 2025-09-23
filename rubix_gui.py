from tkinter import *
from cube_data import Cube

class CubeNet:
    def __init__(self):
        # cube data values
        self.cube = Cube()

        # frequently accessed values
        self.face_abbr = ("u", "l", "f", "r", "b", "d")
        self.letters_to_colour = {
            "W": "white",
            "O": "orange",
            "G": "green",
            "R": "red",
            "B": "blue",
            "Y": "yellow"
        }

        # GUI
        self.main_window = Tk()
        self.main_window.title("Rubix Cube Simulator")


        cube_net_frame = Frame(self.main_window)
        cube_net_frame.pack()

        self.face_frames = {}
        grid_count = 0
        for face in self.face_abbr:
            self.face_frames[face] = Frame(cube_net_frame)
            if face in ("l", "f", "r", "b"):
                self.face_frames[face].grid(row = 1, column = grid_count)
                grid_count += 1
        self.face_frames["u"].grid(row = 0, column = 1)
        self.face_frames["d"].grid(row = 2, column = 1)

        self.face_tiles = {}
        for face in self.face_abbr:
            self.face_tiles[face] = [[Label(self.face_frames[face], width = 5, height = 2, font=("Calibri Bold", 12)) for _ in range(3)] for _  in range(3)]
            for row in range(3):
                for column in range(3):
                    self.face_tiles[face][row][column].grid(row = row, column = column)

        self.update_faces()

        self.button_frame = Frame(self.main_window)
        self.button_frame.pack()

        for column, face in enumerate(self.face_abbr):
            print(face)
            Button(self.button_frame, font = ("Calibri Bold", 12), text = face.upper(), width = 7, height = 2, command = lambda current_face = face: self.turn_side(current_face, prime = False)).grid(row=0, column= column, padx = 10, pady = 10)
            Button(self.button_frame, font=("Calibri Bold", 12), text=f"{face.upper()}'", width=7, height=2, command=lambda current_face = face: self.turn_side(current_face, prime=True)).grid(row=1, column=column, padx=10, pady=10)

        #Button(self.button_frame, font = ("Calibri Bold", 12), text = "U",width = 7, height = 2, command = lambda: self.turn_side("u")).grid(row = 0, column=0, padx = 10, pady = 10)
        #Button(self.button_frame, font=("Calibri Bold", 12), text="U'", width=7, height=2, command=lambda: self.turn_side("u", True)).grid(row=1, column=0, padx=10, pady=10)
        #Button(self.button_frame, font = ("Calibri Bold", 12), text="F",width = 7, height = 2, command=lambda: self.turn_side("f")).grid(row = 0, column=1, padx = 10, pady = 10)
        #Button(self.button_frame, font = ("Calibri Bold", 12), text="R",width = 7, height = 2, command=lambda: self.turn_side("r")).grid(row = 0, column=2, padx = 10, pady = 10)
        #Button(self.button_frame, font=("Calibri Bold", 12), text="R'", width=7, height=2, command=lambda: self.turn_side("r", True)).grid(row=1, column=2, padx=10, pady=10)


    def update_faces(self):
        for face in self.face_abbr:
            for row in range(3):
                for column in range(3):
                    colour_letter = getattr(self.cube, f"{face}_face")[row][column]
                    self.face_tiles[face][row][column].config(text = colour_letter, bg = self.letters_to_colour[colour_letter])

    def turn_side(self, face, prime = False):
        direction = "ac" if prime else "c"
        if face == "u":
            self.cube.u_turn(direction= direction)
        elif face == "l":
            self.cube.l_turn(direction= direction)
        elif face == "f":
            self.cube.f_turn(direction = direction)
        elif face == "r":
            self.cube.r_turn(direction= direction)
        elif face == "b":
            self.cube.b_turn(direction= direction)
        elif face == "d":
            print("turning d side")
            self.cube.d_turn(direction= direction)

        self.update_faces()

cube_net = CubeNet()

mainloop()