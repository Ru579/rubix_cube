from tkinter import *
from cube_data import Cube

class CubeNet:
    def __init__(self):
        # cube data values
        self.cube = Cube()


        # frequently accessed values
        self.face_abbr = ("u", "l", "f", "r", "b", "d")
        self.letters_to_colour = {
            "w": "white",
            "o": "orange",
            "g": "green",
            "r": "red",
            "b": "blue",
            "y": "yellow"
        }

        # GUI
        self.main_window = Tk()
        self.main_window.title("Rubix Cube Simulator")

        self.cube_net_frame = Frame(self.main_window, width = 1200)
        self.cube_net_frame.pack()

        self.face_frames = {}
        grid_count = 0
        for face in self.face_abbr:
            self.face_frames[face] = Frame(self.cube_net_frame)
            if face in ("l", "f", "r", "b"):
                self.face_frames[face].grid(row = 1, column = grid_count)
                grid_count += 1
        self.face_frames["u"].grid(row = 0, column = 1)
        self.face_frames["d"].grid(row = 2, column = 1)


        #self.f_face = Frame(self.cube_net_frame)
        #self.b_face = Frame(self.cube_net_frame)
        #self.u_face = Frame(self.cube_net_frame)
        #self.d_face = Frame(self.cube_net_frame)
        #self.r_face = Frame(self.cube_net_frame)
        #self.l_face = Frame(self.cube_net_frame)
        #for frame in (self.f_face, self.b_face, self.u_face, self.d_face, self.r_face, self.l_face):
        #    frame.pack()


        self.face_tiles = {}
        for face in self.face_abbr:
            self.face_tiles[face] = [[[Label(self.face_frames[face], width = 50, height = 50) for _ in range(3)] for _  in range(3)]]

        #self.face_tiles = {
        #    "f": [[Label(self.f_face, width = 50, height = 50) for _ in range(3)] for _  in range(3)],
        #    "b": [],
        #    "u": [],
        #    "d": [],
        #    "r": [],
        #    "l": []
        #}

    def update_faces(self):
        for face in self.face_abbr:
            for row in range(3):
                for column in range(3):
                    self.face_tiles[row][column].config(bg = self.letters_to_colour[getattr(self.cube, f"{face}_face")[row][column]])

cube_net = CubeNet()

mainloop()