#!/usr/bin/python

from math import *
from tkinter import *

# Base class for Hexagon shape
class Hexagon:
    def __init__(self, parent, x, y, length, color, tags):
        self.parent = parent
        self.x = x
        self.y = y
        self.length = length
        self.color = color
        self.tags = tags
        self.draw_hex()

    def draw_hex(self):
        start_x = self.x
        start_y = self.y
        angle = 60
        coords = []

        for k in range(6):
            end_x = start_x + self.length * cos(radians(angle * k))
            end_y = start_y + self.length * sin(radians(angle * k))
            coords.append([start_x, start_y])
            start_x = end_x
            start_y = end_y

        self.parent.create_polygon(
            coords[0][0], coords[0][1],
            coords[1][0], coords[1][1],
            coords[2][0], coords[2][1],
            coords[3][0], coords[3][1],
            coords[4][0], coords[4][1],
            coords[5][0], coords[5][1],
            fill=self.color,
            outline="black",
            tags=self.tags
        )


class FrequencyReuse(Tk):

    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 650

    def __init__(self, cluster_size, i_val, j_val, edge_len=30):
        super().__init__()

        self.cluster_size = cluster_size
        self.i_val = i_val
        self.j_val = j_val
        self.edge_len = edge_len

        self.hexagons = []
        self.reuse_cells = []
        self.first_click = True

        self.canvas = Canvas(self,
                             width=self.CANVAS_WIDTH,
                             height=self.CANVAS_HEIGHT,
                             bg="#4dd0e1")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.call_back)

        self.title("Frequency Reuse Simulation")

        self.create_grid(16, 10)
        self.calculate_distances()

    def create_grid(self, cols, rows):
        size = self.edge_len

        for c in range(cols):
            offset = 0 if c % 2 == 0 else size * sqrt(3) / 2

            for r in range(rows):
                x = c * (size * 1.5) + 50
                y = (r * (size * sqrt(3))) + offset + 15
                hx = Hexagon(self.canvas, x, y, size, "#fafafa", f"{r},{c}")
                self.hexagons.append(hx)

    def calculate_distances(self):
        self.hex_radius = sqrt(3) / 2 * self.edge_len
        self.center_dist = sqrt(3) * self.hex_radius

    def call_back(self, event):
        selected_id = self.canvas.find_closest(event.x, event.y)[0]
        hexagon = self.hexagons[selected_id - 1]

        if self.first_click:
            self.first_click = False
            self.selected_hex = hexagon
            self.canvas.itemconfigure(hexagon.tags, fill="green")
            self.calculate_reuse_cells(hexagon)

        else:
            if selected_id in self.reuse_cells:
                self.canvas.itemconfigure(hexagon.tags, fill="green")
                print("Correct Co-Channel Cell")
            else:
                self.canvas.itemconfigure(hexagon.tags, fill="red")
                print("Not a Co-Channel Cell")

    def calculate_reuse_cells(self, hexagon):
        sx, sy = hexagon.x + 15, hexagon.y + 25
        angle = 330

        for _ in range(6):
            end_x = sx + self.center_dist * self.i_val * cos(radians(angle))
            end_y = sy + self.center_dist * self.i_val * sin(radians(angle))

            reuse_x = end_x + self.center_dist * self.j_val * cos(radians(angle - 60))
            reuse_y = end_y + self.center_dist * self.j_val * sin(radians(angle - 60))

            cell = self.canvas.find_closest(reuse_x, reuse_y)[0]
            self.reuse_cells.append(cell)

            angle -= 60


if __name__ == "__main__":

    print("Common (i, j) values: (1,0), (1,1), (2,0), (2,1), (3,0), (2,2)")

    i = int(input("Enter i: "))
    j = int(input("Enter j: "))

    if i == 0 and j == 0:
        raise ValueError("i & j cannot both be zero")

    if j > i:
        raise ValueError("j cannot be greater than i")

    N = i*i + i*j + j*j
    print("Cluster size N =", N)

    app = FrequencyReuse(cluster_size=N, i_val=i, j_val=j)
    app.mainloop()
