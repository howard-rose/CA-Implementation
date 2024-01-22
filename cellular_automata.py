from cell import *
import copy

class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = []

        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(Cell(False))
            self.cells.append(row)

    def step(self):
        new_cells = copy.deepcopy(self.cells)

        for r in range(self.rows):
            for c in range(self.cols):
                new_cells[r][c].step(self.get_neighbors(r, c))

        self.cells = new_cells

    def get_neighbors(self, r, c):
        neighbors = []

        x_offsets = (-1, -1, -1, 0, 0, 1, 1, 1)
        y_offsets = (-1, 0, 1, -1, 1, -1, 0, 1)

        for x, y in zip(x_offsets, y_offsets):
            if self.within_bounds(r + y, c + x):
                neighbors.append(self.cells[r + y][c + x])

        return neighbors

    def within_bounds(self, r, c):
        return -1 < r < self.rows and -1 < c < self.cols
